#!/usr/bin/env python3
"""The documents of the UBL example world, checked against the UBL 2.5 model.

world/documents.json lists the flows of the world (an ore delivery, a public
tender, ...) and in each flow the documents that are exchanged: the document
type, who sends it, who receives it, why, and every party it mentions at its
place in the UBL structure (for example Order/Delivery/Despatch/CarrierParty).

world/ubl-model.json (made by tools/extract_ubl_model.py from the UBL 2.5
entity model) says which party element of each document type sends it and
which receives it. This module checks every document against the model:

  * every path exists in the UBL structure of that document type;
  * the sender fills a sender element of the document and the receiver a
    receiver element, or the document says on whose behalf they act;
  * every mandatory party element at document level is filled;
  * no document type, association or property is deprecated: the world
    uses only what UBL 2.5 endorses;
  * a bank named in a document is the bank of that account holder;
  * values that UBL requires to be manifest are stated (rule IND6), such as
    the delivery terms of an order;
  * every party of the world sends, receives or is mentioned in a document.

Usage: python3 tools/world_docs.py      (prints the problems, exit 1 if any)
"""
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
SPEC = "https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html"


def load_model():
    return json.load(open(os.path.join(ROOT, "world", "ubl-model.json"), encoding="utf-8"))


def words(name):
    """'DespatchAdvice' -> 'Despatch Advice'."""
    return re.sub(r"(?<!^)(?=[A-Z])", " ", name).replace(" Of ", " of ")


def spec_link(doc):
    return f"{SPEC}#S-{words(doc).upper().replace(' ', '-')}-SCHEMA"  # e.g. #S-BILL-OF-LADING-SCHEMA


def resolve(model, doc, path):
    """The last association of a path below a document: (name, target, cardinality, definition), or None."""
    a, last = doc, None
    for step in path.split("/"):
        hit = [x for x in model["abies"][a]["asbies"] if x[0] == step]
        if not hit:
            return None
        last = hit[0]
        a = last[1]
    return last


DEPRECATED = "(Deprecated)"


def walk(model, doc, path):
    """Problems with a path below a document: a step that does not exist or is deprecated.
    The last step may be a basic property (for a value)."""
    a, steps = doc, path.split("/")
    for i, step in enumerate(steps):
        hit = [x for x in model["abies"][a]["asbies"] if x[0] == step]
        if not hit:
            bbie = [b for b in model["abies"][a]["bbies"] if b[0] == step]
            if bbie and i == len(steps) - 1:
                return [f"{doc}/{path}: {step} is deprecated"] if bbie[0][2] else []
            return [f"{doc}/{path} does not exist in UBL 2.5"]
        if hit[0][3].startswith(DEPRECATED) or model["abies"][hit[0][1]]["deprecated"]:
            return [f"{doc}/{path}: {step} is deprecated"]
        a = hit[0][1]
    return []


# Values that must be stated in a document type, because leaving them out would
# carry meaning, which UBL forbids (rule IND6, "Manifest Values" in section 2.2.2).
MANIFEST = {
    # who arranges and pays the transport follows from the delivery terms, never from a missing carrier
    "Order": ["DeliveryTerms/ID"],
}


def ids(value):
    return value if isinstance(value, list) else [value]


def fills(doc, party):
    """Paths in a document that the party fills."""
    return [k for k, v in doc["parties"].items() if party in ids(v)]


def bank_problems(world, d):
    """A bank named in a document must be the bank where the account holder keeps its account:
    the payee's account (PayeeParty, else AccountingSupplierParty) and the payer's (AccountingCustomerParty)."""
    out = []
    party = {p["id"]: p for p in world["parties"]}
    holder = {"PayeeFinancialAccount": d["parties"].get("PayeeParty", d["parties"].get("AccountingSupplierParty")),
              "PayerFinancialAccount": d["parties"].get("AccountingCustomerParty")}
    for path, bank in d["parties"].items():
        steps = path.split("/")
        if steps[-1] != "FinancialInstitution":
            continue
        account = next((s for s in steps if s in holder), None)
        who = holder.get(account)
        acc = party.get(who, {}).get("identity", {}).get("account") if who else None
        if not acc:
            out.append(f"{path}: {who} has no account in the world")
        elif acc["bank"] != bank:
            out.append(f"{path}: {who} keeps its account at {acc['bank']}, not at {bank}")
    return out


