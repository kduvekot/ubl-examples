#!/usr/bin/env python3
"""Make the code lists of the UBL example world.

The world's countries (XU, XB, XL) are ISO 3166-1 user-assigned codes and its
currencies are invented, so they are not in the UBL 2.5 default code lists.
UBL's two-phase validation lets trading partners use their own code lists
(UBL 2.5 Appendix F). This script makes them:

  world/codelists/CountryIdentificationCode-2.4-world.gc   UBL's country and currency lists, unchanged, with
  world/codelists/CurrencyCode-2.4-world.gc                the world's codes added (from world/countries.json)
  world/codelists/ubl-default-codes.json   the UBL 2.5 context/value associations (CVA)
                                           with the codes of every value list they name,
                                           for code list validation without network
  world/codelists/gc/*.gc                  every other list of the world, from world/codelists/lists.json
                                           (tools/codelists.py): the Trade Accord's regional lists, the national
                                           lists, world copies of external lists (built from the copies in
                                           world/codelists/sources) and of UBL lists that lack a listID
  world/codelists/world-codes.json         the world's context/value associations, resolved: which list every
                                           code element and code attribute uses, with the codes; phase 2 of
                                           tools/validate_examples.py reads only this
  world/codelists/UBL-World-2.5.cva        the same associations as an OASIS CVA file

Each copy gets its own identification (version and URIs, under
urn:ubl-examples:world), so a validator can tell it from the original; the
LocationUri points to the copy published with the site. The world currency codes are checked against the
ISO 4217 list and the world's market identifier codes against the ISO 10383 list, so that no invented code is a
real one; both lists are kept in world/codelists/sources.

Usage: python3 tools/build_codelists.py            (writes the world's lists; downloads UBL's originals)
       python3 tools/build_codelists.py --offline  (writes the world's lists only)
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
import codelists  # noqa: E402
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


# ---------------------------------------------------------------- the world's own lists (world/codelists/lists.json)
AGENCY = {"regional": "Lumeport Trade Accord"}
LANG_NAME = {"en": "English", "qau": "Urvanian", "qal": "Lisavan"}


def gc_file(key):
    return key.replace(":", "-") + "Code.gc"


def gc_list(key, lst):
    """A genericode 1.0 file of one list: code, name (in English, and in the languages of the list's countries
    for the world's own lists), description."""
    ET.register_namespace("gc", GC)
    root = ET.Element(f"{{{GC}}}CodeList")
    scope = lst["scope"]
    ident = ET.SubElement(root, "Identification")
    ET.SubElement(ident, "ShortName").text = codelists.short_name(key)
    ET.SubElement(ident, "LongName", {"xml:lang": "en"}).text = f"{lst['name']} (UBL example world)"
    ET.SubElement(ident, "LongName", Identifier="listID").text = lst["listID"]
    version = lst.get("version", "1.0")
    ET.SubElement(ident, "Version").text = version
    canonical = lst["listID"] if lst["listID"].startswith("urn:") else \
        f"urn:ubl-examples:world:codelist:copy:{codelists.short_name(key)}"
    ET.SubElement(ident, "CanonicalUri").text = canonical
    ET.SubElement(ident, "CanonicalVersionUri").text = f"{canonical}:{version}"
    ET.SubElement(ident, "LocationUri").text = PAGES + "gc/" + gc_file(key)
    agency = ET.SubElement(ident, "Agency")
    countries = world_data.load()["countries"]
    ET.SubElement(agency, "LongName", {"xml:lang": "en"}).text = \
        AGENCY.get(scope) or (f"Government of {countries[scope]['name']}" if scope in countries else lst.get("agency") or "OASIS Universal Business Language (UBL) TC")
    langs = ["en"] + codelists.LANGS.get(scope, []) if scope in codelists.LANGS else ["en"]
    cols = ET.SubElement(root, "ColumnSet")
    columns = [("code", "Code", "normalizedString", None, "required")]
    columns += [("name" if l == "en" else f"name-{l}", "Name", "string", l, "required") for l in langs]
    columns += [("description", "Description", "string", "en", "optional")]
    if any(c.get("mime") for c in lst["codes"].values()):
        columns.append(("mime", "MimeType", "string", None, "optional"))
    for cid, short, typ, lang, use in columns:
        col = ET.SubElement(cols, "Column", Id=cid, Use=use)
        ET.SubElement(col, "ShortName").text = short
        ET.SubElement(col, "Data", {"Type": typ, **({"Lang": lang} if lang else {})})
    k = ET.SubElement(cols, "Key", Id="codeKey")
    ET.SubElement(k, "ShortName").text = "CodeKey"
    ET.SubElement(k, "ColumnRef", Ref="code")
    rows = ET.SubElement(root, "SimpleCodeList")
    for code, c in lst["codes"].items():
        vals = [("code", code)] + [("name" if l == "en" else f"name-{l}", codelists.name_in(lst, code, l))
                                   for l in langs]
        if c.get("description"):
            vals.append(("description", c["description"]))
        if c.get("mime"):
            vals.append(("mime", c["mime"]))
        rows.append(row(vals))
    ET.indent(root, space="   ")
    if scope == "external" and lst.get("source"):
        src = lst["source"]
        note = (f"A world copy of {lst['name']}: the codes the world uses, and others of the same list. Built from "
                f"world/codelists/sources/{src.get('file') or ', '.join(src['files'])} ({src.get('version', version)}).")
        if any(c.get("added") for c in lst["codes"].values()):
            note += f" Added for the world: {', '.join(k for k, c in lst['codes'].items() if c.get('added'))}."
    elif scope == "external":
        note = (f"A world copy of {lst['name']}: the codes the world uses, and others of the same list. No "
                f"machine-readable copy of the source could be kept ({lst.get('reference', '')}); the codes and names "
                "are as the standard publishes them.")
    elif scope == "ubl-copy":
        note = (f"A world copy of UBL's default list {lst['ubl']} ({lst['uri']}), with the same codes, given a listID: "
                "UBL's own list has none, or one that an instance cannot quote.")
    else:
        note = f"A code list of the UBL example world: {lst['name'].lower()}. {lst.get('description', '')}".strip()
    head = (f'<?xml version="1.0" encoding="UTF-8"?>\n<!-- {note} Made by tools/build_codelists.py from '
            f'world/codelists/lists.json. -->\n')
    return head.encode() + ET.tostring(root, encoding="utf-8") + b"\n"


def address(b):
    """The CVA address of a binding: the element, under its parents, with the binding's condition."""
    cond = "".join(f"[cbc:{k}='{v}']" for k, v in (b.get("when") or {}).items())
    if b.get("parents"):
        return " | ".join(f"*[local-name()='{p}']{cond}/cbc:{b['element']}" for p in b["parents"])
    if cond:
        raise SystemExit(f"world/codelists/lists.json: a condition needs parents ({b['element']})")
    return f"cbc:{b['element']}"


def regions():
    """The region subtags of BCP 47 (IANA language subtag registry): two letters, and the private-use XA..XZ."""
    text = open(os.path.join(OUT, "sources", "iana", "language-subtag-registry.txt"), encoding="utf-8").read()
    out = set()
    for rec in text.split("%%"):
        f = dict(re.findall(r"^([A-Za-z-]+): (.*)$", rec, re.M))
        if f.get("Type") == "region" and re.fullmatch(r"[A-Z]{2}(\.\.[A-Z]{2})?", f.get("Subtag", "")):
            a, _, b = f["Subtag"].partition("..")
            out |= {a} if not b else {a[0] + chr(c) for c in range(ord(a[1]), ord(b[1]) + 1)}
    return sorted(out)


def world_lists():
    """Every file this script makes from world/codelists/lists.json: {path relative to the repository: bytes}."""
    model = codelists.load()
    files = {}
    for key, lst in model["lists"].items():
        if lst["scope"] in ("ubl", "world-ubl"):
            continue
        files[f"world/codelists/gc/{gc_file(key)}"] = gc_list(key, lst)
    ubl = codelists.ubl_lists()
    ubl_cva = json.load(open(os.path.join(OUT, "ubl-default-codes.json"), encoding="utf-8"))
    lists = {}
    for key, lst in model["lists"].items():
        entry = {"listID": lst["listID"], "scope": lst["scope"], "name": lst["name"]}
        if lst["scope"] == "ubl":
            entry["ubl"] = lst["ubl"]
            entry["location"] = ubl[lst["ubl"]]["uri"]
        else:
            entry["location"] = lst.get("file") and f"world/codelists/{lst['file']}" or \
                f"world/codelists/gc/{gc_file(key)}"
            entry["codes"] = list(lst["codes"])
        lists[key] = entry
    contexts = [{"element": b["element"], "address": address(b), "lists": b["lists"],
                 **({"parents": b["parents"]} if b.get("parents") else {}),
                 **({"when": b["when"]} if b.get("when") else {}),
                 **({"attribute": b["attribute"]} if b.get("attribute") else {})} for b in model["bindings"]]
    attrs = []
    for name, key in model["attributes"].items():
        if key == "ubl":                   # the attribute contexts of UBL's CVA, as they are
            for c in ubl_cva["contexts"]:
                if c["address"].endswith(f"@{name}"):
                    lst = next(k for k, l in model["lists"].items() if l.get("ubl") == c["values"][-1])
                    attrs.append({"attribute": name, "address": c["address"], "lists": [lst]})
        else:
            a = {"attribute": name, "address": f"@{name}", "lists": [key]}
            if name == "languageID":
                a["rule"] = "BCP 47 (RFC 5646): a language subtag of the list, optionally a region subtag"
                a["regions"] = regions()
            attrs.append(a)
    cva = {"description": "The context/value associations of the UBL example world, made by tools/build_codelists.py "
                          "from world/codelists/lists.json. Every code element is checked against the list its "
                          "context names; where a context names several lists, the code's listID chooses one. "
                          "An identifier element that holds a code (TaxCategory/ID, Language/ID, AttributeID ...) is "
                          "checked the same way, its schemeID naming the list. "
                          "They replace UBL's own associations for the world's documents.",
           "contexts": contexts, "unlisted": model["unlisted"], "attributes": attrs, "lists": lists}
    if model.get("pending"):
        cva["pending"] = model["pending"]
    files["world/codelists/world-codes.json"] = (json.dumps(cva, ensure_ascii=False, indent=1) + "\n").encode()
    files["world/codelists/UBL-World-2.5.cva"] = cva_xml(cva)
    return files


def cva_xml(cva):
    ns = "http://docs.oasis-open.org/codelist/ns/ContextValueAssociation/1.0/"
    ET.register_namespace("cva", ns)
    root = ET.Element(f"{{{ns}}}ContextValueAssociation", {"name": "UBL-World-2.5", "id": "urn:ubl-examples:world:cva"})
    ET.SubElement(ET.SubElement(root, "Annotation"), "Description").text = cva["description"]
    ET.SubElement(root, "Title").text = "Code lists of the UBL example world"
    vls = ET.SubElement(root, "ValueLists")
    for key, lst in cva["lists"].items():
        uri = lst["location"] if lst["scope"] == "ubl" else os.path.relpath(lst["location"], "world/codelists")
        ET.SubElement(vls, "ValueList", {"xml:id": key.replace(":", "-"), "uri": uri})
    ims = ET.SubElement(ET.SubElement(root, "InstanceMetadataSets"), "InstanceMetadataSet", {"xml:id": "code"})
    ET.SubElement(ims, "InstanceMetadata", address="@listID", identification="LongName[@Identifier='listID']")
    ims = ET.SubElement(root.find("InstanceMetadataSets"), "InstanceMetadataSet", {"xml:id": "scheme"})
    ET.SubElement(ims, "InstanceMetadata", address="@schemeID", identification="LongName[@Identifier='listID']")
    ctxs = ET.SubElement(root, "Contexts")
    for c in cva["contexts"]:
        ET.SubElement(ctxs, "Context", address=c["address"], values=" ".join(k.replace(":", "-") for k in c["lists"]),
                      metadata="scheme" if c.get("attribute") == "schemeID" else "code")
    for a in cva["attributes"]:
        ET.SubElement(ctxs, "Context", address=a["address"], values=" ".join(k.replace(":", "-") for k in a["lists"]))
    ET.indent(root, space="   ")
    return b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="utf-8") + b"\n"


