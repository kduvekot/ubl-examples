#!/usr/bin/env python3
"""The code lists of the UBL example world, as one model: which list every code element uses, and the codes of
every list.

The source is world/codelists/lists.json:

  lists      every list the world uses, by key:
               scope "regional"   a list of the Lumeport Trade Accord, valid in all three countries;
                                  listID urn:ubl-examples:world:codelist:<Name>Code
               scope "XU" | "XB" | "XL"   a national list of one country;
                                  listID urn:ubl-examples:world:<CC>:codelist:<Name>Code
               scope "external"   a world copy of a real list (UN/EDIFACT, ISO, IMO ...), with the listID in the
                                  standard's own text style; its codes come from the copy of the list in
                                  world/codelists/sources where there is one, never invented
               scope "ubl-copy"   a world copy of a UBL default list, given a listID (UBL's has none, or a broken
                                  one)
               scope "ubl"        a UBL 2.5 default list, used as it is (world/codelists/ubl-default-codes.json)
               scope "world-ubl"  the world's copies of UBL's country and currency lists (world/codelists/*.gc)
  bindings   which list(s) a code element uses: by element name, optionally only under certain parent elements
             (split elements: one element, several meanings) or only when a sibling has a value (allowances and
             charges); a binding with several lists lets the listID choose among them
  unlisted   the code elements that have no list on purpose, with the reason (codes a party defines for itself)

tools/build_codelists.py writes the genericode files and the world's context/value associations from this model;
tools/build_examples.py uses it to give every code its listID and to check every code against its list. Phase 2
of tools/validate_examples.py reads only the generated files, so it checks the documents independently.
"""
import csv
import json
import os
import re
import xml.etree.ElementTree as ET

import world_data

SRC = os.path.join(world_data.ROOT, "world", "codelists")
SOURCES = os.path.join(SRC, "sources")
REGIONAL = "urn:ubl-examples:world:codelist:{}Code"
NATIONAL = "urn:ubl-examples:world:{}:codelist:{}Code"
LANGS = {"regional": ["qau", "qal"], "XU": ["qau"], "XB": [], "XL": ["qal"]}
_MODEL = None


def short_name(key):
    """The genericode ShortName of a list: its concept name followed by Code."""
    return key.split(":")[-1] + "Code"


def list_id(key, spec):
    if spec["scope"] == "regional":
        return REGIONAL.format(key)
    if spec["scope"] in ("XU", "XB", "XL"):
        return NATIONAL.format(spec["scope"], key.split(":")[-1])
    return spec.get("listID")


# ---------------------------------------------------------------- reading the sources of external lists
def _cefact(path):
    d = json.load(open(path, encoding="utf-8"))
    return {v["value"]: {"name": v["comment"]} for v in d["values"]}


def _peppol(path):
    root = ET.parse(path).getroot()
    ns = {"c": root.tag.split("}")[0][1:]}
    return {c.findtext("c:Id", namespaces=ns): {"name": c.findtext("c:Name", namespaces=ns),
                                               "description": c.findtext("c:Description", namespaces=ns) or ""}
            for c in root.findall("c:Code", ns)}


def _cpc(path):
    with open(path, encoding="cp1252") as f:     # the UN Statistics Division's text file is in Windows-1252
        return {r["CPC21code"]: {"name": r["CPC21title"]} for r in csv.DictReader(f)}


def _iso639(path):
    """The ISO 639-2 table of the Library of Congress: alpha-3 bibliographic|terminologic|alpha-2|English|French.
    Every code becomes its own entry, lower case; the local-use range qaa-qtz is not a code."""
    out = {}
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            b, t, a2, en, fr = line.rstrip("\n").split("|")
            if "-" in b:
                continue
            for code, kind in ((b, "ISO 639-2 bibliographic code" if t else "ISO 639-2 code"),
                               (t, "ISO 639-2 terminologic code"), (a2, "ISO 639-1 code")):
                if code and code not in out:
                    out[code] = {"name": en, "description": f"{kind}; in French: {fr}"}
    return out


