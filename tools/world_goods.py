#!/usr/bin/env python3
"""The goods of the UBL example world against the built examples (world/examples/*/*.xml): lots and serials, the
goods chains with their yields, the items' physics and the loads of the vehicles.

Checks:
  * lots and serials (O64): every lot, serial or trace number in the built documents, in a structured element
    (LotNumberID, SerialID, ProductTraceID) or in any text, is in its maker's production record (world/items.json
    production_records; Valdara's in goods_chain), on the same item, with the same manufacture and expiry dates; it
    is never written in another form (the same digits under the maker's prefix); no line ships more than its lots
    made, a line with serials has one serial for each unit, and no lot leaves its maker in more than it made over
    all flows; no document quotes a lot before the day it was made;
  * goods chains (O66): for each chain of world/items.json chains, what comes out in the documents over its period
    is no more than what went in times the highest conversion rate (a balance: equal), the documents counted are
    dated within the period, and a rate stated in steps is their product;
  * item physics (O62): every item with a weight has a physics sheet; dimensions, density and solid fraction give
    the weight, within the material's density range (world/items.json materials, each with its source); a unit by
    mass, volume or energy weighs what its unit and material say; contents and the items of a pack sum to the
    whole; an item in oak and the same model in ash differ in weight as their woods do; every package a person
    lifts is within the handling limit for the people who lift it (ISO 11228-1: 25 kg for one, 33 kg for two),
    above that only with the handling aid it states;
  * loads (O62): each vehicle the documents name carries no more than the fleet data allows (world/parties.json):
    a road vehicle with its tares within its maximum gross weight (40 t for an articulated or drawbar vehicle,
    the world's rule), a tank within its maximum load, the pallets on a curtain-sider within its floor, one
    container on a container chassis (one a run where the leg gives its runs), a train's containers one to a
    wagon within the wagon's payload, the ore within the ore wagons' payload, a barge's cargo within its
    deadweight, a ship's containers within its TEU; a road leg whose vehicle no document names is checked with the
    vehicle the leg names (world/documents.json "vehicle") or its carrier's one vehicle, against the largest load
    of the flow's despatch documents (O278).

Usage: python3 tools/world_goods.py [--notes]   (prints the problems, exit 1 if any; --notes also lists what
       could not be checked for lack of data)
"""
import collections
import glob
import json
import os
import re
import sys
from decimal import Decimal

from lxml import etree

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402

HANDLING_LIMIT_KG = {1: 25, 2: 33}    # the world's rule for manual handling (D20), as in tools/world_items.py
NOTES = []
ROAD_MAX_KG = 40000                   # an articulated or drawbar road vehicle, loaded
DECK_WIDTH_M = Decimal("2.45")        # the inner width of a curtain-side trailer
UNIT_KG = {"TNE": Decimal(1000), "KGM": Decimal(1)}
UNIT_TO = {("MWH", "MWH"): 1, ("KWH", "MWH"): Decimal("0.001"), ("TNE", "KGM"): 1000, ("KGM", "KGM"): 1,
           ("EA", "EA"): 1}


def local(e):
    return etree.QName(e).localname


def D(x):
    return Decimal(str(x))


# ---------------------------------------------------------------- the built documents
def built(world):
    """(key, document, root) of every built example, key "flow/NN"."""
    out = []
    for d in world["documents"]:
        p = os.path.join(world_data.ROOT, "world", "examples", d["flow"], f"{d['nn']:02d}-{d['doc']}.xml")
        if os.path.exists(p):
            out.append((f"{d['flow']}/{d['nn']:02d}", d, etree.parse(p).getroot()))
    return out


def issue_date(root):
    e = root.find("{*}IssueDate")
    return e.text if e is not None else None


def item_ids(items):
    """A seller's, a standard or a buyer's item identifier -> the makers' items it names (a resold item is its
    maker's item)."""
    def maker(i):
        seen = set()
        while items[i].get("resale_of") in items and i not in seen:
            seen.add(i)
            i = items[i]["resale_of"]
        return i
    out = collections.defaultdict(set)
    for iid, it in items.items():
        for k in ("sellers_id", "standard_id", "gtin"):
            if it.get(k):
                out[it[k]].add(maker(iid))
        for v in (it.get("buyer_ids") or {}).values() if isinstance(it.get("buyer_ids"), dict) else []:
            out[v if isinstance(v, str) else v.get("id", "")].add(maker(iid))
    return out


