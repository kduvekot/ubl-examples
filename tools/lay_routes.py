#!/usr/bin/env python3
"""Lay the map's roads, railways and pipelines over the terrain as a builder would (O152 stage 3), and write them
square by square into world/map.json ("routes": "pts", with "bridges" and "tunnels").

The network is given below (NETWORK): which places are linked, by which class of way, in the order a builder would
have built them (the railways first, then the main roads, the minor roads, the pipelines). Each link is laid by
tools/routing.py over world/terrain.json and what was laid before it: 8-connected, with the gradient its class is
built for, round hills and along valleys, across the river at a narrow place, with bridges and tunnels where a
real engineer would choose them. The access roads to the parties no route reaches are laid last, by the world
model's own access-road builder (tools/world_model.py, which uses the same router), and written as routes too, so
that the map holds every road and the model has nothing left to lay. The border metering station is put on the
gas pipeline on Bayvarra's side of the border.

Run it when a place, the terrain or the network changes; tools/world_model.py then checks every rule.

Usage: python3 tools/lay_routes.py            lay and write world/map.json; print every way with its length and its
                                              steepest square
       python3 tools/lay_routes.py --report   print the report for world/map.json as it is
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import routing  # noqa: E402
import world_data  # noqa: E402
import world_model as wm  # noqa: E402

# The network. Each link: id, class (rail, main, minor, pipeline), the places it joins in order (a party "p:<id>"
# is entered from the side; a town "t:<name>" at its centre, a village likewise; "h:<town>" a town's harbour;
# "r:<route id>" any square of a route laid before; "s:i,j" a square), and for a route already on the map its
# label, layer and other fields are kept. new: the fields of a route that is not on the map yet.
NETWORK = [
    # the railways: the ore line down the valley from the mine to the works; the works' second siding; the
    # container line from the hub along the rift, past the border, to the distributor's siding at Marrowdale; the
    # wool line from Marrowdale down to Larkmouth's harbour (O153: the old capital's port for the dry east)
    ("ore", "rail", ["p:4-xu", "p:5-xu"]),
    ("factory-siding", "rail", ["p:5-xu", "p:18-xu"]),
    ("rail-x", "rail", ["p:18-xu", "p:6-xb"]),
    ("rail-lark", "rail", ["r:rail-x@6-xb", "h:Larkmouth"],
     {"mode": "rail", "layer": "transport", "label": "The wool line from Marrowdale down to Larkmouth's harbour"}),
    # the main roads, from town to town (the parties on them are reached from their streets, or by an access
    # road), the settlers' roads first: Larkmouth down the coast to Lumeport and inland to Marrowdale (O153: the
    # first landing and capital), Marrowdale to Lumeport, Ferrano through the customs posts to Marrowdale (the
    # chain's road), Lumeport's centre to its port, Ferrano up the valley to Serravona and across the river to the
    # mine
    ("road-lark", "main", ["t:Larkmouth", "t:Lumeport"],
     {"mode": "road", "layer": "transport", "label": "Larkmouth down the coast to Lumeport (domestic XB)"}),
    ("road-wool", "main", ["t:Larkmouth", "t:Marrowdale"],
     {"mode": "road", "layer": "transport", "label": "Larkmouth inland to Marrowdale (domestic XB)"}),
    ("road-b", "main", ["t:Marrowdale", "t:Lumeport"]),
    ("road", "main", ["t:Ferrano", "p:19-xu", "p:19-xb", "t:Marrowdale"]),
    ("road-port", "main", ["t:Lumeport", "p:16-xb"]),
    ("road-serra", "main", ["t:Ferrano", "t:Serravona", "p:4-xu"],
     {"mode": "road", "layer": "transport", "label": "Ferrano up the valley to Serravona and across the river to the mine (domestic XU)"}),
    # Ferrano's river bridge: the road south across the river to the farms (a main road: the town's bridge)
    ("road-farm", "main", ["t:Ferrano", "s:77,128"]),
    # the minor roads: from Larkmouth north-west over the dry east to Gullhaven on the north coast (the settlers'
    # road to the north coast, and the gas plant's); on Lisavu the port through its customs post to the town
    ("road-north", "minor", ["t:Larkmouth", "t:Gullhaven"],
     {"mode": "road", "layer": "transport", "label": "Larkmouth north-west to Gullhaven on the north coast (domestic XB)"}),
    ("road-c", "minor", ["s:237,109", "p:19-xl", "t:Selanu"]),
    # the pipelines: the subsea line from the platform to the gas plant, the main line from the plant across the
    # border to the power station, the branch to Ferrano's city gate from a tee east of the power station, where
    # the line to Ferrano and the line to the power station part (D44: the branch about 98 km)
    ("gas-field", "pipeline", ["platform", "p:42-xb"]),
    ("gas", "pipeline", ["p:42-xb", "s:63,87", "p:43-xu"]),
    ("gas-grid", "pipeline", ["s:63,87", "p:44-xu"]),
]
CLASS_OF_ROUTE = {"rail": "rail", "main": "main", "minor": "minor", "pipeline": "pipeline"}


def load():
    world = world_data.load()
    terrain, E = wm.load_terrain()
    W, H = wm.W, wm.H
    kind = [[terrain["kind"][j][i] for j in range(H)] for i in range(W)]
    cty = {"U": "XU", "B": "XB", "L": "XL"}
    country = [[cty.get(terrain["country"][j][i]) for j in range(H)] for i in range(W)]
    water = {}
    for x, y, lv in terrain["river"]:
        water[(x, y)] = min(lv, water.get((x, y), 1e9))
    land = routing.Land(kind, country, E, W, H, [tuple(q) for q in terrain["estuary"]], water)
    land.load_fine(world_data.ROOT, terrain["rasters"])
    return world, terrain, land


def lay(world, terrain, land, log=print, upto=None):
    party = {p["id"]: p for p in world["parties"]}
    towns = {t["name"]: t for t in world.get("towns", []) + world.get("localities", [])}
    routes = {r["id"]: r for r in world["routes"]}
    built = routing.Built()
    fp = {pid: set(wm.footprint(p)) for pid, p in party.items()}
    all_fp = set().union(*fp.values())
    harbour = {tuple(t["harbour"]["at"]): n for n, t in towns.items() if t.get("harbour")}
    built.blocked = set(all_fp) | set(harbour)
    built.add("river", [tuple(q[:2]) for q in terrain["river"]])
    for q in land.estuary:
        built.sq["river"].add(q)
    # the open water in front of ports and harbours
    for p in world["parties"]:
        if p.get("water"):
            for q in fp[p["id"]]:
                for k in (1, 2):
                    built.blocked.add((q[0] + p["water"][0] * k, q[1] + p["water"][1] * k))
    for t in towns.values():
        if t.get("harbour"):
            (i, j), (di, dj) = t["harbour"]["at"], t["harbour"]["water"]
            for k in (1, 2):
                built.blocked.add((i + di * k, j + dj * k))
    platform = tuple(world["platforms"][0]["at"])
    # a pipeline keeps out of the towns and villages: their built-up area and TOWN_CLEAR beyond it
    town_zone = set()
    for t in towns.values():
        r = t["built_km"] / 2 / wm.KM + wm.TOWN_CLEAR + 1.0
        for i in range(int(t["c"][0] - r - 1), int(t["c"][0] + r + 2)):
            for j in range(int(t["c"][1] - r - 1), int(t["c"][1] + r + 2)):
                if math.hypot(i - t["c"][0], j - t["c"][1]) <= r:
                    town_zone.add((i, j))
    customs = [tuple(party[p]["at"]) for p in party if party[p]["kind"] == "customs"]
    cross_pairs = {(a, b) for a in customs for b in customs if abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1}
    laid = {}

    def dry_near(c, mode):
        """The square at or next to c that a way may end on (a village's centre may be on the river, a town's on a
        rail line)."""
        c = tuple(c)
        other = {"road": ("rail", "pipeline"), "rail": ("road", "pipeline"), "pipeline": ("road", "rail")}[mode]
        for r in range(0, 4):
            cand = [(c[0] + a, c[1] + b) for a in range(-r, r + 1) for b in range(-r, r + 1) if max(abs(a), abs(b)) == r]
            cand = [q for q in cand if land.kind[q[0]][q[1]] not in "sw" and q not in built.blocked
                    and not any(q in built.sq[x] for x in other) and q not in built.structures]
            if cand:
                return min(cand, key=lambda q: math.hypot(q[0] - c[0], q[1] - c[1]))
        raise SystemExit(f"no dry square near {c}")

    def place(ref, cls, as_goal):
        """The squares of a place: (squares, whether entered only from the side)."""
        kind_, _, v = ref.partition(":")
        if ref == "platform":
            return {platform}, False
        if kind_ == "p":
            sq = fp[v]
            if cls == "pipeline":                       # a pipeline ends beside the building, not in it
                sq = {(q[0] + d[0], q[1] + d[1]) for q in sq for d in wm.DIRS} - all_fp
                sq = {q for q in sq if land.kind[q[0]][q[1]] not in "sw" and q not in built.sq["road"] and q not in built.sq["rail"]}
                return sq, False
            return set(sq), True
        if kind_ == "t":
            return {dry_near(towns[v]["c"], routing.CLASSES[cls]["mode"])}, False
        if kind_ == "h":
            return {tuple(towns[v]["harbour"]["at"])}, True
        if kind_ == "s":
            return {tuple(int(x) for x in v.split(","))}, False
        if kind_ == "r":
            rid, _, near = v.partition("@")
            path = laid[rid][0]
            if near:                                    # the squares of the route beside a party
                sq = {q for q in path if any(abs(q[0] - y[0]) + abs(q[1] - y[1]) <= 1 for y in fp[near]) and q not in all_fp}
                return sq, False
            return set(path[3:-3]) - all_fp, False      # a branch: anywhere but at the route's ends
        raise SystemExit(f"unknown place {ref}")

    for rid, cls, places, *extra in NETWORK:
        if rid == upto:                                 # for a look at what was laid before a link
            return built, laid, place
        mode = routing.CLASSES[cls]["mode"]
        path, sts = [], {}
        for a, b in zip(places, places[1:]):
            starts, s_orth = place(a, cls, False) if not path else ({path[-1]}, path[-1] in all_fp or path[-1] in harbour)
            goals, g_orth = place(b, cls, True)
            orth = (starts if s_orth else set()) | (goals if g_orth else set())
            blocked_before = set(built.blocked)
            built.blocked |= {q for q in starts | goals if q in all_fp or q in harbour}
            avoid = set()
            if cls == "pipeline":
                avoid = town_zone - starts - goals
            if path:
                avoid |= set(path[:-1])
            sdir = (path[-1][0] - path[-2][0], path[-1][1] - path[-2][1]) if len(path) > 1 and path[-1] not in all_fp else None
            got = routing.route(land, built, cls, sorted(starts), goals, allow_cross=cross_pairs, orth_ends=orth,
                                sea_ok=(a == "platform"), avoid=avoid, start_dir=sdir)
            built.blocked = blocked_before
            if not got:
                raise SystemExit(f"{rid}: no way from {a} to {b}")
            seg, s2 = got
            path = path + (seg if not path else seg[1:])
            sts.update(s2)
        built.add(mode if mode != "road" else "road", path, sts)
        if mode == "road":
            pass
        laid[rid] = (path, sts, cls, extra[0] if extra else None)
        log(f"  laid {rid} ({cls}): {len(path)} squares, {routing.length_km(path):.0f} km, "
            f"{sum(1 for v in sts.values() if v == 'bridge')} bridge and {sum(1 for v in sts.values() if v == 'tunnel')} tunnel squares")
    # the routes on the map: the laid ways in place of the old points
    out = []
    order = [n[0] for n in NETWORK]
    for r in world["routes"]:
        if r["id"] in laid:
            continue
        if r["mode"] in ("road", "rail", "pipeline") and not r["id"].startswith("access-"):
            raise SystemExit(f"route {r['id']} is on the map but not in the network")
    for rid in order:
        path, sts, cls, new = laid[rid]
        r = dict(routes.get(rid) or new)
        r["id"] = rid
        r.pop("path", None)
        r["class"] = cls if cls in ("main", "minor") else None
        if r["class"] is None:
            r.pop("class")
        r["pts"] = [list(q) for q in path]
        water = {q for q in path if land.kind[q[0]][q[1]] == "w"}
        r["bridges"] = [list(q) for q in path if sts.get(q) == "bridge" or q in water]
        r["tunnels"] = [list(q) for q in path if sts.get(q) == "tunnel"]
        for k in ("bridges", "tunnels"):
            if not r[k] or r["mode"] == "pipeline":
                r.pop(k)
        out.append(r)
    # the metering station: on the gas pipeline, the last square in Bayvarra before the border, if free
    gas = laid["gas"][0]
    k = next(k for k in range(len(gas) - 1) if land.country[gas[k][0]][gas[k][1]] == "XB" and land.country[gas[k + 1][0]][gas[k + 1][1]] == "XU")
    st = next(gas[x] for x in range(k, max(0, k - 3), -1) if gas[x] not in built.sq["road"] and gas[x] not in built.sq["rail"]
              and land.kind[gas[x][0]][gas[x][1]] not in "sw")
    return out, list(st)


def access_roads(world):
    """The roads the world model lays itself (to parties no route reaches), as routes."""
    model, problems = wm.build(json.loads(json.dumps(world)))
    return model.get("access", []), problems


def write(routes, station):
    m = json.load(open(world_data.path("map"), encoding="utf-8"))
    keep = [r for r in m["routes"] if r["mode"] not in ("road", "rail", "pipeline")]
    first = {r["id"]: k for k, r in enumerate(m["routes"])}
    allr = keep + routes
    allr.sort(key=lambda r: (first.get(r["id"], 10_000), 0))
    m["routes"] = allr
    m["stations"][0]["at"] = station
    world_data.save("map", m)


def main():
    world, terrain, land = load()
    if "--report" not in sys.argv:
        print("laying the network:")
        routes, station = lay(world, terrain, land)
        world["routes"] = [r for r in world["routes"] if r["mode"] not in ("road", "rail", "pipeline")] + routes
        world["stations"][0]["at"] = station
        acc, _ = access_roads(world)
        for k, a in enumerate(acc):
            end = a["path"][-1]
            rid = f"access-{a['to']}" if a["to"] else f"link-{end[0]}-{end[1]}"
            r = {"id": rid, "mode": "road", "layer": "network", "class": "minor",
                 "label": f"Access road to {a['name']}" if a["to"] else "A road joining two parts of the network",
                 "pts": a["path"]}
            if a.get("bridges"):
                r["bridges"] = a["bridges"]
            routes.append(r)
            print(f"  laid {r['id']} (minor): {len(a['path'])} squares, {routing.length_km([tuple(q) for q in a['path']]):.0f} km")
        write(routes, station)
        world = world_data.load()
    report(world)


def report(world):
    model, problems = wm.build(json.loads(json.dumps(world)))
    V = model["v"]
    T = model["tiles"]
    print("\nevery way: length (km, along its squares; smoothed as drawn), steepest square (gradient, where)")
    for r in world["routes"]:
        if r["mode"] not in ("road", "rail", "pipeline"):
            continue
        path = [tuple(q) for q in r["pts"]]
        L = routing.length_km(path)
        sm = smooth_km(path)
        worst, at = 0.0, None
        if r["mode"] != "pipeline":
            for k in range(1, len(path) - 1):
                g = gradient(V, T, path[k - 1], path[k], path[k + 1])
                if g is not None and g > worst:
                    worst, at = g, path[k]
        cls = r.get("class", r["mode"])
        st = [s for s in model["structures"] if s["way"] == r["id"]]
        sts = ", ".join(f"{s['kind']} {s['km']} km at {s['squares'][0]}" for s in st)
        print(f"  {r['id']:<16} {cls:<9} {L:6.1f} km ({sm:6.1f} drawn)  steepest {worst * 100:4.1f} % at {at}" + (f"  [{sts}]" if sts else ""))
    print("\nstructures:")
    for s in model["structures"]:
        print(f"  {s['way']:<16} {s['kind']:<7} {s['km']:4.1f} km from {s['squares'][0]} to {s['squares'][-1]}, ends at "
              f"{s['ends_m'][0]} and {s['ends_m'][1]} m" + (f", deck up to {s['deck_above_m']} m above the ground or water below"
                                                             if s['kind'] == 'bridge' else f", at least {s['cover_m']} m of ground above"))
    distances(world, model)
    for p in problems:
        print("problem:", p)


def distances(world, model):
    """The decided distances (D19, D44) against the drawn ways: by road between the town centres (the shortest way on
    the road network), by rail between the mine and the works, the pipelines."""
    import heapq
    T = model["tiles"]
    adj = {}
    for i in range(wm.W):
        for j in range(wm.H):
            m = T[i][j].get("rd", 0)
            for bit, (di, dj) in enumerate(wm.DIRS8):
                if m & (1 << bit) and "rd" in T[i + di][j + dj]:
                    adj.setdefault((i, j), []).append(((i + di, j + dj), math.hypot(di, dj)))
    towns = {t["name"]: tuple(t["c"]) for t in world["towns"] + world["localities"]}

    def near_road(c):
        return min((q for q in adj), key=lambda q: math.hypot(q[0] - c[0], q[1] - c[1]))

    def road_km(a, b):
        s, g = near_road(towns[a]), near_road(towns[b])
        dist, todo = {s: 0.0}, [(0.0, s)]
        while todo:
            d, q = heapq.heappop(todo)
            if q == g:
                return d * wm.KM
            if d > dist[q]:
                continue
            for y, l in adj.get(q, ()):
                if d + l < dist.get(y, 1e18):
                    dist[y] = d + l
                    heapq.heappush(todo, (d + l, y))
        return None
    r = {x["id"]: x for x in world["routes"]}
    print("\ndecided (D19, D44) against drawn:")
    for a, b, want in (("Ferrano", "Marrowdale", 182), ("Marrowdale", "Lumeport", 84), ("Lumeport", "Larkmouth", None),
                       ("Larkmouth", "Marrowdale", None), ("Ferrano", "Serravona", None), ("Larkmouth", "Gullhaven", None)):
        km = road_km(a, b)
        print(f"  {a}-{b} by road: {km:.0f} km" + (f" (decided about {want}, {100 * (km / want - 1):+.0f} %)" if want else ""))
    for rid, want, what in (("ore", 154, "mine-works by rail"), ("rail-x", None, "hub-Lumeway by rail"),
                            ("rail-lark", None, "Marrowdale-Larkmouth by rail"), ("gas", 196, "the gas pipeline"),
                            ("gas-grid", 98, "its branch"), ("gas-field", 80, "the field line")):
        km = routing.length_km([tuple(q) for q in r[rid]["pts"]])
        print(f"  {what}: {km:.0f} km" + (f" (decided about {want}, {100 * (km / want - 1):+.0f} %)" if want else ""))


def smooth_km(path, it=3):
    pts = [tuple(map(float, q)) for q in path]
    for _ in range(it):
        if len(pts) < 3:
            break
        new = [pts[0]]
        for a, b in zip(pts, pts[1:]):
            new += [(.75 * a[0] + .25 * b[0], .75 * a[1] + .25 * b[1]), (.25 * a[0] + .75 * b[0], .25 * a[1] + .75 * b[1])]
        new.append(pts[-1])
        pts = new
    return sum(math.dist(a, b) for a, b in zip(pts, pts[1:])) * wm.KM


def gradient(V, T, a, q, b):
    """The gradient of a way through square q (from neighbour a to neighbour b): between the middles of the edges
    (or the corners) it enters and leaves by, on the fitted heights; on a bridge or in a tunnel, along its deck."""
    t = T[q[0]][q[1]]
    if "dk" in t:
        return None
    def at(d):
        x, y = q[0] + .5 + d[0] / 2, q[1] + .5 + d[1] / 2
        i0, j0 = int(math.floor(x)), int(math.floor(y))
        u, v = x - i0, y - j0
        i1, j1 = min(i0 + 1, len(V) - 1), min(j0 + 1, len(V[0]) - 1)
        return V[i0][j0] * (1 - u) * (1 - v) + V[i1][j0] * u * (1 - v) + V[i0][j1] * (1 - u) * v + V[i1][j1] * u * v
    da, db = (a[0] - q[0], a[1] - q[1]), (b[0] - q[0], b[1] - q[1])
    dist = math.hypot((db[0] - da[0]) / 2, (db[1] - da[1]) / 2) * wm.KM * 1000
    return abs(at(db) - at(da)) / dist if dist else None


if __name__ == "__main__":
    main()
