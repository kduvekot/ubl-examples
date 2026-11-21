#!/usr/bin/env python3
"""The movements of the goods in the UBL example world against the built examples (world/examples/*/*.xml).

Checks (stage 7, B1 with Q10 and A6 with Q6):
  * times (O60): every departure and arrival pair the documents give for a stage of a transport (planned with
    planned, estimated with estimated, actual with actual, requested with requested; in one stage or, where a flow
    gives one of each, across its documents) fits its leg's length on the map at the real speed of the leg's vehicle
    (world/map.json speeds) plus the allowances the leg names (world/map.json allowances; world/documents.json leg
    "timing"), within 15 % or 30 minutes, whichever is larger; an aircraft's still-air time is the air route's
    timetable (taxiing, climb and descent, then cruise);
  * transit days: a despatch advice's estimated delivery is its despatch date plus the flow's door_to_door_days or
    its main leg's transit_days, where the data gives them, and that many days hold the leg at its speed;
  * the routes' facts (world/map.json routes wiki facts): a Length or Distance in km is the route's length on the
    map (the sea route's as measured on the real ocean), a Passage in hours is the sea route at the feeder's speed;
  * tax treatment against the goods' movement (O266, O259): each invoice or order that a leg carries (leg
    "carries") has a tax category fitting where its goods go: an export code (XU EXP, XB EXP) only where the goods
    leave the seller's country (a leg it is carried on crosses that country's border, its delivery terms name a
    place abroad, or it cites an export declaration); TRANSIT only where the goods pass through under transit;
    a domestic supply of another country (TAXED_IN) only where they are already there.

Usage: python3 tools/world_movement.py   (prints the problems, exit 1 if any)
"""
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import world_data  # noqa: E402
import world_goods  # noqa: E402

MODE_CODE = {"1": "sea", "2": "rail", "3": "road", "4": "air", "8": "river"}
VEHICLE = {"road": "truck", "rail": "container_train", "river": "barge", "sea": "feeder", "air": "freighter"}
KIND = {"Planned": "planned", "Estimated": "estimated", "Actual": "actual", "Requested": "requested"}
TOLERANCE, MIN_TOLERANCE_H = 0.15, 0.5


def local(e):
    return world_goods.local(e)


def when(ev):
    d, t = ev.findtext("{*}OccurrenceDate"), ev.findtext("{*}OccurrenceTime")
    if not d or not t:
        return None
    return datetime.datetime.fromisoformat(f"{d}T{t}")


def stages(root):
    """(stage name, mode or None, {kind: {"D": datetime, "A": datetime}}) for every shipment stage of a document."""
    out = []
    for st in root.iter():
        if not isinstance(st.tag, str) or not local(st).endswith("ShipmentStage"):
            continue
        ev = {}
        for k, kind in KIND.items():
            for w in ("Departure", "Arrival"):
                e = st.find(f"{{*}}{k}{w}TransportEvent")
                t = when(e) if e is not None else None
                if t:
                    ev.setdefault(kind, {})[w[0]] = t
        if ev:
            out.append((local(st), MODE_CODE.get(st.findtext("{*}TransportModeCode") or ""), ev))
    return out


def main_leg(legs):
    return next((x for x in legs if x["mode"] != "road"), legs[0] if legs else None)


def stage_leg(flow, name, mode):
    legs = flow.get("legs", [])
    main = main_leg(legs)
    if not main:
        return None
    if name.startswith("PreCarriage"):
        c = [x for x in legs if x["to"] == main["from"] and x is not main]
    elif name.startswith("OnCarriage"):
        c = [x for x in legs if x["from"] == main["to"] and x is not main]
    else:
        c = [main] if mode in (None, main["mode"]) else [x for x in legs if x["mode"] == mode]
    if mode:
        c = [x for x in c if x["mode"] == mode]
    return c[0] if c else None


def leg_km(flow_id, leg):
    import world_map as wmap
    if leg["mode"] == "sea":
        return wmap.sea_km()
    if leg["mode"] == "air":
        return wmap.air_km()
    return wmap.leg_km(flow_id, leg["from"], leg["to"], leg["mode"])


