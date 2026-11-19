"""Draw the position of the UBL example world on a depth map of the South Atlantic, with the real zones and claims.

usage: python3 -I analysis/world-position/plot_world_position.py      (writes world-position.png next to this script)

Needs numpy, matplotlib, Pillow, shapely and pyproj. The world's land is drawn from the terrain in WGS 84
(world_outline.py: the coordinate rule of the examples), not as a box. The zones are the Marine Regions layers that
check_maritime_claims.py fetches into <repo>/.review/geo/ (not committed): the 200-nautical-mile zones (World EEZ
v12), the extended continental shelf claims (World Extended Continental Shelves v2) and the land; the International
Seabed Authority's terminated contract area on the Rio Grande Rise as the extent of its blocks.
The depth grid is NOAA ETOPO1 at 10 arc-minutes, fetched once from NOAA's ERDDAP server into
<repo>/.review/geo/etopo.csv:
https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?altitude[(-55):10:(-5)][(-65):10:(25)]
See README.md in this folder.
"""
import json
import math
import pathlib
import sys
import urllib.request

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.cm as cm  # noqa: E402
import matplotlib.colors as mc  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402
from PIL import Image  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import check_maritime_claims as cmc  # noqa: E402
import world_outline as wo  # noqa: E402

DATA = ROOT / ".review" / "geo" / "etopo.csv"
URL = "https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?altitude[(-55):10:(-5)][(-65):10:(25)]"
if not DATA.is_file():
    DATA.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(URL, DATA)
_d = np.genfromtxt(DATA, delimiter=",", skip_header=2)
lat = np.unique(_d[:, 0])
lon = np.unique(_d[:, 1])
Z = _d[:, 2].reshape(len(lat), len(lon))

INK = "#1f2933"
MUTED = "#5f6b7a"
ACC = "#c2410c"
LAND = "#d9d6cf"
EEZ = "#2b6f4e"
ECS = "#7a3e9d"
sea = LinearSegmentedColormap.from_list(
    "sea", ["#eef5fb", "#c9dff1", "#9cc3e3", "#6ba3d0", "#3f7fb8", "#225a94", "#123c6b"][::-1])
levels = [-7000, -5000, -4000, -3500, -3000, -2500, -2000, -1000, 0]

# the world: land masks and the country grid in WGS 84 (the coordinate rule is linear per area, so each raster is a
# regular longitude-latitude grid)
GEOG = json.loads((ROOT / "world" / "countries.json").read_text())["geography"]
TERRAIN = json.loads((ROOT / "world" / "terrain.json").read_text())
MASKS = []
for r in TERRAIN["rasters"].values():
    land_ = (np.array(Image.open(ROOT / r["cover"])).T != 0).astype(float)
    s = r["cells_per_square"]
    xs = r["x0"] + (np.arange(land_.shape[0]) + 0.5) / s - 0.5
    ys = r["y0"] + (np.arange(land_.shape[1]) + 0.5) / s - 0.5
    lo, _ = wo.to_wgs84(xs, np.full_like(xs, ys[0]), GEOG)
    _, la = wo.to_wgs84(np.full_like(ys, xs[0]), ys, GEOG)
    MASKS.append((lo, la, land_.T))
CTY = np.array([[1.0 if ch == "U" else 2.0 if ch == "B" else 0.0 for ch in row] for row in TERRAIN["country"]])
cx = np.arange(CTY.shape[1], dtype=float)
cy = np.arange(CTY.shape[0], dtype=float)
main_cols = cx < GEOG["insets"][0]["from_column"]
CLON, _ = wo.to_wgs84(cx[main_cols], np.full(main_cols.sum(), 94.0), GEOG)
_, CLAT = wo.to_wgs84(np.full_like(cy, 50.0), cy, GEOG)
CTY = CTY[:, main_cols]

# the zones, claims and land from Marine Regions (cached by check_maritime_claims.py)
EEZS = list(cmc.features("eez"))
ECSS = list(cmc.features("ecs"))
LANDS = cmc.land()


def polys(g):
    for p in getattr(g, "geoms", [g]):
        if p.geom_type == "Polygon":
            yield p


