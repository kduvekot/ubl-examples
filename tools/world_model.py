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
  rd  road connections, an 8-bit mask (DIRS8): 1 = +i, 2 = +j, 4 = -i, 8 = -j, and the diagonal steps 16 = (+i, +j),
      32 = (-i, +j), 64 = (-i, -j), 128 = (+i, -j), which pass through the corner the two squares share (O152 stage 3)
  rl  rail pieces, each a pair of directions to the neighbours it leads to ([di, dj], diagonals included, or null
      for the centre)
  br  1 for a bridge square: a road or rail crosses water here, or a route lists it as a bridge (a viaduct over a
      valley, or a bridge over another way)
  tn  1 for a tunnel square: the way runs under the land
  dk  on a bridge or tunnel square and on its two approaches: the height of the way at the square's middle, in
      metres (the deck runs straight from the ground at the far edge of one approach to the far edge of the other)
  ab  1 for a bridge's or a tunnel's approach (an embankment or a cutting: its ground is left as it is)
  ov  where a road and a rail line cross on a bridge (an overpass): "road" or "rail", the way on the bridge
  hb  1 for a town's own harbour (map "towns", "harbour": Larkmouth's quay, without a party)
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
  mf  on a square of a managed forest (world/terrain.json "managed_forests", the forest of Upland State): its
      compartments, a string of SUB x SUB characters (the sub-square a along i, b along j at a * SUB + b), each the
      number of its age class (0 felled and replanted, 1 young, 2 pole, 3 mature) or "." outside the forest
  lu  the land use of the square's cells (tools/land_use.py: who farms the land around the towns and villages, and
      how): a string of S x S characters, the cell a along i, b along j at a * S + b (S = 4 on the mainland, cells
      of 875 m as the sub-squares; 8 on Lisavu, cells of 437.5 m): d field, p pasture or hay meadow, o orchard,
      olive grove or vineyard, f wood, g open grass or grazing, h scrub or heath, r rock, m marsh, s and w water;
      given where its cells are not all of the square's kind ("k" is the most common kind of its land cells,
      pasture counted as grass and orchards as fields)
  ud  in a town that gives its districts (map "towns", "districts"): the district of each built-up sub-square, a
      string of SUB x SUB characters (as "um"), the district's index in its town's list (0-9, a-z) or "."

