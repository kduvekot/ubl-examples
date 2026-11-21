#!/usr/bin/env python3
"""The world's key facts, computed from the world data and the map (stage 7 B2, O250, Q11).

A published text of the world data (world/*.json: the Encyclopedia's wiki texts and facts, the flows' texts) does not
copy a figure the data already holds: it writes a placeholder {fact:<key>} and the builders fill it in with the
figure as the register below renders it ("159 km"; the text keeps its own "about"). tools/build_wiki.py and
tools/build_world.py fill the world they load (fill_world); tools/world_movement.py fills a route fact before it
compares it with the map; tools/build_examples.py fills a document's reason (world/documents.json "why") on its page.

The facts are of two kinds: the map's (lengths, passage, the ore train's wagons), and the flows' stories (the
quantities, prices, weights, temperatures and times a flow's text, a document's reason, an Encyclopedia article or a
party's "what" and "how" state), computed from the flows' deals and constants in tools/examples_scenarios.py and
from the world data they rest on (items, fleets, the Accord's rules, the air route's timetable). The generators take
a fact from here (render) instead of writing it again.

The method note (note/src/03-world.md) keeps its literals: NOTE lists where it states a registered fact, and the
check below stops the build when the note no longer says what the data computes.

Run as a script (by tools/check_world.py) it checks
  - every placeholder in the world data names a registered fact;
  - no published text of the world data writes a registered fact's figure as a literal (it would go stale: write the
    placeholder), except the uses EXEMPT lists, which are other things of the same size; a map fact anywhere, a
    story fact in the stories (STORY), each by its rendering or the pattern its entry gives;
  - every NOTE anchor still holds the fact's rendering;
  - no generator string (GENERATORS) writes a registered fact as a literal, except the strings that define it
    (GENERATOR_EXEMPT).

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


def _sc():
    """The scenarios (tools/examples_scenarios.py): the flows' deals and their constants. Imported only when a fact
    from them is asked for, so the register itself stays light."""
    import examples_scenarios
    return examples_scenarios


def _layer(name):
    return json.load(open(os.path.join(ROOT, "world", f"{name}.json"), encoding="utf-8"))


def _item(iid):
    return next(x for x in _layer("items")["items"] if x["id"] == iid)


def _fleet(pid, vid):
    p = next(x for x in _layer("parties")["parties"] if x["id"] == pid)
    return next(v for v in p.get("fleet", []) if v["id"] == vid)


def _deal(flow, item=None, key="ordered", where=None):
    """The quantity of a flow's deal (of one item, or of the lines a test picks), from the scenarios."""
    from decimal import Decimal
    deal = getattr(_sc(), flow.upper()).deal
    return sum(Decimal(str(d[key])) for d in deal
               if (item is None or d["item"] == item) and (where is None or where(d)))


def t1(x):
    """Tonnes to one decimal, from kilograms."""
    return f"{float(x) / 1000:,.1f} t"


