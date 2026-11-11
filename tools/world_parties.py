#!/usr/bin/env python3
"""The identity of the parties of the UBL example world, and its checks.

Every party in world/parties.json has an identity: a name, the identifiers of
its country's schemes (company register, tax number), a postal address that
matches its place on the map, an electronic address, a contact and, where it
is paid, an account at a bank of the world.

UBL forbids empty elements (rule IND5): any party element in a document must
hold at least one of its parts. The identity makes sure there is always
something to put in it, and these checks keep it consistent:

  * every party has a name; every organisation an identifier;
  * tax numbers and account numbers carry valid check digits;
  * the city is the nearest town or locality in the party's own country
    and state, and in a country with states the state (name and code)
    follows the country's rule, and so does the state code a sales tax
    permit starts with;
  * every account is held at a bank of the world in the same country;
  * e-mail addresses and websites use the reserved .example domain (RFC
    2606), and telephone numbers the country code +999 that the ITU keeps in
    reserve, so none can reach a real organisation;
  * industry codes are ISIC Rev. 4 classes, and parties referred to exist;
  * the ISIN of a listed security has the structure and check digit of
    ISO 6166 (Luhn over the digits with each letter expanded to 10..35).

Usage: python3 tools/world_parties.py      (prints the problems, exit 1 if any)
"""
import math
import re
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402


def mod11(digits):
    """Check digit for the XU tax number: weights 9..2 over 8 digits, modulus 11 (10 is not allowed)."""
    s = sum(int(d) * w for d, w in zip(digits, range(9, 1, -1))) % 11
    return None if s == 10 else str(s)


def account_check(country, bank, number):
    """Two check digits in the structure of ISO 13616 (mod 97), with the world's country codes."""
    raw = f"{bank}{number}{country}00"
    n = int("".join(str(int(ch, 36)) for ch in raw))
    return f"{98 - n % 97:02d}"


def account_of_branch(bank, acc):
    """The national account number holds the bank and branch codes, in its country's way (decision ID-Q9): in
    Bayvarra the bank code and the sort code, in Urvania the ABI and CAB codes, on the island the bank code and the
    branch number. The branch is one of the bank's."""
    idn, n = bank["identity"], acc["number"]
    branch = next((b for b in idn.get("branches", []) if b["id"] == acc.get("branch")), None)
    if not branch or n[:2] != bank["c"]:
        return False
    if bank["c"] == "XU":
        return n[4:14] == branch["id"].replace("-", "") and branch["id"].startswith(idn["abi"])
    return n[4:8] == idn["bank_code"] and n[8:8 + len(branch["id"])] == branch["id"]


def account_valid(acc):
    country, check, rest = acc[:2], acc[2:4], acc[4:]
    return account_check(country, rest[:4], rest[4:]) == check


def isin_valid(isin):
    """ISO 6166: two letters, nine alphanumerics and a check digit; the Luhn sum over the string with
    each letter written as its number (A=10 .. Z=35) is a multiple of 10."""
    if not re.fullmatch(r"[A-Z]{2}[0-9A-Z]{9}[0-9]", isin or ""):
        return False
    digits = "".join(str(int(ch, 36)) for ch in isin)
    total = 0
    for i, ch in enumerate(reversed(digits)):
        n = int(ch) * (2 if i % 2 else 1)
        total += n - 9 if n > 9 else n
    return total % 10 == 0


def tax_id_valid(country, tax_id, state_code=None):
    """state_code: in Bayvarra, the code of the party's state or territory, which the sales tax permit starts with."""
    if country == "XU":
        return len(tax_id) == 11 and tax_id[:2] == "XU" and tax_id[2:].isdigit() and mod11(tax_id[2:10]) == tax_id[10]
    if country == "XB":
        st, _, num = tax_id.partition("-")
        return st == state_code and len(num) == 7 and num.isdigit()
    return False


def nearest_town(world, p):
    """The nearest town or locality in the party's own country and, where there are states, its own state."""
    places = [t for t in world["towns"] + world.get("localities", [])
              if t["country"] == p["c"] and state_of(world, {"c": t["country"], "at": t["c"]}) == state_of(world, p)]
    return min(places, key=lambda t: math.dist(t["c"], p["at"]))["name"] if places else None


def state_of(world, p):
    """The state (or territory) a place is in, by its country's rule: in Bayvarra the Northern Territory north
    of a map row, and south of it a state border along a map column."""
    rule = world["countries"][p["c"]].get("subdivision_rule")
    if not rule:
        return None
    if "north_of_row" in rule and p["at"][1] < rule["north_of_row"]:
        return rule["north"]
    return rule["west"] if p["at"][0] < rule["column"] else rule["east"]