def line_of(e):
    while e is not None and not (local(e).endswith("Line") or local(e) == "GoodsItem"):
        e = e.getparent()
    return e


def line_qty(line):
    if line is None:
        return None, None
    for c in line:
        if local(c).endswith("Quantity") and c.text:
            return D(c.text), c.get("unitCode")
    return None, None


def item_of(e):
    while e is not None and local(e) != "Item":
        e = e.getparent()
    return e


def named_items(item_el, ids):
    if item_el is None:
        return set()
    out = set()
    for path in ("{*}SellersItemIdentification/{*}ID", "{*}StandardItemIdentification/{*}ID",
                 "{*}BuyersItemIdentification/{*}ID", "{*}ManufacturersItemIdentification/{*}ID"):
        for x in item_el.findall(path):
            out |= ids.get(x.text, set())
    return out


# ---------------------------------------------------------------- lots and serials (O64)
def records(world, items):
    """number -> its record: maker, item (and the items it may be quoted on), made, qty, expiry, charge."""
    out, charges = {}, {}
    pr = world.get("production_records", {}).get("makers", {})
    for maker, m in pr.items():
        for r in m.get("records", []):
            num = r.get("lot") or r.get("serial")
            on = {r["item"]} | ({items[r["item"]]["content"]["item"]} if items[r["item"]].get("content") else set())
            out[num] = {**r, "maker": maker, "on": on, "kind": "lot" if r.get("lot") else "serial"}
            if r.get("charge"):
                charges[r["charge"]] = num
    chain = world.get("goods_chain", {})
    for p in chain.get("production", []):
        it = p["item"]
        if p.get("lot"):
            out[p["lot"]] = {"maker": "5-xu", "item": it, "on": {it}, "made": p["made"], "qty": p["qty"],
                             "kind": "lot", "lot": p["lot"]}
        rng = [(p["serials"], "bench-casting", {"bench-casting"})] if p.get("serials") else []
        if p.get("frame_serials"):
            rng.append((p["frame_serials"], "bench-casting", {"bench-casting", it}))
        for (a, b), sit, on in rng:
            for n in range(a, b + 1):
                for pre in ("VI-SF-", "VI-TR-"):
                    out[f"{pre}{n:05d}"] = {"maker": "5-xu", "item": sit, "on": on, "made": p["made"], "qty": 1,
                                            "kind": "serial" if pre == "VI-SF-" else "trace"}
    return out, charges


