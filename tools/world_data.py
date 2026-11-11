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
