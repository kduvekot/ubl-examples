"""Top-down map of the UBL example world, refined from the 3D tile map (tools/world_model.py).

The 3D map has 256 x 192 squares of 3.5 km (world_model.GRID = 4 squares per 14 km); the noise that shapes
it is sampled in chart units of 14 km (world_model.chart), the squares of the first map. Level 0 is the noise
the model uses; every next level halves the 14 km square and adds one finer octave of the same noise, so the
coastline, the hills and the forests grow detail while every square keeps what the 3D map shows. Roads, rail,
the river and the pipelines follow the model's own paths, with their corners cut (Chaikin); towns, buildings
and airports stay on their squares.

Usage (from the repository root): python3 tools/world_model.py model.json, then
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 6 roadmap   (road-map style)
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 2 strip     (the levels)
(the fifth argument is the number of pixels per 3.5 km square)
"""
import json, math, sys
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
line = lambda j: (21.5 + 1.6 * math.sin(C(j) / 4.2)) * G           # the land border, in squares (as in the model)
west_end = math.floor(min(line(j) for j in range(H)))
def river_j(i):
    pts = river["pts"]
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        if ax <= i <= bx and ax < bx:
            return ay + (by - ay) * (i - ax) / (bx - ax)
    return pts[-1][1] if i > pts[-1][0] else None
def south_of_river(i, j):
    rj = river_j(i) if i >= west_end else None
    return rj is not None and j > rj

def detail(x, y, levels):
    """The finer octaves added level by level: each halves the square and the amplitude (x, y in chart units)."""
    d, amp = 0.0, 0.10
    for k in range(1, levels + 1):
        f = 2 ** k
        d += (wm.smooth(x * f + 17.3 * k, y * f - 9.1 * k) - .5) * amp
        amp /= 2
    return d

def sample(x, y, levels):
    """Land, country, terrain and height at a point in squares (square centres at integers)."""
    sx, sy = x, y
    x, y = C(x), C(y)                             # chart units from here on
    n = wm.noise(x, y)
    nd = n + detail(x, y, levels) * (1 if levels else 0)
    main = ((x - 21.5) / 19.5) ** 2 + ((y - 24.5) / 20) ** 2 < 1 - (nd - .5) * .55
    isle = ((x - 52.5) / 8.2) ** 2 + ((y - 21.5) / 11.5) ** 2 < 1 - (nd - .5) * .5
    if not (main or isle):
        return None
    c = "XL" if isle else ("XU" if (sx < (9999 if south_of_river(sx, sy) else line(sy))) else "XB")
    k = "g"
    taper = max(0.0, x - 16.5) * .07 + max(0.0, y - 14.5) * .07   # the model's box x<17, y<15, faded out
    if c == "XU" and nd - taper > .42:
        k = "r"
    elif nd > .62:
        k = "f"
    elif c == "XB" and nd < .33 and 24 < x < 32:
        k = "d"
    for f in WORLD.get("forests", []):
        if k in ("g", "d") and math.hypot(sx - f["c"][0], sy - f["c"][1]) <= f["r"] + (wm.noise(x * 3, y * 3) - .3) * G:
            k = "f"
    for f in WORLD.get("fields", []):
        if k == "g" and math.hypot(sx - f["c"][0], sy - f["c"][1]) <= f["r"] + ((wm.noise(x * 2, y * 2) - .5) * 1.6 + detail(x, y, levels) * 4) * G:
            k = "d"
    h = max(0.0, nd - .30) * 1.2 + (max(0.0, nd - taper - .40) * 3.0 if c == "XU" else 0)
    return c, k, h

def coast_dist(x, y, levels):
    x, y = C(x), C(y)
    n = wm.noise(x, y) + detail(x, y, levels) * (1 if levels else 0)
    a = 1 - (n - .5) * .55 - (((x - 21.5) / 19.5) ** 2 + ((y - 24.5) / 20) ** 2)
    b = 1 - (n - .5) * .5 - (((x - 52.5) / 8.2) ** 2 + ((y - 21.5) / 11.5) ** 2)
    return max(a, b)

LAND = {"g": (204, 220, 170), "f": (128, 171, 112), "r": (196, 182, 150), "d": (226, 214, 150)}
TINT = {"XU": (0, 6, -6), "XB": (6, 2, -8), "XL": (10, 0, -10)}

