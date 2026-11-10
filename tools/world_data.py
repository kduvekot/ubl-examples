#!/usr/bin/env python3
"""Load the UBL example world. The world is kept in one file per layer:

  world/countries.json   the countries: names, currencies, tax schemes, identifier and address schemes
  world/parties.json     the parties: place on the map, what they do, their identity
  world/map.json         routes, towns and fields of the map
  world/documents.json   the flows of documents between the parties
  world/ubl-model.json   generated from the UBL 2.5 model by tools/extract_ubl_model.py

load() merges the layers into one dictionary (countries, parties, routes, towns,
fields, flows, documents); every tool reads the world through it.
"""
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
LAYERS = ("countries", "parties", "map", "documents")


def path(layer):
    return os.path.join(ROOT, "world", f"{layer}.json")


def load():
    world = {}
    for layer in LAYERS:
        data = json.load(open(path(layer), encoding="utf-8"))
        data.pop("description", None)
        world.update(data)
    return world


def save(layer, data):
    """Write one layer file in the format used throughout (indent 1, UTF-8)."""
    with open(path(layer), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")