def lot_problems(world, items, docs):
    out = []
    rec, charges = records(world, items)
    pr = world.get("production_records", {}).get("makers", {})
    if not pr:
        return ["production records: none (world/items.json production_records)"]
    ids = item_ids(items)
    # the records themselves
    for num, r in rec.items():
        if r["item"] not in items:
            out.append(f"production record {num}: unknown item {r['item']}")
        if items.get(r["item"], {}).get("seller") not in (r["maker"], None) and r["kind"] != "trace":
            out.append(f"production record {num}: {r['item']} is not an item of its maker {r['maker']}")
        for f in r.get("from", []):
            src = rec.get(f["lot"])
            if not src:
                out.append(f"production record {num}: made from {f['lot']}, which has no record")
            elif src["made"] > r["made"]:
                out.append(f"production record {num}: made on {r['made']} from {f['lot']}, made later on "
                           f"{src['made']}")
            elif D(f["qty"]) > D(src["qty"]):
                out.append(f"production record {num}: takes {f['qty']} of {f['lot']}, which made {src['qty']}")
    patterns = [(maker, re.compile(rf"\b(?:{p})\b")) for maker, m in pr.items() for p in m.get("patterns", [])]
    prefixes = sorted({p.split("-")[0] for m in pr.values() for p in m.get("patterns", [])})
    digits = collections.defaultdict(set)
    for num in list(rec) + list(charges):
        digits[re.sub(r"\D", "", num)].add(num)
    loose = re.compile(r"\b(?:" + "|".join(re.escape(p) for p in prefixes) + r")-[A-Z0-9][A-Z0-9-]*\d\b")
    shipped = collections.defaultdict(dict)       # lot -> flow -> the most its maker's lines of the flow carry
    for key, d, root in docs:
        date = issue_date(root)
        # any text: every number in a maker's form is recorded, and no recorded number in another form
        for e in root.iter():
            if not isinstance(e.tag, str) or not e.text:
                continue
            for maker, rx in patterns:
                for m in rx.finditer(e.text):
                    tok = m.group(0)
                    if tok not in rec and tok not in charges:
                        out.append(f"{key}: {tok} (in {local(e)}) is in the form of {maker}'s numbers, but not in "
                                   "its production record (O64)")
                    elif date and tok in rec and rec[tok]["made"] > date:
                        out.append(f"{key}: quotes {tok} on {date}, before it was made on {rec[tok]['made']}")
            for m in loose.finditer(e.text):
                tok = m.group(0)
                if tok in rec or tok in charges:
                    continue
                same = digits.get(re.sub(r"\D", "", tok), set())
                letters = re.findall(r"[A-Z]+", tok)
                same = {s for s in same if re.findall(r"[A-Z]+", s) == letters}
                if same:
                    out.append(f"{key}: {tok} (in {local(e)}) looks like {', '.join(sorted(same))} written in "
                               "another form: a number, once assigned, never changes (O64)")
        # the structured elements, line by line
        lines = collections.OrderedDict()
        for inst in root.iter("{*}ItemInstance"):
            line = line_of(inst)
            nums = [x.text for x in inst.findall("{*}LotIdentification/{*}LotNumberID")]
            sers = [x.text for x in inst.findall("{*}SerialID")]
            trace = [x.text for x in inst.findall("{*}ProductTraceID")]
            on = named_items(item_of(inst), ids)
            made = inst.findtext("{*}ManufactureDate")
            expiry = inst.findtext("{*}LotIdentification/{*}ExpiryDate")
            ln = lines.setdefault(id(line), {"line": line, "lots": [], "serials": [], "on": on})
            ln["lots"] += nums
            ln["serials"] += sers
            for num in nums + sers + trace:
                r = rec.get(num)
                if not r:
                    out.append(f"{key}: {num} has no production record of its maker (O64)")
                    continue
                if on and not (on & r["on"]):
                    out.append(f"{key}: {num} is quoted on {', '.join(sorted(on))}, but its record is "
                               f"{r['item']} (O64)")
                if made and made != r["made"]:
                    out.append(f"{key}: {num} has manufacture date {made}, its record {r['made']}")
                if expiry and num in nums and expiry != r.get("expiry"):
                    out.append(f"{key}: lot {num} expires {expiry}, its record {r.get('expiry')}")
            for s, t in zip(sers, trace):
                if s.split("-")[-1] != t.split("-")[-1]:
                    out.append(f"{key}: serial {s} with trace number {t}: the trace number is the serial's count")
        for ln in lines.values():
            q, unit = line_qty(ln["line"])
            if q is None:
                continue
            lots = list(dict.fromkeys(ln["lots"]))
            if lots and all(n in rec for n in lots):
                made = sum(D(rec[n]["qty"]) for n in lots)
                if q > made:
                    out.append(f"{key}: a line of {q} {unit} of lot(s) {', '.join(lots)}, which made {made}")
                maker = rec[lots[0]]["maker"]
                own = {i for i in ln["on"] if items[i]["seller"] == maker}
                ours = ln["line"] is not None and any(
                    x.text in {items[i]["sellers_id"] for i in own}
                    for x in ln["line"].iter("{*}ID") if local(x.getparent()) == "SellersItemIdentification")
                if len(lots) == 1 and ours:
                    f = d["flow"]
                    shipped[lots[0]][f] = max(shipped[lots[0]].get(f, 0), q)
            sers = list(dict.fromkeys(ln["serials"]))
            rej = ln["line"].findtext("{*}RejectedQuantity") if ln["line"] is not None else None
            if sers and not lots and unit == "EA" and q != len(sers) and not (rej and D(rej) == len(sers)):
                out.append(f"{key}: a line of {q} with {len(sers)} serials: one serial a unit (or each unit "
                           "rejected)")
    for lot, flows in shipped.items():
        total = sum(flows.values())
        if total > D(rec[lot]["qty"]):
            out.append(f"lot {lot}: its maker ships {total} over the flows {', '.join(sorted(flows))}, but made "
                       f"{rec[lot]['qty']} (O64)")
    return out


