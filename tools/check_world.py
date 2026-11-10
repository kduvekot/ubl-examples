#!/usr/bin/env python3
"""Check the layout of the UBL world (world/world.json).

  * no two buildings share a tile;
  * no building stands on a road, rail line or river; a route may only
    start or end on the footprint of a building (that is where it goes);
  * no building stands on the river at all;
  * a party marked "on": "road" or "on": "rail" (a customs post over the
    road, a station on the line) may stand on a route of that kind;
  * a quay (kind "quay") lies next to the river.

Routes are laid on the tile grid with the same rules as the map
(site/world.html, pathTiles): roads go in an L per pair of waypoints,
first along the longer direction; rail and river take one step at a time
along the direction with the larger remaining distance (a staircase, which
the map draws as a straight diagonal line).

Usage: python3 tools/check_world.py      (exit status 1 if there are problems)
"""
import json
import os
import sys

root = os.path.join(os.path.dirname(__file__), "..")
world = json.load(open(os.path.join(root, "world", "world.json"), encoding="utf-8"))


def sign(v):
    return (v > 0) - (v < 0)


def path_tiles(pts, mode):
    out = [tuple(pts[0])]
    for bi, bj in pts[1:]:
        i, j = out[-1]
        if mode == "road":            # an L: the longer leg first, then the shorter
            first_i = abs(bi - i) >= abs(bj - j)
            for axis in ("i", "j") if first_i else ("j", "i"):
                while (i != bi) if axis == "i" else (j != bj):
                    if axis == "i":
                        i += sign(bi - i)
                    else:
                        j += sign(bj - j)
                    out.append((i, j))
        else:                         # staircase
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


problems = []
owner, parties_at = {}, {}
for p in world["parties"]:
    for t in footprint(p):
        if t in owner:
            problems.append(f"#{p['n']} {p['name']} and {owner[t]} share tile {t}")
        owner[t] = f"#{p['n']} {p['name']}"
        parties_at[t] = p

for r in world["routes"]:
    if r["mode"] in ("sea", "air"):
        continue
    tiles = path_tiles(r["pts"], r["mode"])
    for k, t in enumerate(tiles):
        if t not in owner:
            continue
        end = k in (0, len(tiles) - 1)
        if parties_at[t].get("on") == r["mode"]:
            continue                  # built on this route on purpose (customs post, rail station)
        if r["mode"] == "river":
            problems.append(f"{owner[t]} stands on the river ({r['id']}) at {t}")
        elif not end:
            problems.append(f"{owner[t]} stands on {r['mode']} route '{r['id']}' at {t}")

# a quay lies on the river bank: next to a river tile
river = set()
for r in world["routes"]:
    if r["mode"] == "river":
        river |= set(path_tiles(r["pts"], "river"))
for p in world["parties"]:
    if p.get("kind") == "quay" and not any(
            (p["at"][0] + a, p["at"][1] + b) in river for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))):
        problems.append(f"#{p['n']} {p['name']} is a quay but not next to the river")

for line in problems:
    print("problem:", line)
print(f"{len(world['parties'])} parties, {len(world['routes'])} routes: "
      + ("no problems" if not problems else f"{len(problems)} problems"))
sys.exit(1 if problems else 0)
