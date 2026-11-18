#!/usr/bin/env python3
"""Write the place list (O91, O152 stage 2) from the world data, or check that it is current.

The place list, analysis/place-list.md, is made from the map and is not edited by hand. It reads:
  world/map.json        the towns, localities, named villages, the platform, the metering station and the routes;
  world/parties.json    every party's square and address;
  world/terrain.json    the heights (through the world model), the countries, the border crossing on the river;
  world/countries.json  the coordinate rule ("geography": 3.5 km squares around the mainland's centre 30.0 S
                        15.0 W and Lisavu's own centre 33.0 S 2.65 W, as coordinate() in tools/build_examples.py
                        states them in the documents) and Bayvarra's states ("subdivision_rule");
  world/documents.json  the transport legs of the flows.
It builds the world model (tools/world_model.py) for the heights, the road network and the legs' ways, so its
figures are the map's own: a distance along a route is the length of its squares (3.5 km a side, 4.95 km a
diagonal), as tools/lay_routes.py --report gives it ("the map is leading", owner 2026-11-18, O152).

Usage: python3 tools/place_list.py           write analysis/place-list.md
       python3 tools/place_list.py --check   say whether analysis/place-list.md is current (exit 1 if not)
"""
import heapq
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "analysis", "place-list.md")
sys.path.insert(0, HERE)

import world_data          # noqa: E402
import world_model as wm   # noqa: E402

KNOT_KMH = 1.852 * 13.5          # the feeder ship's service speed, 13.5 knots (D19)
ATR_CRUISE_KMH = 500             # the ATR 72-600F's cruise (D19 as corrected with D36)
EARTH_KM = 6371.0
SPEEDS = {"road": (60, 70), "rail": (40, 60), "river": (10, 12)}   # usual averages, km/h, for the timing column

# What the old place list (2026-11-18, the 14 km grid) and D19/D44 said, for the comparison: (what, old list, D19/D44)
EARLIER = [
    ("Ferrano", "30.60° S 15.90° W (proposed; D19 16.4° W)", "30.6° S 16.4° W"),
    ("Lumeport", "31.40° S 13.80° W", "31.4° S 13.8° W"),
    ("Selanu", "33.05° S 2.22° W", "near 33.0° S 2.65° W (island centre)"),
    ("Marrowdale", "31.01° S 14.41° W", "-"),
]
EARLIER_KM = {   # id of a figure below: (old place list, D19/D44)
    "Ferrano-Marrowdale": ("182", "182 (documents 186)"),
    "Marrowdale-Lumeport": ("84", "84 (documents 38)"),
    "ore": ("154", "about 154"),
    "gas": ("about 255 (via the metering station)", "about 196 (D44)"),
    "gas-grid": ("about 210", "about 98 (D44)"),
    "gas-field": ("about 38", "about 80 (D44); documents: four kilometres"),
    "river": ("about 285", "-"),
    "sea": ("about 1,150 km, 620 nm, 46 h", "about 1,050 km, 570 nm, 42 h"),
    "air": ("1,107 km", "about 1,100 km; block 2 h 45 east, 3 h 00 west"),
}


# ---------------------------------------------------------------- positions
def latlon(world, at):
    """South latitude and west longitude of a point in squares, by the rule of coordinate() in
    tools/build_examples.py (rounded to six decimals as the documents state them)."""
    g = world["geography"]
    area = next((a for a in g.get("insets", []) if at[0] >= a["from_column"]), g["mainland"])
    (ci, cj), c = area["centre_tile"], area["centre"]
    km = g["km_per_tile"]
    lat_c, lon_c = c["latitude_south"], c["longitude_west"]
    lat = lat_c + km * (at[1] - cj) / 111.0
    lon = lon_c - km * (at[0] - ci) / (111.32 * math.cos(math.radians(lat_c)))
    return round(lat, 6), round(lon, 6)


def fmt_pos(world, at):
    lat, lon = latlon(world, at)

    def dm(x):
        d = int(x)
        return f"{d}° {(x - d) * 60:05.2f}′"
    return f"{lat:.4f} S {lon:.4f} W ({dm(lat)} S, {dm(lon)} W)"


