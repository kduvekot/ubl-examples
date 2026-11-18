"""Top-down map of the UBL example world, refined from the 3D tile map (tools/world_model.py).

The 3D map has 256 x 192 squares of 3.5 km (world_model.GRID = 4 squares per 14 km). Level 0 is the model as it
is: every square shows its terrain (land, sea, river, forest, field, rock) and the ground has the model's height
("v", a height per square corner in levels of world_model.LEVEL_M metres). Every next level halves the 14 km
square and adds one finer octave of the model's own noise, which bends the edges between the squares' terrains
(the coast, the forest edges, the fields) into natural lines, so that every square keeps what the 3D map shows.
The relief is shaded, and the land tinted by height, from the model's height alone (the noise only adds a little
texture). Roads, rail, the river and the pipelines follow the model's own paths, with their corners cut (Chaikin);
towns, buildings and airports stay on their squares.

Usage (from the repository root): python3 tools/world_model.py model.json, then
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 6 roadmap   (road-map style)
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 2 strip     (the levels)
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 0 sheet     (A3, 1 : 2,500,000)
(the fifth argument is the number of pixels per 3.5 km square)
"""
import json, math, sys
import numpy as np
sys.path.insert(0, "tools")
import world_model as wm
from PIL import Image, ImageDraw, ImageFont, ImageFilter

model_path, map_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
LEVELS = int(sys.argv[4]) if len(sys.argv) > 4 else 5
PX = int(sys.argv[5]) if len(sys.argv) > 5 else 24
M = json.load(open(model_path))
T, ROUTES = M["model"]["tiles"], M["routes"]
WORLD = json.load(open(map_path))
W, H = wm.W, wm.H
G = wm.GRID                                       # squares per 14 km
KM = wm.KM                                        # km per square
C = wm.chart                                      # square -> chart units (14 km)

river = next(r for r in WORLD["routes"] if r["mode"] == "river")
V = np.array(M["model"]["v"], dtype=np.float32)    # corner heights in levels, [W + 1][H + 1]
LEVEL_M = M["model"].get("level_m", wm.LEVEL_M)
KIND = {"s": 0, "w": 1, "g": 2, "f": 3, "r": 4, "d": 5}
COUNTRY = {None: 0, "XU": 1, "XB": 2, "XL": 3}
K = np.array([[KIND[T[i][j]["k"]] if not T[i][j].get("es") else 0 for j in range(H)] for i in range(W)], dtype=np.int8)
CTY = np.array([[COUNTRY[T[i][j]["c"]] for j in range(H)] for i in range(W)], dtype=np.int8)

# ---------------------------------------------------------------- the model's noise, on arrays
def np_hsh(x, y):
    h = (x.astype(np.int64) * 374761393 + y.astype(np.int64) * 668265263) & 0xFFFFFFFF
    h = ((h ^ (h >> 13)) * 1274126177) & 0xFFFFFFFF
    return ((h ^ (h >> 16)) & 0xFFFFFFFF) / 4294967295

def np_smooth(x, y):
    xi, yi = np.floor(x), np.floor(y)
    xf, yf = x - xi, y - yi
    a, b, c, d = np_hsh(xi, yi), np_hsh(xi + 1, yi), np_hsh(xi, yi + 1), np_hsh(xi + 1, yi + 1)
    u, v = xf * xf * (3 - 2 * xf), yf * yf * (3 - 2 * yf)
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v

def detail(x, y, levels, seed=0.0):
    """The finer octaves added level by level (x, y in chart units of 14 km): each halves the square and the
    amplitude."""
    d, amp = np.zeros_like(x), 0.10
    for k in range(1, levels + 1):
        f = 2 ** k
        d += (np_smooth(x * f + 17.3 * k + seed, y * f - 9.1 * k - seed) - .5) * amp
        amp /= 2
    return d