# ---------------------------------------------------------------- goods chains (O66)
def ref_root(docs, ref):
    for key, d, root in docs:
        if key == ref:
            return root
    return None


def quantity(root, items, ids, entry, unit):
    """The quantity of an entry of a chain in its document, in the chain's unit."""
    total = Decimal(0)
    if entry.get("goods"):
        for g in root.iter("{*}GoodsItem"):
            for c in g:
                if local(c) == "Quantity" and c.text:
                    total += D(c.text) * D(UNIT_TO[(c.get("unitCode"), unit)])
        return total
    it = items[entry["item"]]
    for line in root.iter():
        if not isinstance(line.tag, str) or not local(line).endswith("Line") or local(line) == "OrderLine":
            continue
        item = line.find("{*}Item")
        if item is None or entry["item"] not in named_items(item, ids):
            continue
        q, u = line_qty(line)
        if q is None:
            continue
        if entry.get("part"):
            kg = sum(D(p["n"]) * D(p["kg"]) for p in it["parts"] if p["name"] == entry["part"])
            total += q * kg * D(UNIT_TO.get((u, "EA"), 1)) if unit == "KGM" else q
        elif entry.get("content"):
            total += q * D(it["content"]["count"])
        elif (u, unit) in UNIT_TO:
            total += q * D(UNIT_TO[(u, unit)])
        elif unit == "KGM":
            total += q * D(it["net_kg"])
        else:
            raise KeyError(f"no conversion from {u} to {unit}")
    return total


def chain_problems(world, items, docs):
    out = []
    chains = world.get("chains")
    if not chains:
        return ["goods chains: none (world/items.json chains)"]
    rec, _ = records(world, items)
    ids = item_ids(items)
    for name, ch in chains.items():
        if name == "note":
            continue
        where = f"goods chain {name}"
        if ch.get("ledger"):
            if not world.get(ch["ledger"]):
                out.append(f"{where}: its ledger {ch['ledger']} is missing")
            continue
        lo, hi = (D(x) for x in ch["rate"])
        if ch.get("steps"):
            top = Decimal(1)
            for s in ch["steps"]:
                r = s["rate"]
                top *= D(r[1] if isinstance(r, list) else r)
            if abs(top - hi) > Decimal("0.01"):
                out.append(f"{where}: its highest rate {hi} is not the product of its steps, {top:.3f}")
        sums = {}
        for side in ("in", "out"):
            total = Decimal(0)
            for e in ch[side]:
                if e.get("record"):
                    r = rec.get(e["record"])
                    if not r:
                        out.append(f"{where}: {e['record']} has no production record")
                        continue
                    total += D(r["qty"])
                    continue
                root = ref_root(docs, e["doc"])
                if root is None:
                    out.append(f"{where}: no built document {e['doc']}")
                    continue
                date = issue_date(root)
                if not ch["period"][0] <= date <= ch["period"][1]:
                    out.append(f"{where}: {e['doc']} of {date} is outside the period {ch['period'][0]} to "
                               f"{ch['period'][1]}")
                q = quantity(root, items, ids, e, ch["unit"])
                if not q:
                    out.append(f"{where}: {e['doc']} has no quantity of {e.get('item', 'goods')}")
                total += q
            sums[side] = total
        if ch.get("balance"):
            if sums["out"] != sums["in"]:
                out.append(f"{where}: {sums['in']} {ch['unit']} in, {sums['out']} out: a balance (O66)")
        elif sums["out"] > sums["in"] * hi:
            out.append(f"{where}: {sums['out']} {ch['unit']} out of {sums['in']} in is a rate of "
                       f"{sums['out'] / sums['in']:.3f}, above the highest, {hi} (O66)")
    return out