def mm3(d):
    return " × ".join(n0(x) for x in d) + " mm"


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
    # the flows' deals and stories (examples_scenarios.py) and the world data they rest on; a fourth element is the
    # pattern a literal of the fact has in a text ({r}: the rendering), where the bare figure is too common to tell
    "ore.tonnes": ("the ore train's weighed load (the ore deal, delivered)",
                   lambda: _deal("ore", key="delivered"), lambda x: f"{x:,} t"),
    "ore.tonnes_about": ("the ore train's load, to 10 t",
                         lambda: _deal("ore", key="delivered"), lambda x: f"{n0(_near(float(x), 10))} t"),
    "ore.iron": ("the iron content of the lump ore (items.json ore-lump)",
                 lambda: next(q[1] for q in _item("ore-lump")["quantity_properties"] if q[0] == "Iron content"),
                 lambda x: f"{x} %", r"{r} (?:iron|Fe)\b"),
    "ore.moisture": ("the moisture measured at loading (examples_scenarios ORE_MOISTURE)",
                     lambda: _sc().ORE_MOISTURE[0], lambda x: f"{x} %", r"{r} moisture"),
    "ore.deduction": ("the moisture clause's deduction (the ore deal's line allowance)",
                      lambda: _sc().ORE.deal[0]["line_allowance"]["percent"], lambda x: f"{x} %",
                      r"{r} of the value"),
    "ore.bonus": ("the transport plan's bonus for a train on the first day (examples_scenarios ORE_BONUS)",
                  lambda: _sc().ORE_BONUS, lambda x: f"{x} %", r"{r} bonus"),
    "road.benches": ("the benches of the road flow's deal", lambda: _deal("road", "bench-serra"),
                     lambda x: f"{x} park benches"),
    "road.frames": ("the spare frames of the road flow's deal", lambda: _deal("road", "bench-casting"),
                    lambda x: f"{x} spare side frames"),
    "rail.benches": ("the benches of the rail flow's deal: two containers", lambda: _deal("rail", "bench-serra"),
                     lambda x: f"{x} benches"),
    "plastics.tonnes": ("the granulate of the plastics flow's deal", lambda: _deal("plastics"),
                        lambda x: f"{x} tonnes"),
    "retail.benches": ("the benches of the store's order", lambda: _deal("retail", "bench-serra-b"),
                       lambda x: f"{x} benches"),
    "retail.off": ("the reopening's discount (items.json resales store-bench-reopening)",
                   lambda: next(r for r in _layer("items")["resales"]["sales"]
                                if r["id"] == "store-bench-reopening")["less_percent"],
                   lambda x: f"{x} %", r"{r} off"),
    "sea.benches": ("the benches of the sea flow's deal", lambda: _deal("sea", "bench-serra-b"),
                    lambda x: f"{x} benches"),
    "sea.port_benches": ("the Port of Selanu's benches of the sea deal",
                         lambda: _deal("sea", "bench-serra-b", where=lambda d: d.get("port")),
                         lambda x: f"{x} benches", r"{r} for the Port"),
    "sea.bench_pallets": ("the pallets of four the sea deal's benches travel on",
                          lambda: _deal("sea", "bench-serra-b") / 4, lambda x: f"{int(x)} pallets"),
    "sea.bench_price": ("the distributor's island price of the bench (items.json bench-serra-b)",
                        lambda: _item("bench-serra-b")["price"]["amount"], lambda x: f"{n0(x)} lume",
                        r"{r} a bench"),
    "sea.frame_price": ("the distributor's island price of the frame (items.json bench-casting-b, buyer 1-xl)",
                        lambda: _item("bench-casting-b")["buyer_prices"]["1-xl"]["amount"], lambda x: n0(x),
                        r"(?<![\d,.]){r} a frame"),
    "tender.calloff": ("the first call-off's benches under the framework contract", lambda: _deal("tender"),
                       lambda x: f"{x} benches"),
    "waste.year_t": ("the film the producer notifies for the year (examples_scenarios WASTE_YEAR_T)",
                     lambda: _sc().WASTE_YEAR_T, lambda x: f"{x} t"),
    "waste.bales": ("the bales of a load (examples_scenarios WASTE_BALES)", lambda: _sc().WASTE_BALES,
                    lambda x: f"{x} bales"),
    "waste.gross": ("the waste truck weighed full (examples_scenarios WASTE_GROSS)", lambda: _sc().WASTE_GROSS, t1),
    "waste.net": ("the waste of a load: full less empty", lambda: _sc().WASTE_NET, t1),
    "trasvia.t07_tare": ("Trasvia's tractor unit 07 and its trailer, empty (parties.json 13-xu T-07)",
                         lambda: sum(_fleet("13-xu", "T-07")["tare_kg"].values()), t1),
    "trasvia.t07_payload": ("what the Accord's road limit leaves tractor unit 07 to carry",
                            lambda: _layer("countries")["road_rules_accord"]["max_combination_kg"]
                            - sum(_fleet("13-xu", "T-07")["tare_kg"].values()), t1),
    "road.limit": ("the Trade Accord's road limit for a combination (countries.json road_rules_accord)",
                   lambda: _layer("countries")["road_rules_accord"]["max_combination_kg"],
                   lambda x: f"{x // 1000} t", r"(?<![\d,.]){r}\b"),
    "wood.bundles": ("the bundles of the wood flow's deal", lambda: _deal("wood"), lambda x: f"{x} bundles"),
    "wood.slats": ("the slats in them (items.json slat-1800, per bundle)",
                   lambda: _deal("wood") * _item("slat-1800")["package"]["per_package"], lambda x: f"{n0(x)} slats"),
    "wood.bundle_slats": ("the slats of a bundle (items.json slat-1800)",
                          lambda: _item("slat-1800")["package"]["per_package"], lambda x: f"{x}",
                          r"bundle of {r}\b"),
    "wood.benches": ("the benches the slats make, at the bench's five slats (items.json bench-serra parts)",
                     lambda: _deal("wood") * _item("slat-1800")["package"]["per_package"]
                     / next(pt["n"] for pt in _item("bench-serra")["parts"] if pt["name"] == "slat"),
                     lambda x: f"{n0(x)} benches"),
    "wood.weight": ("the wood flow's load on its pallets, to 0.1 t",
                    lambda: _sc().kit.gross_weight(_sc().WOOD, "ordered"), t1),
    "wood.pallets": ("the pallets the bundles travel on (examples_scenarios WOOD_PALLETS)",
                     lambda: _sc().WOOD_PALLETS, lambda x: f"{x}", r"(?<![\d,.]){r} (?:heat-treated )?pallets"),
    "modification.bundles": ("the bundles of the sawmill's processing job (examples_scenarios MOD_BUNDLES)",
                             lambda: _sc().MOD_BUNDLES, lambda x: f"{x} bundles"),
    "wood.slat_size": ("the slat's size (items.json slat-1800)", lambda: _item("slat-1800")["dimensions_mm"], mm3),
    "wood.blank_size": ("the ash blank's size (items.json ash-blank-1830)",
                        lambda: _item("ash-blank-1830")["dimensions_mm"], mm3),
    "xu.vat": ("Urvania's standard VAT rate (countries.json)",
               lambda: _layer("countries")["countries"]["XU"]["tax"]["schemes"][0]["rates"]["standard"],
               lambda x: f"{x} %", r"{r} VAT|VAT at {r}|value added tax of {r}"),
    "fx.ferra": ("ferra to the lume at the Accord's parity (countries.json exchange_rates)",
                 lambda: round(1 / _layer("countries")["exchange_rates"]["XUF/XBL"]),
                 lambda x: f"{x} ferra", r"{r} to the lume"),
    "reefer.set_point": ("the fruit's carriage set point (items.json apples-gala storage)",
                         lambda: _item("apples-gala")["storage"]["set_point_c"], lambda x: f"{x} °C"),
    "reefer.humidity": ("the fruit's relative humidity (items.json apples-gala storage)",
                        lambda: _item("apples-gala")["storage"]["humidity_percent"], lambda x: f"{x} %",
                        r"{r} (?:relative )?humidity"),
    "reefer.carton": ("the fruit's carton, net (items.json apples-gala)", lambda: _item("apples-gala")["net_kg"],
                      lambda x: f"{x:g} kg", r"cartons of {r}"),
    "lpg.tonnes": ("the propane of a tanker load (the lpg deal, ordered)", lambda: _deal("lpg"),
                   lambda x: f"{x} t", r"{r} of propane"),
    "lpg.tare": ("the tanker empty: tractor and tank semi-trailer (parties.json 52-xb GT-04)",
                 lambda: sum(_fleet("52-xb", "GT-04")["tare_kg"].values()), lambda x: f"{round(x / 1000)} t",
                 r"(?<![\d,.]){r} with its tractor"),
    "lpg.loaded": ("the tanker loaded: its tare and the propane weighed", lambda: _sc().LPG_GROSS,
                   lambda x: f"{round(x / 1000)} t", r"weighs about {r}"),
    "lpg.km": ("the tanker's road from the gas plant to the water company, to 5 km (leg lpg 42-xb -> 34-xb)",
               lambda: _wm().leg_km("lpg", "42-xb", "34-xb"), lambda x: f"{n0(_near(x, 5))} km"),
    "lpg.tank_m3": ("the tank's capacity (parties.json 52-xb GT-04)",
                    lambda: _fleet("52-xb", "GT-04")["tank"]["capacity_m3"], lambda x: f"{x} m³"),
    "lpg.tank_kg": ("the tank's maximum load (parties.json 52-xb GT-04)",
                    lambda: _fleet("52-xb", "GT-04")["tank"]["max_load_kg"], lambda x: f"{n0(x)} kg"),
    "medicines.cold": ("the vaccines' storage range (items.json flu-vaccine)",
                       lambda: _item("flu-vaccine")["storage"], lambda x: f"{x['min']} to {x['max']} °C"),
    "medicines.set_point": ("the vaccines' carriage set point (items.json flu-vaccine)",
                            lambda: _item("flu-vaccine")["storage"]["set"], lambda x: f"{x} °C", r"set to {r}"),
    "air.kxl207": ("the morning flight's departure from Lumeport (map.json route air, flight departures)",
                   lambda: _wm().flight()["departures"]["KXL207"], lambda x: x, r"KXL207 leaves Lumeport at {r}"),
    "air.kxl209": ("the afternoon flight's departure from Lumeport (map.json route air, flight departures)",
                   lambda: _wm().flight()["departures"]["KXL209"], lambda x: x, r"KXL209 at {r}"),
    "kelaro.payload": ("the freighter's payload (parties.json 12-xl KXL capacity)",
                       lambda: _fleet("12-xl", "KXL")["capacity"]["payload_kg"], lambda x: f"{n0(x)} kg"),
    "kelaro.volume": ("the freighter's volume (parties.json 12-xl KXL capacity)",
                      lambda: _fleet("12-xl", "KXL")["capacity"]["volume_m3"], lambda x: f"{x:g} m³"),
    "tidewell.th_gt": ("the Tidewell Harbour's gross tonnage (parties.json 11-xb TH)",
                       lambda: int(_fleet("11-xb", "TH")["gross_t"]), lambda x: f"{n0(x)} gross tonnes"),
    "tidewell.tr_gt": ("the Tidewell Reef's gross tonnage (parties.json 11-xb TR)",
                       lambda: int(_fleet("11-xb", "TR")["gross_t"]), lambda x: f"{n0(x)} gross tonnes"),
    "tidewell.th_teu": ("the Tidewell Harbour's capacity (parties.json 11-xb TH)",
                        lambda: _fleet("11-xb", "TH")["capacity_teu"], lambda x: f"{n0(x)} TEU"),
    "tidewell.tr_teu": ("the Tidewell Reef's capacity (parties.json 11-xb TR)",
                        lambda: _fleet("11-xb", "TR")["capacity_teu"], lambda x: f"{n0(x)} TEU"),
    "tidewell.th_crew": ("the Tidewell Harbour's crew (parties.json 11-xb TH)",
                         lambda: _fleet("11-xb", "TH")["crew"], lambda x: f"a crew of {x}"),
    "tidewell.tr_crew": ("the Tidewell Reef's crew (parties.json 11-xb TR)",
                         lambda: _fleet("11-xb", "TR")["crew"], lambda x: f"a crew of {x}"),
    "store.marrow_bench": ("the store's price of the Marrow bench (items.json marrow-bench-oak-r)",
                           lambda: _item("marrow-bench-oak-r")["price"]["amount"], lambda x: f"{n0(x)} lume",
                           r"bench at {r}"),
    "store.marrow_chair": ("the store's price of the Marrow chair (items.json marrow-chair-oak-r)",
                           lambda: _item("marrow-chair-oak-r")["price"]["amount"], lambda x: n0(x),
                           r"chair at {r}\b"),
    "elettrica.tariff": ("the retail company's electricity tariff (items.json electricity)",
                         lambda: _item("electricity")["price"]["amount"], lambda x: f"{x:g} ferra",
                         r"{r} a kilowatt hour"),
    "cotton.bale": ("the lint in a bale (items.json cotton-bale, per package)",
                    lambda: _item("cotton-bale")["package"]["per_package"], lambda x: f"{x} kg",
                    r"bales of about {r}"),
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
    ("medicines.cold", "parties/parties/27/wiki"),     # the cargo terminal's cold room, not the vaccines' range
]

