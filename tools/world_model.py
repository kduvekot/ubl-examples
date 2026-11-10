#!/usr/bin/env python3
"""Build the tile model of the UBL world from world/world.json, and check it.

The world is a finished snapshot: everything is built, nothing grows. This
script decides the structure; the map (site/world.html) only draws it.

For every tile the model records:
  k   terrain: s sea, w river water, g grass, f forest, r rocks, d field
  c   country (XA, XB, XC) or null
  h   height (0 flat; hills are 1 or 2)
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
  * roads, rails and buildings stand on flat ground (h = 0);
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

    # 4. routes: roads and rails on their tiles; bridges over the river
    road = set()
    rails = {}
    for r in world["routes"]:
        if r["mode"] in ("road", "rail"):
            path = path_tiles(r["pts"], r["mode"])
            r["path"] = path
            for k, (i, j) in enumerate(path):
                t = T[i][j]
                p = owner.get((i, j))
                if p and p.get("on") != r["mode"] and 0 < k < len(path) - 1:
                    problems.append(f"#{p['n']} {p['name']} stands on {r['mode']} route '{r['id']}' at {(i, j)}")
                if t["k"] == "w":
                    t["br"] = 1
                elif t["k"] == "s":
                    t["k"], t["c"] = "g", t["c"] or ("XC" if i >= 42 else ("XA" if i < border(j) else "XB"))
                if t["k"] != "w":
                    flatten(i, j)
                if r["mode"] == "road":
                    if not p or p.get("on") == "road":
                        road.add((i, j))
                else:
                    prev = (path[k - 1][0] - i, path[k - 1][1] - j) if k else None
                    nxt = (path[k + 1][0] - i, path[k + 1][1] - j) if k < len(path) - 1 else None
                    if not p or p.get("on") == "rail":
                        rails.setdefault((i, j), []).append([prev, nxt])
        elif r["mode"] == "river":
            r["path"] = path_tiles(r["pts"], "rail")

    # 5. towns: a street grid (main cross, side streets every third tile), clipped to land
    for tw in world.get("towns", []):
        ci, cj, rad = tw["c"][0], tw["c"][1], tw["r"]
        for i in range(ci - rad, ci + rad + 1):
            for j in range(cj - rad, cj + rad + 1):
                t = tile(i, j)
                if not t or t["k"] in ("s", "w") or (i, j) in owner or (i, j) in rails:
                    continue
                d = math.hypot(i - ci, j - cj)
                main = (i == ci or j == cj) and d <= rad
                side = ((i - ci) % 3 == 0 or (j - cj) % 3 == 0) and d <= rad * .75
                if main or side:
                    road.add((i, j))
                    flatten(i, j)

    # 6. access: every party next to a road (rail parties: road or rail; ports, quays: water too)
    def neighbours(cells):
        out = set()
        for (i, j) in cells:
            for di, dj in DIRS:
                q = (i + di, j + dj)
                if q not in cells:
                    out.add(q)
        return out

    def free(q):
        t = tile(*q)
        return t and t["k"] not in ("s", "w") and q not in owner and t["h"] == 0

    for p in world["parties"]:
        fp = set(footprint(p))
        around = neighbours(fp)
        if any(q in road for q in around) or any(q in road for q in fp):
            continue
        if p["kind"] in ("mine", "terminal", "depot") and any(q in rails for q in around | fp):
            continue
        # lay an access road: breadth-first search to the nearest road tile
        prev, todo, found = {}, deque(), None
        for q in around:
            if free(q) or q in road:
                prev[q] = None
                todo.append(q)
        while todo:
            q = todo.popleft()
            if q in road:
                found = q
                break
            for di, dj in DIRS:
                nq = (q[0] + di, q[1] + dj)
                if nq not in prev and (free(nq) or nq in road):
                    prev[nq] = q
                    todo.append(nq)
        if not found:
            problems.append(f"#{p['n']} {p['name']} has no access and no road can reach it")
            continue
        q = prev[found]
        while q is not None:
            road.add(q)
            flatten(*q)
            q = prev[q]

    # road connections: a mask per road tile, towards neighbouring road tiles,
    # and towards the building a road ends at
    for (i, j) in road:
        mask = 0
        for bit, (di, dj) in enumerate(DIRS):
            q = (i + di, j + dj)
            if q in road:
                mask |= 1 << bit
        if bin(mask).count("1") <= 1:
            for bit, (di, dj) in enumerate(DIRS):
                if (i + di, j + dj) in owner:
                    mask |= 1 << bit
                    break
        T[i][j]["rd"] = mask
    for (i, j), pieces in rails.items():
        T[i][j]["rl"] = pieces

    # 7. houses: in towns, on free tiles next to a street, facing it; taller in the centre
    for tw in world.get("towns", []):
        ci, cj, rad = tw["c"][0], tw["c"][1], tw["r"]
        for i in range(ci - rad - 1, ci + rad + 2):
            for j in range(cj - rad - 1, cj + rad + 2):
                t = tile(i, j)
                d = math.hypot(i - ci, j - cj)
                if not t or d > rad + .6 or not free((i, j)) or (i, j) in road or (i, j) in rails:
                    continue
                face = next((b for b, (di, dj) in enumerate(DIRS) if (i + di, j + dj) in road), None)
                if face is None or hsh(i * 13, j * 7) > .9:        # a few gardens stay open
                    continue
                level = 3 if d < rad * .35 else 2 if d < rad * .7 else 1
                t["k"], t["hs"] = "g", [level, face]

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
            if t["k"] == "g" and t["h"] == 0 and (i, j) not in road and (i, j) not in rails and \
                    "b" not in t and "hs" not in t and "yd" not in t and hsh(i * 5, j * 17) < .05:
                t["tr"] = 1

    # 9. checks on the finished model
    for i in range(W):
        for j in range(H):
            t = T[i][j]
            if ("rd" in t or "rl" in t) and t["k"] in ("s", "w") and not t.get("br"):
                problems.append(f"route on water without a bridge at {(i, j)}")
            if ("rd" in t or "rl" in t or "b" in t or "hs" in t) and t["h"] != 0:
                problems.append(f"something built on a hill at {(i, j)}")
            if "hs" in t:
                di, dj = DIRS[t["hs"][1]]
                if (i + di, j + dj) not in road:
                    problems.append(f"house at {(i, j)} does not face a street")
    for p in world["parties"]:
        fp = set(footprint(p))
        ok = any(q in road for q in neighbours(fp) | fp)
        ok = ok or (p["kind"] in ("mine", "terminal", "depot") and any(q in rails for q in neighbours(fp) | fp))
        if not ok:
            problems.append(f"#{p['n']} {p['name']} has no access")
    for p in world["parties"]:
        if p.get("kind") == "quay" and not any(tile(*q) and tile(*q)["k"] == "w" for q in neighbours(set(footprint(p)))):
            problems.append(f"#{p['n']} {p['name']} is a quay but not on the river bank")

    model = {"W": W, "H": H, "tiles": [[T[i][j] for j in range(H)] for i in range(W)]}
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