def great_circle(world, a, b):
    (la1, lo1), (la2, lo2) = latlon(world, a), latlon(world, b)
    p1, p2 = math.radians(-la1), math.radians(-la2)
    dl = math.radians(-lo2 + lo1)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * EARTH_KM * math.asin(math.sqrt(h))


def grid_km(a, b):
    return math.dist(a, b) * wm.KM


def path_km(path):
    return sum(math.dist(a, b) for a, b in zip(path, path[1:])) * wm.KM


def compass(a, b):
    east, north = b[0] - a[0], a[1] - b[1]
    if not east and not north:
        return "at the centre"
    names = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return names[round(math.degrees(math.atan2(east, north)) / 45) % 8]


def n0(x):
    return f"{x:,.0f}"


def n1(x):
    return f"{x:,.1f}"


def hm(hours):
    h, m = divmod(round(hours * 60), 60)
    return f"{h} h {m:02d}"


# ---------------------------------------------------------------- the model
def load():
    world = world_data.load()
    _, corners = wm.load_terrain()
    probe = json.loads(json.dumps(world))      # build() annotates its copy: the towns' built-up areas
    model, _ = wm.build(probe)
    model["_ground"] = corners
    built = {}
    for tw in probe.get("towns", []) + probe.get("localities", []):
        built[tw["name"]] = tw.get("built", {})
    return world, model, built


def height(model, at, fitted=False):
    """The natural ground of the square (world/terrain.json, the mean of its four corners, metres); with fitted,
    the level the world model's 3D map gives it (built squares are levelled)."""
    V = model["v"] if fitted else model["_ground"]
    i, j = int(at[0]), int(at[1])
    return round(sum(max(0, V[x][y]) for x in (i, i + 1) for y in (j, j + 1)) / 4)


def road_graph(model):
    T = model["tiles"]
    adj = {}
    for i in range(wm.W):
        for j in range(wm.H):
            m = T[i][j].get("rd", 0)
            for bit, (di, dj) in enumerate(wm.DIRS8):
                if m & (1 << bit) and "rd" in T[i + di][j + dj]:
                    adj.setdefault((i, j), []).append(((i + di, j + dj), math.hypot(di, dj)))
    return adj


def shortest(adj, starts, goals):
    """The shortest way (in squares of length) on the road network from any start square to any goal square."""
    dist, prev, todo = {}, {}, []
    for s, d0 in starts.items():
        if s in adj:
            dist[s] = d0
            prev[s] = None
            heapq.heappush(todo, (d0, s))
    goals = {g: d for g, d in goals.items() if g in adj}
    best = None
    while todo:
        d, q = heapq.heappop(todo)
        if d > dist.get(q, 1e18):
            continue
        if q in goals and (best is None or d + goals[q] < best[0]):
            best = (d + goals[q], q)
        if best and d > best[0]:
            break
        for y, l in adj.get(q, ()):
            if d + l < dist.get(y, 1e18):
                dist[y], prev[y] = d + l, q
                heapq.heappush(todo, (d + l, y))
    if not best:
        return None, None
    out, q = [], best[1]
    while q is not None:
        out.append(q)
        q = prev[q]
    return best[0] * wm.KM, out[::-1]


def height_text(model, at):
    g, f = height(model, at), height(model, at, True)
    return f"{g} m" if abs(g - f) <= 20 else f"{g} m (3D map {f} m)"


# ---------------------------------------------------------------- the places
def state_of(world, cty, at):
    if cty != "XB":
        return "Province of Ferrano" if cty == "XU" else "-"
    r = world["countries"]["XB"]["subdivision_rule"]
    if at[1] < r["north_of_row"]:
        return r["north"]
    return r["west"] if at[0] < r["column"] else r["east"]


def first_clause(text, most=170):
    """The first sentence; if that is long, up to its first colon or semicolon."""
    text = (text or "").strip()
    if ". " in text:
        text = text.split(". ")[0] + "."
    for stop in (": ", "; "):
        if len(text) > most and stop in text:
            text = text.split(stop)[0] + "."
    return text


