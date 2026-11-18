#!/usr/bin/env python3
"""Make the world's terrain from its geology (O152), or check that the committed terrain is current.

Inputs:  world/terrain-inputs.json (the geology: coast outline, river axis, rift, basin, massif, Lisavu's volcano,
         the border line's anchors), this script and tools/terrain_lib.py (the method).
Outputs: world/terrain.json        per 3.5 km square of the world model's grid (256 x 192): the kind (s sea,
                                   w river or estuary water, d field, f forest, g grass/pasture, h scrub/heath/moor,
                                   r rock, m marsh), the country, the corner heights in metres, the main river's
                                   squares with their water level, the estuary's squares; the streams and the
                                   border line for the printed map; measures of the land;
         world/terrain/*.png       the fine rasters (875 m cells on the mainland, 437.5 m on Lisavu): height
                                   (16-bit, metres + 1000) and land cover (8-bit, the class numbers), for the sheet.
The world model (tools/world_model.py) and the site build read only the outputs: they need neither scipy nor numba.

Usage: python3 tools/terrain.py            generate (needs numpy, scipy, numba: pip install numpy scipy numba;
                                           about a minute)
       python3 tools/terrain.py --check    say whether the outputs were made from the current inputs and method
                                           (standard library only)
"""
import base64
import hashlib
import json
import os
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
INPUTS = os.path.join(ROOT, "world", "terrain-inputs.json")
OUT = os.path.join(ROOT, "world", "terrain.json")
RASTERS = os.path.join(ROOT, "world", "terrain")
SOURCES = [INPUTS, os.path.join(os.path.dirname(__file__), "terrain.py"), os.path.join(os.path.dirname(__file__), "terrain_lib.py")]
OFFSET_M = 1000                                     # the height rasters hold metres + OFFSET_M


def fingerprint():
    h = hashlib.sha256()
    for p in SOURCES:
        h.update(open(p, "rb").read().replace(b"\r\n", b"\n"))
    return h.hexdigest()


def check():
    if not os.path.exists(OUT):
        sys.exit("world/terrain.json is missing: run python3 tools/terrain.py")
    have = json.load(open(OUT, encoding="utf-8")).get("made_from")
    if have != fingerprint():
        sys.exit("world/terrain.json is not current (world/terrain-inputs.json, tools/terrain.py or tools/terrain_lib.py "
                 "changed): run python3 tools/terrain.py (needs numpy, scipy, numba)")
    for name in ("mainland-height.png", "mainland-cover.png", "lisavu-height.png", "lisavu-cover.png"):
        if not os.path.exists(os.path.join(RASTERS, name)):
            sys.exit(f"world/terrain/{name} is missing: run python3 tools/terrain.py")
    print("world/terrain.json is current")


