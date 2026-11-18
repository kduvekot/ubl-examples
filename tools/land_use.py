#!/usr/bin/env python3
"""The land use of the world (O152, owner 2026-11-18): which land is farmed, and how. Standard library only (Pillow,
when present, only reads the rasters faster); tools/world_model.py calls it, and the model's tiles carry the result
("lu", "k"), which the 3D map and the printed sheet both draw.

Farmland is a property of the land, not of each village. The terrain (tools/terrain.py) gives every cell of 875 m
(437.5 m on Lisavu) its natural cover (forest, grass, scrub and heath, rock, marsh, and "field" for open, level,
well-drained land that could be ploughed), its height and its yearly rain. Each cell is farmed in the way of its
region, by its own soil, slope, rain and aspect (in the southern hemisphere a slope facing north gets the sun):

  * Urvania: the river valley (within about 9 km of the main river, below 400 m): fields on the terraces and the
    valley floor, flood meadows beside the river, vineyards and orchards on the slopes facing the sun; the wet west
    (over 880 mm): a mosaic of small fields, hay meadows, orchards and woodlots; the drier hills: wheat and barley
    on the level, olives and vines on the sunny slopes, sheep;
  * Bayvarra: wheat land (over 540 mm) in large paddocks on the level open land, sheep runs on the rougher ground;
    the dry east: open sheep and cattle runs, with home paddocks near the homesteads;
  * Lisavu: cotton on the dry lee side's level land, gardens and fruit in the wet windward valleys;
  * a cell is farmed only within reach of the people who farm it (REACH: the distance, km, to the nearest town,
    village or road; the dispersed farmsteads lie along the roads; the edge is ragged, paddock by paddock, and
    the reach is wider than the gaps between the villages, so it seldom shows); further out the land keeps its natural
    cover, and the terrain's "field" there is open grassland ("g"): no one ploughs it;
  * rock, marsh, water, land above 1,000 m and the managed forests are never farmed.
So the farmland's edges follow the land (the level ground, the forest's edge, the river, the rain), and villages
lie within it. The classes: d field, p pasture or hay meadow, o orchard, olive grove or vineyard, f wood, g open
grass or grazing, h scrub or heath, r rock, m marsh, s and w water. Deterministic: the only noise is a hash of the
cell (or of a block of 2 x 2 cells: a paddock).
"""
import math
import os
import struct
import zlib

CLASSES = "swdfghrm"           # the terrain's cover classes (tools/terrain_lib.py), by number
MAX_FARM_M = 1000              # nothing is farmed above this height
# how far from a town, a village or a road the land of each way of farming is worked (km)
REACH = {"valley": 9.0, "mixed": 8.0, "dryland": 10.0, "wheat": 14.0, "pastoral": 22.0, "cotton": 7.0, "gardens": 3.0}


def region(cty, z, rain, river_km):
    """The way of farming of a cell, from its country, height, rain and distance to the main river (km)."""
    if cty == "U":
        if river_km < 9 and z < 400:
            return "valley"
        return "mixed" if rain >= 880 else "dryland"
    if cty == "B":
        return "wheat" if rain >= 540 else "pastoral"
    if cty == "L":
        return "cotton" if rain < 1150 else "gardens"
    return None


def use(reg, c, s, sun, d, r, h1, h2, hb, flood):
    """The use of a cell: its region, natural class c, slope s, whether it faces the sun, the distance d (km) to
    the nearest town, village or road and the region's reach r, hashes h1, h2 of the cell and hb of its paddock (a
    block of 2 x 2 cells), whether it lies on the river's flood plain. None keeps the natural cover."""
    near = d < .5 * r
    if reg == "valley":
        if flood:
            return "p"                                   # flood meadows: the villages stand on the terraces above
        if s >= .2 or (c == "f" and h1 < .4):
            return "f"
        if s < .045:
            return "d" if h2 < .82 else "p"
        if sun and s < .18:
            return "o" if h2 < .75 else "p"
        return "p" if s < .15 else "f"
    if reg == "mixed":
        if c == "f" and not (near and s < .08 and h1 < .35):
            return "f"
        if s >= .17:
            return "f"
        if s < .06:
            return "d" if h2 < .6 else "p" if h2 < .88 else "o"
        return "o" if near and h2 < .12 else "p"
    if reg == "dryland":
        if s >= .18 or c == "f":
            return None
        if s < .06:
            return "d" if h2 < .78 else "g"
        if sun and s < .16 and h2 < .5:
            return "o"
        return "p" if near and s < .12 else "g"
    if reg == "wheat":
        if c == "f" or s >= .14:
            return None
        if s < .045 and c in "dg" and hb < (.85 if c == "d" else .35):
            return "d"                                   # wheat paddocks of 2 x 2 cells (1.75 km)
        return "g"
    if reg == "pastoral":
        if c == "f" or s >= .12:
            return None
        if d < 2.5 and s < .04 and hb < .5:
            return "d"                                   # the home paddocks: hay, lucerne, the garden
        return "g"
    if reg == "cotton":
        if s < .07 and c in "dg":
            return "d"
        return "p" if s < .16 and c != "f" else None
    if reg == "gardens":
        if s >= .22 or (c == "f" and d > 1.5):
            return None
        return "o" if h2 < .5 else "p"
    return None


