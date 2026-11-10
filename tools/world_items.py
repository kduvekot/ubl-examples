#!/usr/bin/env python3
"""The items of the UBL example world (world/items.json), and their checks.

Every party that sells something has items: goods with their measurements,
weights, packaging, customs tariff code and country of origin, or services.
Prices are in the seller's currency. A distributor or retailer that resells
an item has an item of its own that points to the original (resale_of), so
that the manufacturer's identifiers travel along the chain.

Checks:
  * units of measure and packaging types are codes of the UBL 2.5 default
    lists (UN/ECE Recommendations 20 and 21);
  * the world item number of goods, issued by the identifier issuing agency,
    has a valid check digit and is unique;
  * prices are positive and in the seller's currency; a unit price may have
    more decimals than the currency (up to 4), because only amounts to pay
    are rounded to the currency's minor unit; gross weight is at least net
    weight;
  * customs tariff codes have the form of an HS subheading (6 digits);
  * a resold item points to an item of another seller, and a component of a
    bill of materials to an existing item; and the reseller or maker orders
    it from that seller somewhere in the flows;
  * every party that bills or offers in the documents (Invoice, Credit Note,
    self-billed documents, Quotation, Catalogue, Purchase Receipt, Utility
    Statement) has items to put on its lines, and every seller of items
    takes part in such a document;
  * the exchange rates between the world's currencies agree with each other.

Usage: python3 tools/world_items.py      (prints the problems, exit 1 if any)
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402

UNIT_PRICE_DECIMALS = 4   # a unit price may have more decimals than its currency
ISSUER = "31-xu"   # the identifier issuing agency
SELLING = {"Invoice": "AccountingSupplierParty", "CreditNote": "AccountingSupplierParty",
           "SelfBilledInvoice": "AccountingSupplierParty", "SelfBilledCreditNote": "AccountingSupplierParty",
           "Quotation": "SellerSupplierParty", "Catalogue": "ProviderParty",
           "PurchaseReceipt": "AccountingSupplierParty", "UtilityStatement": "SenderParty"}


def item_number(body):
    """A world item number: 12 digits, the last a check digit (weights 3 and 1 from the right, modulus 10)."""
    s = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(body)))
    return body + str((10 - s % 10) % 10)


def valid_item_number(n):
    return bool(re.fullmatch(r"\d{12}", n)) and item_number(n[:-1]) == n


def codes():
    return json.load(open(os.path.join(world_data.ROOT, "world", "codelists", "ubl-default-codes.json"), encoding="utf-8"))


def check(world):
    problems = []
    parties = {p["id"]: p for p in world["parties"]}
    items = {i["id"]: i for i in world["items"]}
    cl = codes()
    units, packs = cl["UnitOfMeasureCode"]["codes"], cl["PackagingTypeCode"]["codes"]
    seen = {}
    for it in world["items"]:
        where = f"item {it['id']}"
        seller = parties.get(it["seller"])
        if not seller:
            problems.append(f"{where}: unknown seller {it['seller']}")
            continue
        cur = world["countries"][seller["c"]]["currency"]
        if it["unit"] not in units:
            problems.append(f"{where}: unit {it['unit']} is not a UN/ECE Rec 20 code of the UBL list")
        if it.get("package") and it["package"]["type"] not in packs:
            problems.append(f"{where}: packaging {it['package']['type']} is not a UN/ECE Rec 21 code of the UBL list")
        pr = it["price"]
        if pr["currency"] != cur["code"]:
            problems.append(f"{where}: price in {pr['currency']}, but the seller's currency is {cur['code']}")
        if pr["amount"] <= 0:
            problems.append(f"{where}: price must be positive")
        # a unit price may be finer than the currency (29.80 yen per kWh is normal); amounts to pay are
        # rounded to the currency's minor units, which the amounts layer checks
        if round(pr["amount"], UNIT_PRICE_DECIMALS) != pr["amount"]:
            problems.append(f"{where}: unit price {pr['amount']} has more than {UNIT_PRICE_DECIMALS} decimals")
        if it["kind"] == "goods" and not it.get("resale_of"):
            n = it.get("standard_id")
            if not n or not valid_item_number(n):
                problems.append(f"{where}: goods need a world item number with a valid check digit")
            elif n in seen:
                problems.append(f"{where}: same world item number as {seen[n]}")
            else:
                seen[n] = it["id"]
            hs = it.get("hs", "")
            if not re.fullmatch(r"\d{4}\.\d{2}", hs):
                problems.append(f"{where}: customs tariff code {hs!r} is not an HS subheading (nnnn.nn)")
            if it.get("origin") not in world["countries"]:
                problems.append(f"{where}: country of origin {it.get('origin')} is not a country of the world")
            if it.get("gross_kg", 0) < it.get("net_kg", 0):
                problems.append(f"{where}: gross weight below net weight")
        if it.get("resale_of"):
            orig = items.get(it["resale_of"])
            if not orig:
                problems.append(f"{where}: resale of unknown item {it['resale_of']}")
            elif orig["seller"] == it["seller"]:
                problems.append(f"{where}: resale of its own item")
        for comp in it.get("components", []):
            if comp["item"] not in items:
                problems.append(f"{where}: component {comp['item']} is not an item of the world")
    # cross-layer: who bills or offers has items, who has items bills or offers
    sellers = {i["seller"] for i in world["items"]}
    billing = set()
    for d in world["documents"]:
        el = SELLING.get(d["doc"])
        if not el or el not in d["parties"]:
            continue
        who = d["parties"][el]
        billing.add(who)
        if who not in sellers:
            problems.append(f"{d['flow']} {d['doc']} {d['from']} -> {d['to']}: {who} sells but has no items")
    for s in sorted(sellers - billing):
        problems.append(f"party {s}: has items but never bills or offers them")
    # a component or a resold item is bought: an order from the maker or reseller to the item's seller exists
    bought = {(d["parties"].get("BuyerCustomerParty"), d["parties"].get("SellerSupplierParty"))
              for d in world["documents"] if d["doc"] == "Order"}
    for it in world["items"]:
        needs = [items[c["item"]] for c in it.get("components", []) if c["item"] in items]
        if it.get("resale_of") in items:
            needs.append(items[it["resale_of"]])
        for n in needs:
            if (it["seller"], n["seller"]) not in bought:
                problems.append(f"item {it['id']}: needs {n['id']}, but {it['seller']} never orders from {n['seller']}")
    # exchange rates agree: a/b * b/c = a/c
    rates = {tuple(k.split("/")): v for k, v in world.get("exchange_rates", {}).items()}
    if not rates:
        problems.append("no exchange rates between the world's currencies (world/countries.json)")
    for (a, b), r1 in rates.items():
        for (b2, c), r2 in rates.items():
            if b == b2 and (a, c) in rates and abs(r1 * r2 - rates[(a, c)]) > 1e-9 * rates[(a, c)]:
                problems.append(f"exchange rates {a}/{b} x {b}/{c} = {r1 * r2}, but {a}/{c} = {rates[(a, c)]}")
    return problems


if __name__ == "__main__":
    w = world_data.load()
    probs = check(w)
    print("\n".join(probs) or f"items: {len(w['items'])} items of {len({i['seller'] for i in w['items']})} sellers, no problems")
    sys.exit(1 if probs else 0)