def chain_figures(world, items, docs):
    ids = item_ids(items)
    rec, _ = records(world, items)
    out = []
    for name, ch in world.get("chains", {}).items():
        if name == "note" or ch.get("ledger"):
            continue
        s = {}
        for side in ("in", "out"):
            s[side] = sum((D(rec[e["record"]]["qty"]) if e.get("record") else
                           quantity(ref_root(docs, e["doc"]), items, ids, e, ch["unit"])) for e in ch[side])
        out.append(f"goods chain {name}: {s['in']} {ch['unit']} in, {s['out']} out, rate "
                   f"{s['out'] / s['in']:.3f} (range {ch['rate'][0]} to {ch['rate'][1]})")
    return out


# ---------------------------------------------------------------- item physics (O62)
def physics_problems(world, items):
    out = []
    mats = {k: v for k, v in world.get("materials", {}).items() if k != "note"}
    if not mats:
        return ["materials: none (world/items.json materials)"]
    for k, m in mats.items():
        if not m["range"][0] <= m["kg_m3"] <= m["range"][1] or not m.get("source"):
            out.append(f"material {k}: its density {m['kg_m3']} needs a range around it and a source")
    for iid, it in items.items():
        if it.get("net_kg") is None:
            continue
        where = f"item {iid}"
        ph = it.get("physics")
        if not ph:
            out.append(f"{where}: has a weight but no physics sheet (O62)")
            continue
        net = D(it["net_kg"])
        by = ph.get("by")
        mat = mats.get(ph.get("material")) if ph.get("material") else None
        if ph.get("material") and not mat:
            out.append(f"{where}: unknown material {ph['material']}")
            continue

        def in_range(rho, what):
            if not D(mat["range"][0]) <= rho <= D(mat["range"][1]):
                out.append(f"{where}: {what} give a density of {rho:.0f} kg/m³, outside {mat['name']}'s "
                           f"{mat['range'][0]} to {mat['range'][1]} (O62)")
        if by == "envelope":
            l_, w_, h_ = (D(x) / 1000 for x in ph["envelope_mm"])
            in_range(net / (l_ * w_ * h_ * D(ph["solid_fraction"])), "its envelope, solid fraction and weight")
            dims = it.get("dimensions_mm")
            if dims and sorted(dims) != sorted(ph["envelope_mm"]) and not it.get("parts"):
                out.append(f"{where}: its envelope {ph['envelope_mm']} is not its dimensions {dims}")
        elif by == "sheet":
            a = D(ph["sheet_mm"][0]) * D(ph["sheet_mm"][1]) / 10**6
            in_range(net / (a * ph["layers"] * D(ph["thickness_um"]) / 10**6), "its film")
        elif by == "volume":
            per = {"MTQ": 1, "LTR": Decimal("0.001")}.get(it["unit"])
            if per is None:
                out.append(f"{where}: sold by volume, but in {it['unit']}")
            else:
                in_range(net / per, f"its weight a {it['unit']}")
        elif by == "mass":
            if it["unit"] not in UNIT_KG or net != UNIT_KG[it["unit"]]:
                out.append(f"{where}: sold by mass in {it['unit']}, but a unit weighs {net} kg")
        elif by == "energy":
            lo, hi = (D(x) for x in ph["kg_per_mwh"])
            if it["unit"] != "MWH" or not lo <= net <= hi or not ph.get("source"):
                out.append(f"{where}: {net} kg a {it['unit']} is outside its calorific range {lo} to {hi} kg/MWh")
        elif by == "contents":
            s = sum(D(c[1]) for c in ph["contents"])
            if abs(s - net) > Decimal("0.005"):
                out.append(f"{where}: its contents weigh {s} kg, its net weight is {net} kg")
        elif by == "content":
            c = it["content"]
            s = D(c["count"]) * D(items[c["item"]]["net_kg"])
            if abs(s - net) > Decimal("0.01"):
                out.append(f"{where}: {c['count']} × {c['item']} weigh {s} kg, its net weight is {net} kg")
        elif by == "parts":
            if not it.get("parts"):
                out.append(f"{where}: its weight is its parts', but it lists none")
            else:
                for p in it["parts"]:
                    src = [i for i in items.values() if i.get("physics", {}).get("envelope_mm") and p.get("mm")
                           and sorted(i["physics"]["envelope_mm"]) == sorted(p["mm"])]
                    for s in src:
                        if abs(D(s["net_kg"]) - D(p["kg"])) > Decimal("0.01"):
                            out.append(f"{where}: its part {p['name']} weighs {p['kg']} kg, the item {s['id']} "
                                       f"{s['net_kg']} kg")
        elif by != "unit":
            out.append(f"{where}: physics by {by}: unknown")
        if D(it["gross_kg"]) < net:
            out.append(f"{where}: gross weight below net weight")
        # the handling limit, for the package a person lifts
        lift = ph.get("lift")
        if lift in (1, 2):
            per = (it.get("carton") or {}).get("per_carton") or (it.get("package") or {}).get("per_package") or 1
            kg = D(it["gross_kg"]) * D(per)
            if kg > HANDLING_LIMIT_KG[lift] and not ph.get("aid"):
                out.append(f"{where}: a package of {kg} kg lifted by {lift} person(s) is above the handling limit "
                           f"of {HANDLING_LIMIT_KG[lift]} kg (D20, O62)")
        elif lift not in ("machine", None):
            out.append(f"{where}: lift {lift}: one, two or machine")
    # an item in oak and the same model in ash: the same wood volume, so the weights go with the densities
    for iid, it in items.items():
        if not iid.endswith("-oak") or (iid[:-4] + "-ash") not in items:
            continue
        ash = items[iid[:-4] + "-ash"]
        mo, ma = it.get("physics", {}).get("material"), ash.get("physics", {}).get("material")
        if (mo, ma) != ("oak", "ash"):
            continue
        want = D(mats["oak"]["kg_m3"]) / D(mats["ash"]["kg_m3"])
        got = D(it["net_kg"]) / D(ash["net_kg"])
        if abs(got - want) > Decimal("0.02") * want:
            out.append(f"item {iid}: weighs {got:.3f} times its ash variant, but oak is {want:.3f} times as dense "
                       "(O62)")
    return out


