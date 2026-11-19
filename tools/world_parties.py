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
  * the city is the nearest named place of the map (town, locality or named
    village) in the party's own country and state; its postal code is one of
    that place's, a quarter is one of its town's districts on the map, and in
    a country with states the state (name and code)
    follows the country's rule, and so does the state code a sales tax
    permit starts with;
  * every account is held at a bank of the world in the same country;
  * e-mail addresses and websites use the reserved .example domain (RFC
    2606), and telephone numbers the country code +999 that the ITU keeps in
    reserve, so none can reach a real organisation;
  * industry codes are ISIC Rev. 4 classes, and parties referred to exist;
  * a public body has no company figures; a company was entered in the
    register on a working day that is no holiday of its country, and its
    turnover per person falls in the band for its kind of business
    (parties.json turnover_per_person; decisions D14, D46, open point O30);
  * the ISIN of a listed security has the structure and check digit of
    ISO 6166 (Luhn over the digits with each letter expanded to 10..35);
  * identification (D5, open points O22 and O32): a party identifies itself
    and its items in one convention, GS1, ISO (Codana) or its own numbers; a
    Codana company number has five digits, is held by one party, and Codana
    gives the numbers in order of registration since it began (the party
    registered after its founding, and a later registration has a higher
    number); a GS1 company prefix is 952 and four digits, held by one party,
    and its GLNs are under it; every Codana identifier of the party starts
    with its own company number (the items' KXU numbers in world_items.py);
  * every register issues its own numbers (D5, O22): no identifier of a party
    repeats a run of five digits of another of its identifiers, apart from
    the stated reuse of the business register number in the electronic
    address and the customs trader number and the keys one numbering system
    builds from its own company number or prefix; no telephone number repeats
    a run of four digits of an identifier of its party, and no two parties
    share a telephone number.

Usage: python3 tools/world_parties.py      (prints the problems, exit 1 if any)
"""
import math
import re
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402


# the functions a party's desk can have (world/parties.json identity.desks; tools/build_examples.py desk_for)
DESK_FUNCTIONS = {"sales", "purchasing", "receivables", "payables", "goods_in", "despatch", "logistics", "customs",
                  "tenders", "operations", "procurement", "customs_export", "customs_import", "customs_transit",
                  "carnet", "certificates"}


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


def named_places(world):
    """The places an address can name: every town, locality and named village of the map."""
    return world["towns"] + world.get("localities", []) + [v for v in world.get("villages", []) if v.get("names")]


def own_places(world, p):
    return [t for t in named_places(world)
            if t["country"] == p["c"] and state_of(world, {"c": t["country"], "at": t["c"]}) == state_of(world, p)]


def nearest_town(world, p):
    """The nearest named place (town, locality or named village of the map) in the party's own country and, where
    there are states, its own state: the place of its address (O152 stage 2 B, as the place list measures it)."""
    places = own_places(world, p)
    return min(places, key=lambda t: math.dist(t["c"], p["at"]))["name"] if places else None


def city_fits(world, p, city):
    """The address's place is the nearest named place, or no more than a square (3.5 km) farther than it, as the
    place list (tools/place_list.py) allows: the map is a diagram inside the towns (O82)."""
    places = {t["name"]: t for t in own_places(world, p)}
    if city not in places:
        return False
    d = lambda t: math.dist(t["c"], p["at"])
    return d(places[city]) <= min(map(d, places.values())) + 1


def postal_problems(world, p, a):
    """The postal code is one of its place's (world/countries.json, address "postal_codes")."""
    import re
    codes = world["countries"][p["c"]]["address"].get("postal_codes")
    if not codes:
        return []
    pat = codes.get(a.get("CityName"))
    if not pat:
        return [f"party {p['id']}: no postal codes for {a.get('CityName')} (world/countries.json)"]
    if not re.fullmatch(pat, a.get("PostalZone") or ""):
        return [f"party {p['id']}: postal code {a.get('PostalZone')} is not one of {a.get('CityName')}'s ({pat})"]
    return []


def quarter_problems(world, p, a):
    """A quarter named in an address is a district of its town on the map (world/map.json, "districts")."""
    q = a.get("CitySubdivisionName")
    if not q:
        return []
    town = next((t for t in world["towns"] if t["name"] == a.get("CityName")), None)
    names = [d["name"] for d in (town or {}).get("districts", [])]
    return [] if q in names else [f"party {p['id']}: quarter {q} is not a district of {a.get('CityName')} on the map"]


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
        if not city_fits(world, p, a.get("CityName")):
            problems.append(f"{where}: city {a.get('CityName')} but the nearest town of its country is {town}")
        problems += postal_problems(world, p, a) + quarter_problems(world, p, a)
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
        problems += figure_problems(world, p)
        prov = world["countries"][p["c"]].get("province") if p["c"] else None
        if not st and a.get("CountrySubentity") and a.get("CountrySubentity") != prov:
            problems.append(f"{where}: its country has no states" + (f"; its province is {prov}" if prov else ""))
        if a.get("Region"):
            problems.append(f"{where}: Region is an informal area, not a country subdivision; a province or state "
                            "goes in CountrySubentity (worklist C03)")
        for k in ("StreetName", "BuildingNumber"):
            if not a.get(k) and not (k == "BuildingNumber" and a.get("Description")):   # a farm has no house number
                problems.append(f"{where}: address without {k}")
        mail = idn.get("contact", {}).get("email", "")
        if mail and not mail.endswith(".example"):
            problems.append(f"{where}: e-mail {mail} must use the reserved .example domain")
        for fn, dk in idn.get("desks", {}).items():
            if fn not in DESK_FUNCTIONS:
                problems.append(f"{where}: desk {fn} is not one of the desk functions ({', '.join(sorted(DESK_FUNCTIONS))})")
            if not all(dk.get(k) for k in ("name", "job_title", "department", "email")):
                problems.append(f"{where}: desk {fn} needs a name, job title, department and e-mail")
            if not dk.get("email", "").endswith(".example"):
                problems.append(f"{where}: desk {fn} e-mail {dk.get('email')} must use the reserved .example domain")
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
    problems += identification_problems(world) + repeat_problems(world)
    return problems


REPEAT_IDENTIFIER, REPEAT_TELEPHONE = 5, 4   # the shortest digit run that counts as a repeat (D5, O22)


def identification_problems(world):
    """Each party's identification convention (D5, O22, O32): Codana company numbers in order of registration,
    GS1 company prefixes with their GLNs, each number held by one party."""
    import world_ids
    out, cins, prefixes = [], {}, {}
    since = world["identifier_schemes"]["ISO 6523"]["issued_since"]
    for p in world["parties"]:
        where, idn = f"party {p['id']}", p.get("identity", {})
        conv = idn.get("identification")
        if not conv:
            continue
        kind = conv.get("convention")
        if kind not in ("GS1", "ISO", "own"):
            out.append(f"{where}: identification convention {kind} is not GS1, ISO or own")
        if kind == "ISO":
            cin, reg = conv.get("codana_cin", ""), conv.get("codana_registered", "")
            if not re.fullmatch(r"\d{5}", cin):
                out.append(f"{where}: Codana company number {cin!r} is not five digits")
                continue
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", reg) or int(reg[:4]) < since:
                out.append(f"{where}: Codana registration {reg!r} is not a date from {since}, when Codana began")
            founded = idn.get("legal", {}).get("founded")
            if founded and reg < founded:
                out.append(f"{where}: registered with Codana on {reg}, before it was founded on {founded}")
            if cin in cins:
                out.append(f"{where}: Codana company number {cin} is also {cins[cin][0]}'s")
            cins[cin] = (p["id"], reg)
        if kind == "GS1":
            pre = conv.get("company_prefix", "")
            if not re.fullmatch(r"952\d{4}", pre):
                out.append(f"{where}: GS1 company prefix {pre!r} is not 952 and four digits (952 is GS1's prefix "
                           "for examples)")
            if pre in prefixes:
                out.append(f"{where}: GS1 company prefix {pre} is also {prefixes[pre]}'s")
            prefixes[pre] = p["id"]
            glns = [conv.get("gln")] + [x["gln"] for x in conv.get("locations", {}).values()]
            for g in glns:
                if not (g and re.fullmatch(r"\d{13}", g) and g.startswith(pre) and world_ids.gs1(g)):
                    out.append(f"{where}: GLN {g} is not a GS1 key of 13 digits under its prefix {pre}")
    order = sorted(cins.items(), key=lambda kv: (kv[1][1], kv[0]))
    for (c1, (p1, r1)), (c2, (p2, r2)) in zip(order, order[1:]):
        if c2 <= c1:
            out.append(f"party {p2}: Codana company number {c2}, registered {r2}, is not higher than {p1}'s {c1}, "
                       f"registered {r1}: Codana gives its numbers in order of registration (O22)")
    return out


def party_identifiers(world, p):
    """The identifiers of a party, as (family, label, value): the family groups the stated reuse (the register
    number in the electronic address and the customs trader number) and the keys a numbering system builds from
    its own company number or prefix (a Codana number in the party's 0990 identifier and its KXU numbers, a GS1
    prefix in its GLNs and GTINs); between families no digits may repeat."""
    idn = p.get("identity", {})
    out = [("register", k, idn.get(k)) for k in ("registry_id", "endpoint", "customs_id")]
    out.append(("tax", "tax_id", idn.get("tax_id")))
    out.append(("isin", "listing", idn.get("legal", {}).get("listing", {}).get("id")))
    conv = idn.get("identification") or {}
    out.append(("codana", "codana_cin", conv.get("codana_cin")))
    out += [("gs1", "company_prefix", conv.get("company_prefix")), ("gs1", "gln", conv.get("gln"))]
    out += [("gs1", f"gln {k}", x["gln"]) for k, x in conv.get("locations", {}).items()]
    for it in world["items"]:
        if it["seller"] == p["id"]:
            out += [("codana", f"item {it['id']}", it.get("standard_id")), ("gs1", f"item {it['id']}", it.get("gtin"))]
    return [x for x in out if x[2]]


def subscriber(number):
    """The digits of a telephone number after the country digit and its first group (an area code, a mobile
    prefix, the island's exchange): the part a party is given."""
    return re.sub(r"\D", "", number.split(" ", 3)[3] if number.count(" ") >= 3 else "")


def repeat_problems(world):
    """No identifier of a party repeats the digits of another, and no telephone number an identifier's (D5, O22)."""
    import itertools
    import world_ids
    out, phones = [], {}
    for p in world["parties"]:
        where, ids = f"party {p['id']}", party_identifiers(world, p)
        for (f1, l1, v1), (f2, l2, v2) in itertools.combinations(ids, 2):
            run = world_ids.shared_run(v1, v2, REPEAT_IDENTIFIER)
            if f1 != f2 and run:
                out.append(f"{where}: {l1} {v1} and {l2} {v2} share the digits {run}: every register issues its "
                           "own numbers (D5)")
        for kind, number in sorted(p.get("identity", {}).get("contact", {}).items()):
            if kind not in ("telephone", "mobile", "telefax") or not number:
                continue
            if number in phones:
                out.append(f"{where}: {kind} {number} is also {phones[number]}'s")
            phones[number] = p["id"]
            for _, label, value in ids:
                run = world_ids.shared_run(subscriber(number), value, REPEAT_TELEPHONE)
                if run:
                    out.append(f"{where}: {kind} {number} repeats the digits {run} of its {label} {value}: a "
                               "telephone number has no relation to an identifier (O22)")
    return out


def in_lume(world, amount, currency):
    """An amount in lume, at the world's reference rates (world/countries.json exchange_rates)."""
    from decimal import Decimal
    if currency == "XBL":
        return Decimal(amount)
    rates = world["exchange_rates"]
    if f"{currency}/XBL" in rates:
        return Decimal(amount) * Decimal(str(rates[f"{currency}/XBL"]))
    return Decimal(amount) / Decimal(str(rates[f"XBL/{currency}"]))


def holiday_on(world, country, day):
    """The name of the country's holiday that falls on a day of any year, or None. The holidays are given with
    their dates in 2026 (world/countries.json holidays); a holiday counts on the same day of the month and,
    unless the country keeps fixed dates only, also on the same weekday of the month (the third Monday in
    February), since some of its holidays are set that way. Stricter than the calendar, never looser."""
    import datetime
    hol = world["countries"][country].get("holidays", {})
    fixed = hol.get("rule", "").startswith("Fixed dates")
    for iso, name in hol.get("2026", {}).items():
        h = datetime.date.fromisoformat(iso)
        if h.month != day.month:
            continue
        if h.day == day.day or (not fixed and h.weekday() == day.weekday()
                                and (h.day - 1) // 7 == (day.day - 1) // 7):
            return name
    return None


def figure_problems(world, p):
    """A party's founding date, headcount and turnover (worklist C60, decisions D4, D14 and D46, open points O21
    and O30): a public body has no company figures; a company is entered in the register on a working day that
    is not a holiday of its country, and its turnover per person falls in the band for its kind of business
    (parties.json turnover_per_person), unless it is listed there as awaiting the owner's decision."""
    import datetime
    problems, where = [], f"party {p['id']}"
    idn = p["identity"]
    le = idn.get("legal", {})
    if idn.get("kind") == "public":
        for k in ("founded", "headcount", "turnover", "capital", "business"):
            if k in le:
                problems.append(f"{where}: a public body has no company figures, but has {k} (D46)")
        return problems
    if le.get("founded"):
        day = datetime.date.fromisoformat(le["founded"])
        if day.weekday() >= 5:
            problems.append(f"{where}: founded on a {day:%A} ({day}), when the register is closed (O21)")
        name = holiday_on(world, p["c"], day)
        if name:
            problems.append(f"{where}: founded on {day}, on {name}, a holiday of {p['c']} (O21)")
    if not le.get("turnover") or idn.get("person") or le.get("sole_proprietor"):
        return problems                        # a farm is in the farm register, not the companies register (D46)
    rule = world["turnover_per_person"]
    band = rule["bands"].get(le.get("business"))
    if not band:
        problems.append(f"{where}: business {le.get('business')!r} is not one of the kinds of turnover_per_person "
                        f"({', '.join(rule['bands'])}) (O30)")
        return problems
    t = le["turnover"]
    per = in_lume(world, t["amount"], t["currency"]) / le["headcount"]
    inside = band["min"] <= per <= band["max"]
    if not inside and p["id"] not in rule.get("awaiting_owner", {}):
        problems.append(f"{where}: turnover per person {per:,.0f} lume ({le['headcount']} persons, {t['amount']} "
                        f"{t['currency']}) is outside the band of {band['min']:,} to {band['max']:,} for "
                        f"{band['name'].lower()} (D14, O30)")
    if inside and p["id"] in rule.get("awaiting_owner", {}):
        problems.append(f"{where}: listed as awaiting the owner in turnover_per_person, but its turnover per person "
                        f"({per:,.0f} lume) is inside its band: take it off the list")
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
    for card in [idn[k] for k in ("card", "credit_card") if idn.get(k)]:
        issuer = world_parties_party(world, card["issuer"])
        scheme = world["card_schemes"].get(card["scheme"])
        numeric = world["countries"][issuer["c"]]["numeric"]
        if not (re.fullmatch(r"\d{16}", card["pan"]) and card["pan"][:6] == "9" + numeric
                + issuer["identity"]["card_issuer_digits"] and world_ids.luhn(card["pan"])):
            out.append(f"{where}: card number {card['pan']} is not 9, the issuer's country {numeric}, its issuer digits "
                       "and a Luhn check digit (ISO/IEC 7812)")
        if not scheme:
            out.append(f"{where}: card scheme {card['scheme']} is not a card scheme of the world")
        elif card.get("aid") and not card["aid"].startswith(scheme["rid"]):
            out.append(f"{where}: chip application {card['aid']} does not start with the scheme's RID {scheme['rid']}")
        elif scheme["rid"][:4] != "D" + world["countries"][scheme["country"]]["numeric"]:
            out.append(f"{where}: the RID {scheme['rid']} is not in the national category D of {scheme['country']}")
        if bool(card.get("valid_from")) != bool(card.get("expires")) or (card.get("expires") and not (
                re.fullmatch(r"\d{4}-\d{2}", card["valid_from"]) and re.fullmatch(r"\d{4}-\d{2}", card["expires"])
                and card["valid_from"] < card["expires"])):
            out.append(f"{where}: card {card['pan']}: the validity runs from a month (YYYY-MM) to a later month")
        if card.get("cv2") and not re.fullmatch(r"\d{3}", card["cv2"]):
            out.append(f"{where}: card {card['pan']}: the security code has three digits")
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


def world_parties_party(world, pid):
    return next(x for x in world["parties"] if x["id"] == pid)


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
    if spec.get("municipalities"):
        town = spec.get("localities", {}).get(a.get("CityName"), a.get("CityName"))   # a locality's municipality
        if a["ID"][:4] != spec["municipalities"].get(town):
            return [f"{where}: address number {a['ID']} is not from the municipality of {town}"]
    return []


if __name__ == "__main__":
    w = world_data.load()
    probs = check(w)
    print("\n".join(probs) or f"party identities: {len(w['parties'])} parties, no problems")
    sys.exit(1 if probs else 0)