def _mic(path):
    with open(path, encoding="utf-8-sig") as f:
        return {r["MIC"]: {"name": r["MARKET NAME-INSTITUTION DESCRIPTION"].strip(),
                           "description": f"{r['ISO COUNTRY CODE (ISO 3166)']}, {r['STATUS'].lower()}"}
                for r in csv.DictReader(f)}


def _pronom(paths):
    out = {}
    for p in paths:
        x = open(p, encoding="utf-8").read()
        ids = dict((t, i) for i, t in re.findall(r"<Identifier>([^<]+)</Identifier>\s*<IdentifierType>([^<]+)<", x))
        name = re.search(r"<FormatName>([^<]+)", x).group(1).strip()
        version = re.search(r"<FormatVersion>([^<]+)", x).group(1).strip()
        out[ids["PUID"]] = {"name": f"{name}, version {version}", "mime": ids.get("MIME", "")}
    return out


def _epsg(path):
    d = json.load(open(path, encoding="utf-8"))
    return {str(d["Code"]): {"name": d["Name"], "description": f"{d['Kind']} coordinate reference system"}}


def _rec28(path):
    """UN/ECE Recommendation 28, code list Revision 4.2: the CSV made once from UNECE's spreadsheet (see
    world/codelists/sources/PROVENANCE.md), so the build needs no spreadsheet reader."""
    with open(path, encoding="utf-8") as f:
        return {r["code"]: {"name": r["name"], "description": r["description"]} for r in csv.DictReader(f)}


def _optd_aircraft(path):
    """OpenTravelData's table of IATA aircraft type codes (a secondary source: IATA SSIM Appendix A is not public)."""
    with open(path, encoding="utf-8") as f:
        return {r["iata_code"]: {"name": r["model"] if r["model"].startswith(r["manufacturer"])
                                 else f"{r['manufacturer']} {r['model']}",
                                 "description": f"ICAO type designator {r['icao_code']}; {r['nb_engines']} engines."}
                for r in csv.DictReader(f, delimiter="^")}


READERS = {"rec28": _rec28, "optd-aircraft": _optd_aircraft, "cefact": _cefact, "peppol": _peppol, "cpc": _cpc, "iso639": _iso639, "mic": _mic, "epsg": _epsg}


def source_codes(spec):
    src = spec["source"]
    if src["format"] == "pronom":
        return _pronom([os.path.join(SOURCES, f) for f in src["files"]])
    return READERS[src["format"]](os.path.join(SOURCES, src["file"]))


# ---------------------------------------------------------------- the model
def ubl_lists():
    return json.load(open(os.path.join(SRC, "ubl-default-codes.json"), encoding="utf-8"))["lists"]


def _gc_codes(path):
    root = ET.parse(path).getroot()
    ident = root.find("Identification")
    lid = next((ln.text for ln in ident.findall("LongName") if ln.get("Identifier") == "listID"), None)
    codes = {}
    for r in root.find("SimpleCodeList"):
        vals = {v.get("ColumnRef"): v.findtext("SimpleValue") for v in r}
        codes[vals["code"]] = {"name": vals.get("name", "")}
    return lid, codes