# ---------------------------------------------------------------- loads (O62)
def fleet(world):
    by_plate, by_vessel, by_train, by_party = {}, {}, {}, collections.defaultdict(list)
    for p in world["parties"] + world.get("abroad", []):
        for v in p.get("fleet") or []:
            v = {**v, "party": p["id"]}
            by_party[p["id"]].append(v)
            if v.get("plate"):
                by_plate[v["plate"]] = v
            if v.get("kind") in ("sea", "inland"):
                by_vessel[v["name"]] = v
            for t in (v.get("train"), v.get("ore_train")):
                if t:
                    by_train[t] = v
    return by_plate, by_vessel, by_train, by_party


def cargo(root):
    """The load of a document: containers (id -> gross with tare, size type), the cargo's gross weight, and the
    transport handling units with their floor area and stacking."""
    cont = {}
    for te in root.iter("{*}TransportEquipment"):
        if te.findtext("{*}TransportEquipmentTypeCode") == "CN" or te.findtext("{*}SizeTypeCode"):
            g = te.findtext("{*}GrossWeightMeasure")
            c = cont.setdefault(te.findtext("{*}ID"), {"kg": None, "size": None})
            c["kg"] = c["kg"] or (D(g) if g else None)
            c["size"] = c["size"] or te.findtext("{*}SizeTypeCode")
    g = root.find(".//{*}Consignment/{*}GrossWeightMeasure")
    kg = D(g.text) if g is not None else None
    if kg is None:
        gi = [D(x.text) for x in root.iter("{*}GrossWeightMeasure") if local(x.getparent()) == "GoodsItem"]
        kg = sum(gi) if gi else None
    thus, area = 0, Decimal(0)
    for t in root.iter("{*}TransportHandlingUnit"):
        if t.find("{*}TransportEquipment") is not None and t.find("{*}TransportHandlingUnitTypeCode") is None:
            continue           # the equipment, not a unit on it
        thus += 1
        dims = {m.findtext("{*}AttributeID"): D(m.findtext("{*}Measure"))
                for m in t.findall("{*}MeasurementDimension") if m.findtext("{*}Measure")}
        stack = 2 if t.findtext("{*}HandlingCode") == "STACK2" else 1
        if "LENGTH" in dims and "WIDTH" in dims:
            area += dims["LENGTH"] * dims["WIDTH"] / 10**6 / stack
    q = root.find(".//{*}TotalTransportHandlingUnitQuantity")
    if q is not None and not thus:
        thus = int(D(q.text))
    return cont, kg, thus, area


