#!/usr/bin/env python3
"""Lay a road, a railway or a pipeline over the terrain as a builder would (O152 stage 3). Standard library only:
tools/lay_routes.py lays the map's routes with it, and tools/world_model.py its access roads, if any are missing.

The ways run over the squares of the world model (3.5 km), 8-connected: from a square to any of its eight
neighbours (a diagonal step passes through the corner the two squares share). The cost of a way is its length in
squares, raised by:
  * the rise and fall: every metre a way climbs and descends between two squares, over the terrain's fine heights
    (875 m cells): a way follows the valleys and crosses a ridge at its lowest, at a pass;
  * the gradient: each class has the gradient it is built for (a main road about 6 to 7 %, a minor road up to
    10 %, a railway 1.5 to 2 %, measured between the squares' mean heights); a step over the class's hard limit
    is not taken, a step towards it costs more the steeper it is (a longer line round a hill is cheaper than a
    straight one up it, a valley cheaper than a ridge);
  * the cross-fall: a square whose corners differ much is a side slope, to be cut and filled;
  * the ground: marsh, bare rock and forest cost more than open land;
  * the turns: a turn of 45 degrees costs a little, a turn of 90 degrees more; sharper turns are not made (the
    ways read as curves, not as zigzags);
  * a way may join a road of its own kind that is already built (it costs less: a network grows from what is
    there), and cross one of another kind only straight on, at right angles (a level crossing, or a pipeline
    under a road), at right angles or at 45 degrees (a skew crossing), never along it and never through the corner of
    a diagonal step of another way;
  * bridges and tunnels are engineering choices, priced by their length: a bridge (straight, from bank to bank,
    or over a valley as a viaduct whose deck keeps the gradient) where the ground falls away or water is in the
    way; a tunnel (straight, under a spur or a ridge with enough rock above it) where the way would otherwise
    be over its gradient or much longer. A bridge over the estuary costs much more than one over the river,
    a tunnel much more than a bridge; they are tried only where the plain step is steep or wet.
Land borders are crossed only where the caller allows it (a road at its customs posts); the sea only by a
pipeline from its offshore platform.

route() returns the squares of the way and the squares it bridges or tunnels; the caller lays them.
"""
import heapq
import math

DIRS8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
KM = 3.5
SQ2 = math.sqrt(2)

# The classes of way. grade: the gradient it is built for; hard: the gradient it never exceeds between two
# squares; half, lean (roads): the gradient a road never exceeds on its own line within a square, and how much the
# land may lean across it (owner, 2026-11-19: Land.half_ok); slack: metres of cut or fill allowed for that; climb:
# the weight of the gradient cost; turn45/turn90: the cost of a turn; bridge/tunnel: the cost of a square of bridge
# or tunnel (on top of its length), max_bridge/max_tunnel: the longest, in squares; join: the
# cost factor on a square of an existing way of the same kind; rf: squares of extra cost per 100 m of rise and
# fall between two squares (the climbs and descents of the land between them); max_high: the highest a bridge's
# deck may stand above the land or the water under it (metres).
CLASSES = {
    "main": dict(mode="road", grade=.06, hard=.07, half=.07, lean=.06, climb=.8, relief=.6, turn45=.10, turn90=.45, bridge=4.0, valley=6.0,
                 estuary=20.0, tunnel=18.0, max_bridge=3, max_tunnel=2, join=.8, cover=1.0, rf=1.0, max_high=140),
    "minor": dict(mode="road", grade=.08, hard=.10, half=.10, lean=.08, climb=.6, relief=.4, turn45=.06, turn90=.3, bridge=4.0, valley=8.0,
                  estuary=40.0, tunnel=None, max_bridge=1, max_tunnel=0, join=.5, cover=1.0, rf=.7, max_high=80),
    "rail": dict(mode="rail", grade=.015, hard=.02, climb=1.6, relief=.6, turn45=.18, turn90=1.2, bridge=5.0, valley=6.0,
                 estuary=20.0, tunnel=14.0, max_bridge=3, max_tunnel=3, join=.6, cover=1.0, rf=2.0, max_high=120),
    "pipeline": dict(mode="pipeline", grade=.08, hard=None, climb=1.2, relief=.8, turn45=.08, turn90=.35, bridge=None,
                     valley=None, estuary=None, tunnel=None, max_bridge=0, max_tunnel=0, join=None, cover=1.4, rf=.3, max_high=0),
}
# a minor road where no reasonable way keeps to the rule on the land as it is (owner, 2026-11-19, O173 option c):
# the builder may cut or fill up to ROAD_SLACK_M on each half of a square; the world model makes the cut
ROAD_SLACK_M = 100
CLASSES["minor-cut"] = dict(CLASSES["minor"], slack=ROAD_SLACK_M)
COVER = {"m": 1.6, "r": 1.2, "f": .3, "h": .1}            # extra cost per square of marsh, rock, forest, heath
TUNNEL_COVER = 40                                          # metres of ground at least above a tunnel's line
BRIDGE_FREE = 10                                           # metres the ground may rise above a bridge deck's line


