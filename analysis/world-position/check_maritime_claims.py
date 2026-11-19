"""Open point O55: does the UBL example world lie on the high seas, clear of every real zone, claim and licence?

usage: python3 -I analysis/world-position/check_maritime_claims.py      (from the repository root)

Needs numpy, Pillow, shapely and pyproj. Prints, for the mainland and for Lisavu, whether any part of the land lies
inside a zone, and the shortest distance (geodesic on WGS 84) from the coast to each zone's limit and to real land.

The world's coast comes from the terrain (world_outline.py). The zones are fetched once into <repo>/.review/geo/
(not committed) from the Marine Regions web feature service (Flanders Marine Institute, VLIZ):
  * MarineRegions:eez        World EEZ v12 (2023-10-25): 200-nautical-mile zones and the limits declared by states
  * MarineRegions:ecs        World Extended Continental Shelves v2 (2024-10-10): CLCS submissions, recommendations,
                             deposits
  * MarineRegions:high_seas  World High Seas v2 (2024-10-10)
  * MarineRegions:land_v9    land polygons (cut here to the South Atlantic and saved as land-south-atlantic.json)
Brazil's amended executive summary of 12 March 2025 (second version, Oriental and Meridional Margins) is newer than
the Marine Regions ECS layer: its 2,173 outer-limit points are read from the UN DOALOS PDF with pdftotext (if
installed). The International Seabed Authority's exploration areas in the Atlantic are entered below as the extents
of their block coordinates, read from the ISA documents named beside them (a box is nearer than the blocks, so the
distance is a lower bound).
See README.md in this folder ("Sources and limits").
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.request

import numpy as np
from pyproj import Geod
from shapely.geometry import MultiPoint, Point, box, shape
from shapely.ops import nearest_points, unary_union
from shapely.prepared import prep

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import world_outline  # noqa: E402

GEO = HERE.parents[1] / ".review" / "geo"
WFS = ("https://geo.vliz.be/geoserver/MarineRegions/wfs?service=WFS&version=1.0.0&request=GetFeature"
       "&typeName=MarineRegions:{layer}&outputFormat=application/json&bbox=-75,-62,35,5")
BRA_2025 = ("https://www.un.org/depts/los/clcs_new/submissions_files/bra02_rev18/"
            "BR-OMM-2ndVER-ExecutiveSummary.pdf")
UK_DEPOSIT = ("https://www.un.org/depts/los/LEGISLATIONANDTREATIES/PDFFILES/DEPOSIT/"
              "GBR_{name}_EEZ_geographical_coordinates.pdf")
UK_ZONES = {"Tristan_da_Cunha": "Tristan da Cunha", "St_Helena": "Saint Helena", "Ascension": "Ascension"}
REGION = box(-75, -62, 35, 5)
NM = 1.852
G = Geod(ellps="WGS84")

# ISA exploration contracts in the Atlantic (isa.org.jm/exploration-contracts/, read 2026-11-19): (name, status,
# lon_min, lon_max, lat_min, lat_max, source)
ISA = [
    ("ISA: CPRM (Brazil), cobalt-rich crusts, Rio Grande Rise", "contract 9 Nov 2015, voluntarily terminated 27 Jun 2022",
     -36.52, -32.82, -32.04, -29.82,
     "https://www.isa.org.jm/wp-content/uploads/2022/10/CPRMTemplate_Final4_0.pdf"),
    ("ISA: Russian Federation, sulphides, Mid-Atlantic Ridge", "contract 29 Oct 2012 to 28 Oct 2027",
     -46.73, -44.65, 12.81, 20.91, "https://www.isa.org.jm/wp-content/uploads/2022/06/isba-17c-12_0.pdf"),
    ("ISA: Ifremer (France), sulphides, Mid-Atlantic Ridge", "contract 18 Nov 2014 to 17 Nov 2029",
     -46.42, -44.64, 21.01, 26.25,
     "https://www.isa.org.jm/wp-content/uploads/2022/10/Public-information-on-contracts-Ifremer_PMS.pdf"),
    ("ISA: Poland, sulphides, Mid-Atlantic Ridge", "contract 12 Feb 2018 to 11 Feb 2033",
     -45.0, -38.0, 26.15, 32.84, "https://isa.org.jm/wp-content/uploads/2022/06/isba-23c-11_1.pdf"),
]


def fetch(name, url):
    path = GEO / name
    if not path.is_file():
        GEO.mkdir(parents=True, exist_ok=True)
        print("fetching", url, file=sys.stderr)
        urllib.request.urlretrieve(url, path)
    return path


def features(layer):
    data = json.loads(fetch(f"mr-{layer}.json", WFS.format(layer=layer)).read_text())
    for f in data["features"]:
        g = shape(f["geometry"])
        if g.intersects(REGION):
            yield f["properties"], g.intersection(REGION)


def land():
    path = GEO / "land-south-atlantic.json"
    if not path.is_file():
        raw = fetch("mr-land_v9.json", WFS.format(layer="land_v9"))
        parts = []
        for f in json.loads(raw.read_text())["features"]:
            g = shape(f["geometry"]).intersection(REGION)
            parts += list(getattr(g, "geoms", [g]))
        path.write_text(json.dumps([p.__geo_interface__ for p in parts if not p.is_empty]))
        raw.unlink()
    return [shape(p) for p in json.loads(path.read_text())]


def brazil_2025():
    pdf = fetch("BR-OMM-2ndVER-ExecutiveSummary.pdf", BRA_2025)
    if not shutil.which("pdftotext"):
        return None
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    pts = [(float(a), float(b)) for a, b in
           re.findall(r"^\s*\d{4}-BR-OMM-OL-REV2024\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)", text, re.M)]
    return MultiPoint(pts) if pts else None


def uk_deposits():
    """The outer limits of the EEZs of Tristan da Cunha, St Helena and Ascension as the United Kingdom deposited them
    with the UN Secretary-General (M.Z.N.150.2019.LOS, 6 December 2019; Legal Notices 1, 2 and 16 of 2017)."""
    if not shutil.which("pdftotext"):
        return []
    out = []
    for name, label in UK_ZONES.items():
        pdf = fetch(f"GBR_{name}_EEZ.pdf", UK_DEPOSIT.format(name=name))
        text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
        pts = [(-(int(c) + float(d) / 60) if w == "W" else int(c) + float(d) / 60,
                -(int(a) + float(b) / 60) if ns == "S" else int(a) + float(b) / 60)
               for a, b, ns, c, d, w in re.findall(r"(\d{2})-(\d{2}\.\d+)([NS])\s+(\d{3})-(\d{2}\.\d+)([EW])", text)]
        if pts:
            out.append((f"{label}: EEZ outer limit as deposited by the United Kingdom (M.Z.N.150.2019.LOS)",
                        "200NM, official deposit", MultiPoint(pts)))
    return out


def distance(coast, geom):
    """Shortest geodesic distance (km) from the coast points to geom, and the two points."""
    lon, lat = coast
    pts = MultiPoint(np.column_stack([lon, lat]))
    a, b = nearest_points(pts, geom.boundary if geom.geom_type.endswith("Polygon") else geom)
    # refine on the ellipsoid around the planar nearest pair: the 200 coast points nearest to b
    d = np.hypot((lon - b.x) * np.cos(np.radians(b.y)), lat - b.y)
    best = None
    for k in np.argsort(d)[:200]:
        p = Point(lon[k], lat[k])
        q = nearest_points(p, geom.boundary if geom.geom_type.endswith("Polygon") else geom)[1]
        km = G.inv(p.x, p.y, q.x, q.y)[2] / 1000
        if best is None or km < best[0]:
            best = (km, p, q)
    return best


def inside(cells, geom):
    pg = prep(geom)
    lon, lat = cells
    step = max(1, lon.size // 20000)
    return any(pg.contains(Point(x, y)) for x, y in zip(lon[::step], lat[::step]))


def document_points():
    """Every LocationCoordinate in the examples (world/examples/*/*.xml), as (longitude, latitude) arrays."""
    import xml.etree.ElementTree as ET
    pts = set()
    for f in sorted((HERE.parents[1] / "world" / "examples").glob("*/*.xml")):
        for loc in ET.parse(f).iter():
            if not loc.tag.endswith("}LocationCoordinate"):
                continue
            v = {c.tag.split("}")[1]: c.text for c in loc}
            la = float(v["LatitudeDegreesMeasure"]) + float(v["LatitudeMinutesMeasure"]) / 60
            lo = float(v["LongitudeDegreesMeasure"]) + float(v["LongitudeMinutesMeasure"]) / 60
            pts.add((-lo if v["LongitudeDirectionCode"] == "West" else lo,
                     -la if v["LatitudeDirectionCode"] == "South" else la))
    pts = sorted(pts)
    return np.array([p[0] for p in pts]), np.array([p[1] for p in pts])


def all_inside(cells, geom):
    pg = prep(geom)
    return all(pg.contains(Point(x, y)) for x, y in zip(*cells))


def main():
    coast = {k: (v[0], v[1]) for k, v in world_outline.coast_cells().items()}
    cells = {k: (v[0], v[1]) for k, v in world_outline.land_cells().items()}
    coast["document coordinates"] = cells["document coordinates"] = document_points()
    rows = []
    eezs = list(features("eez"))
    land_pieces = land()
    for layer in ("eez", "ecs"):
        for props, g in features(layer):
            rows.append((props["geoname"], props["pol_type"], g))
    rows += uk_deposits()
    bra = brazil_2025()
    if bra is not None:
        rows.append(("Brazil, outer limit, amended executive summary (12 Mar 2025)", "ECS CLCS Submission", bra))
    for name, status, x0, x1, y0, y1, _ in ISA:
        rows.append((name, status, box(x0, y0, x1, y1)))
    hs = unary_union([g for _, g in features("high_seas")])
    for area in ("mainland", "lisavu", "document coordinates"):
        print(f"\n== {area}: {coast[area][0].size} points")
        print("   every point in the high seas (Marine Regions High Seas v2):", all_inside(cells[area], hs))
        out = []
        for name, kind, g in rows:
            hit = g.geom_type.endswith("Polygon") and inside(cells[area], g)
            km, p, q = distance(coast[area], g)
            out.append((km, name, kind, hit, p, q))
        centre = Point(float(np.mean(coast[area][0])), float(np.mean(coast[area][1])))
        pieces = sorted(land_pieces, key=lambda g: centre.distance(g))[:25]
        pieces += [g for g in land_pieces if g.area > 500 and g not in pieces]       # the continents (deg²)
        seen = {}
        for piece in pieces:
            km, p, q = distance(coast[area], piece)
            if piece.area > 500:
                where = "South America" if q.x < -20 else "Africa"
            else:                                                     # an island: named by the zone off its coast
                where = min(eezs, key=lambda e: e[1].distance(q))[0]["territory1"]
                if where == "Tristan da Cunha" and q.y < -39:
                    where = "Gough Island (Tristan da Cunha)"
            if where not in seen or km < seen[where][0]:
                seen[where] = (km, p, q)
        for where, (km, p, q) in seen.items():
            out.append((km, f"real land: {where} (nearest point {q.y:.2f}, {q.x:.2f})", "land", False, p, q))
        for km, name, kind, hit, p, q in sorted(out, key=lambda t: t[0]):
            print(f"   {km:8,.0f} km {km / NM:7,.0f} nmi  {'INSIDE ' if hit else ''}{name} [{kind}]"
                  f"  from {-p.y:.2f} S {-p.x:.2f} W to {q.y:.2f}, {q.x:.2f}")


if __name__ == "__main__":
    main()