def base(ax, ext):
    ax.contourf(lon, lat, np.where(Z > 0, np.nan, Z), levels=levels, cmap=sea, extend="min")
    for g in LANDS:
        for p in polys(g):
            x, y = p.exterior.xy
            ax.fill(x, y, color=LAND, ec=MUTED, lw=0.4, zorder=2)
    ax.set_xlim(ext[0], ext[1])
    ax.set_ylim(ext[2], ext[3])
    ax.set_aspect(1 / np.cos(np.radians((ext[2] + ext[3]) / 2)))
    ax.tick_params(colors=MUTED, labelsize=8, length=2)
    for s_ in ax.spines.values():
        s_.set_color("#b8c0cc")
        s_.set_linewidth(0.6)
    ax.xaxis.set_major_formatter(lambda v, p: f"{abs(v):.0f}°{'W' if v < 0 else 'E' if v > 0 else ''}")
    ax.yaxis.set_major_formatter(lambda v, p: f"{abs(v):.0f}°{'S' if v < 0 else 'N' if v > 0 else ''}")


def zones(ax, lw=0.8):
    for props, g in EEZS:
        for p in polys(g):
            x, y = p.exterior.xy
            ax.fill(x, y, fc=EEZ, alpha=0.10, zorder=1.5)
            ax.plot(x, y, color=EEZ, lw=lw, ls=(0, (3, 2)), zorder=3)
    for props, g in ECSS:
        for p in polys(g):
            x, y = p.exterior.xy
            ax.fill(x, y, fc="none", ec=ECS, lw=lw, hatch="////", alpha=0.6, zorder=3)
    x0, x1, y0, y1 = cmc.ISA[0][2:6]
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc="none", ec=INK, lw=0.8, ls=(0, (1, 1.5)), zorder=4))


def world(ax, border=False):
    for lo, la, m in MASKS:
        ax.contourf(lo, la, m, levels=[0.5, 1.5], colors=[ACC], alpha=0.85, zorder=5)
        ax.contour(lo, la, m, levels=[0.5], colors=[ACC], linewidths=0.6, zorder=5)
    if border:
        ax.contour(CLON, CLAT, np.where(CTY == 0, np.nan, CTY), levels=[1.5], colors=["white"], linewidths=0.9,
                   linestyles=[(0, (3, 2))], zorder=6)


fig = plt.figure(figsize=(13, 13.2), dpi=200, facecolor="white")
ax = fig.add_axes([0.06, 0.50, 0.90, 0.45])
base(ax, (-60, 20, -48, -5))
zones(ax)
world(ax)
ax.set_title("Where the world lies: the high seas of the South Atlantic", loc="left", fontsize=14, color=INK, pad=10,
             fontweight="bold")
real = [("Tristan da Cunha", -12.3, -37.1, (6, -3)), ("Gough Island", -9.9, -40.3, (6, -3)),
        ("Saint Helena", -5.7, -15.95, (6, -3)), ("Ascension", -14.4, -7.95, (6, -3)),
        ("Trindade and Martim Vaz", -29.3, -20.5, (6, -3))]
for n, x, y, off in real:
    ax.annotate(n, (x, y), xytext=off, textcoords="offset points", fontsize=8.5, color=INK, zorder=7)
ax.text(-52, -14, "SOUTH AMERICA", fontsize=10, color=MUTED, ha="center")
ax.text(16.5, -21, "AFRICA", fontsize=10, color=MUTED, ha="center")
ax.annotate("Rio Grande Rise: Brazil's extended-shelf claim\n(hatched; CLCS submission of 2018, amended 2025)",
            (-31.0, -32.5), xytext=(-57, -44.5), fontsize=8.5, color=INK,
            arrowprops=dict(arrowstyle="-", color=INK, lw=0.8))
ax.annotate("Mainland: Urvania and Bayvarra,\non the Mid-Atlantic Ridge", (-15.0, -28.2), xytext=(-31, -12.5),
            fontsize=10, color=INK, fontweight="bold", arrowprops=dict(arrowstyle="-", color=INK, lw=0.8), va="top")
ax.annotate("Lisavu, on a seamount\nof the Walvis Ridge", (-2.65, -33.45), xytext=(3, -41.5), fontsize=10,
            color=INK, fontweight="bold", arrowprops=dict(arrowstyle="-", color=INK, lw=0.8), ha="center")
ax.text(4.5, -37.8, "Namibia and South Africa:\nextended-shelf claims (hatched)", fontsize=8, color=INK, ha="left")
ax.text(-12.3, -34.9, "200-nautical-mile zone", fontsize=7.5, color=EEZ, ha="center")

# close-up
ax2 = fig.add_axes([0.06, 0.085, 0.90, 0.37])
base(ax2, (-21, 4, -39.5, -26.5))
zones(ax2, lw=1.0)
world(ax2, border=True)
ax2.set_title("Close-up: the mainland and Lisavu at their true positions, and the nearest limits",
              loc="left", fontsize=14, color=INK, pad=10, fontweight="bold")
