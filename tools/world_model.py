#!/usr/bin/env python3
"""Build the tile model of the UBL world from the world layers (map, parties), and check it.

The map is a grid of W x H = 256 x 192 squares of 3.5 km (GRID = 4 squares per 14 km, the squares of the
first map); every distance below is given in squares and in km.

The world is a finished snapshot: everything is built, nothing grows. This
script decides the structure; the map (site/world.html) only draws it.

For every tile the model records:
  k   terrain (world/terrain.json): s sea, w river or estuary water, g grass, f forest, r rock (high ground, cliff
      faces), d field, h scrub or heath, m marsh
  c   country (XU, XB, XL) or null
  h   height of the tile's lowest corner, in metres (corner heights are in model "v")
  n   a stable noise value 0..1, for variation in the drawing
  rd  road connections, a 4-bit mask: 1 = +i, 2 = +j, 4 = -i, 8 = -j
  rl  rail pieces, each a pair of edge directions ([di, dj] or null for the centre)
  br  1 if a road or rail crosses water here (a bridge)
  b   id of the party standing here
  hs  a house: [level 1..4, facing direction 0..3 towards its street]; in a town, a square of houses (the
      built-up area's own streets run within it), outside the towns a single house (a farmstead)
  um  the built-up area of a town or village on this square: a mask of its SUB x SUB sub-squares of 875 m
      (bit a * SUB + b for the sub-square a along i, b along j), on every kind of square it covers (houses,
      parties, roads, rails)
  ul  the density of the built-up area on this square: 1 houses, 2 terraces, 3 blocks of flats, 4 towers (the
      centre of a capital)
  tr  1 for a single tree on open ground
  yd  1 for the fenced yard around an industry
  az  1 in the approach zone of an airport runway
  es  1 for river water at least ESTUARY wide (the estuary): drawn as open water, the
      rest of the river as a narrower stream within its tiles
  ms  1 for a pipeline's border metering station (map "stations")

Structural rules (the build stops when one is broken):
  * buildings do not share tiles and do not stand on roads, rails or water,
    except parties marked "on" a route (customs posts, rail stations);
  * every party has access: a road next to it, or rail for rail parties,
    or water for ports and quays; missing access roads are laid by the model;
  * every town and village is built up over the area its built_km gives (map "towns", "localities"), on land,
    off the airports and their approach zones and TOWN_CLEAR from a pipeline (step 6);
  * every house faces a street: the road next to it, or, in a town, the next square of houses on the way to
    one (the town's own streets);
  * every landmass has one connected road network; every party lies on it
    (an access road is laid where needed, ending at the building);
  * a dead end must lead somewhere: to a party or a house (a road that ends
    at nothing gets a farmstead, or is removed);
  * the terrain comes from world/terrain.json (tools/terrain.py, O152): the kind and the country of every
    square, the height of every square corner in metres (model "v"), with no limit between neighbouring corners;
    0 at the sea and in the estuary;
  * what is built is fitted to the land: buildings, houses, yards, stations, junctions and bends stand on a
    platform (four corners level); a straight road or rail square is a ramp, level across, rising at most
    RAIL_RISE = 70 m (rail, 2 %) or ROAD_RISE = 245 m (road, 7 %) along its direction;
  * the river runs downhill: its water lies at the heights its route gives,
    never rising from source to mouth, and the land beside it is nowhere lower
    than the river (it lies in its valley);
  * roads and rails cross the river only on straight bridges; level
    crossings are a straight road across a straight rail;
  * tall structures (a mast, a cooling tower) keep TALL_CLEARANCE = 2 squares
    (7 km) from an airport and its approach zones;
  * an airport has an approach zone of APPROACH = 3 squares (10.5 km) beyond
    each runway end, low and flat at runway height, with nothing tall in it;
  * the land border follows the watershed north of the crossing and the river below it (all land south of
    the river is Urvania): tools/terrain.py draws it into the terrain's countries;
  * a road across a land border passes a customs post on each side (within
    BORDER_POST = 3 squares, 10.5 km, along the road); a rail line across it
    passes a rail station (a terminal, where the train is cleared, anywhere on the
    line); rail lines end at a party;
  * sea routes run over water from port to port, air routes from airport
    to airport;
  * pipelines are buried: they run in straight lines along the tile grid,
    cross a road, a rail line or the river underneath, at right angles and
    in a straight line, never along them, and keep out of towns; nothing is
    built or planted on them (the right of way is kept clear); a pipeline
    leaves the sea only once, at its landfall, from an offshore platform;
  * a pipeline starts at a party, at its offshore platform or on another
    pipeline (a branch), and ends at a party; across a land border it
    passes a border metering station within METERING = 3 squares (10.5 km) of
    the crossing;
  * every transport leg of a flow (world/documents.json) is possible: road,
    rail or river connects its two parties (in the estuary, which is open
    water, a barge may use any of it), a sea or air route their port
    or airport, or the pipelines, in the direction of the flow, the gas
    producer and its customer; its carrier has a means of that mode; every
    carrier a document of the flow names carries one of its legs; and every
    pipeline carries a pipeline leg (or feeds the producer from its platform).
    The model records each leg's way on the map ("legs"): the map's vehicles
    travel exactly these.

Usage: python3 tools/world_model.py [out.json]   (default: print a summary)
"""
import json
import math
import os
import sys
from collections import deque

ROOT = os.path.join(os.path.dirname(__file__), "..")
# The grid. The first map had 64 x 48 squares of 14 km; on 2026-11-18 the owner made the squares four times
# finer (3.5 km), so that the map can hold real detail. GRID is the number of squares per 14 km: every length
# below that was written in squares of the first map is multiplied by it, and the shapes made by the noise
# (land, border, hills, forests) are sampled in units of 14 km ("chart units", see chart()), so they keep
# their shapes at any GRID.
GRID = 4
KM = 14 / GRID                                    # kilometres per square: 3.5
W, H = 64 * GRID, 48 * GRID                       # 256 x 192 squares
TALL = {"telecom", "power", "gasplant"}           # kinds with a mast, a cooling tower or a flare stack
# Distances of the rules, in squares of 3.5 km. On the first map they were whole squares of 14 km (an approach
# zone of 42 km, a mast 56 km from an airport); since the redraw of 2026-11-18 they are realistic distances.
TALL_CLEARANCE = 2                                # squares (7 km) they keep from an airport and its approach zones
APPROACH = 3                                      # squares (10.5 km) of approach zone beyond each runway end
BORDER_POST = 3                                   # squares (10.5 km) along the road within which a border crossing has its customs post
METERING = 3                                      # squares (10.5 km) along a pipeline within which a border crossing is metered
TOWN_CLEAR = 1                                    # squares (3.5 km) a pipeline keeps from a town's built-up area
PORT_BASIN = 2                                    # squares (7 km) of open water kept in front of a port's quay
STREETS = 3                                       # squares between a town's side streets (the street pattern, not a distance)
SUB = 4                                           # sub-squares per square side for the built-up areas (875 m)
BUILT_WARP = .35                                  # how far the noise moves a built-up area's edge, as a share of its radius
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]        # bit 0..3 of the road mask
ESTUARY = 1.5                                     # a river this wide (squares, 5 km) is open water: an estuary
LEVEL_M = 1                                       # model "v" holds metres (since O152 stage 1; it was levels of 100 m)
RAIL_RISE = 70                                    # metres a straight rail square may rise along its direction (2 %)
ROAD_RISE = 245                                   # metres a straight road square may rise along its direction (7 %)
FLAT_TOL = 1                                      # metres: a platform's corners may differ by this much (rounding)
TERRAIN = os.path.join(ROOT, "world", "terrain.json")


