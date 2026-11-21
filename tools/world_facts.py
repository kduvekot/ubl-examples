#!/usr/bin/env python3
"""The world's key facts, computed from the world data and the map (stage 7 B2, O250, Q11).

A published text of the world data (world/*.json: the Encyclopedia's wiki texts and facts, the flows' texts) does not
copy a figure the data already holds: it writes a placeholder {fact:<key>} and the builders fill it in with the
figure as the register below renders it ("159 km"; the text keeps its own "about"). tools/build_wiki.py and
tools/build_world.py fill the world they load (fill_world); tools/world_movement.py fills a route fact before it
compares it with the map.

The method note (note/src/03-world.md) keeps its literals: NOTE lists where it states a registered fact, and the
check below stops the build when the note no longer says what the data computes.

Run as a script (by tools/check_world.py) it checks
  - every placeholder in the world data names a registered fact;
  - no published text of the world data writes a registered fact's figure as a literal (it would go stale: write the
    placeholder), except the uses EXEMPT lists, which are other things of the same size;
  - every NOTE anchor still holds the fact's rendering.

A fact says which length it means: a route's length (the line laid on the map, end to end, world_map.route_km) is not
a leg's (a flow's transport from party to party along it, world_map.leg_km): the ore line is about 166 km, the ore
train's run from the mine siding to the works siding about 159 km.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.join(os.path.dirname(__file__), "..")
LAYERS = ("countries", "parties", "map", "documents", "items")


def n0(x):
    return f"{int(x):,}"


def _near(x, step):
    import math
    return int(step * math.floor(x / step + 0.5))


def _ore_wagons():
    world = json.load(open(os.path.join(ROOT, "world", "parties.json"), encoding="utf-8"))
    for p in world["parties"]:
        for v in p.get("fleet", []):
            if v.get("ore_wagons"):
                return len(v["ore_wagons"])
    raise KeyError("no ore train with ore wagons in world/parties.json")


def _wm():
    import world_map
    return world_map


# key: (what it is, how it is computed, how it is rendered)
FACTS = {
    "ore.line_km": ("the ore line's length, mine portal to the works (route ore)",
                    lambda: _wm().route_km("ore"), lambda x: f"{n0(round(x))} km"),
    "ore.run_km": ("the ore train's run, mine siding to works siding (leg ore 4-xu -> 5-xu)",
                   lambda: _wm().leg_km("ore", "4-xu", "5-xu"), lambda x: f"{n0(round(x))} km"),
    "ore.wagons": ("the ore wagons of the ore train (Ferrano Rail Cargo's fleet)",
                   _ore_wagons, lambda x: f"{x} wagons"),
    "road.km": ("the road Ferrano - Marrowdale (route road)",
                lambda: _wm().route_km("road"), lambda x: f"{n0(round(x))} km"),
    "gas.pipeline_km": ("the gas pipeline, gas plant to the power station (route gas)",
                        lambda: _wm().route_km("gas"), lambda x: f"{n0(round(x))} km"),
    "gas.grid_km": ("the pipeline's branch to the grid's city gate (route gas-grid)",
                    lambda: _wm().route_km("gas-grid"), lambda x: f"{n0(round(x))} km"),
    "gas.field_km": ("the subsea line from the platform to the gas plant (route gas-field)",
                     lambda: _wm().route_km("gas-field"), lambda x: f"{n0(round(x))} km"),
    "sea.km": ("the sea route Lumeport - Selanu on the real ocean (world_map.sea_km), to 50 km",
               lambda: _wm().sea_km(), lambda x: f"{n0(_near(x, 50))} km"),
    "sea.hours": ("the passage at the feeder's service speed (world_map.sea_hours), whole hours",
                  lambda: _wm().sea_hours(), lambda x: f"{round(x)} hours"),
    "sea.knots": ("the feeder's service speed (world/map.json speeds sea feeder)",
                  lambda: _wm().SPEEDS["sea"]["feeder"]["knots"], lambda x: f"{x:g} knots"),
    "air.km": ("the great circle between the airports (world_map.air_km), to 10 km",
               lambda: _wm().air_km(), lambda x: f"{n0(round(x, -1))} km"),
}

# Where the method note states a registered fact: the sentence around it, with {} for the rendering (whitespace as
# in a single line).
NOTE = [
    ("road.km", "By road Ferrano to Marrowdale is about {} and"),
    ("ore.line_km", "the ore line runs about {};"),
    ("gas.pipeline_km", "the gas pipeline runs about {} from the gas plant to the power station"),
    ("gas.grid_km", "its branch to the grid's city gate about {},"),
    ("gas.field_km", "the subsea line from the platform about {}."),
    ("sea.km", "round the island's south-eastern cape, it is about {}, which the ship sails in"),
    ("sea.hours", "which the ship sails in about {} at"),
    ("sea.knots", "about 48 hours at {}."),
    ("air.km", "The island airline's freighter flies about {} between the airports"),
]

# Literals in published texts that are the size of a registered fact but another thing: (key, JSON path prefix).
EXEMPT = [
    ("air.km", "countries/countries/XL/wiki/lead"),    # Lumeport to the island in a straight line, not the airports
]

_VALUES = {}


def value(key):
    if key not in FACTS:
        raise KeyError(f"{{fact:{key}}} is not a registered fact (tools/world_facts.py)")
    if key not in _VALUES:
        _VALUES[key] = FACTS[key][1]()
    return _VALUES[key]


def render(key):
    return FACTS[key][2](value(key))


PLACEHOLDER = re.compile(r"\{fact:([a-z0-9_.]+)\}")


def fill(text):
    """A text with its {fact:…} placeholders filled in."""
    if not isinstance(text, str) or "{fact:" not in text:
        return text
    return PLACEHOLDER.sub(lambda m: render(m.group(1)), text)


def fill_world(obj):
    """Fill every placeholder of a loaded world (or any part of it) in place; returns it."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            obj[k] = fill(v) if isinstance(v, str) else fill_world(v)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            obj[i] = fill(v) if isinstance(v, str) else fill_world(v)
    return obj