def raster(levels, px, rows=None):
    """The terrain at px pixels per square: kind, country, height (metres) and hill shade (0..1, light from the
    north-west) per pixel. The kind and the country are the model's squares, looked up at a position the finer
    octaves bend by up to half a square; the height is the model's corner heights, interpolated, with a little
    texture."""
    w, h = W * px, H * px
    X = (np.arange(w, dtype=np.float32) + .5) / px - .5
    Y = (np.arange(h, dtype=np.float32) + .5) / px - .5
    xx, yy = np.meshgrid(X, Y, indexing="ij")                      # [w][h], in squares
    cx, cy = xx / G, yy / G                                         # chart units
    if levels:
        wx = detail(cx, cy, levels, 3.3) * 4.5 * G                  # about half a square at most
        wy = detail(cx, cy, levels, 8.1) * 4.5 * G
    else:
        wx = wy = 0
    ti = np.clip(np.rint(xx + wx), 0, W - 1).astype(np.int32)
    tj = np.clip(np.rint(yy + wy), 0, H - 1).astype(np.int32)
    kind, cty = K[ti, tj], CTY[ti, tj]
    vx, vy = np.clip(xx + .5, 0, W - 1e-3), np.clip(yy + .5, 0, H - 1e-3)
    i0, j0 = vx.astype(np.int32), vy.astype(np.int32)
    u, v = vx - i0, vy - j0
    elev = (V[i0, j0] * (1 - u) * (1 - v) + V[i0 + 1, j0] * u * (1 - v) + V[i0, j0 + 1] * (1 - u) * v
            + V[i0 + 1, j0 + 1] * u * v) * LEVEL_M
    if levels:
        elev = elev + detail(cx, cy, levels, 5.7) * (40 + elev * .15)
    elev = np.where(kind == 0, 0, np.maximum(elev, 0))
    # the model's heights come in whole levels: smooth the steps away (three box blurs of about half a square,
    # close to a Gaussian) before the hills are shaded
    r = max(1, int(px * .6))
    for _ in range(3):
        for ax in (0, 1):
            c = np.cumsum(np.pad(elev, [(r + 1, r) if a == ax else (0, 0) for a in (0, 1)], mode="edge"), axis=ax)
            elev = (np.take(c, range(2 * r + 1, c.shape[ax]), axis=ax) - np.take(c, range(0, c.shape[ax] - 2 * r - 1), axis=ax)) / (2 * r + 1)
    elev = np.where(kind == 0, 0, elev)
    m_per_px = KM * 1000 / px
    gx, gy = np.gradient(elev, m_per_px)
    exag = 6.0                                                      # vertical exaggeration of the shading
    nx, ny, nz = -gx * exag, -gy * exag, np.ones_like(gx)
    norm = np.sqrt(nx * nx + ny * ny + nz * nz)
    lx, ly, lz = -.5, -.5, .707                                     # light from the north-west, 45 degrees up
    shade = np.clip((nx * lx + ny * ly + nz * lz) / norm, 0, 1)
    return kind, cty, elev, shade

HYPSO = [(0, (232, 238, 222)), (150, (238, 238, 220)), (400, (236, 230, 208)), (700, (226, 214, 190)),
         (1000, (212, 202, 186)), (1300, (236, 234, 230))]

def tint(elev):
    """The land's colour by its height (hypsometric tint, light and soft as on a road map)."""
    out = np.zeros(elev.shape + (3,), dtype=np.float32)
    for (a, ca), (b, cb) in zip(HYPSO, HYPSO[1:]):
        u = np.clip((elev - a) / (b - a), 0, 1)[..., None]
        sel = ((elev >= a) & (elev < b)) | ((b == HYPSO[-1][0]) & (elev >= b))
        out = np.where(sel[..., None], np.array(ca) + (np.array(cb) - np.array(ca)) * u, out)
    return out

def colour(kind, cty, elev, shade, style):
    """Pixels of the terrain in the road-map style ("flat") or the stronger 3D style ("3d")."""
    land = kind != 0
    if style == "flat":
        img = tint(elev)
        for k, col, a in ((3, (190, 222, 180), .75), (5, (236, 234, 210), .8), (4, (214, 208, 198), .7)):
            sel = (kind == k)[..., None]
            img = np.where(sel, img * (1 - a) + np.array(col) * a, img)
        f = (1 + (shade - .707) * .9)[..., None]
        water = np.array((170, 211, 223), dtype=np.float32)
    else:
        img = np.zeros(kind.shape + (3,), dtype=np.float32)
        for k, col in ((2, (204, 220, 170)), (1, (204, 220, 170)), (3, (128, 171, 112)), (4, (196, 182, 150)), (5, (226, 214, 150))):
            img = np.where((kind == k)[..., None], np.array(col, dtype=np.float32), img)
        img = img * (1 - np.clip(elev / 1600, 0, .5))[..., None] + np.array((150, 130, 110)) * np.clip(elev / 1600, 0, .5)[..., None]
        for c, t in ((1, (0, 6, -6)), (2, (6, 2, -8)), (3, (10, 0, -10))):
            img = np.where((cty == c)[..., None], img + np.array(t), img)
        f = (1 + (shade - .707) * 1.4)[..., None]
        water = np.array((150, 190, 225), dtype=np.float32)
    img = np.where(land[..., None], np.clip(img * f, 0, 255), water)
    return Image.fromarray(np.transpose(img.astype(np.uint8), (1, 0, 2)), "RGB")

