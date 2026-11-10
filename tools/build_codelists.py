#!/usr/bin/env python3
"""Make the code lists of the UBL example world.

The world's countries (XU, XB, XL) are ISO 3166-1 user-assigned codes and its
currencies are invented, so they are not in the UBL 2.5 default code lists.
UBL's two-phase validation lets trading partners use their own code lists
(UBL 2.5 Appendix F). This script makes them by copying the UBL 2.5 default
lists unchanged and adding the world's codes from world/countries.json:

  world/codelists/CountryIdentificationCode-2.4-world.gc
  world/codelists/CurrencyCode-2.4-world.gc
  world/codelists/ubl-default-codes.json   the UBL 2.5 context/value associations (CVA)
                                           with the codes of every value list they name,
                                           for code list validation without network

Each copy gets its own identification (version and URIs, under
urn:ubl-examples:world), so a validator can tell it from the original; the
LocationUri points to the copy published with the site. The world currency codes are checked against the
current ISO 4217 list, so that no invented code is a real one.

Usage: python3 tools/build_codelists.py            (downloads the originals, writes the lists)
       python3 tools/build_codelists.py --check    (no network: are the lists up to date?)
"""
import hashlib
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402

BASE = "https://docs.oasis-open.org/ubl/os-UBL-2.5/cl/gc/default/"
LISTS = {  # file -> sha256 of the UBL 2.5 original
    "CountryIdentificationCode-2.4.gc": "3b5f7249138e554574a4b31b5b6839fd0c92cb12bac8df597d37459db5962114",
    "CurrencyCode-2.4.gc": "ede125e1900093e6be9ff686d7c693ebf337dbbc674000cd323469367422c981",
}
ISO4217 = "https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml"
GC = "http://docs.oasis-open.org/codelist/ns/genericode/1.0/"
OUT = os.path.join(world_data.ROOT, "world", "codelists")
PAGES = "https://kduvekot.github.io/ubl-examples/codelists/"


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def row(values):
    r = ET.Element("Row")
    for col, val in values:
        v = ET.SubElement(r, "Value", ColumnRef=col)
        ET.SubElement(v, "SimpleValue").text = val
    return r


def derive(name, raw, rows):
    ET.register_namespace("gc", GC)
    root = ET.fromstring(raw)
    ident = root.find("Identification")
    version = ident.find("Version")
    base_version = version.text
    version.text = f"{base_version}-world"
    world = os.path.basename(name).replace(".gc", "-world.gc")
    short = ident.find("ShortName").text
    ident.find("CanonicalUri").text = f"urn:ubl-examples:world:codelist:{short}"
    ident.find("CanonicalVersionUri").text = f"urn:ubl-examples:world:codelist:{short}:{version.text}"
    ident.find("LocationUri").text = PAGES + world
    for ln in ident.findall("LongName"):
        if ln.get("{http://www.w3.org/XML/1998/namespace}lang") == "en":
            ln.text += " (UBL example world)"
    codes = root.find("SimpleCodeList")
    existing = {r.find("Value[@ColumnRef='code']/SimpleValue").text for r in codes}
    for values in rows:
        if values[0][1] in existing:
            raise SystemExit(f"{name}: {values[0][1]} is already in the UBL list")
        codes.append(row(values))
    ET.indent(root, space="   ")
    path = os.path.join(OUT, world)
    with open(path, "wb") as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(b"<!-- Derived from " + (BASE + name).encode() + b" (version " + base_version.encode() +
                b"), unchanged, with the codes of the UBL example world added at the end"
                b" by tools/build_codelists.py from world/countries.json. -->\n")
        f.write(ET.tostring(root, encoding="utf-8"))
        f.write(b"\n")
    return os.path.relpath(path, world_data.ROOT), len(existing), len(rows)


CVA = "https://docs.oasis-open.org/ubl/os-UBL-2.5/cva/UBL-DefaultDTQ-2.5.cva"
CVA_NS = "http://docs.oasis-open.org/codelist/ns/ContextValueAssociation/1.0/"


