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
  * goods are identified in their maker's convention (decision ID-Q7, D5): a
    GTIN under the company prefix of a GS1 party (GS1 prefix 952, reserved for
    examples); on the Codana side the globally unique form of ISO/IEC 15459
    (KXU, the maker's Codana company number and its own reference, the
    seller's item number without its initials and hyphens: at most 20
    characters, no check character); or only the seller's own number. A GS1
    wholesaler or retailer may give its own GTIN to an item it resells whose
    maker has none (D5), but not to one that already has a GTIN, because the
    brand owner numbers the item (D7); every number is unique. A store's own
    label made by another party (brand_owner, the private-label case: the
    Elderwick pieces Brackenmere makes for Brightmarket) carries a GTIN under
    the brand owner's prefix, whoever sells it;
  * prices are positive, except for an item given free with another of the
    same seller (free_with: the care kit with each Marrow bench, in oak or in
    ash), whose price
    is zero and in the seller's currency; a unit price may have
    more decimals than the currency (up to 4), because only amounts to pay
    are rounded to the currency's minor unit; gross weight is at least net
    weight;
  * items of one seller that share an item number are variants of one model,
    each with a variant code of its own (ExtendedID); on the GS1 side each
    variant has its own GTIN (O155: the Marrow bench and chair in oak and ash);
  * customs tariff codes have the form of an HS subheading (6 digits);
  * the CPC Ver.2.1 subclass of goods is the one the UN Statistics Division's correspondence HS 2017 -> CPC
    Ver.2.1 gives for its HS subheading (world/codelists/sources/cpc/CPC21-HS2017.csv; decision P5); the world
    uses HS 2022, so a subheading that is not in the HS 2017 table is reported, not failed;
  * a resold item points to an item of another seller, and a component of a
    bill of materials to an existing item; and the reseller or maker orders
    it from that seller somewhere in the flows;
  * every party that bills or offers in the documents (Invoice, Credit Note,
    self-billed documents, Quotation, Catalogue, Purchase Receipt, Utility
    Statement) has items to put on its lines, and every seller of items
    takes part in such a document;
  * the exchange rates between the world's currencies agree with each other;
  * a price agreed for one buyer (buyer_prices: Valdara's distributor price
    for Lumeway, D14) is below the seller's own price, in its currency, with
    a price type of the world's list that is before tax (O28); a price that
    includes the carriage to the buyer (delivered: an Incoterms rule under
    which the seller pays the main carriage, such as Lumeway's CIF price for
    the island, O30) may be above it;
  * prices along the chain (D14, O30; items.json resales): nobody resells
    below what they paid plus the freight the documents state (shared over
    a transport's load by gross weight) and the import tax they bear, and a
    reseller's gross margin falls in the band for its kind of business, or
    for the kind of goods where a sale names one (clothing), a promotion only
    below the upper limit; freight the buyer pays on top at cost (recharged)
    is neither the reseller's cost nor part of its price; every resold item
    is in a resale;
    a resale listed as awaiting the owner must still fail.

Usage: python3 tools/world_items.py      (prints the problems, exit 1 if any)
"""
import json
from decimal import Decimal
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
    """A GS1 key from its body: the check digit (weights 3 and 1 from the right, modulus 10) appended."""
    s = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(body)))
    return body + str((10 - s % 10) % 10)


CODANA_MAX = 20     # Codana's rule book: no identifier longer than 20 characters (ISO/IEC 15459, one-line bar code)


def codana_item_number(cin, sellers_id):
    """The globally unique form of an item number on the Codana side (D5): KXU, the company's Codana number and
    its own reference, the seller's item number without its initials and hyphens (VI-B180 -> KXU<cin>B180)."""
    return f"KXU{cin}{''.join(sellers_id.split('-')[1:])}"


CPC_HS = os.path.join(world_data.ROOT, "world", "codelists", "sources", "cpc", "CPC21-HS2017.csv")
NOTES = []        # what the checks report without failing
_CORRESPONDENCE = None


def cpc_for_hs(hs):
    """The CPC Ver.2.1 subclasses the official correspondence gives for an HS 2017 subheading (six digits), or None
    if the subheading is not in the HS 2017 table (new or changed in HS 2022)."""
    global _CORRESPONDENCE
    if _CORRESPONDENCE is None:
        import csv
        _CORRESPONDENCE = {}
        with open(CPC_HS, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                _CORRESPONDENCE.setdefault(r["HS 2017"].replace(".", ""), set()).add(r["CPC Ver. 2.1"])
    return _CORRESPONDENCE.get(hs)


def cpc_hs_problem(cpc, hs, where):
    """A problem if the CPC is not one the correspondence gives for the HS subheading; a note (NOTES) if the
    subheading is not in the HS 2017 table, which must then be checked by hand."""
    allowed = cpc_for_hs(hs)
    if allowed is None:
        note = f"{where}: HS {hs} is not in the HS 2017 -> CPC 2.1 correspondence (HS 2022 change?): check CPC {cpc} by hand"
        if note not in NOTES:
            NOTES.append(note)
        return None
    if cpc not in allowed:
        return f"{where}: CPC {cpc} is not the CPC Ver.2.1 the correspondence gives for HS {hs} ({', '.join(sorted(allowed))})"
    return None


def codes():
    """The codes of each UBL default code list (all versions the UBL 2.5 CVA names), with their names:
    {"UnitOfMeasureCode": {"codes": {code: name}}, ...}."""
    cva = json.load(open(os.path.join(world_data.ROOT, "world", "codelists", "ubl-default-codes.json"), encoding="utf-8"))
    out = {}
    for lst in sorted(cva["lists"].values(), key=lambda x: x["uri"]):   # later versions override names
        out.setdefault(lst["short"], {"codes": {}})["codes"].update(lst["names"])
    return out


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
        if "rate_percent" in pr:       # a premium on the insured value (O173)
            if not 0 < pr["rate_percent"] < 100 or pr.get("cover_percent", 0) < 100 or not pr.get("why"):
                problems.append(f"{where}: a rate price needs a rate between 0 and 100 %, a cover of at least 100 % "
                                "and its reason (why)")
        elif it.get("free_with"):
            if pr["amount"] != 0:
                problems.append(f"{where}: given free with {it['free_with']}, so its price is zero")
            for w in it["free_with"]:      # each piece it comes with: a model's variants are items of their own
                if items.get(w, {}).get("seller") != it["seller"]:
                    problems.append(f"{where}: given free with {w}, which is not an item of the same seller")
        elif pr["amount"] <= 0:
            problems.append(f"{where}: price must be positive")
        # a unit price may be finer than the currency (29.80 yen per kWh is normal); amounts to pay are
        # rounded to the currency's minor units, which the amounts layer checks
        if "amount" in pr and round(pr["amount"], UNIT_PRICE_DECIMALS) != pr["amount"]:
            problems.append(f"{where}: unit price {pr['amount']} has more than {UNIT_PRICE_DECIMALS} decimals")
        conv = seller["identity"].get("identification", {})
        if it.get("brand_owner"):        # a private label: the brand owner numbers the item, not the maker (D7)
            owner = parties.get(it["brand_owner"])
            if not owner:
                problems.append(f"{where}: unknown brand owner {it['brand_owner']}")
            else:
                conv = owner["identity"].get("identification", {})
                if it.get("resale_of") or not it.get("brand"):
                    problems.append(f"{where}: a brand owner only on the maker's item, with its brand")
        if it.get("gtin") and it.get("resale_of"):    # the brand owner numbers the item (D7)
            up = items.get(it["resale_of"])
            while up and not up.get("gtin"):
                up = items.get(up.get("resale_of"))
            if up:
                problems.append(f"{where}: a GTIN of its own, but the item it resells already has the GTIN "
                                f"{up['gtin']} of {up['seller']}: under GS1 rules the brand owner numbers the item")
        if it.get("gtin"):                # a GTIN under the GS1 company prefix of the party that allocates it
            if conv.get("convention") != "GS1":
                problems.append(f"{where}: a GTIN, but {it.get('brand_owner', it['seller'])} does not identify its "
                                "items the GS1 way")
            elif not (re.fullmatch(r"\d{13}", it["gtin"]) and it["gtin"].startswith(conv["company_prefix"])
                      and item_number(it["gtin"][:-1]) == it["gtin"]):
                problems.append(f"{where}: GTIN {it['gtin']} is not a GTIN-13 under the company prefix "
                                f"{conv['company_prefix']} with a valid check digit")
            elif it["gtin"] in seen:
                problems.append(f"{where}: same GTIN as {seen[it['gtin']]}")
            seen[it["gtin"]] = it["id"]
        if it["kind"] == "goods" and not it.get("resale_of"):
            n = it.get("standard_id")
            if conv.get("convention") == "GS1":
                if not it.get("gtin") or n:
                    problems.append(f"{where}: a GS1 maker identifies its goods by a GTIN only")
            elif conv.get("convention") == "own":
                if n:
                    problems.append(f"{where}: {it['seller']} identifies its goods by its own item numbers only, "
                                    "not by a Codana item number")
            elif conv.get("convention") != "ISO":
                problems.append(f"{where}: {it['seller']} has no identification convention (world/parties.json, "
                                "identification: GS1, ISO or own)")
            elif not n or n != codana_item_number(conv["codana_cin"], it["sellers_id"]):
                problems.append(f"{where}: goods of a Codana party need the item number "
                                f"{codana_item_number(conv['codana_cin'], it['sellers_id'])}: KXU, the maker's "
                                "company number and its own reference, the item's issuer being the maker (O32)")
            elif len(n) > CODANA_MAX or not re.fullmatch(r"KXU\d{5}[A-Z0-9]+", n):
                problems.append(f"{where}: Codana item number {n} is longer than {CODANA_MAX} characters or not "
                                "upper-case letters and digits")
            elif n in seen and not variants_of_one_model(it, items.get(seen[n], {})):
                problems.append(f"{where}: same item number as {seen[n]}")
            elif n not in seen:
                seen[n] = it["id"]
            hs = it.get("hs", "")
            if not re.fullmatch(r"\d{6}", hs):
                problems.append(f"{where}: customs tariff code {hs!r} is not an HS subheading (six digits)")
            if not re.fullmatch(r"\d{5}", it.get("cpc", "")):
                problems.append(f"{where}: goods need a UN CPC Ver.2.1 subclass (five digits)")
            elif re.fullmatch(r"\d{6}", hs):
                why = cpc_hs_problem(it["cpc"], hs, where)
                if why:
                    problems.append(why)
            nat = it.get("national_tariff")
            if nat and not (re.fullmatch(r"\d{8}", nat) and nat.startswith(hs)):
                problems.append(f"{where}: national tariff code {nat!r} does not extend the HS subheading {hs}")
            if it.get("origin") not in world["countries"]:
                problems.append(f"{where}: country of origin {it.get('origin')} is not a country of the world")
            if it.get("origin_criterion") not in ("P", "S", "V"):
                problems.append(f"{where}: goods need the Trade Accord's preference criterion of their origin "
                                "(origin_criterion P, S or V, D18)")
            if it.get("gross_kg", 0) < it.get("net_kg", 0):
                problems.append(f"{where}: gross weight below net weight")
        if it.get("resale_of") and it.get("standard_id"):
            problems.append(f"{where}: a resold item carries its maker's number, not one of its own")
        if it.get("resale_of"):
            orig = items.get(it["resale_of"])
            if not orig:
                problems.append(f"{where}: resale of unknown item {it['resale_of']}")
            elif orig["seller"] == it["seller"]:
                problems.append(f"{where}: resale of its own item")
        for comp in it.get("components", []):
            if comp["item"] not in items:
                problems.append(f"{where}: component {comp['item']} is not an item of the world")
    # variants: items of one seller under one item number differ by their variant (ExtendedID), and a GS1 item's
    # variants each carry a GTIN of their own, because the shopper sees and chooses them (O155)
    by_number = {}
    for it in world["items"]:
        by_number.setdefault((it["seller"], it["sellers_id"]), []).append(it)
    for (seller, number), its in sorted(by_number.items()):
        if len(its) < 2:
            continue
        ext = [i.get("variant", {}).get("extended") for i in its]
        if None in ext or len(set(ext)) != len(ext):
            problems.append(f"items {', '.join(i['id'] for i in its)}: one item number {number} of {seller}, but "
                            "not told apart by a variant of their own (variant.extended)")
    for it in world["items"]:
        if it.get("variant_numbers") and not (it.get("resale_of") and items.get(it["resale_of"], {}).get("variant")):
            problems.append(f"item {it['id']}: numbers a variant of its own (variant_numbers), but resells no variant")
        if it.get("variant") and not it["variant"].get("what"):
            problems.append(f"item {it['id']}: a variant needs what it differs in (variant.what)")
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
    problems += buyer_price_problems(world)
    problems += resale_problems(world)
    problems += physics_problems(items)
    problems += emission_problems(items)
    problems += chain_problems(world, items)
    return problems


def chain_problems(world, items):
    """The goods chain of the bench (D21, O65): in each warehouse's ledger the stock of every lot, serial and item
    never goes below zero and nothing leaves before it arrived; every lot and serial range was made before Valdara
    shipped it and arrives no earlier than it was shipped; a lot is shipped in no more than was made."""
    chain = world.get("goods_chain")
    if not chain:
        return []
    out = []
    made = {}
    for p in chain["production"]:
        if p["item"] not in items:
            out.append(f"goods chain: production of unknown item {p['item']}")
            continue
        key = p.get("lot") or tuple(p["serials"])
        made[(p["item"], key)] = p
        for fl, date in p["shipped"]:
            if date < p["made"]:
                out.append(f"goods chain: {key} is shipped in flow {fl} on {date}, before it was made on {p['made']}")
    serials = sorted((p["serials"][0], p["serials"][1], p["made"], p["item"]) for p in chain["production"]
                     if p.get("serials")) + sorted((p["frame_serials"][0], p["frame_serials"][1], p["made"],
                                                    "bench-casting") for p in chain["production"]
                                                   if p.get("frame_serials"))
    serials.sort()
    for (a0, a1, ad, _), (b0, b1, bd, _) in zip(serials, serials[1:]):
        if b0 <= a1:
            out.append(f"goods chain: serials {a0}-{a1} and {b0}-{b1} overlap")
        if bd < ad:
            out.append(f"goods chain: serials {b0}-{b1} (cast {bd}) are higher than {a0}-{a1} (cast {ad}): serials "
                       "rise with the day of casting (D21)")

    melts, coats = {}, {}
    for p in chain["production"]:     # one melt per casting day, one coating batch per lot (worklist C70)
        if p.get("melt"):
            if melts.setdefault(p["made"], p["melt"]) != p["melt"]:
                out.append(f"goods chain: two melts on {p['made']}; a casting day has one melt (C70)")
        if p.get("coating"):
            if coats.setdefault(p["coating"], p["lot"]) != p["lot"]:
                out.append(f"goods chain: coating batch {p['coating']} on two lots (C70)")
    if len(set(melts.values())) != len(melts):
        out.append("goods chain: one melt number on two casting days (C70)")
    for a_, b_ in zip(sorted(melts.items()), sorted(melts.items())[1:]):
        if b_[1] <= a_[1]:
            out.append(f"goods chain: melt {b_[1]} of {b_[0]} does not follow {a_[1]} of {a_[0]} (C70)")

    def unit(ln):
        return ln.get("lot") or (tuple(ln["serials"]) if ln.get("serials") else None)

    def key(ln):
        """A ledger line's stock: its item, lot or serials, and whether it is damaged stock, which is held apart
        and is not for sale (O174): a sale or despatch takes only sound stock."""
        return (ln["item"], unit(ln), bool(ln.get("damaged")))

    def count(ln):
        return ln["qty"] if "qty" in ln else ln["serials"][1] - ln["serials"][0] + 1
    for pid, led in chain["ledgers"].items():
        stock = {}
        for o in led.get("opening", []):
            stock[key(o)] = stock.get(key(o), 0) + o["qty"]
        last = ""
        for e in led["entries"]:
            where = f"goods chain, ledger of {pid}, {e['date']} ({e['flow']})"
            if e["date"] < last:
                out.append(f"{where}: entries out of date order")
            last = e["date"]
            for ln in e.get("in", []):
                k = key(ln)
                p = made.get(k[:2]) if k[1] else None
                if p and not any(d <= e["date"] for _, d in p["shipped"]):
                    out.append(f"{where}: {k[1]} arrives before Valdara shipped it")
                if k[2] and not ln.get("lot") and not ln.get("serials"):
                    out.append(f"{where}: damaged stock of {ln['item']} needs its lot or serials (O174)")
                stock[k] = stock.get(k, 0) + count(ln)
            for ln in e.get("out", []):
                k = key(ln)
                same = [kk for kk in stock if kk[0] == ln["item"] and kk[2] == k[2]]     # sound and damaged apart
                have = stock.get(k, 0) if k[1] else sum(stock[kk] for kk in same)
                if have < count(ln):
                    out.append(f"{where}: {count(ln)} of {ln['item']} {k[1] or ''}{' (damaged)' if k[2] else ''} "
                               f"leave, but only {have} are in {'damaged ' if k[2] else 'sound '}stock (D21, O65, "
                               "O174)")
                if k[1]:
                    stock[k] = have - count(ln)
                else:          # an issue without a lot: from the oldest stock of the item
                    left = count(ln)
                    for kk in same:
                        take = min(left, stock[kk])
                        stock[kk] -= take
                        left -= take
            for ln in e.get("crossdock", []):
                k = (ln["item"], unit(ln))
                if k not in made or not any(d <= e["date"] for _, d in made[k]["shipped"]):
                    out.append(f"{where}: {k[1]} passes through before it was shipped")
        for k, v in stock.items():
            if v < 0:
                out.append(f"goods chain, ledger of {pid}: {k} below zero")
        if led.get("closing"):          # the stock the story states at the end of the ledger (O174)
            for c in led["closing"]:
                sound = sum(v for (i, _, d), v in stock.items() if i == c["item"] and not d)
                damaged = sum(v for (i, _, d), v in stock.items() if i == c["item"] and d)
                if (sound, damaged) != (c["qty"] - c.get("damaged", 0), c.get("damaged", 0)):
                    out.append(f"goods chain, ledger of {pid}: ends with {sound + damaged} of {c['item']}, "
                               f"{damaged} damaged; the closing stock says {c['qty']}, {c.get('damaged', 0)} "
                               "damaged")
    return out


def emission_problems(items):
    """An item's footprint (D10, worklist C09): stated stage by stage, each stage once, with no system boundary in
    FullnessIndicationCode; where a figure gives a factor and a base, the value is their product."""
    from decimal import Decimal
    out = []
    for iid, it in items.items():
        if it.get("emission"):
            out.append(f"item {iid}: a footprint is a list of emissions by stage (emissions), not one figure (D10)")
        stages = [em.get("stage") for em in it.get("emissions", [])]
        if len(set(stages)) != len(stages) or None in stages:
            out.append(f"item {iid}: each emission states its own life cycle stage, once (D10)")
        for em in it.get("emissions", []):
            if em.get("method", {}).get("fullness"):
                out.append(f"item {iid}: FullnessIndicationCode is about transport equipment, not a footprint (D10)")
            if ("factor" in em) != ("base" in em):
                out.append(f"item {iid}: an emission factor needs its base, and a base its factor (C09)")
            elif "factor" in em and Decimal(em["factor"]) * Decimal(em["base"][0]) != Decimal(em["value"]):
                out.append(f"item {iid}: emission {em['value']} is not factor {em['factor']} x base {em['base'][0]} "
                           "(C09)")
    return out


# the world's rule for manual handling (D20): ISO 11228-1, 25 kg for one person, about two thirds of the combined
# capacity (about 33 kg) for two people lifting together
HANDLING_LIMIT_KG = {1: 25, 2: 33}


def physics_problems(items):
    """Item physics where the world states it (D20, the first part of O62): the parts of an item sum to its net
    weight, its parcels to its gross weight, every parcel is within the handling limit for the people who lift it,
    and an item sold as a spare part ships in the same parcel as in the whole."""
    from decimal import Decimal
    out = []
    for iid, it in items.items():
        where = f"item {iid}"
        if it.get("parts"):
            net = sum(Decimal(str(p["n"])) * Decimal(str(p["kg"])) for p in it["parts"])
            if abs(net - Decimal(str(it["net_kg"]))) > Decimal("0.1"):   # each part rounded to its own digits
                out.append(f"{where}: its parts weigh {net} kg, but its net weight is {it['net_kg']} kg")
        if it.get("parcels"):
            gross = sum(Decimal(str(p["gross_kg"])) for p in it["parcels"])
            if gross != Decimal(str(it["gross_kg"])):
                out.append(f"{where}: its parcels weigh {gross} kg, but its gross weight is {it['gross_kg']} kg")
            for p in it["parcels"]:
                if Decimal(str(p["gross_kg"])) > HANDLING_LIMIT_KG[p["lift"]]:
                    out.append(f"{where}: parcel {p['no']} weighs {p['gross_kg']} kg, above the handling limit "
                               f"for {p['lift']} person(s) (D20)")
        if it.get("carton"):
            whole = [w for w in items.values() if any(c.get("item") == iid for c in w.get("spare_parts", []))]
            for w in whole:
                if not any(Decimal(str(p["gross_kg"])) == Decimal(str(it["gross_kg"])) and p["mm"] == it["carton"]["mm"]
                           for p in w.get("parcels", [])):
                    out.append(f"{where}: a spare part ships in a parcel the whole item {w['id']} does not have")
            if Decimal(str(it["gross_kg"])) > HANDLING_LIMIT_KG[1]:
                out.append(f"{where}: one carton of {it['gross_kg']} kg is above the one-person handling limit")
    return out


# ---------------------------------------------------------------- prices along the chain (D14, O28, O30)
def price_types():
    """The world's price type list, with whether each type includes tax (lists.json PriceType, O28)."""
    lst = json.load(open(os.path.join(world_data.ROOT, "world", "codelists", "lists.json"),
                         encoding="utf-8"))["lists"]["PriceType"]
    return lst["tax_included"]


CARRIAGE_PAID = {"CPT", "CIP", "CFR", "CIF", "DAP", "DPU", "DDP"}   # Incoterms 2020: the seller pays the main carriage


def variants_of_one_model(a, b):
    """Two variants of one model (the bench in Ferro grey and in moss green, D28 point 8) share the maker's item
    number; the variant is told apart by its extended ID (ExtendedID, as Lumeway's LD-10442 is for any colour)."""
    va, vb = a.get("variant", {}), b.get("variant", {})
    return (a.get("sellers_id") == b.get("sellers_id") and va.get("extended") and vb.get("extended")
            and va.get("extended") != vb.get("extended") and va.get("what") == vb.get("what"))


def buyer_price_problems(world):
    """A price agreed for one buyer (buyer_prices: Valdara's distributor price for Lumeway, D14) is in the seller's
    currency, names a price type of the world's list that is before tax, as every item price is (O28), and is
    below the seller's own price, unless it includes the carriage to the buyer (delivered: an Incoterms rule under
    which the seller pays the main carriage, such as Lumeway's CIF price for the island, O30)."""
    problems = []
    parties = {p["id"]: p for p in world["parties"]}
    types = price_types()
    for it in world["items"]:
        for buyer, bp in it.get("buyer_prices", {}).items():
            where = f"item {it['id']}: price for {buyer}"
            if buyer not in parties or buyer == it["seller"]:
                problems.append(f"{where}: not a buyer of the world other than the seller")
            own = Decimal(str(it["price"]["amount"]))
            if bp["currency"] != it["price"]["currency"]:
                if not bp.get("contract_currency"):
                    problems.append(f"{where}: in {bp['currency']}, not in the seller's currency "
                                    f"{it['price']['currency']} (only a contract price awarded in the buyer's "
                                    "currency may be, with contract_currency, D28 point 10)")
                else:          # compared with the seller's own price at the world's reference rate
                    r = world["exchange_rates"]
                    a, b = it["price"]["currency"], bp["currency"]
                    own *= Decimal(str(r[f"{a}/{b}"])) if f"{a}/{b}" in r else 1 / Decimal(str(r[f"{b}/{a}"]))
            if bp.get("type") not in types:
                problems.append(f"{where}: price type {bp.get('type')!r} is not a code of the world's price type list")
            elif types[bp["type"]]:
                problems.append(f"{where}: price type {bp['type']} includes tax, but item prices are before tax (O28)")
            if bp.get("delivered") and bp["delivered"] not in CARRIAGE_PAID:
                problems.append(f"{where}: delivered {bp['delivered']!r} is not an Incoterms rule under which the "
                                f"seller pays the main carriage ({', '.join(sorted(CARRIAGE_PAID))})")
            above = Decimal(str(bp["amount"])) > own if bp.get("contract_currency") else Decimal(str(bp["amount"])) >= own
            if not 0 < bp["amount"] or (above and not bp.get("delivered")):    # a contract price may equal the list
                problems.append(f"{where}: {bp['amount']} is not below the seller's own price {it['price']['amount']}")
            if not bp.get("why"):
                problems.append(f"{where}: needs the reason for the price (why)")
    return problems


def _lume(world, amount, currency):
    from decimal import Decimal
    if currency == "XBL":
        return Decimal(str(amount))
    rates = world["exchange_rates"]
    if f"{currency}/XBL" in rates:
        return Decimal(str(amount)) * Decimal(str(rates[f"{currency}/XBL"]))
    return Decimal(str(amount)) / Decimal(str(rates[f"XBL/{currency}"]))


def maker_item(items, iid):
    """The maker's item a resold item goes back to."""
    while items[iid].get("resale_of"):
        iid = items[iid]["resale_of"]
    return iid


def gross_kg(items, iid):
    """An item's gross weight, its maker's where a resold item gives none."""
    it = items[iid]
    while "gross_kg" not in it and it.get("resale_of"):
        it = items[it["resale_of"]]
    return it.get("gross_kg")


def insurance_premium(price, base):
    """The premium of a cargo insurance at a rate on the insured value (O173): price is the item's rate price
    (rate_percent, cover_percent), base the value insured without the premium (the goods and the freight, in the
    CIF value). The insured value is cover_percent of the base plus the premium itself, so the premium is the fixed
    point p = round(rate × cover × (base + p)), to the cent. Returns (premium, insured value)."""
    from decimal import Decimal, ROUND_HALF_UP
    cent = Decimal("0.01")
    r = Decimal(str(price["rate_percent"])) / 100
    c = Decimal(str(price["cover_percent"])) / 100
    base = Decimal(str(base))
    p = (r * c * base / (1 - r * c)).quantize(cent, ROUND_HALF_UP)
    for cand in (p, p - cent, p + cent):
        if (r * c * (base + cand)).quantize(cent, ROUND_HALF_UP) == cand:
            return cand, (c * (base + cand)).quantize(cent, ROUND_HALF_UP)
    raise SystemExit(f"insurance premium: no premium to the cent on a base of {base}")


def insured_base(world, items, fr):
    """The value a freight's cargo insurance covers, without the premium (O173): the load at the insured buyer's
    prices and the freight services named, in lume."""
    from decimal import Decimal
    ins = fr["insured"]
    out = Decimal(0)
    for l in fr["load"]:
        pr = items[l["item"]].get("buyer_prices", {}).get(ins["buyer"]) or items[l["item"]]["price"]
        out += _lume(world, Decimal(str(pr["amount"])) * Decimal(str(l["qty"])), pr["currency"])
    for sv in fr["services"]:
        if sv["item"] in ins["with"]:
            pr = items[sv["item"]]["price"]
            out += _lume(world, Decimal(str(pr["amount"])) * Decimal(str(sv["qty"])), pr["currency"])
    return out


def freight_costs(world, items):
    """Each stated freight of resales.freight in lume per unit of each item it carries: the services' prices times
    their quantities (the kilometres of the transport leg on the map, as the carrier invoices them, or the
    chargeable weight of the load), shared over the load by gross weight. {name: {item: lume per unit}}."""
    from decimal import Decimal
    out = {}
    for name, fr in world["resales"]["freight"].items():
        load_kg = sum(Decimal(str(l["qty"])) * Decimal(str(gross_kg(items, l["item"]))) for l in fr["load"])
        total = Decimal(0)
        for sv in fr["services"]:
            if "km_of_leg" in sv:
                import world_map
                q = Decimal(world_map.whole(world_map.leg_km(*sv["km_of_leg"])))
            elif sv["qty"] == "load_kg":
                q = load_kg
            else:
                q = Decimal(str(sv["qty"]))
            pr = items[sv["item"]]["price"]
            if "rate_percent" in pr:     # a premium on the insured value of the load (O173)
                if not fr.get("insured"):
                    raise SystemExit(f"items.json resales.freight.{name}: {sv['item']} is priced at a rate, but the "
                                     "freight states no insured value (insured)")
                total += _lume(world, insurance_premium(pr, insured_base(world, items, fr))[0] * q, pr["currency"])
                continue
            total += _lume(world, Decimal(str(pr["amount"])) * q, pr["currency"])
        out[name] = {l["item"]: total * Decimal(str(gross_kg(items, l["item"]))) / load_kg for l in fr["load"]}
    return out


def sale_price(it, s):
    """The price per unit a resale s is made at: the price agreed for the sale's buyer (buyer_prices), where it
    holds for the sale's delivery terms (a price with the carriage in it, delivered, holds only for those terms),
    else the item's own price."""
    bp = it.get("buyer_prices", {}).get(s.get("buyer"))
    if bp and (not bp.get("delivered") or bp["delivered"] == s.get("terms")):
        return bp
    return it["price"]


def resale_figures(world):
    """Each resale of items.json resales with its price, its cost and its gross margin, in lume per sale:
    [(sale, price, cost, margin percent, how the cost is made)]. The price is the buyer's own price for the item
    (buyer_prices), where one holds for the sale's delivery terms, else the reseller's price; freight the buyer pays
    on top at cost (recharged) is left out of the cost, as it is out of the price."""
    from decimal import Decimal
    items = {i["id"]: i for i in world["items"]}
    parties = {p["id"]: p for p in world["parties"]}
    freight = freight_costs(world, items)
    sales = {s["id"]: s for s in world["resales"]["sales"]}
    out = {}
    for s in world["resales"]["sales"]:
        seller_cur = world["countries"][parties[s["seller"]]["c"]]["currency"]["code"]
        listed = sum(Decimal(str(sale_price(items[i], s)["amount"])) * q for i, q in s["items"])
        p = Decimal(str(s.get("price", listed))) * (1 - Decimal(str(s.get("less_percent", 0))) / 100)
        price = _lume(world, p, seller_cur)
        parts, cost = [], Decimal(0)
        for iid, q in s["items"]:
            orig = items[iid]["resale_of"]
            if s.get("bought_from"):        # what the reseller paid: the price its own purchase was made at
                paid = out[s["bought_from"]][1] / sum(qq for _, qq in sales[s["bought_from"]]["items"])
            else:
                pr = items[orig].get("buyer_prices", {}).get(s["seller"]) or items[orig]["price"]
                paid = _lume(world, pr["amount"], pr["currency"])
            cost += paid * q
            parts.append(f"{q} × {paid:.2f} paid for {orig}")
            for name in s.get("freight", []) + s.get("recharged", []):
                # the share of the goods carried that are the same goods
                f = freight[name][next(l["item"] for l in world["resales"]["freight"][name]["load"]
                                       if maker_item(items, l["item"]) == maker_item(items, iid))]
                if name in s.get("recharged", []):      # paid by the buyer on top, at cost: a pass-through
                    parts.append(f"{f:.2f} {name} recharged to the buyer")
                    continue
                cost += f * q
                parts.append(f"{f:.2f} {name}")
            if s.get("import_tax"):
                scheme = next(x for x in world["countries"][parties[s["seller"]]["c"]]["tax"]["schemes"]
                              if x["id"] == s["import_tax"])
                tax = paid * Decimal(str(scheme["rate"])) / 100
                cost += tax * q
                parts.append(f"{tax:.2f} {scheme['name'].lower()}")
        out[s["id"]] = (s, price, cost, (price - cost) / price * 100, " + ".join(parts))
    return out


def resale_problems(world):
    """D14's rules of thumb for every resale (O30): nobody resells below what they paid plus the freight the
    documents state (and the import tax they bear), and the gross margin falls in the band for the reseller's kind
    of business, a promotion only below its upper limit; every resold item is in a resale; a sale awaiting the
    owner still fails."""
    rs = world.get("resales")
    if not rs:
        return ["items.json: no resales for the margin check (D14, O30)"]
    parties = {p["id"]: p for p in world["parties"]}
    problems, failing = [], set()
    for sid, (s, price, cost, margin, how) in resale_figures(world).items():
        where = f"resale {sid} ({s['what']})"
        kind = parties[s["seller"]]["identity"].get("legal", {}).get("business")
        kind = s.get("band", kind)                 # a band for the kind of goods (clothing), else the business's
        band = rs["margin_bands"].get(kind)
        found = []
        if price < cost:
            found.append(f"sold at {price:.2f} lume, below its cost of {cost:.2f} ({how}) (D14, O30)")
        if not band:
            found.append(f"no margin band {kind!r} for the seller's business or the sale's kind of goods")
        elif (margin < band["min"] and not s.get("promotion")) or margin > band["max"]:
            found.append(f"gross margin {margin:.1f} % (price {price:.2f}, cost {cost:.2f} lume: {how}) is outside the "
                         f"band of {band['min']} to {band['max']} % for a {band['name'].lower()}"
                         + (" (in a promotion, only the upper limit)" if s.get("promotion") else "") + " (D14, O30)")
        if found:
            failing.add(sid)
            if sid not in rs.get("awaiting_owner", {}):
                problems += [f"{where}: {x}" for x in found]
    for sid in rs.get("awaiting_owner", {}):
        if sid not in failing:
            problems.append(f"resale {sid}: listed as awaiting the owner in resales, but it passes: take it off the list")
    sold = {i for s in rs["sales"] for i, _ in s["items"]}
    for it in world["items"]:
        if it.get("resale_of") and not it.get("free_with") and it["id"] not in sold \
                and not any(it.get("variant") and o.get("variant") and o["id"] in sold and o["sellers_id"] == it["sellers_id"]
                            and o["seller"] == it["seller"] for o in world["items"]):
            problems.append(f"item {it['id']}: resold, but in no resale of items.json resales (D14, O30)")
    return problems


if __name__ == "__main__":
    w = world_data.load()
    probs = check(w)
    for n in NOTES:
        print(f"note: {n}")
    print("\n".join(probs) or f"items: {len(w['items'])} items of {len({i['seller'] for i in w['items']})} sellers, no problems"
          + (f" ({len(NOTES)} notes)" if NOTES else ""))
    sys.exit(1 if probs else 0)
