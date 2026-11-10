#!/usr/bin/env python3
"""Build the tile model of the UBL world from world/world.json, and check it.

The world is a finished snapshot: everything is built, nothing grows. This
script decides the structure; the map (site/world.html) only draws it.

For every tile the model records:
  k   terrain: s sea, w river water, g grass, f forest, r rocks, d field
  c   country (XA, XB, XC) or null
  h   height of the tile's lowest corner (corner heights are in model "v")
  n   a stable noise value 0..1, for variation in the drawing
  rd  road connections, a 4-bit mask: 1 = +i, 2 = +j, 4 = -i, 8 = -j
  rl  rail pieces, each a pair of edge directions ([di, dj] or null for the centre)
  br  1 if a road or rail crosses water here (a bridge)
  b   id of the party standing here
  hs  a house: [level 1..3, facing direction 0..3 towards its street]
  tr  1 for a single tree on open ground
  yd  1 for the fenced yard around an industry

Structural rules (the build stops when one is broken):
  * buildings do not share tiles and do not stand on roads, rails or water,
    except parties marked "on" a route (customs posts, rail stations);
  * every party has access: a road next to it, or rail for rail parties,
    or water for ports and quays; missing access roads are laid by the model;
  * every house stands next to a street, facing it;
  * every landmass has one connected road network; every party lies on it
    (an access road is laid where needed, ending at the building);
  * a dead end must lead somewhere: to a party or a house (a road that ends
    at nothing gets a farmstead, or is removed);
  * roads, rails and buildings stand on flat ground; the terrain has a
    height per tile corner (model "v"), at most one level between
    neighbouring corners, 0 at the water;
  * roads and rails cross the river only on bridges.

Usage: python3 tools/world_model.py [out.json]   (default: print a summary)
"""
import json
import math
import os
import sys
from collections import deque