# The facts of the map (above, to air.km) are checked in every published text; the facts of the flows' stories
# only in the stories: the flows' texts, the documents' reasons, the Encyclopedia's texts and the parties' "what"
# and "how". Item and fleet data state their own figures (an item's description, a tank's approval): they are the
# source, not a copy.
MAP_FACTS = {"ore.line_km", "ore.run_km", "ore.wagons", "road.km", "gas.pipeline_km", "gas.grid_km",
             "gas.field_km", "sea.km", "sea.hours", "sea.knots", "air.km"}
STORY = re.compile(r"^documents/flows/\d+/text$|^documents/documents/\d+/why$|/wiki/|"
                   r"^parties/parties/\d+/(?:what|how)$")

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
            if k not in MAP_FACTS and not STORY.search(path):
                continue
            pat = (FACTS[k][3].replace("{r}", re.escape(r)) if len(FACTS[k]) > 3 else
                   rf"(?<![\d,.]){re.escape(r)}(?![\w³²])")
            hit = re.search(pat, bare)
            if hit and not any(k == ek and path.startswith(ep) for ek, ep in EXEMPT):
                i = hit.start()
                out.append(f"{path}: the literal \"{r}\" is the fact {k} ({FACTS[k][0]}): write {{fact:{k}}} "
                           f"(…{bare[max(0, i - 60):i + len(r)]}…)")
    note = " ".join(open(os.path.join(ROOT, "note", "src", "03-world.md"), encoding="utf-8").read().split())
    for k, anchor in NOTE:
        if anchor.format(rendered[k]) not in note:
            out.append(f"note/src/03-world.md: \"{anchor.format(rendered[k])}\" not found: the note states the fact "
                       f"{k} ({FACTS[k][0]}), which the data computes as {rendered[k]}")
    return out, used


