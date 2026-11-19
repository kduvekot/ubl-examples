"""The coast of the UBL example world in WGS 84, from the terrain (world/terrain.json and world/terrain/*-cover.png).

Every cell of the terrain's fine rasters that is not sea (cover class 0) is land; its position follows the rule the
examples use for coordinates (`coordinate()` in tools/build_examples.py, world/countries.json `geography`): squares
of km_per_tile on both axes around the centre of their area, a degree of latitude 111.0 km, a degree of longitude
111.32 km times the cosine of the area's centre latitude; Lisavu (from its inset's first column) around its own true
centre. A square's number is taken as its centre, so positions are good to about half a square (1.75 km).

    land_cells()  -> {"mainland": (lon, lat, cell_km), "lisavu": (...)}: every land cell (degrees, east and north positive)
    coast_cells() -> the same, only the land cells next to the sea (the coast, islets included)
Needs numpy and Pillow; run from the repository root or anywhere (paths are taken from this file).
"""
import json
import math
import pathlib

import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[2]


def _geography():
    return json.loads((ROOT / "world" / "countries.json").read_text())["geography"]


def to_wgs84(x, y, g=None):
    """Map square (x, y), fractional, to (longitude, latitude) in degrees, east and north positive."""
    g = g or _geography()
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    lon = np.empty_like(x)
    lat = np.empty_like(y)
    areas = [g["mainland"]] + list(g.get("insets", []))
    for k, area in enumerate(areas):
        if k == 0:
            sel = np.ones(x.shape, bool)
            for a in areas[1:]:
                sel &= x < a["from_column"]
        else:
            sel = x >= area["from_column"]
        (ci, cj), c = area["centre_tile"], area["centre"]
        lat_c, lon_c = c["latitude_south"], c["longitude_west"]
        lat[sel] = -(lat_c + g["km_per_tile"] * (y[sel] - cj) / 111.0)
        lon[sel] = -(lon_c - g["km_per_tile"] * (x[sel] - ci) / (111.32 * math.cos(math.radians(lat_c))))
    return lon, lat


def _cells(coast_only):
    g = _geography()
    terrain = json.loads((ROOT / "world" / "terrain.json").read_text())
    out = {}
    for name, r in terrain["rasters"].items():
        cover = np.array(Image.open(ROOT / r["cover"])).T          # [x][y]
        land = cover != 0
        if coast_only:
            pad = np.pad(land, 1, constant_values=False)
            inner = pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:]
            land = land & ~inner
        i, j = np.nonzero(land)
        s = r["cells_per_square"]
        lon, lat = to_wgs84(r["x0"] + (i + 0.5) / s - 0.5, r["y0"] + (j + 0.5) / s - 0.5, g)
        out[name] = (lon, lat, r["cell_m"] / 1000.0)
    return out


def land_cells():
    return _cells(False)


def coast_cells():
    return _cells(True)


if __name__ == "__main__":
    for name, (lon, lat, km) in land_cells().items():
        print(f"{name}: {lon.size} land cells of {km} km, {lon.size * km * km:,.0f} km²; "
              f"{-lat.max():.2f} to {-lat.min():.2f} S, {-lon.min():.2f} to {-lon.max():.2f} W")
