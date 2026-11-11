#!/usr/bin/env python3
"""The specifications the documents of the world claim: CustomizationID and ProfileID (world/specifications.json).

A transaction is one kind of business message between two roles, with a defined purpose, content and rules, as in
CEN BII and Peppol; one or more document types carry it. Its specification has three levels, chained in
CustomizationID with "#compliant#" (the EN 16931 / Peppol / XRechnung convention):

  1. the transaction of the Lumeport Trade Accord        urn:ubl-examples:world:trns:<transaction>:1.0
  2. a national specification built on it, where the sender's or receiver's country has one
                                                         urn:ubl-examples:world:<CC>:<name>:1.0
  3. the specification of a community of trading partners that exchange among themselves
                                                         urn:ubl-examples:world:community:<name>:1.0

ProfileID names the Accord's process profile the document belongs to (urn:ubl-examples:world:profile:<name>:1.0),
generic and versioned; it no longer names a flow. ProfileExecutionID still names one run of the process.
"""
import json
import os

import world_data

PATH = os.path.join(world_data.ROOT, "world", "specifications.json")
COMPLIANT = "#compliant#"
_SPECS = None


def load():
    global _SPECS
    if _SPECS is None:
        _SPECS = json.load(open(PATH, encoding="utf-8"))
    return _SPECS


def urn(level, key):
    s = load()
    return s["urns"][level].format(id=key, version=s["version"])


def described():
    """Every specification by its URN: {urn: (level, key, spec)}."""
    s = load()
    out = {}
    for level, group in (("transaction", "transactions"), ("national", "national"), ("community", "communities"),
                         ("profile", "profiles")):
        for key, spec in s[group].items():
            out[urn(level, key)] = (level, key, spec)
    return out


def _parties(doc):
    return {path.split("/")[0]: pid for path, pid in doc["parties"].items() if isinstance(pid, str)}


def transaction(doc):
    hits = [k for k, t in load()["transactions"].items() if doc["doc"] in t["documents"]]
    if len(hits) != 1:
        raise SystemExit(f"{doc['flow']} {doc['doc']}: {len(hits)} transactions in world/specifications.json carry it")
    return hits[0]


def national(doc, world):
    """The national specification that applies to the document, or None."""
    party = {p["id"]: p for p in world["parties"]}
    roles = _parties(doc)
    for key, spec in load()["national"].items():
        if doc["doc"] not in spec["documents"]:
            continue
        w = spec["when"]
        seller = roles.get("AccountingSupplierParty")
        buyer = roles.get("AccountingCustomerParty")
        if w.get("seller_country") and seller and party[seller]["c"] == w["seller_country"]:
            return key
        if w.get("buyer_public") and buyer and party[buyer]["c"] == w["buyer_public"] and \
                party[buyer]["cat"] in ("government", "procurement"):
            return key
    return None


def community(doc):
    """The community specification the document follows, or None."""
    for key, spec in load()["communities"].items():
        if spec["when"] == "between_members" and doc["from"] in spec["members"] and doc["to"] in spec["members"]:
            return key
        if spec["when"] == "flow_and_documents" and doc["flow"] in spec["flows"] and doc["doc"] in spec["documents"]:
            return key
    return None


def customization(doc, world):
    """The CustomizationID of a document, and why."""
    t = transaction(doc)
    parts = [urn("transaction", t)]
    s = load()
    why = [f"the Trade Accord's transaction \"{s['transactions'][t]['name']}\""]
    n = national(doc, world)
    if n:
        parts.append(urn("national", n))
        why.append(f"the national specification \"{s['national'][n]['name']}\"")
    c = community(doc)
    if c:
        parts.append(urn("community", c))
        why.append(f"the community specification \"{s['communities'][c]['name']}\"")
    return COMPLIANT.join(parts), why


def profile(doc):
    """The ProfileID of a document: the first process profile that carries its document type and whose flow or
    community, where it names one, is the document's."""
    s = load()
    c = community(doc)
    for key, p in s["profiles"].items():
        if doc["doc"] not in p["documents"]:
            continue
        if (p.get("flows") or p.get("communities")) and not (doc["flow"] in p.get("flows", []) or
                                                            c in p.get("communities", [])):
            continue
        return key
    raise SystemExit(f"{doc['flow']} {doc['doc']}: no process profile in world/specifications.json carries it")
