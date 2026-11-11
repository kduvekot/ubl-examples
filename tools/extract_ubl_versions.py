#!/usr/bin/env python3
"""Which UBL 2 version first defines each element: world/ubl-versions.json.

UBLVersionID "Identifies the earliest version of the UBL 2 schema for this document type that defines all of the
elements that might be encountered in the current instance." To give each example that version, this script reads
the published models of every UBL 2 version (the OASIS Standard stage of each) and records, for every aggregate
(ABIE) and each of its children (basic or association), the first version in which the aggregate has that child,
and for every document type the first version that has it.

Sources, from docs.oasis-open.org, each checked against its SHA-256:
  UBL 2.0   the schemas (xsd/maindoc/*.xsd and xsd/common/UBL-CommonAggregateComponents-2.0.xsd): UBL 2.0 published
            its model as spreadsheets only, and the schemas are generated from it
  UBL 2.1 to 2.5   the entity models (mod/UBL-Entities-<v>.gc), the source of their schemas

tools/build_examples.py reads world/ubl-versions.json and computes the UBLVersionID of each document.

Usage: python3 tools/extract_ubl_versions.py [cache-dir]     (downloads into the cache directory, default .ubl-versions)
"""
import hashlib
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://docs.oasis-open.org/ubl/"
MODELS = {   # version -> (path under BASE, sha256)
    "2.1": ("os-UBL-2.1/mod/UBL-Entities-2.1.gc", "3defa90e98881d3b4a8d1fc3940676f3c2d9e1a884a02b48ae84922df31d46f8"),
    "2.2": ("os-UBL-2.2/mod/UBL-Entities-2.2.gc", "b147f254be17cb89c73208622b631eca05c2f6e7ee1a51855cc151a8035d55da"),
    "2.3": ("os-UBL-2.3/mod/UBL-Entities-2.3.gc", "38374ff6ebe4a4ab0257c85a5bcf6ea0082beaac26f0ff5f0e51473ee1554254"),
    "2.4": ("os-UBL-2.4/mod/UBL-Entities-2.4.gc", "fa441eceec11cb5ba2bb38ac76a589eccad878e691bde998f7ce017ceee90913"),
    "2.5": ("os-UBL-2.5/mod/UBL-Entities-2.5.gc", "c7df070e1a2927792a8a85103665924973d2559552ea87aa495ea7248fe988d1"),
}
SCHEMAS_20 = "os-UBL-2.0/xsd/"
SCHEMAS_20_SHA256 = "d02af6b279f1f10a7ea2c41ba0b2535d2d23edab3ef464913b71d58e5e8c79c4"   # the maindoc schemas + CAC
VERSIONS = ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5"]
OUT = os.path.join(os.path.dirname(__file__), "..", "world", "ubl-versions.json")
XS = "{http://www.w3.org/2001/XMLSchema}"


def fetch(url, cache):
    path = os.path.join(cache, url[len(BASE):].replace("/", "_"))
    if not os.path.exists(path):
        with urllib.request.urlopen(url, timeout=300) as r, open(path, "wb") as f:
            f.write(r.read())
    return path


def gc_children(path):
    """(children per aggregate, document types) of a UBL entity model in genericode."""
    children, docs, current = {}, set(), None
    for _, el in ET.iterparse(path):
        if el.tag.rsplit("}", 1)[-1] != "Row":
            continue
        r = {v.get("ColumnRef"): (v.findtext("{*}SimpleValue") or v.findtext("SimpleValue") or "") for v in el}
        el.clear()
        name = r.get("ComponentName") or r.get("UBLName")      # UBL 2.1 calls the column UBLName
        if r.get("ComponentType") == "ABIE":
            current = name
            children.setdefault(current, set())
            if not r["ModelName"].startswith("UBL-CommonLibrary"):
                docs.add(current)
        elif r.get("ComponentType") in ("BBIE", "ASBIE"):
            children[current].add(name)
    return children, docs


def xsd_children(paths, maindoc):
    children, docs = {}, set()
    for path in paths:
        for ct in ET.parse(path).getroot().iter(f"{XS}complexType"):
            name = ct.get("name") or ""
            if not name.endswith("Type"):
                continue
            abie = name[:-4]
            if path in maindoc:
                docs.add(abie)
            kids = children.setdefault(abie, set())
            for e in ct.iter(f"{XS}element"):
                if e.get("ref"):
                    kids.add(e.get("ref").split(":")[-1])
    return children, docs


def main():
    cache = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", ".ubl-versions")
    os.makedirs(cache, exist_ok=True)
    sources, models = {}, {}
    listing = urllib.request.urlopen(BASE + SCHEMAS_20 + "maindoc/", timeout=120).read().decode()
    maindoc = [fetch(BASE + SCHEMAS_20 + "maindoc/" + f, cache)
               for f in sorted(set(re.findall(r'href="(UBL-[A-Za-z]+-2\.0\.xsd)"', listing)))]
    cac = fetch(BASE + SCHEMAS_20 + "common/UBL-CommonAggregateComponents-2.0.xsd", cache)
    models["2.0"] = xsd_children(maindoc + [cac], set(maindoc))
    digest = hashlib.sha256(b"".join(open(p, "rb").read() for p in maindoc + [cac])).hexdigest()
    if digest != SCHEMAS_20_SHA256:
        raise SystemExit(f"{SCHEMAS_20}: the UBL 2.0 schemas differ from the ones this script was written for")
    sources["2.0"] = {"url": BASE + SCHEMAS_20, "files": len(maindoc) + 1, "sha256": digest}
    for v, (rel, sha) in MODELS.items():
        path = fetch(BASE + rel, cache)
        digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
        if sha and digest != sha:
            raise SystemExit(f"{rel}: differs from the model this script was written for")
        models[v] = gc_children(path)
        sources[v] = {"url": BASE + rel, "sha256": digest}
    since, documents = {}, {}
    for v in VERSIONS:
        children, docs = models[v]
        for abie, kids in children.items():
            entry = since.setdefault(abie, {})
            for k in kids:
                entry.setdefault(k, v)
        for d in docs:
            documents.setdefault(d, v)
    out = {"description": "The first UBL 2 version that defines each child of each aggregate, and each document type, "
                          "made by tools/extract_ubl_versions.py from the published models of UBL 2.0 to 2.5.",
           "sources": sources, "documents": dict(sorted(documents.items())),
           "children": {a: dict(sorted(k.items())) for a, k in sorted(since.items())}}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=0, ensure_ascii=False)
        f.write("\n")
    print(f"world/ubl-versions.json: {len(documents)} document types, {sum(len(k) for k in since.values())} children")


if __name__ == "__main__":
    main()
