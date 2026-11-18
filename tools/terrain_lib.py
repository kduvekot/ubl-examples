"""The world's terrain, made from its geology (O152): the kernels and the steps of tools/terrain.py.

Needs numpy, scipy and numba (pip install numpy scipy numba); only tools/terrain.py imports this module, and only
when it generates. The site build and the world model read the committed outputs (world/terrain.json and
world/terrain/*.png), which need none of these.

Method (see tools/terrain.py for the outputs):
  * geology first: a coast from the earlier outline, smoothed and roughened inside D19's box; regional relief from
    control points; the main basin tilting towards the rift from a divide all round; the volcanic massif of the
    north-west; the rift (graben) with its floor, escarpments and shoulders; the drowned estuary at Lumeport. On
    Lisavu: an old shield-stratovolcano with a caldera, a young cone, a lava plain, a windward coast cut back by the
    sea and by giant landslides, with fajãs, stacks and valleys with amphitheatre heads;
  * climate: an orographic rain model under the westerlies (rain from forced ascent, rain shadows in the lee);
  * a stream-power landscape calibrated to the geology (Braun & Willett 2013, Cordonnier et al. 2016): the
    drainage network and its valleys come from the steady state of uplift and fluvial incision (priority-flood
    depression filling, Barnes et al. 2014; D8 flow; rain-weighted flow accumulation), the uplift is tuned so that
    the low-passed heights match the geology;
  * land cover from height, slope, rain and the height above the nearest stream;
  * aggregation to the 3.5 km squares of the world model: kind, corner heights in metres, the main river and the
    estuary; the countries, with the land border along the high ground north of the crossing.
Everything is deterministic: every noise has its own seed.
"""
import heapq
import math

import numpy as np
from numba import njit
from scipy import ndimage
from scipy.spatial import cKDTree

KM = 3.5
SEA, WATER, FIELD, FOREST, GRASS, HEATH, ROCK, MARSH = range(8)
KIND = "swdfghrm"                                   # tile kinds by class: sea, water, field, forest, grass, heath, rock, marsh

# ------------------------------------------------------------------------------------------- kernels (numba)
DR = np.array([-1, -1, -1, 0, 0, 1, 1, 1], dtype=np.int64)
DC = np.array([-1, 0, 1, -1, 1, -1, 0, 1], dtype=np.int64)
DD = np.array([1.41421356, 1.0, 1.41421356, 1.0, 1.0, 1.41421356, 1.0, 1.41421356])


@njit
def priority_flood(z, outlet, eps):
    """Fill depressions (priority-flood + epsilon): every land cell gets a descending path to an outlet."""
    ny, nx = z.shape
    out = z.copy()
    done = np.zeros((ny, nx), dtype=np.bool_)
    heap = [(0.0, 0, 0)]
    heap.pop()
    for r in range(ny):
        for c in range(nx):
            if outlet[r, c]:
                done[r, c] = True
                seed = r == 0 or c == 0 or r == ny - 1 or c == nx - 1
                if not seed:
                    for k in range(8):
                        rr = r + DR[k]; cc = c + DC[k]
                        if 0 <= rr < ny and 0 <= cc < nx and not outlet[rr, cc]:
                            seed = True
                            break
                if seed:
                    heapq.heappush(heap, (out[r, c], r, c))
    while len(heap) > 0:
        h, r, c = heapq.heappop(heap)
        for k in range(8):
            rr = r + DR[k]; cc = c + DC[k]
            if 0 <= rr < ny and 0 <= cc < nx and not done[rr, cc]:
                done[rr, cc] = True
                if out[rr, cc] <= h + eps:
                    out[rr, cc] = h + eps
                heapq.heappush(heap, (out[rr, cc], rr, cc))
    return out


@njit
def receivers(z, outlet, cell):
    """D8 steepest-descent receiver of every cell (itself for outlets); distance in m."""
    ny, nx = z.shape
    rec = np.empty(ny * nx, dtype=np.int64)
    dist = np.ones(ny * nx)
    for r in range(ny):
        for c in range(nx):
            i = r * nx + c
            rec[i] = i
            if outlet[r, c]:
                continue
            best = 0.0
            for k in range(8):
                rr = r + DR[k]; cc = c + DC[k]
                if 0 <= rr < ny and 0 <= cc < nx:
                    s = (z[r, c] - z[rr, cc]) / (DD[k] * cell)
                    if s > best:
                        best = s
                        rec[i] = rr * nx + cc
                        dist[i] = DD[k] * cell
    return rec, dist


@njit
def accumulate(order, rec, w):
    """Flow accumulation; order = cell indices by descending height."""
    a = w.copy()
    for t in range(order.size):
        i = order[t]
        j = rec[i]
        if j != i:
            a[j] += a[i]
    return a


@njit
def steady_heights(order_asc, rec, dist, area, u, a0, smax, base):
    """Steady-state stream-power heights (n = 1): each cell above its receiver by u * sqrt(a0 / A) * distance,
    the slope capped at smax (the hillslope threshold)."""
    z = base.copy()
    for t in range(order_asc.size):
        i = order_asc[t]
        j = rec[i]
        if j == i:
            continue
        s = u[i] * np.sqrt(a0 / area[i])
        if s > smax[i]:
            s = smax[i]
        z[i] = z[j] + s * dist[i]
    return z


RR16 = np.array([-1, -1, -1, 0, 0, 1, 1, 1, -2, -2, -1, -1, 1, 1, 2, 2], dtype=np.int64)
CC16 = np.array([-1, 0, 1, -1, 1, -1, 0, 1, -1, 1, -2, 2, -2, 2, -1, 1], dtype=np.int64)