def render(levels, px):
    """Raster at px pixels per square in the 3D style; levels = how many times the 14 km square was halved."""
    return colour(*raster(levels, px), "3d")

def border_dots(img, px, levels, colour_, r):
    """The land border, dotted where the country changes between neighbouring pixels (not to the island)."""
    _, cty, _, _ = raster(levels, px)
    ok = (cty > 0) & (cty < 3)
    edge = np.zeros(cty.shape, bool)
    edge[1:, :] |= (cty[1:, :] != cty[:-1, :]) & ok[1:, :] & ok[:-1, :]
    edge[:, 1:] |= (cty[:, 1:] != cty[:, :-1]) & ok[:, 1:] & ok[:, :-1]
    q = max(2, int(px * G / 6))                                     # one dot per q x q pixels
    d = ImageDraw.Draw(img, "RGBA")
    done = set()
    for x, y in zip(*np.nonzero(edge)):
        cell = (x // q, y // q)
        if cell not in done:
            done.add(cell)
            d.ellipse([x - r, y - r, x + r, y + r], fill=colour_)

def chaikin(pts, it=3):
    for _ in range(it):
        if len(pts) < 3:
            return pts
        new = [pts[0]]
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            new += [(.75 * ax + .25 * bx, .75 * ay + .25 * by), (.25 * ax + .75 * bx, .25 * ay + .75 * by)]
        new.append(pts[-1])
        pts = new
    return pts

def overlay(img, px, full=True):
    d = ImageDraw.Draw(img, "RGBA")
    U = px * G                                    # pixels per 14 km: widths and lettering
    P = lambda q: ((q[0] + .5) * px, (q[1] + .5) * px)
    # river and estuary: the model's course, corners cut, as wide as the map says
    widths = river.get("widths", [0.9] * len(river["pts"]))
    rp = [tuple(p) for p in river["pts"]]
    seg = []
    for k, ((ax, ay), (bx, by)) in enumerate(zip(rp, rp[1:])):
        seg.append(((ax, ay), (bx, by), widths[min(k, len(widths) - 1)]))
    fine = chaikin(rp, 5)
    # widths per waypoint, interpolated along the smoothed course; stamped as discs, so the river is one
    # smooth tube that widens into its estuary
    cum = [0.0]
    for a, b in zip(rp, rp[1:]):
        cum.append(cum[-1] + math.dist(a, b))
    def width_at(q):
        best = min(range(len(rp)), key=lambda k: math.dist(rp[k], q))
        return widths[min(best, len(widths) - 1)]
    dense = []
    for a, b in zip(fine, fine[1:]):
        n = max(1, int(math.dist(a, b) * px / 2))
        dense += [(a[0] + (b[0] - a[0]) * t / n, a[1] + (b[1] - a[1]) * t / n) for t in range(n)]
    wsm = [width_at(q) for q in dense]
    for _ in range(30):                     # smooth the width along the course
        wsm = [wsm[0]] + [(wsm[k - 1] + 2 * wsm[k] + wsm[k + 1]) / 4 for k in range(1, len(wsm) - 1)] + [wsm[-1]]
    for q, wv in zip(dense, wsm):
        x, y = P(q)
        r = max(1.5, px * wv * .28)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(84, 140, 196, 255))
    # towns: built-up land around the houses, small blocks for the houses
    for i in range(W):
        for j in range(H):
            if T[i][j].get("hs"):
                x, y = P((i, j))
                r = px * (.62 + .25 * wm.hsh(i * 7, j * 3))
                d.ellipse([x - r, y - r, x + r, y + r], fill=(222, 210, 200, 255))
    for i in range(W):
        for j in range(H):
            if T[i][j].get("hs"):
                x, y = P((i, j))
                for q in range(5):
                    ox = (wm.hsh(i * 13 + q, j * 5) - .5) * px * .8
                    oy = (wm.hsh(i * 3, j * 11 + q) - .5) * px * .8
                    s2 = px * (.07 + .06 * wm.hsh(i + q, j - q))
                    d.rectangle([x + ox - s2, y + oy - s2, x + ox + s2, y + oy + s2], fill=(150, 120, 110, 255))
    # pipelines, rail, roads (model paths, corners cut)
    for r in ROUTES:
        pts = chaikin([tuple(p) for p in (r.get("path") or r["pts"])], 3)
        xy = [P(p) for p in pts]
        if r["mode"] == "pipeline":
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(126, 82, 160, 255), width=max(2, U // 10))
        elif r["mode"] == "rail":
            d.line(xy, fill=(40, 40, 40, 255), width=max(3, U // 6), joint="curve")
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(250, 250, 250, 255), width=max(1, U // 14))
        elif r["mode"] == "road":
            d.line(xy, fill=(120, 40, 30, 255), width=max(3, U // 5), joint="curve")
            d.line(xy, fill=(232, 120, 80, 255), width=max(2, U // 8), joint="curve")
        elif r["mode"] in ("sea", "air"):
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(40, 90, 150, 200) if r["mode"] == "sea" else (90, 90, 90, 200), width=max(1, U // 12))
    # access roads: the model's road tiles that no route covers, walked into chains and smoothed
    covered = {tuple(q) for r in ROUTES if r["mode"] == "road" for q in r.get("path", [])}
    adj = {}
    for i in range(W):
        for j in range(H):
            m = T[i][j].get("rd", 0)
            for bit, (di, dj) in enumerate(wm.DIRS):
                if m & (1 << bit):
                    adj.setdefault((i, j), set()).add((i + di, j + dj))
    seen = set()
    for a in adj:
        for b in adj[a]:
            e = frozenset((a, b))
            if e in seen or (a in covered and b in covered):
                continue
            chain = [a, b]
            seen.add(e)
            while len(adj.get(chain[-1], ())) == 2:
                nxt = [q for q in adj[chain[-1]] if q != chain[-2]]
                if not nxt or frozenset((chain[-1], nxt[0])) in seen:
                    break
                seen.add(frozenset((chain[-1], nxt[0])))
                chain.append(nxt[0])
            xy = [P(q) for q in chaikin(chain, 2)]
            d.line(xy, fill=(160, 96, 70, 255), width=max(2, U // 9), joint="curve")
    # airports: a runway on the approach-zone squares
    for i in range(W):
        for j in range(H):
            if T[i][j].get("az"):
                x, y = P((i, j))
                d.rectangle([x - px * .5, y - px * .09, x + px * .5, y + px * .09], fill=(110, 110, 110, 255))
    # party buildings
    for i in range(W):
        for j in range(H):
            if T[i][j].get("b"):
                x, y = P((i, j))
                d.rectangle([x - px * .17, y - px * .14, x + px * .17, y + px * .14], fill=(70, 55, 60, 255))
    return d

def border_line(img, px):
    """The land border, traced where the country changes."""
    border_dots(img, px, 3, (170, 45, 40, 235), 1.3)

def labels(img, px):
    d = ImageDraw.Draw(img, "RGBA")
    U = px * G                                    # pixels per 14 km: widths and lettering
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(U * .75))
        fs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(U * .55))
        fc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(U * 1.3))
    except OSError:
        f = fs = fc = ImageFont.load_default()
    P = lambda q: ((q[0] + .5) * px, (q[1] + .5) * px)
    def txt(q, t, font, fill=(30, 30, 40, 255), dx=0, dy=0):
        x, y = P(q)
        d.text((x + dx, y + dy), t, font=font, fill=fill, stroke_width=max(1, U // 12), stroke_fill=(255, 255, 255, 200))
    for t in WORLD["towns"]:
        txt(t["c"], t["name"], f, dx=U * .6, dy=-U * 1.2)
    for l in WORLD["localities"]:
        txt(l["c"], l["name"], fs, dx=U * .5, dy=-U * .8)
    txt((5 * G, 30 * G), "URVANIA", fc, fill=(80, 100, 70, 220))
    txt((30 * G, 19 * G), "BAYVARRA", fc, fill=(110, 95, 60, 220))
    txt((53 * G, 33 * G), "LISAVU", fc, fill=(120, 90, 60, 220))
    txt((42 * G, 41 * G), "Atlantic Ocean", fs, fill=(50, 90, 130, 230))
    # scale bar: 100 km
    x0, y0 = U * 2, img.size[1] - U * 2
    L = 100 / KM * px
    d.rectangle([x0 - 6, y0 - U * .9, x0 + L + U * 2.2, y0 + U * .5], fill=(255, 255, 255, 200))
    for k in range(4):
        d.rectangle([x0 + k * L / 4, y0, x0 + (k + 1) * L / 4, y0 + U * .25], fill=(30, 30, 40, 255) if k % 2 == 0 else (255, 255, 255, 255), outline=(30, 30, 40, 255))
    d.text((x0, y0 - U * .8), "0", font=fs, fill=(30, 30, 40, 255))
    d.text((x0 + L - U * .6, y0 - U * .8), "100 km", font=fs, fill=(30, 30, 40, 255))
    d.text((x0 + L + U * .4, y0 - U * .1), f"1 square = {KM:g} km", font=fs, fill=(30, 30, 40, 255))



def strip(levels_list, px, out_path):
    """The refinement, level by level: terrain only, side by side."""
    imgs = [render(lv, px) for lv in levels_list]
    w, h = imgs[0].size
    sheet = Image.new("RGB", (w * len(imgs) + 10 * (len(imgs) - 1), h + 40), (255, 255, 255))
    d = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except OSError:
        f = ImageFont.load_default()
    for k, (lv, im) in enumerate(zip(levels_list, imgs)):
        sheet.paste(im, (k * (w + 10), 40))
        size = KM / (2 ** lv)
        d.text((k * (w + 10) + 6, 10), f"level {lv}: squares of {size:g} km", font=f, fill=(30, 30, 40))
    sheet.save(out_path)




# ---------------------------------------------------------------- road-map style (flat, like a web map)
PAL = {"water": (170, 211, 223), "land": (242, 239, 233), "forest": (205, 230, 196), "field": (238, 238, 222),
     "hills": (232, 228, 214), "urban": (232, 227, 220), "building": (217, 210, 200),
     "road_main": (252, 214, 112), "road_main_edge": (226, 176, 70), "road": (255, 255, 255),
     "road_edge": (214, 208, 198), "rail": (150, 150, 150), "border": (150, 130, 170), "airport": (220, 220, 228),
     "label": (60, 64, 67), "label_soft": (110, 110, 110), "water_label": (80, 130, 175)}

def render_flat(levels, px):
    return colour(*raster(levels, px), "flat")

def overlay_flat(img, px):
    d = ImageDraw.Draw(img, "RGBA")
    U = px * G                                    # pixels per 14 km: widths and lettering
    P = lambda q: ((q[0] + .5) * px, (q[1] + .5) * px)
    # river: one tube, widening into the estuary
    widths = river.get("widths", [0.9] * len(river["pts"]))
    rp = [tuple(p) for p in river["pts"]]
    fine = chaikin(rp, 5)
    dense = []
    for a, b in zip(fine, fine[1:]):
        n = max(1, int(math.dist(a, b) * px / 2))
        dense += [(a[0] + (b[0] - a[0]) * t / n, a[1] + (b[1] - a[1]) * t / n) for t in range(n)]
    wsm = [widths[min(min(range(len(rp)), key=lambda k: math.dist(rp[k], q)), len(widths) - 1)] for q in dense]
    for _ in range(30):
        wsm = [wsm[0]] + [(wsm[k - 1] + 2 * wsm[k] + wsm[k + 1]) / 4 for k in range(1, len(wsm) - 1)] + [wsm[-1]]
    for q, wv in zip(dense, wsm):
        x, y = P(q); r = max(1.5, px * wv * .26)
        d.ellipse([x - r, y - r, x + r, y + r], fill=PAL["water"])
    # built-up areas: the house squares merged into one smooth area per town
    mask = Image.new("L", img.size, 0)
    md = ImageDraw.Draw(mask)
    for i in range(W):
        for j in range(H):
            if T[i][j].get("hs"):
                x, y = P((i, j)); r = px * (.72 + .2 * wm.hsh(i * 7, j * 3))
                md.ellipse([x - r, y - r, x + r, y + r], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(px * .35)).point(lambda v: 255 if v > 110 else 0)
    img.paste(Image.new("RGB", img.size, PAL["urban"]), (0, 0), mask)
    d = ImageDraw.Draw(img, "RGBA")
    for i in range(W):
        for j in range(H):
            if T[i][j].get("hs") or T[i][j].get("b"):
                x, y = P((i, j))
                for q in range(6 if T[i][j].get("hs") else 2):
                    ox = (wm.hsh(i * 13 + q, j * 5) - .5) * px * .8
                    oy = (wm.hsh(i * 3, j * 11 + q) - .5) * px * .8
                    s2 = px * (.05 + .05 * wm.hsh(i + q, j - q))
                    d.rectangle([x + ox - s2, y + oy - s2 * .8, x + ox + s2, y + oy + s2 * .8], fill=PAL["building"])
    # airports: grey ground with a runway
    for i in range(W):
        for j in range(H):
            if T[i][j].get("az"):
                x, y = P((i, j))
                d.rectangle([x - px * .55, y - px * .3, x + px * .55, y + px * .3], fill=PAL["airport"])
                d.rectangle([x - px * .55, y - px * .06, x + px * .55, y + px * .06], fill=(190, 190, 200))
    # minor roads (walked into chains), then rail, then main roads on top
    covered = {tuple(q) for r in ROUTES if r["mode"] == "road" for q in r.get("path", [])}
    adj = {}
    for i in range(W):
        for j in range(H):
            m = T[i][j].get("rd", 0)
            for bit, (di, dj) in enumerate(wm.DIRS):
                if m & (1 << bit):
                    adj.setdefault((i, j), set()).add((i + di, j + dj))
    chains, seen = [], set()
    for a in adj:
        for b in adj[a]:
            e = frozenset((a, b))
            if e in seen or (a in covered and b in covered):
                continue
            chain = [a, b]; seen.add(e)
            while len(adj.get(chain[-1], ())) == 2:
                nxt = [q for q in adj[chain[-1]] if q != chain[-2]]
                if not nxt or frozenset((chain[-1], nxt[0])) in seen:
                    break
                seen.add(frozenset((chain[-1], nxt[0]))); chain.append(nxt[0])
            chains.append([P(q) for q in chaikin(chain, 2)])
    for xy in chains:
        d.line(xy, fill=PAL["road_edge"], width=max(3, U // 6), joint="curve")
    for xy in chains:
        d.line(xy, fill=PAL["road"], width=max(2, U // 9), joint="curve")
    for r in ROUTES:
        xy = [P(p) for p in chaikin([tuple(p) for p in (r.get("path") or r["pts"])], 3)]
        if r["mode"] == "rail":
            d.line(xy, fill=PAL["rail"], width=max(2, U // 10), joint="curve")
            for a, b in zip(xy[::3], xy[1::3]):
                d.line([a, b], fill=(255, 255, 255), width=max(1, U // 18))
        elif r["mode"] == "pipeline":
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(190, 170, 205), width=max(1, U // 16))
        elif r["mode"] in ("sea", "air"):
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(120, 160, 200) if r["mode"] == "sea" else (170, 170, 170), width=max(1, U // 16))
    MAIN = {"road", "road-b", "road-port", "road-c"}
    for r in ROUTES:
        if r["mode"] == "road" and r["id"] not in MAIN:
            xy = [P(p) for p in chaikin([tuple(p) for p in r["path"]], 3)]
            d.line(xy, fill=PAL["road_edge"], width=max(3, U // 6), joint="curve")
            d.line(xy, fill=PAL["road"], width=max(2, U // 9), joint="curve")
    for r in ROUTES:
        if r["mode"] == "road" and r["id"] in MAIN:
            xy = [P(p) for p in chaikin([tuple(p) for p in r["path"]], 3)]
            d.line(xy, fill=PAL["road_main_edge"], width=max(4, U // 4), joint="curve")
    for r in ROUTES:
        if r["mode"] == "road" and r["id"] in MAIN:
            xy = [P(p) for p in chaikin([tuple(p) for p in r["path"]], 3)]
            d.line(xy, fill=PAL["road_main"], width=max(3, U // 6), joint="curve")
    # land border: dotted, traced where the country changes
    border_dots(img, px, 3, PAL["border"], U * .045)

def labels_flat(img, px):
    d = ImageDraw.Draw(img, "RGBA")
    U = px * G                                    # pixels per 14 km: widths and lettering
    F = lambda bold, size: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""), int(size))
    P = lambda q: ((q[0] + .5) * px, (q[1] + .5) * px)
    def txt(q, t, font, fill, dx=0, dy=0, anchor="lm", halo=True):
        x, y = P(q)
        d.text((x + dx, y + dy), t, font=font, fill=fill, anchor=anchor,
               stroke_width=max(2, U // 10) if halo else 0, stroke_fill=(255, 255, 255, 230))
    def dot(q, col, r=.22):
        x, y = P(q); d.ellipse([x - U * r, y - U * r, x + U * r, y + U * r], fill=col, outline=(255, 255, 255), width=max(1, U // 14))
    # Lisavu is an inset: about 1,000 km east of Lumeport, drawn nearer (a frame and a note say so; on the sheet
    # the island has a panel of its own instead)
    isle = [(i, j) for i in range(W) for j in range(H) if T[i][j]["c"] == "XL"]
    x0, y0 = P((min(i for i, _ in isle) - 4, min(j for _, j in isle) - 7))
    x1, y1 = P((W - 1.5, max(j for _, j in isle) + 4))
    for k in (range(int(x0), int(x1), int(U * .4)) if INSET_FRAME else ()):
        d.line([(k, y0), (min(x1, k + U * .2), y0)], fill=PAL["water_label"], width=max(1, U // 16))
        d.line([(k, y1), (min(x1, k + U * .2), y1)], fill=PAL["water_label"], width=max(1, U // 16))
    for k in (range(int(y0), int(y1), int(U * .4)) if INSET_FRAME else ()):
        d.line([(x0, k), (x0, min(y1, k + U * .2))], fill=PAL["water_label"], width=max(1, U // 16))
    INSET_FRAME and d.multiline_text((x0 + U * .3, y0 + U * .3), "Lisavu, about 1,000 km east of Lumeport:\ndrawn nearer, at the same scale",
                     font=F(False, U * .45), fill=PAL["water_label"], anchor="la")
    for t in WORLD["towns"]:
        dot(t["c"], (90, 90, 90), .28)
        right = t["c"][0] > W - 40                                  # near the right edge: the name on the left
        txt(t["c"], t["name"], F(True, U * .85), PAL["label"], dx=-U * .45 if right else U * .45, dy=U * .9 if right else -U * .7,
            anchor="rm" if right else "lm")
    for l in WORLD["localities"]:
        dot(l["c"], (120, 120, 120), .18)
        txt(l["c"], l["name"], F(False, U * .62), PAL["label"], dx=U * .35, dy=-U * .5)
    # ports and airports from the model's parties
    POI = {"16-xb": "Port of Lumeport", "16-xl": "Port of Selanu", "17-xb": "Lumeport Airport", "17-xl": "Selanu Airport"}
    where = {}
    for i in range(W):
        for j in range(H):
            b = T[i][j].get("b")
            if b in POI:
                where.setdefault(b, []).append((i, j))
    PLACE = {"16-xb": (.5, .7, "lm"), "17-xb": (-.5, -.1, "rm"), "16-xl": (.5, 3.4, "rm"), "17-xl": (-.5, -1.2, "rm")}
    for b, sq in where.items():
        q = (sum(a for a, _ in sq) / len(sq), sum(c for _, c in sq) / len(sq))
        col = (66, 133, 244) if b.startswith("16") else (120, 120, 140)
        dot(q, col, .3)
        dx, dy, anchor = PLACE[b]
        txt(q, POI[b], F(False, U * .58), (40, 90, 170) if b.startswith("16") else PAL["label_soft"], dx=U * dx, dy=U * dy, anchor=anchor)
    sp = lambda t: " ".join(t)
    txt((5 * G, 30 * G), sp("URVANIA"), F(False, U * 1.1), (125, 125, 125, 255), anchor="lm")
    txt((29 * G, 19 * G), sp("BAYVARRA"), F(False, U * 1.1), (125, 125, 125, 255), anchor="lm")
    txt((52 * G, 33.5 * G), sp("LISAVU"), F(False, U * 1.0), (125, 125, 125, 255), anchor="lm")
    txt((42 * G, 41 * G), "Atlantic Ocean", F(False, U * .75), PAL["water_label"], anchor="lm", halo=False)
    # scale bar
    if not INSET_FRAME:
        return
    x0, y0 = U * 2.2, img.size[1] - U * 1.6
    L = 100 / KM * px
    d.line([(x0, y0), (x0 + L, y0)], fill=(80, 80, 80), width=max(2, U // 10))
    for xx in (x0, x0 + L / 2, x0 + L):
        d.line([(xx, y0 - U * .25), (xx, y0)], fill=(80, 80, 80), width=max(2, U // 10))
    d.text((x0 + L + U * .4, y0), "100 km", font=F(False, U * .55), fill=(80, 80, 80), anchor="lm")

INSET_FRAME = True

# ---------------------------------------------------------------- the printed sheet (O151)
SCALE = 2_500_000                                 # 1 : 2,500,000
DPI = 300
SHEET_MM = (420, 297)                             # A3 landscape
MM = DPI / 25.4                                   # pixels per mm

def sheet(out_path, levels=5):
    """The map as a printed sheet: A3 landscape at 1 : 2,500,000 and 300 dpi, in two panels in one frame (style C
    of O151): the mainland, and Lisavu, which lies about 1,000 km east and is shown at the same scale."""
    global INSET_FRAME
    INSET_FRAME = False
    px_true = KM * 1e6 / SCALE * MM               # pixels per square at the sheet's scale (16.5 at 300 dpi)
    px = math.ceil(px_true)
    img = render_flat(levels, px)
    overlay_flat(img, px)
    labels_flat(img, px)
    f = px_true / px
    img = img.resize((round(img.size[0] * f), round(img.size[1] * f)), Image.LANCZOS)
    sea = PAL["sea"] if "sea" in PAL else img.getpixel((2, 2))
    paper, ink = (255, 255, 255), (60, 64, 67)
    Wp, Hp = (round(v * MM) for v in SHEET_MM)
    out = Image.new("RGB", (Wp, Hp), paper)
    d = ImageDraw.Draw(out)
    F = lambda bold, mm: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""), round(mm * MM))
    m, gut, head, foot = 10 * MM, 6 * MM, 11 * MM, 16 * MM
    top, bottom = m + head, Hp - m - foot
    w_isle = 94 * MM
    w_main = Wp - 2 * m - gut - w_isle
    def panel(x0, w, cols, title):
        """A panel of the sheet, centred on the land of the given columns."""
        land = [(i, j) for i in cols for j in range(H) if K[i, j] != 0]
        ci = (min(i for i, _ in land) + max(i for i, _ in land) + 1) / 2
        cj = (min(j for _, j in land) + max(j for _, j in land) + 1) / 2
        h = bottom - top
        sx, sy = ci * px_true - w / 2, cj * px_true - h / 2
        tile = Image.new("RGB", (round(w), round(h)), sea)
        tile.paste(img, (round(-sx), round(-sy)))
        out.paste(tile, (round(x0), round(top)))
        d.rectangle([x0, top, x0 + w, bottom], outline=ink, width=round(.35 * MM))
        d.text((x0, top - 2.5 * MM), title, font=F(True, 4.2), fill=ink, anchor="ls")
    isle_from = min(i for i in range(W) for j in range(H) if CTY[i, j] == 3) - 2
    panel(m, w_main, range(0, isle_from), "URVANIA AND BAYVARRA")
    xi = m + w_main + gut
    panel(xi, w_isle, range(isle_from, W), "LISAVU")
    # the footer: scale bar, scale, note
    x0, y0 = m, bottom + 8 * MM
    L = 100 * 1e6 / SCALE * MM                    # 100 km on the sheet
    lw = round(.4 * MM)
    for k in range(4):                            # alternating 25 km blocks
        d.rectangle([x0 + k * L / 4, y0 - 1.2 * MM, x0 + (k + 1) * L / 4, y0], fill=ink if k % 2 == 0 else paper, outline=ink, width=lw)
    for k, t in ((0, "0"), (2, "50"), (4, "100 km")):
        d.text((x0 + k * L / 4, y0 + 1.2 * MM), t, font=F(False, 2.6), fill=ink, anchor="ma" if k < 4 else "la")
    d.text((x0 + L + 8 * MM, y0 - .6 * MM), "Scale 1 : 2,500,000", font=F(True, 3.2), fill=ink, anchor="lm")
    d.text((xi, bottom + 4 * MM), "Same scale. Lisavu lies about 1,000 km\neast of Lumeport.", font=F(False, 2.6), fill=ink, anchor="la")
    d.rectangle([m - 3 * MM, m - 3 * MM, Wp - m + 3 * MM, Hp - m + 3 * MM], outline=ink, width=round(.25 * MM))
    out.save(out_path, dpi=(DPI, DPI))
    print(out_path, out.size, "px per square", round(px_true, 3))

def road_map(out_path, levels=5, px=24, ss=2):
    big = render_flat(levels, px * ss)
    overlay_flat(big, px * ss)
    labels_flat(big, px * ss)
    img = big.resize((W * px, H * px), Image.LANCZOS)
    img.save(out_path)
    print(out_path, img.size)


if __name__ == "__main__" and len(sys.argv) > 6 and sys.argv[6] == "roadmap":
    road_map(out, LEVELS, PX)
    sys.exit()

if __name__ == "__main__" and len(sys.argv) > 6 and sys.argv[6] == "sheet":
    sheet(out, LEVELS)
    sys.exit()

if __name__ == "__main__" and len(sys.argv) > 6 and sys.argv[6] == "strip":
    strip([0, 1, 2, 3, 5], PX, out)
    sys.exit()

if __name__ == "__main__":
    img = render(LEVELS, PX)
    if LEVELS > 0:
        overlay(img, PX)
        border_line(img, PX)
        labels(img, PX)
    img.save(out)
    print(out, img.size)
