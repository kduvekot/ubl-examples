"""Top-down map of the UBL example world, refined from the 3D tile map (tools/world_model.py).

The 3D map has 256 x 192 squares of 3.5 km (world_model.GRID = 4 squares per 14 km). The land itself is drawn
from the terrain's fine rasters (world/terrain/*.png, made by tools/terrain.py, O152: heights and land cover in cells
of 875 m on the mainland and 437.5 m on Lisavu): coast, relief (shaded, the land tinted by height), forests, fields,
heath, rock and marsh as the terrain has them, and the rivers from the terrain's streams, wider as they drain more;
the managed forest of Upland State with its compartments by age (terrain "managed_forests"), the mine sign at the
mine.
The countries are the model's squares, their edge bent a little by the model's noise. Roads, rail and the
pipelines follow the model's own paths, with their corners cut (Chaikin);
the land use round the towns and villages from the model ("lu", tools/land_use.py: fields, pasture, orchards and
vineyards, woods), elsewhere the terrain's natural cover; the villages as dots by their size, the named ones with
their names, their minor roads as thin lines; the towns' built-up areas tinted by their districts' character (or,
with "periods", by the period they grew in);
towns are drawn as their built-up areas, true to size (the model's sub-squares "um", 875 m), with their names beside
them; buildings and airports stay on their squares.

Usage (from the repository root): python3 tools/world_model.py model.json, then
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 6 roadmap   (road-map style)
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 0 sheet     (A3, 1 : 2,500,000)
  ... out.png 5 0 sheet periods   (the same, the towns' built-up areas coloured by the period of their districts)
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

V = np.array(M["model"]["v"], dtype=np.float32)    # corner heights (metres), [W + 1][H + 1]
LEVEL_M = M["model"].get("level_m", wm.LEVEL_M)
KIND = {"s": 0, "w": 1, "g": 2, "f": 3, "r": 4, "d": 5, "h": 6, "m": 7, "p": 8, "o": 9}   # p pasture, o orchard (land use)
TERRAIN = json.load(open("world/terrain.json"))
# the terrain's land cover classes (tools/terrain_lib.py: sea, water, field, forest, grass, heath, rock, marsh) as KIND codes
COVER_TO_KIND = np.array([0, 1, 5, 3, 2, 6, 4, 7], dtype=np.int8)
FINE = []
for name, r_ in TERRAIN["rasters"].items():
    FINE.append((r_["x0"], r_["y0"], r_["cells_per_square"],
                 np.array(Image.open(r_["height"]), dtype=np.float32).T - r_["offset_m"],     # [x][y], metres
                 COVER_TO_KIND[np.array(Image.open(r_["cover"])).T]))
# the land use (tools/land_use.py, model "lu" and "k"): who farms each cell round the towns and villages; where the
# model gives a square no "lu", its cells are all of its kind; the parties' squares, a harbour, a station and the
# managed forest keep the terrain's cover
for x0_, y0_, S_, _, Km_ in FINE:
    for a_ in range(Km_.shape[0] // S_):
        for b_ in range(Km_.shape[1] // S_):
            t_ = M["model"]["tiles"][x0_ + a_][y0_ + b_]
            if "lu" in t_:
                lu_ = t_["lu"]
                Km_[a_ * S_:(a_ + 1) * S_, b_ * S_:(b_ + 1) * S_] = np.array([KIND[c] for c in lu_], np.int8).reshape(S_, S_)
            elif t_["k"] not in ("s", "w") and not any(k in t_ for k in ("b", "hb", "ms", "mf")):
                Km_[a_ * S_:(a_ + 1) * S_, b_ * S_:(b_ + 1) * S_] = KIND[t_["k"]]
COUNTRY = {None: 0, "XU": 1, "XB": 2, "XL": 3}
PARTIES = json.load(open("world/parties.json", encoding="utf-8"))["parties"]
OWNED = {(i, j) for i in range(W) for j in range(H) if T[i][j].get("b")}
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
    north-west) per pixel. Kind and height come from the terrain's fine rasters (height interpolated, cover the
    nearest cell); the country is the model's square, looked up at a position the model's noise bends by up to half
    a square, so that the border is not a staircase."""
    w, h = W * px, H * px
    X = (np.arange(w, dtype=np.float32) + .5) / px                # in squares (square i spans i .. i + 1)
    Y = (np.arange(h, dtype=np.float32) + .5) / px
    xx, yy = np.meshgrid(X, Y, indexing="ij")
    kind = np.zeros((w, h), np.int8)
    elev = np.zeros((w, h), np.float32)
    for x0, y0, S, Hm, Km in FINE:
        fx, fy = (xx - x0) * S - .5, (yy - y0) * S - .5
        inside = (fx >= 0) & (fy >= 0) & (fx < Hm.shape[0] - 1) & (fy < Hm.shape[1] - 1)
        i0, j0 = np.clip(fx, 0, Hm.shape[0] - 2).astype(np.int32), np.clip(fy, 0, Hm.shape[1] - 2).astype(np.int32)
        u, v = np.clip(fx - i0, 0, 1), np.clip(fy - j0, 0, 1)
        e = Hm[i0, j0] * (1 - u) * (1 - v) + Hm[i0 + 1, j0] * u * (1 - v) + Hm[i0, j0 + 1] * (1 - u) * v + Hm[i0 + 1, j0 + 1] * u * v
        k = Km[np.clip(np.rint(fx), 0, Hm.shape[0] - 1).astype(np.int32), np.clip(np.rint(fy), 0, Hm.shape[1] - 1).astype(np.int32)]
        elev = np.where(inside, e, elev)
        kind = np.where(inside, k, kind)
    elev = np.where(kind == 0, 0, np.maximum(elev, 0))
    cx, cy = (xx - .5) / G, (yy - .5) / G
    wx = detail(cx, cy, 3, 3.3) * 4.5 * G if levels else 0
    wy = detail(cx, cy, 3, 8.1) * 4.5 * G if levels else 0
    cty = CTY[np.clip(np.floor(xx + wx), 0, W - 1).astype(np.int32), np.clip(np.floor(yy + wy), 0, H - 1).astype(np.int32)]
    cty = np.where(kind == 0, 0, cty)
    m_per_px = KM * 1000 / px
    gx, gy = np.gradient(elev, m_per_px)
    exag = 4.0                                                      # vertical exaggeration of the shading
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
    land = (kind != 0) & (kind != 1)
    if style == "flat":
        img = tint(elev)
        for k, col, a in ((3, (190, 222, 180), .75), (5, (243, 228, 176), .8), (4, (214, 208, 198), .7),
                          (6, (228, 224, 200), .7), (7, (206, 226, 214), .75), (8, (212, 234, 188), .75),
                          (9, (228, 202, 224), .8)):
            sel = (kind == k)[..., None]
            img = np.where(sel, img * (1 - a) + np.array(col) * a, img)
        f = (1 + (shade - .707) * .9)[..., None]
        water = np.array((170, 211, 223), dtype=np.float32)
    else:
        img = np.zeros(kind.shape + (3,), dtype=np.float32)
        for k, col in ((2, (204, 220, 170)), (1, (204, 220, 170)), (3, (128, 171, 112)), (4, (196, 182, 150)), (5, (226, 214, 150)),
                       (6, (190, 180, 140)), (7, (170, 200, 180)), (8, (180, 212, 150)), (9, (196, 170, 190))):
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

