#!/usr/bin/env python3
"""Lay the map's roads, railways and pipelines over the terrain as a builder would (O152 stage 3), and write them
square by square into world/map.json ("routes": "pts", with "bridges" and "tunnels").

The network is given below (NETWORK): which places are linked, by which class of way, in the order a builder would
have built them (the railways first, then the main roads, the minor roads, the pipelines). Each link is laid by
tools/routing.py over world/terrain.json and what was laid before it: 8-connected, with the gradient its class is
built for, round hills and along valleys, across the river at a narrow place, with bridges and tunnels where a
real engineer would choose them. The access roads to the parties no route reaches are laid next, by the world
model's own access-road builder (tools/world_model.py, which uses the same router), and written as routes too, so
that the map holds every road and the model has nothing left to lay. Last come the minor roads to the villages
(map "villages", O152; lay_villages below), so that everything laid before them stays as it is. The border metering station is put on the
gas pipeline on Bayvarra's side of the border.

Run it when a place, the terrain or the network changes; tools/world_model.py then checks every rule.

Usage: python3 tools/lay_routes.py            lay and write world/map.json; print every way with its length and its
                                              steepest square
       python3 tools/lay_routes.py --report   print the report for world/map.json as it is
       python3 tools/lay_routes.py --refit    keep every route, but lay again the minor roads to villages that no
                                              longer keep to the road rule on their own line (routing.Land.half_ok;
                                              after a change of the terrain or the rule), and write world/map.json
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
    # wool line from Marrowdale down to Larkmouth's harbour (O153: the old capital's port for the dry east); the
    # port line from Marrowdale down to the Port of Lumeport
    ("ore", "rail", ["p:4-xu", "p:5-xu"]),
    ("factory-siding", "rail", ["p:5-xu", "p:18-xu"]),
    ("rail-x", "rail", ["p:18-xu", "p:6-xb"]),
    ("rail-lark", "rail", ["r:rail-x@6-xb", "h:Larkmouth"],
     {"mode": "rail", "layer": "transport", "label": "The wool line from Marrowdale down to Larkmouth's harbour"}),
    # the port line: the Ferrano-Marrowdale line goes on down to the quays of the Port of Lumeport (the capital's
    # container and bulk port)
    ("rail-port", "rail", ["r:rail-x@6-xb", "p:16-xb"],
     {"mode": "rail", "layer": "transport", "label": "The port line from Marrowdale down to the quays of the Port of Lumeport"},
     {"keep_off": ["41-xb", "34-xb", "c-xb"]}),
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
    # Lumeport's civic street (O244): Civic Square, from the main roads' end across the port railway over Government
    # Hill and round its east flank to the insurer's door, one street for the civic bodies on the hill (2-xb, 21-xb,
    # 24-xb, 28-xb, 29-xb, 11-xb, 48-xb) in place of their separate access roads; the Department of Agriculture
    # (57-xb) stands beside it on the east flank
    ("civic", "minor", ["s:137,126", "s:141,126", "s:141,127", "p:29-xb"],
     {"mode": "road", "layer": "network", "class": "minor", "label": "Civic Square, the street over Government Hill in Lumeport"}),
    # the minor roads: from Larkmouth north-west over the dry east to Gullhaven on the north coast (the settlers'
    # road to the north coast, and the gas plant's); on Lisavu the port through its customs post to the town
    ("road-north", "minor", ["t:Larkmouth", "t:Gullhaven"],
     {"mode": "road", "layer": "transport", "label": "Larkmouth north-west to Gullhaven on the north coast (domestic XB)"}),
    ("road-c", "minor", ["s:237,109", "p:19-xl", "t:Selanu"]),
    # the waste road: the works' hazardous production waste by truck to the recovery plant (flow waste; a
    # supply-chain route since the first map, de34b46)
    ("waste", "minor", ["p:5-xu", "p:7-xu"],
     {"mode": "road", "layer": "chain", "label": "Production waste"}),
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
            if len(extra) > 1 and extra[1].get("keep_off"):
                # through a town: not beside these buildings, so that a street can still reach them
                avoid |= {(q[0] + d[0], q[1] + d[1]) for pid in extra[1]["keep_off"] for q in fp[pid] for d in wm.DIRS8} - goals - starts
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
        laid[rid] = (path, sts, cls, extra[0] if extra and extra[0] else None)
        log(f"  laid {rid} ({cls}): {len(path)} squares, {routing.length_km(path):.0f} km, "
            f"{sum(1 for v in sts.values() if v == 'bridge')} bridge and {sum(1 for v in sts.values() if v == 'tunnel')} tunnel squares")
    # the routes on the map: the laid ways in place of the old points
    out = []
    order = [n[0] for n in NETWORK]
    for r in world["routes"]:
        if r["id"] in laid:
            continue
        if r["mode"] in ("road", "rail", "pipeline") and not r["id"].startswith(("access-", "village-")):
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


def lay_villages(world, terrain, land, routes, log=print, cls="minor", skip=frozenset()):
    """The minor roads to the villages (map "villages", O152): each village is joined to the road network by a minor
    road (up to 10 %, bridges as before, no tunnel), laid over the terrain with the same router after every other
    way, so that the main roads, the railways, the pipelines and the access roads stay as they are. The road ends
    on the square beside the village (its houses face it); a village beside a road needs none. The villages nearest
    the network are joined first, so that the roads to the further ones can run on from them, as a network grows.
    Returns the new routes."""
    built = routing.Built()
    fp = {p["id"]: set(wm.footprint(p)) for p in world["parties"]}
    all_fp = set().union(*fp.values())
    towns = world.get("towns", []) + world.get("localities", [])
    built.blocked = set(all_fp) | {tuple(t["harbour"]["at"]) for t in towns if t.get("harbour")}
    for p in world["parties"]:
        if p.get("water"):
            for q in fp[p["id"]]:
                for k in (1, 2):
                    built.blocked.add((q[0] + p["water"][0] * k, q[1] + p["water"][1] * k))
    for t in towns:
        if t.get("harbour"):
            (i, j), (di, dj) = t["harbour"]["at"], t["harbour"]["water"]
            for k in (1, 2):
                built.blocked.add((i + di * k, j + dj * k))
    built.blocked |= {tuple(st["at"]) for st in world.get("stations", [])}
    built.add("river", [tuple(q[:2]) for q in terrain["river"]])
    for q in land.estuary:
        built.sq["river"].add(q)
    for r in routes:
        if r["mode"] in ("road", "rail", "pipeline"):
            path = [tuple(q) for q in r["pts"]]
            sts = {tuple(q): "bridge" for q in r.get("bridges", [])}
            if r["mode"] != "pipeline":
                sts.update({q: "bridge" for q in path if land.kind[q[0]][q[1]] == "w"})
            sts.update({tuple(q): "tunnel" for q in r.get("tunnels", [])})
            built.add(r["mode"], path, sts)
    villages = world.get("villages", [])
    vsq = {tuple(v["c"]) for v in villages}
    built.blocked |= vsq
    # squares a road may not join at: a level crossing, a structure and its approaches, a party's square
    def joinable(q):
        return q not in built.sq["rail"] and q not in built.sq["pipeline"] and q not in built.structures \
            and q not in all_fp
    D4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # a minor road keeps 2 squares off a bridge or a tunnel and its approaches (their ground is fitted to the deck)
    near_struct = {(q[0] + a, q[1] + b) for q in built.structures for a in range(-2, 3) for b in range(-2, 3)}
    def near_road(v):
        return (min((abs(v["c"][0] - q[0]) + abs(v["c"][1] - q[1]) for q in built.sq["road"]), default=999), v["c"])

    out = []

    def climbs_over(path):
        """A road that climbs more than REFIT_CLIMB_M above the higher of its two ends (the rule of refit's
        reasonable, owner 2026-11-19, MO002 option c; O244: kept on every lay, so that a full relay does not lay a
        mountain road to a cove that a refit would refuse): such a village is reached by a track or by sea."""
        hs = [land.hc[i][j] for i, j in path]
        return max(hs) > max(hs[0], hs[-1]) + REFIT_CLIMB_M

    def link(v):
        """Join village v to the roads: True if done (or beside a road already), None if no way was found."""
        c = tuple(v["c"])
        if any((c[0] + a, c[1] + b) in built.sq["road"] for a, b in D4):
            return True                                    # on a road already
        starts = [(c[0] + a, c[1] + b) for a, b in D4]
        starts = [q for q in starts if land.inside(q) and land.kind[q[0]][q[1]] not in "sw" and q not in built.blocked
                  and not any(q in built.sq[x] for x in ("rail", "pipeline")) and q not in near_struct]
        for R in (8, 16, 32):
            box = (c[0] - R, c[1] - R, c[0] + R, c[1] + R)
            goals = {q for q in built.sq["road"] if box[0] <= q[0] <= box[2] and box[1] <= q[1] <= box[3] and joinable(q)
                     and land.country[q[0]][q[1]] == land.country[c[0]][c[1]] and q not in near_struct}
            if not goals or not starts:
                continue
            got = routing.route(land, built, cls, sorted(starts), goals, box=box, avoid=vsq | (near_struct - goals))
            if got and climbs_over(got[0]):
                got = None                                 # over a mountain to a village: no builder's road (MO002 c)
            if got:
                break
        else:
            return None
        path, sts = got
        built.add("road", path, sts)
        near_struct.update((q[0] + a, q[1] + b) for q in built.structures for a in range(-2, 3) for b in range(-2, 3))
        r = {"id": f"village-{c[0]}-{c[1]}", "mode": "road", "layer": "network", "class": "minor",
             "label": f"Minor road to {v['name'] or 'a village'}", "pts": [list(q) for q in path]}
        br = [list(q) for q in path if sts.get(q) == "bridge" or land.kind[q[0]][q[1]] == "w"]
        if br:
            r["bridges"] = br
        out.append(r)
        return True

    todo = sorted([v for v in villages if tuple(v["c"]) not in skip], key=near_road)
    while todo:                       # passes: a village far from every road is tried again once others have roads
        failed = [v for v in todo if link(v) is None]
        if len(failed) == len(todo):
            break
        todo = sorted(failed, key=near_road)
    log(f"  laid {len(out)} minor roads to villages, {sum(len(r['pts']) for r in out)} squares, "
        f"{sum(routing.length_km([tuple(q) for q in r['pts']]) for r in out):.0f} km; "
        f"{len(villages) - len(out) - len(failed)} villages beside a road already")
    for v in failed:
        log(f"  no road to the village at {v['c']} ({v['name'] or 'unnamed'})")
    return out


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


def refit(world, terrain, land):
    """The routes, with the village roads that leave the road rule on any square laid again (owner, 2026-11-19,
    MO002 option c), each village in turn:
      1. a way that keeps to the rule on every square, if it is reasonable (see reasonable below);
      2. otherwise a way on which the builder cuts or fills at most routing.ROAD_SLACK_M on each half of a square
         (class "minor-cut"; the world model makes the cut), if that is reasonable;
      3. otherwise no road: the village is reached by a track or by sea (as Felulaka's story says).
    Returns (routes, the ids taken out, {village road id: what became of it})."""
    routes = [r for r in world["routes"] if r["mode"] in ("road", "rail", "pipeline")]
    c = routing.CLASSES["minor"]
    old = {r["id"]: r for r in routes}

    def breaks(r):
        P = [tuple(q[:2]) for q in r["pts"]]
        br = {tuple(q) for q in r.get("bridges", [])}
        for a, b in zip(P, P[1:]):
            if a in br or b in br:
                continue
            if not (land.half_ok(a, (b[0] - a[0], b[1] - a[1]), c["half"], c["lean"])
                    and land.half_ok(b, (a[0] - b[0], a[1] - b[1]), c["half"], c["lean"])):
                return True
        return False

    def reasonable(r):
        """A builder's road: at most twice as long as the road it replaces (or REFIT_EXTRA squares longer), and
        not climbing more than REFIT_CLIMB_M above the higher of its two ends."""
        P = [tuple(q[:2]) for q in r["pts"]]
        n0 = len(old[r["id"]]["pts"]) if r["id"] in old else 1
        if len(P) > max(2 * n0, n0 + REFIT_EXTRA):
            return False
        hs = [land.hc[i][j] for i, j in P]
        return max(hs) <= max(hs[0], hs[-1]) + REFIT_CLIMB_M

    def cut_too_deep(keep, new):
        """The new roads on which the world model, fitting the land to them, moves a corner more than
        routing.ROAD_SLACK_M (the router's allowance is measured on the road's line; the model's fit, with corners
        held at the sea, can cut deeper: this checks the result)."""
        w = json.loads(json.dumps(world))
        w["routes"] = [r for r in w["routes"] if r["mode"] not in ("road", "rail", "pipeline")] + json.loads(json.dumps(keep + new))
        model, _ = wm.build(w)
        V, E = model["v"], terrain_e
        return [r for r in new if max(abs(V[i + a][j + b] - E[i + a][j + b]) for i, j, *_ in r["pts"] for a in (0, 1)
                                      for b in (0, 1)) > routing.ROAD_SLACK_M + 1]
    terrain_e = wm.load_terrain()[1]

    out = {r["id"] for r in routes if r["id"].startswith("village-") and breaks(r)}
    keep = [r for r in routes if r["id"] not in out]
    print(f"refit: laying again {len(out)} village roads: {', '.join(sorted(out))}")
    fate = {}
    for cls in ("minor", "minor-cut"):
        refused = set()
        for _ in range(8):        # lay; if a road is unreasonable, set its village aside and lay them all again
            new = lay_villages(world, terrain, land, keep, log=lambda s: None, cls=cls, skip=refused)
            bad = {tuple(int(x) for x in r["id"].split("-")[1:3]) for r in new if not reasonable(r)}
            if not bad and cls == "minor-cut" and new:
                bad = {tuple(int(x) for x in r["id"].split("-")[1:3]) for r in cut_too_deep(keep, new)}
            if bad:
                refused |= bad
                continue
            keep += new
            for r in new:
                fate[r["id"]] = "within the rule" if cls == "minor" else f"with cuts of at most {routing.ROAD_SLACK_M} m"
            break
    road_sq = {tuple(q[:2]) for r in keep if r["mode"] == "road" for q in r["pts"]}
    villages = {tuple(v["c"]): v for v in world.get("villages", [])}
    linked = {r["id"] for r in keep}
    for vid in out | set(fate):
        if vid in linked:
            continue
        vc = tuple(int(x) for x in vid.split("-")[1:3])
        beside = any((vc[0] + a, vc[1] + b) in road_sq for a, b in ((1, 0), (0, 1), (-1, 0), (0, -1)))
        fate[vid] = "beside a road now" if beside else "no road (a track or the sea)"
    for vid in sorted(fate):
        v = villages.get(tuple(int(x) for x in vid.split("-")[1:3]), {})
        print(f"  {vid} ({v.get('name') or 'unnamed'}): {fate[vid]}")
    return keep, out, fate


LATE_ACCESS = 6                                            # squares: a longer access road waits for its village's road
REFIT_EXTRA = 4                                            # squares a relaid road may be longer than twice the old one
REFIT_CLIMB_M = 300                                        # metres it may climb above the higher of its ends


def main():
    world, terrain, land = load()
    if "--refit" in sys.argv:
        routes, _, _ = refit(world, terrain, land)
        write(routes, world["stations"][0]["at"])
        report(world_data.load())
        return
    if "--report" not in sys.argv:
        print("laying the network:")
        routes, station = lay(world, terrain, land)
        world["routes"] = [r for r in world["routes"] if r["mode"] not in ("road", "rail", "pipeline")] + routes
        world["stations"][0]["at"] = station
        # a party in a village that no way of the network passes (O244: Harrowmead's fruit packers) is reached from
        # its village's road, not by a road of its own to the network: its access road is laid after the villages'
        acc, _ = access_roads(world)
        late = later_parties(world) & {a["to"] for a in acc if len(a["path"]) > LATE_ACCESS}
        add_access(routes, [a for a in acc if a["to"] not in late])
        routes += lay_villages(world, terrain, land, routes)
        if late:
            world["routes"] = [r for r in world["routes"] if r["mode"] not in ("road", "rail", "pipeline")] + routes
            acc, _ = access_roads(world)
            add_access(routes, acc)
        write(routes, station)
        world = world_data.load()
    report(world)


def later_parties(world):
    """The parties whose address is a named village (map "villages") with no road of the routes beside its centre:
    if their own road to the network would be longer than LATE_ACCESS squares, it waits for the village's road."""
    road = {tuple(q[:2]) for r in world["routes"] if r["mode"] == "road" for q in r["pts"]}
    vil = {v["name"]: tuple(v["c"]) for v in world.get("villages", []) if v.get("name")}
    out = set()
    for p in world["parties"]:
        c = vil.get(p.get("identity", {}).get("address", {}).get("CityName"))
        if c and not any((c[0] + a, c[1] + b) in road for a in (-1, 0, 1) for b in (-1, 0, 1)):
            out.add(p["id"])
    return out


def add_access(routes, acc):
    """Add the world model's access roads (and links) to routes, as routes."""
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
                            ("rail-lark", None, "Marrowdale-Larkmouth by rail"), ("rail-port", None, "Marrowdale-port of Lumeport by rail"), ("gas", 196, "the gas pipeline"),
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
