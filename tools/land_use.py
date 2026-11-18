#!/usr/bin/env python3
"""The land use of the world (O152, owner 2026-11-18): who farms the land, and how, from the towns and villages of
the map. Standard library only (Pillow, when present, only reads the rasters faster); tools/world_model.py calls
it, and the model's tiles carry the result ("lu", "k"), which the 3D map and the printed sheet both draw.

The terrain (tools/terrain.py) gives the natural cover of every cell of 875 m (437.5 m on Lisavu): forest, grass,
scrub and heath, rock, marsh, and "field" for open, level, well-watered land that could be ploughed. Nobody farms
it there unless a settlement does:

  * every town and village of the map (world/map.json "towns", "localities", "villages") farms the land within its
    reach, in its way of farming ("farming"); a cell belongs to the settlement whose reach it lies deepest in (the
    distance divided by the reach), so neighbouring villages share the land between them;
  * within a settlement's reach, the farming decides each cell from its slope, its height, the side it faces (in
    the southern hemisphere a slope facing north gets the sun) and how far it lies from the settlement (FARMING
    below): fields ("d"), pasture and hay meadows with hedges ("p"), orchards, olive groves and vineyards ("o"),
    woodland kept for fuel and timber ("f"), and open grazing ("g") where the stock runs on the natural grass;
  * rock, marsh, water, land above 1,000 m and the managed forests keep their natural cover;
  * outside every reach the natural cover stays, and land the terrain marks as "field" is open grassland ("g"):
    no one ploughs it.

The density of the villages (dense in the wet west and the valley, far apart on the dry east and the plateau) is
the map's; the reach of each way of farming follows it: small fields and woods close round the old Urvanian
villages, big wheat paddocks and open runs round the British-era stations. Deterministic: the only noise is a hash
of the cell.
"""
import math
import os
import struct
import zlib

CLASSES = "swdfghrm"           # the terrain's cover classes (tools/terrain_lib.py), by number
# What a cell can become: d field, p pasture or hay meadow, o orchard, olive grove or vineyard, f woodland, g open
# grazing; "keep" leaves the natural cover. Per way of farming: reach (km, for a village of the middle band), and
# the rule, a function of (slope, sunny, dist_km, reach_km, h1, h2, natural class) -> class or None (keep the
# natural cover); h1 and h2 are hashes of the cell (0..1), for the mix of uses.


def _mixed(s, sun, d, r, h1, h2, c):
    """The old Urvanian villages of the wet west: small fields on the level, hay meadows and pasture on the slopes,
    orchards by the village, chestnut and oak woods on the steep ground and in scattered woodlots."""
    if s >= .16 or h1 < .14 or (c == "f" and h1 < .5):
        return "f"
    if d < 1.6 and s < .12 and h2 < .35:
        return "o"
    if s < .06:
        return "d" if h2 < .72 else "p"
    return "p"


def _valley(s, sun, d, r, h1, h2, c):
    """The river valley: fields and market gardens on the valley floor, vineyards and orchards on the slopes that
    face the sun, meadows on the others, woods on the steep sides."""
    if s >= .2 or (c == "f" and h1 < .35):
        return "f"
    if s < .045:
        return "d" if h2 < .85 else "p"
    if sun and s < .18:
        return "o" if h2 < .8 else "p"
    return "p" if h1 > .1 else "f"


def _dryland(s, sun, d, r, h1, h2, c):
    """The drier Urvanian hills: wheat and barley on the level, olives and vines on the sunny slopes, enclosed
    pasture near the village and open sheep grazing further out; the steep ground left as it is."""
    if s >= .18 or (c == "f" and h1 < .4):
        return None
    if s < .06:
        return "d" if h2 < .8 else "g"
    if sun and s < .16 and h2 < .6:
        return "o"
    return "p" if d < .7 * r else "g"


def _wheat_sheep(s, sun, d, r, h1, h2, c):
    """Bayvarra's wheat-and-sheep land: big wheat paddocks on the level land near the village and the railway,
    sheep on open runs beyond; woods left standing away from the village."""
    if s < .05 and d < .65 * r and h1 < .78:
        return "d"
    if s >= .14 or (c == "f" and d > 2.5):
        return None
    return "g"


def _pastoral(s, sun, d, r, h1, h2, c):
    """The dry east's sheep and cattle stations: the home paddocks (hay, lucerne, the garden) by the homestead,
    open runs fenced into big paddocks beyond, where the stock grazes the natural grass and scrub."""
    if d < 2.2 and s < .05:
        return "d" if h2 < .7 else "p"
    return "g" if s < .12 and c != "f" else None


def _forestry(s, sun, d, r, h1, h2, c):
    """A forest village: clearings with meadows and gardens round it; the forest round them stays."""
    return "p" if d < .6 * r and s < .12 else None


