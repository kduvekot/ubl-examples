#!/usr/bin/env python3
"""Validate the example documents of the world in two phases, as UBL prescribes.

Phase 1  XSD: every document against the UBL 2.5 runtime schema of its type, from
         the endorsed set (no deprecated document types or elements).
Phase 2  code values, twice:
  (a)    UBL's own phase 2: val/UBL-DefaultDTQ-2.5.xsl, run with Saxon exactly as
         UBL's validate.sh does, with the UBL default code lists. The world replaces
         some of those lists (its countries and currencies are not in them, its
         languages are written in lower case, it uses UN/EDIFACT 5189 and 7161 for
         allowances and charges, and it gives a listID to the lists UBL leaves without
         one), so this phase may object only to values in the contexts of lists the
         world replaces, and to nothing else.
  (b)    the world's own context/value associations (world/codelists/world-codes.json,
         made by tools/build_codelists.py from world/codelists/lists.json), which
         replace UBL's: every code element must carry the listID of its list and a
         code of that list, compared exactly; an element with several possible lists
         (by parent element, by ChargeIndicator, or by listID) must use one of them; a
         code element no association covers is an error, unless the world lists it as
         a code a party defines for itself. An identifier element that holds a code
         (TaxCategory/ID, TaxScheme/ID, Language/ID, HazardClassID, DeliveryTerms/ID,
         AttributeID ...) is checked the same way, with its schemeID naming the list. Code attributes: @currencyID (the world's
         currency list), @unitCode and @mimeCode (UBL's lists), @languageID (BCP 47: a
         language of the world's ISO 639 list and an optional region subtag).

Usage: python3 tools/validate_examples.py world/examples/<flow>/*.xml
Needs .ubl/ (sh tools/fetch_ubl_validation.sh <DocumentType>...) and Java for (a).
"""
import json
import os
import re
import subprocess
import sys
import tempfile

from lxml import etree

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402

ROOT = world_data.ROOT
UBL = os.path.join(ROOT, ".ubl")
NS = {"cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
      "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"}


def doc_type(path):
    return etree.parse(path).getroot().tag.split("}")[1]


def phase1(path):
    xsd = os.path.join(UBL, "endorsed", "xsdrt", "maindoc", f"UBL-{doc_type(path)}-2.5.xsd")
    schema = etree.XMLSchema(etree.parse(xsd))
    ok = schema.validate(etree.parse(path))
    return [] if ok else [f"phase 1: line {e.line}: {e.message}" for e in schema.error_log]


def world_cva():
    cva = json.load(open(os.path.join(ROOT, "world", "codelists", "world-codes.json"), encoding="utf-8"))
    ubl = json.load(open(os.path.join(ROOT, "world", "codelists", "ubl-default-codes.json"), encoding="utf-8"))["lists"]
    for lst in cva["lists"].values():
        lst["codes"] = set(lst["codes"]) if "codes" in lst else set(ubl[lst["ubl"]]["codes"])
    # the UBL lists the world replaces: their contexts in UBL's own phase 2 may object
    kept = {lst["ubl"].split("-")[0] for lst in cva["lists"].values() if lst["scope"] == "ubl"}
    cva["replaced"] = {l["short"][:-4] for l in ubl.values()} - kept
    return cva


def phase2a(path, replaced):
    """UBL's own phase 2. Returns the problems in contexts of lists the world does not replace, and the number of
    objections to values in lists it replaces, per list."""
    with tempfile.TemporaryDirectory() as tmp:
        svrl = os.path.join(tmp, "svrl.xml")
        subprocess.run(["java", "-jar", os.path.join(UBL, "val", "saxon9he.jar"), f"-s:{path}",
                        f"-xsl:{os.path.join(UBL, 'val', 'UBL-DefaultDTQ-2.5.xsl')}", f"-o:{svrl}"],
                       check=True, capture_output=True)
        text = open(svrl, encoding="utf-8").read()
    problems, expected = [], {}
    for m in re.finditer(r"<svrl:failed-assert.*?<svrl:text>(.*?)</svrl:text>", text, re.S):
        msg = " ".join(m.group(1).split())
        v = re.search(r"Value supplied '([^']*)' is unacceptable for constraints identified by '([^']*)'", msg)
        short = v and v.group(2).split()[0].rsplit("-", 1)[0]
        if short in replaced:
            expected[short] = expected.get(short, 0) + 1
        else:
            problems.append(f"phase 2a (UBL default code lists): {msg}")
    return problems, expected