def load_terrain():
    """The terrain (world/terrain.json, made by tools/terrain.py from world/terrain-inputs.json, O152): per square
    the kind and the country, per square corner the height in metres, the main river's squares (source to mouth)
    with their water level, the estuary's squares. Returns the file and the corner heights E[vi][vj] (corner
    (vi, vj) is the north-west corner of square (vi, vj))."""
    import array
    import base64
    t = json.load(open(TERRAIN, encoding="utf-8"))
    c = t["corners_m"]
    a = array.array("h")
    a.frombytes(base64.b64decode(c["int16_le_base64"]))
    if sys.byteorder != "little":
        a.byteswap()
    rows, cols = c["rows"], c["cols"]
    return t, [[a[vj * cols + vi] for vj in range(rows)] for vi in range(cols)]


def chart(i):
    """The chart coordinate of square i, in units of 14 km (the squares of the first map, whose square x is
    square GRID * x now): the noise and the shapes of land and border are sampled in it."""
    return i / GRID


# ---------------------------------------------------------------- noise
def hsh(x, y):
    h = (x * 374761393 + y * 668265263) & 0xFFFFFFFF
    h = ((h ^ (h >> 13)) * 1274126177) & 0xFFFFFFFF
    return ((h ^ (h >> 16)) & 0xFFFFFFFF) / 4294967295


def smooth(x, y):
    xi, yi = math.floor(x), math.floor(y)
    xf, yf = x - xi, y - yi
    a, b, c, d = hsh(xi, yi), hsh(xi + 1, yi), hsh(xi, yi + 1), hsh(xi + 1, yi + 1)
    u, v = xf * xf * (3 - 2 * xf), yf * yf * (3 - 2 * yf)
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v


def noise(x, y):
    return smooth(x / 6, y / 6) * .6 + smooth(x / 3, y / 3) * .3 + smooth(x, y) * .1


def sign(v):
    return (v > 0) - (v < 0)


def path_tiles(pts, mode):
    """Roads: an L per pair of waypoints (longer leg first). Rail (and the river's course, the sea lanes): a
    staircase that keeps as close as it can to the straight line between the waypoints."""
    out = [tuple(pts[0])]
    for bi, bj in pts[1:]:
        i, j = out[-1]
        if mode != "road":
            ai, aj = i, j
            L = math.hypot(bi - ai, bj - aj) or 1
            off = lambda x, y: abs((x - ai) * (bj - aj) - (y - aj) * (bi - ai)) / L
            while (i, j) != (bi, bj):
                si, sj = sign(bi - i), sign(bj - j)
                if si and sj:
                    if (off(i + si, j), -abs(bi - i)) <= (off(i, j + sj), -abs(bj - j)):
                        i += si
                    else:
                        j += sj
                elif si:
                    i += si
                else:
                    j += sj
                out.append((i, j))
            continue
        if mode == "road":
            for axis in (("i", "j") if abs(bi - i) >= abs(bj - j) else ("j", "i")):
                while (i != bi) if axis == "i" else (j != bj):
                    if axis == "i":
                        i += sign(bi - i)
                    else:
                        j += sign(bj - j)
                    out.append((i, j))
        else:
            while (i, j) != (bi, bj):
                if abs(bi - i) >= abs(bj - j):
                    i += sign(bi - i)
                else:
                    j += sign(bj - j)
                out.append((i, j))
    return out


def footprint(p):
    a, b = p.get("size", [1, 1])
    return [(p["at"][0] + i, p["at"][1] + j) for i in range(a) for j in range(b)]