@njit
def least_cost(cost_cell, passable, start):
    """Dijkstra over the cells (16 directions): the cost of a step is its length times the mean cost of its cells."""
    ny, nx = cost_cell.shape
    INF = 1e30
    cost = np.full(ny * nx, INF)
    prev = np.full(ny * nx, -1, dtype=np.int64)
    s0 = start[0] * nx + start[1]
    cost[s0] = 0.0
    heap = [(0.0, s0)]
    while len(heap) > 0:
        cst, i = heapq.heappop(heap)
        if cst > cost[i]:
            continue
        r = i // nx; c = i % nx
        for k in range(16):
            rr = r + RR16[k]; cc = c + CC16[k]
            if rr < 0 or cc < 0 or rr >= ny or cc >= nx or not passable[rr, cc]:
                continue
            e = np.sqrt(RR16[k] ** 2 + CC16[k] ** 2) * 0.5 * (cost_cell[r, c] + cost_cell[rr, cc])
            j = rr * nx + cc
            if cst + e < cost[j]:
                cost[j] = cst + e
                prev[j] = i
                heapq.heappush(heap, (cost[j], j))
    return cost, prev


# ------------------------------------------------------------------------------------------- fields
def fbm(shape, scales_cells, amps, seed):
    """Value-noise fBm: a sum of bicubic-upsampled random grids at the given feature sizes (cells)."""
    rng = np.random.default_rng(seed)
    out = np.zeros(shape)
    for sc, a in zip(scales_cells, amps):
        gy = max(2, int(np.ceil(shape[0] / sc)) + 3)
        gx = max(2, int(np.ceil(shape[1] / sc)) + 3)
        g = rng.standard_normal((gy, gx))
        z = ndimage.zoom(g, sc, order=3)
        oy = rng.integers(0, sc); ox = rng.integers(0, sc)
        out += a * z[oy:oy + shape[0], ox:ox + shape[1]]
    return out


def smoothstep(x):
    x = np.clip(x, 0, 1)
    return x * x * (3 - 2 * x)


def polyline_field(pts, X, Y, key_vals=None, step=0.05):
    """Distance (squares) from each cell to the polyline, the along-path distance of the nearest point, the
    cumulative length at the vertices, and per-vertex values interpolated along the path."""
    pts = np.asarray(pts, float)
    seg = np.diff(pts, axis=0)
    segl = np.hypot(seg[:, 0], seg[:, 1])
    cum = np.concatenate([[0], np.cumsum(segl)])
    dense, s_dense = [], []
    for a in range(len(seg)):
        n = max(2, int(segl[a] / step))
        tt = np.linspace(0, 1, n, endpoint=False)
        dense.append(pts[a] + tt[:, None] * seg[a])
        s_dense.append(cum[a] + tt * segl[a])
    dense.append(pts[-1:]); s_dense.append([cum[-1]])
    dense = np.vstack(dense); s_dense = np.concatenate(s_dense)
    d, idx = cKDTree(dense).query(np.c_[X.ravel(), Y.ravel()])
    s = s_dense[idx].reshape(X.shape)
    d = d.reshape(X.shape)
    vals = None
    if key_vals is not None:
        vals = [np.interp(s, cum, np.asarray(kv, float)) for kv in key_vals]
    return d, s, cum, vals


def gauss_points(points, X, Y, spread):
    num = np.zeros(X.shape); den = np.zeros(X.shape)
    for (px, py, m) in points:
        w = np.exp(-((X - px) ** 2 + (Y - py) ** 2) / (2 * spread ** 2)) + 1e-12
        num += w * m; den += w
    return num / den


def angle_noise(theta, seed, terms=((1, 0.5), (2, 0.35), (3, 0.25), (5, 0.18), (8, 0.12), (13, 0.08), (21, 0.05))):
    """Smooth periodic noise of an angle (radii that vary round a volcano)."""
    r = np.random.default_rng(seed)
    out = np.zeros_like(theta)
    for k, a in terms:
        out += a * np.sin(k * theta + r.uniform(0, 2 * np.pi))
    return out


def polygon_mask(poly, X0, Y0, S, shape):
    """Cells inside a polygon (squares), by the even-odd rule at the cell centres."""
    ny, nx = shape
    Xc = X0 + (np.arange(nx) + 0.5) / S
    inside = np.zeros(shape, bool)
    P = np.asarray(poly, float)
    for r in range(ny):
        y = Y0 + (r + 0.5) / S
        xs = []
        for (ax, ay), (bx, by) in zip(P, np.roll(P, -1, axis=0)):
            if (ay <= y < by) or (by <= y < ay):
                xs.append(ax + (y - ay) * (bx - ax) / (by - ay))
        xs.sort()
        for a, b in zip(xs[0::2], xs[1::2]):
            inside[r] |= (Xc >= a) & (Xc < b)
    return inside


def orographic_rain(z, sea, cell, wet=1.0):
    """Moisture carried by a westerly wind (+x), row by row: rain from a base rate plus forced ascent; the air
    dries as it rains and takes moisture up again over the sea. Returns mm a year."""
    ny, nx = z.shape
    zs = ndimage.gaussian_filter(np.maximum(z, 0), 3)
    rain = np.zeros_like(z)
    q = np.ones(ny) * wet
    for c in range(nx):
        up = np.maximum(0, (zs[:, c] - zs[:, max(c - 1, 0)]) / cell) if c else np.zeros(ny)
        r = q * (0.0035 + 0.3 * np.minimum(up, 0.3)) * (cell / 875.0)
        r = np.where(sea[:, c], q * 0.002, r)
        rain[:, c] = r
        q = q - 0.55 * r
        q = np.where(sea[:, c], q + (1 - q) * 0.03 * (cell / 875.0), q)
        q = np.clip(q, 0.05, 1)
    rain = ndimage.gaussian_filter(rain, 4 * 875.0 / cell)
    return 350 + rain / (0.0035 * (cell / 875.0)) * 520 + 0.35 * np.maximum(z, 0)