def load():
    """Every list with its codes resolved: {key: {scope, listID, name, codes: {code: {name, description, ...}}}}."""
    global _MODEL
    if _MODEL is not None:
        return _MODEL
    data = json.load(open(os.path.join(SRC, "lists.json"), encoding="utf-8"))
    ubl = ubl_lists()
    lists = {}
    for key, spec in data["lists"].items():
        lst = dict(spec)
        scope = spec["scope"]
        if scope in ("ubl", "ubl-copy"):
            u = ubl[spec["ubl"]]
            codes = {c: {"name": u["names"].get(c, "")} for c in u["codes"]}
            lst["listID"] = u["listID"] if scope == "ubl" else spec["listID"]
            lst["uri"] = u["uri"]
            lst.setdefault("name", spec.get("name") or u["short"])
        elif scope == "world-ubl":
            lid, codes = _gc_codes(os.path.join(SRC, spec["file"]))
            lst["listID"] = lid
        elif scope == "external" and spec.get("source"):
            available = source_codes(spec)
            wanted = spec.get("codes", "all")
            codes = {}
            for c in (available if wanted == "all" else wanted):
                if c not in available:
                    raise SystemExit(f"world/codelists/lists.json: {key}: {c} is not in the source "
                                     f"{spec['source'].get('file') or spec['source'].get('files')}")
                codes[c] = dict(available[c])
                if wanted != "all" and isinstance(wanted, dict) and wanted[c]:
                    codes[c]["description"] = wanted[c]
            for c, extra in spec.get("add", {}).items():   # local additions a standard leaves to its users
                codes[c] = {"name": extra[0], "description": extra[1], "added": True}
        else:
            codes = {c: {"name": v[0], "description": v[1] if len(v) > 1 else ""} for c, v in spec["codes"].items()}
        lst["codes"] = codes
        lst["listID"] = list_id(key, lst)
        lst["key"] = key
        lists[key] = lst
    bindings = []
    for b in data["bindings"]:
        b = dict(b)
        b["lists"] = b["list"] if isinstance(b["list"], list) else [b["list"]]
        for k in b["lists"]:
            if k not in lists:
                raise SystemExit(f"world/codelists/lists.json: binding of {b['element']} names an unknown list {k}")
        bindings.append(b)
    # the specific bindings (under given parents, or with a condition) come before the general ones
    bindings.sort(key=lambda b: (not (b.get("parents") or b.get("when")),))
    _MODEL = {"lists": lists, "bindings": bindings, "unlisted": data["unlisted"], "attributes": data["attributes"],
              "pending": data.get("pending", [])}
    return _MODEL


def binding(element, parent, siblings=None):
    """The binding for a code element under a parent element (its local name); siblings maps the names of the
    parent's other basic elements to their values (for a binding with a condition). None if unbound."""
    for b in load()["bindings"]:
        if b["element"] != element:
            continue
        if b.get("parents") and parent not in b["parents"]:
            continue
        if b.get("when") and any((siblings or {}).get(k) != v for k, v in b["when"].items()):
            continue
        return b
    return None


def id_bound(element):
    """Whether an identifier element (not a ...Code) holds codes of a list in some context (decision ID-Q2)."""
    return any(b["element"] == element and b.get("attribute") == "schemeID" for b in load()["bindings"])


def choose(b, code, list_id_given=None):
    """The list of a binding that holds the code: the one the listID names, else the first that has the code."""
    lists = load()["lists"]
    for k in b["lists"]:
        lst = lists[k]
        if list_id_given and lst["listID"] != list_id_given:
            continue
        if code in lst["codes"]:
            return lst
    return None


def describe(lst):
    """Where a list comes from, in words, for the reason pages."""
    s = lst["scope"]
    name = lst["name"] if lst["name"][:2].isupper() else lst["name"].lower()     # keep an acronym: UBL document type
    if s == "regional":
        return f"the Trade Accord's {name} list"
    if s in ("XU", "XB", "XL"):
        return f"{world_data.load()['countries'][s]['name']}'s national {name} list"
    if s == "external":
        return f"the world's copy of {lst['name']}"
    if s == "ubl-copy":
        return f"the world's copy of UBL's {lst['name']} list, with a listID"
    if s == "world-ubl":
        return f"the world's copy of UBL's {lst['name']} list"
    return f"UBL's default {lst['name']} list"


def name_in(lst, code, lang):
    """The name of a code in one of the world's languages: English as in the list, the invented languages word by
    word (world_data.translate)."""
    name = lst["codes"][code]["name"]
    return name if lang == "en" else world_data.translate(name, lang)


def entity_size(headcount, turnover, currency):
    """The Trade Accord's size class of an enterprise (lists.json, EntitySize): the smallest class whose limits it
    keeps, for both its headcount and its yearly turnover in its own currency."""
    from decimal import Decimal
    lst = load()["lists"]["EntitySize"]
    for code, t in lst["thresholds"].items():
        if headcount < t["headcount"] and Decimal(turnover) <= Decimal(t["turnover"][currency]):
            return code
    return "LARGE"