# The generators' strings (the reasons and values they write) take a registered fact from the register
# (render(key)), not as a literal; GENERATOR_EXEMPT holds the strings that define the figure itself (a flow's deal,
# its line's own "why") or are another thing of the same size: (key, a piece of the string).
GENERATORS = ("tools/examples_scenarios.py", "tools/examples_kit.py")
GENERATOR_EXEMPT = [
    ("sea.hours", "Planned downtime announced 48 hours ahead"),          # the telecom's planned downtime
    ("plastics.tonnes", "120 tonnes of recycled granulate"),             # the plastics deal itself
    ("plastics.tonnes", "Bunkering: 120 tonnes of marine gas oil"),      # the feeder's fuel
    ("retail.benches", "24 benches more at the promotional price"),      # the promotion's expected extra sales
    ("waste.gross", "38.2 t"),                                           # the feeder's fuel meter reading
    ("wood.bundles", "96 bundles of 50 slats, 4,800 slats"),             # the wood deal itself
    ("wood.slats", "96 bundles of 50 slats, 4,800 slats"),
    ("modification.bundles", "96 bundles of 50 slats, 4,800 slats"),
    ("wood.bundles", "The 96 bundles travel four to a pallet"),          # the deal's pallet charge, beside it
    ("modification.bundles", "The 96 bundles travel four to a pallet"),
    ("wood.pallets", "The 96 bundles travel four to a pallet"),
    ("wood.pallets", "24 pallets"),                                      # every flow's pallets of four benches
    ("wood.bundle_slats", "Bench slat 1800, bundle of 50"),              # an item's name
]