class Land:
    """The terrain as the router sees it: per square the kind, the country and the mean and spread of its corner
    heights (metres), the estuary's squares."""

    def __init__(self, kind, country, corners, W, H, estuary=(), water=None):
        self.W, self.H = W, H
        self.kind, self.country = kind, country                  # [i][j]
        self.hc = [[(corners[i][j] + corners[i + 1][j] + corners[i][j + 1] + corners[i + 1][j + 1]) / 4 for j in range(H)]
                   for i in range(W)]
        self.rng = [[max(corners[i][j], corners[i + 1][j], corners[i][j + 1], corners[i + 1][j + 1])
                     - min(corners[i][j], corners[i + 1][j], corners[i][j + 1], corners[i + 1][j + 1]) for j in range(H)]
                    for i in range(W)]
        self.corners = corners                                   # [i][j]: the height of each square corner
        self.estuary = set(estuary)
        self.water = dict(water or {})                           # the river's squares: their water level
        self.fine = []                                           # the terrain's fine height rasters, if loaded
        self._rf = {}

    def half_ok(self, q, d, grade, lean, slack=0.0):
        """Whether a road can run on its own line from the middle of square q to the edge or corner in direction d
        on the land as it is (owner, 2026-11-19; the world model's road_fits): within grade along it, and the land
        across it, a quarter square to each side of its middle, within lean; slack: metres a builder may cut or fill
        to get there (a class's "slack")."""
        i, j = q
        C = self.corners
        c = [C[i][j], C[i + 1][j], C[i][j + 1], C[i + 1][j + 1]]
        h = lambda u, v: c[0] * (1 - u) * (1 - v) + c[1] * u * (1 - v) + c[2] * (1 - u) * v + c[3] * u * v
        di, dj = d
        ell = math.hypot(di, dj)
        half = KM * 500
        if abs(h(.5 + di / 2, .5 + dj / 2) - h(.5, .5)) > grade * ell * half + slack:
            return False
        mu, mv, pu, pv = .5 + di / 4, .5 + dj / 4, -dj / ell * .25, di / ell * .25
        return abs(h(mu + pu, mv + pv) - h(mu - pu, mv - pv)) <= lean * half + slack

    def load_fine(self, root, rasters):
        """Read the terrain's fine height rasters (world/terrain/*-height.png, 875 m and 437.5 m cells; needs Pillow,
        which the site build has): with them the cost of a step counts every rise and fall of the land between the
        two squares, not only the difference of their mean heights, so that a way follows the valleys and crosses
        the ridges where they are low."""
        import os
        from PIL import Image
        for r in rasters.values():
            im = Image.open(os.path.join(root, r["height"]))
            w, h = im.size
            data = list(im.getdata())
            self.fine.append((r["x0"], r["y0"], r["cells_per_square"], w, h, data, r["offset_m"]))

    def height_at(self, x, y):
        for x0, y0, S, w, h, data, off in self.fine:
            c, r = int((x - x0) * S), int((y - y0) * S)
            if 0 <= c < w and 0 <= r < h:
                return data[r * w + c] - off
        i, j = min(self.W - 1, max(0, int(x))), min(self.H - 1, max(0, int(y)))
        return self.hc[i][j]

    def rise_fall(self, a, b):
        """The metres a way climbs and descends between the centres of squares a and b, over the fine heights
        (every 875 m or finer); without the fine rasters, the difference of the squares' mean heights."""
        key = (a, b) if a <= b else (b, a)
        v = self._rf.get(key)
        if v is None:
            if not self.fine:
                v = abs(self.hc[b[0]][b[1]] - self.hc[a[0]][a[1]])
            else:
                n = 8
                pts = [self.height_at(a[0] + .5 + (b[0] - a[0]) * k / n, a[1] + .5 + (b[1] - a[1]) * k / n) for k in range(n + 1)]
                pts[0], pts[-1] = self.hc[a[0]][a[1]], self.hc[b[0]][b[1]]
                v = sum(abs(y - x) for x, y in zip(pts, pts[1:]))
            self._rf[key] = v
        return v

    def inside(self, q):
        return 0 <= q[0] < self.W and 0 <= q[1] < self.H


