#!/usr/bin/env python3
"""Build the UBL world pages from the world layers (tools/world_data.py).

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
sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402
world = world_data.load()
parties = {p["id"]: p for p in world["parties"]}

# The tile model: built and checked by tools/world_model.py (the build stops on problems)
sys.path.insert(0, os.path.dirname(__file__))
import world_model  # noqa: E402
model, problems = world_model.build(world)
if problems:
    sys.exit("world model problems:\n  " + "\n  ".join(problems))

# The documents: checked against the UBL 2.5 model by tools/world_docs.py
import world_docs  # noqa: E402
model_ubl = world_docs.load_model()
problems = world_docs.check(world, model_ubl)
if problems:
    sys.exit("world document problems:\n  " + "\n  ".join(problems))
view = world_docs.views(world, model_ubl)
uniq = lambda xs: ", ".join(dict.fromkeys(world_docs.words(x) for x in xs)) or "–"
for p in world["parties"]:
    v = view[p["id"]]
    p["sends"] = uniq(d["doc"] for d in v["sends"])
    p["receives"] = uniq(d["doc"] for d in v["receives"])
    p["roles"] = ", ".join(v["elements"])
    p["label"] = p["identity"]["name"]

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
    return p["identity"]["name"]

def address_lines(p):
    """The postal address in the format of the party's country (world/countries.json)."""
    a = p["identity"]["address"]
    fmt = world["countries"][p["c"]]["address"]["lines"]
    out = []
    for line in fmt:
        words = [a.get(k, "") for k in line.split()]
        out.append(" ".join(w for w in words if w))
    return out + [world["countries"][p["c"]]["name"]]

def identity(p):
    idn, c = p["identity"], world["countries"][p["c"]]
    rows = [("Name", idn["name"])]
    if idn.get("registry_id"):
        rows.append(("Registry number", f"`{idn['registry_id']}` ({c['registry']['name']})"))
    if idn.get("tax_id"):
        scheme = c["tax"]["schemes"][0]
        rows.append(("Tax number", f"`{idn['tax_id']}` ({scheme['name']}, `{scheme['id']}`)"))
    rows.append(("Address", "<br>".join(address_lines(p))))
    if idn.get("endpoint"):
        rows.append(("Electronic address", f"`{idn['endpoint']}`"))
    if idn.get("contact"):
        rows.append(("Contact", f"{idn['contact']['name']}, `{idn['contact']['email']}`"))
    if idn.get("account"):
        acc = idn["account"]
        rows.append(("Account", f"`{acc['number']}` at {link(acc['bank'])}"))
    if idn.get("bank_code"):
        rows.append(("Bank code", f"`{idn['bank_code']}`"))
    held = [q for q in world["parties"] if q.get("identity", {}).get("account", {}).get("bank") == p["id"]]
    if held:
        rows.append(("Holds the accounts of", ", ".join(link(q["id"]) for q in held)))
    cur = c["currency"]
    rows.append((f"In {c['name']}", f"Currency: {cur['name']} (`{cur['code']}`). Taxes: {c['tax']['summary']}"))
    return ["## Identity", "", "| | |", "|---|---|"] + [f"| {k} | {v} |" for k, v in rows] + [""]

def link(pid):
    return f"[{label(parties[pid])}](world-{pid}.html)"

flows = {f["id"]: f for f in world["flows"]}

def as_roles(d, pid):
    return ", ".join(f"`{x}`" for x in world_docs.fills(d, pid)) or "no party element of its own"

def others(d, pid):
    """The other parties a document mentions, with their place in it."""
    rows = []
    for path, v in d["parties"].items():
        for o in world_docs.ids(v):
            if o != pid and o not in (d["from"], d["to"]):
                rows.append(f"{link(o)} as `{path}`")
    return rows

def entry(d, pid, kind):
    doc = f"[**{world_docs.words(d['doc'])}**]({world_docs.spec_link(d['doc'])})"
    if kind == "sends":
        head = f"{doc} to {link(d['to'])}"
    elif kind == "receives":
        head = f"{doc} from {link(d['from'])}"
    else:
        head = f"{doc} from {link(d['from'])} to {link(d['to'])}"
    lines = [f"- {head}: {d['why']}", ""]
    me = f"  In it as {as_roles(d, pid)}"
    agent = d.get("sends_for") if kind == "sends" else d.get("receives_for") if kind == "receives" else None
    if agent:
        principal = world_docs.ids(d["parties"][agent])[0]
        me += f", on behalf of {link(principal)} (`{agent}`)"
    if kind == "mentioned":
        defs = [world_docs.definition(model_ubl, d, x) for x in world_docs.fills(d, pid)]
        me += "".join(f" ({x.rstrip('.')})" for x in defs if x)
    lines.append(me + ".")
    rest = others(d, pid)
    if rest:
        lines += ["", "  Also mentions: " + "; ".join(rest) + "."]
    return lines + [""]

KINDS = (("sends", "Sends"), ("receives", "Receives"), ("mentioned", "Is named in documents between others"))

def by_flow(v, pid):
    """One section per flow the party takes part in: what it sends, receives and is named in."""
    out = []
    for fid, f in flows.items():
        parts = [(kind, title, [d for d in v[kind] if d["flow"] == fid]) for kind, title in KINDS]
        if not any(docs for _, _, docs in parts):
            continue
        out += [f"## {f['title']}", "", f["text"], ""]
        for kind, title, docs in parts:
            if docs:
                out += [f"**{title}**", ""]
                for d in docs:
                    out += entry(d, pid, kind)
    return out

os.makedirs(mddir, exist_ok=True)
for p in world["parties"]:
    c = world["countries"][p["c"]]
    v = view[p["id"]]
    lines = [f"# {label(p)}", ""]
    meta = f"*#{p['n']} {p['name']} · {c['name']} ({p['c']}) · {CATEGORY[p['cat']]}*"
    if p.get("proposed"):
        meta += " · *proposed addition to the 26+C set*"
    lines += [meta, "", p["what"], ""] + identity(p) + ["## How UBL helps", "", p["how"], ""]
    n = lambda k: len(v[k])
    lines += [f"In this world it sends {n('sends')} and receives {n('receives')} documents, and is named in "
              f"{n('mentioned')} documents between other parties. They are listed per flow below.", ""]
    lines += by_flow(v, p["id"])
    lines += ["## UBL party elements", "", "The party elements in which this party appears:", "",
              " ".join(f"`{e}`" for e in v["elements"]), ""]
    if v["partners"]:
        lines += ["## Trading partners in the world", "",
                  "The parties it exchanges documents with:", ""]
        lines += [f"- {link(q)}, {world['countries'][parties[q]['c']]['name']}" for q in v["partners"]] + [""]
    lines += ["## In the world", "",
              f"[See {p['name']} on the map](world.html#{p['id']}) · "
              f"{c['name']}: {c['note']}", "",
              "*Who sends and who receives each document type follows the UBL 2.5 semantic model "
              "(the SenderParty and ReceiverParty elements and the definitions of the documents and their party "
              "elements), completed by the party role table of the UBL specification where the model does not say it. "
              "Every place named in a document is checked against the UBL 2.5 structure.*", ""]
    open(os.path.join(mddir, f"world-{p['id']}.md"), "w", encoding="utf-8").write("\n".join(lines))
print(f"world: map, {len(world['parties'])} party pages, {len(world['documents'])} documents")