def generator_problems():
    """Registered facts written as literals in the generators' strings (tokenize: comments and docstrings are not
    strings the examples show)."""
    import io
    import tokenize
    out = []
    rendered = {k: render(k) for k in FACTS}
    for rel in GENERATORS:
        src = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        prev = None
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            kind = tok.type
            if kind in (tokenize.STRING, getattr(tokenize, "FSTRING_MIDDLE", -1)) and \
                    not (prev in (tokenize.INDENT, tokenize.NEWLINE, tokenize.DEDENT) and tok.string.startswith('"""')):
                for k, r in rendered.items():
                    pat = (FACTS[k][3].replace("{r}", re.escape(r)) if len(FACTS[k]) > 3 else
                           rf"(?<![\d,.]){re.escape(r)}(?![\w³²])")
                    if re.search(pat, tok.string) and not any(k == ek and piece in tok.string
                                                              for ek, piece in GENERATOR_EXEMPT):
                        out.append(f"{rel}:{tok.start[0]}: the literal \"{r}\" is the fact {k}: write "
                                   f"world_facts.render({k!r})")
            if kind not in (tokenize.NL, tokenize.COMMENT):
                prev = kind
    return out


def main():
    out, used = problems()
    out += generator_problems()
    for p in out:
        print(p)
    print(f"world facts: {len(FACTS)} registered, {len(used)} used as placeholders, {len(NOTE)} note anchors, "
          f"{len(out)} problems")
    if out:
        sys.exit(1)


if __name__ == "__main__":
    main()