def road_problems(where, v, cont, kg, thus, area, runs=1):
    """A road vehicle's load; on a container chassis one box a run (the leg's runs, world/documents.json), the
    heaviest box then the load of a run."""
    out = []
    if v.get("type") == "37" and runs > 1 and cont:
        if len(cont) > runs:
            out.append(f"{where}: {len(cont)} containers in {runs} runs of one container chassis ({v['plate']})")
        cont = dict([max(cont.items(), key=lambda c: c[1]["kg"] or 0)])
    tare = sum(D(x) for x in (v.get("tare_kg") or {}).values())
    limit = D(v.get("max_gross_kg") or ROAD_MAX_KG)
    load = sum(c["kg"] for c in cont.values() if c["kg"]) if cont else (kg or 0)
    if tare and tare + load > limit:
        out.append(f"{where}: {v['name']} ({v['plate']}) weighs {tare + load} kg loaded, above {limit} kg (O62)")
    tank = v.get("tank")
    if tank and kg and kg > D(tank["max_load_kg"]):
        out.append(f"{where}: {kg} kg in a tank for {tank['max_load_kg']} kg")
    if v.get("type") == "37" and len(cont) > 1:
        out.append(f"{where}: {len(cont)} containers on one container chassis ({v['plate']})")
    if v.get("loading_m") and area > D(v["loading_m"]) * DECK_WIDTH_M:
        out.append(f"{where}: {area:.1f} m² of pallets on {v['loading_m']} m of floor ({v['plate']}) (O62)")
    if v.get("pallets") and not area and thus > v["pallets"]:
        out.append(f"{where}: {thus} pallets on a vehicle for {v['pallets']} ({v['plate']})")
    return out