def places(world):
    """Every town, locality and named village: (name, kind, country, square, population text, why)."""
    capitals = {"Ferrano", "Lumeport", "Selanu"}
    out = []
    for tw in world["towns"]:
        core = next((d for d in tw.get("districts", []) if d["character"] == "core"), None)
        why = tw.get("note") or (core["note"] if core else "")
        out.append({"name": tw["name"], "kind": "capital" if tw["name"] in capitals else "town", "c": tw["country"],
                    "at": tw["c"], "people": n0(tw["population"]), "why": first_clause(why), "built_km": tw["built_km"],
                    "districts": tw.get("districts", [])})
    for lo in world["localities"]:
        p = lo["population"]
        out.append({"name": lo["name"], "kind": "village (locality)", "c": lo["country"], "at": lo["c"],
                    "people": f"{n0(p[0])}–{n0(p[1])}" if isinstance(p, list) else n0(p), "why": first_clause(lo.get("note")),
                    "built_km": lo["built_km"], "districts": []})
    for v in world["villages"]:
        if not v.get("name"):
            continue
        other = [f"{n}" for k, n in sorted(v.get("names", {}).items()) if n != v["name"]]
        out.append({"name": v["name"] + (f" ({', '.join(other)})" if other else ""), "key": v["name"], "kind": v["band"],
                    "c": v["country"], "at": v["c"], "people": n0(v["people"]), "why": first_clause(v["why"]),
                    "built_km": v["built_km"], "districts": v.get("districts", [])})
    for p in out:
        p.setdefault("key", p["name"])
    return out


