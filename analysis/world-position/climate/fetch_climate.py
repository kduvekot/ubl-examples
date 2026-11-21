"""The climate of the UBL World from real data at its position on the ocean (owner, 2026-11-21: factual data, kept
so that a later move or change of the world can be checked against it again).

Fetches NASA POWER's monthly climatology (MERRA-2 meteorology, CERES SYN1deg sunshine; the API states the period,
2001-2025 when first fetched) for the points below, writes the raw answers to data/<name>.json and the monthly
table to climate-table.md. The points follow world/countries.json "geography": the mainland's centre and Lisavu's
centre, plus two points inside the mainland's extent and two real islands to compare. These are values over the
open sea at sea level: the world's land does not exist, so height and mountains (the terrain) come on top.

    python3 analysis/world-position/climate/fetch_climate.py          fetch again and rewrite the table
    python3 analysis/world-position/climate/fetch_climate.py --table  rewrite the table from data/ only

Standard library only. API: https://power.larc.nasa.gov/api/temporal/climatology/point
"""
import json
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARAMS = "T2M,T2M_MAX,T2M_MIN,PRECTOTCORR,WS10M,WS50M,WD10M,ALLSKY_SFC_SW_DWN,RH2M,CLOUD_AMT"
URL = ("https://power.larc.nasa.gov/api/temporal/climatology/point?parameters={p}&community=RE"
       "&longitude={lon}&latitude={lat}&format=JSON")
M = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
DAYS = [31, 28.25, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def points():
    g = json.loads((ROOT / "world" / "countries.json").read_text())["geography"]
    c = g["mainland"]["centre"]
    lat, lon = -c["latitude_south"], -c["longitude_west"]
    isl = g["insets"][0]["centre"]
    return [("mainland", "the mainland's centre", lat, lon),
            ("mainland-north", "the mainland's north", lat + 1.5, lon + 0.5),
            ("mainland-east", "the mainland's east (Bayvarra)", lat - 0.5, lon + 2.5),
            ("lisavu", "Lisavu's centre", -isl["latitude_south"], -isl["longitude_west"]),
            ("tristan", "Tristan da Cunha (real, to compare)", -37.1, -12.3),
            ("sthelena", "St Helena (real, to compare)", -15.95, -5.7)]


def compass(d):
    return ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"][
        int((d + 11.25) % 360 // 22.5)]


def table():
    out = ["# The climate at the world's position: NASA POWER monthly averages", "",
           "Made by `fetch_climate.py` from the raw answers in `data/`. Values over the open sea at sea level. "
           "Rain in mm per month (the daily mean times the days), temperature in °C, wind at 10 m in m/s and the "
           "direction it comes from (the mean direction), sunshine on a level surface in kWh/m² a day, cloud in %.", ""]
    for name, label, lat, lon in points():
        f = HERE / "data" / f"{name}.json"
        if not f.exists():
            continue
        d = json.loads(f.read_text())
        p, rng = d["properties"]["parameter"], d["header"]["range"]
        rain = [round(p["PRECTOTCORR"][m] * k) for m, k in zip(M, DAYS)]
        out += [f"## {label} ({abs(lat):.2f}° S, {abs(lon):.2f}° {'W' if lon < 0 else 'E'})", "",
                f"{rng}. Year: mean {p['T2M']['ANN']:.1f} °C, rain {sum(rain)} mm, wind {p['WS10M']['ANN']:.1f} m/s, "
                f"sunshine {p['ALLSKY_SFC_SW_DWN']['ANN']:.2f} kWh/m² a day, cloud {p['CLOUD_AMT']['ANN']:.0f} %.", "",
                "| | " + " | ".join(m.title() for m in M) + " |", "|---|" + "---:|" * 12]
        rows = [("Mean °C", [f"{p['T2M'][m]:.1f}" for m in M]),
                ("High °C", [f"{p['T2M_MAX'][m]:.1f}" for m in M]),
                ("Low °C", [f"{p['T2M_MIN'][m]:.1f}" for m in M]),
                ("Rain mm", [str(x) for x in rain]),
                ("Wind from", [compass(p["WD10M"][m]) for m in M]),
                ("Wind m/s", [f"{p['WS10M'][m]:.1f}" for m in M]),
                ("Wind 50 m m/s", [f"{p['WS50M'][m]:.1f}" for m in M]),
                ("Sun kWh/m²/d", [f"{p['ALLSKY_SFC_SW_DWN'][m]:.1f}" for m in M]),
                ("Cloud %", [f"{p['CLOUD_AMT'][m]:.0f}" for m in M])]
        out += [f"| {k} | " + " | ".join(v) + " |" for k, v in rows] + [""]
    (HERE / "climate-table.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    if "--table" not in sys.argv:
        (HERE / "data").mkdir(exist_ok=True)
        for name, label, lat, lon in points():
            with urllib.request.urlopen(URL.format(p=PARAMS, lat=lat, lon=lon), timeout=120) as r:
                (HERE / "data" / f"{name}.json").write_bytes(r.read())
            print("fetched", name)
    table()
    print("wrote climate-table.md")