def load_problems(world, docs):
    out, notes = [], []
    by_plate, by_vessel, by_train, by_party = fleet(world)
    named = collections.defaultdict(set)          # flow -> carriers whose vehicle a document names
    teu = collections.defaultdict(dict)           # vessel -> container -> TEU
    for key, d, root in docs:
        cont, kg, thus, area = cargo(root)
        plates = {e.text for e in root.iter("{*}LicensePlateID")}
        for pl in plates:
            v = by_plate.get(pl)
            if not v:
                continue
            named[d["flow"]].add(v["party"])
            runs = max([leg.get("runs", 1) for f in world["flows"] if f["id"] == d["flow"]
                        for leg in f.get("legs", []) if leg["carrier"] == v["party"] and leg["mode"] == "road"] or [1])
            out += road_problems(key, v, cont, kg, thus, area, runs)
        for vn in {e.text for e in root.iter("{*}VesselName")}:
            v = by_vessel.get(vn)
            if not v:
                continue
            named[d["flow"]].add(v["party"])
            for cid, c in cont.items():
                teu[vn][cid] = 2 if (c["size"] or "4").startswith("4") else 1
            if v["kind"] == "inland":
                if not v.get("deadweight_t"):
                    out.append(f"{key}: {vn} has no deadweight in the fleet data (O278)")
                elif kg and kg > D(v["deadweight_t"]) * 1000:
                    out.append(f"{key}: {vn} carries {kg} kg, above its deadweight of {v['deadweight_t']} t")
        for tr in {e.text for e in root.iter("{*}TrainID")}:
            v = by_train.get(tr)
            if not v:
                continue
            named[d["flow"]].add(v["party"])
            wagons = v.get("wagons") or []
            wagon = v.get("wagon") or {}
            if len(cont) > len(wagons) * wagon.get("slots", 1):
                out.append(f"{key}: {len(cont)} containers on train {tr} of {len(wagons)} container wagons")
            if not wagon.get("payload_kg"):
                out.append(f"{key}: train {tr}: the fleet data gives no payload per container wagon (O278)")
            else:
                for cid, c in cont.items():
                    if c["kg"] and c["kg"] > wagon["payload_kg"]:
                        out.append(f"{key}: container {cid} of {c['kg']} kg on a wagon for {wagon['payload_kg']} kg")
    for vn, cs in teu.items():
        v = by_vessel[vn]
        if v.get("capacity_teu") and sum(cs.values()) > v["capacity_teu"]:
            out.append(f"{vn}: {sum(cs.values())} TEU in the documents, above its {v['capacity_teu']}")
        elif not v.get("capacity_teu"):
            notes.append(f"{vn}: no TEU capacity in the fleet data")
    # the ore train: its ore wagons and their payload (O278)
    for key, d, root in docs:
        if d["flow"] == "ore" and d["doc"] == "Waybill":
            v = by_train.get(next((v["ore_train"] for vs in by_party.values() for v in vs if v.get("ore_train")),
                                  ""))
            if v:
                kg, n, pay = cargo(root)[1], len(v.get("ore_wagons", [])), (v.get("ore_wagon") or {}).get("payload_kg")
                if not pay:
                    out.append(f"{key}: the ore train's wagons have no payload in the fleet data (O278)")
                elif kg and kg > n * pay:
                    out.append(f"{key}: the ore train carries {kg} kg in {n} ore wagons of {pay} kg")
    # road legs whose vehicle no document names: the vehicle the leg names (world/documents.json "vehicle"), or the
    # carrier's one road vehicle, with the flow's largest despatch
    for f in world["flows"]:
        for leg in f.get("legs", []):
            if leg["mode"] != "road" or leg["carrier"] in named[f["id"]]:
                continue
            road = [v for v in by_party.get(leg["carrier"], []) if v["kind"] == "road"]
            if leg.get("vehicle"):
                road = [v for v in road if v["id"] == leg["vehicle"]]
                if not road:
                    out.append(f"{f['id']}: road leg {leg['from']} -> {leg['to']} names vehicle {leg['vehicle']}, "
                               f"which is not a road vehicle of {leg['carrier']}")
                    continue
            if len(road) != 1:
                out.append(f"{f['id']}: road leg {leg['from']} -> {leg['to']} by {leg['carrier']}: "
                           f"{len(road)} road vehicles in its fleet, none named in the documents or the leg (O278)")
                continue
            v = road[0]
            loads = [(key, cargo(root)) for key, d, root in docs if d["flow"] == f["id"]
                     and d["doc"] in ("DespatchAdvice", "PackingList", "Waybill", "ForwardingInstructions")
                     and d.get("from", leg["from"]) == leg["from"]]
            if not loads:
                continue
            key, c = max(loads, key=lambda kc: (kc[1][1] or 0, kc[1][3], kc[1][2]))
            out += road_problems(f"{key} (leg {leg['from']} -> {leg['to']})", v, *c)
            if not v.get("tare_kg"):
                notes.append(f"{f['id']}: {v['name']}: no tare in the fleet data")
    return out, notes


def check(world):
    items = {i["id"]: i for i in world["items"]}
    docs = built(world)
    out = lot_problems(world, items, docs)
    out += chain_problems(world, items, docs)
    out += physics_problems(world, items)
    loads, notes = load_problems(world, docs)
    notes = NOTES + notes
    out += loads
    return out, notes, (chain_figures(world, items, docs) if not out else [])


def main():
    world = world_data.load()
    problems, notes, figures = check(world)
    for p in problems:
        print(p)
    if not problems:
        items = {i["id"]: i for i in world["items"]}
        chains = [k for k in world.get("chains", {}) if k != "note"]
        sheets = sum(1 for i in items.values() if i.get("physics"))
        print(f"goods: {len(records(world, items)[0])} recorded lots and serials, {len(chains)} goods chains, "
              f"{sheets} physics sheets, the vehicles' loads: no problems ({len(notes)} notes, --notes lists them)")
    if "--notes" in sys.argv[1:]:
        for n in figures + notes:
            print("note:", n)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