def render(levels, px):
    """Raster at px pixels per square; levels = how many times the 14 km square was halved for the noise."""
    w, h = W * px, H * px
    img = Image.new("RGB", (w, h))
    pix = img.load()
    heights = [[0.0] * h for _ in range(w)]
    step = 1 / px
    block = max(1, px * G // (2 ** levels)) if levels < 8 else 1   # pixels per refined square
    cache = {}
    for X in range(w):
        for Y in range(h):
            bx, by = X // block, Y // block
            key = (bx, by)
            if key not in cache:
                x = (bx * block + block / 2) * step - .5
                y = (by * block + block / 2) * step - .5
                cache[key] = (sample(x, y, levels), coast_dist(x, y, levels))
            s, cd = cache[key]
            if s is None:
                depth = min(1.0, max(0.0, -cd) * 3)
                col = tuple(int(a + (b - a) * depth) for a, b in zip((178, 214, 236), (112, 160, 200)))
                pix[X, Y] = col
            else:
                c, k, hh = s
                base = LAND[k]
                t = TINT[c]
                pix[X, Y] = tuple(max(0, min(255, base[i] + t[i])) for i in range(3))
                heights[X][Y] = hh
    # hill shading from the height field (light from the north-west)
    shade = Image.new("L", (w, h), 128)
    sp = shade.load()
    for X in range(1, w - 1):
        for Y in range(1, h - 1):
            if heights[X][Y] <= 0:
                continue
            gx = heights[X + 1][Y] - heights[X - 1][Y]
            gy = heights[X][Y + 1] - heights[X][Y - 1]
            v = 128 - (gx + gy) * px * G * 9
            sp[X, Y] = int(max(60, min(200, v)))
    shade = shade.filter(ImageFilter.GaussianBlur(px * G / 10))
    img = Image.composite(img, img, shade)
    out_img = Image.new("RGB", (w, h))
    op, ip, shp = out_img.load(), img.load(), shade.load()
    for X in range(w):
        for Y in range(h):
            f = shp[X, Y] / 128
            r, g, b = ip[X, Y]
            op[X, Y] = (min(255, int(r * f)), min(255, int(g * f)), min(255, int(b * f)))
    return out_img

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
    """The land border, traced where the country changes between neighbouring fine samples."""
    d = ImageDraw.Draw(img, "RGBA")
    U = px * G                                    # pixels per 14 km: widths and lettering
    st = G / 4
    y = 0.0
    while y < H:
        x = 0.0
        prev = None
        while x < W:
            s = sample(x, y, 3)
            c = s[0] if s else None
            if prev and c and prev != c and "XL" not in (prev, c):
                X, Y = (x + .5) * px, (y + .5) * px
                if int((x + y) * 6) % 3:
                    d.ellipse([X - 1.3, Y - 1.3, X + 1.3, Y + 1.3], fill=(170, 45, 40, 235))
            prev = c if c else prev
            x += st
        y += st / 2
    # and along the river where it is the border
    for i in range(W):
        for j in range(H):
            pass

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
    txt((7 * G, 33 * G), "URVANIA", fc, fill=(80, 100, 70, 220))
    txt((30 * G, 14 * G), "BAYVARRA", fc, fill=(110, 95, 60, 220))
    txt((49 * G, 34 * G), "LISAVU", fc, fill=(120, 90, 60, 220))
    txt((44 * G, 40 * G), "Atlantic Ocean", fs, fill=(50, 90, 130, 230))
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
    w, h = W * px, H * px
    img = Image.new("RGB", (w, h), PAL["water"])
    pix = img.load()
    block = max(1, px * G // (2 ** levels))
    cache = {}
    step = 1 / px
    for X in range(w):
        for Y in range(h):
            key = (X // block, Y // block)
            if key not in cache:
                x = (key[0] * block + block / 2) * step - .5
                y = (key[1] * block + block / 2) * step - .5
                cache[key] = sample(x, y, levels)
            s = cache[key]
            if s is not None:
                k = s[1]
                pix[X, Y] = PAL["forest"] if k == "f" else PAL["field"] if k == "d" else PAL["hills"] if k == "r" else PAL["land"]
    return img

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
    # land border: dashed, traced between neighbouring fine samples of different countries
    st = G / 6                                    # squares between samples
    pts = []
    y = 0.0
    while y < H:
        x, prev = 0.0, None
        while x < W:
            s = sample(x, y, 3); c = s[0] if s else None
            if prev and c and prev != c and "XL" not in (prev, c):
                pts.append(((x + .5 - st / 2) * px, (y + .5) * px))
            prev = c if c else prev
            x += st
        y += st / 3
    for k, (X, Y) in enumerate(pts):
        if (k // 6) % 2 == 0:
            d.ellipse([X - U * .045, Y - U * .045, X + U * .045, Y + U * .045], fill=PAL["border"])

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
    for t in WORLD["towns"]:
        dot(t["c"], (90, 90, 90), .28)
        txt(t["c"], t["name"], F(True, U * .85), PAL["label"], dx=U * .45, dy=-U * .7)
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
    for b, sq in where.items():
        q = (sum(a for a, _ in sq) / len(sq), sum(c for _, c in sq) / len(sq))
        col = (66, 133, 244) if b.startswith("16") else (120, 120, 140)
        dot(q, col, .3)
        txt(q, POI[b], F(False, U * .58), (40, 90, 170) if b.startswith("16") else PAL["label_soft"], dx=U * .5, dy=U * .6)
    sp = lambda t: " ".join(t)
    txt((6 * G, 31 * G), sp("URVANIA"), F(False, U * 1.1), (125, 125, 125, 255), anchor="lm")
    txt((29 * G, 15 * G), sp("BAYVARRA"), F(False, U * 1.1), (125, 125, 125, 255), anchor="lm")
    txt((48 * G, 35 * G), sp("LISAVU"), F(False, U * 1.0), (125, 125, 125, 255), anchor="lm")
    txt((40 * G, 42 * G), "Atlantic Ocean", F(False, U * .75), PAL["water_label"], anchor="lm", halo=False)
    txt((44 * G, 9 * G), "Lisavu lies about 1,000 km east; drawn nearer", F(False, U * .45), PAL["water_label"], anchor="lm", halo=False)
    # scale bar
    x0, y0 = U * 2.2, img.size[1] - U * 1.6
    L = 100 / KM * px
    d.line([(x0, y0), (x0 + L, y0)], fill=(80, 80, 80), width=max(2, U // 10))
    for xx in (x0, x0 + L / 2, x0 + L):
        d.line([(xx, y0 - U * .25), (xx, y0)], fill=(80, 80, 80), width=max(2, U // 10))
    d.text((x0 + L + U * .4, y0), "100 km", font=F(False, U * .55), fill=(80, 80, 80), anchor="lm")

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