def expected_hours(world, flow_id, leg, kind, dep):
    """The hours a leg takes at its vehicle's speed plus the allowances it names for this kind of time."""
    import world_map as wmap
    timing = leg.get("timing", {})
    vehicle = timing.get("vehicle", VEHICLE[leg["mode"]])
    kmh = wmap.speed(leg["mode"], vehicle)
    km = leg_km(flow_id, leg)
    al = timing.get("allowances", [])
    if isinstance(al, dict):
        al = al.get(kind, [])
    if leg["mode"] == "air":
        f = next(x for x in world["routes"] if x["id"] == "air")["flight"]
        hours = (f["taxi_min"] + f["climb_descent_min"]) / 60 + max(0.0, km - f["climb_descent_km"]) / kmh
    elif "night_mooring" in al:
        sails, moors = wmap.allowance("night_mooring")
        naive = dep.replace(tzinfo=None)
        hours = (wmap.sail_by_day(naive, km, kmh, sails, moors) - naive).total_seconds() / 3600
    else:
        hours = km / kmh
    hours += sum(wmap.allowance(a) for a in al if a != "night_mooring")
    return hours, km, kmh, al


def time_problems(world, docs):
    import world_map as wmap
    out = []
    flows = {f["id"]: f for f in world["flows"]}
    for f in world["flows"]:
        for leg in f.get("legs", []):
            t = leg.get("timing", {})
            al = t.get("allowances", [])
            names = sum(al.values(), []) if isinstance(al, dict) else al
            for a in names:
                if a not in wmap.ALLOWANCES or a == "note":
                    out.append(f"{f['id']}: leg {leg['from']} -> {leg['to']} names the allowance {a}, which "
                               "world/map.json allowances does not have")
            if t.get("vehicle") and t["vehicle"] not in wmap.SPEEDS.get(leg["mode"], {}):
                out.append(f"{f['id']}: leg {leg['from']} -> {leg['to']}: no speed for {leg['mode']} {t['vehicle']}")
    groups = {}           # (flow, stage, mode, kind) -> {"D": {...}, "A": {...}} over the flow's documents
    pairs = []
    for key, d, root in docs:
        for name, mode, ev in stages(root):
            for kind, da in ev.items():
                g = groups.setdefault((d["flow"], name, mode, kind), {"D": {}, "A": {}})
                for w, t in da.items():
                    g[w].setdefault(t, key)
                if "D" in da and "A" in da:
                    pairs.append((key, d["flow"], name, mode, kind, da["D"], da["A"]))
    seen = {(p[1], p[2], p[3], p[4], p[5], p[6]) for p in pairs}
    for (flow, name, mode, kind), g in groups.items():
        if len(g["D"]) == 1 and len(g["A"]) == 1:
            (dt, k1), (at, k2) = next(iter(g["D"].items())), next(iter(g["A"].items()))
            if (flow, name, mode, kind, dt, at) not in seen:
                pairs.append((f"{k1} with {k2}", flow, name, mode, kind, dt, at))
    for key, flow, name, mode, kind, dep, arr in pairs:
        leg = stage_leg(flows[flow], name, mode)
        if not leg:
            out.append(f"{key}: {name} ({kind}) has no leg in world/documents.json")
            continue
        hours, km, kmh, al = expected_hours(world, flow, leg, kind, dep)
        got = (arr - dep).total_seconds() / 3600
        if abs(got - hours) > max(TOLERANCE * hours, MIN_TOLERANCE_H):
            out.append(f"{key}: {name} {kind} {dep.isoformat()} -> {arr.isoformat()} takes {got:.2f} h; the leg "
                       f"{leg['from']} -> {leg['to']} ({km:.1f} km at {kmh} km/h"
                       f"{' with ' + ', '.join(al) if al else ''}) takes {hours:.2f} h (O60)")
    COUNT["pairs"] = len(pairs)
    # transit days: the despatch advices' estimates
    for key, d, root in docs:
        if d["doc"] != "DespatchAdvice":
            continue
        fl = flows[d["flow"]]
        main = main_leg(fl.get("legs", []))
        days = fl.get("door_to_door_days", main.get("transit_days") if main else None)
        sent = root.findtext(".//{*}Despatch/{*}ActualDespatchDate")
        start = root.findtext(".//{*}EstimatedDeliveryPeriod/{*}StartDate")
        if days is None or not sent or not start:
            continue
        gap = (datetime.date.fromisoformat(start) - datetime.date.fromisoformat(sent)).days
        if gap != days:
            out.append(f"{key}: despatched {sent}, expected {start}: {gap} days, not the {days} of world/documents.json "
                       f"({'door_to_door_days' if 'door_to_door_days' in fl else 'transit_days'})")
        COUNT["transit"] += 1
    for f in world["flows"]:
        for leg in f.get("legs", []):
            if "transit_days" not in leg or leg["mode"] == "pipeline":
                continue
            hours, km, kmh, al = expected_hours(world, f["id"], leg, "planned",
                                                datetime.datetime(2026, 1, 1, 8, 0))
            if hours > (leg["transit_days"] + 1) * 24:
                out.append(f"{f['id']}: leg {leg['from']} -> {leg['to']}: transit_days {leg['transit_days']}, but "
                           f"{km:.1f} km at {kmh} km/h take {hours:.1f} h")
    return out