def streams(d, px, colour_, scale=1.0):
    """The rivers: the terrain's streams (tools/terrain.py), each a line that widens as it drains more land; and the
    small brooks the terrain names (Lumeport's, O153), thin."""
    P = lambda q: (q[0] * px, q[1] * px)
    for b in TERRAIN.get("brooks", {}).values():
        for line in b["lines"]:
            if len(line) > 1:
                wdt = max(1, round(scale * px * .07))
                d.line([P((x, y)) for x, y, _ in line], fill=colour_, width=wdt, joint="curve")
    for name, lines in TERRAIN["streams"].items():
        thr = 400 if name == "mainland" else 60
        for line in lines:
            pts = [(x, y, a) for x, y, a in line]
            for (ax, ay, aa), (bx, by, ba) in zip(pts, pts[1:]):
                if ba < thr:
                    continue
                wdt = max(1, round(scale * px * (.07 + .08 * math.log10(ba / thr + 1) * 2.2)))
                d.line([P((ax, ay)), P((bx, by))], fill=colour_, width=wdt)

def overlay(img, px, full=True):
    d = ImageDraw.Draw(img, "RGBA")
    U = px * G                                    # pixels per 14 km: widths and lettering
    P = lambda q: ((q[0] + .5) * px, (q[1] + .5) * px)
    # rivers: the terrain's streams (the estuary is open water in the terrain)
    streams(d, px, (84, 140, 196, 255))
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