def write_cva():
    """The UBL 2.5 context/value associations with the codes of every value list they name.

    Code list validation (phase 2) checks the value at each context address against the union of
    the lists named for it, and the list metadata (listID) if the instance gives it. The lists are
    resolved from their official locations, relative to the CVA file, as the CVA prescribes."""
    import urllib.parse
    raw = fetch(CVA)
    root = ET.fromstring(raw)
    lists = {}
    for vl in root.iter(f"{{{CVA_NS}}}ValueList") if root.find(f".//{{{CVA_NS}}}ValueList") is not None else root.iter("ValueList"):
        uri = urllib.parse.urljoin(CVA, vl.get("uri"))
        gc = ET.fromstring(fetch(uri))
        ident = gc.find("Identification")
        list_id = next((ln.text for ln in ident.findall("LongName") if ln.get("Identifier") == "listID"), None)
        lists[vl.get("{http://www.w3.org/XML/1998/namespace}id")] = {
            "uri": uri, "short": ident.find("ShortName").text, "listID": list_id,
            "codes": sorted({r.find("Value[@ColumnRef='code']/SimpleValue").text for r in gc.find("SimpleCodeList")}),
            "names": {r.find("Value[@ColumnRef='code']/SimpleValue").text: (r.findtext("Value[@ColumnRef='name']/SimpleValue") or "")
                      for r in gc.find("SimpleCodeList")}}
    contexts = [{"address": c.get("address"), "values": c.get("values").split()}
                for c in root.iter("Context")]
    out = {"source": CVA, "contexts": contexts, "lists": lists}
    with open(os.path.join(OUT, "ubl-default-codes.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=0, sort_keys=True)
        f.write("\n")
    print(f"world/codelists/ubl-default-codes.json: {len(contexts)} contexts, {len(lists)} value lists")


def world_rows(countries):
    return {
        "CountryIdentificationCode-2.4.gc": [
            [("code", k), ("name", c["name"]), ("numericcode", c["numeric"]), ("ref", c["alpha3"])]
            for k, c in countries.items()],
        "CurrencyCode-2.4.gc": [
            [("code", c["currency"]["code"]), ("name", c["currency"]["name"]), ("numericcode", c["currency"]["numeric"]),
             ("fractionaldigits", str(c["currency"]["minor_units"])), ("country", c["name"].upper())]
            for c in countries.values()],
    }


def check():
    """Without network: the committed lists hold exactly the world codes of world/countries.json."""
    problems = []
    for name, rows in world_rows(world_data.load()["countries"]).items():
        path = os.path.join(OUT, name.replace(".gc", "-world.gc"))
        if not os.path.exists(path):
            problems.append(f"{path}: missing; run tools/build_codelists.py")
            continue
        got = [[(v.get("ColumnRef"), v.findtext("SimpleValue")) for v in r]
               for r in ET.parse(path).getroot().find("SimpleCodeList")][-len(rows):]
        if got != rows:
            problems.append(f"{os.path.relpath(path, world_data.ROOT)}: out of date with world/countries.json; "
                            "run tools/build_codelists.py")
    return problems


def main():
    if "--check" in sys.argv:
        problems = check()
        print("\n".join(problems) or "world code lists: up to date")
        sys.exit(1 if problems else 0)
    countries = world_data.load()["countries"]
    try:
        iso = fetch(ISO4217).decode("utf-8")
        taken = {c for c in re.findall(r"<Ccy>([A-Z]{3})</Ccy>", iso)}
        numbers = set(re.findall(r"<CcyNbr>(\d{3})</CcyNbr>", iso))
        for code, c in countries.items():
            cur = c["currency"]
            if cur["code"] in taken or cur["numeric"] in numbers:
                raise SystemExit(f"{code}: currency {cur['code']} / {cur['numeric']} is a real ISO 4217 code")
    except OSError as e:
        print(f"warning: the current ISO 4217 list could not be read ({e}); currency codes not checked")
    rows = world_rows(countries)
    os.makedirs(OUT, exist_ok=True)
    write_cva()
    for name in LISTS:
        raw = fetch(BASE + name)
        if hashlib.sha256(raw).hexdigest() != LISTS[name]:
            raise SystemExit(f"{name}: the UBL 2.5 original has changed")
        path, n, added = derive(name, raw, rows[name])
        print(f"{path}: {n} UBL codes + {added} world codes")


if __name__ == "__main__":
    main()