def build(world):
    problems = []
    # a town's radius in squares, from the width of its built-up area (map "built_km")
    for tw in world.get("towns", []) + world.get("localities", []):
        tw["r"] = tw["built_km"] / 2 / KM
    T = [[None] * H for _ in range(W)]
    terrain, E = load_terrain()

    # 1. land, countries, terrain: from the terrain (world/terrain.json). The land border follows the watershed
    #    north of the crossing and the river below it (owner, 2026-11-18, option A); tools/terrain.py draws it.
    CTY = {"U": "XU", "B": "XB", "L": "XL"}
    estuary = {tuple(q) for q in terrain["estuary"]}
    for i in range(W):
        for j in range(H):
            n = noise(chart(i), chart(j))
            t = {"k": terrain["kind"][j][i], "c": CTY.get(terrain["country"][j][i]), "h": 0, "n": round(n, 3)}
            if (i, j) in estuary:
                t["es"] = 1
            T[i][j] = t
    tile = lambda i, j: T[i][j] if 0 <= i < W and 0 <= j < H else None

    # 2. the river: its squares (world/terrain.json "river", source to mouth) are water at their own level, falling
    #    to the sea; below them the estuary is open water. A river route (the barges) follows the river's squares from
    #    the square nearest its first point down to the estuary.
    river_level, course = {}, []
    for x, y, lv in terrain["river"]:
        if (x, y) not in river_level:
            river_level[(x, y)] = min(lv, river_level[course[-1]]) if course else lv
            course.append((x, y))
    for r in world["routes"]:
        if r["mode"] != "river":
            continue
        a0 = tuple(r["pts"][0])
        k0 = min(range(len(course)), key=lambda k: math.dist(course[k], a0))
        r["path"] = course[k0:]
        end = course[-1]
        mouth = next(((end[0] + di, end[1] + dj) for di, dj in DIRS if (end[0] + di, end[1] + dj) in estuary), None)
        if mouth:
            r["path"] = r["path"] + [mouth]                # into the estuary, open water
        r["water"] = True

    # 3. parties: footprints on flat ground; a port's quay side is open water
    owner = {}
    for p in world["parties"]:
        for (i, j) in footprint(p):
            t = T[i][j]
            if t["k"] in ("s", "w"):
                problems.append(f"#{p['n']} {p['name']} stands on water at {(i, j)}")
            t["k"], t["h"], t["c"] = "g", 0, p["c"]
            if (i, j) in owner:
                problems.append(f"#{p['n']} {p['name']} and {owner[(i, j)]['name']} share tile {(i, j)}")
            owner[(i, j)] = p
            t["b"] = p["id"]
        if p.get("water"):
            di, dj = p["water"]
            for (i, j) in footprint(p):
                for k in range(1, PORT_BASIN + 1):
                    t = tile(i + di * k, j + dj * k)
                    if t and "b" not in t:
                        t["k"], t["c"], t["h"] = "s", None, 0

    # 3a. pipelines and their stations. A pipeline is buried: its tiles keep their terrain, but its right
    #     of way is kept clear (no house, yard, tree or forest on it). A border metering station stands
    #     on the pipeline, on flat land.
    pipes = {}
    for r in world["routes"]:
        if r["mode"] == "pipeline":
            pts = r["pts"]
            for (ai, aj), (bi, bj) in zip(pts, pts[1:]):
                if ai != bi and aj != bj:
                    problems.append(f"pipeline '{r['id']}' is not straight along the tile grid from {(ai, aj)} to {(bi, bj)}")
            r["path"] = pipes[r["id"]] = path_tiles(pts, "road")
    corridor = {q for path in pipes.values() for q in path}
    pipe_ends = frozenset(q for path in pipes.values() for q in (path[0], path[-1]))
    stations = {}
    for st in world.get("stations", []):
        q = tuple(st["at"])
        stations[q] = st
        t = tile(*q)
        if not t or t["k"] in ("s", "w") or q in owner:
            problems.append(f"{st['kind']} station at {q} must stand on free land")
            continue
        t["k"], t["ms"] = "g", 1
        if q not in corridor:
            problems.append(f"{st['kind']} station at {q} is not on a pipeline")
    for q in corridor:
        t = tile(*q)
        if t and t["k"] == "f":
            t["k"] = "g"

    # 3b. a sea route is a shipping lane: land on it becomes water, unless something is built there
    for r in world["routes"]:
        if r["mode"] == "sea":
            for q in path_tiles(r["pts"], "rail"):
                t = tile(*q)
                if t and t["k"] != "s" and q not in owner:
                    t["k"], t["c"], t["h"] = "s", None, 0

    # 4. routes. Road connections are explicit edges between neighbouring tiles; nothing is
    #    connected just because two road tiles touch.
    road, rails, edges, into = set(), {}, set(), {}

    def link(a, b):
        edges.add(frozenset((a, b)))

    def lay_road(path):
        """Lay a road along a chain of neighbouring tiles; water tiles become bridges."""
        for k, q in enumerate(path):
            t = T[q[0]][q[1]]
            if t["k"] == "w":
                t["br"] = 1
            elif t["k"] == "s":
                t["k"] = "g"
            road.add(q)
            if k:
                link(path[k - 1], q)

    def enter(q, building_tile):
        into.setdefault(q, set()).add((building_tile[0] - q[0], building_tile[1] - q[1]))

    for r in world["routes"]:
        if r["mode"] in ("road", "rail"):
            path = path_tiles(r["pts"], r["mode"])
            r["path"] = path
            if r["mode"] == "road":
                chain = []
                for k, q in enumerate(path):
                    p = owner.get(q)
                    if p and p.get("on") != "road":
                        if 0 < k < len(path) - 1:
                            problems.append(f"#{p['n']} {p['name']} stands on road route '{r['id']}' at {q}")
                        if chain:
                            enter(chain[-1], q)          # the road ends at this building
                        lay_road(chain)
                        chain = []
                        continue
                    chain.append(q)
                lay_road(chain)
            else:
                for k, (i, j) in enumerate(path):
                    p = owner.get((i, j))
                    if p and p.get("on") != "rail" and 0 < k < len(path) - 1:
                        problems.append(f"#{p['n']} {p['name']} stands on rail route '{r['id']}' at {(i, j)}")
                    t = T[i][j]
                    if t["k"] == "w":
                        t["br"] = 1
                    prev = (path[k - 1][0] - i, path[k - 1][1] - j) if k else None
                    nxt = (path[k + 1][0] - i, path[k + 1][1] - j) if k < len(path) - 1 else None
                    if not p or p.get("on") == "rail":
                        rails.setdefault((i, j), []).append([prev, nxt])

    def neighbours(cells):
        out = set()
        for (i, j) in cells:
            for di, dj in DIRS:
                q = (i + di, j + dj)
                if q not in cells:
                    out.add(q)
        return out

    def free(q, water_ok=False):
        t = tile(*q)
        return bool(t) and q not in owner and q not in rails and q not in stations and (t["k"] not in ("s", "w") or (water_ok and t["k"] == "w"))

    # 5. towns: streets as lines (a main cross, side streets every third tile); only the part
    #    connected to the town centre stays
    for tw in world.get("towns", []):
        ci, cj, rad = tw["c"][0], tw["c"][1], max(1, round(tw["r"]))
        lines = [("i", cj, rad), ("j", ci, rad)]
        for k in range(STREETS, rad + 1, STREETS):
            lines += [("i", cj + k, rad * .75), ("i", cj - k, rad * .75), ("j", ci + k, rad * .75), ("j", ci - k, rad * .75)]
        streets = set()
        for axis, fixed, reach in lines:
            prev = None
            for m in range(-rad, rad + 1):
                q = (ci + m, fixed) if axis == "i" else (fixed, cj + m)
                ok = math.hypot(q[0] - ci, q[1] - cj) <= reach and free(q)
                if ok:
                    streets.add(q)
                    road.add(q)
                    if prev:
                        link(prev, q)
                prev = q if ok else None
        tw["streets"] = streets

    def components():
        adj = {q: set() for q in road}
        for e in edges:
            a2, b2 = tuple(e)
            if a2 in adj and b2 in adj:
                adj[a2].add(b2)
                adj[b2].add(a2)
        comp, out = {}, []
        for q in road:
            if q in comp:
                continue
            c, st = {q}, [q]
            comp[q] = len(out)
            while st:
                x = st.pop()
                for y in adj[x]:
                    if y not in comp:
                        comp[y] = len(out)
                        c.add(y)
                        st.append(y)
            out.append(c)
        return out, adj

    def drop(cells):
        for q in cells:
            road.discard(q)
            into.pop(q, None)
        for e in list(edges):
            if e & cells:
                edges.discard(e)

    # keep, per town, only the street network around its centre
    comps, _ = components()
    for tw in world.get("towns", []):
        best = max(comps, key=lambda c: len(c & tw["streets"]))
        drop({q for q in tw["streets"] if q not in best})

    # landmasses: land and river together (bridges cross the river), the sea separates them
    mass = {}
    for i in range(W):
        for j in range(H):
            if T[i][j]["k"] != "s" and (i, j) not in mass:
                st, mass[(i, j)] = [(i, j)], len(set(mass.values()))
                mid = mass[(i, j)]
                while st:
                    x = st.pop()
                    for di, dj in DIRS:
                        y = (x[0] + di, x[1] + dj)
                        if tile(*y) and T[y[0]][y[1]]["k"] != "s" and y not in mass:
                            mass[y] = mid
                            st.append(y)

    def crossable_rail(y, d):
        """A rail tile a road may cross: one straight piece, at right angles to the road."""
        pcs = rails.get(y)
        if not pcs or len(pcs) != 1 or not (pcs[0][0] and pcs[0][1]):
            return False
        a2, b2 = pcs[0]
        straight = a2[0] == -b2[0] and a2[1] == -b2[1]
        return straight and (a2[0] == 0) != (d[0] == 0)

    def connect(starts, goal, avoid=frozenset()):
        """Shortest free path from any start tile to a goal tile, laid as road. It never crosses
        a land border, never branches off a bridge, and crosses rail lines and the river only in
        a straight line at right angles (a level crossing, a bridge)."""
        prev, came, todo = {}, {}, deque()
        for q in starts:
            prev[q], came[q] = None, None
            todo.append(q)
        while todo:
            q = todo.popleft()
            if q in goal and q not in starts:
                path = []
                while q is not None:
                    path.append(q)
                    q = prev[q]
                path.reverse()
                lay_road(path)
                return path
            crossing = q not in starts and (q in rails or T[q[0]][q[1]]["k"] == "w")
            for d in DIRS:
                if crossing and d != came[q]:
                    continue                      # keep straight on while crossing
                y = (q[0] + d[0], q[1] + d[1])
                ty = tile(*y)
                if not ty or y in prev or y in avoid or y in owner or ty["k"] == "s":
                    continue
                cq, cy = T[q[0]][q[1]]["c"], ty["c"]
                if cq and cy and cq != cy:
                    continue                      # border crossings only on routes with customs
                if y in goal and (ty["k"] == "w" or y in rails):
                    continue                      # never join at a bridge or a level crossing
                if y in rails and not crossable_rail(y, d):
                    continue
                prev[y], came[y] = q, d
                todo.append(y)
        return None

    def main_network(m):
        comps2, _ = components()
        on_mass = [c for c in comps2 if mass.get(next(iter(c))) == m]
        return max(on_mass, key=len) if on_mass else set()

    # every landmass has one road network: link the smallest piece to the nearest other piece,
    # until one network is left
    for m in set(mass.values()):
        for _ in range(60):
            comps2, _ = components()
            on_mass = sorted((c for c in comps2 if mass.get(next(iter(c))) == m), key=len)
            if len(on_mass) <= 1:
                break
            piece, others = on_mass[0], set().union(*on_mass[1:])
            if not connect(piece, others):
                problems.append(f"road piece at {sorted(piece)[0]} cannot be linked to the network")
                drop(piece)

    # every party lies on its landmass's network: lay an access road to it if needed
    for p in world["parties"]:
        fp = set(footprint(p))
        net = main_network(mass[fp and next(iter(fp))])
        around = neighbours(fp)
        touching = [q for q in around | fp if q in net]
        if touching:
            for q in touching:
                if q in around and len([e for e in edges if q in e]) <= 1:
                    enter(q, next(b2 for b2 in fp if abs(b2[0] - q[0]) + abs(b2[1] - q[1]) == 1))
            continue
        starts = [q for q in around if free(q) and q not in corridor]     # not along a pipeline's right of way
        path = connect(starts, net, avoid=pipe_ends)
        if not path:
            problems.append(f"#{p['n']} {p['name']} cannot be reached by road")
            continue
        enter(path[0], next(b2 for b2 in fp if abs(b2[0] - path[0][0]) + abs(b2[1] - path[0][1]) == 1))

    # 5b. airports: the runway runs along the longer side; beyond each end an approach zone of
    #     APPROACH squares, as wide as the airport, must stay low and flat (water is fine): no buildings,
    #     houses, yards, forest or hills, and the land in it at runway height
    approach = {}
    for p in world["parties"]:
        if p["kind"] != "airport":
            continue
        (i0, j0), (a, b) = p["at"], p.get("size", [1, 1])
        along_i = a >= b
        zone = []
        for k in range(1, APPROACH + 1):
            for w2 in range(b if along_i else a):
                zone += [(i0 - k, j0 + w2), (i0 + a - 1 + k, j0 + w2)] if along_i else [(i0 + w2, j0 - k), (i0 + w2, j0 + b - 1 + k)]
        for q in zone:
            t = tile(*q)
            if not t:
                continue
            approach[q] = p
            t["az"] = 1 if (k := abs(q[0] - p["at"][0]) if along_i else abs(q[1] - p["at"][1])) else 1
            if t["k"] in ("f", "r"):
                t["k"] = "g"
            o = owner.get(q)
            if o:
                problems.append(f"#{o['n']} {o['name']} stands in the approach zone of #{p['n']} {p['name']} at {q}")
        # tall structures (masts, cooling towers) keep clear of the airport and its approach
        # zones by at least TALL_CLEARANCE tiles in every direction
        near = set(zone) | {(i0 + di, j0 + dj) for di in range(a) for dj in range(b)}
        for o in world["parties"]:
            if o["kind"] in TALL:
                gap = min(max(abs(x - u), abs(y - v)) for (x, y) in footprint(o) for (u, v) in near)
                if gap < TALL_CLEARANCE:
                    problems.append(f"#{o['n']} {o['name']} ({o['kind']}) is {gap} tiles from the runway or approach "
                                    f"of #{p['n']} {p['name']}; tall structures keep {TALL_CLEARANCE} tiles clear")

    # 6. built-up areas and houses. Every town and village (map "towns", "localities") is built up over the area
    #    of a circle as wide as its built_km (owner, 2026-11-18), counted on sub-squares of KM / SUB (875 m), SUB x
    #    SUB per square (model "um"). Its edge is made irregular by the model's noise (a warp of BUILT_WARP of
    #    its radius), it reaches out along the roads, and it follows the land: not on the sea or the river, not on an airport or in its approach zones, and
    #    TOWN_CLEAR from a pipeline's right of way. The area is found by scaling that shape until it holds the
    #    decided area. Party squares, roads and rails inside it are part of it; every other square in it holds
    #    houses ("hs"), denser and taller towards the centre (level 4, towers, only in the capitals).
    def degree(q):
        return sum(1 for e in edges if q in e)

    near_pipe = {(i + a2, j + b2) for (i, j) in corridor for a2 in range(-TOWN_CLEAR, TOWN_CLEAR + 1)
                 for b2 in range(-TOWN_CLEAR, TOWN_CLEAR + 1)}
    built = {}                                            # square -> the town or village built up there

    def buildable(q):
        t = tile(*q)
        o = owner.get(q)
        return bool(t) and t["k"] not in ("s", "w") and q not in approach and q not in near_pipe and q not in stations \
            and not (o and o["kind"] == "airport")

    for tw in world.get("towns", []) + world.get("localities", []):
        ci, cj, rad = tw["c"][0], tw["c"][1], tw["r"]
        pop = max(tw["population"]) if isinstance(tw.get("population"), list) else tw.get("population", 0)
        reach = math.ceil(rad * 3) + 2
        box_ = [(i, j) for i in range(ci - reach, ci + reach + 1) for j in range(cj - reach, cj + reach + 1)
                if buildable((i, j)) and (i, j) not in built]
        ways = [q for q in road if abs(q[0] - ci) <= reach + 1 and abs(q[1] - cj) <= reach + 1]

        def spread(x, y):
            """How far (x, y) lies out, in squares: from the centre, warped by the noise, nearer along the roads."""
            wx = (noise(x * 1.7 + 31.7, y * 1.7 - 12.9) - .5) * 2 * BUILT_WARP * rad
            wy = (noise(x * 1.7 - 7.3, y * 1.7 + 45.1) - .5) * 2 * BUILT_WARP * rad
            d = math.hypot(x - ci + wx, y - cj + wy)
            dr = min((max(abs(x - a2), abs(y - b2)) for a2, b2 in ways), default=9)
            if dr < 1:
                d *= .78 + .22 * dr                    # ribbons along the roads
            return d

        subs = [(q, a2, b2, spread(q[0] - .5 + (a2 + .5) / SUB, q[1] - .5 + (b2 + .5) / SUB))
                for q in box_ for a2 in range(SUB) for b2 in range(SUB)]
        want = max(1, round(math.pi * (tw["built_km"] / 2) ** 2 / (KM / SUB) ** 2))     # sub-squares
        lo, hi = 0.0, 4 * rad + 4
        for _ in range(40):
            mid_ = (lo + hi) / 2
            if sum(1 for *_, d in subs if d < mid_) < want:
                lo = mid_
            else:
                hi = mid_
        scale = hi
        cells = [(q, a2, b2) for q, a2, b2, d in subs if d < scale]
        for q, a2, b2 in cells:
            t = tile(*q)
            t["um"] = t.get("um", 0) | 1 << (a2 * SUB + b2)
            built[q] = tw
        top = 4 if pop >= 250_000 else 3 if pop >= 20_000 else 1
        for q in {q for q, _, _ in cells}:
            t = tile(*q)
            u = spread(*q) / scale
            t["ul"] = min(top, 4 if u < .22 else 3 if u < .45 else 2 if u < .75 else 1)
            if q in owner or q in road or q in rails or q in corridor or "hs" in t:
                continue
            t["k"], t["hs"] = "g", [t["ul"], None]
        n = len(cells)
        xs = [q[0] * SUB + a2 for q, a2, _ in cells]
        ys = [q[1] * SUB + b2 for q, _, b2 in cells]
        tw["built"] = {"km2": round(n * (KM / SUB) ** 2, 1), "across_km": round(2 * math.sqrt(n / math.pi) * KM / SUB, 1),
                       "west_east_km": round((max(xs) - min(xs) + 1) * KM / SUB, 1) if n else 0,
                       "north_south_km": round((max(ys) - min(ys) + 1) * KM / SUB, 1) if n else 0}

    # where each party stands to the built-up area of its place (its address's CityName): inside, at the edge
    # (on the next square), or outside; reported, not a rule (works and depots may stand outside their town)
    for tw in world.get("towns", []) + world.get("localities", []):
        where = tw["built"]["parties"] = {}
        for p in world["parties"]:
            if p.get("identity", {}).get("address", {}).get("CityName") != tw["name"]:
                continue
            fp = footprint(p)
            if any(built.get(q) is tw for q in fp):
                where[p["id"]] = "inside"
            elif any(built.get((q[0] + a2, q[1] + b2)) is tw for q in fp for a2 in (-1, 0, 1) for b2 in (-1, 0, 1)):
                where[p["id"]] = "edge"
            else:
                where[p["id"]] = "outside"

    # every house square of a town faces its street: a road next to it, or the next house square on the way to
    # one (the town's own streets run within its squares); a house square with no way to a road stays open land
    todo = deque(q for q in road)
    seen = set(road)
    while todo:
        q = todo.popleft()
        for b2, (di, dj) in enumerate(DIRS):
            y = (q[0] + di, q[1] + dj)
            t = tile(*y)
            if t and y not in seen and t.get("hs") and t["hs"][1] is None:
                t["hs"][1] = DIRS.index((-di, -dj))
                seen.add(y)
                todo.append(y)
    for q, tw in built.items():
        t = tile(*q)
        if t.get("hs") and t["hs"][1] is None:
            del t["hs"]

    # 7. dead ends must lead somewhere: a road that ends at nothing gets a farmstead if there is
    #    room, otherwise it is removed
    def leads_somewhere(q):
        if q in into:
            return True
        return any((q[0] + di, q[1] + dj) in owner or "hs" in (tile(q[0] + di, q[1] + dj) or {}) for di, dj in DIRS)

    changed = True
    while changed:
        changed = False
        for q in sorted(road):
            if degree(q) <= 1 and not leads_somewhere(q):
                spot = next(((q[0] + di, q[1] + dj) for di, dj in DIRS
                             if free((q[0] + di, q[1] + dj)) and (q[0] + di, q[1] + dj) not in road
                             and (q[0] + di, q[1] + dj) not in rails and (q[0] + di, q[1] + dj) not in approach
                             and (q[0] + di, q[1] + dj) not in corridor), None)
                if spot and T[q[0]][q[1]]["k"] != "w":
                    face = DIRS.index((q[0] - spot[0], q[1] - spot[1]))
                    T[spot[0]][spot[1]]["k"], T[spot[0]][spot[1]]["hs"] = "g", [1, face]
                else:
                    drop({q})
                changed = True

    # road connections per tile: edges to neighbouring road tiles, plus the building a road ends at
    for (i, j) in road:
        mask = 0
        for bit, (di, dj) in enumerate(DIRS):
            if frozenset(((i, j), (i + di, j + dj))) in edges or (di, dj) in into.get((i, j), ()):
                mask |= 1 << bit
        T[i][j]["rd"] = mask
    for (i, j), pieces in rails.items():
        T[i][j]["rl"] = pieces

    # 8. industries get a fenced yard on free neighbouring tiles; single trees on open land
    for p in world["parties"]:
        if p["kind"] in ("mine", "factory", "warehouse", "waste"):
            for q in neighbours(set(footprint(p))):
                t = tile(*q)
                if t and free(q) and q not in road and q not in rails and "hs" not in t and q not in approach and q not in corridor and hsh(q[0] * 3, q[1] * 11) < .55:
                    t["k"], t["yd"] = "g", 1
    for i in range(W):
        for j in range(H):
            t = T[i][j]
            if t["k"] == "g" and (i, j) not in road and (i, j) not in rails and \
                    "b" not in t and "hs" not in t and "yd" not in t and (i, j) not in approach and (i, j) not in corridor \
                    and hsh(i * 5, j * 17) < .05:
                t["tr"] = 1

    # 9. height: a height per tile corner (vertex) in metres, from the terrain (world/terrain.json), with no limit
    #    between neighbouring corners (the land has hills, valleys and cliffs). 0 at the sea and in the estuary; the
    #    river at its own level, never rising downstream, its banks not below it. What is built is fitted to the land:
    #    a building, a house square, a yard, a station, a junction or a bend of a road or rail, a level crossing and
    #    an airport's approach square stand on a platform (their four corners level); a straight road or rail square
    #    is a ramp, level across and rising at most RAIL_RISE (rail) or ROAD_RISE (road) metres along its direction.
    V = [[float(E[vi][vj]) for vj in range(H + 1)] for vi in range(W + 1)]
    fixed = [[False] * (H + 1) for _ in range(W + 1)]        # corners at the water keep their height
    touches = lambda vi, vj: [tile(vi - a2, vj - b2) for a2 in (0, 1) for b2 in (0, 1) if tile(vi - a2, vj - b2)]
    for vi in range(W + 1):
        for vj in range(H + 1):
            ts = touches(vi, vj)
            wet = [river_level[(vi - a2, vj - b2)] for a2 in (0, 1) for b2 in (0, 1)
                   if (vi - a2, vj - b2) in river_level and T[vi - a2][vj - b2]["k"] == "w"]
            if any(t["k"] == "s" or t.get("es") for t in ts) or len(ts) < 4:
                V[vi][vj], fixed[vi][vj] = 0.0, True
            elif wet:
                V[vi][vj], fixed[vi][vj] = float(max(wet)), True
    # the banks: no corner beside the river lies below its water (a lower bound, kept when fitting below)
    # (a corner beside the river is held at or above the lowest water it is next to)
    floor = {}
    for (i, j), lv in river_level.items():
        for a2 in range(i - 1, i + 3):
            for b2 in range(j - 1, j + 3):
                if 0 <= a2 <= W and 0 <= b2 <= H and not fixed[a2][b2]:
                    floor[(a2, b2)] = min(floor.get((a2, b2), 1e9), lv)
    for (a2, b2), lv in floor.items():
        V[a2][b2] = max(V[a2][b2], float(lv))
    STRAIGHT_I, STRAIGHT_J = 1 | 4, 2 | 8          # road masks of a straight road along i / along j

    def ground_rule(q):
        """('flat' | 'ramp-i' | 'ramp-j', rise limit in metres) or None (free terrain) for the tile at q."""
        t = T[q[0]][q[1]]
        if q in river_level and t["k"] == "w" and not t.get("br"):
            return None                                     # the river falls along its course (fixed corners)
        if t["k"] in ("s", "w") or "b" in t or "hs" in t or "yd" in t or "ms" in t or (q in approach and t["k"] != "s"):
            return ("flat", 0)
        if q in road and q in rails:
            return ("flat", 0)                              # level crossing
        if q in road:
            m = T[q[0]][q[1]].get("rd", 0)
            return ("ramp-i", ROAD_RISE) if m == STRAIGHT_I else ("ramp-j", ROAD_RISE) if m == STRAIGHT_J else ("flat", 0)
        if q in rails:
            pcs = rails[q]
            if len(pcs) == 1 and pcs[0][0] and pcs[0][1] and pcs[0][0][0] == -pcs[0][1][0] and pcs[0][0][1] == -pcs[0][1][1]:
                return ("ramp-i", RAIL_RISE) if pcs[0][0][1] == 0 else ("ramp-j", RAIL_RISE)
            return ("flat", 0)
        return None

    def corner_groups(q, rule):
        i, j = q
        if rule == "flat":
            return [[(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]]
        if rule == "ramp-i":                                # level across the road, along each of its ends
            return [[(i, j), (i, j + 1)], [(i + 1, j), (i + 1, j + 1)]]
        return [[(i, j), (i + 1, j)], [(i, j + 1), (i + 1, j + 1)]]

    RULES = [(i, j, ground_rule((i, j))) for i in range(W) for j in range(H)]
    RULES = [(i, j, r) for i, j, r in RULES if r and not (T[i][j]["k"] == "s" and not ("b" in T[i][j] or "rd" in T[i][j] or "rl" in T[i][j]))]
    fitted = [0.0]

    def settle():
        """Fit what is built to the land. The corners that must be level together (a platform's four, a ramp's two
        across each end) are joined into groups; each group stands at the mean height of its corners' ground, or
        at the water where it touches the river or the sea (a quay, a bridge: the highest water it touches, the
        bank rising to it), and never below the river beside it. Then each ramp's two ends are brought within its
        rise limit (cut and fill: both ends move towards each other, a group at the water stays)."""
        parent = {}

        def find(x):
            while parent.setdefault(x, x) != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)
        ramps = []
        for i, j, (rule, limit) in RULES:
            groups = corner_groups((i, j), rule)
            for g in groups:
                for c2 in g[1:]:
                    union(g[0], c2)
            if rule != "flat":
                ramps.append((groups[0][0], groups[1][0], limit))
        members = {}
        for c2 in list(parent):
            members.setdefault(find(c2), []).append(c2)
        level, pinned = {}, set()
        for root, cs in members.items():
            fx = [V[a2][b2] for a2, b2 in cs if fixed[a2][b2]]
            lo = max([floor.get(c2, -1e9) for c2 in cs])
            if fx:
                level[root] = max(fx)
                pinned.add(root)
            else:
                level[root] = max(sum(E[a2][b2] for a2, b2 in cs) / len(cs), lo)
        for _ in range(2000):
            moved = 0.0
            for x, y, limit in ramps:
                rx, ry = find(x), find(y)
                if rx == ry:
                    continue
                d = level[rx] - level[ry]
                if abs(d) <= limit:
                    continue
                over = abs(d) - limit
                sx = -1 if d > 0 else 1                     # the direction rx must move to close the gap
                if rx in pinned and ry in pinned:
                    continue
                if rx in pinned:
                    level[ry] += -sx * over
                elif ry in pinned:
                    level[rx] += sx * over
                else:
                    level[rx] += sx * over / 2
                    level[ry] -= sx * over / 2
                moved += over
            if moved < 0.5:
                break
        for root, cs in members.items():
            for a2, b2 in cs:
                fitted[0] += abs(V[a2][b2] - level[root])
                V[a2][b2] = level[root]
    settle()
    for vi in range(W + 1):
        for vj in range(H + 1):
            V[vi][vj] = int(round(V[vi][vj]))
    for i in range(W):
        for j in range(H):
            T[i][j]["h"] = min(V[i][j], V[i + 1][j], V[i][j + 1], V[i + 1][j + 1])

    # 10. checks on the finished model
    # the river runs downhill: from its source to its mouth its level never rises, and the land beside it is
    # nowhere lower than the river (it lies in its valley)
    prev = None
    for q in course:
        lv = river_level[q]
        if prev is not None and lv > prev:
            problems.append(f"the river rises from {prev} m to {lv} m at {q}")
        prev = lv if prev is None else min(prev, lv)
    for (a2, b2), lv in floor.items():
        if not fixed[a2][b2] and V[a2][b2] < lv - FLAT_TOL:
            problems.append(f"the land at corner {(a2, b2)} lies below the river beside it ({V[a2][b2]} m < {lv} m)")
    comps2, adj = components()
    for m in set(mass.values()):
        pieces = [c for c in comps2 if mass.get(next(iter(c))) == m]
        if len(pieces) > 1:
            problems.append(f"landmass {m} has {len(pieces)} separate road networks ({sorted(map(len, pieces), reverse=True)})")
    for q in road:
        if len(adj[q]) <= 1 and not leads_somewhere(q):
            problems.append(f"road at {q} is a dead end that leads nowhere")
    for i in range(W):
        for j in range(H):
            t = T[i][j]
            if ("rd" in t or "rl" in t) and t["k"] == "s":
                problems.append(f"route on the sea at {(i, j)}")
            if ("rd" in t or "rl" in t) and t["k"] == "w" and not t.get("br"):
                problems.append(f"route on the river without a bridge at {(i, j)}")
            rule = ground_rule((i, j)) if t["k"] != "s" or "b" in t or "rd" in t or "rl" in t else None
            if rule:
                lv = [[V[a2][b2] for a2, b2 in g2] for g2 in corner_groups((i, j), rule[0])]
                if any(max(g2) - min(g2) > FLAT_TOL for g2 in lv):
                    problems.append(f"{'something built on a slope' if rule[0] == 'flat' else 'a ramp that is not level across'} at {(i, j)}")
                elif rule[0] != "flat" and abs(lv[0][0] - lv[1][0]) > rule[1] + FLAT_TOL:
                    problems.append(f"a {'rail' if rule[1] == RAIL_RISE else 'road'} square rises {abs(lv[0][0] - lv[1][0])} m "
                                    f"(at most {rule[1]} m) at {(i, j)}")
            if (i, j) in approach and ("hs" in t or "tr" in t or "yd" in t or t["k"] in ("f", "r")):
                problems.append(f"something tall in the approach zone of #{approach[(i, j)]['n']} at {(i, j)}")
            if t.get("br"):
                m = t.get("rd")
                pcs = t.get("rl", [])
                straight_rail = len(pcs) == 1 and all(pcs[0]) and pcs[0][0][0] == -pcs[0][1][0] and pcs[0][0][1] == -pcs[0][1][1]
                if (m is not None and m not in (STRAIGHT_I, STRAIGHT_J)) or (pcs and not straight_rail):
                    problems.append(f"a bridge that is not straight (junction or bend on the bridge) at {(i, j)}")
            if "rd" in t and "rl" in t:
                pcs = t["rl"]
                ok = t["rd"] in (STRAIGHT_I, STRAIGHT_J) and len(pcs) == 1 and all(pcs[0]) and \
                    ((t["rd"] == STRAIGHT_I and pcs[0][0][0] == 0) or (t["rd"] == STRAIGHT_J and pcs[0][0][1] == 0))
                if not ok:
                    problems.append(f"level crossing at {(i, j)} is not a straight road across a straight rail")
            if "hs" in t:
                q, n = (i, j), 0                              # in a town, along the squares of houses to a road
                while q not in road and n < 64 and "hs" in (tile(*q) or {}) and (n == 0 or "um" in tile(*q)):
                    di, dj = DIRS[tile(*q)["hs"][1]]
                    q, n = (q[0] + di, q[1] + dj), n + 1
                if q not in road:
                    problems.append(f"house at {(i, j)} does not face a street")
    for p in world["parties"]:
        fp = set(footprint(p))
        net = main_network(mass[next(iter(fp))])
        if not (neighbours(fp) | fp) & net:
            problems.append(f"#{p['n']} {p['name']} is not on the road network")
    for p in world["parties"]:
        if p.get("kind") == "quay" and not any(tile(*q) and tile(*q)["k"] == "w" for q in neighbours(set(footprint(p)))):
            problems.append(f"#{p['n']} {p['name']} is a quay but not on the river bank")
    # border crossings: a road across the land border passes a customs post on each side
    # (within BORDER_POST squares along the road); a rail line passes a rail station near the border
    def along(start, steps, through):
        seen2, todo, found = {start}, deque([(start, 0)]), []
        while todo:
            q, d = todo.popleft()
            found.append(q)
            if d == steps:
                continue
            for y in adj.get(q, ()) if through == "road" else ():
                if y not in seen2:
                    seen2.add(y)
                    todo.append((y, d + 1))
        return found
    customs = {}
    for p in world["parties"]:
        if p["kind"] == "customs":
            for q in footprint(p):
                customs[q] = p["c"]
    for e in edges:
        a2, b2 = tuple(e)
        ca, cb = T[a2[0]][a2[1]]["c"], T[b2[0]][b2[1]]["c"]
        if ca and cb and ca != cb:
            for side, c in ((a2, ca), (b2, cb)):
                if not any(customs.get(q) == c for q in along(side, BORDER_POST, "road")):
                    problems.append(f"road crossing the {ca}/{cb} border at {side} has no customs post of {c} nearby")
    for r in world["routes"]:
        if r["mode"] == "rail":
            path = r["path"]
            for k in range(len(path) - 1):
                ca, cb = T[path[k][0]][path[k][1]]["c"], T[path[k + 1][0]][path[k + 1][1]]["c"]
                if ca and cb and ca != cb:
                    on_line = path + [y for q in (path[0], path[-1]) for y in neighbours({q})]
                    if not any(owner.get(q, {}).get("kind") == "terminal" for q in on_line):
                        problems.append(f"rail line '{r['id']}' crosses the {ca}/{cb} border at {path[k]} without passing a rail station (terminal)")
            for end in (path[0], path[-1]):
                if not (neighbours({end}) | {end}) & set(owner):
                    problems.append(f"rail line '{r['id']}' ends at {end} without reaching a party")
        if r["mode"] == "sea":
            for q in path_tiles(r["pts"], "rail"):
                if tile(*q)["k"] != "s":
                    problems.append(f"sea route '{r['id']}' runs over land at {q}")
            for end in (tuple(r["pts"][0]), tuple(r["pts"][-1])):
                if not any(owner.get(q, {}).get("kind") == "port" for q in neighbours({end})):
                    problems.append(f"sea route '{r['id']}' does not start or end at a port ({end})")
        if r["mode"] == "air":
            for end in (tuple(r["pts"][0]), tuple(r["pts"][-1])):
                if owner.get(end, {}).get("kind") != "airport":
                    problems.append(f"air route '{r['id']}' does not start or end at an airport ({end})")

    # pipelines: buried, crossing roads, rails and the river underneath at right angles, out of towns,
    # from a party, its platform or another pipeline to a party, metered at a land border
    platform_at = {tuple(pf["at"]): pf for pf in world.get("platforms", [])}
    for r in world["routes"]:
        if r["mode"] != "pipeline":
            continue
        path, name = r["path"], f"pipeline '{r['id']}'"
        wet = [T[i][j]["k"] == "s" for (i, j) in path]
        if any(wet) and (path[0] not in platform_at or wet != sorted(wet, reverse=True)):
            problems.append(f"{name} runs on the sea other than from an offshore platform to its landfall")
        for k, q in enumerate(path):
            t = T[q[0]][q[1]]
            if q in owner:
                problems.append(f"{name} runs through #{owner[q]['n']} {owner[q]['name']} at {q}")
            if "hs" in t or "yd" in t or "tr" in t or t["k"] == "f":
                problems.append(f"{name}: its right of way at {q} is built on or planted")
            near = {built[y]["name"] for y in ((q[0] + a2, q[1] + b2) for a2 in range(-TOWN_CLEAR, TOWN_CLEAR + 1)
                                               for b2 in range(-TOWN_CLEAR, TOWN_CLEAR + 1)) if y in built}
            for town in sorted(near):
                problems.append(f"{name} runs through or within {TOWN_CLEAR} squares of the built-up area of {town} at {q}")
            crossed = [what for what, there in (("road", "rd" in t), ("rail line", "rl" in t), ("river", t["k"] == "w")) if there]
            if not crossed:
                continue
            if k in (0, len(path) - 1):
                problems.append(f"{name} ends on a {crossed[0]} at {q}")
                continue
            a, b = path[k - 1], path[k + 1]
            along_i = a[1] == b[1]
            if not (a[0] == b[0] or along_i):
                problems.append(f"{name} bends under a {crossed[0]} at {q}; it crosses in a straight line")
                continue
            pcs = t.get("rl", [])
            if ("rd" in t and t["rd"] != (STRAIGHT_J if along_i else STRAIGHT_I)) or \
                    (pcs and not (len(pcs) == 1 and all(pcs[0]) and pcs[0][0][0] == -pcs[0][1][0] and pcs[0][0][1] == -pcs[0][1][1]
                                  and (pcs[0][0][0] == 0) == along_i)):
                problems.append(f"{name} crosses a {crossed[0]} at {q} other than at right angles under a straight piece")
        for k in range(len(path) - 1):
            ca, cb = T[path[k][0]][path[k][1]]["c"], T[path[k + 1][0]][path[k + 1][1]]["c"]
            if ca and cb and ca != cb and T[path[k][0]][path[k][1]]["k"] != "s":
                if not any(q in stations for q in path[max(0, k - METERING + 1):k + METERING + 1]):
                    problems.append(f"{name} crosses the {ca}/{cb} border at {path[k]} without a metering station within {METERING} squares")
        others = {q for o in world["routes"] if o["mode"] == "pipeline" and o is not r for q in o["path"]}
        touches = lambda q: {owner[y]["id"] for y in neighbours({q}) | {q} if y in owner}
        if not (touches(path[0]) or path[0] in platform_at or path[0] in others):
            problems.append(f"{name} starts at {path[0]} at no party, platform or other pipeline")
        if not touches(path[-1]):
            problems.append(f"{name} ends at {path[-1]} at no party")

    leg_problems, legs = check_legs(world, T, adj, owner, neighbours)
    problems += leg_problems

    for tw in world.get("towns", []):
        tw.pop("streets", None)

    model = {"W": W, "H": H, "grid": GRID, "km": KM, "approach": APPROACH, "level_m": LEVEL_M, "fitted_m": round(fitted[0]),
             "tiles": [[T[i][j] for j in range(H)] for i in range(W)], "v": V, "legs": legs}
    return model, problems