def bcp47(tag, languages, regions):
    m = re.fullmatch(r"([a-z]{2,3})(?:-([A-Z]{2}))?", tag)
    if not m:
        return "not a language subtag in lower case with an optional region subtag in upper case"
    if m.group(1) not in languages:
        return f"the language subtag {m.group(1)} is not in the world's ISO 639 list"
    if m.group(2) and m.group(2) not in regions:
        return f"the region subtag {m.group(2)} is not a BCP 47 region"
    return None


def phase2b(path, cva):
    """The world's context/value associations. Each code element is checked by the first context that addresses
    it, as in a Schematron pattern."""
    tree = etree.parse(path)
    problems, done = [], set()
    lists = cva["lists"]
    for ctx in cva["contexts"]:
        cand = [lists[k] for k in ctx["lists"]]
        for node in tree.xpath(ctx["address"] if ctx["address"].startswith("/") else "//" + " | //".join(
                p.strip() for p in ctx["address"].split("|")), namespaces=NS):
            if node in done:
                continue
            done.add(node)
            attr = ctx.get("attribute", "listID")      # an identifier holding a code names its list in schemeID
            where, value, given = tree.getpath(node), node.text, node.get(attr)
            names = " or ".join(l["listID"] for l in cand)
            if given is None:
                problems.append(f"phase 2b: {where}: no {attr} (the world's list: {names})")
                continue
            lst = next((l for l in cand if l["listID"] == given), None)
            if lst is None:
                problems.append(f"phase 2b: {where}: {attr} '{given}' is not the list for this context ({names})")
            elif value not in lst["codes"]:
                problems.append(f"phase 2b: {where}: '{value}' is not a code of {given}")
    for node in tree.xpath("//cbc:*[substring(local-name(), string-length(local-name()) - 3) = 'Code']",
                           namespaces=NS):
        if node in done:
            continue
        name, parent = etree.QName(node).localname, etree.QName(node.getparent()).localname
        if f"{name}@{parent}" in cva.get("pending", ()):     # while the world's lists are being made: not yet checked
            continue
        if not any(u["element"] == name and (not u.get("parents") or parent in u["parents"]) for u in cva["unlisted"]):
            problems.append(f"phase 2b: {tree.getpath(node)}: no code list of the world covers {name} in {parent}")
    for a in cva["attributes"]:
        lst = lists[a["lists"][0]]
        xp = " | ".join("//" + p.strip() for p in a["address"].split("|"))
        for value in tree.xpath(xp, namespaces=NS):
            where = tree.getpath(value.getparent()) + "/@" + a["attribute"]
            if a["attribute"] == "languageID":
                why = bcp47(value, lst["codes"], set(a["regions"]))
                if why:
                    problems.append(f"phase 2b: {where}: '{value}' is not a BCP 47 language tag of the world: {why}")
            elif value not in lst["codes"]:
                problems.append(f"phase 2b: {where}: '{value}' is not a code of {lst['listID'] or lst['name']}")
    return problems


def main(paths):
    cva = world_cva()
    failed = 0
    print(f"Phase 2b uses the world's {len(cva['contexts'])} code element contexts and {len(cva['attributes'])} "
          f"attribute contexts (world/codelists/world-codes.json), in place of UBL's; UBL's own phase 2 may object "
          f"only in the contexts of the lists the world replaces: {', '.join(sorted(cva['replaced']))}."
          + (f" Not yet bound to a list of the world: {len(cva['pending'])} code elements." if cva.get("pending") else ""))
    for path in paths:
        problems = phase1(path)
        expected = {}
        if not problems:
            p2a, expected = phase2a(path, cva["replaced"])
            problems = p2a + phase2b(path, cva)
        name = os.path.relpath(path, ROOT)
        if problems:
            failed += 1
            print(f"{name}: INVALID")
            for p in problems:
                print(f"  {p}")
        else:
            objections = ", ".join(f"{n} in {k}" for k, n in sorted(expected.items())) or "none"
            print(f"{name}: valid (phase 1; phase 2 with the world's code lists; UBL's own phase 2 objects only "
                  f"in lists the world replaces: {objections})")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