def texts():
    """Every published string of the world data with its path (keys starting with _ are the workshop's)."""
    def walk(o, p):
        if isinstance(o, dict):
            for k, v in o.items():
                if not str(k).startswith("_"):
                    yield from walk(v, p + [str(k)])
        elif isinstance(o, list):
            for i, v in enumerate(o):
                yield from walk(v, p + [str(i)])
        elif isinstance(o, str):
            yield "/".join(p), o
    for layer in LAYERS:
        data = json.load(open(os.path.join(ROOT, "world", f"{layer}.json"), encoding="utf-8"))
        data.pop("description", None)
        yield from walk(data, [layer])


def problems():
    out, used = [], set()
    rendered = {k: render(k) for k in FACTS}
    for path, t in texts():
        for m in PLACEHOLDER.finditer(t):
            used.add(m.group(1))
            if m.group(1) not in FACTS:
                out.append(f"{path}: {{fact:{m.group(1)}}} is not a registered fact")
        bare = PLACEHOLDER.sub("", t)
        for k, r in rendered.items():
            if re.search(rf"(?<![\d,.]){re.escape(r)}\b", bare) and not any(
                    k == ek and path.startswith(ep) for ek, ep in EXEMPT):
                i = bare.find(r)
                out.append(f"{path}: the literal \"{r}\" is the fact {k} ({FACTS[k][0]}): write {{fact:{k}}} "
                           f"(…{bare[max(0, i - 60):i + len(r)]}…)")
    note = " ".join(open(os.path.join(ROOT, "note", "src", "03-world.md"), encoding="utf-8").read().split())
    for k, anchor in NOTE:
        if anchor.format(rendered[k]) not in note:
            out.append(f"note/src/03-world.md: \"{anchor.format(rendered[k])}\" not found: the note states the fact "
                       f"{k} ({FACTS[k][0]}), which the data computes as {rendered[k]}")
    return out, used


def main():
    out, used = problems()
    for p in out:
        print(p)
    print(f"world facts: {len(FACTS)} registered, {len(used)} used as placeholders, {len(NOTE)} note anchors, "
          f"{len(out)} problems")
    if out:
        sys.exit(1)


if __name__ == "__main__":
    main()