def landscape(target, sea, rain_mm, cell, iters, smax, seed, sig=4.0, keep=None, guide_iters=6, log=None):
    """Stream-power landscape calibrated to a geological target: the steady state of uplift and incision,
    the uplift tuned so that the low-passed heights match the target. keep: an upper bound (the carved trunk
    river). The first guide_iters iterations route the water over the smoothed geology."""
    rng = np.random.default_rng(seed)
    a0 = cell * cell
    w = a0 * np.clip(rain_mm / 1000.0, 0.3, 4)
    land = ~sea
    tl = ndimage.gaussian_filter(np.where(land, np.maximum(target, 1), 0), sig)
    norm = ndimage.gaussian_filter(land.astype(float), sig) + 1e-6
    tl = tl / norm
    gy, gx = np.gradient(ndimage.gaussian_filter(target, 2), cell)
    u = np.clip(np.hypot(gx, gy), 0.003, 0.5) + 0.01
    z = target.copy()
    guide = ndimage.gaussian_filter(target, 6)
    if keep is not None:
        guide = np.minimum(guide, keep)
    base = np.where(sea, target, 0.0).ravel()
    for it in range(iters):
        jitter = (fbm(z.shape, [24, 10, 4], [1.0, 0.6, 0.3], 1000 + it) * 4.0 + rng.standard_normal(z.shape) * 0.5) \
            * (1.0 + 0.01 * np.abs(z))
        wg = max(0.0, 1.0 - it / guide_iters) if guide_iters else 0.0
        zroute = wg * guide + (1 - wg) * z
        zf = priority_flood(zroute + jitter, sea, 1e-3)
        rec, dist = receivers(zf, sea, cell)
        order = np.argsort(zf.ravel(), kind='stable')
        area = accumulate(order[::-1], rec, w.ravel())
        zn = steady_heights(order, rec, dist, area, u.ravel(), a0 * 0.6, smax.ravel(), base).reshape(z.shape)
        zl = ndimage.gaussian_filter(np.where(land, zn, 0), sig) / norm
        u = np.clip(u * np.clip(tl / np.maximum(zl, 1), 0.5, 2.0) ** 0.8, 2.5e-3, 3)
        z = np.where(land, zn, target)
        if keep is not None:
            z = np.minimum(z, keep)
        if log:
            log(f'  landscape step {it}: mean |lowpass - target| {np.abs(zl - tl)[land].mean():.0f} m')
    return z


def route(z, sea, cell, rain_mm, seed=999):
    """Final flow routing over a slightly perturbed surface (no straight parallel channels on flats)."""
    zr = z + np.where(sea, 0, fbm(z.shape, [16, 6], [1.0, 0.5], seed) * 1.5)
    zf = priority_flood(zr, sea, 1e-3)
    rec, dist = receivers(zf, sea, cell)
    order = np.argsort(-zf.ravel(), kind='stable')
    akm2 = accumulate(order, rec, np.full(z.size, cell * cell / 1e6))
    return zf, rec.reshape(z.shape), akm2.reshape(z.shape)