def state_code(world, p):
    st = state_of(world, p)
    subs = world["countries"][p["c"]]["address"].get("subdivisions") or {}
    return next((k for k, v in subs.items() if v == st), None)


def check(world):
    problems = []
    parties = {p["id"]: p for p in world["parties"]}
    seen_names, seen_endpoints = {}, {}
    for p in world["parties"]:
        where = f"party {p['id']}"
        idn = p.get("identity")
        if not idn:
            problems.append(f"{where}: no identity")
            continue
        if not idn.get("name"):
            problems.append(f"{where}: no name (IND5: a party element needs content)")
        if idn["name"] in seen_names:
            problems.append(f"{where}: same name as {seen_names[idn['name']]}")
        seen_names[idn["name"]] = p["id"]
        person = idn.get("person", False)
        if not person and not idn.get("registry_id"):
            problems.append(f"{where}: an organisation needs a registry identifier")
        state = (state_code(world, p) or "").split("-")[-1] or None     # XB-CO: the permit starts with CO
        if idn.get("tax_id") and not tax_id_valid(p["c"], idn["tax_id"], state):
            problems.append(f"{where}: tax number {idn['tax_id']} is not valid for {p['c']}"
                            + (f" (the permit of {state_of(world, p)} starts with {state})" if state_of(world, p) else ""))
        a = idn.get("address", {})
        town = nearest_town(world, p)
        if a.get("CityName") != town:
            problems.append(f"{where}: city {a.get('CityName')} but the nearest town of its country is {town}")
        st = state_of(world, p)
        if st and a.get("CountrySubentity") != st:
            problems.append(f"{where}: state {a.get('CountrySubentity')} but its place is in {st}")
        if st and a.get("CountrySubentityCode") != state_code(world, p):
            problems.append(f"{where}: state code {a.get('CountrySubentityCode')} but {st} has the code {state_code(world, p)}")
        le = idn.get("legal", {})
        if le and not person and not le.get("sole_proprietor") and p["c"] and \
                (not isinstance(le.get("headcount"), int) or not le.get("turnover")):
            problems.append(f"{where}: a company needs its headcount and turnover, from which its size class follows")
        if le.get("turnover"):
            t = le["turnover"]
            cur = world["countries"][p["c"]]["currency"]
            if t["currency"] != cur["code"] or len(t["amount"].partition(".")[2]) != cur["minor_units"]:
                problems.append(f"{where}: turnover {t['amount']} {t['currency']} is not in {cur['code']} with its "
                                f"{cur['minor_units']} decimals")
        if not st and a.get("CountrySubentity"):
            problems.append(f"{where}: its country has no states")
        for k in ("StreetName", "BuildingNumber"):
            if not a.get(k) and not (k == "BuildingNumber" and a.get("Description")):   # a farm has no house number
                problems.append(f"{where}: address without {k}")
        mail = idn.get("contact", {}).get("email", "")
        if mail and not mail.endswith(".example"):
            problems.append(f"{where}: e-mail {mail} must use the reserved .example domain")
        ep = idn.get("endpoint")
        if ep:
            if ep in seen_endpoints:
                problems.append(f"{where}: same electronic address as {seen_endpoints[ep]}")
            seen_endpoints[ep] = p["id"]
        if idn.get("website") and not idn["website"].split("/")[2].endswith(".example"):
            problems.append(f"{where}: website {idn['website']} must use the reserved .example domain")
        plan = world["countries"][p["c"]].get("phone_plan")
        for kind in ("telephone", "telefax", "mobile"):
            number = idn.get("contact", {}).get(kind)
            if number and plan and not re.match(plan["pattern"], number):
                problems.append(f"{where}: {kind} {number} does not follow {world['countries'][p['c']]['name']}'s "
                                f"numbering plan (world/countries.json): {plan['note']}")
        phone = idn.get("contact", {}).get("telephone")
        if phone and not phone.startswith(world["countries"][p["c"]]["phone_prefix"]):
            problems.append(f"{where}: telephone {phone} must start with {world['countries'][p['c']]['phone_prefix']} "
                            "(+999 is reserved by the ITU, so the number reaches no one)")
        if idn.get("industry") and not (len(idn["industry"]) == 4 and idn["industry"].isdigit()):
            problems.append(f"{where}: industry code {idn['industry']} is not an ISIC Rev. 4 class (4 digits)")
        for rel, key in ((idn.get("service_provider"), "party"), (idn.get("legal", {}).get("shareholder"), "party")):
            if rel and rel[key] not in parties:
                problems.append(f"{where}: refers to unknown party {rel[key]}")
        listing = idn.get("legal", {}).get("listing")
        if listing and not isin_valid(listing.get("id")):
            problems.append(f"{where}: ISIN {listing.get('id')} fails ISO 6166 (structure or check digit)")
        if listing and listing.get("id", "")[:2] != p["c"]:
            problems.append(f"{where}: ISIN {listing.get('id')} must start with the issuer's country code {p['c']}")
        acc = idn.get("account")
        if acc:
            bank = parties.get(acc["bank"])
            if not bank or bank.get("cat") != "finance" or "bank" not in bank["identity"].get("kind", ""):
                problems.append(f"{where}: account at {acc['bank']}, which is not a bank of the world")
            elif bank["c"] != p["c"] and not acc.get("abroad"):
                problems.append(f"{where}: account at a bank in another country")
            if not account_valid(acc["number"]):
                problems.append(f"{where}: account number {acc['number']} has wrong check digits")
            elif bank and not account_of_branch(bank, acc):
                problems.append(f"{where}: account number {acc['number']} does not hold the codes of bank "
                                f"{acc['bank']} and its branch {acc.get('branch')} (decision ID-Q9)")
        problems += identifier_problems(world, p)
    return problems