def number(s):
    m = re.search(r"([\d,]+(?:\.\d+)?)", s)
    return float(m.group(1).replace(",", "")) if m else None


def route_problems(world):
    import world_map as wmap
    out = []
    for r in world["routes"]:
        facts = (r.get("wiki") or {}).get("facts") or {}
        for k, v in facts.items():
            if "{" in v or k not in ("Length", "Distance", "Passage"):
                continue                   # a fact the Encyclopedia fills in from the map itself
            n = number(v)
            if k == "Passage":
                x, unit = (wmap.sea_hours(), "hours") if r["id"] == "sea" else (None, None)
            elif r["id"] == "sea":
                x, unit = wmap.sea_km(), "km"
            elif r["id"] == "air":
                x, unit = wmap.air_km(), "km"
            else:
                x, unit = wmap.route_km(r["id"]), "km"
            if x is None or n is None or unit not in v:
                out.append(f"route {r['id']}: the fact {k} \"{v}\" cannot be compared with the map")
            elif abs(n - x) > max(1.0, 0.01 * x):
                out.append(f"route {r['id']}: {k} \"{v}\", but the map gives {x:.1f} {unit} (O60)")
            COUNT["facts"] += 1
    return out


COUNT = {"pairs": 0, "transit": 0, "facts": 0, "taxed": 0}

# ---------------------------------------------------------------- tax treatment against the movement (A6, Q6)
SALES = {"Order": "to", "OrderChange": "to", "OrderResponse": "from", "Invoice": "from", "CreditNote": "from",
         "DebitNote": "from", "SelfBilledInvoice": "to", "SelfBilledCreditNote": "to"}
SCHEME_COUNTRY = {"VAT": "XU", "STT": "XB"}        # the general taxes of world/countries.json


def country(world, pid):
    p = next((x for x in world["parties"] + world.get("abroad", []) if x["id"] == pid), None)
    return (p or {}).get("c") or pid.rsplit("-", 1)[-1].upper()


def gln_country(world, gln):
    """A location number of the world (952, the party's number, the location): its party's country."""
    if not re.fullmatch(r"952\d{10}", gln or ""):
        return None
    n = int(gln[3:5])
    p = next((x for x in world["parties"] if x.get("n") == n), None)
    return p and p.get("c")


def place_country(world, ident):
    if not ident:
        return None
    if re.fullmatch(r"[A-Z]{2}[A-Z0-9]{3}", ident):
        return ident[:2]
    return gln_country(world, ident)


def categories(root):
    out = set()
    for tc in root.iter("{*}TaxCategory", "{*}ClassifiedTaxCategory"):
        if (tc.findtext("{*}TaxScheme/{*}ID") or "") not in SCHEME_COUNTRY:
            continue                                   # not a general tax on the supply (a withholding tax, excise)
        code = tc.find("{*}TaxExemptionReasonCode")
        lst = code.get("listID", "") if code is not None else ""
        m = re.search(r":(X[UBL]):codelist:", lst)
        out.add((tc.findtext("{*}ID"), code.text if code is not None else None, m.group(1) if m else None,
                 SCHEME_COUNTRY.get(tc.findtext("{*}TaxScheme/{*}ID") or "")))
    return out