# ---------------------------------------------------------------- road-map style (flat, like a web map)
PAL = {"water": (170, 211, 223), "land": (242, 239, 233), "forest": (205, 230, 196), "field": (238, 238, 222),
     "hills": (232, 228, 214), "urban": (238, 196, 186), "urban_edge": (196, 140, 128), "building": (217, 210, 200),
     "road_main": (252, 214, 112), "road_main_edge": (226, 176, 70), "road": (255, 255, 255),
     "road_edge": (214, 208, 198), "rail": (150, 150, 150), "border": (150, 130, 170), "airport": (220, 220, 228),
     "label": (60, 64, 67), "label_soft": (110, 110, 110), "water_label": (80, 130, 175),
     "road_village": (150, 140, 128), "village": (196, 120, 106)}

def render_flat(levels, px):
    return colour(*raster(levels, px), "flat")

def overlay_flat(img, px):
    d = ImageDraw.Draw(img, "RGBA")
    U = px * G                                    # pixels per 14 km: widths and lettering
    P = lambda q: ((q[0] + .5) * px, (q[1] + .5) * px)
    # the managed forest (world/terrain.json "managed_forests", the forest of Upland State): over the forest tint,
    # its compartments of 875 m in a lighter or deeper green by their age (felled and replanted, young, pole,
    # mature), a fine line where two compartments of different ages meet, and the forest's edge
    managed_forest(img, px)
    d = ImageDraw.Draw(img, "RGBA")
    # rivers: the terrain's streams, wider downstream (the estuary is open water in the terrain)
    streams(d, px, PAL["water"])
    # the rapids above Ferrano (O153): short bars across the river, the map sign for rapids
    rp = [tuple(q) for q in M["model"].get("rapids", [])]
    for k, q in enumerate(rp):
        a, b = rp[max(0, k - 1)], rp[min(len(rp) - 1, k + 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        l = math.hypot(dx, dy) or 1
        nx, ny = -dy / l, dx / l
        for f in (-.25, .25):
            cx, cy = P((q[0] + dx / l * f, q[1] + dy / l * f))
            d.line([(cx - nx * px * .32, cy - ny * px * .32), (cx + nx * px * .32, cy + ny * px * .32)], fill=(40, 90, 150), width=max(2, U // 16))
    # built-up areas: the model's built-up sub-squares ("um", SUB x SUB per square, 875 m), merged into one area
    # per town with a smoothed edge (blurred and cut at the middle, which keeps the area), in the urban colour
    # with a fine darker edge; nothing else marks a town (no building blocks: at 1 : 2,500,000 a road map shows
    # the built-up area only)
    S = wm.SUB
    mask = Image.new("L", img.size, 0)
    md = ImageDraw.Draw(mask)
    for i in range(W):
        for j in range(H):
            um = T[i][j].get("um", 0)
            for a in range(S):
                for b in range(S):
                    if um >> (a * S + b) & 1:
                        x0, y0 = i * px + a * px / S, j * px + b * px / S
                        md.rectangle([x0, y0, x0 + px / S - 1, y0 + px / S - 1], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(px / S * .7)).point(lambda v: 255 if v >= 128 else 0)
    BUILT_MASK[0] = mask
    # airports: grey ground with a runway
    for i in range(W):
        for j in range(H):
            if T[i][j].get("az"):
                x, y = P((i, j))
                d.rectangle([x - px * .55, y - px * .3, x + px * .55, y + px * .3], fill=PAL["airport"])
                d.rectangle([x - px * .55, y - px * .06, x + px * .55, y + px * .06], fill=(190, 190, 200))
    # minor roads (walked into chains), then rail, then main roads on top. Every road, rail line and pipeline is a
    # route laid square by square over the land (8-connected, tools/lay_routes.py, O152 stage 3): drawn as a smooth
    # curve through its squares (Chaikin), with a cased bridge symbol over its bridge squares and a dashed line
    # between the portals of a tunnel; the town streets the model adds are walked into chains from the road masks
    covered = {tuple(q) for r in ROUTES if r["mode"] == "road" for q in r.get("path", [])}
    adj = {}
    for i in range(W):
        for j in range(H):
            m = T[i][j].get("rd", 0)
            for bit, (di, dj) in enumerate(wm.DIRS8):
                if m & (1 << bit):
                    adj.setdefault((i, j), set()).add((i + di, j + dj))
    chains, seen = [], set()
    town = lambda q: "um" in T[q[0]][q[1]]
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
            if all(town(q) for q in chain):
                continue                          # the streets of a town: its built-up area stands for them
            chains.append([P(q) for q in chaikin(chain, 2)])

    def pieces(r, it=3):
        """A route's smooth curve, cut into its pieces on the ground, on bridges and in tunnels: [(kind, points)]
        (kind None, "bridge" or "tunnel"); the curve is smoothed once, over the whole route, and each piece
        takes the part of it between the middles of the edges (or corners) its squares share."""
        path = [tuple(q) for q in (r.get("path") or r["pts"])]
        kinds_ = []
        for q in path:
            t = T[q[0]][q[1]]
            on_deck = r["mode"] != "pipeline" and ((t.get("br") or t.get("tn")) and (t.get("ov") in (None, r["mode"])))
            kinds_.append(("tunnel" if t.get("tn") else "bridge") if on_deck else None)
        if r["mode"] == "road":
            kinds_ = [k if (q not in OWNED) else None for q, k in zip(path, kinds_)]
        n = 2 ** it
        curve = chaikin(path, it)
        # the smoothed point that stands for path square k is near index k * n (Chaikin doubles the segments)
        out, start = [], 0
        for k in range(1, len(path) + 1):
            if k == len(path) or kinds_[k] != kinds_[start]:
                lo = max(0, start * n - n // 2) if start else 0
                hi = min(len(curve) - 1, k * n - n // 2) if k < len(path) else len(curve) - 1
                out.append((kinds_[start], [P(q) for q in curve[lo:hi + 1]]))
                start = k
        return out

    def bridge_mark(d, xy, w):
        """A cased bridge: the road's ends of the deck closed by two short ticks, the deck outlined in dark grey."""
        if len(xy) < 2:
            return
        d.line(xy, fill=(70, 70, 70), width=w + max(4, U // 10), joint="curve")
        for a, b in ((xy[0], xy[1]), (xy[-1], xy[-2])):
            dx, dy = b[0] - a[0], b[1] - a[1]
            l = math.hypot(dx, dy) or 1
            nx, ny = -dy / l, dx / l
            o = (w + max(4, U // 10)) / 2
            for sgn in (1, -1):
                p0 = (a[0] + nx * o * sgn, a[1] + ny * o * sgn)
                d.line([p0, (p0[0] - dx / l * o * .9 + nx * o * .6 * sgn, p0[1] - dy / l * o * .9 + ny * o * .6 * sgn)],
                       fill=(70, 70, 70), width=max(1, U // 26))

    def draw_way(d, r, fill, edge, w, we):
        for kind_, xy in pieces(r):
            if len(xy) < 2:
                continue
            if kind_ == "tunnel":                 # between the portals: a dashed line, no casing
                for a2, b2 in zip(xy[::2], xy[1::2]):
                    d.line([a2, b2], fill=edge, width=max(1, w // 2))
                continue
            if kind_ == "bridge":
                bridge_mark(d, xy, we)
            if edge:
                d.line(xy, fill=edge, width=we, joint="curve")
            d.line(xy, fill=fill, width=w, joint="curve")

    for xy in chains:
        d.line(xy, fill=PAL["road_edge"], width=max(3, U // 6), joint="curve")
    for xy in chains:
        d.line(xy, fill=PAL["road"], width=max(2, U // 9), joint="curve")
    for r in ROUTES:
        if r["mode"] == "rail":
            for kind_, xy in pieces(r):
                if len(xy) < 2:
                    continue
                if kind_ == "tunnel":
                    for a2, b2 in zip(xy[::2], xy[1::2]):
                        d.line([a2, b2], fill=PAL["rail"], width=max(1, U // 20))
                    continue
                if kind_ == "bridge":
                    bridge_mark(d, xy, max(2, U // 10))
                d.line(xy, fill=PAL["rail"], width=max(2, U // 10), joint="curve")
                for a2, b2 in zip(xy[::3], xy[1::3]):
                    d.line([a2, b2], fill=(255, 255, 255), width=max(1, U // 18))
        elif r["mode"] == "pipeline":
            xy = [P(p) for p in chaikin([tuple(p) for p in (r.get("path") or r["pts"])], 3)]
            for a2, b2 in zip(xy[::2], xy[1::2]):
                d.line([a2, b2], fill=(190, 170, 205), width=max(1, U // 16))
        elif r["mode"] in ("sea", "air"):
            xy = [P(p) for p in chaikin([tuple(p) for p in (r.get("path") or r["pts"])], 3)]
            for a2, b2 in zip(xy[::2], xy[1::2]):
                d.line([a2, b2], fill=(120, 160, 200) if r["mode"] == "sea" else (170, 170, 170), width=max(1, U // 16))
    MAIN = {r["id"] for r in ROUTES if r["mode"] == "road" and r.get("class") == "main"}
    for r in ROUTES:                              # the villages' minor roads: a thin line, no casing (O152)
        if r["mode"] == "road" and r["id"].startswith("village-"):
            draw_way(d, r, PAL["road_village"], None, max(1, U // 26), max(2, U // 12))
    for r in ROUTES:
        if r["mode"] == "road" and r["id"] not in MAIN and not r["id"].startswith("village-"):
            draw_way(d, r, PAL["road"], PAL["road_edge"], max(2, U // 9), max(3, U // 6))
    # the built-up areas over the minor roads and the rail (a town of 4 km is 1.6 mm on the sheet, narrower than
    # the road symbols through it), under the main roads
    edge = mask.filter(ImageFilter.MaxFilter(3))
    img.paste(Image.new("RGB", img.size, PAL["urban_edge"]), (0, 0), edge)
    img.paste(Image.new("RGB", img.size, PAL["urban"]), (0, 0), mask)
    districts(img, px, mask)
    d = ImageDraw.Draw(img, "RGBA")
    # the small brooks over the built-up areas they run through (Lumeport's, O153: the town's first water)
    for b in TERRAIN.get("brooks", {}).values():
        for line in b["lines"]:
            if len(line) > 1:
                d.line([P((x - .5, y - .5)) for x, y, _ in line], fill=PAL["water"], width=max(2, U // 16), joint="curve")
    for r in ROUTES:
        if r["mode"] == "road" and r["id"] in MAIN:
            draw_way(d, r, PAL["road_main"], PAL["road_main_edge"], max(3, U // 6), max(4, U // 4))
    # a town's own harbour (Larkmouth, O153): a quay on the water
    for i in range(W):
        for j in range(H):
            if T[i][j].get("hb"):
                x, y = P((i, j))
                d.rectangle([x - px * .18, y - px * .3, x + px * .5, y + px * .3], fill=(120, 120, 130))
    # land border: dotted, traced where the country changes
    border_dots(img, px, 3, PAL["border"], U * .045)

# the towns' districts (map "towns", "districts"; model "ud"): on the sheet the built-up area is tinted by the
# district's character (the old core darker, industry and the port greyer); with DISTRICT_MODE "period" (the crops
# of the towns' growth) by the period the district grew in
CHAR_TINT = {"core": (214, 160, 150), "administration": (226, 178, 168), "residential": (238, 196, 186),
             "suburb": (243, 212, 204), "industry": (206, 196, 210), "port": (196, 204, 218)}
PERIOD_TINT = {"urvanian": (150, 60, 40), "tuscan": (214, 120, 30), "italian": (226, 196, 60), "british": (90, 150, 200),
               "independence": (120, 180, 110), "lisavan": (150, 60, 40), "settler": (180, 70, 60),
               "colonial": (226, 170, 60), "interwar": (160, 110, 190), "postwar": (90, 150, 200),
               "agreement": (120, 180, 110)}
DISTRICT_MODE = ["character"]

def districts(img, px, mask):
    S = wm.SUB
    towns = [t for t in WORLD["towns"] if t.get("districts")]
    lay = Image.new("RGB", img.size, (0, 0, 0))
    sel = Image.new("L", img.size, 0)
    d, ds = ImageDraw.Draw(lay), ImageDraw.Draw(sel)
    for i in range(W):
        for j in range(H):
            ud = T[i][j].get("ud")
            if not ud:
                continue
            tw = min(towns, key=lambda t: math.hypot(t["c"][0] - i, t["c"][1] - j))
            for a in range(S):
                for b in range(S):
                    c = ud[a * S + b]
                    if c == ".":
                        continue
                    dist = tw["districts"]["0123456789abcdefghijklmnopqrstuvwxyz".index(c)]
                    col = PERIOD_TINT[dist["period"]] if DISTRICT_MODE[0] == "period" else CHAR_TINT[dist["character"]]
                    x0, y0 = i * px + a * px / S, j * px + b * px / S
                    box = [x0 - 1, y0 - 1, x0 + px / S, y0 + px / S]
                    d.rectangle(box, fill=col)
                    ds.rectangle(box, fill=255)
    sel = sel.filter(ImageFilter.GaussianBlur(px / S * .5)).point(lambda v: 255 if v >= 128 else 0)
    from PIL import ImageChops
    img.paste(lay, (0, 0), ImageChops.multiply(sel, mask))

MF_TINT = [(232, 234, 206), (204, 228, 188), (184, 216, 170), (166, 204, 154)]   # felled, young, pole, mature

def managed_forest(img, px):
    S = wm.SUB
    cells = {}
    for i in range(W):
        for j in range(H):
            ages = T[i][j].get("mf")
            if ages:
                for a in range(S):
                    for b in range(S):
                        if ages[a * S + b] != ".":
                            cells[(i * S + a, j * S + b)] = int(ages[a * S + b])
    if not cells:
        return
    c = px / S
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    for (x, y), age in cells.items():
        d.rectangle([x * c, y * c, (x + 1) * c - 1, (y + 1) * c - 1], fill=MF_TINT[age] + (190,))
    line, edge = (112, 156, 104, 200), (86, 130, 80, 230)
    w = max(1, round(px / 24))
    for (x, y), age in cells.items():
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            o = cells.get((x + dx, y + dy))
            if o is not None and (o == age or (dx, dy) in ((-1, 0), (0, -1))):
                continue                              # one line per pair of compartments
            x0, y0 = (x + (dx > 0)) * c, (y + (dy > 0)) * c
            seg = [(x0, y0), (x0, y0 + c)] if dx else [(x0, y0), (x0 + c, y0)]
            d.line(seg, fill=edge if o is None else line, width=w)
    img.paste(Image.alpha_composite(img.convert("RGBA"), lay).convert("RGB"))

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
    placed = []
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
        x, y = P(q)
        placed.append(d.textbbox((x + U * dx, y + U * dy), POI[b], font=F(False, U * .58), anchor=anchor))
        placed.append((x - U * .3, y - U * .3, x + U * .3, y + U * .3))
    # mines: the map sign for a mine (hammer and pick) at the mine's square, the adit (Serravona Mining, 4-xu)
    for p in PARTIES:
        if p.get("kind") == "mine":
            x, y = P(p["at"])
            f = F(True, U * .55)
            d.text((x, y), "\u2692", font=f, fill=(50, 50, 55), anchor="mm", stroke_width=max(2, U // 10), stroke_fill=(255, 255, 255, 235))
            placed.append(d.textbbox((x, y), "\u2692", font=f, anchor="mm"))
    # towns: the built-up area is the symbol; the name stands beside it, on the side where it covers the least
    # built-up land, other names and roads. Villages (about 1 km, under half a millimetre) get a dot.
    occupied = BUILT_MASK[0]
    busy_cols = [PAL[k] for k in ("road_main", "road_main_edge", "road", "road_edge", "rail", "urban", "urban_edge")] + [(190, 170, 205)]
    def free_score(box):
        x0, y0, x1, y1 = (int(v) for v in box)
        if x0 < 0 or y0 < 0 or x1 >= img.size[0] or y1 >= img.size[1]:
            return 1e9
        built = sum(occupied.crop((x0, y0, x1, y1)).histogram()[128:]) / max(1, (x1 - x0) * (y1 - y0))
        pix = [img.getpixel((x, y)) for x in range(x0, x1, 3) for y in range(y0, y1, 3)]
        busy = sum(1 for c in pix if any(abs(c[0] - k[0]) + abs(c[1] - k[1]) + abs(c[2] - k[2]) < 24 for k in busy_cols)) / max(1, len(pix))
        clash = sum(1 for b in placed if box[0] < b[2] and box[2] > b[0] and box[1] < b[3] and box[3] > b[1])
        return built * 10 + busy * 4 + clash * 100
    S = wm.SUB
    for t in WORLD["towns"]:
        ci, cj = t["c"]
        reach = 8
        near = t["built_km"] / KM + 1                 # the town's own built-up area, not the villages round it
        cells = [(i * S + a, j * S + b) for i in range(ci - reach, ci + reach + 1) for j in range(cj - reach, cj + reach + 1)
                 if 0 <= i < W and 0 <= j < H and math.hypot(i - ci, j - cj) <= near
                 for a in range(S) for b in range(S) if T[i][j].get("um", 0) >> (a * S + b) & 1]
        x0 = min(x for x, _ in cells) * px / S; x1 = (max(x for x, _ in cells) + 1) * px / S
        y0 = min(y for _, y in cells) * px / S; y1 = (max(y for _, y in cells) + 1) * px / S
        font = F(True, U * .85)
        tw_, th_ = d.textbbox((0, 0), t["name"], font=font)[2:]
        gap = U * .25
        cands = [("lm", (x1 + gap, (y0 + y1) / 2)), ("rm", (x0 - gap, (y0 + y1) / 2)),
                 ("lb", (x1 + gap * .4, y0 + gap * .4)), ("rb", (x0 - gap * .4, y0 + gap * .4)),
                 ("ms", ((x0 + x1) / 2, y0 - gap)), ("ma", ((x0 + x1) / 2, y1 + gap)),
                 ("lt", (x1 + gap * .4, y1 - gap * .4)), ("rt", (x0 - gap * .4, y1 - gap * .4))]
        def box(anchor, xy):
            x, y = xy
            bx = x if anchor[0] == "l" else x - tw_ if anchor[0] == "r" else x - tw_ / 2
            by = y - th_ / 2 if anchor[1] == "m" else y - th_ if anchor[1] in "sb" else y
            return (bx, by, bx + tw_, by + th_)
        anchor, xy = min(cands, key=lambda c: free_score(box(*c)))
        placed.append(box(anchor, xy))
        d.text(xy, t["name"], font=font, fill=PAL["label"], anchor=anchor, stroke_width=max(2, U // 10), stroke_fill=(255, 255, 255, 230))
    for l in WORLD["localities"]:
        dot(l["c"], (120, 120, 120), .14)
        txt(l["c"], l["name"], F(False, U * .62), PAL["label"], dx=U * .3, dy=-U * .4)
    # the villages (map "villages", O152): a dot by their size; the named ones with their name (in Urvania the
    # English (Italian) name, on Lisavu the Lisavan one, or the English one where settlers named the place), placed
    # where it covers the least
    sp_ = lambda t: " ".join(t)                   # the country names (drawn last) are kept free of village names
    for q_, t_, sz_ in (((5 * G, 30 * G), "URVANIA", 1.1), ((29 * G, 19 * G), "BAYVARRA", 1.1), ((52 * G, 33.5 * G), "LISAVU", 1.0)):
        x_, y_ = P(q_)
        placed.append(d.textbbox((x_, y_), sp_(t_), font=F(False, U * sz_), anchor="lm"))
    R_BAND = {"hamlet": .045, "village": .065, "large village": .085, "small town": .11, "country town": .14}
    for v in WORLD.get("villages", []):
        x, y = P(v["c"])
        r = U * R_BAND[v["band"]]
        d.ellipse([x - r, y - r, x + r, y + r], fill=PAL["village"], outline=(120, 70, 60), width=max(1, U // 40))
    for v in sorted(WORLD.get("villages", []), key=lambda v: -v["people"]):
        if not v["name"]:
            continue
        vf = F(v["band"] == "country town", U * (.6 if v["band"] == "country town" else .5 if v["band"] == "small town" else .44))
        x, y = P(v["c"])
        tw_, th_ = d.textbbox((0, 0), v["name"], font=vf)[2:]
        g = U * .16
        cands = [("lm", (x + g, y)), ("rm", (x - g, y)), ("ms", (x, y - g)), ("ma", (x, y + g)),
                 ("lb", (x + g * .7, y - g * .4)), ("lt", (x + g * .7, y + g * .4)),
                 ("rb", (x - g * .7, y - g * .4)), ("rt", (x - g * .7, y + g * .4)),
                 ("ms", (x, y - 3 * g)), ("ma", (x, y + 3 * g))]
        def vbox(anchor, xy):
            bx = xy[0] if anchor[0] == "l" else xy[0] - tw_ if anchor[0] == "r" else xy[0] - tw_ / 2
            by = xy[1] - th_ / 2 if anchor[1] == "m" else xy[1] - th_ if anchor[1] in "sb" else xy[1]
            return (bx, by, bx + tw_, by + th_)
        anchor, xy = min(cands, key=lambda c: free_score(vbox(*c)))
        placed.append(vbox(anchor, xy))
        d.text(xy, v["name"], font=vf, fill=PAL["label"], anchor=anchor, stroke_width=max(2, U // 14),
               stroke_fill=(255, 255, 255, 230))
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
BUILT_MASK = [None]                               # the built-up areas drawn by overlay_flat, for placing the names

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
    if len(sys.argv) > 7 and sys.argv[7] == "periods":     # the built-up areas coloured by the period they grew in
        DISTRICT_MODE[0] = "period"
    sheet(out, LEVELS)
    sys.exit()

if __name__ == "__main__":
    img = render(LEVELS, PX)
    if LEVELS > 0:
        overlay(img, PX)
        border_line(img, PX)
        labels(img, PX)
    img.save(out)
    print(out, img.size)