def real_code_problems():
    """The world's invented codes must not be real ones: currencies against ISO 4217, market identifier codes
    against ISO 10383 (both kept in world/codelists/sources)."""
    problems = []
    iso = open(os.path.join(OUT, "sources", "iso4217", "list-one.xml"), encoding="utf-8").read()
    taken, numbers = set(re.findall(r"<Ccy>([A-Z]{3})</Ccy>", iso)), set(re.findall(r"<CcyNbr>(\d{3})</CcyNbr>", iso))
    for code, c in world_data.load()["countries"].items():
        cur = c["currency"]
        if cur["code"] in taken or cur["numeric"] in numbers:
            problems.append(f"{code}: currency {cur['code']} / {cur['numeric']} is a real ISO 4217 code")
    icd = codelists.READERS["peppol"](os.path.join(OUT, "sources", "peppol", "ICD.xml"))
    for sid, spec in world_data.load().get("identifier_schemes", {}).items():   # the Codana ICD is not a real one
        for code in re.findall(r"\^(\d{4}):", spec["pattern"]) if sid == "ISO 6523" else ():
            if code in icd:
                problems.append(f"ISO 6523: the world's code designator {code} is a real ICD ({icd[code]['name']})")
    mic = codelists.READERS["mic"](os.path.join(OUT, "sources", "iso10383", "ISO10383_MIC.csv"))
    for key, lst in codelists.load()["lists"].items():
        for code in lst["codes"] if lst.get("checked_against") == "ISO 10383" else ():
            if code in mic:
                problems.append(f"{key}: {code} is a real ISO 10383 market identifier code ({mic[code]['name']})")
            if not re.fullmatch(r"[A-Z0-9]{4}", code):
                problems.append(f"{key}: {code} is not shaped like an ISO 10383 MIC (four letters or digits)")
    return problems