FLEET_KIND = {"road": "road", "rail": "rail", "river": "inland", "sea": "sea", "air": "air", "pipeline": "pipeline"}
CARRIER_ROLES = ("CarrierParty", "SubstituteCarrierParty", "PerformingCarrierParty", "TransportServiceProviderParty")


def check_legs(world, T, adj, owner, neighbours):
    """Every transport leg of a flow (world/documents.json, "legs") must be possible in the world: a road
    from party to party on the road network, a rail line or the river connecting them, a sea or air route
    between their port or airport, the pipelines from the producer to its customer, in the direction the
    gas flows; the carrier must have a means of that mode in its fleet; and every carrier a document of the
    flow names must carry one of its legs. Returns the problems and the legs with their way on the map
    ("path", tiles from the from-party to the to-party; a road leg's first and last tiles are its two buildings):
    the map's vehicles travel exactly these."""
    problems, legs = [], []
    party = {p["id"]: p for p in world["parties"]}

    def near(pid):
        fp = set(footprint(party[pid]))
        return fp | neighbours(fp)

    def way(starts, goals, step):
        """The shortest way from a start tile to a goal tile (a list of tiles), or None."""
        prev, todo = {q: None for q in starts}, deque(sorted(starts, key=str))
        while todo:
            q = todo.popleft()
            if q in goals:
                out = []
                while q is not None:
                    out.append(q)
                    q = prev[q]
                return out[::-1]
            for y in sorted(step(q), key=str):
                if y not in prev:
                    prev[y] = q
                    todo.append(y)
        return None

    def graph(mode, directed=False):
        g = {}
        for r in world["routes"]:
            if r["mode"] == mode:
                path = [tuple(q) for q in r["path"]]
                for a, b in zip(path, path[1:]):
                    g.setdefault(a, set()).add(b)
                    if not directed:
                        g.setdefault(b, set()).add(a)
        return g

    rail = graph("rail")
    course = graph("river")              # barges follow the river's course, not any water tile ...
    for i in range(W):                   # ... except in the estuary, which is open water: any of it is navigable
        for j in range(H):
            if T[i][j].get("es"):
                for di, dj in DIRS:
                    if 0 <= i + di < W and 0 <= j + dj < H and T[i + di][j + dj].get("es"):
                        course.setdefault((i, j), set()).add((i + di, j + dj))
    # pipelines: the gas flows from the first point of each to the last; a pipeline that ends at a party
    # feeds it, one that starts at a party (or at its platform) is fed by it
    pipe = graph("pipeline", directed=True)
    platform_of = {tuple(pf["at"]): pf["party"] for pf in world.get("platforms", [])}
    at_party = lambda q: {owner[y]["id"] for y in neighbours({q}) if y in owner}
    for r in world["routes"]:
        if r["mode"] == "pipeline":
            path = [tuple(q) for q in r["path"]]
            for pid in at_party(path[0]) | ({platform_of[path[0]]} if path[0] in platform_of else set()):
                pipe.setdefault(("party", pid), set()).add(path[0])
            for pid in at_party(path[-1]):
                pipe.setdefault(path[-1], set()).add(("party", pid))

    def route_between(mode, a, b):
        """The points of a sea or air route from a's port or airport to b's."""
        for r in world["routes"]:
            if r["mode"] != mode:
                continue
            pts = [tuple(q) for q in r["pts"]]
            for x, y, order in ((a, b, pts), (b, a, pts[::-1])):
                if pts[0] in near(x) | neighbours(near(x)) and pts[-1] in near(y) | neighbours(near(y)):
                    return order
        return None

    used_pipes = set()
    for f in world["flows"]:
        carriers = set()
        for leg in f.get("legs", []):
            m, a, b, c = leg["mode"], leg["from"], leg["to"], leg["carrier"]
            carriers.add(c)
            what = f"flow '{f['id']}': {m} leg {party[a]['identity']['name']} -> {party[b]['identity']['name']}"
            if not any(x["kind"] == FLEET_KIND[m] for x in party[c].get("fleet", [])):
                problems.append(f"{what}: carrier {party[c]['identity']['name']} has no {m} means in its fleet")
            if m == "road":
                path = way([q for q in near(a) if q in adj], {q for q in near(b) if q in adj}, lambda q: adj[q])
            elif m == "rail":
                path = way([q for q in near(a) if q in rail], {q for q in near(b) if q in rail}, lambda q: rail[q])
            elif m == "river":
                path = way([q for q in near(a) if q in course], {q for q in near(b) if q in course}, lambda q: course[q])
            elif m == "pipeline":
                path = way([("party", a)], {("party", b)}, lambda q: pipe.get(q, ()))
                if path:
                    path = [q for q in path if q[0] != "party"]
                    used_pipes.update(zip(path, path[1:]))
            else:
                path = route_between(m, a, b)
            if not path:
                problems.append(f"{what}: no {m} connection between them on the map")
                continue
            if m == "road":                  # a truck leaves from its building and drives into the other
                gate = lambda pid, q: next((y for y in footprint(party[pid]) if abs(y[0] - q[0]) + abs(y[1] - q[1]) == 1), None)
                path = [x for x in [gate(a, path[0])] + path + [gate(b, path[-1])] if x]
            legs.append({"flow": f["id"], "mode": m, "from": a, "to": b, "carrier": c, "path": [list(q) for q in path]})
        for d in world["documents"]:
            if d["flow"] != f["id"]:
                continue
            for path_, pid in d["parties"].items():
                if path_.split("/")[-1] in CARRIER_ROLES and pid not in carriers:
                    problems.append(f"flow '{f['id']}': {d['doc']} names carrier {party[pid]['identity']['name']} "
                                    f"({path_}), but no leg of the flow is carried by it")
    # every pipeline carries a pipeline leg in the direction of the flow, or feeds a producer from its platform
    producers = {leg["from"] for leg in legs if leg["mode"] == "pipeline"}
    for r in world["routes"]:
        if r["mode"] != "pipeline":
            continue
        path = [tuple(q) for q in r["path"]]
        src = platform_of.get(path[0])
        feeds = src in producers and src in at_party(path[-1])
        if not feeds and not all(e in used_pipes for e in zip(path, path[1:])):
            problems.append(f"pipeline '{r['id']}' carries no pipeline leg of a flow in the direction of the flow")
    return problems, legs