Structural rules (the build stops when one is broken):
  * buildings do not share tiles and do not stand on roads, rails or water,
    except parties marked "on" a route (customs posts, rail stations);
  * every party has access: a road next to it, or rail for rail parties,
    or water for ports and quays; missing access roads are laid by the model, over the terrain with the router of
    the map's routes (tools/routing.py; tools/lay_routes.py writes them into the map, so that the map holds every
    road and the model normally lays none);
  * every town and village is built up over the area its built_km gives (map "towns", "localities", "villages"),
    a town as the union of its districts where it gives them (each a circle of its size round its centre, grown
    to the decided area), on land,
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
  * what is built is fitted to the land: buildings, houses, yards, stations, junctions, ends and bends of 90 degrees
    between two sides stand on a platform (four corners level); a road or rail square a way passes straight through,
    or bends 45 degrees in, is a ramp, level across, rising at most RAIL_RISE = 70 m (rail, 2 %), ROAD_RISE = 245 m
    (a main road, 7 %) or ROAD_RISE_MINOR = 350 m (a minor road, 10 %) along its direction; on a diagonal the
    ramp runs from corner to corner, level across the other two corners;
  * roads, rails and pipelines are given square by square (O152 stage 3, tools/lay_routes.py), each square a
    neighbour of the last, diagonals included; no way crosses another, or passes between two squares of water,
    through the corner two squares share;
  * bridges and tunnels: a run of bridge or tunnel squares is straight, has an approach on the ground at each end
    and holds no junction; its deck rises no more than its length allows; a bridge's deck stands above the ground
    (at most BRIDGE_FREE below it) or the water, a tunnel's way at least TUNNEL_COVER under the ground; a road may
    cross a rail line (or a rail line a road) on a bridge;
  * the river runs downhill: its water lies at the heights its route gives,
    never rising from source to mouth, and the land beside it is nowhere lower
    than the river (it lies in its valley);
  * roads and rails cross the river only on straight bridges; level
    crossings are a straight road across a straight rail, at right angles or at 45 degrees (a skew crossing);
  * the barges keep below the rapids above Ferrano (world/terrain.json "rapids", O153): no river route and no quay
    at or above them;
  * tall structures (a mast, a cooling tower) keep TALL_CLEARANCE = 2 squares
    (7 km) from an airport and its approach zones;
  * an airport has an approach zone of APPROACH = 3 squares (10.5 km) beyond
    each runway end, low and flat at runway height, with nothing tall in it;
  * the land border follows the watershed north of the crossing and the river below it (all land south of
    the river is Urvania): tools/terrain.py draws it into the terrain's countries;
  * a road across a land border passes a customs post on each side (within
    BORDER_POST = 3 squares, 10.5 km, along the road); a rail line across it
    passes a rail station (a terminal, where the train is cleared, anywhere on the
    line); rail lines end at a party, a town's harbour or another rail line (a branch);
  * sea routes run over water from port to port, air routes from airport
    to airport;
  * pipelines are buried: they run square by square over the land (as laid by tools/lay_routes.py),
    cross a road, a rail line or the river underneath, straight on under a straight piece, at right angles or
    at 45 degrees, never along them, and keep out of towns; nothing is
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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import routing  # noqa: E402  (tools/routing.py: the router of roads, rails and pipelines over the terrain)

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
DIAG = [(1, 1), (-1, 1), (-1, -1), (1, -1)]       # bit 4..7: the diagonal steps, through the corner two squares share
DIRS8 = DIRS + DIAG
ESTUARY = 1.5                                     # a river this wide (squares, 5 km) is open water: an estuary
LEVEL_M = 1                                       # model "v" holds metres (since O152 stage 1; it was levels of 100 m)
RAIL_RISE = 70                                    # metres a rail square may rise along its direction (2 % of 3.5 km)
ROAD_RISE = 245                                   # metres a main road square may rise along its direction (7 %)
ROAD_RISE_MINOR = 350                             # metres a minor road square may rise (10 %; access roads, streets)
BRIDGE_FREE = 25                                  # metres the ground may stand above a bridge deck's line (its abutments)
TUNNEL_COVER = 20                                 # metres of ground at least above a tunnel's line
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
    """The squares of a route. Given square by square (each point a neighbour of the last, diagonals included:
    roads, rails and pipelines since O152 stage 3), as given. Otherwise between waypoints: roads an L per pair of
    waypoints (longer leg first); rail (and the river's course, the sea lanes) a staircase that keeps as close as
    it can to the straight line between the waypoints."""
    if len(pts) > 1 and all(max(abs(b[0] - a[0]), abs(b[1] - a[1])) == 1 for a, b in zip(pts, pts[1:])):
        return [tuple(q) for q in pts]                # given square by square (8-connected, O152 stage 3)
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
    for tw in world.get("towns", []) + world.get("localities", []) + world.get("villages", []):
        tw["r"] = tw["built_km"] / 2 / KM
    T = [[None] * H for _ in range(W)]
    terrain, E = load_terrain()
    import land_use                                 # tools/land_use.py: the land use round the towns and villages
    managed_sq = [(i, j) for mf in terrain.get("managed_forests", []) for i, j, _ in mf["squares"]]
    LU = land_use.tiles(land_use.land_use(ROOT, terrain, world, managed_sq), W, H)

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
    for mf in terrain.get("managed_forests", []):
        for i, j, ages in mf["squares"]:
            T[i][j]["mf"] = ages
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

    # 3a. a town's harbour (map "towns", "harbour"; Larkmouth, O153): a quay square with open water in front, like
    #     a port, without a party
    harbours = {}
    for tw in world.get("towns", []):
        hb = tw.get("harbour")
        if not hb:
            continue
        q = tuple(hb["at"])
        t = tile(*q)
        if not t or t["k"] in ("s", "w") or q in owner:
            problems.append(f"the harbour of {tw['name']} at {q} must stand on free land")
            continue
        harbours[q] = tw
        t["k"], t["hb"] = "g", 1
        di, dj = hb["water"]
        if (tile(q[0] + di, q[1] + dj) or {}).get("k") != "s":
            problems.append(f"the harbour of {tw['name']} at {q} does not face the sea")
        for k in range(1, PORT_BASIN + 1):
            t2 = tile(q[0] + di * k, q[1] + dj * k)
            if t2 and "b" not in t2:
                t2["k"], t2["c"], t2["h"] = "s", None, 0

    # 3b. pipelines and their stations. A pipeline is buried: its tiles keep their terrain, but its right
    #     of way is kept clear (no house, yard, tree or forest on it). A border metering station stands
    #     on the pipeline, on flat land. Since O152 stage 3 a pipeline is given square by square, as laid
    #     over the land (tools/lay_routes.py): each square a neighbour of the last, diagonals included.
    pipes = {}
    for r in world["routes"]:
        if r["mode"] == "pipeline":
            pts = r["pts"]
            for a2, b2 in zip(pts, pts[1:]):
                if max(abs(b2[0] - a2[0]), abs(b2[1] - a2[1])) != 1:
                    problems.append(f"pipeline '{r['id']}' jumps from {tuple(a2)} to {tuple(b2)}: give it square by square")
            r["path"] = pipes[r["id"]] = path_tiles(pts, "road")
    corridor = {q for path in pipes.values() for q in path}
    pipe_ends = frozenset(q for path in pipes.values() for q in (path[0], path[-1]))
    stations = {}
    for st in world.get("stations", []):
        q = tuple(st["at"])
        stations[q] = st
        t = tile(*q)
        if not t or t["k"] in ("s", "w") or q in owner or q in harbours:
            problems.append(f"{st['kind']} station at {q} must stand on free land")
            continue
        t["k"], t["ms"] = "g", 1
        if q not in corridor:
            problems.append(f"{st['kind']} station at {q} is not on a pipeline")
    for q in corridor:
        t = tile(*q)
        if t and t["k"] == "f":
            t["k"] = "g"

    # 3c. a sea route is a shipping lane: land on it becomes water, unless something is built there
    for r in world["routes"]:
        if r["mode"] == "sea":
            for q in path_tiles(r["pts"], "rail"):
                t = tile(*q)
                if t and t["k"] != "s" and q not in owner and q not in harbours:
                    t["k"], t["c"], t["h"] = "s", None, 0

    # 4. routes. Road connections are explicit edges between neighbouring tiles (diagonal neighbours included, O152
    #    stage 3); nothing is connected just because two road tiles touch. A route's squares on the river, and those
    #    it lists as "bridges", are bridge squares (model "br": the deck spans them); those it lists as "tunnels" are
    #    tunnel squares (model "tn": the way runs under the land). A road route has a class ("main", 7 %, or "minor",
    #    10 %; the model's own streets and access roads are minor).
    road, rails, edges, into = set(), {}, set(), {}
    road_rise = {}                                     # road square -> the rise it may have (the strictest road on it)
    struct = {}                                        # square -> "bridge" | "tunnel"
    laid = []                                          # (name, mode, path) of every road and rail laid: for the checks

    def link(a, b):
        edges.add(frozenset((a, b)))

    struct_way = {}                                    # structure square -> the mode of the way on the deck
    abut = {}                                          # a structure's approach square -> the way
    name_of = {}

    def mark(q, structures, mode):
        t = T[q[0]][q[1]]
        kind_ = "bridge" if t["k"] == "w" else structures.get(q)
        if kind_:
            if q in struct_way and struct_way[q] != mode:
                problems.append(f"a road and a rail line share the {kind_} at {q}")
            struct[q], struct_way[q] = kind_, mode
            t["br" if kind_ == "bridge" else "tn"] = 1
        elif t["k"] == "s":
            t["k"] = "g"

    def lay_road(path, rise=ROAD_RISE_MINOR, structures=None, name="road"):
        """Lay a road along a chain of neighbouring tiles; water tiles and the listed bridges become bridges, the
        listed tunnels tunnels."""
        for k, q in enumerate(path):
            mark(q, structures or {}, "road")
            road.add(q)
            road_rise[q] = min(road_rise.get(q, 1e9), rise)
            if k:
                link(path[k - 1], q)
        if path:
            if name != "chain":
                laid.append((name, "road", list(path)))
            note_abut(path, "road")

    def note_abut(path, mode):
        """The approaches of the structures along a way: the squares before and after each run of them."""
        for k, q in enumerate(path):
            if struct.get(q) and struct_way.get(q) == mode:
                for y in (path[k - 1] if k else None, path[k + 1] if k + 1 < len(path) else None):
                    if y is not None and not (struct.get(y) and struct_way.get(y) == mode):
                        abut[y] = name_of.get(mode, mode)

    def enter(q, building_tile):
        into.setdefault(q, set()).add((building_tile[0] - q[0], building_tile[1] - q[1]))

    for r in world["routes"]:
        if r["mode"] in ("road", "rail"):
            path = path_tiles(r["pts"], r["mode"])
            r["path"] = path
            sts = {tuple(q): "bridge" for q in r.get("bridges", [])}
            sts.update({tuple(q): "tunnel" for q in r.get("tunnels", [])})
            if r["mode"] == "road":
                rise = ROAD_RISE if r.get("class") == "main" else ROAD_RISE_MINOR
                chain, after = [], None
                for k, q in enumerate(path):
                    p = owner.get(q)
                    if p and p.get("on") != "road":
                        if 0 < k < len(path) - 1:
                            problems.append(f"#{p['n']} {p['name']} stands on road route '{r['id']}' at {q}")
                        if chain:
                            enter(chain[-1], q)          # the road ends at this building
                        lay_road(chain, rise, sts, "chain")
                        chain, after = [], q
                        continue
                    if not chain and after and abs(after[0] - q[0]) + abs(after[1] - q[1]) == 1:
                        enter(q, after)                  # the road leaves this building
                    chain.append(q)
                lay_road(chain, rise, sts, "chain")
                laid.append((r["id"], "road", list(path)))  # the whole way, its buildings included: for the checks
            else:
                for k, (i, j) in enumerate(path):
                    p = owner.get((i, j))
                    if p and p.get("on") != "rail" and 0 < k < len(path) - 1:
                        problems.append(f"#{p['n']} {p['name']} stands on rail route '{r['id']}' at {(i, j)}")
                    prev = (path[k - 1][0] - i, path[k - 1][1] - j) if k else None
                    nxt = (path[k + 1][0] - i, path[k + 1][1] - j) if k < len(path) - 1 else None
                    if not p or p.get("on") == "rail":
                        mark((i, j), sts, "rail")
                        rails.setdefault((i, j), []).append([prev, nxt])
                laid.append((r["id"], "rail", list(path)))
                note_abut(path, "rail")

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
        return bool(t) and q not in owner and q not in rails and q not in stations and q not in harbours and q not in struct \
            and q not in abut \
            and (t["k"] not in ("s", "w") or (water_ok and t["k"] == "w"))

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

    land = None

    access = []                                         # the roads the model lays itself: {to, name, path, bridges}

    def connect(starts, goal, avoid=frozenset(), to=None):
        """The cheapest way from any start tile to a goal tile over the terrain, laid as a minor road
        (tools/routing.py, the same cost as the map's routes: gradient, cross-fall, ground, turns; 8-connected). It
        never crosses a land border, never joins at a bridge, a tunnel or a level crossing, and crosses rail lines
        and pipelines only straight on at right angles, the river only on a bridge."""
        nonlocal land
        if land is None:
            land = routing.Land([[T[i][j]["k"] for j in range(H)] for i in range(W)],
                                [[T[i][j]["c"] for j in range(H)] for i in range(W)], E, W, H, estuary, river_level)
            try:
                land.load_fine(ROOT, terrain["rasters"])    # the same cost as tools/lay_routes.py (Pillow)
            except ImportError:
                pass
        built_ = routing.Built()
        built_.sq["road"] = set(road)
        for e in edges:
            a2, b2 = tuple(e)
            built_.steps["road"].setdefault(a2, set()).add((b2[0] - a2[0], b2[1] - a2[1]))
            built_.steps["road"].setdefault(b2, set()).add((a2[0] - b2[0], a2[1] - b2[1]))
        for q, pcs in rails.items():
            built_.sq["rail"].add(q)
            built_.steps["rail"][q] = {d for pc in pcs for d in pc if d}
        for path in pipes.values():
            built_.add("pipeline", path)
        built_.add("river", course)
        built_.blocked = set(owner) | set(stations) | set(harbours)
        built_.structures = set(struct) | set(abut)
        goals = {q for q in goal if q not in rails and q not in struct and q not in abut and q not in corridor}
        starts = [q for q in starts if q not in rails and q not in struct and q not in abut]
        if not starts:
            return None
        got = routing.route(land, built_, "minor", list(starts), goals, avoid=set(avoid) | (set(corridor) - set(starts)))
        if not got:
            return None
        path, sts = got
        lay_road(path, ROAD_RISE_MINOR, sts, f"access-{to['id']}" if to else "link")
        access.append({"to": to["id"] if to else None, "name": to["name"] if to else "the network",
                       "path": [list(q) for q in path],
                       "bridges": [list(q) for q in path if sts.get(q) == "bridge" or T[q[0]][q[1]]["k"] == "w"]})
        return path

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
        path = connect(starts, net, avoid=pipe_ends, to=p)
        if not path:
            problems.append(f"#{p['n']} {p['name']} cannot be reached by road")
            continue
        enter(path[0], next(b2 for b2 in fp if abs(b2[0] - path[0][0]) + abs(b2[1] - path[0][1]) == 1))

    # 5a. the land use (tools/land_use.py): the kind of each square and the land use of its cells follow from who
    #     farms it. Applied after the access roads, which are laid over the terrain's own cover (as
    #     tools/lay_routes.py lays every way); not on the parties' squares, a harbour or a station; on a pipeline's
    #     right of way nothing is planted (its wood is open grass).
    for (i, j), (lu, kind) in LU.items():
        t = T[i][j]
        if t["k"] in ("s", "w") or "b" in t or "hb" in t or "ms" in t or kind is None or (i, j) in managed_sq:
            continue
        if (i, j) in corridor:
            lu = lu.replace("f", "g")
            kind = "g" if kind == "f" else kind
        t["k"] = kind
        if lu != kind * len(lu):
            t["lu"] = lu

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
            if "lu" in t:                                    # no wood in the approach zone either
                t["lu"] = t["lu"].replace("f", "g")
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

    for tw in world.get("towns", []) + world.get("localities", []) + world.get("villages", []):
        ci, cj, rad = tw["c"][0], tw["c"][1], tw["r"]
        pop = max(tw["population"]) if isinstance(tw.get("population"), list) else tw.get("population", 0)
        reach = math.ceil(rad * 3) + (2 if rad > .5 else 1)  # a village of a square or less: the squares round it
        box_ = [(i, j) for i in range(ci - reach, ci + reach + 1) for j in range(cj - reach, cj + reach + 1)
                if buildable((i, j)) and (i, j) not in built]
        ways = [q for q in road if abs(q[0] - ci) <= reach + 1 and abs(q[1] - cj) <= reach + 1]

        dists = tw.get("districts") or []

        def district(x, y):
            """(index, how far (x, y) lies out of the district it lies deepest in, in shares of its radius)."""
            return min(((k, math.hypot(x - ds["at"][0], y - ds["at"][1]) / (ds["r_km"] / KM)) for k, ds in enumerate(dists)),
                       key=lambda kd: kd[1])

        def spread(x, y):
            """How far (x, y) lies out, in squares: from the centre (or, in a town that gives its districts, from
            the district it lies deepest in, as a share of that district's radius times the town's), warped by the
            noise, nearer along the roads."""
            wx = (noise(x * 1.7 + 31.7, y * 1.7 - 12.9) - .5) * 2 * BUILT_WARP * rad
            wy = (noise(x * 1.7 - 7.3, y * 1.7 + 45.1) - .5) * 2 * BUILT_WARP * rad
            if dists:
                d = district(x + wx, y + wy)[1] * rad
            else:
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
            if dists:                                  # the district of each built sub-square (model "ud")
                x, y = q[0] - .5 + (a2 + .5) / SUB, q[1] - .5 + (b2 + .5) / SUB
                k = district(x, y)[0]
                ud = list(t.get("ud", "." * SUB * SUB))
                ud[a2 * SUB + b2] = "0123456789abcdefghijklmnopqrstuvwxyz"[k]
                t["ud"] = "".join(ud)
        top = 4 if pop >= 250_000 else 3 if pop >= 20_000 else 1
        R_eq = math.sqrt(len(cells) / math.pi) / SUB       # the radius of a circle of the built-up area, in squares
        for q in {q for q, _, _ in cells}:
            t = tile(*q)
            u = math.hypot(q[0] - ci, q[1] - cj) / R_eq * .8 if dists else spread(*q) / scale
            t["ul"] = min(top, 4 if u < .22 else 3 if u < .45 else 2 if u < .75 else 1)
            if q in owner or q in road or q in rails or q in corridor or q in harbours or "hs" in t:
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
        return any((q[0] + di, q[1] + dj) in owner or (q[0] + di, q[1] + dj) in harbours or "hs" in (tile(q[0] + di, q[1] + dj) or {})
                   for di, dj in DIRS)

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

    # road connections per tile: edges to neighbouring road tiles (the eight neighbours: bits 0..7 of DIRS8), plus
    # the building a road ends at
    for (i, j) in road:
        mask = 0
        for bit, (di, dj) in enumerate(DIRS8):
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
    HALF = math.sqrt(2) / 2                          # a diagonal square's ramp: two halves of a diagonal

    def links(q, mode=None):
        """The directions the road and the rail of square q lead to (a building a road ends at included); only the
        road's or the rail's if mode is given."""
        t = T[q[0]][q[1]]
        out = set()
        m = t.get("rd", 0) if q in road and mode != "rail" else 0
        out |= {d for bit, d in enumerate(DIRS8) if m & (1 << bit)}
        if mode != "road":
            for pc in rails.get(q, ()):
                out |= {tuple(d) for d in pc if d}
        return out

    def overpass(q):
        """For a bridge square that also holds a way on the ground (a road over a rail line, or a rail line over
        a road): the mode of that way below; else None."""
        if struct.get(q) != "bridge" or T[q[0]][q[1]]["k"] == "w":
            return None
        under = "rail" if struct_way.get(q) == "road" else "road"
        return under if (q in rails if under == "rail" else q in road) else None

    def shape(ls):
        """The ramp of a square a way passes through, from the two directions it leads to: straight along i or j
        ('ramp-i', 'ramp-j'), straight on a diagonal ('ramp-d' from the north-west corner to the south-east one,
        'ramp-a' from the north-east corner to the south-west one), a bend of 45 degrees along its straight side's
        axis; a bend of 90 degrees between two sides is a platform ('flat')."""
        a2, b2 = sorted(ls)
        ortho = [d for d in (a2, b2) if d[0] == 0 or d[1] == 0]
        if len(ortho) == 1:
            return "ramp-i" if ortho[0][1] == 0 else "ramp-j"
        if a2[0] == -b2[0] and a2[1] == -b2[1]:
            if len(ortho) == 2:
                return "ramp-i" if a2[1] == 0 else "ramp-j"
            return "ramp-d" if a2[0] == a2[1] else "ramp-a"
        if len(ortho) == 2:
            return "flat"
        v = (b2[0] - a2[0], b2[1] - a2[1])               # two diagonals at right angles: along their chord
        return "ramp-i" if v[1] == 0 else "ramp-j"

    def ground_rule(q):
        """(shape, rise limit in metres for a whole square) or None (free terrain) for the tile at q. Shapes: 'flat'
        (four corners level), 'ramp-i', 'ramp-j', 'ramp-d', 'ramp-a' (see shape())."""
        t = T[q[0]][q[1]]
        if q in river_level and t["k"] == "w" and not t.get("br"):
            return None                                     # the river falls along its course (fixed corners)
        if q in abut:
            return None                                     # an approach: the way on its embankment or in its cutting
        if q in struct:
            under = overpass(q)
            if not under:
                return None                                 # a bridge spans the ground, a tunnel runs under it
            ls = links(q, under)                            # an overpass: the ground fitted to the way below
            return (shape(ls), RAIL_RISE if under == "rail" else road_rise.get(q, ROAD_RISE_MINOR)) if len(ls) == 2 else ("flat", 0)
        if t["k"] in ("s", "w") or "b" in t or "hs" in t or "yd" in t or "ms" in t or "hb" in t or (q in approach and t["k"] != "s"):
            return ("flat", 0)
        if q in road and q in rails:
            return ("flat", 0)                              # level crossing
        if q in road or q in rails:
            ls = links(q)
            if len(ls) != 2 or len(rails.get(q, ())) > 1:
                return ("flat", 0)                          # an end, a junction, a siding's points
            return (shape(ls), road_rise.get(q, ROAD_RISE_MINOR) if q in road else RAIL_RISE)
        return None

    def corner_groups(q, rule):
        """The corners of square q that stand level together, in order along the way; and the ramps between them
        (pairs of group indexes, the share of the square's rise limit)."""
        i, j = q
        if rule == "flat":
            return [[(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]], []
        if rule == "ramp-i":                                # level across the road, along each of its ends
            return [[(i, j), (i, j + 1)], [(i + 1, j), (i + 1, j + 1)]], [(0, 1, 1.0)]
        if rule == "ramp-j":
            return [[(i, j), (i + 1, j)], [(i, j + 1), (i + 1, j + 1)]], [(0, 1, 1.0)]
        if rule == "ramp-d":                                # level across the diagonal: the two other corners
            return [[(i, j)], [(i + 1, j), (i, j + 1)], [(i + 1, j + 1)]], [(0, 1, HALF), (1, 2, HALF)]
        return [[(i + 1, j)], [(i, j), (i + 1, j + 1)], [(i, j + 1)]], [(0, 1, HALF), (1, 2, HALF)]

    def shared(a2, b2):
        """The corners two neighbouring squares share: an edge's two, or one for diagonal neighbours."""
        ca = {(a2[0] + x, a2[1] + y) for x in (0, 1) for y in (0, 1)}
        return sorted(ca & {(b2[0] + x, b2[1] + y) for x in (0, 1) for y in (0, 1)})

    # the structures along the ways: each a run of bridge or tunnel squares with an approach square at each end (an
    # embankment or a cutting, its ground left as it is): the deck runs straight from the ground at the far edge (or
    # corner) of one approach to the ground at the far edge of the other
    runs = []                    # (way, kind, squares with the approaches, entry corners, exit corners, rise limit, centres)
    for name, mode, path in laid:
        k = 0
        on = lambda q: q in struct and struct_way.get(q) == mode and q not in owner
        while k < len(path):
            if not on(path[k]):
                k += 1
                continue
            k1 = k
            while k1 + 1 < len(path) and on(path[k1 + 1]):
                k1 += 1
            sq = path[k:k1 + 1]
            if k < 2 or k1 > len(path) - 3 or path[k - 1] in owner or path[k1 + 1] in owner:
                problems.append(f"{mode} '{name}': a {struct[sq[0]]} without an approach on the ground at each end at {sq[0]}")
            else:
                seq = path[k - 1:k1 + 2]
                steps = [(b2[0] - a2[0], b2[1] - a2[1]) for a2, b2 in zip(seq, seq[1:])]
                if len(set(steps)) != 1:
                    problems.append(f"{mode} '{name}': the {struct[sq[0]]} at {sq[0]} is not straight")
                if len({struct[q] for q in sq}) > 1:
                    problems.append(f"{mode} '{name}': a bridge runs into a tunnel at {sq[0]}")
                ell = lambda a2, b2: math.hypot(b2[0] - a2[0], b2[1] - a2[1])
                pos = [ell(path[k - 2], seq[0]) / 2]
                for a2, b2 in zip(seq, seq[1:]):
                    pos.append(pos[-1] + ell(a2, b2))
                total = pos[-1] + ell(seq[-1], path[k1 + 2]) / 2
                lim = RAIL_RISE if mode == "rail" else min(road_rise.get(path[k - 1], ROAD_RISE), road_rise.get(path[k1 + 1], ROAD_RISE))
                runs.append((name, struct[sq[0]], seq, shared(path[k - 2], seq[0]), shared(seq[-1], path[k1 + 2]), lim * total,
                             [x / total for x in pos]))
                for q in (seq[0], seq[-1]):
                    abut[q] = name
            k = k1 + 1

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
            groups, pairs = corner_groups((i, j), rule)
            for g in groups:
                find(g[0])
                for c2 in g[1:]:
                    union(g[0], c2)
            for x, y, share in pairs:
                ramps.append((groups[x][0], groups[y][0], limit * share))
        for name, kind_, sq, ent, ext, lim, _ in runs:  # a deck: its two ends within the rise its length allows
            for g in (ent, ext):
                find(g[0])
                for c2 in g[1:]:
                    union(g[0], c2)
            ramps.append((ent[0], ext[0], lim))
        members = {}
        for c2 in list(parent):
            members.setdefault(find(c2), []).append(c2)
        level, pinned, low = {}, set(), {}
        for root, cs in members.items():
            fx = [V[a2][b2] for a2, b2 in cs if fixed[a2][b2]]
            lo = max([floor.get(c2, -1e9) for c2 in cs])
            low[root] = lo
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
                for r_ in (rx, ry):                         # never below the river beside it
                    if level[r_] < low[r_]:
                        level[r_] = low[r_]
                moved += over
            if moved < 0.5:
                break
        for root, cs in members.items():
            for a2, b2 in cs:
                fitted[0] += abs(V[a2][b2] - level[root])
                V[a2][b2] = level[root]
                if root in pinned:
                    at_water.add((a2, b2))
    at_water = set()                                    # corners of what is built at the water (a quay, a bridgehead)
    settle()
    for vi in range(W + 1):
        for vj in range(H + 1):
            V[vi][vj] = int(round(V[vi][vj]))
    for i in range(W):
        for j in range(H):
            T[i][j]["h"] = min(V[i][j], V[i + 1][j], V[i][j + 1], V[i + 1][j + 1])
    # the decks: a bridge's or a tunnel's way runs straight from the ground at one end to the ground at the other;
    # model "dk" is its height at the middle of each of its squares (metres)
    structures = []
    for name, kind_, seq, ent, ext, lim, frac in runs:
        h0, h1 = V[ent[0][0]][ent[0][1]], V[ext[0][0]][ext[0][1]]
        for f, q in zip(frac, seq):
            T[q[0]][q[1]]["dk"] = int(round(h0 + (h1 - h0) * f))
        for q in (seq[0], seq[-1]):
            T[q[0]][q[1]]["ab"] = 1
            if len(links(q)) != 2 or (q in road and q in rails) or len(rails.get(q, ())) > 1 or q in struct:
                problems.append(f"the approach of the {kind_} of '{name}' at {q} holds a junction or another way")
        sq = seq[1:-1]
        km_ = round(math.hypot(sq[-1][0] - seq[0][0], sq[-1][1] - seq[0][1]) * KM, 1)
        rise = abs(h1 - h0)
        if rise > lim + FLAT_TOL:
            problems.append(f"the {kind_} of '{name}' at {sq[0]} rises {rise} m on its deck (at most {round(lim)} m)")
        ground = lambda q: river_level[q] if T[q[0]][q[1]]["k"] == "w" and q in river_level else \
            sum(V[q[0] + a2][q[1] + b2] for a2 in (0, 1) for b2 in (0, 1)) / 4
        for q in sq:
            t = T[q[0]][q[1]]
            g = ground(q)
            if kind_ == "bridge" and g > t["dk"] + BRIDGE_FREE:
                problems.append(f"the bridge of '{name}' at {q} runs into the ground ({round(g)} m, the deck {t['dk']} m)")
            if kind_ == "tunnel" and g < t["dk"] + TUNNEL_COVER:
                problems.append(f"the tunnel of '{name}' at {q} has too little ground above it ({round(g)} m, the way {t['dk']} m)")
        structures.append({"way": name, "kind": kind_, "squares": [list(q) for q in sq], "approaches": [list(seq[0]), list(seq[-1])],
                           "km": km_, "ends_m": [h0, h1],
                           "deck_above_m": max(0, round(max(T[q[0]][q[1]]["dk"] - ground(q) for q in sq))) if kind_ == "bridge" else None,
                           "cover_m": round(min(ground(q) - T[q[0]][q[1]]["dk"] for q in sq)) if kind_ == "tunnel" else None,
                           "over": sorted({T[q[0]][q[1]]["k"] == "w" and ("estuary" if q in estuary else "river") or
                                           (("rail" if q in rails and struct_way[q] == "road" else "road" if q in road and struct_way[q] == "rail"
                                             else "valley")) for q in sq}) if kind_ == "bridge" else None})

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
        if not fixed[a2][b2] and (a2, b2) not in at_water and V[a2][b2] < lv - FLAT_TOL:
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
                groups, pairs = corner_groups((i, j), rule[0])
                lv = [[V[a2][b2] for a2, b2 in g2] for g2 in groups]
                if any(max(g2) - min(g2) > FLAT_TOL for g2 in lv):
                    problems.append(f"{'something built on a slope' if rule[0] == 'flat' else 'a ramp that is not level across'} at {(i, j)}")
                else:
                    for x, y, share in pairs:
                        if abs(lv[x][0] - lv[y][0]) > rule[1] * share + FLAT_TOL:
                            problems.append(f"a {'rail' if rule[1] == RAIL_RISE else 'road'} square rises {abs(lv[x][0] - lv[y][0])} m "
                                            f"(at most {round(rule[1] * share)} m) at {(i, j)}")
            if (i, j) in approach and ("hs" in t or "tr" in t or "yd" in t or t["k"] in ("f", "r")):
                problems.append(f"something tall in the approach zone of #{approach[(i, j)]['n']} at {(i, j)}")
            if (i, j) in struct:
                under = overpass((i, j))
                st_ = lambda u, v: u[0] == -v[0] and u[1] == -v[1]
                ls = links((i, j), struct_way[(i, j)])
                ok = len(ls) == 2 and st_(*ls) and len(t.get("rl", [])) <= 1
                if ok and under:
                    us = links((i, j), under)
                    ok = len(us) == 2 and st_(*us) and (lambda u, v: u[0] * v[1] - u[1] * v[0] != 0)(sorted(ls)[0], sorted(us)[0])
                    t["ov"] = struct_way[(i, j)]
                elif ok and ("rd" in t and "rl" in t):
                    ok = False
                if not ok:
                    problems.append(f"a {struct[(i, j)]} that is not straight, or holds a junction or a second way, at {(i, j)}")
            if "rd" in t and "rl" in t and not overpass((i, j)):
                pcs = t["rl"]
                rl_ = {tuple(d) for d in pcs[0] if d} if len(pcs) == 1 else set()
                rd_ = links((i, j)) - rl_ if len(pcs) == 1 else set()
                ok = len(pcs) == 1 and all(pcs[0]) and len(rl_) == 2 and len(rd_) == 2
                if ok:
                    (a2, b2), (c2, d2) = sorted(rl_), sorted(rd_)
                    ok = a2[0] == -b2[0] and a2[1] == -b2[1] and c2[0] == -d2[0] and c2[1] == -d2[1] \
                        and a2[0] * c2[1] - a2[1] * c2[0] != 0
                if not ok:
                    problems.append(f"level crossing at {(i, j)} is not a straight road across a straight rail (at 90 or 45 degrees)")
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
            other_rail = {q for o in world["routes"] if o["mode"] == "rail" and o is not r for q in o["path"]}
            for end in (path[0], path[-1]):
                if not ((neighbours({end}) | {end}) & (set(owner) | set(harbours)) or end in other_rail):
                    problems.append(f"rail line '{r['id']}' ends at {end} without reaching a party, a harbour or another line")
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
            d = (b[0] - q[0], b[1] - q[1])
            if (q[0] - a[0], q[1] - a[1]) != d:
                problems.append(f"{name} bends under a {crossed[0]} at {q}; it crosses in a straight line")
                continue
            if q in struct:
                problems.append(f"{name} crosses under a {struct[q]} at {q}")
                continue
            ls = links(q)
            if ("rd" in t or "rl" in t) and not (len(ls) == 2 and len(t.get("rl", [])) <= 1 and
                                                 (lambda u, v: u[0] == -v[0] and u[1] == -v[1] and u[0] * d[1] - u[1] * d[0] != 0)(*ls)):
                problems.append(f"{name} crosses a {crossed[0]} at {q} other than straight across under a straight piece")
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

    # no way crosses another, or the river, through the corner two squares share: a diagonal step of one way and a
    # diagonal step of another between the two other squares of the same four, or a diagonal step between two
    # squares of water
    diag_steps = set()
    for name, mode, path in laid + [(r["id"], "pipeline", r["path"]) for r in world["routes"] if r["mode"] == "pipeline"]:
        for a2, b2 in zip(path, path[1:]):
            if a2[0] != b2[0] and a2[1] != b2[1]:
                diag_steps.add((frozenset((a2, b2)), name))
                s1, s2 = tile(b2[0], a2[1]), tile(a2[0], b2[1])
                if s1 and s2 and s1["k"] in ("w", "s") and s2["k"] in ("w", "s") and mode != "pipeline":
                    problems.append(f"{mode} '{name}' passes between two squares of water at the corner of {a2} and {b2}")
    corners_ = {}
    for e, name in diag_steps:
        a2, b2 = tuple(e)
        corners_.setdefault((max(a2[0], b2[0]), max(a2[1], b2[1])), set()).add((e, name))
    for c2, es in corners_.items():
        if len({e for e, _ in es}) > 1:
            problems.append(f"{' and '.join(sorted({n for _, n in es}))} cross through the corner {c2} of four squares")
    # the river is navigable below the rapids above Ferrano (world/terrain.json "rapids", O153): the barges and the
    # quays stay below their foot
    rapids = [tuple(q) for q in terrain.get("rapids", [])]
    if rapids:
        foot = course.index(rapids[-1]) if rapids[-1] in course else -1
        for r in world["routes"]:
            if r["mode"] == "river" and any(course.index(q) <= foot for q in r["path"] if q in course):
                problems.append(f"river route '{r['id']}' uses the river at or above the rapids (from {rapids[0]} to {rapids[-1]})")
        for p in world["parties"]:
            if p.get("kind") == "quay":
                wet = [y for y in neighbours(set(footprint(p))) if y in course]
                if wet and min(course.index(y) for y in wet) <= foot:
                    problems.append(f"#{p['n']} {p['name']} is a quay at or above the rapids")

    leg_problems, legs = check_legs(world, T, adj, owner, neighbours)
    problems += leg_problems

    for tw in world.get("towns", []):
        tw.pop("streets", None)

    model = {"W": W, "H": H, "grid": GRID, "km": KM, "approach": APPROACH, "level_m": LEVEL_M, "fitted_m": round(fitted[0]),
             "tiles": [[T[i][j] for j in range(H)] for i in range(W)], "v": V, "legs": legs, "structures": structures,
             "rapids": [list(q) for q in rapids], "access": access,
             # the border on the water (the river below the crossing, the estuary's axis), in tile coordinates (a
             # square's centre at its index)
             "border_water": [[round(x - .5, 2), round(y - .5, 2)] for x, y in terrain.get("border_water", [])]}
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
          f"{sum(1 for t in flat if t.get('br'))} bridge squares and {sum(1 for t in flat if t.get('tn'))} tunnel squares "
          f"({sum(1 for x in model['structures'] if x['kind'] == 'bridge')} bridges, "
          f"{sum(1 for x in model['structures'] if x['kind'] == 'tunnel')} tunnels): "
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