def iso20022_problems():
    """The world's copies of ISO 20022 external code sets give each code's definition word for word as the release
    kept in world/codelists/sources/iso20022 does (its JSON schema lists every code with its definition)."""
    problems = []
    defs = json.load(open(os.path.join(OUT, "sources", "iso20022", "2Q2026_externalcodesets_v3.json"),
                          encoding="utf-8"))["definitions"]
    for key, lst in codelists.load()["lists"].items():
        name = (lst.get("listID") or "").removeprefix("ISO 20022 ")
        if not name.startswith("External") or name not in defs:
            continue
        given = dict(re.findall(r"\*`([A-Z0-9]+)`-([^\n]*)", defs[name]["description"]))
        for code, c in lst["codes"].items():
            if code not in given:
                problems.append(f"{key}: {code} is not a code of {name} in the 2Q2026 release")
            elif c["description"] != given[code].strip():
                problems.append(f"{key}: {code}: the definition differs from the 2Q2026 release: {given[code]!r}")
    return problems


def check():
    """Without network: the committed lists hold exactly the world codes of world/countries.json, and the world's
    own lists are what world/codelists/lists.json makes."""
    problems = real_code_problems() + iso20022_problems()
    for rel, data in world_lists().items():
        path = os.path.join(world_data.ROOT, rel)
        if not os.path.exists(path) or open(path, "rb").read() != data:
            problems.append(f"{rel}: out of date with world/codelists/lists.json; run tools/build_codelists.py --offline")
    stale = sorted(set(os.listdir(os.path.join(OUT, "gc"))) - {os.path.basename(r) for r in world_lists()}) \
        if os.path.isdir(os.path.join(OUT, "gc")) else []
    problems += [f"world/codelists/gc/{s}: no longer a list of the world" for s in stale]
    if world_data.MISSING_WORDS:
        problems.append("words missing from the vocabularies of the world's languages (world/countries.json; save the list as missing.json and run python3 tools/lexicon.py missing.json qau|qal): "
                        + json.dumps(sorted(world_data.MISSING_WORDS)))
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
    problems = real_code_problems() + iso20022_problems()
    if problems:
        raise SystemExit("\n".join(problems))
    files = world_lists()
    if world_data.MISSING_WORDS:
        raise SystemExit("words missing from the vocabularies of the world's languages (world/countries.json; save the list as missing.json and run python3 tools/lexicon.py missing.json qau|qal): "
                         + json.dumps(sorted(world_data.MISSING_WORDS)))
    os.makedirs(os.path.join(OUT, "gc"), exist_ok=True)
    for name in os.listdir(os.path.join(OUT, "gc")):
        if f"world/codelists/gc/{name}" not in files:
            os.remove(os.path.join(OUT, "gc", name))
    for rel, data in files.items():
        with open(os.path.join(world_data.ROOT, rel), "wb") as f:
            f.write(data)
    print(f"world/codelists: {sum(r.startswith('world/codelists/gc/') for r in files)} lists, world-codes.json, "
          "UBL-World-2.5.cva")
    if "--offline" in sys.argv:
        return
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