MAP = json.loads((ROOT / "world" / "map.json").read_text())
for t in MAP["towns"]:
    if t["name"] in ("Ferrano", "Lumeport", "Marrowdale", "Larkmouth", "Selanu"):
        x, y = wo.to_wgs84(np.array([float(t["c"][0])]), np.array([float(t["c"][1])]), GEOG)
        ax2.plot(x[0], y[0], "o", ms=4.5, mfc="white", mec=INK, mew=1.1, zorder=8)
        ax2.annotate(t["name"], (x[0], y[0]), xytext=(6, 3), textcoords="offset points", fontsize=8.5, color=INK,
                     zorder=8)
ax2.text(-16.6, -31.45, "URVANIA", fontsize=10, color="white", ha="center", fontweight="bold", zorder=8)
ax2.text(-13.6, -29.3, "BAYVARRA", fontsize=10, color="white", ha="center", fontweight="bold", zorder=8)
ax2.text(-2.65, -34.0, "LISAVU", fontsize=10, color=INK, ha="center", fontweight="bold", zorder=8)
ax2.annotate("Tristan da Cunha", (-12.3, -37.1), xytext=(7, -3), textcoords="offset points", fontsize=8.5,
             color=INK, zorder=8)
ax2.annotate("Gough Island", (-9.9, -40.3), xytext=(7, -3), textcoords="offset points", fontsize=8.5, color=INK)
# the shortest gaps to the Tristan da Cunha zone, measured (check_maritime_claims.py)
tristan = next(g for p, g in EEZS if p["territory1"] == "Tristan da Cunha")
coast = wo.coast_cells()
namibia = next(g for p, g in ECSS if p["territory1"] == "Namibia" and p["pol_type"] == "ECS CLCS Submission")
for area, zone, dx, dy in (("mainland", tristan, 0.2, 0), ("lisavu", tristan, 0.2, 0), ("lisavu", namibia, -0.6, 0.75)):
    km, p, q = cmc.distance((coast[area][0], coast[area][1]), zone)
    ax2.plot([p.x, q.x], [p.y, q.y], color=INK, lw=1.0, zorder=7)
    ax2.text((p.x + q.x) / 2 + dx, (p.y + q.y) / 2 + dy, f"{km:,.0f} km\n({km / 1.852:,.0f} nmi)", fontsize=8.5,
             color=INK, zorder=8, va="center")
ax2.text(-12.3, -35.4, "limit of the 200-nautical-mile zone of Tristan da Cunha", fontsize=7.5, color=EEZ,
         ha="center")
ax2.text(-0.9, -36.9, "limit of Namibia's\nextended-shelf claim\n(CLCS submission, 2009)", fontsize=7.5, color=ECS,
         ha="center")
km = 500 / (111.32 * np.cos(np.radians(27.2)))
ax2.plot([-20.4, -20.4 + km], [-27.2, -27.2], color=INK, lw=2)
ax2.text(-20.4 + km / 2, -26.95, "500 km", fontsize=8.5, color=INK, ha="center")

cax = fig.add_axes([0.16, 0.905, 0.20, 0.010])
cb = fig.colorbar(cm.ScalarMappable(norm=mc.BoundaryNorm(levels, sea.N), cmap=sea), cax=cax,
                  orientation="horizontal", ticks=[-5000, -4000, -3000, -2000, -1000, 0])
cb.ax.set_xticklabels(["5,000", "4,000", "3,000", "2,000", "1,000", "0"], fontsize=7.5, color=INK)
cb.outline.set_linewidth(0.4)
fig.text(0.16, 0.922, "Depth of the sea floor, metres", fontsize=8, color=INK, ha="left", va="center")
fig.text(0.06, 0.012,
         "Orange: the land of the fictional world from its terrain, placed by the coordinate rule of the examples "
         "(squares of 3.5 km; Lisavu around 33.0° S, 2.65° W). Green, dashed: 200-nautical-mile zones (Marine "
         "Regions,\nWorld EEZ v12). Purple, hatched: extended continental shelf claims (Marine Regions, World "
         "Extended Continental Shelves v2). Dotted box: the International Seabed Authority's former contract area "
         "on the Rio Grande Rise\n(CPRM, terminated 2022). Sea floor: NOAA ETOPO1 every 10 arc-minutes. Land: "
         "Marine Regions land polygons.", fontsize=7.5, color=MUTED)
fig.savefig(HERE / "world-position.png")
print("written", HERE / "world-position.png")