def _cotton(s, sun, d, r, h1, h2, c):
    """Lisavu's lee side: cotton fields on the level dry land, gardens and pasture on the slopes."""
    if s < .07:
        return "d"
    if s < .16:
        return "p" if h2 < .7 else "o"
    return None


def _gardens(s, sun, d, r, h1, h2, c):
    """Lisavu's wet windward valleys: fruit and vegetable gardens close round the village, pasture beyond, the
    forest on the slopes."""
    if s >= .22:
        return None
    if d < 1.4:
        return "o"
    return "p" if s < .15 else None


def _fishing(s, sun, d, r, h1, h2, c):
    """A fishing village: gardens and a few small fields and paddocks behind the shore."""
    if s >= .15 or (c == "f" and d > 1.5):
        return None
    return "d" if s < .05 and h2 < .5 else "p"


def _market(s, sun, d, r, h1, h2, c):
    """A town's own hinterland: market gardens and dairy pasture that feed it."""
    if s >= .16:
        return None
    if s < .05:
        return "d" if h2 < .7 else "p"
    return "o" if sun and h2 < .4 else "p"


FARMING = {
    "mixed": (6.5, _mixed), "valley": (6.0, _valley), "dryland": (7.5, _dryland), "wheat-sheep": (11.0, _wheat_sheep),
    "pastoral": (16.0, _pastoral), "forestry": (3.0, _forestry), "cotton": (6.0, _cotton), "gardens": (3.5, _gardens),
    "fishing": (4.0, _fishing), "market": (8.0, _market),
}
BAND_REACH = {"small": .8, "middle": 1.0, "large": 1.2}     # a village's reach by its population band
MAX_FARM_M = 1000                                          # nothing is farmed above this height


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


def settlements(world):
    """The places that farm, with their way of farming and their reach in km."""
    out = []
    for t in world.get("towns", []) + world.get("localities", []) + world.get("villages", []):
        far = t.get("farming")
        if not far:
            continue
        reach = t.get("farm_km") or FARMING[far][0] * BAND_REACH.get(t.get("band", "middle"), 1.0)
        out.append((t["c"][0] + .5, t["c"][1] + .5, far, reach))
    return out


def land_use(root, terrain, world, keep_squares=()):
    """The land use per cell of each of the terrain's cover rasters: {raster name: (x0, y0, cells per square,
    width, height, list of rows of class letters "swdfghrmpo")}. keep_squares: squares whose cover stays as it is
    (the managed forests)."""
    places = settlements(world)
    keep = set(map(tuple, keep_squares))
    result = {}
    for name, r in terrain["rasters"].items():
        w, h, cov = read_png(os.path.join(root, r["cover"]))
        _, _, hgt = read_png(os.path.join(root, r["height"]))
        S, x0, y0, cell = r["cells_per_square"], r["x0"], r["y0"], r["cell_m"]
        off = r["offset_m"]
        km = cell / 1000
        # the places that can reach this raster, by the squares they reach
        near = {}
        for p in places:
            px, py = (p[0] - x0) * S, (p[1] - y0) * S          # in cells
            rc = p[3] / km
            if px < -rc or py < -rc or px > w + rc or py > h + rc:
                continue
            for bx in range(int((px - rc) // 16), int((px + rc) // 16) + 1):
                for by in range(int((py - rc) // 16), int((py + rc) // 16) + 1):
                    near.setdefault((bx, by), []).append((px, py, p[2], rc, p[3]))
        rows = []
        for y in range(h):
            row = []
            for x in range(w):
                c = CLASSES[cov[y * w + x]]
                if c in "swrm":
                    row.append(c)
                    continue
                z = hgt[y * w + x] - off
                best, bd = None, 1.0
                for px, py, far, rc, rkm in near.get((x // 16, y // 16), ()):
                    q = math.hypot(x + .5 - px, y + .5 - py) / rc
                    if q <= bd:
                        best, bd = (far, rkm, q * rkm), q
                new = None
                sq = (x0 + x // S, y0 + y // S)
                if best and z < MAX_FARM_M and sq not in keep:
                    far, rkm, dkm = best
                    xl, xr = max(0, x - 1), min(w - 1, x + 1)
                    yt, yb = max(0, y - 1), min(h - 1, y + 1)
                    gx = (hgt[y * w + xr] - hgt[y * w + xl]) / ((xr - xl) * cell)
                    gy = (hgt[yb * w + x] - hgt[yt * w + x]) / ((yb - yt) * cell)
                    s = math.hypot(gx, gy)
                    sun = gy > .02 and gy > .5 * abs(gx)            # rises to the south: faces north, to the sun
                    new = FARMING[far][1](s, sun, dkm, rkm, hsh(x0 * S + x, y0 * S + y, 1), hsh(x0 * S + x, y0 * S + y, 2), c)
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