# ---------------------------------------------------------------- the report
def write(world, model, built):
    L = []
    w = L.append
    party = {p["id"]: p for p in world["parties"]}
    pl = places(world)
    by_name = {p["key"]: p for p in pl}
    towns = [p for p in pl if p["kind"] in ("capital", "town", "village (locality)")]
    adj = road_graph(model)
    routes = {r["id"]: r for r in world["routes"]}
    rlen = {rid: path_km([tuple(q) for q in r["pts"]]) for rid, r in routes.items()
            if r["mode"] in ("road", "rail", "pipeline")}
    legs = model["legs"]
    T = model["tiles"]

    w("# The place list (O91)")
    w("")
    w("Made by `python3 tools/place_list.py` from the world data (`world/map.json`, `world/parties.json`, "
      "`world/terrain.json`, `world/countries.json`, `world/documents.json`); do not edit it by hand. "
      "`python3 tools/place_list.py --check` (run by `tools/check_world.py`) says whether it is current.")
    w("")
    w("It replaces the place list of 2026-11-18 written for the 14 km grid and D19's positions. The rules it follows:")
    w("")
    w("- **The map is leading** (owner, 2026-11-18, O152): a distance is the length of the route on the map, square "
      "by square (3.5 km a side, 4.95 km a diagonal), as `tools/lay_routes.py --report` measures it.")
    w("- **Positions** are WGS 84 as the documents state them (`coordinate()` in `tools/build_examples.py`): 3.5 km "
      "squares on both axes around the mainland's centre (30.0° S, 15.0° W at square 91.5/94) and, for Lisavu, "
      "drawn nearer as an inset, around its own centre (33.0° S, 2.65° W at square 225/112); a degree of latitude "
      "is 111.0 km, of longitude 111.32 km × cos(latitude of the area's centre). The minutes are those the "
      "documents print.")
    w("- **Straight lines** on land are measured on the map (squares × 3.5 km); between the mainland and Lisavu they "
      "are great-circle distances between the stated positions, since the inset is not at its true distance.")
    w("- **Heights** are the natural ground of the square (`world/terrain.json`, the mean of its four corners, "
      "metres above the sea); the 3D map levels built squares, so it may show a town lower (section 6).")
    w("- **The map is a diagram inside the towns** (O82): a party takes a whole 3.5 km square, so the parties of "
      "a town spread over two to five times its built-up width (O92, open). Distances inside and around a town "
      "are therefore longer on the map than on the ground; section 3 flags them.")
    w("")

    # 1. places ---------------------------------------------------------
    w("## 1. Places")
    w("")
    w("Every town, the two villages that are localities of parties, and every named village of the map "
      f"({len(pl)} places). Names in brackets are the place's name in the national language. Population: the "
      "decided figure, or the band for a locality.")
    w("")
    w("| Place | Kind | Country, state | Square | Position (WGS 84) | Height | People | Why it is there |")
    w("|---|---|---|---|---|---|---|---|")
    order = {"capital": 0, "town": 1, "village (locality)": 2, "country town": 3, "small town": 4,
             "large village": 5, "village": 6, "hamlet": 7}
    for p in sorted(pl, key=lambda p: ("XU XB XL".split().index(p["c"]), order.get(p["kind"], 9), p["key"])):
        w(f"| **{p['name']}** | {p['kind']} | {p['c']}, {state_of(world, p['c'], p['at'])} | {p['at'][0]}/{p['at'][1]} | "
          f"{fmt_pos(world, p['at'])} | {height_text(model, p['at'])} | {p['people']} | {p['why']} |")
    w("")
    w("**Other places the documents use:**")
    w("")
    w("| Place | Country | Square | Position (WGS 84) | Height | What it is |")
    w("|---|---|---|---|---|---|")
    for pf in world.get("platforms", []):
        w(f"| Gas platform ({party[pf['party']]['identity']['name']}) | offshore, XB's shelf | {pf['at'][0]}/{pf['at'][1]} | "
          f"{fmt_pos(world, pf['at'])} | sea | {first_clause(pf['note'])} Offshore block "
          f"{pf['at'][0] // wm.GRID:02d}/{pf['at'][1] // wm.GRID:02d}. |")
    for st in world.get("stations", []):
        w(f"| Border metering station ({st['pipeline']} pipeline) | {st['country']}, "
          f"{state_of(world, st['country'], st['at'])} | {st['at'][0]}/{st['at'][1]} | {fmt_pos(world, st['at'])} | "
          f"{height_text(model, st['at'])} | {first_clause(st['note'])} |")
    crossing = None
    rp = [tuple(q) for q in routes["road"]["pts"]]
    for a, b in zip(rp, rp[1:]):
        if T[a[0]][a[1]].get("c") == "XU" and T[b[0]][b[1]].get("c") == "XB":
            crossing = (a, b)
            break
    if crossing:
        a, b = crossing
        w(f"| Road border crossing (route `road`) | XU/XB | {a[0]}/{a[1]} → {b[0]}/{b[1]} | {fmt_pos(world, b)} | "
          f"{height_text(model, b)} | Where the main road from Ferrano to Marrowdale passes from Urvania into Bayvarra. |")
    tc = json.load(open(os.path.join(ROOT, "world", "terrain.json"), encoding="utf-8"))["crossing"]
    w(f"| The border's river point (terrain \"crossing\") | XU/XB | {tc[0]}/{tc[1]} | {fmt_pos(world, tc)} | river | "
      f"Where the land border meets the main river, at the confluence of the largest plateau tributary; below it "
      f"the river is the border. |")
    w("")

    # 2. parties --------------------------------------------------------
    w("## 2. Parties")
    w("")
    w("Every party on the map with its place (the town of its address), the district of that town nearest to it, "
      "its distance and direction from the place's centre, and the position its documents state. \"Built-up\" is "
      "the world model's verdict: inside the town's built-up area, at its edge, or outside it.")
    w("")
    w("| Party | Address: street, city (quarter) | Place | District nearest | From the centre | Built-up | Square | Position (WGS 84) | Height |")
    w("|---|---|---|---|---|---|---|---|---|")
    doubts_party = []
    for p in world["parties"]:
        a = p["identity"].get("address", {})
        city = a.get("CityName")
        place = by_name.get(city)
        at = p["at"]
        nearest = min(pl, key=lambda q: grid_km(q["at"], at))
        if not place:
            place = nearest
        d = grid_km(place["at"], at)
        dist = "at the centre" if d < 0.05 else f"{n1(d)} km {compass(place['at'], at)}"
        dn = "-"
        if place["districts"]:
            dd = min(place["districts"], key=lambda x: grid_km(x["at"], at) / x["r_km"])
            dn = f"{dd['name']} ({dd['character']}, {n1(grid_km(dd['at'], at))} km)"
        b = built.get(place["key"], {}).get("parties", {}).get(p["id"], "-")
        quarter = f" ({a['CitySubdivisionName']})" if a.get("CitySubdivisionName") else ""
        w(f"| {p['identity']['name']} ({p['id']}) | {a.get('StreetName', '-')}, {city or '-'}{quarter} | {place['key']} | "
          f"{dn} | {dist} | {b} | {at[0]}/{at[1]} | {fmt_pos(world, at)} | {height_text(model, at)} |")
        if nearest["key"] != place["key"] and grid_km(nearest["at"], at) < d - 3.5:
            doubts_party.append(f"{p['identity']['name']} ({p['id']}): its address says {city}, {n1(d)} km away; "
                                f"{nearest['key']} ({nearest['kind']}, {nearest['c']}) is nearer, {n1(grid_km(nearest['at'], at))} km.")
        if b == "outside":
            doubts_party.append(f"{p['identity']['name']} ({p['id']}) lies outside {place['key']}'s built-up area "
                                f"({n1(d)} km from the centre; the town is about {place['built_km']} km across).")
        if T[at[0]][at[1]].get("c") and T[at[0]][at[1]]["c"] != p["c"]:
            doubts_party.append(f"{p['identity']['name']} ({p['id']}) stands on a square of {T[at[0]][at[1]]['c']}, not {p['c']}.")
    w("")

    # 3. distances -------------------------------------------------------
    w("## 3. Distances along the routes")
    w("")
    w("### 3.1 The named routes")
    w("")
    w("Every road, railway and pipeline of the map except the villages' minor roads and the parties' access roads, "
      "with its length along its squares, the straight line between its ends and the detour factor (length ÷ "
      "straight line). The ends are named after the nearest place or party.")
    w("")
    w("| Route | Mode | What it is | From → to | Length | Straight | Factor | Earlier (old list; D19/D44) |")
    w("|---|---|---|---|---|---|---|---|")
    exact = {tuple(x["at"]): x["identity"]["name"] for x in world["parties"]}
    exact.update({tuple(pf["at"]): "the gas platform" for pf in world.get("platforms", [])})
    exact.update({tuple(q["at"]): q["key"] for q in pl})

    def name_at(q):
        if tuple(q) in exact:
            return exact[tuple(q)]
        near = min(pl, key=lambda x: (grid_km(x["at"], q), x["key"]))
        return f"{near['key']} ({n1(grid_km(near['at'], q))} km {compass(near['at'], q)})"
    for r in world["routes"]:
        rid = r["id"]
        if r["mode"] not in ("road", "rail", "pipeline") or rid.startswith(("village-", "access-")):
            continue
        pts = [tuple(q) for q in r["pts"]]
        Lk, S = rlen[rid], grid_km(pts[0], pts[-1])
        e = EARLIER_KM.get(rid) or (EARLIER_KM["Ferrano-Marrowdale"] if rid == "road" else None)
        mode = f"{r['class']} road" if r["mode"] == "road" else r["mode"]
        w(f"| `{rid}` | {mode} | {r.get('label', '')} | "
          f"{name_at(pts[0])} → {name_at(pts[-1])} | **{n1(Lk)} km** | {n1(S)} km | {Lk / S:.2f} | "
          f"{'; '.join(e) if e else '-'} |")
    w("")

    w("### 3.2 Between the towns by road")
    w("")
    w("The shortest way on the road network between the centres (the road square nearest each centre), as "
      "`tools/lay_routes.py --report` gives it, with the main routes it uses.")
    w("")
    w("| Between | By road | Routes | Straight | Factor | Earlier (old list; D19) |")
    w("|---|---|---|---|---|---|")
    sq_routes = {}
    for r in world["routes"]:
        if r["mode"] == "road" and not r["id"].startswith(("village-", "access-")):
            for q in r["pts"]:
                sq_routes.setdefault(tuple(q), []).append(r["id"])

    def used(path):
        seen, out = {}, []
        for q in path:
            for rid in sq_routes.get(q, []):
                seen[rid] = seen.get(rid, 0) + 1
        for q in path:
            for rid in sq_routes.get(q, []):
                if seen[rid] >= 3 and rid not in out:
                    out.append(rid)
        return ", ".join(f"`{x}`" for x in out) or "town streets, minor roads"

    def near_road(c):
        return min(adj, key=lambda q: (math.hypot(q[0] - c[0], q[1] - c[1]), q))
    pairs = [("Ferrano", "Marrowdale"), ("Marrowdale", "Lumeport"), ("Ferrano", "Lumeport"), ("Lumeport", "Larkmouth"),
             ("Larkmouth", "Marrowdale"), ("Ferrano", "Serravona"), ("Larkmouth", "Gullhaven"), ("Ferrano", "Gullhaven")]
    for a, b in pairs:
        A, B = by_name[a]["at"], by_name[b]["at"]
        km, path = shortest(adj, {near_road(A): 0.0}, {near_road(B): 0.0})
        S = grid_km(A, B)
        e = EARLIER_KM.get(f"{a}-{b}")
        w(f"| {a} – {b} | **{n0(km)} km** | {used(path)} | {n0(S)} km | {km / S:.2f} | {'; '.join(e) if e else '-'} |")
    w("")

    w("### 3.3 The transport legs of the flows")
    w("")
    w("Every leg of `world/documents.json` as the world model lays it on the map, party to party (the way the map's "
      "vehicles drive: the fewest squares from building to building), and for road legs also the shortest way in "
      "kilometres on the road network, with the routes used, the straight line, the detour factor and the time "
      "the distance takes at the mode's usual average (truck 60–70 km/h with breaks, freight train 40–60 km/h, "
      "barge 10–12 km/h). Sea and air legs are in section 4.")
    w("")
    w("| Flow | Mode | From → to | On the map | Shortest | Routes | Straight | Factor | Time at usual speed | transit_days |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    inflated = []
    for f in world["flows"]:
        for leg in f.get("legs", []):
            if leg["mode"] in ("sea", "air"):
                continue
            ml = next((x for x in legs if x["flow"] == f["id"] and x["from"] == leg["from"] and x["to"] == leg["to"]
                       and x["mode"] == leg["mode"]), None)
            if not ml:
                continue
            path = [tuple(q) for q in ml["path"]]
            km = path_km(path)
            A, B = party[leg["from"]]["at"], party[leg["to"]]["at"]
            S = grid_km(A, B)
            sh, rts = "-", "-"
            if leg["mode"] == "road":
                skm, sp = shortest(adj, {q: 0.0 for q in path[1:2]}, {q: 0.0 for q in path[-2:-1]})
                if skm is not None:
                    skm += (math.dist(path[0], path[1]) + math.dist(path[-2], path[-1])) * wm.KM
                    sh = f"{n1(skm)} km"
                    rts = used(sp)
            elif leg["mode"] == "rail":
                rts = ", ".join(f"`{r['id']}`" for r in world["routes"] if r["mode"] == "rail"
                                and sum(1 for q in r["pts"] if tuple(q) in set(path)) >= 3)
            elif leg["mode"] == "pipeline":
                rts = ", ".join(f"`{r['id']}`" for r in world["routes"] if r["mode"] == "pipeline"
                                and sum(1 for q in r["pts"] if tuple(q) in set(path)) >= 2)
            else:
                rts = "the river's course and the estuary"
            lo, hi = SPEEDS.get(leg["mode"], (None, None))
            t = f"{hm(km / hi)} – {hm(km / lo)}" if lo else "-"
            fn = lambda pid: f"{party[pid]['identity']['name']} ({pid})"
            w(f"| {f['id']} | {leg['mode']} | {fn(leg['from'])} → {fn(leg['to'])} | **{n1(km)} km** | {sh} | {rts} | "
              f"{n1(S)} km | {km / S if S else 0:.2f} | {t} | {leg.get('transit_days', '-')} |")
            pa, pb = party[leg["from"]], party[leg["to"]]
            ca, cb = pa["identity"].get("address", {}).get("CityName"), pb["identity"].get("address", {}).get("CityName")
            if ca == cb and leg["mode"] == "road":
                inflated.append(f"{f['id']}: {fn(leg['from'])} → {fn(leg['to'])}, both in {ca}: {n1(km)} km on the map")
    w("")
    if inflated:
        w("**Legs inside one town or its surroundings** (the diagram's party squares make them longer than on the "
          "ground; O82, O92):")
        w("")
        for x in inflated:
            w(f"- {x}.")
        w("")

    # 4. long distances --------------------------------------------------
    w("## 4. The long distances: Lumeport – Selanu")
    w("")
    p16b, p16l, p17b, p17l = (party[x]["at"] for x in ("16-xb", "16-xl", "17-xb", "17-xl"))
    sea = [tuple(q) for q in routes["sea"]["pts"]]
    segs = []
    for a, b in zip(sea, sea[1:]):
        ia = a[0] >= 200
        ib = b[0] >= 200
        segs.append((a, b, grid_km(a, b) if ia == ib else great_circle(world, a, b), ia != ib))
    sea_km = sum(s[2] for s in segs)
    ocean = next(s for s in segs if s[3])
    near_m = sum(s[2] for s in segs if not s[3] and s[0][0] < 200)
    near_l = sum(s[2] for s in segs if not s[3] and s[0][0] >= 200)
    straight_ports = great_circle(world, p16b, p16l)
    w("The sea route `sea` of the map, measured on the real ocean: its squares on the mainland side (Lumeport's port "
      "out through the estuary and the bay) and on Lisavu's side (from the open sea south-west of the island round "
      "its south-eastern cape and up the lee coast to the port) along the map, and the open ocean between them as "
      "the great circle between the stated positions.")
    w("")
    w("| | Distance | Nautical miles | Time |")
    w("|---|---|---|---|")
    w(f"| Lumeport port – Selanu port, straight line (great circle) | {n0(straight_ports)} km | "
      f"{n0(straight_ports / 1.852)} nm | |")
    w(f"| Sea route: Lumeport port to the open sea | {n0(near_m)} km | {n0(near_m / 1.852)} nm | |")
    w(f"| Sea route: open ocean, {ocean[0][0]}/{ocean[0][1]} to {ocean[1][0]}/{ocean[1][1]} | {n0(ocean[2])} km | "
      f"{n0(ocean[2] / 1.852)} nm | |")
    w(f"| Sea route: round the cape to Selanu port | {n0(near_l)} km | {n0(near_l / 1.852)} nm | |")
    w(f"| **Sea route, in all** | **{n0(sea_km)} km** | **{n0(sea_km / 1.852)} nm** | "
      f"**{hm(sea_km / KNOT_KMH)} at 13.5 knots** (factor {sea_km / straight_ports:.2f}) |")
    air = great_circle(world, p17b, p17l)
    still = 10 / 60 + 20 / 60 + max(0.0, air - 100) / ATR_CRUISE_KMH
    w(f"| **Lumeport airport – Selanu airport, great circle** | **{n0(air)} km** | **{n0(air / 1.852)} nm** | "
      f"{hm(still)} gate to gate in still air (taxi 10 min, climb and descent 20 min over about 100 km, cruise "
      f"at {ATR_CRUISE_KMH} km/h) |")
    w("")
    w("**Against the decisions:**")
    w("")
    w(f"- D19: \"about 1,050 km by sea\", \"about 570 nautical miles, 42 hours at 13.5 knots\"; the old place list: "
      f"about 1,150 km, 620 nm, 46 hours. The map's route: **{n0(sea_km)} km, {n0(sea_km / 1.852)} nm, "
      f"{hm(sea_km / KNOT_KMH)}**. O53 asks for one passage time (the documents have 38 to 43 hours); O123 for the "
      f"crossing of about 42–46 hours.")
    w(f"- D19 as corrected with D36: the flight about 1,100 km, about 2 h 30 gate to gate in still air, about "
      f"2 h 15–2 h 20 eastbound with the westerlies, 2 h 45 westbound; block times 2 h 45 east and 3 h 00 west. "
      f"The positions now give **{n0(air)} km** and **{hm(still)}** in still air"
      + (": the block times keep their margin." if still <= 2.75 else ": the block times would have to grow.")
      + " The island's clocks are an hour ahead (D27).")
    w(f"- The straight line port to port is {n0(straight_ports)} km (D19: about 1,000 km).")
    w("")

    # 5. what changed ----------------------------------------------------
    w("## 5. What changed against the old place list and D19/D44")
    w("")
    w("| | Old place list | D19 / D44 | Now (the map) |")
    w("|---|---|---|---|")
    for nm, old, d19 in EARLIER:
        w(f"| {nm} | {old} | {d19} | {fmt_pos(world, by_name[nm]['at'])} |")
    rb = shortest(adj, {near_road(by_name['Marrowdale']['at']): 0.0}, {near_road(by_name['Lumeport']['at']): 0.0})[0]
    w(f"| Ferrano – Marrowdale by road | 182 km | 182 km (documents 186) | {n1(rlen['road'])} km (`road`) |")
    w(f"| Marrowdale – Lumeport by road | 84 km | 84 km (documents 38) | {n0(rb)} km centre to centre; "
      f"{n1(rlen['road-b'])} km along `road-b` |")
    for rid, what in (("ore", "Mine – works by rail"), ("gas", "Gas pipeline, plant to power station"),
                      ("gas-grid", "Branch to the city gate"), ("gas-field", "Gas field line")):
        o, d = EARLIER_KM[rid]
        w(f"| {what} | {o} | {d} | {n1(rlen[rid])} km (`{rid}`) |")
    rv = next((x for x in legs if x["mode"] == "river"), None)
    if rv:
        w(f"| River, Rinova's quay – Rivermouth's quay | about 285 km | - | {n1(path_km([tuple(q) for q in rv['path']]))} km |")
    w(f"| Lumeport – Selanu by sea | about 1,150 km, 46 h | about 1,050 km, 42 h | {n0(sea_km)} km, {hm(sea_km / KNOT_KMH)} |")
    w(f"| Lumeport – Selanu by air | 1,107 km | about 1,100 km | {n0(air)} km |")
    w(f"| Lumeport airport from the centre | 17 km SW | 10–15 km (O91) | "
      f"{n1(grid_km(by_name['Lumeport']['at'], p17b))} km {compass(by_name['Lumeport']['at'], p17b)} |")
    w(f"| Selanu airport from the town | 10 km NW | about 10 km (O91) | "
      f"{n1(grid_km(by_name['Selanu']['at'], p17l))} km {compass(by_name['Selanu']['at'], p17l)} |")
    w("")
    w("The old list's five questions are settled by the map: Ferrano and Lumeport stand at their natural sites "
      "(O152 stage 1), the river below the crossing is the border with Urvania on its south bank (option A, O152), "
      "the land is resized to D19 and the routes are laid over the terrain (O152 stage 3), and the sea crossing is "
      "measured here. The decided distances of O152 (\"the map is leading\") are those of section 3.1.")
    w("")

    # 6. doubts -----------------------------------------------------------
    w("## 6. Gaps and doubts for the owner")
    w("")
    w("Found by the generator (each from the data above):")
    w("")
    for x in doubts_party:
        w(f"- {x}")
    if crossing:
        cb = crossing[1]
        for pid in ("19-xu", "19-xb"):
            w(f"- {party[pid]['identity']['name']} ({pid}) stands {n1(grid_km(party[pid]['at'], cb))} km from where "
              f"the road `road` crosses the border ({cb[0]}/{cb[1]}).")
    lev = [f"{p['key']} {height(model, p['at'], True)} m (ground {height(model, p['at'])} m)" for p in towns
           if abs(height(model, p["at"], True) - height(model, p["at"])) > 50]
    if lev:
        w("- The 3D map levels these places' centre squares well below their natural ground: " + "; ".join(lev) + ".")
    km_g = shortest(adj, {near_road(by_name["Ferrano"]["at"]): 0.0}, {near_road(by_name["Gullhaven"]["at"]): 0.0})[0]
    w(f"- Gullhaven (Kelpstone Gas) is reached by road only from Larkmouth (`road-north`): Ferrano – Gullhaven is "
      f"{n0(km_g)} km by road against {n0(grid_km(by_name['Ferrano']['at'], by_name['Gullhaven']['at']))} km in a "
      f"straight line. The lpg flow (D48, a road tanker from the gas plant) needs this settled.")
    for a, b in (("Ferrano", "Marrowdale"),):
        km_leg = next(path_km([tuple(q) for q in x["path"]]) for x in legs if x["flow"] == "road" and x["mode"] == "road")
        w(f"- {a} – {b}: the decided figure is the route `road` centre to centre, {n1(rlen['road'])} km; the road "
          f"flow's truck leg from Castrano Logistics to Lumeway is {n1(km_leg)} km on the map. Which one the "
          f"waybill invoices is a choice (O54, O60).")
    w("")
    return "\n".join(L) + "\n"


def main():
    world, model, built = load()
    text = write(world, model, built)
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != text:
            print("place list: analysis/place-list.md is not current; run python3 tools/place_list.py", file=sys.stderr)
            sys.exit(1)
        print("place list: analysis/place-list.md is current", file=sys.stderr)
        return
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"place list: wrote {os.path.relpath(OUT, ROOT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