class Built:
    """What is already built: the squares and steps of the roads, rails and pipelines, the river, the squares a way
    may not use (buildings, stations, a town's centre for a pipeline), and the bridge and tunnel squares (nothing
    joins or crosses there). axis(q, kind): the direction a way of that kind runs straight through q, or None
    (a bend, a junction, an end)."""

    def __init__(self):
        self.sq = {"road": set(), "rail": set(), "pipeline": set(), "river": set()}
        self.steps = {"road": {}, "rail": {}, "pipeline": {}, "river": {}}    # q -> set of directions
        self.blocked = set()
        self.structures = set()

    def add(self, kind, path, structures=()):
        for k, q in enumerate(path):
            self.sq[kind].add(q)
            s = self.steps[kind].setdefault(q, set())
            if k:
                s.add((path[k - 1][0] - q[0], path[k - 1][1] - q[1]))
            if k + 1 < len(path):
                s.add((path[k + 1][0] - q[0], path[k + 1][1] - q[1]))
        self.structures |= set(structures)
        for k, q in enumerate(path):                      # a structure's approaches: nothing joins them either
            if q in structures:
                for y in (path[k - 1] if k else None, path[k + 1] if k + 1 < len(path) else None):
                    if y is not None and y not in structures:
                        self.structures.add(y)

    def axis(self, q, kind):
        s = self.steps[kind].get(q)
        if not s or len(s) != 2:
            return None
        a, b = tuple(s)
        return a if (a[0] == -b[0] and a[1] == -b[1]) else None

    def diagonal(self, a, b):
        """Whether some way steps diagonally from square a to square b (they share a corner)."""
        d = (b[0] - a[0], b[1] - a[1])
        return any(d in self.steps[k].get(a, ()) for k in self.steps)


def across(d, e):
    """Two straight ways cross, at right angles or at 45 degrees (a skew crossing), not along each other."""
    return d[0] * e[1] - d[1] * e[0] != 0