FLEET_IDS = {"plate": "vehicle-register", "trailer": "vehicle-register", "aircraft": "aircraft-register",
             "call_sign": "call-sign", "mmsi": "mmsi"}


def identifier_problems(world, p):
    """The party's identifiers, and those of its fleet, follow its country's schemes (world/countries.json,
    identifiers; decisions ID-Q3 and ID-Q4), checked like the telephone numbers: the register number, the tax
    number, the customs trader number, plates, aircraft registrations, UIC wagon numbers (with the check digit),
    call signs, MMSIs and driving licences."""
    import world_ids
    out, where, ids = [], f"party {p['id']}", world["countries"][p["c"]].get("identifiers", {})
    idn = p["identity"]
    values = [("register", idn.get("registry_id")), ("tax", idn.get("tax_id")), ("customs-trader", idn.get("customs_id"))]
    for f in p.get("fleet", []):
        values += [(kind, f.get(k)) for k, kind in FLEET_IDS.items()]
        values += [("rail-vehicle-register", w) for w in f.get("wagons", []) + f.get("ore_wagons", [])]
        if f.get("driver"):
            values.append(("driving-licence", f["driver"].get("id")))
    for b in idn.get("branches", []):
        values.append(("bank-branch", b["id"]))
    if idn.get("bic"):
        bic = world["identifier_schemes"]["urn:ubl-examples:world:bank-identifier"]
        why = world_ids.problem(bic, idn["bic"])
        if why or idn["bic"][:4] != idn.get("bank_code") or idn["bic"][4:6] != p["c"]:
            out.append(f"{where}: bank identifier {idn['bic']} is not the bank's code, its country and a location "
                       f"(ISO 9362 structure){': ' + why if why else ''}")
    a = idn.get("address", {})
    if a.get("ID"):
        out += address_register_problems(world, p, a)
    for kind, value in values:
        if not value or (kind == "tax" and p["c"] == "XL"):
            continue
        if kind not in ids:
            out.append(f"{where}: {p['c']} has no {kind} scheme for {value} (world/countries.json, identifiers)")
            continue
        why = world_ids.problem(ids[kind], value)
        if why:
            out.append(f"{where}: {why}")
    return out


def address_register(world, country, a):
    """The kind of the address register an address belongs to (decision ID-Q8): Urvania's national register, the
    City of Lumeport's register for an address in the city, a Bayvarran state's register elsewhere, the island
    post office's delivery points."""
    ids = world["countries"][country].get("identifiers", {})
    for kind, spec in ids.items():
        if not kind.endswith("address-register") and kind != "delivery-point":
            continue
        if spec.get("city") and a.get("CityName") != spec["city"]:
            continue
        if spec.get("subdivision") and (a.get("CountrySubentityCode") != spec["subdivision"]
                                        or a.get("CityName") in spec.get("outside", [])):
            continue
        return kind, spec
    return None, None


def address_register_problems(world, p, a):
    """The address's number is in the register of its country, state or city, in that register's format, and in
    Urvania it starts with the code of the address's municipality."""
    import world_ids
    where = f"party {p['id']}"
    kind, spec = address_register(world, p["c"], a)
    if not spec:
        return [f"{where}: no address register for {a.get('CityName')} (world/countries.json)"]
    why = world_ids.problem(spec, a["ID"])
    if why:
        return [f"{where}: address {why}"]
    if spec.get("municipalities") and a["ID"][:4] != spec["municipalities"].get(a.get("CityName")):
        return [f"{where}: address number {a['ID']} is not from the municipality of {a.get('CityName')}"]
    return []


if __name__ == "__main__":
    w = world_data.load()
    probs = check(w)
    print("\n".join(probs) or f"party identities: {len(w['parties'])} parties, no problems")
    sys.exit(1 if probs else 0)