def check(world, model):
    problems = []
    parties = {p["id"] for p in world["parties"]}
    flows = {f["id"] for f in world["flows"]}
    used = set()
    for n, d in enumerate(world["documents"], 1):
        where = f"document {n} ({d['flow']} {d['doc']} {d['from']} -> {d['to']})"
        spec = model["documents"].get(d["doc"])
        if d["flow"] not in flows:
            problems.append(f"{where}: unknown flow")
        if spec is None:
            problems.append(f"{where}: not a UBL 2.5 document type")
            continue
        if spec["deprecated"]:
            problems.append(f"{where}: {d['doc']} is deprecated in UBL 2.5; use an endorsed document type")
        if d["from"] == d["to"]:
            problems.append(f"{where}: sender and receiver are the same party")
        for path, value in d["parties"].items():
            problems += [f"{where}: {x}" for x in walk(model, d["doc"], path)]
            if resolve(model, d["doc"], path) is None and not walk(model, d["doc"], path):
                problems.append(f"{where}: {d['doc']}/{path} is not an association")
            for v in ids(value):
                if v not in parties:
                    problems.append(f"{where}: unknown party {v} at {path}")
                used.add(v)
        for side, key, elements in (("sender", "from", spec["senders"]), ("receiver", "to", spec["receivers"])):
            party = d[key]
            if party not in parties:
                problems.append(f"{where}: unknown {side} {party}")
            if not elements:
                continue
            agent_for = d.get("sends_for" if side == "sender" else "receives_for")
            if agent_for:
                if agent_for not in elements:
                    problems.append(f"{where}: {agent_for} is not a {side} element of {d['doc']}")
                elif agent_for not in d["parties"]:
                    problems.append(f"{where}: the {side} acts for {agent_for}, which is not filled")
                if not fills(d, party):
                    problems.append(f"{where}: the {side} acts for another party but is not in the document")
            elif not set(fills(d, party)) & set(elements):
                problems.append(f"{where}: the {side} {party} must fill {' or '.join(elements)}")
        for path in d.get("values", {}):
            problems += [f"{where}: {x}" for x in walk(model, d["doc"], path)]
        for path in MANIFEST.get(d["doc"], []):
            if path not in d.get("values", {}):
                problems.append(f"{where}: {path} must be stated (IND6: an absence carries no meaning)")
        for p in spec["parties"]:
            if p["cardinality"].startswith("1") and p["element"] not in d["parties"]:
                problems.append(f"{where}: mandatory {p['element']} is not filled")
        used.update((d["from"], d["to"]))
        problems += [f"{where}: {x}" for x in bank_problems(world, d)]
    for f in world["flows"]:
        if not any(d["flow"] == f["id"] for d in world["documents"]):
            problems.append(f"flow {f['id']}: has no documents")
    for p in sorted(parties - used):
        problems.append(f"party {p}: takes part in no document")
    return problems


def views(world, model):
    """Per party: the documents it sends, receives and is mentioned in, and its trading partners."""
    out = {p["id"]: {"sends": [], "receives": [], "mentioned": [], "partners": [], "elements": []}
           for p in world["parties"]}
    for d in world["documents"]:
        for pid in {d["from"], d["to"]} | {v for x in d["parties"].values() for v in ids(x)}:
            v = out[pid]
            if pid == d["from"]:
                v["sends"].append(d)
            elif pid == d["to"]:
                v["receives"].append(d)
            else:
                v["mentioned"].append(d)
            for path in fills(d, pid):
                el = path.rsplit("/", 1)[-1]
                if el not in v["elements"]:
                    v["elements"].append(el)
        for a, b in ((d["from"], d["to"]), (d["to"], d["from"])):
            if b not in out[a]["partners"]:
                out[a]["partners"].append(b)
    return out


def definition(model, d, path):
    hit = resolve(model, d["doc"], path)
    return hit[3] if hit else ""


if __name__ == "__main__":
    import world_data
    w = world_data.load()
    probs = check(w, load_model())
    print("\n".join(probs) or f"{len(w['documents'])} documents in {len(w['flows'])} flows: no problems")
    sys.exit(1 if probs else 0)