def generate():
    import numpy as np
    from PIL import Image
    from scipy import ndimage
    # tools/ holds a coverage.py that would shadow the package numba imports: load the library by its path
    here = os.path.abspath(os.path.dirname(__file__))
    sys.path[:] = [p for p in sys.path if os.path.abspath(p or ".") != here]
    import importlib.util
    spec = importlib.util.spec_from_file_location("terrain_lib", os.path.join(here, "terrain_lib.py"))
    T = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(T)
    inp = json.load(open(INPUTS, encoding="utf-8"))
    log = lambda s: print(s, file=sys.stderr)
    W, H = 256, 192
    log("mainland ...")
    md = T.mainland(inp, log)
    log("Lisavu ...")
    ld = T.lisavu(inp, log)
    lcm, lcl = T.cover(md), T.cover(ld, island=True)
    km, cm = T.tiles(md, lcm, W, H)
    kl, cl = T.tiles(ld, lcl, W, H)
    kinds = np.where(kl >= 0, kl, np.where(km >= 0, km, T.SEA))
    corners = np.where(~np.isnan(cl), cl, np.where(~np.isnan(cm), cm, 0.0))
    # the estuary: squares that are mostly estuary water
    S, X0, Y0 = md['S'], md['X0'], md['Y0']
    ny, nx = md['z'].shape
    est = md['estuary'].reshape(ny // S, S, nx // S, S).mean(axis=(1, 3)) > 0.5
    until = inp["mainland"]["river_axis"]["estuary_until_x"]
    estuary = [(X0 + b, Y0 + a) for a, b in zip(*np.where(est)) if kinds[Y0 + a, X0 + b] == T.SEA and X0 + b < until]
    # the main river
    river = T.river_tiles(md, kinds)
    for x, y, _ in river:
        kinds[y, x] = T.WATER
    for x, y in estuary:
        kinds[y, x] = T.WATER
    # sea corners at 0: every corner that touches a sea square
    seat = kinds == T.SEA
    touch = np.zeros((H + 1, W + 1), bool)
    touch[:-1, :-1] |= seat; touch[1:, :-1] |= seat; touch[:-1, 1:] |= seat; touch[1:, 1:] |= seat
    corners[touch] = 0
    for x, y in estuary:
        corners[y:y + 2, x:x + 2] = 0
    # countries: Lisavu; on the mainland the border along the high ground north of the crossing, the river below it
    east, crossing = T.border(md, inp, log)
    country = np.full((H, W), ".")
    landc = ~md['sea']
    eb = east.reshape(ny // S, S, nx // S, S).sum(axis=(1, 3)) / np.maximum(1, landc.reshape(ny // S, S, nx // S, S).sum(axis=(1, 3)))
    land_t = kinds != T.SEA
    for a in range(ny // S):
        for b in range(nx // S):
            if land_t[Y0 + a, X0 + b]:
                country[Y0 + a, X0 + b] = "B" if eb[a, b] > 0.5 else "U"
    country[:, 200:][land_t[:, 200:]] = "L"
    # the land south of the river from the crossing to the sea is Urvania (the river is the border there)
    # (the watershed rule already gives it: Bayvarra is only what drains north of the river)
    # the rasters for the sheet
    os.makedirs(RASTERS, exist_ok=True)
    rasters = {}
    for name, d, lc in (("mainland", md, lcm), ("lisavu", ld, lcl)):
        hgt = np.clip(np.round(d['z']) + OFFSET_M, 0, 65535).astype(np.uint16)
        Image.fromarray(hgt).save(os.path.join(RASTERS, f"{name}-height.png"), optimize=True)
        Image.fromarray(lc.astype(np.uint8)).save(os.path.join(RASTERS, f"{name}-cover.png"), optimize=True)
        rasters[name] = {"height": f"world/terrain/{name}-height.png", "cover": f"world/terrain/{name}-cover.png",
                         "x0": int(d['X0']), "y0": int(d['Y0']), "cells_per_square": int(d['S']),
                         "cell_m": d['cell'], "offset_m": OFFSET_M}
    # measures
    def extent(d):
        land = ~d['sea']
        lab, n = ndimage.label(land)
        sizes = ndimage.sum(land, lab, range(1, n + 1))
        main = lab == 1 + np.argmax(sizes)
        xs, ys = d['X'][main], d['Y'][main]
        a2 = (d['cell'] / 1000) ** 2
        return {"west_east_km": round(float((xs.max() - xs.min() + 1 / d['S']) * T.KM)),
                "north_south_km": round(float((ys.max() - ys.min() + 1 / d['S']) * T.KM)),
                "area_km2": round(float(main.sum() * a2)), "islets": int(n - 1),
                "highest_m": round(float(d['z'].max())),
                "highest_at": [round(float(d['X'].flat[np.argmax(d['z'])]), 1), round(float(d['Y'].flat[np.argmax(d['z'])]), 1)]}
    meas = {"mainland": extent(md), "lisavu": extent(ld)}
    for c, n in (("U", "XU"), ("B", "XB"), ("L", "XL")):
        meas[n + "_km2_by_squares"] = int((country == c).sum() * T.KM ** 2)
    stem = md['stem']
    meas["river_km"] = round(float(sum(np.hypot(*(stem[k] - stem[k - 1])) for k in range(1, len(stem))) * md['cell'] / 1000))
    meas["river_basin_km2"] = round(float(md['akm2'][tuple(stem[-1])]))
    meas["river_source_m"] = round(float(md['z'][tuple(stem[0])]))
    coast = (~ld['sea']) & ndimage.binary_dilation(ld['sea'], structure=np.ones((3, 3), bool))
    wc = coast & (ld['west'] > 0.5) & ~ld['faja'] & ~ld['stacks']
    hc = ndimage.maximum_filter(ld['z'], 3)[wc]
    meas["lisavu_west_cliffs_m"] = {"median": round(float(np.median(hc))), "p10": round(float(np.percentile(hc, 10))),
                                    "p90": round(float(np.percentile(hc, 90))), "max": round(float(hc.max()))}
    for k, v in meas.items():
        log(f"{k}: {v}")
    cint = np.round(corners).astype("<i2")
    out = {
        "description": "The world's terrain, made by tools/terrain.py from world/terrain-inputs.json (O152): per 3.5 km "
                       "square of the world model's grid the kind and the country, per square corner the height in "
                       "metres, the main river's squares with their water level (source to mouth) and the estuary's "
                       "squares; the border crossing on the river; streams for the printed map; the fine rasters in world/terrain/. "
                       "Do not edit: change the inputs and run the script.",
        "made_from": fingerprint(),
        "W": W, "H": H, "km": T.KM,
        "kinds": {"s": "sea", "w": "river or estuary water", "d": "field", "f": "forest", "g": "grass, pasture",
                  "h": "scrub, heath, moor", "r": "bare rock, scree, cliff", "m": "marsh, salt meadow"},
        "kind": ["".join(T.KIND[k] for k in kinds[j]) for j in range(H)],
        "country": ["".join(country[j]) for j in range(H)],
        "corners_m": {"rows": H + 1, "cols": W + 1, "int16_le_base64": base64.b64encode(cint.tobytes()).decode()},
        "river": [[int(x), int(y), round(float(lv))] for x, y, lv in river],
        "estuary": sorted([[int(x), int(y)] for x, y in estuary]),
        "crossing": crossing,
        "streams": {"mainland": T.streams(md, 150, 2), "lisavu": T.streams(ld, 25, 2)},
        "rasters": rasters,
        "measures": meas,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")
    log(f"wrote {OUT} and world/terrain/*.png")


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    else:
        generate()