def upstream_stem(rec, area, mouth_rc, min_area):
    """Hack's main stem upwards from a mouth: always the donor with the largest catchment."""
    ny, nx = area.shape
    a = area.ravel(); r = rec.ravel()
    donors = {}
    for idx in np.where(r != np.arange(r.size))[0]:
        donors.setdefault(int(r[idx]), []).append(int(idx))
    i = mouth_rc[0] * nx + mouth_rc[1]
    path = [i]
    while i in donors:
        d = max(donors[i], key=lambda q: a[q])
        if a[d] < min_area:
            break
        i = d; path.append(i)
    return np.array([(p // nx, p % nx) for p in path[::-1]])


def grid(win, S):
    X0, X1, Y0, Y1 = win
    ny, nx = (Y1 - Y0) * S, (X1 - X0) * S
    X, Y = np.meshgrid(X0 + (np.arange(nx) + 0.5) / S, Y0 + (np.arange(ny) + 0.5) / S)
    return X, Y, ny, nx


# ------------------------------------------------------------------------------------------- the mainland
def mainland(inp, log=print):
    m = inp["mainland"]
    S = m["cells_per_square"]
    cell = KM * 1000 / S
    X0, X1, Y0, Y1 = m["window"]
    X, Y, ny, nx = grid(m["window"], S)
    # --- the coast: the earlier outline, smoothed, displaced and roughened, inside D19's box
    land_t = np.zeros((256 if Y1 <= 256 else Y1, X1))
    land_t = np.zeros((max(Y1, 192), max(X1, 192)))
    for j, runs in enumerate(m["outline"]):
        for a, b in runs:
            land_t[j, a:b] = 1
    land_c = np.kron(land_t[Y0:Y1, X0:X1], np.ones((S, S)))
    L = ndimage.gaussian_filter(land_c, 2.0 * S)
    wx = fbm((ny, nx), [200, 100, 50, 25, 12], [9, 10, 8, 5, 2.5], 12)
    wy = fbm((ny, nx), [200, 100, 50, 25, 12], [9, 10, 8, 5, 2.5], 13)
    rr, cc = np.mgrid[0:ny, 0:nx]
    L = ndimage.map_coordinates(L, [rr + wy, cc + wx], order=1, mode='nearest')
    noise_coast = fbm((ny, nx), [64, 32, 16, 8, 4], [0.13, 0.11, 0.08, 0.05, 0.025], 11)
    s = L - 0.5 + noise_coast
    bx0, bx1, by0, by1 = m["box"]
    box = (np.minimum.reduce([X - bx0, bx1 - X, Y - by0, by1 - Y]) + 0.3 + fbm((ny, nx), [40, 16, 6], [1.2, 0.7, 0.35], 14)) / 2.0
    s = np.minimum(s, box)
    for (ix, iy, r_) in m["islets"]:
        s = np.maximum(s, 0.25 * (1 - np.hypot(X - ix, Y - iy) / r_) + 0.04 * noise_coast / 0.13)
    s = np.where(np.minimum.reduce([X - bx0 + 2.7, bx1 + 2.3 - X, Y - by0 + 2.7, by1 + 2.8 - Y]) < 0, np.minimum(s, -0.1), s)
    # --- the river's axis
    ax = m["river_axis"]
    axis = [tuple(p) for p in ax["points"]]
    floor_m, half_w = ax["floor_m"], ax["half_width"]
    jit = fbm((ny, nx), [40, 16], [0.6, 0.3], 5)
    d, sa, cum, (F, HW, EW, ES) = polyline_field(axis, X, Y, [floor_m, half_w, ax["escarpment"], ax["estuary"]])
    A = np.asarray(axis, float)
    dense = []
    for a in range(len(A) - 1):
        for t in np.linspace(0, 1, 40, endpoint=False):
            dense.append(A[a] + t * (A[a + 1] - A[a]))
    dense.append(A[-1]); dense = np.array(dense)
    tang = np.gradient(dense, axis=0); tang /= np.hypot(tang[:, 0], tang[:, 1])[:, None]
    nrm = np.c_[-tang[:, 1], tang[:, 0]]
    sl = np.concatenate([[0], np.cumsum(np.hypot(*np.diff(dense, axis=0).T))])
    hw_d = np.interp(sl, np.concatenate([[0], np.cumsum(np.hypot(*np.diff(A, axis=0).T))]), half_w)
    amp = np.clip(hw_d - 0.8, 0, 1.4)
    off = amp * (0.7 * np.sin(sl / 3.1) + 0.3 * np.sin(sl / 1.3 + 1.0))
    dm, _, _, _ = polyline_field(dense + nrm * off[:, None], X, Y)
    d_raw = d
    d = np.abs(d + jit * np.clip(HW / 2.6, 0, 1))
    s = np.where(ES > 0.05, np.minimum(s, (d_raw - ES) / 1.2 * 0.5 + 0.03 * noise_coast / 0.1), s)
    sea = s < 0
    lab, n = ndimage.label(~sea)
    sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
    sea = ~np.isin(lab, 1 + np.where(sizes >= 2)[0])
    dcoast = ndimage.distance_transform_edt(~sea) * cell / 1000
    dsea = ndimage.distance_transform_edt(sea) * cell / 1000
    # --- regional relief, the Upland edge
    Ereg = gauss_points(m["relief_points"], X, Y, m["relief_spread"])
    ue = m["upland_edge"]
    de, _, _, _ = polyline_field(ue["line"], X, Y)
    ly = [p[1] for p in ue["line"]]; lx = [p[0] for p in ue["line"]]
    side = np.sign(X - np.interp(Y, ly, lx))
    Ereg = Ereg + np.where(side < 0, ue["step_m"], -ue["step_m"]) * smoothstep(de / 2.0)
    # --- the main basin tilts towards the rift
    divide = m["basin_divide"]["points"]
    basin = polygon_mask([(x, y) for x, y, _ in divide], X0, Y0, S, (ny, nx))
    ddiv, _, _, (Hdiv,) = polyline_field([(x, y) for x, y, _ in divide], X, Y, [[h for _, _, h in divide]])
    ddiv = np.maximum(ddiv + fbm((ny, nx), [60, 24], [1.5, 0.7], 71) * np.clip(ddiv / 3, 0, 1), 0)
    self_F = np.interp(sa, cum, floor_m)
    t = d / (d + ddiv + 1e-6)
    Ebowl = self_F + (Hdiv - self_F) * t ** 0.7
    Eout = np.minimum(Ereg, Hdiv - 45 * ddiv ** 0.8)
    Ereg = np.where(basin, 0.95 * Ebowl + 0.05 * Ereg, np.maximum(Eout, 0.25 * Ereg))
    # --- the volcanic massif
    massif = np.zeros_like(X)
    for (cx, cy, hm, R) in m["cones"]["cones"]:
        r = np.hypot(X - cx, Y - cy) / R
        massif = np.maximum(massif, hm * np.clip(1 - r, 0, 1) ** 1.7)
    kx, ky, kd, kr = m["cones"]["caldera"]
    massif -= kd * np.exp(-(np.hypot(X - kx, Y - ky) / kr) ** 2)
    massif_w = np.clip(massif / 900, 0, 1)
    E = np.maximum(Ereg, massif + Ereg * 0.35)
    # --- the rift
    shoulder = Ereg + 40 * np.exp(-((d - HW - EW) / 4.0) ** 2) * (HW > 1)
    shoulder = np.where(HW > 1, np.maximum(shoulder, F + 90), shoulder)
    E_out = np.maximum(E, shoulder)
    E_out = np.where(massif > 50, np.maximum(E, F + 60), E_out)
    Ev = F + (E_out - F) * smoothstep((d - HW) / EW)
    E = np.where(d < HW + EW, Ev, E_out)
    # --- detail
    rough = 70 + 260 * massif_w + 160 * np.clip((E - 200) / 500, 0, 1)
    rough = rough * (1 - 0.85 * np.clip(1 - (d - HW) / 0.6, 0, 1) * (HW > 1))
    n1 = fbm((ny, nx), [48, 24, 12, 6, 3], [1, 0.6, 0.4, 0.22, 0.12], 21)
    ridged = 1 - np.abs(fbm((ny, nx), [32, 16, 8, 4], [1, 0.5, 0.3, 0.15], 22))
    E = E + rough * (0.6 * n1 * np.where(basin, 0.6, 1.0) + 0.5 * massif_w * (ridged - 0.6))
    # --- the coast: plains ramp to the sea, cliffs on the volcanic west
    wc = m["west_cliffs"]
    west_cliff = smoothstep((wc["x0"] - X) / 12) * smoothstep((Y - wc["y0"]) / 6) * smoothstep((wc["y1"] - Y) / 6)
    ramp_km = 9 * (1 - west_cliff) + 0.9 * west_cliff + 6 * smoothstep((60 - Y) / 10) * (1 - west_cliff)
    E = np.maximum(E, 2)
    E = 1.5 + (E - 1.5) * (0.06 * west_cliff + (1 - 0.06 * west_cliff) * smoothstep(dcoast / ramp_km))
    E[sea] = -8 - 9 * dsea[sea] ** 0.9
    estuary = sea & (ES > 0) & (d < ES + 1.5)
    E[estuary] = np.maximum(-25, E[estuary])
    E = np.where((d < HW) & ~sea, E + 0.006 * dm * 3500 + 2.0 * n1, E)
    z0 = E.copy()
    # --- climate and landscape
    rain = orographic_rain(z0, sea, cell)
    smax = 0.08 + 0.22 * massif_w + 0.25 * np.clip((z0 - 300) / 600, 0, 1) + 0.9 * west_cliff * (dcoast < 2)
    carve = np.where(HW > 1, F + 0.006 * dm * 3500 + 25 * smoothstep((d - HW) / 0.3) + 60 * np.clip((d - HW) / 0.8, 0, 1),
                     F + 0.07 * d * 3500)
    zone = np.where(HW > 1, d < HW + 0.8, d < 2.5) & (ES <= 0) & ~sea
    z = landscape(z0, sea, rain, cell, 14, smax, 7, keep=np.where(zone, carve, 1e9), log=log)
    z = np.where(sea, z, np.maximum(z, 1.0))
    hi = z > 1200
    z[hi] = 1200 + 800 * (1 - np.exp(-(z[hi] - 1200) / 800))
    z, rec, akm2 = route(z, sea, cell, rain)
    mx, my = ax["mouth_near"]
    near = (~sea) & ndimage.binary_dilation(sea, structure=np.ones((3, 3), bool)) & (np.hypot(X - mx, Y - my) < 5)
    mouth = np.unravel_index(np.argmax(np.where(near, akm2, 0)), akm2.shape)
    stem = upstream_stem(rec, akm2, mouth, 0.5)
    return dict(z=z, sea=sea, rain=rain, rec=rec, akm2=akm2, stem=stem, X=X, Y=Y, S=S, X0=X0, Y0=Y0, cell=cell,
                estuary=estuary, west=west_cliff)


# ------------------------------------------------------------------------------------------- Lisavu
def lisavu(inp, log=print):
    m = inp["lisavu"]
    S = m["cells_per_square"]
    cell = KM * 1000 / S
    Xg, Yg, ny, nx = grid(m["window"], S)
    X0, _, Y0, _ = m["window"]
    rng = np.random.default_rng(1974)
    X = Xg + fbm((ny, nx), [96, 48, 24, 12], [1.1, 0.8, 0.45, 0.2], 91)
    Y = Yg + fbm((ny, nx), [96, 48, 24, 12], [1.1, 0.8, 0.45, 0.2], 92)
    oc = m["old_centre"]
    C1 = np.array(oc["at"])
    dx, dy = X - C1[0], Y - C1[1]
    ang = np.radians(oc["turn_deg"])
    u_ = dx * np.cos(ang) - dy * np.sin(ang)
    v_ = dx * np.sin(ang) + dy * np.cos(ang)
    theta1 = np.arctan2(v_, u_)
    Rx = np.where(u_ < 0, oc["radius_west"], oc["radius_east"]) * (1 + 0.10 * angle_noise(theta1, 1))
    Ry = oc["radius_ns"] * (1 + 0.12 * angle_noise(theta1, 2))
    r1 = np.sqrt((u_ / Rx) ** 2 + (v_ / Ry) ** 2)
    E1 = oc["height_m"] * np.clip(1 - r1, 0, 1) ** 1.25 + 120 * np.clip(1 - r1, 0, 1)
    for (px, py, h, rr) in oc["vents"]:
        E1 += h * np.exp(-((X - px) ** 2 + (Y - py) ** 2) / (2 * rr ** 2)) * smoothstep((1 - r1) / 0.4)
    yc = m["young_cone"]
    (cx2, cy2) = yc["at"]
    r2 = np.hypot(X - cx2, (Y - cy2) * 1.2) / (yc["radius"] * (1 + 0.15 * angle_noise(np.arctan2(Y - cy2 - 1, X - cx2 - .5), 3)))
    E2 = yc["height_m"] * np.clip(1 - r2, 0, 1) ** 1.5
    lp = m["lava_plain"]
    (cx3, cy3), (ra3, rb3) = lp["at"], lp["radius"]
    r3 = np.hypot((X - cx3) / ra3, (Y - cy3) / rb3) * (1 + 0.15 * angle_noise(np.arctan2(Y - 105.5, X - 238.5), 4))
    E3 = lp["height_m"] * np.clip(1 - r3, 0, 1) ** 0.5
    E = np.maximum.reduce([E1, E2, E3]) + 0.25 * np.minimum.reduce([E1, E2, E3])
    # the caldera, breached to the west-south-west
    ca = m["caldera"]
    cal = np.array(ca["at"])
    rc = np.hypot(X - cal[0], (Y - cal[1]) * 1.1) * (1 + 0.18 * angle_noise(np.arctan2(Y - cal[1], X - cal[0]), 9))
    bowl = smoothstep(1.05 - rc / ca["radius"])
    E = E - bowl * (ca["depth_m"] + 90 * (X - cal[0]) - 40 * (Y - cal[1])) \
        + 60 * np.exp(-((rc - ca["radius"] - .2) / 0.6) ** 2) * (1 + fbm((ny, nx), [10, 5], [0.8, 0.4], 94))
    # the windward coast: marine retreat and landslide scars
    th = np.arctan2(Y - C1[1], X - C1[0])
    west = np.clip(np.cos(th - np.pi), 0, 1) ** 0.8 * smoothstep((228 - X) / 6)
    ret = m["cliff_retreat"] + 0.9 * angle_noise(th, 11, ((3, 0.4), (5, 0.35), (8, 0.3))) \
        + fbm((ny, nx), [40, 20, 10, 5], [0.7, 0.5, 0.3, 0.15], 93)
    dist1 = np.hypot((X - C1[0]), (Y - C1[1]) * 0.62)
    scar = np.zeros_like(X)
    for sx, sy, rad in m["landslides"]:
        scar = np.maximum(scar, smoothstep(1.15 - np.hypot(X - sx, Y - sy) / rad))
    E = E * (1 - 0.82 * scar) + 60 * scar
    # the outline
    n_c = fbm((ny, nx), [80, 40, 20, 10, 5], [60, 45, 30, 18, 9], 77)
    land = (E + n_c - 70 > 0) & (E > 25)
    land &= ~((west > 0.15) & (dist1 > ret))
    b = m["bay"]
    row = (np.abs(Yg - b["row"]) < 0.3) & land
    BAY = (Xg[row].max() - 1.1, b["row"])
    bay = np.hypot(Xg - BAY[0], (Yg - BAY[1]) * 1.25) < b["radius"] + 0.2 * fbm((ny, nx), [16, 8], [0.6, 0.3], 79)
    bay |= (np.abs(Yg - b["row"] - 0.1 - 0.15 * (Xg - BAY[0])) < 0.45) & (Xg > BAY[0])
    land &= ~bay
    for (cx, cy, rr) in m["coves"]:
        land &= ~(np.hypot(Xg - cx, Yg - cy) < rr * (1 + 0.3 * fbm((ny, nx), [12, 6], [0.6, 0.3], int(cx * 10))))
    faja = np.zeros_like(land)
    for fx, fy, fr in m["fajas"]:
        faja |= np.hypot(X - fx, (Y - fy) * 0.8) < fr * (1 + 0.25 * fbm((ny, nx), [10, 5], [0.6, 0.3], int(fx * 7)))
    land |= faja
    stk = np.zeros_like(land)
    for sx, sy, sr in m["stacks"]:
        stk |= np.hypot(X - sx, Y - sy) < sr
    land |= stk
    lab, n = ndimage.label(land)
    sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
    land = np.isin(lab, 1 + np.where(sizes >= 2)[0])
    seal, _ = ndimage.label(~land)
    land |= seal != seal[0, 0]
    sea = ~land
    dcoast = ndimage.distance_transform_edt(land) * cell / 1000
    dsea = ndimage.distance_transform_edt(sea) * cell / 1000
    # windward valleys with amphitheatre heads
    keep = np.full(X.shape, 1e9)
    for (mo, hd, hf, ar) in m["valleys"]["list"]:
        mid = (np.array(mo) + np.array(hd)) / 2 + rng.normal(0, 0.35, 2)
        dv, sv, cumv, _ = polyline_field([tuple(mo), tuple(mid), tuple(hd)], X, Y)
        fl = 4 + (hf - 4) * (sv / cumv[-1]) ** 1.6
        wall = 0.55 + 0.25 * fbm((ny, nx), [20, 8], [0.6, 0.3], int(hf))
        carve = fl + wall * np.maximum(dv - 0.12, 0) * 3500
        dh = np.hypot(X - hd[0], Y - hd[1])
        arr = ar * (1 + 0.28 * angle_noise(np.arctan2(Y - hd[1], X - hd[0]), int(hf) + 5))
        carve = np.minimum(carve, hf + 0.05 * dh * 3500 + 25 * fbm((ny, nx), [10, 5], [0.7, 0.4], int(hf) + 6)
                           + 0.9 * np.maximum(dh - arr, 0) * 3500)
        keep = np.minimum(keep, np.where(dv < 2.2, carve, 1e9))
        E = np.minimum(E, np.where(dv < 2.2, carve, 1e9))
    # detail, coasts, cliffs
    ridged = 1 - np.abs(fbm((ny, nx), [40, 20, 10, 5], [1, 0.5, 0.3, 0.15], 81))
    n1 = fbm((ny, nx), [48, 24, 12, 6], [1, 0.6, 0.35, 0.2], 82)
    plain = smoothstep(1 - r3) * (E3 >= np.maximum(E1, E2))
    E = E + (25 + 0.12 * np.maximum(E, 0)) * (0.8 * n1 + 0.3 * (ridged - 0.6) * smoothstep(E / 800)) * (1 - 0.85 * plain)
    E = E * (1 - m["cliff_lowering"] * west * (1 - smoothstep(dcoast / 3.5)))
    ramp_km = 0.35 * west + 3.5 * (1 - west)
    E = np.maximum(E, 3)
    E = 2 + (E - 2) * (0.1 * west + (1 - 0.1 * west) * smoothstep(dcoast / ramp_km))
    E = np.where(faja, 8 + 25 * smoothstep(dcoast / 0.6) + 6 * n1, E)
    E = np.where(stk, 60 + 80 * smoothstep(dcoast / 0.25), E)
    E[sea] = -10 - 30 * dsea[sea]
    bsh = bay & sea & (dsea < 3)
    E[bsh] = np.maximum(-30, E[bsh])
    lobes = fbm((ny, nx), [28, 14, 7], [1.0, 0.6, 0.3], 95)
    E = np.where(land, E + 70 * lobes * smoothstep(E / 300) * (1 - west), E)
    z0 = E.copy()
    rain = orographic_rain(z0, sea, cell, wet=1.0)
    smax = (0.18 + 0.35 * np.clip(z0 / 1200, 0, 1)) * np.exp(0.7 * fbm((ny, nx), [40, 16, 6], [0.7, 0.4, 0.2], 83)) \
        + 2.0 * west * (dcoast < 0.9) + 1.5 * (keep < 1e8) * np.clip(z0 / 600, 0, 1)
    keep = np.where(land, keep, 1e9)
    z = landscape(z0, sea, rain, cell, 10, smax, 85, sig=3.0, keep=keep, guide_iters=0, log=log)
    z = np.where(sea, z, np.maximum(z, 1.0))
    cliffband = land & (west > 0.3) & (dcoast < 0.5) & ~faja & ~stk
    z = np.where(cliffband, np.maximum(z, 0.85 * z0), z)
    hi = z > 1250
    z[hi] = 1250 + 600 * (1 - np.exp(-(z[hi] - 1250) / 600))
    z, rec, akm2 = route(z, sea, cell, rain)
    return dict(z=z, sea=sea, rain=rain, rec=rec, akm2=akm2, X=Xg, Y=Yg, S=S, X0=X0, Y0=Y0, cell=cell,
                west=west, faja=faja, stacks=stk, bay=bay, estuary=np.zeros_like(sea))


# ------------------------------------------------------------------------------------------- land cover
def hand(z, rec, akm2, thr):
    """Height above the nearest drainage (a channel of at least thr km2)."""
    order = np.argsort(z.ravel(), kind='stable')
    r = rec.ravel(); zr = z.ravel(); ch = (akm2.ravel() >= thr)
    cz = np.empty(z.size)
    for i in order:
        cz[i] = zr[i] if (ch[i] or r[i] == i) else cz[r[i]]
    return (zr - cz).reshape(z.shape)


def cover(d, island=False):
    """Land cover per cell, from height, slope, rain and the height above the nearest stream."""
    z, sea, rain, akm2, rec = d['z'], d['sea'], d['rain'], d['akm2'], d['rec']
    cell = d['cell']; X, Y = d['X'], d['Y']
    gy, gx = np.gradient(z, cell)
    slope = ndimage.gaussian_filter(np.hypot(gx, gy), 1.0)
    h = hand(z, rec, akm2, 20.0)
    ny, nx = z.shape
    n1 = fbm((ny, nx), [24, 12, 6], [1, 0.6, 0.3], 51 + island)
    n2 = fbm((ny, nx), [16, 8, 4], [1, 0.5, 0.3], 61 + island)
    lc = np.full(z.shape, GRASS)
    near_sea = ndimage.distance_transform_edt(~sea) * cell / 1000
    lc[(slope < 0.055 + 0.025 * n1) & (z < 700) & ((h < 90) | (slope < 0.03)) & (rain > 540)] = FIELD
    forest = (slope > 0.13 + 0.03 * n2) | ((rain > 1300) & (slope > 0.05) & (z > 150)) \
        | ((slope > 0.08) & (n2 > 0.45)) | ((n2 > 1.1) & (slope > 0.03))
    lc[forest & (z < 1500)] = FOREST
    lc[(z > 1300 + 80 * n1) | ((rain < 620) & (slope > 0.07)) | ((z > 1050) & (slope < 0.12) & (n1 > 0.3))] = HEATH
    lc[(z > 1650 + 60 * n1) | (slope > 0.55) | ((z > 1450) & (slope > 0.3))] = ROCK
    lc[(z < 5 + 3 * n1) & (h < 3) & (slope < 0.012) & (near_sea < 7)] = MARSH
    lc[sea] = SEA
    if island:
        lc[(rain > 1500) & ~sea & (z < 1350) & (lc != ROCK)] = FOREST
        lee = (rain < 1150) & ~sea & np.isin(lc, [FOREST, GRASS])
        wood = (n2 > 0.2) & (rain > 950)
        lc[lee & wood] = FOREST
        rest = lee & ~wood
        lc[rest] = GRASS
        lc[rest & (rain < 820) & (slope >= 0.12) & (n1 > -0.2)] = HEATH
        lc[~sea & (rain < 1150) & (slope < 0.06) & (z < 400) & (lc != MARSH)] = FIELD
        lc[(rain < 900) & ~sea & (slope < 0.07) & (z < 250) & (X > 226) & (Y < 112)] = FIELD    # the cotton plain
    return lc


# ------------------------------------------------------------------------------------------- tiles
def tiles(d, lc, W=256, H=192):
    """Per 3.5 km square of the window: the kind (the most common class of its land cells; sea where most of
    its cells are sea), and the corner heights (metres, the mean of the land cells round the corner; 0 where a
    sea square touches it). Returns kinds [H][W] (class numbers, -1 outside the window), corners [H+1][W+1]
    (nan outside)."""
    S = d['S']; X0, Y0 = d['X0'], d['Y0']
    z = d['z']; ny, nx = z.shape
    ty, tx = ny // S, nx // S
    blocks = lc.reshape(ty, S, tx, S).transpose(0, 2, 1, 3).reshape(ty, tx, S * S)
    kinds = np.full((H, W), -1)
    for a in range(ty):
        for b in range(tx):
            v = blocks[a, b]
            land = v != SEA
            if land.sum() * 2 < v.size:
                kinds[Y0 + a, X0 + b] = SEA
            else:
                kinds[Y0 + a, X0 + b] = np.argmax(np.bincount(v[land], minlength=8))
    zl = np.where(lc == SEA, np.nan, z)
    pad = np.pad(zl, S // 2, constant_values=np.nan)
    corners = np.full((H + 1, W + 1), np.nan)
    for a in range(ty + 1):
        for b in range(tx + 1):
            win = pad[a * S:a * S + S, b * S:b * S + S]
            corners[Y0 + a, X0 + b] = 0 if np.all(np.isnan(win)) else np.nanmean(win)
    return kinds, corners


def river_tiles(d, kinds):
    """The main river's squares, source to mouth, 4-connected (a diagonal step takes the square it cuts), and
    the water level of each (never rising downstream), until it reaches the sea."""
    X, Y, z, stem = d['X'], d['Y'], d['z'], d['stem']
    tl, lv = [], []
    for r, c in stem:
        t = (int(X[r, c]), int(Y[r, c]))
        if not tl or tl[-1] != t:
            if tl and abs(tl[-1][0] - t[0]) == 1 and abs(tl[-1][1] - t[1]) == 1:
                tl.append((t[0], tl[-1][1])); lv.append(z[r, c])
            tl.append(t); lv.append(z[r, c])
        else:
            lv[-1] = min(lv[-1], z[r, c])
    out, level = [], 1e9
    for (x, y), h in zip(tl, lv):
        if kinds[y, x] == SEA:
            break
        level = min(level, h)
        out.append((x, y, level))
    return out


def streams(d, min_km2, step=2):
    """The streams of at least min_km2 as polylines of [x, y, km2] (squares), every step-th cell, for the sheet."""
    rec = d['rec'].ravel(); a = d['akm2'].ravel(); sea = d['sea'].ravel()
    X, Y = d['X'].ravel(), d['Y'].ravel()
    ch = (a >= min_km2) & ~sea
    donors = np.zeros(a.size, int)
    for i in np.where(ch)[0]:
        if rec[i] != i:
            donors[rec[i]] += 1
    heads = [i for i in np.where(ch)[0] if donors[i] == 0]
    seen = np.zeros(a.size, bool)
    lines = []
    for h in heads:
        i = h; pts = [i]
        while True:
            j = rec[i]
            if j == i:
                break
            pts.append(j)
            if seen[j] or sea[j]:
                break
            seen[j] = True
            i = j
        keep = pts[::step] + ([pts[-1]] if (len(pts) - 1) % step else [])
        lines.append([[round(float(X[q]), 3), round(float(Y[q]), 3), int(a[q])] for q in keep])
    return lines


def border(d, inp, log=print):
    """The land border between Urvania and Bayvarra (owner, 2026-11-18, option A: the watershed). The main river
    is the border from the crossing, at the confluence of its largest plateau tributary, to the estuary: all land
    south of it is Urvania. North of the crossing the border follows the watershed: Urvania keeps the basins of
    every tributary that joins the main river at or upstream of the crossing (that tributary's whole valley
    included), and the coastal basins whose outlet lies at or west of a given column; the rest of the land north
    of the river is Bayvarra's. Returns a cell mask of Bayvarra's mainland, and the crossing (squares)."""
    b = inp["border"]
    z, sea, X, Y, S, X0, Y0 = d['z'], d['sea'], d['X'], d['Y'], d['S'], d['X0'], d['Y0']
    ny, nx = z.shape
    rec = d['rec'].ravel()
    seaf = sea.ravel()
    stem = d['stem']
    stem_idx = stem[:, 0] * nx + stem[:, 1]
    pos = np.full(rec.size, -1); pos[stem_idx] = np.arange(len(stem_idx))
    on_stem = pos >= 0
    # every cell's terminal: the last cell before the main river (a tributary's mouth) or before the sea (a
    # coastal outlet); pointer jumping along the receivers
    stop = on_stem | seaf | on_stem[rec] | seaf[rec] | (rec == np.arange(rec.size))
    nxt = np.where(stop, np.arange(rec.size), rec)
    for _ in range(40):
        nn = nxt[nxt]
        if np.array_equal(nn, nxt):
            break
        nxt = nn
    term = nxt
    def rc(p):
        return (int((p[1] - Y0) * S), int((p[0] - X0) * S))
    # the crossing tributary: the tributary mouth nearest the given point
    mouths = np.unique(term[~seaf & ~on_stem & on_stem[rec[term]]])
    r0, c0 = rc(b["crossing_tributary"])
    mr, mc = mouths // nx, mouths % nx
    t9 = mouths[np.argmin((mr - r0) ** 2 + (mc - c0) ** 2)]
    k9 = pos[rec[t9]]                                   # where it joins the main river
    trib = ~seaf & ~on_stem & on_stem[rec[term]]
    up = trib & (pos[rec[term]] <= k9)                  # tributaries joining at or upstream of the crossing
    coastal = ~seaf & ~on_stem & ~on_stem[rec[term]]
    west_coast = coastal & (X.ravel()[term] <= b["coastal_west_of_x"])
    xu_north = (up | west_coast | (on_stem & (pos <= k9))).reshape(ny, nx)
    river = np.zeros((ny, nx), bool)
    river[stem[:, 0], stem[:, 1]] = True
    river |= d['estuary']
    barrier = ndimage.binary_dilation(river, iterations=1) & ~sea | river | xu_north
    lab, n = ndimage.label(~sea & ~barrier)
    xb = np.zeros((ny, nx), bool)
    for sd in b["bayvarra_seeds"]:
        r, c = rc(sd)
        if lab[r, c] > 0:
            xb |= lab == lab[r, c]
    # what is left (islets, slivers cut off by the river's band) goes to the nearer country
    xu = xu_north.copy()
    xu[stem[:, 0], stem[:, 1]] = True
    for sd in b["urvania_seeds"]:
        r, c = rc(sd)
        if lab[r, c] > 0:
            xu |= lab == lab[r, c]
    rest = ~sea & ~xb & ~xu
    if rest.any():
        dxb = ndimage.distance_transform_edt(~xb)
        dxu = ndimage.distance_transform_edt(~xu)
        xb |= rest & (dxb < dxu)
    xb &= ~sea
    cr, cc = divmod(int(rec[t9]), nx)
    crossing = [round(float(X[cr, cc]), 2), round(float(Y[cr, cc]), 2)]
    log(f"border: crossing at the confluence {crossing}, the tributary's basin {int(((term == t9) & ~seaf).sum() * (d['cell'] / 1000) ** 2)} km2")
    return xb & ~sea, crossing
