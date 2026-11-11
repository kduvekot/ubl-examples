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
    and state, and in a country with states the state follows the
    country's rule;
  * every account is held at a bank of the world in the same country;
  * e-mail addresses and websites use the reserved .example domain (RFC
    2606), and telephone numbers the country code +999 that the ITU keeps in
    reserve, so none can reach a real organisation;
  * industry codes are ISIC Rev. 4 classes, and parties referred to exist.

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


def account_valid(acc):
    country, check, rest = acc[:2], acc[2:4], acc[4:]
    return account_check(country, rest[:4], rest[4:]) == check


def tax_id_valid(country, tax_id):
    if country == "XU":
        return len(tax_id) == 11 and tax_id[:2] == "XU" and tax_id[2:].isdigit() and mod11(tax_id[2:10]) == tax_id[10]
    if country == "XB":
        st, _, num = tax_id.partition("-")
        return st in ("UL", "CO") and len(num) == 7 and num.isdigit()
    return False


def nearest_town(world, p):
    """The nearest town or locality in the party's own country and, where there are states, its own state."""
    places = [t for t in world["towns"] + world.get("localities", [])
              if t["country"] == p["c"] and state_of(world, {"c": t["country"], "at": t["c"]}) == state_of(world, p)]
    return min(places, key=lambda t: math.dist(t["c"], p["at"]))["name"] if places else None


def state_of(world, p):
    rule = world["countries"][p["c"]].get("subdivision_rule")
    if not rule:
        return None
    return rule["west"] if p["at"][0] < rule["column"] else rule["east"]


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
        if idn.get("tax_id") and not tax_id_valid(p["c"], idn["tax_id"]):
            problems.append(f"{where}: tax number {idn['tax_id']} is not valid for {p['c']}")
        a = idn.get("address", {})
        town = nearest_town(world, p)
        if a.get("CityName") != town:
            problems.append(f"{where}: city {a.get('CityName')} but the nearest town of its country is {town}")
        st = state_of(world, p)
        if st and a.get("CountrySubentity") != st:
            problems.append(f"{where}: state {a.get('CountrySubentity')} but its place is in {st}")
        if not st and a.get("CountrySubentity"):
            problems.append(f"{where}: its country has no states")
        for k in ("StreetName", "BuildingNumber"):
            if not a.get(k):
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
        acc = idn.get("account")
        if acc:
            bank = parties.get(acc["bank"])
            if not bank or bank.get("cat") != "finance" or "bank" not in bank["identity"].get("kind", ""):
                problems.append(f"{where}: account at {acc['bank']}, which is not a bank of the world")
            elif bank["c"] != p["c"] and not acc.get("abroad"):
                problems.append(f"{where}: account at a bank in another country")
            if not account_valid(acc["number"]):
                problems.append(f"{where}: account number {acc['number']} has wrong check digits")
            elif acc["number"][:2] != bank["c"] or acc["number"][4:8] != bank["identity"].get("bank_code"):
                problems.append(f"{where}: account number does not belong to bank {acc['bank']}")
    return problems


if __name__ == "__main__":
    w = world_data.load()
    probs = check(w)
    print("\n".join(probs) or f"party identities: {len(w['parties'])} parties, no problems")
    sys.exit(1 if probs else 0)