def hsh(x, y, salt=0):
    h = (x * 374761393 + y * 668265263 + salt * 1442695041) & 0xFFFFFFFF
    h = ((h ^ (h >> 13)) * 1274126177) & 0xFFFFFFFF
    return ((h ^ (h >> 16)) & 0xFFFFFFFF) / 4294967295


def read_png(path):
    """A greyscale PNG (8 or 16 bit, not interlaced) as (width, height, flat list of values): with Pillow if it is
    there, else with the standard library (the same values)."""
    try:
        from PIL import Image
        im = Image.open(path)
        return im.size[0], im.size[1], list(im.getdata())
    except ImportError:
        pass
    data = open(path, "rb").read()
    k, idat = 8, b""
    while k < len(data):
        n, = struct.unpack(">I", data[k:k + 4])
        kind = data[k + 4:k + 8]
        body = data[k + 8:k + 8 + n]
        if kind == b"IHDR":
            w, h, depth, ctype, _, _, inter = struct.unpack(">IIBBBBB", body)
            if ctype != 0 or inter or depth not in (8, 16):
                raise ValueError(f"{path}: only greyscale 8 or 16 bit, not interlaced")
        elif kind == b"IDAT":
            idat += body
        k += 12 + n
    raw = zlib.decompress(idat)
    bpp = depth // 8
    stride = w * bpp
    prev = bytearray(stride)
    out = []
    pos = 0
    for _ in range(h):
        f = raw[pos]
        line = bytearray(raw[pos + 1:pos + 1 + stride])
        pos += 1 + stride
        if f == 1:
            for i in range(bpp, stride):
                line[i] = (line[i] + line[i - bpp]) & 255
        elif f == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 255
        elif f == 3:
            for i in range(stride):
                line[i] = (line[i] + ((line[i - bpp] if i >= bpp else 0) + prev[i]) // 2) & 255
        elif f == 4:
            for i in range(stride):
                a = line[i - bpp] if i >= bpp else 0
                b, c = prev[i], prev[i - bpp] if i >= bpp else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        out.extend(line if bpp == 1 else [line[i] << 8 | line[i + 1] for i in range(0, stride, 2)])
        prev = line
    return w, h, out


def access(terrain, world, W, H):
    """The distance (km) from every square's centre to the nearest town or village (its built-up area) or road
    square, over the squares (a chamfer distance: 3.5 km a side step, 4.95 km a diagonal one)."""
    INF = 1e9
    D = [[INF] * H for _ in range(W)]
    for r in world.get("routes", []):
        if r["mode"] == "road":
            for i, j in r["pts"]:
                D[i][j] = 0.0
    for t in world.get("towns", []) + world.get("localities", []) + world.get("villages", []):
        i, j = t["c"]
        D[i][j] = 0.0
        rr = int(t["built_km"] / 7)
        for a in range(-rr, rr + 1):
            for b in range(-rr, rr + 1):
                if 0 <= i + a < W and 0 <= j + b < H and math.hypot(a, b) <= rr:
                    D[i + a][j + b] = 0.0
    k1, k2 = 3.5, 3.5 * math.sqrt(2)
    for i in range(W):
        for j in range(H):
            v = D[i][j]
            if i:
                v = min(v, D[i - 1][j] + k1, D[i - 1][j - 1] + k2 if j else INF, D[i - 1][j + 1] + k2 if j + 1 < H else INF)
            if j:
                v = min(v, D[i][j - 1] + k1)
            D[i][j] = v
    for i in range(W - 1, -1, -1):
        for j in range(H - 1, -1, -1):
            v = D[i][j]
            if i + 1 < W:
                v = min(v, D[i + 1][j] + k1, D[i + 1][j + 1] + k2 if j + 1 < H else INF, D[i + 1][j - 1] + k2 if j else INF)
            if j + 1 < H:
                v = min(v, D[i][j + 1] + k1)
            D[i][j] = v
    return D


def land_use(root, terrain, world, keep_squares=(), W=256, H=192):
    """The land use per cell of each of the terrain's cover rasters: {raster name: (x0, y0, cells per square,
    width, height, list of rows of class letters "swdfghrmpo")}. keep_squares: squares whose cover stays as it is
    (the managed forests)."""
    keep = set(map(tuple, keep_squares))
    D = access(terrain, world, W, H)
    river = {}
    for x, y, lv in terrain["river"]:
        river[(x, y)] = min(lv, river.get((x, y), 1e9))
    # the distance from every square to the main river (squares), for the valley
    RD = {}
    frontier = list(river)
    for q in frontier:
        RD[q] = 0
    k = 0
    while k < len(frontier):
        q = frontier[k]
        k += 1
        if RD[q] >= 4:
            continue
        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            y = (q[0] + a, q[1] + b)
            if y not in RD:
                RD[y] = RD[q] + 1
                frontier.append(y)
    country = terrain["country"]
    result = {}
    for name, r in terrain["rasters"].items():
        w, h, cov = read_png(os.path.join(root, r["cover"]))
        _, _, hgt = read_png(os.path.join(root, r["height"]))
        _, _, rain = read_png(os.path.join(root, r["rain"]))
        S, x0, y0, cell = r["cells_per_square"], r["x0"], r["y0"], r["cell_m"]
        off = r["offset_m"]
        rows = []
        for y in range(h):
            row = []
            for x in range(w):
                c = CLASSES[cov[y * w + x]]
                if c in "swrm":
                    row.append(c)
                    continue
                sq = (x0 + x // S, y0 + y // S)
                z = hgt[y * w + x] - off
                new = None
                if z < MAX_FARM_M and sq not in keep:
                    # the distance to the people who farm it: interpolated between the squares' centres
                    fx, fy = x0 + (x + .5) / S - .5, y0 + (y + .5) / S - .5
                    i0, j0 = int(math.floor(fx)), int(math.floor(fy))
                    u, v = fx - i0, fy - j0
                    i1, j1 = min(W - 1, i0 + 1), min(H - 1, j0 + 1)
                    d = (D[i0][j0] * (1 - u) * (1 - v) + D[i1][j0] * u * (1 - v) + D[i0][j1] * (1 - u) * v
                         + D[i1][j1] * u * v)
                    reg = region(country[sq[1]][sq[0]], z, rain[y * w + x], RD.get(sq, 9) * 3.5)
                    gxc, gyc = x0 * S + x, y0 * S + y
                    if reg and d < REACH[reg] * (.7 + .6 * hsh(gxc // 2, gyc // 2, 4)):    # a ragged edge
                        xl, xr = max(0, x - 1), min(w - 1, x + 1)
                        yt, yb = max(0, y - 1), min(h - 1, y + 1)
                        gx = (hgt[y * w + xr] - hgt[y * w + xl]) / ((xr - xl) * cell)
                        gy = (hgt[yb * w + x] - hgt[yt * w + x]) / ((yb - yt) * cell)
                        s = math.hypot(gx, gy)
                        sun = gy > .02 and gy > .5 * abs(gx)        # rises to the south: faces north, to the sun
                        flood = RD.get(sq) is not None and RD[sq] <= 1 and any(
                            (sq[0] + a, sq[1] + b) in river and z < river[(sq[0] + a, sq[1] + b)] + 6
                            for a in (-1, 0, 1) for b in (-1, 0, 1))
                        new = use(reg, c, s, sun, d, REACH[reg], hsh(gxc, gyc, 1), hsh(gxc, gyc, 2),
                                  hsh(gxc // 2, gyc // 2, 3), flood)
                        if new == "f" and c == "h":
                            new = "h"
                if new is None:
                    new = "g" if c == "d" else c
                row.append(new)
            rows.append("".join(row))
        result[name] = (x0, y0, S, w, h, rows)
    return result


TILE_KIND = {"p": "g", "o": "d"}                 # the kind of a square holding these: grass, field


def tiles(result, W, H):
    """Per square: the string of its cells' land use (S x S characters, the cell at a along x and b along y at
    index a * S + b, as the model's sub-squares) and its kind (the most common kind of its land cells, pasture
    counted as grass and orchards as fields). Returns {(i, j): (lu, kind)} for the squares the rasters cover."""
    out = {}
    for x0, y0, S, w, h, rows in result.values():
        for b in range(h // S):
            for a in range(w // S):
                cells = [rows[b * S + v][a * S + u] for u in range(S) for v in range(S)]
                land = [TILE_KIND.get(c, c) for c in cells if c not in "sw"]
                kind = max(sorted(set(land)), key=land.count) if land else None
                out[(x0 + a, y0 + b)] = ("".join(cells), kind)
    return out