def tax_problems(world, docs):
    out = []
    by_key = {k: (d, r) for k, d, r in docs}
    by_id = {(d["flow"], r.findtext("{*}ID")): k for k, d, r in docs}
    exports = {(d["flow"], r.findtext("{*}ID")) for k, d, r in docs if d["doc"] == "ExportCustomsDeclaration"}
    carried = {}                                       # key -> [(from country, to country, leg)]
    for f in world["flows"]:
        for leg in f.get("legs", []):
            if "carries" not in leg:
                out.append(f"{f['id']}: leg {leg['from']} -> {leg['to']} does not say whose goods it carries")
                continue
            for k in leg["carries"]:
                if k not in by_key or by_key[k][0]["doc"] not in SALES or by_key[k][0]["flow"] != f["id"]:
                    out.append(f"{f['id']}: leg {leg['from']} -> {leg['to']} carries {k}, which is no order, "
                               "invoice or note of its flow")
                    continue
                carried.setdefault(k, []).append((country(world, leg["from"]), country(world, leg["to"]), leg))

    def legs_of(key, seen=()):
        """The legs that carry a document's goods: its own, or those of the order or invoice it refers to."""
        if key in carried:
            return carried[key]
        d, root = by_key[key]
        for e in root.iter("{*}OrderReference", "{*}InvoiceDocumentReference", "{*}CreditNoteDocumentReference",
                           "{*}OriginatorDocumentReference"):
            k = by_id.get((d["flow"], e.findtext("{*}ID")))
            if k and k != key and k not in seen and k in by_key and by_key[k][0]["doc"] in SALES:
                got = legs_of(k, seen + (key,))
                if got:
                    return got
        return []

    for key, d, root in docs:
        if d["doc"] not in SALES:
            continue
        seller = d.get(SALES[d["doc"]])
        if not seller:
            continue
        home = country(world, seller)
        if home not in ("XU", "XB", "XL"):
            continue                                   # a seller outside the Accord: its own country's rules
        moves = legs_of(key)
        leaves = any(a == home and b != home for a, b, _ in moves)
        enters = any(a != home and b == home for a, b, _ in moves)
        dt = root.find(".//{*}DeliveryTerms")
        place = place_country(world, dt.findtext(".//{*}DeliveryLocation/{*}ID")) if dt is not None else None
        declared = any((d["flow"], e.findtext("{*}ID")) in exports for e in root.iter("{*}DocumentReference",
                                                                                     "{*}AdditionalDocumentReference"))
        for cat, code, code_country, scheme_country in sorted(categories(root), key=str):
            if cat == "O":
                continue                               # outside the scope of the tax: services, levies
            COUNT["taxed"] += 1
            if code == "EXP":
                if not (leaves or (place and place != home) or declared):
                    out.append(f"{key}: {code_country} EXP, but no leg carries its goods out of {home}, its "
                               "delivery terms name no place abroad and it cites no export declaration (A6)")
            elif code == "TRANSIT":
                if not (enters and any(b != home for a, b, _ in moves)):
                    out.append(f"{key}: {code_country} TRANSIT, but its legs do not bring the goods through {home} "
                               "from abroad and on abroad (A6)")
            else:
                taxed_in = code_country or scheme_country or home
                if taxed_in != home:
                    if any(a != taxed_in or b != taxed_in for a, b, _ in moves):
                        out.append(f"{key}: a supply taxed in {taxed_in}, but a leg moves its goods across "
                                   f"{taxed_in}'s border (A6)")
                    elif not moves:
                        out.append(f"{key}: a supply taxed in {taxed_in} by a seller of {home}, and no leg shows "
                                   f"the goods in {taxed_in} (A6)")
                elif leaves and cat in ("S", "E", "Z") and code != "SVCABROAD":
                    out.append(f"{key}: {cat} {code or ''} of {home}, but a leg carries its goods out of {home}: "
                               "an export (A6)")
    return out


def check(world):
    docs = world_goods.built(world)
    out = time_problems(world, docs)
    out += route_problems(world)
    out += tax_problems(world, docs)
    return out


def main():
    world = world_data.load()
    problems = check(world)
    for p in problems:
        print(p)
    if not problems:
        print(f"movements: {COUNT['pairs']} departure and arrival pairs, {COUNT['transit']} transit estimates, "
              f"{COUNT['facts']} route facts against the map at the world's speeds, {COUNT['taxed']} tax categories "
              "against the goods' movement: no problems")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
