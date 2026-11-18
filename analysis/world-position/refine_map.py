"""Top-down map of the UBL example world, refined from the 3D tile map (tools/world_model.py).

Level 0 is the 3D map: 64 x 48 squares of 14 km. Every next level halves the square and adds one finer
octave of the same noise the model uses, so the coastline, the hills and the forests grow detail while
every original square keeps what the 3D map shows. Roads, rail, the river and the pipelines follow the
model's own paths, with their corners cut (Chaikin); towns, buildings and airports stay on their squares.

Usage (from the repository root): python3 tools/world_model.py model.json, then
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 24 roadmap   (road-map style)
  python3 -I analysis/world-position/refine_map.py model.json world/map.json out.png 5 8 strip      (the levels)
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
KM = 14.0

river = next(r for r in WORLD["routes"] if r["mode"] == "river")
line = lambda j: 21.5 + 1.6 * math.sin(j / 4.2)
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
    """The finer octaves added level by level: each halves the square and the amplitude."""
    d, amp = 0.0, 0.10
    for k in range(1, levels + 1):
        f = 2 ** k
        d += (wm.smooth(x * f + 17.3 * k, y * f - 9.1 * k) - .5) * amp
        amp /= 2
    return d

def sample(x, y, levels):
    """Land, country, terrain and height at a point in tile units (tile centres at integers)."""
    n = wm.noise(x, y)
    nd = n + detail(x, y, levels) * (1 if levels else 0)
    main = ((x - 21.5) / 19.5) ** 2 + ((y - 24.5) / 20) ** 2 < 1 - (nd - .5) * .55
    isle = ((x - 52.5) / 8.2) ** 2 + ((y - 21.5) / 11.5) ** 2 < 1 - (nd - .5) * .5
    if not (main or isle):
        return None
    c = "XL" if isle else ("XU" if (x < (99 if south_of_river(x, y) else line(y))) else "XB")
    k = "g"
    taper = max(0.0, x - 16.5) * .07 + max(0.0, y - 14.5) * .07   # the model's box x<17, y<15, faded out
    if c == "XU" and nd - taper > .42:
        k = "r"
    elif nd > .62:
        k = "f"
    elif c == "XB" and nd < .33 and 24 < x < 32:
        k = "d"
    for f in WORLD.get("forests", []):
        if k in ("g", "d") and math.hypot(x - f["c"][0], y - f["c"][1]) <= f["r"] + wm.noise(x * 3, y * 3) - .3:
            k = "f"
    for f in WORLD.get("fields", []):
        if k == "g" and math.hypot(x - f["c"][0], y - f["c"][1]) <= f["r"] + (wm.noise(x * 2, y * 2) - .5) * 1.6 + detail(x, y, levels) * 4:
            k = "d"
    h = max(0.0, nd - .30) * 1.2 + (max(0.0, nd - taper - .40) * 3.0 if c == "XU" else 0)
    return c, k, h

def coast_dist(x, y, levels):
    n = wm.noise(x, y) + detail(x, y, levels) * (1 if levels else 0)
    a = 1 - (n - .5) * .55 - (((x - 21.5) / 19.5) ** 2 + ((y - 24.5) / 20) ** 2)
    b = 1 - (n - .5) * .5 - (((x - 52.5) / 8.2) ** 2 + ((y - 21.5) / 11.5) ** 2)
    return max(a, b)

LAND = {"g": (204, 220, 170), "f": (128, 171, 112), "r": (196, 182, 150), "d": (226, 214, 150)}
TINT = {"XU": (0, 6, -6), "XB": (6, 2, -8), "XL": (10, 0, -10)}

def render(levels, px):
    """Raster at px pixels per tile; levels = how many times the square was halved for the noise."""
    w, h = W * px, H * px
    img = Image.new("RGB", (w, h))
    pix = img.load()
    heights = [[0.0] * h for _ in range(w)]
    step = 1 / px
    block = max(1, px // (2 ** levels)) if levels < 8 else 1   # pixels per refined square
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
            v = 128 - (gx + gy) * px * 9
            sp[X, Y] = int(max(60, min(200, v)))
    shade = shade.filter(ImageFilter.GaussianBlur(px / 10))
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
                d.line([a, b], fill=(126, 82, 160, 255), width=max(2, px // 10))
        elif r["mode"] == "rail":
            d.line(xy, fill=(40, 40, 40, 255), width=max(3, px // 6), joint="curve")
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(250, 250, 250, 255), width=max(1, px // 14))
        elif r["mode"] == "road":
            d.line(xy, fill=(120, 40, 30, 255), width=max(3, px // 5), joint="curve")
            d.line(xy, fill=(232, 120, 80, 255), width=max(2, px // 8), joint="curve")
        elif r["mode"] in ("sea", "air"):
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(40, 90, 150, 200) if r["mode"] == "sea" else (90, 90, 90, 200), width=max(1, px // 12))
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
            d.line(xy, fill=(160, 96, 70, 255), width=max(2, px // 9), joint="curve")
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
    st = 1 / 4
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
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(px * .75))
        fs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(px * .55))
        fc = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(px * 1.3))
    except OSError:
        f = fs = fc = ImageFont.load_default()
    P = lambda q: ((q[0] + .5) * px, (q[1] + .5) * px)
    def txt(q, t, font, fill=(30, 30, 40, 255), dx=0, dy=0):
        x, y = P(q)
        d.text((x + dx, y + dy), t, font=font, fill=fill, stroke_width=max(1, px // 12), stroke_fill=(255, 255, 255, 200))
    for t in WORLD["towns"]:
        txt(t["c"], t["name"], f, dx=px * .6, dy=-px * 1.2)
    for l in WORLD["localities"]:
        txt(l["c"], l["name"], fs, dx=px * .5, dy=-px * .8)
    txt((7, 33), "URVANIA", fc, fill=(80, 100, 70, 220))
    txt((30, 14), "BAYVARRA", fc, fill=(110, 95, 60, 220))
    txt((49, 34), "LISAVU", fc, fill=(120, 90, 60, 220))
    txt((44, 40), "Atlantic Ocean", fs, fill=(50, 90, 130, 230))
    # scale bar: 100 km
    x0, y0 = px * 2, img.size[1] - px * 2
    L = 100 / KM * px
    d.rectangle([x0 - 6, y0 - px * .9, x0 + L + px * 2.2, y0 + px * .5], fill=(255, 255, 255, 200))
    for k in range(4):
        d.rectangle([x0 + k * L / 4, y0, x0 + (k + 1) * L / 4, y0 + px * .25], fill=(30, 30, 40, 255) if k % 2 == 0 else (255, 255, 255, 255), outline=(30, 30, 40, 255))
    d.text((x0, y0 - px * .8), "0", font=fs, fill=(30, 30, 40, 255))
    d.text((x0 + L - px * .6, y0 - px * .8), "100 km", font=fs, fill=(30, 30, 40, 255))
    d.text((x0 + L + px * .4, y0 - px * .1), "1 square = 14 km", font=fs, fill=(30, 30, 40, 255))



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
G = {"water": (170, 211, 223), "land": (242, 239, 233), "forest": (205, 230, 196), "field": (238, 238, 222),
     "hills": (232, 228, 214), "urban": (232, 227, 220), "building": (217, 210, 200),
     "road_main": (252, 214, 112), "road_main_edge": (226, 176, 70), "road": (255, 255, 255),
     "road_edge": (214, 208, 198), "rail": (150, 150, 150), "border": (150, 130, 170), "airport": (220, 220, 228),
     "label": (60, 64, 67), "label_soft": (110, 110, 110), "water_label": (80, 130, 175)}

def render_flat(levels, px):
    w, h = W * px, H * px
    img = Image.new("RGB", (w, h), G["water"])
    pix = img.load()
    block = max(1, px // (2 ** levels))
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
                pix[X, Y] = G["forest"] if k == "f" else G["field"] if k == "d" else G["hills"] if k == "r" else G["land"]
    return img

def overlay_flat(img, px):
    d = ImageDraw.Draw(img, "RGBA")
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
        d.ellipse([x - r, y - r, x + r, y + r], fill=G["water"])
    # built-up areas: the house squares merged into one smooth area per town
    mask = Image.new("L", img.size, 0)
    md = ImageDraw.Draw(mask)
    for i in range(W):
        for j in range(H):
            if T[i][j].get("hs"):
                x, y = P((i, j)); r = px * (.72 + .2 * wm.hsh(i * 7, j * 3))
                md.ellipse([x - r, y - r, x + r, y + r], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(px * .35)).point(lambda v: 255 if v > 110 else 0)
    img.paste(Image.new("RGB", img.size, G["urban"]), (0, 0), mask)
    d = ImageDraw.Draw(img, "RGBA")
    for i in range(W):
        for j in range(H):
            if T[i][j].get("hs") or T[i][j].get("b"):
                x, y = P((i, j))
                for q in range(6 if T[i][j].get("hs") else 2):
                    ox = (wm.hsh(i * 13 + q, j * 5) - .5) * px * .8
                    oy = (wm.hsh(i * 3, j * 11 + q) - .5) * px * .8
                    s2 = px * (.05 + .05 * wm.hsh(i + q, j - q))
                    d.rectangle([x + ox - s2, y + oy - s2 * .8, x + ox + s2, y + oy + s2 * .8], fill=G["building"])
    # airports: grey ground with a runway
    for i in range(W):
        for j in range(H):
            if T[i][j].get("az"):
                x, y = P((i, j))
                d.rectangle([x - px * .55, y - px * .3, x + px * .55, y + px * .3], fill=G["airport"])
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
        d.line(xy, fill=G["road_edge"], width=max(3, px // 6), joint="curve")
    for xy in chains:
        d.line(xy, fill=G["road"], width=max(2, px // 9), joint="curve")
    for r in ROUTES:
        xy = [P(p) for p in chaikin([tuple(p) for p in (r.get("path") or r["pts"])], 3)]
        if r["mode"] == "rail":
            d.line(xy, fill=G["rail"], width=max(2, px // 10), joint="curve")
            for a, b in zip(xy[::3], xy[1::3]):
                d.line([a, b], fill=(255, 255, 255), width=max(1, px // 18))
        elif r["mode"] == "pipeline":
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(190, 170, 205), width=max(1, px // 16))
        elif r["mode"] in ("sea", "air"):
            for a, b in zip(xy[::2], xy[1::2]):
                d.line([a, b], fill=(120, 160, 200) if r["mode"] == "sea" else (170, 170, 170), width=max(1, px // 16))
    MAIN = {"road", "road-b", "road-port", "road-c"}
    for r in ROUTES:
        if r["mode"] == "road" and r["id"] not in MAIN:
            xy = [P(p) for p in chaikin([tuple(p) for p in r["path"]], 3)]
            d.line(xy, fill=G["road_edge"], width=max(3, px // 6), joint="curve")
            d.line(xy, fill=G["road"], width=max(2, px // 9), joint="curve")
    for r in ROUTES:
        if r["mode"] == "road" and r["id"] in MAIN:
            xy = [P(p) for p in chaikin([tuple(p) for p in r["path"]], 3)]
            d.line(xy, fill=G["road_main_edge"], width=max(4, px // 4), joint="curve")
    for r in ROUTES:
        if r["mode"] == "road" and r["id"] in MAIN:
            xy = [P(p) for p in chaikin([tuple(p) for p in r["path"]], 3)]
            d.line(xy, fill=G["road_main"], width=max(3, px // 6), joint="curve")
    # land border: dashed, traced between neighbouring fine samples of different countries
    st = 1 / 6
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
            d.ellipse([X - px * .045, Y - px * .045, X + px * .045, Y + px * .045], fill=G["border"])

def labels_flat(img, px):
    d = ImageDraw.Draw(img, "RGBA")
    F = lambda bold, size: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""), int(size))
    P = lambda q: ((q[0] + .5) * px, (q[1] + .5) * px)
    def txt(q, t, font, fill, dx=0, dy=0, anchor="lm", halo=True):
        x, y = P(q)
        d.text((x + dx, y + dy), t, font=font, fill=fill, anchor=anchor,
               stroke_width=max(2, px // 10) if halo else 0, stroke_fill=(255, 255, 255, 230))
    def dot(q, col, r=.22):
        x, y = P(q); d.ellipse([x - px * r, y - px * r, x + px * r, y + px * r], fill=col, outline=(255, 255, 255), width=max(1, px // 14))
    for t in WORLD["towns"]:
        dot(t["c"], (90, 90, 90), .28)
        txt(t["c"], t["name"], F(True, px * .85), G["label"], dx=px * .45, dy=-px * .7)
    for l in WORLD["localities"]:
        dot(l["c"], (120, 120, 120), .18)
        txt(l["c"], l["name"], F(False, px * .62), G["label"], dx=px * .35, dy=-px * .5)
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
        txt(q, POI[b], F(False, px * .58), (40, 90, 170) if b.startswith("16") else G["label_soft"], dx=px * .5, dy=px * .6)
    sp = lambda t: " ".join(t)
    txt((6, 31), sp("URVANIA"), F(False, px * 1.1), (125, 125, 125, 255), anchor="lm")
    txt((29, 15), sp("BAYVARRA"), F(False, px * 1.1), (125, 125, 125, 255), anchor="lm")
    txt((48, 35), sp("LISAVU"), F(False, px * 1.0), (125, 125, 125, 255), anchor="lm")
    txt((40, 42), "Atlantic Ocean", F(False, px * .75), G["water_label"], anchor="lm", halo=False)
    txt((44, 9), "Lisavu lies about 1,000 km east; drawn nearer", F(False, px * .45), G["water_label"], anchor="lm", halo=False)
    # scale bar
    x0, y0 = px * 2.2, img.size[1] - px * 1.6
    L = 100 / KM * px
    d.line([(x0, y0), (x0 + L, y0)], fill=(80, 80, 80), width=max(2, px // 10))
    for xx in (x0, x0 + L / 2, x0 + L):
        d.line([(xx, y0 - px * .25), (xx, y0)], fill=(80, 80, 80), width=max(2, px // 10))
    d.text((x0 + L + px * .4, y0), "100 km", font=F(False, px * .55), fill=(80, 80, 80), anchor="lm")

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
