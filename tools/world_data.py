#!/usr/bin/env python3
"""Load the UBL example world. The world is kept in one file per layer:

  world/countries.json   the countries: names, currencies, tax schemes, identifier and address schemes
  world/parties.json     the parties: place on the map, what they do, their identity
  world/map.json         routes, towns and fields of the map
  world/documents.json   the flows of documents between the parties
  world/items.json       the items the parties sell: goods and services
  world/ubl-model.json   generated from the UBL 2.5 model by tools/extract_ubl_model.py

load() merges the layers into one dictionary (countries, parties, routes, towns,
fields, flows, documents); every tool reads the world through it.
"""
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
LAYERS = ("countries", "parties", "map", "documents", "items")


def path(layer):
    return os.path.join(ROOT, "world", f"{layer}.json")


def load():
    world = {}
    for layer in LAYERS:
        data = json.load(open(path(layer), encoding="utf-8"))
        data.pop("description", None)
        world.update(data)
    return world


# parts of an address that are not on a line: they say something other than where the post goes
NOT_ON_A_LINE = ("ID", "AddressTypeCode", "AddressFormatCode", "CountrySubentityCode", "TimezoneOffset", "Country",
                 "LocationCoordinate", "AddressLine")


def address_lines(fmt, fields):
    """The lines of an address in a country's address format (countries.json, address.lines and line_rule).
    fields maps a field name to its texts: one per language, the national language first, then English.
    Every line of the address, in the documents and on the world pages, is made by this function."""
    placed = {t for line in fmt["lines"] for t in line.split()}
    unplaced = sorted(k for k, v in fields.items() if v and k not in placed and k not in NOT_ON_A_LINE)
    if unplaced:
        raise ValueError(f"the address format has no place for {', '.join(unplaced)}")
    out = []
    for line in fmt["lines"]:
        words = [" / ".join(fields[t]) for t in line.split() if fields.get(t)]
        if words:
            out.append(" ".join(words))
    return out


def save(layer, data):
    """Write one layer file in the format used throughout (indent 1, UTF-8)."""
    with open(path(layer), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


# ---------------------------------------------------------------- the world's invented languages
_WORLD = None


def _world():
    global _WORLD
    if _WORLD is None:
        _WORLD = load()
    return _WORLD


MISSING_WORDS = set()


def translate(text, code, street=False):
    """A text in Urvanian (qau) or Lisavan (qal): the world's invented languages, word by word from their fixed
    vocabularies (world/countries.json). Names, numbers and codes stay as they are; Lisavan has no articles."""
    lex = _world()["languages"][code].get("lexicon", {})
    out, start = [], True
    for tok in re.findall(r"[A-Za-z][A-Za-z'’]*|\S|\s+", text):
        if not tok[0].isalpha():
            out.append(tok)
            if tok in ".:;!?":
                start = True
            continue
        low = tok.lower()
        if tok in UNIT_SYMBOLS:              # a symbol of a unit stays as it is, as numbers do
            out.append(tok)
            start = False
            continue
        proper = (tok[0].isupper() and not start and not street) or tok in proper_names()
        start = False
        if proper:
            out.append(tok)
            continue
        if code == "qal" and low in ("the", "a", "an"):
            if out and out[-1].isspace():
                out.pop()
            if not out:
                start = True
            continue
        if low not in lex:
            MISSING_WORDS.add(low)
            out.append(tok)
            continue
        w = lex[low]
        out.append(w[0].upper() + w[1:] if tok[0].isupper() or street else w)
    t = "".join(out).strip()
    return t[0].upper() + t[1:] if t else t


def proper_names():
    """Words of names, which a translation keeps: parties, places, countries, currencies, languages, card schemes,
    and the brands and models of items."""
    global PROPER
    if PROPER is None:
        world = _world()
        names = [p["identity"]["name"] for p in world["parties"]] + [t["name"] for t in world["towns"]] + \
                [t["name"] for t in world.get("localities", [])] + \
                [c["name"] for c in world["countries"].values()] + \
                [c["currency"]["name"] for c in world["countries"].values()] + \
                [x["name"] for x in world["languages"].values()] + \
                [x["name"] for x in world.get("card_schemes", {}).values()] + \
                [i[k] for i in world.get("items", []) for k in ("brand", "model") if i.get(k)]
        PROPER = {w for n in names for w in re.findall(r"[A-Z][A-Za-z'’]*", n)} - COMMON_NAME_WORDS
    return PROPER


PROPER = None
UNIT_SYMBOLS = {"mm", "cm", "m", "km", "kg", "t", "kWh", "MWh", "GB"}     # SI and common unit symbols
COMMON_NAME_WORDS = set("""Accord Administration Agency Air Airport Bank Barges Board Border Brokers Cargo Chamber Coastal
Commerce Company Cotton Council Customs Department Distribution Energy Engineering Factoring Farm Forwarding Furniture
Gas Ginnery Grid Haulage Hub Identification Industries Information Insurance Intermodal Island Lines Logistics Maritime
Mill Mining Ocean Packaging Port Power Procurement Public Rail Recovery Review Sawmill Service State Stores Telecom
Terminal Textile Trade Trading Warehousing Water Works Coral Lume Ferra English""".split())   # ordinary words in names
