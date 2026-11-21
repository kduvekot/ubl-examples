"""Distances, times and heights from the world model, for the example generators (O152 stage 2 B).

"Everything follows the new map" (owner, 2026-11-18): a distance a document states is the length of the transport
leg on the map, as the world model (tools/world_model.py) lays it from party to party, or of a route of the map
(world/map.json); the sea and air distances between the mainland and Lisavu are those of the place list
(tools/place_list.py, section 4), measured on the real ocean. The generators read them here instead of writing
them as literals, so that they stay right when the map changes.

The model is built once per process (about 8 seconds).
"""
import datetime
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import place_list   # noqa: E402
import world_data   # noqa: E402
import world_model  # noqa: E402

KNOTS = 13.5                     # the feeder ship's service speed (D19), knots
SHIP_KMH = 1.852 * KNOTS
_CACHE = {}


def _model():
    if "model" not in _CACHE:
        world = world_data.load()
        made = os.environ.get("WORLD_MODEL")           # the model the site build's world check has just written
        if made:                                       # (tools/world_model.py model.json; tools/build_site.sh)
            model = json.load(open(made, encoding="utf-8"))["model"]
        else:
            probe = json.loads(json.dumps(world))      # build() annotates its copy
            model, problems = world_model.build(probe)
            if problems:
                raise SystemExit("world model: " + "; ".join(problems[:5]))
        _CACHE["world"], _CACHE["model"] = world, model
    return _CACHE["world"], _CACHE["model"]


def leg(flow, frm, to, mode=None):
    """The way of a transport leg of a flow (world/documents.json) on the map: its squares, party to party."""
    _, model = _model()
    for x in model["legs"]:
        if x["flow"] == flow and x["from"] == frm and x["to"] == to and (mode is None or x["mode"] == mode):
            return [tuple(q) for q in x["path"]]
    raise KeyError(f"no leg {flow} {frm} -> {to} {mode or ''}")


def leg_km(flow, frm, to, mode=None):
    """The length of a leg on the map in km (3.5 km a square, 4.95 km a diagonal)."""
    return place_list.path_km(leg(flow, frm, to, mode))


def border_km(flow, frm, to, mode=None):
    """How far along a leg it crosses a land border (or the river border), in km: to the first square in another
    country than its start."""
    _, model = _model()
    path = leg(flow, frm, to, mode)
    T = model["tiles"]
    c0 = T[path[0][0]][path[0][1]]["c"]
    for k in range(1, len(path)):
        c = T[path[k][0]][path[k][1]]["c"]
        if c and c != c0:
            return place_list.path_km(path[:k + 1])
    raise KeyError(f"the leg {flow} {frm} -> {to} crosses no border")


def route_km(rid):
    """The length of a route of the map (world/map.json "routes"), along its squares."""
    world, _ = _model()
    r = next(x for x in world["routes"] if x["id"] == rid)
    return place_list.path_km([tuple(q) for q in r["pts"]])


def sea_km():
    """The sea route Lumeport - Selanu (route "sea"), measured on the real ocean as the place list does: its squares
    near each coast along the map, the open ocean as the great circle between the stated positions."""
    world, _ = _model()
    sea = [tuple(q) for q in next(x for x in world["routes"] if x["id"] == "sea")["pts"]]
    km = 0.0
    for a, b in zip(sea, sea[1:]):
        km += place_list.grid_km(a, b) if (a[0] >= 200) == (b[0] >= 200) else place_list.great_circle(world, a, b)
    return km


def sea_hours():
    """The passage time Lumeport - Selanu at the ship's service speed, in hours."""
    return sea_km() / SHIP_KMH


def air_km(world=None):
    """The great circle between the two airports (17-xb, 17-xl), in km."""
    world = world or _model()[0]
    at = {p["id"]: p["at"] for p in world["parties"]}
    return place_list.great_circle(world, at["17-xb"], at["17-xl"])


def flight(world=None):
    """The air route's timetable (world/map.json, route "air", key "flight"): the block time each way in hours, the
    time the flight needs gate to gate in still air over the great circle between the airports (taxiing, climb and
    descent over their stretch, the rest at the cruising speed), and the distance. The block times keep a margin over
    the still-air time, or the build stops (O152, O123; stage 7 A3). The generators, the Encyclopedia's texts and the
    check of every flight's planned times all read it here."""
    world = world or world_data.load()
    f = next(x for x in world["routes"] if x["id"] == "air")["flight"]
    km = air_km(world)
    still = (f["taxi_min"] + f["climb_descent_min"]) / 60 + max(0.0, km - f["climb_descent_km"]) / f["cruise_kmh"]
    for way, hours in f["block_hours"].items():
        if still > hours:
            raise SystemExit(f"air: the flight ({still:.2f} h in still air) no longer fits its {way}bound block time "
                             f"of {hours} h (world/map.json)")  # O152, O123
    return {"east": f["block_hours"]["east"], "west": f["block_hours"]["west"], "still_air": still, "km": km}


def clock_ahead(a, b):
    """How many hours the clocks of country b are ahead of those of country a (world/countries.json timezone)."""
    world = world_data.load()
    tz = {k: world["countries"][k]["timezone"] for k in (a, b)}
    h = {k: int(v[0] + "1") * (int(v[1:3]) + int(v[4:6]) / 60) for k, v in tz.items()}
    return h[b] - h[a]


def duration(hours):
    """A block time as the timetables write it: 2 h 45."""
    m = round(hours * 60)
    return f"{m // 60} h {m % 60:02d}"


def fitted_height(pid):
    """The level the 3D map gives a party's footprint (the mean of its corners, metres): where its buildings stand."""
    world, model = _model()
    p = next(x for x in world["parties"] if x["id"] == pid)
    V = model["v"]
    cs = {(i + a, j + b) for i, j in world_model.footprint(p) for a in (0, 1) for b in (0, 1)}
    return sum(V[i][j] for i, j in cs) / len(cs)


def at(day_iso, hhmm):
    """A local date and time."""
    return datetime.datetime.fromisoformat(f"{day_iso}T{hhmm}")


def after(start, hours):
    """start plus hours, to the minute."""
    return start + datetime.timedelta(minutes=round(hours * 60))


def sail_by_day(start, km, kmh, first="06:30", last="18:30"):
    """When a barge that sails only in daylight (from first to last, local time) and starts at start has made km
    at kmh; it moors for the night where it is."""
    t, left = start, km
    while True:
        day_end = t.replace(hour=int(last[:2]), minute=int(last[3:]))
        if t < day_end:
            run = (day_end - t).total_seconds() / 3600 * kmh
            if run >= left:
                return after(t, left / kmh)
            left -= run
        nxt = (t + datetime.timedelta(days=1)).replace(hour=int(first[:2]), minute=int(first[3:]))
        t = nxt


def hm(t):
    """A time as hh:mm:00."""
    return t.strftime("%H:%M:00")


def nearest(x, step):
    """x rounded to the nearest step (an 'about' figure)."""
    return int(step * math.floor(x / step + 0.5))


def whole(x):
    """x rounded half up to a whole number."""
    return int(math.floor(round(x, 1) + 0.5))


def about(t, step=5):
    """A time rounded to step minutes, as hh:mm, for an 'about' in a text."""
    q = round((t.hour * 60 + t.minute) / step) * step
    return f"{q // 60 % 24:02d}:{q % 60:02d}"