def main():
    sys.path.insert(0, os.path.dirname(__file__))
    import world_data
    world = world_data.load()
    model, problems = build(world)
    for line in problems:
        print("problem:", line, file=sys.stderr)
    flat = [t for col in model["tiles"] for t in col]
    houses = sum(1 for t in flat if "hs" in t)
    roads = sum(1 for t in flat if "rd" in t)
    print(f"world model: {len(world['parties'])} parties, {len(world.get('towns', []))} towns, "
          f"{houses} houses, {roads} road tiles, {sum(1 for t in flat if t['k'] == 'w')} river tiles, "
          f"{sum(1 for t in flat if t.get('br'))} bridges: "
          + ("no problems" if not problems else f"{len(problems)} problems"), file=sys.stderr)
    for tw in world.get("towns", []) + world.get("localities", []):
        b = tw["built"]
        out = {k: [p for p, v in b["parties"].items() if v == k] for k in ("edge", "outside")}
        print(f"  {tw['name']}: built up {b['km2']} km2, {b['across_km']} km across (a circle of that area), "
              f"{b['west_east_km']} km west-east, {b['north_south_km']} km north-south; "
              f"{sum(1 for v in b['parties'].values() if v == 'inside')} parties inside, at the edge: "
              f"{', '.join(out['edge']) or '-'}, outside: {', '.join(out['outside']) or '-'}", file=sys.stderr)
    if len(sys.argv) > 1:
        json.dump({"model": model, "routes": world["routes"]}, open(sys.argv[1], "w"), separators=(",", ":"))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