def route(land, built, cls, starts, goals, *, allow_cross=frozenset(), orth_ends=frozenset(), sea_ok=False,
          avoid=frozenset(), box=None, max_expand=3_000_000, start_dir=None):
    """The cheapest way of class cls from a start square to a goal square. orth_ends: squares (buildings) that may
    only be entered or left straight from the side, not through a corner. allow_cross: pairs of squares between
    which a land border may be crossed. sea_ok: a pipeline from an offshore platform may run on the sea until its
    landfall. avoid: squares not to use. box: (i0, j0, i1, j1) to search in. Returns (path, {square: "bridge" |
    "tunnel"}) or None. start_dir: the direction a way that goes on from its start arrived in."""
    c = CLASSES[cls]
    mode = c["mode"]
    kind, country, hc, rng = land.kind, land.country, land.hc, land.rng
    goals = set(goals)
    hard = c["hard"]
    road_sq, rail_sq, pipe_sq, river_sq = built.sq["road"], built.sq["rail"], built.sq["pipeline"], built.sq["river"]
    own = built.sq[mode] if mode != "pipeline" else set()
    cross_kinds = {"road": ("rail", "pipeline"), "rail": ("road", "pipeline"), "pipeline": ("road", "rail", "river")}[mode]
    gl = list(goals)
    gx = sum(q[0] for q in gl) / len(gl)
    gy = sum(q[1] for q in gl) / len(gl)
    single = len(gl) <= 4
    hmin = min(1.0, c["join"] or 1.0)

    def heur(q):
        if not single:
            return 0.0
        return hmin * min(math.hypot(q[0] - g[0], q[1] - g[1]) for g in gl)

    def inbox(q):
        return land.inside(q) and (box is None or (box[0] <= q[0] <= box[2] and box[1] <= q[1] <= box[3]))

    def wet(q):
        k = kind[q[0]][q[1]]
        return k == "w" or k == "s"

    def ground_ok(q):
        """A square a way may stand on (not water, not a building, not avoided)."""
        if q in avoid or (q in built.blocked and q not in goals):
            return False
        k = kind[q[0]][q[1]]
        if k == "s":
            return sea_ok
        return k != "w"

    def border_ok(a, b):
        ca, cb = country[a[0]][a[1]], country[b[0]][b[1]]
        if not ca or not cb or ca == cb:
            return True
        return (a, b) in allow_cross or (b, a) in allow_cross or mode != "road"

    def corner_ok(a, d):
        """A diagonal step from a in d: not through the corner of another way's diagonal step, not between two
        squares of water."""
        if d[0] == 0 or d[1] == 0:
            return True
        s1, s2 = (a[0] + d[0], a[1]), (a[0], a[1] + d[1])
        if built.diagonal(s1, s2):
            return False
        if land.inside(s1) and land.inside(s2) and wet(s1) and wet(s2) and not sea_ok:
            return False
        return True

    def step_cost(a, b, ell):
        """Cost of a plain step from a to b (length ell squares), or None if it cannot be taken."""
        g = abs(hc[b[0]][b[1]] - hc[a[0]][a[1]]) / (ell * KM * 1000)
        if hard is not None and g > hard:
            return None
        sl = c.get("slack", 0.0)
        if c.get("lean") and not (land.half_ok(a, (b[0] - a[0], b[1] - a[1]), c["half"], c["lean"], sl)
                                  and land.half_ok(b, (a[0] - b[0], a[1] - b[1]), c["half"], c["lean"], sl)):
            return None                                     # the road would leave its rules on its own line in a or b
        e = ell * (1 + c["climb"] * (g / c["grade"]) ** 2 + c["relief"] * max(0.0, rng[b[0]][b[1]] - 60) / 300
                   + c["cover"] * COVER.get(kind[b[0]][b[1]], 0)) + c["rf"] * land.rise_fall(a, b) / 100
        if kind[b[0]][b[1]] == "s":
            e = ell * 1.0                                   # a subsea pipeline: open seabed
        if c["join"] and b in own and b not in built.structures:
            e *= c["join"]
        ca, cb = country[a[0]][a[1]], country[b[0]][b[1]]
        if mode != "road" and ca and cb and ca != cb:
            e += 40.0                                       # a land border is crossed once, where it must be
        if mode == "pipeline" and kind[b[0]][b[1]] != "s":
            if any((b[0] + di, b[1] + dj) in road_sq for di, dj in DIRS8[:4]):
                e *= .85                                    # beside a road: along its corridor
        return e

    def crossing(q, d):
        """Whether a way of this class may pass straight through square q (holding another way) in direction d: the
        other way runs straight through it too, across this one."""
        if q in built.structures:
            return False
        if sum(1 for k in ("road", "rail", "pipeline", "river") if q in built.sq[k]) > 1:
            return False                                    # one way at a time: no crossing at a level crossing
        for k in cross_kinds:
            if q in built.sq[k]:
                if k == "river":
                    continue
                ax = built.axis(q, k)
                if ax is None or not across(ax, d):
                    return False
        return True

    def occupied_other(q):
        return any(q in built.sq[k] for k in cross_kinds if k != "river") or (mode == "pipeline" and q in river_sq) \
            or (mode == "pipeline" and q in pipe_sq) or (mode != "pipeline" and kind[q[0]][q[1]] == "w")

    def over_ok(m, d):
        """A bridge may pass over a road or a rail line that runs straight under it, across its line."""
        for x in ("road", "rail"):
            if m in built.sq[x]:
                ax = built.axis(m, x)
                if ax is None or ax[0] * d[1] - ax[1] * d[0] == 0:
                    return False
        return True

    def turn(pd, d):
        if pd is None:
            return 0.0
        dot = pd[0] * d[0] + pd[1] * d[1]
        n = (pd[0] * pd[0] + pd[1] * pd[1]) ** .5 * (d[0] * d[0] + d[1] * d[1]) ** .5
        cosv = dot / n
        if cosv > .99:
            return 0.0
        if cosv > .6:
            return c["turn45"]
        if cosv > -.1:
            return c["turn90"]
        return None

    start_set = set(starts)
    dist, prev, todo = {}, {}, []
    sd = DIRS8.index(tuple(start_dir)) if start_dir else None   # a way that goes on from where it arrived
    for s in starts:
        st = (s, sd)
        dist[st] = 0.0
        prev[st] = None
        heapq.heappush(todo, (heur(s), 0.0, s, sd))
    expand = 0
    end = None
    while todo:
        f, cost, q, pdi = heapq.heappop(todo)
        st = (q, pdi)
        if cost > dist.get(st, 1e18):
            continue
        if q in goals and q not in start_set:
            end = st
            break
        expand += 1
        if expand > max_expand:
            break
        pd = DIRS8[pdi] if pdi is not None else None
        for di, d in enumerate(DIRS8):
            diag = d[0] != 0 and d[1] != 0
            if diag and ((q in orth_ends and pd is None) or q in avoid):
                continue
            t = turn(pd, d)
            if t is None:
                continue
            if diag and not corner_ok(q, d):
                continue
            ell = SQ2 if diag else 1.0
            moves = []
            b = (q[0] + d[0], q[1] + d[1])
            plain_bad = True
            if inbox(b) and border_ok(q, b) and not (diag and b in orth_ends):
                if b in goals and b in built.blocked:
                    e = ell
                    if hard is not None and abs(hc[b[0]][b[1]] - hc[q[0]][q[1]]) / (ell * KM * 1000) > hard * 1.5:
                        e = None
                    if e is not None:
                        moves.append((b, e, None))
                        plain_bad = False
                elif b in built.structures:
                    pass                                    # nothing joins a bridge or a tunnel
                elif ground_ok(b) and not occupied_other(b):
                    e = step_cost(q, b, ell)
                    if e is not None:
                        moves.append((b, e, None))
                        g = abs(hc[b[0]][b[1]] - hc[q[0]][q[1]]) / (ell * KM * 1000)
                        plain_bad = hard is not None and g > .6 * hard
                elif ground_ok(b) or (land.inside(b) and kind[b[0]][b[1]] == "w"):
                    # b holds another way or the river: pass straight through it (a level crossing, a pipeline
                    # under a road or under the river), landing on the square beyond
                    if (land.inside(b) and kind[b[0]][b[1]] != "w" or mode == "pipeline") and crossing(b, d) \
                            and not (mode != "pipeline" and kind[b[0]][b[1]] == "w"):
                        b2 = (b[0] + d[0], b[1] + d[1])
                        if inbox(b2) and ground_ok(b2) and not occupied_other(b2) and border_ok(b, b2) and border_ok(q, b2) \
                                and corner_ok(b, d) and not (diag and b2 in orth_ends):
                            e1 = 1.5 * ell if mode != "pipeline" else ell
                            e2 = step_cost(b, b2, ell)
                            if e2 is not None and (mode == "pipeline" or step_cost(q, b, ell) is not None):
                                cq, c2 = country[q[0]][q[1]], country[b2[0]][b2[1]]
                                moves.append((b2, e1 + e2 + 1.0 + (40.0 if cq and c2 and cq != c2 and not country[b[0]][b[1]] else 0.0), [b]))
            # bridges and tunnels: straight, k - 1 squares long, tried where the plain step is steep or wet. The
            # squares before and after one are its approaches (an embankment or a cutting up to the deck): never the
            # start or the end of the way, a building, or a square another way joins
            if plain_bad and mode != "pipeline" and pd is not None and q not in built.blocked and q not in own \
                    and q not in goals and q not in built.structures:
                h0 = hc[q[0]][q[1]]
                for k in range(2, max(c["max_bridge"], c["max_tunnel"]) + 2):
                    b2 = (q[0] + d[0] * k, q[1] + d[1] * k)
                    if not inbox(b2) or not ground_ok(b2) or occupied_other(b2) or b2 in goals or b2 in own \
                            or b2 in built.blocked or b2 in built.structures:
                        continue
                    mids = [(q[0] + d[0] * m, q[1] + d[1] * m) for m in range(1, k)]
                    if any(not land.inside(m) or m in built.blocked or m in avoid or m in built.structures
                           or kind[m[0]][m[1]] == "s" for m in mids):
                        break
                    if any(not border_ok(x, y) for x, y in zip([q] + mids, mids + [b2])) or not border_ok(q, b2):
                        break
                    xb = 40.0 if country[q[0]][q[1]] and country[b2[0]][b2[1]] and country[q[0]][q[1]] != country[b2[0]][b2[1]] else 0.0
                    if diag and not all(corner_ok(x, d) for x in [q] + mids):
                        continue
                    h1 = hc[b2[0]][b2[1]]
                    span = k * ell * KM * 1000
                    if hard is not None and abs(h1 - h0) / span > hard:
                        continue
                    # the land under the line, over the fine heights (the river at its water level)
                    n = 8 * k
                    prof = []
                    for u in range(n // (2 * k), n - n // (2 * k) + 1):     # over the squares it spans
                        x, y = q[0] + .5 + d[0] * k * u / n, q[1] + .5 + d[1] * k * u / n
                        sqm = (int(x), int(y))
                        g = land.water[sqm] if sqm in land.water else land.height_at(x, y)
                        prof.append((g, h0 + (h1 - h0) * u / n))
                    others = [m for m in mids if m in road_sq or m in rail_sq or m in pipe_sq]
                    nwet = sum(1 for m in mids if kind[m[0]][m[1]] == "w" and m not in land.estuary)
                    water = nwet > 0 or any(m in land.estuary for m in mids)
                    if nwet > (2 if diag else 1):
                        break                                   # a bridge crosses the river, it does not run along it
                    # a bridge: the land nowhere much above the deck, and water, a valley or a way under it
                    if k - 1 <= c["max_bridge"] and c["bridge"] is not None \
                            and all(g <= dk + BRIDGE_FREE for g, dk in prof) and all(over_ok(m, d) for m in others):
                        depth = max(dk - g for g, dk in prof)
                        if (water or depth >= 25 or others) and depth <= c["max_high"]:
                            high = max(0.0, depth - 15) / 20                     # a high bridge costs more
                            e = 0.0
                            for m in mids:
                                if m in land.estuary:
                                    e += c["estuary"]
                                elif kind[m[0]][m[1]] == "w":
                                    e += c["bridge"]
                                else:
                                    e += c["valley"]
                            e = ell * k + e + (k - 1) * high + t + xb
                            moves.append((b2, e, ("bridge", mids)))
                    # a tunnel: enough rock above the line all through, no water, no other way on top
                    if k - 1 <= c["max_tunnel"] and c["tunnel"] is not None and not water and not others \
                            and min(g - dk for g, dk in prof[2:-2]) >= TUNNEL_COVER \
                            and all(hc[m[0]][m[1]] >= h0 + (h1 - h0) * (x + 1) / k + TUNNEL_COVER for x, m in enumerate(mids)):
                        e = ell * k + c["tunnel"] * (k - 1) + xb
                        moves.append((b2, e + t, ("tunnel", mids)))
            for b2, e, via in moves:
                if b2 in start_set:
                    continue                                # never back through where the way began
                if via is None or isinstance(via, list):
                    e += t
                nc = cost + e
                ns = (b2, di)
                if nc < dist.get(ns, 1e18):
                    dist[ns] = nc
                    prev[ns] = (st, via)
                    heapq.heappush(todo, (nc + heur(b2), nc, b2, di))
    if end is None:
        return None
    path, structures = [], {}
    st = end
    while st is not None:
        q = st[0]
        p = prev[st]
        path.append(q)
        if p is None:
            break
        pst, via = p
        if isinstance(via, tuple):
            for m in reversed(via[1]):
                path.append(m)
                structures[m] = via[0]
        elif isinstance(via, list):
            for m in reversed(via):
                path.append(m)
        st = pst
    path.reverse()
    return path, structures


def length_km(path):
    return sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(path, path[1:])) * KM