ROOT = os.path.join(os.path.dirname(__file__), "..")
W, H = 64, 48
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]        # bit 0..3 of the road mask


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
    """Roads: an L per pair of waypoints (longer leg first). Rail: a staircase."""
    out = [tuple(pts[0])]
    for bi, bj in pts[1:]:
        i, j = out[-1]
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
    T = [[None] * H for _ in range(W)]
    border = lambda j: 21.5 + 1.6 * math.sin(j / 4.2)

    # 1. land, countries, terrain, hills
    for i in range(W):
        for j in range(H):
            n = noise(i, j)
            main = ((i - 21.5) / 19.5) ** 2 + ((j - 24.5) / 20) ** 2 < 1 - (n - .5) * .55
            isle = ((i - 52.5) / 8.2) ** 2 + ((j - 21.5) / 11.5) ** 2 < 1 - (n - .5) * .5
            t = {"k": "s", "c": None, "h": 0, "n": round(n, 3)}
            if main or isle:
                t["c"] = "XC" if isle else ("XA" if i < border(j) else "XB")
                t["k"] = "g"
                if t["c"] == "XA" and j < 15 and i < 17 and n > .42:
                    t["k"], t["h"] = "r", 1 + (n > .58)
                elif n > .62:
                    t["k"] = "f"
                elif t["c"] == "XB" and n < .33 and 24 < i < 32:
                    t["k"] = "d"
            T[i][j] = t
    tile = lambda i, j: T[i][j] if 0 <= i < W and 0 <= j < H else None
    # farmland: fields around the given centres
    for f in world.get("fields", []):
        for i in range(W):
            for j in range(H):
                if T[i][j]["k"] in ("g", "f") and math.hypot(i - f["c"][0], j - f["c"][1]) <= f["r"] + noise(i * 3, j * 3) - .3:
                    T[i][j]["k"] = "d"

    def flatten(i, j):
        t = tile(i, j)
        if t and t["k"] != "s":
            if t["k"] in ("r", "f", "d"):
                t["k"] = "g"
            t["h"] = 0

    # 2. the river: water tiles along its course, 1-2 tiles wide
    for r in world["routes"]:
        if r["mode"] != "river":
            continue
        pts = r["pts"]
        width = r.get("width", 1.4)
        for i in range(W):
            for j in range(H):
                for (ax, ay), (bx, by) in zip(pts, pts[1:]):
                    dx, dy = bx - ax, by - ay
                    u = max(0, min(1, ((i - ax) * dx + (j - ay) * dy) / (dx * dx + dy * dy)))
                    if math.hypot(i - ax - u * dx, j - ay - u * dy) <= width / 2:
                        t = T[i][j]
                        if t["k"] != "s":
                            t["k"], t["h"] = "w", 0
                        break
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
                for k in (1, 2):
                    t = tile(i + di * k, j + dj * k)
                    if t and "b" not in t:
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
                t["k"], t["c"] = "g", t["c"] or ("XC" if q[0] >= 42 else ("XA" if q[0] < border(q[1]) else "XB"))
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
        elif r["mode"] == "river":
            r["path"] = path_tiles(r["pts"], "rail")

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
        return bool(t) and q not in owner and (t["k"] not in ("s", "w") or (water_ok and t["k"] == "w"))

    # 5. towns: streets as lines (a main cross, side streets every third tile); only the part
    #    connected to the town centre stays
    for tw in world.get("towns", []):
        ci, cj, rad = tw["c"][0], tw["c"][1], tw["r"]
        lines = [("i", cj, rad), ("j", ci, rad)]
        for k in range(3, rad + 1, 3):
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

    def connect(starts, goal, avoid=frozenset()):
        """Shortest free path from any start tile to a goal tile; lays it as road."""
        prev, todo = {}, deque()
        for q in starts:
            prev[q] = None
            todo.append(q)
        while todo:
            q = todo.popleft()
            if q in goal and prev[q] is not None or (q in goal and q not in starts):
                path = []
                while q is not None:
                    path.append(q)
                    q = prev[q]
                path.reverse()
                lay_road(path)
                return path
            for di, dj in DIRS:
                y = (q[0] + di, q[1] + dj)
                if y not in prev and y not in avoid and (y in goal or free(y, water_ok=True)):
                    prev[y] = q
                    todo.append(y)
        return None

    def main_network(m):
        comps2, _ = components()
        on_mass = [c for c in comps2 if mass.get(next(iter(c))) == m]
        return max(on_mass, key=len) if on_mass else set()

    # every landmass has one road network: link every other piece to the largest one
    for m in set(mass.values()):
        for _ in range(50):
            comps2, _ = components()
            on_mass = sorted((c for c in comps2 if mass.get(next(iter(c))) == m), key=len, reverse=True)
            if len(on_mass) <= 1:
                break
            piece = on_mass[-1]
            if not connect(piece, on_mass[0]):
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
        starts = [q for q in around if free(q)]
        path = connect(starts, net)
        if not path:
            problems.append(f"#{p['n']} {p['name']} cannot be reached by road")
            continue
        enter(path[0], next(b2 for b2 in fp if abs(b2[0] - path[0][0]) + abs(b2[1] - path[0][1]) == 1))

    # 6. houses: in towns, on free tiles next to a street, facing it; taller in the centre
    def degree(q):
        return sum(1 for e in edges if q in e)

    for tw in world.get("towns", []):
        ci, cj, rad = tw["c"][0], tw["c"][1], tw["r"]
        for i in range(ci - rad - 1, ci + rad + 2):
            for j in range(cj - rad - 1, cj + rad + 2):
                t = tile(i, j)
                d = math.hypot(i - ci, j - cj)
                if not t or d > rad + .6 or not free((i, j)) or (i, j) in road or (i, j) in rails or "hs" in t:
                    continue
                face = next((b2 for b2, (di, dj) in enumerate(DIRS) if (i + di, j + dj) in road), None)
                if face is None or hsh(i * 13, j * 7) > .9:        # a few gardens stay open
                    continue
                level = 3 if d < rad * .35 else 2 if d < rad * .7 else 1
                t["k"], t["hs"] = "g", [level, face]

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
                             and (q[0] + di, q[1] + dj) not in rails), None)
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
                if t and free(q) and q not in road and q not in rails and "hs" not in t and hsh(q[0] * 3, q[1] * 11) < .55:
                    t["k"], t["yd"] = "g", 1
    for i in range(W):
        for j in range(H):
            t = T[i][j]
            if t["k"] == "g" and (i, j) not in road and (i, j) not in rails and \
                    "b" not in t and "hs" not in t and "yd" not in t and hsh(i * 5, j * 17) < .05:
                t["tr"] = 1

    # 9. height: a height per tile corner (vertex), at most one level between neighbouring
    #    corners, 0 at the water; everything built stands on flat ground
    V = [[0] * (H + 1) for _ in range(W + 1)]
    touches = lambda vi, vj: [tile(vi - a2, vj - b2) for a2 in (0, 1) for b2 in (0, 1) if tile(vi - a2, vj - b2)]
    for vi in range(W + 1):
        for vj in range(H + 1):
            ts = touches(vi, vj)
            if any(t["k"] in ("s", "w") for t in ts) or len(ts) < 4:
                V[vi][vj] = 0
            else:
                hill = noise(vi * .8 + 40, vj * .8 + 40)
                V[vi][vj] = max(0, min(5, round((hill - .3) * 10)))
                if any(t["k"] == "r" for t in ts):
                    V[vi][vj] = min(6, V[vi][vj] + 2)
    built = lambda t, q: q in road or q in rails or "b" in t or "hs" in t or "yd" in t

    def settle():
        moved = True
        while moved:
            moved = False
            for vi in range(W + 1):
                for vj in range(H + 1):
                    lo = min([V[vi + a2][vj + b2] for a2, b2 in DIRS if 0 <= vi + a2 <= W and 0 <= vj + b2 <= H] + [99]) + 1
                    if V[vi][vj] > lo:
                        V[vi][vj], moved = lo, True
            for i in range(W):
                for j in range(H):
                    t = T[i][j]
                    if built(t, (i, j)) or t["k"] in ("s", "w"):
                        corners = [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]
                        lo = min(V[a2][b2] for a2, b2 in corners)
                        for a2, b2 in corners:
                            if V[a2][b2] != lo:
                                V[a2][b2], moved = lo, True
    settle()
    for i in range(W):
        for j in range(H):
            T[i][j]["h"] = min(V[i][j], V[i + 1][j], V[i][j + 1], V[i + 1][j + 1])
            if T[i][j]["k"] == "r" and T[i][j]["h"] == 0 and max(V[i][j], V[i + 1][j], V[i][j + 1], V[i + 1][j + 1]) == 0:
                T[i][j]["k"] = "g"

    # 10. checks on the finished model
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
            if built(t, (i, j)) and len({V[i][j], V[i + 1][j], V[i][j + 1], V[i + 1][j + 1]}) > 1:
                problems.append(f"something built on a slope at {(i, j)}")
            if "hs" in t:
                di, dj = DIRS[t["hs"][1]]
                if (i + di, j + dj) not in road:
                    problems.append(f"house at {(i, j)} does not face a street")
    for p in world["parties"]:
        fp = set(footprint(p))
        net = main_network(mass[next(iter(fp))])
        if not (neighbours(fp) | fp) & net:
            problems.append(f"#{p['n']} {p['name']} is not on the road network")
    for p in world["parties"]:
        if p.get("kind") == "quay" and not any(tile(*q) and tile(*q)["k"] == "w" for q in neighbours(set(footprint(p)))):
            problems.append(f"#{p['n']} {p['name']} is a quay but not on the river bank")
    for tw in world.get("towns", []):
        tw.pop("streets", None)

    model = {"W": W, "H": H, "tiles": [[T[i][j] for j in range(H)] for i in range(W)], "v": V}
    return model, problems


def main():
    world = json.load(open(os.path.join(ROOT, "world", "world.json"), encoding="utf-8"))
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
    if len(sys.argv) > 1:
        json.dump({"model": model, "routes": world["routes"]}, open(sys.argv[1], "w"), separators=(",", ":"))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
