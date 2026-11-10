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
  * e-mail addresses use the reserved .example domain (RFC 2606), so none
    can belong to a real organisation.

Usage: python3 tools/world_parties.py      (prints the problems, exit 1 if any)
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402


def mod11(digits):
    """Check digit for the XA tax number: weights 9..2 over 8 digits, modulus 11 (10 is not allowed)."""
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
    if country == "XA":
        return len(tax_id) == 11 and tax_id[:2] == "XA" and tax_id[2:].isdigit() and mod11(tax_id[2:10]) == tax_id[10]
    if country == "XB":
        st, _, num = tax_id.partition("-")
        return st in ("CS", "US") and len(num) == 7 and num.isdigit()
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
