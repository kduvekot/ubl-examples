#!/usr/bin/env python3
"""Build the UBL world pages from world/world.json.

  * <out>/world.html          the map (site/world.html with the data filled in)
  * <md-dir>/world-<id>.md    one Markdown page per party; tools/build_site.sh
                              turns these into HTML with the site template

Usage: python3 tools/build_world.py <out-dir> <md-dir>
"""
import json
import os
import sys

out, mddir = sys.argv[1], sys.argv[2]
root = os.path.join(os.path.dirname(__file__), "..")
world = json.load(open(os.path.join(root, "world", "world.json"), encoding="utf-8"))
parties = {p["id"]: p for p in world["parties"]}

# The tile model: built and checked by tools/world_model.py (the build stops on problems)
sys.path.insert(0, os.path.dirname(__file__))
import world_model  # noqa: E402
model, problems = world_model.build(world)
if problems:
    sys.exit("world model problems:\n  " + "\n  ".join(problems))

# The map: fill in the data
page = open(os.path.join(root, "site", "world.html"), encoding="utf-8").read()
data = json.dumps({"countries": world["countries"], "parties": world["parties"], "routes": world["routes"],
                   "towns": world["towns"], "model": model}, ensure_ascii=False, separators=(",", ":"))
assert "/*WORLD_JSON*/ null" in page
page = page.replace("/*WORLD_JSON*/ null", data.replace("</", "<\\/"))
open(os.path.join(out, "world.html"), "w", encoding="utf-8").write(page)

CATEGORY = {"commerce": "Commerce", "logistics": "Logistics", "government": "Government",
            "finance": "Finance", "procurement": "Public procurement"}

def label(p):
    return f"#{p['n']} {p['name']}"

os.makedirs(mddir, exist_ok=True)
for p in world["parties"]:
    c = world["countries"][p["c"]]
    lines = [f"# {label(p)}", ""]
    meta = f"*{c['name']} ({p['c']}) · {CATEGORY[p['cat']]}*"
    if p.get("proposed"):
        meta += " · *proposed addition to the 26+C set*"
    lines += [meta, "", p["what"], "", "## How UBL helps", "", p["how"], ""]
    lines += ["## Documents it exchanges", ""] + [f"- {d.strip()}" for d in p["docs"].split(",")] + [""]
    lines += ["## UBL roles", "", "The party elements in which this party appears:", ""]
    lines += [f"- `{r.strip()}`" for r in p["roles"].split(",")] + [""]
    if p.get("partners"):
        lines += ["## Trading partners in the world", ""]
        for q in p["partners"]:
            o = parties[q]
            lines.append(f"- [{label(o)}](world-{o['id']}.html), {world['countries'][o['c']]['name']}")
        lines.append("")
    lines += ["## In the world", "",
              f"[See {p['name']} on the map](world.html#{p['id']}) · "
              f"{c['name']}: {c['note']}", "",
              "*Example documents for this party will follow as the example world is built.*", ""]
    open(os.path.join(mddir, f"world-{p['id']}.md"), "w", encoding="utf-8").write("\n".join(lines))
print(f"world: map and {len(world['parties'])} party pages")
