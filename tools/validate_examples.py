#!/usr/bin/env python3
"""Validate the example documents of the world in two phases, as UBL prescribes.

Phase 1  XSD: every document against the UBL 2.5 runtime schema of its type, from
         the endorsed set (no deprecated document types or elements).
Phase 2  code values, twice:
  (a)    UBL's own phase 2: val/UBL-DefaultDTQ-2.5.xsl, run with Saxon exactly as
         UBL's validate.sh does, with the UBL default code lists. The world's
         countries and currencies are not in those lists, so this phase must fail
         on exactly those codes and on nothing else.
  (b)    the same context/value associations (the UBL 2.5 CVA), with the world's
         code lists for countries and currencies in place of the defaults. Every
         value, and the list identifier where a document gives one, must pass.

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
WORLD_LISTS = {"CountryIdentificationCode", "CurrencyCode"}     # replaced by the world's lists in phase 2b


def doc_type(path):
    return etree.parse(path).getroot().tag.split("}")[1]


def phase1(path):
    xsd = os.path.join(UBL, "endorsed", "xsdrt", "maindoc", f"UBL-{doc_type(path)}-2.5.xsd")
    schema = etree.XMLSchema(etree.parse(xsd))
    ok = schema.validate(etree.parse(path))
    return [] if ok else [f"phase 1: line {e.line}: {e.message}" for e in schema.error_log]


def world_codes():
    """The codes of the world's country and currency lists (world/codelists)."""
    out = {}
    for short in WORLD_LISTS:
        gc = etree.parse(os.path.join(ROOT, "world", "codelists", f"{short}-2.4-world.gc"))
        ident = gc.find("Identification")
        list_id = next((ln.text for ln in ident.findall("LongName") if ln.get("Identifier") == "listID"), None)
        out[short] = {"codes": {r.findtext("Value[@ColumnRef='code']/SimpleValue") for r in gc.find("SimpleCodeList")},
                      "listID": list_id}
    return out


def phase2a(path, world_only):
    """UBL's own phase 2. Returns problems other than the expected failures on world codes."""
    with tempfile.TemporaryDirectory() as tmp:
        svrl = os.path.join(tmp, "svrl.xml")
        subprocess.run(["java", "-jar", os.path.join(UBL, "val", "saxon9he.jar"), f"-s:{path}",
                        f"-xsl:{os.path.join(UBL, 'val', 'UBL-DefaultDTQ-2.5.xsl')}", f"-o:{svrl}"],
                       check=True, capture_output=True)
        text = open(svrl, encoding="utf-8").read()
    problems, expected = [], 0
    for m in re.finditer(r"<svrl:failed-assert.*?<svrl:text>(.*?)</svrl:text>", text, re.S):
        msg = " ".join(m.group(1).split())
        v = re.search(r"Value supplied '([^']*)' is unacceptable for constraints identified by '([^']*)'", msg)
        if v and v.group(1) in world_only and v.group(2).split()[0].split("-")[0] in ("Currency", "CountryIdentification"):
            expected += 1
        else:
            problems.append(f"phase 2a (UBL default code lists): {msg}")
    return problems, expected


def phase2b(path, cva, world):
    """The UBL 2.5 CVA with the world's lists for countries and currencies."""
    tree = etree.parse(path)
    problems = []
    for ctx in cva["contexts"]:
        lists = [cva["lists"][v] for v in ctx["values"] if v in cva["lists"]]
        if not lists:
            continue
        short = lists[0]["short"]
        if short in WORLD_LISTS:
            allowed, ids = world[short]["codes"], {world[short]["listID"]}
        else:
            allowed = set().union(*(set(lst["codes"]) for lst in lists))
            ids = {lst["listID"] for lst in lists}
        for part in ctx["address"].split("|"):
            part = part.strip()
            # CVA addresses are Schematron rule contexts: a relative one matches anywhere, an absolute one as
            # written (UBL switches a context off with "/*[parent::*]", which matches nothing)
            xp = part if part.startswith("/") else "//" + part
            for node in tree.xpath(xp, namespaces=NS):
                value = node if isinstance(node, str) else node.text
                owner = node.getparent() if isinstance(node, str) else node
                where = tree.getpath(owner)
                if value not in allowed:
                    problems.append(f"phase 2b: {where}: '{value}' is not in {short}")
                list_id = None if isinstance(node, str) else node.get("listID")
                if list_id and list_id not in ids:
                    problems.append(f"phase 2b: {where}: listID '{list_id}' does not identify {short} "
                                    f"({', '.join(sorted(i for i in ids if i))})")
    return problems


def main(paths):
    cva = json.load(open(os.path.join(ROOT, "world", "codelists", "ubl-default-codes.json"), encoding="utf-8"))
    world = world_codes()
    world_only = (world["CountryIdentificationCode"]["codes"] | world["CurrencyCode"]["codes"]) - \
        {c for lst in cva["lists"].values() if lst["short"] in WORLD_LISTS for c in lst["codes"]}
    failed = 0
    for path in paths:
        problems = phase1(path)
        expected = 0
        if not problems:
            p2a, expected = phase2a(path, world_only)
            problems = p2a + phase2b(path, cva, world)
        name = os.path.relpath(path, ROOT)
        if problems:
            failed += 1
            print(f"{name}: INVALID")
            for p in problems:
                print(f"  {p}")
        else:
            print(f"{name}: valid (phase 1; phase 2 with the world's code lists; UBL's own phase 2 objects only "
                  f"to the world's {expected} country and currency codes)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
