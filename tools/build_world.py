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
                   "towns": world["towns"], "platforms": world.get("platforms", []), "model": model}, ensure_ascii=False, separators=(",", ":"))
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
    fields = {k: [v] for k, v in a.items()}
    return world_data.address_lines(world["countries"][p["c"]]["address"], fields) + [world["countries"][p["c"]]["name"]]

import world_items  # noqa: E402
CODES = world_items.codes()
ITEMS = {i["id"]: i for i in world["items"]}
PARTIES = {p["id"]: p for p in world["parties"]}

def money(pr):
    cur = next(c["currency"] for c in world["countries"].values() if c["currency"]["code"] == pr["currency"])
    # a unit price keeps its own decimals when it is finer than the currency (27.3 ferra per kWh)
    own = len(f"{pr['amount']}".rstrip("0").split(".")[1]) if "." in f"{pr['amount']}" else 0
    return f"{pr['amount']:,.{max(cur['minor_units'], own)}f} {pr['currency']}"

def sells(p):
    mine = [i for i in world["items"] if i["seller"] == p["id"]]
    if not mine:
        return []
    units, packs = CODES["UnitOfMeasureCode"]["codes"], CODES["PackagingTypeCode"]["codes"]
    out = ["## What it sells", "",
           "Its items, as they appear on its quotations, catalogues and invoices. Units of measure and "
           "packaging types are UN/ECE Recommendation 20 and 21 codes from the UBL code lists; customs tariff "
           "codes are Harmonized System subheadings.", ""]
    for i in mine:
        unit = f"`{i['unit']}` ({units[i['unit']]})"
        rows = [("Seller's item ID", f"`{i['sellers_id']}`"), ("Price", f"{money(i['price'])} per {unit}")]
        if i.get("resale_of"):
            o = ITEMS[i["resale_of"]]
            maker = o
            while maker.get("resale_of"):        # follow the resale chain to the maker
                maker = ITEMS[maker["resale_of"]]
            via = f", bought from {link(o['seller'])}" if o is not maker else ""
            ids = f"Codana item number `{maker['standard_id']}`, " if maker.get("standard_id") else ""
            ids += f"GTIN `{maker['gtin']}`, " if maker.get("gtin") else ""
            rows.append(("Resale of", f"{maker['name']} made by {link(maker['seller'])}{via}: {ids}maker's ID "
                                      f"`{maker['sellers_id']}`"))
        if i.get("gtin"):
            rows.append(("GTIN", f"`{i['gtin']}` (GS1, under the company prefix "
                                 f"`{PARTIES[i['seller']]['identity']['identification']['company_prefix']}`)"))
        if i.get("standard_id"):
            rows.append(("Codana item number", f"`{i['standard_id']}` (issued by {link(world_items.ISSUER)})"))
        if i.get("hs"):
            rows.append(("Customs tariff (HS)", f"`{i['hs']}`; origin {world['countries'][i['origin']]['name']}"))
            rows.append(("Product classification (UN CPC Ver.2.1)", f"`{i['cpc']}`"))
        if i.get("dimensions_mm"):
            rows.append(("Dimensions", " × ".join(str(d) for d in i["dimensions_mm"]) + " mm"))
        if i.get("net_kg") and i["kind"] == "goods":
            rows.append(("Weight per unit", f"{i['net_kg']:g} kg net, {i['gross_kg']:g} kg gross"))
        if i.get("package"):
            pk = i["package"]
            per = f", {pk['per_package']} per package" if pk.get("per_package") else ""
            rows.append(("Packaging", f"`{pk['type']}` ({packs[pk['type']]}){per}"))
        if i.get("components"):
            def qty(c):
                u = ITEMS[c["item"]]["unit"]
                return f"{c['qty']:g} ×" if u in ("EA", "C62") else f"{c['qty']:g} {units[u].split(' (')[0]} of"
            rows.append(("Made with", ", ".join(f"{qty(c)} {ITEMS[c['item']]['name']} ({link(ITEMS[c['item']]['seller'])})"
                                                for c in i["components"])))
        out += [f"### {i['name']}", "", i.get("description", ""), "", "| | |", "|---|---|"]
        out += [f"| {k} | {v} |" for k, v in rows] + [""]
    return out

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
    if idn.get("bic"):
        rows.append(("Bank identifier", f"`{idn['bic']}` (ISO 9362 structure); branches: "
                                        + ", ".join(f"`{b['id']}` {b['name']}" for b in idn["branches"])))
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

def example_of(d):
    """The page of the example document for a document of the world, if it has one."""
    same = [x for x in world["documents"] if x["flow"] == d["flow"]]
    n = next(i for i, x in enumerate(same, 1) if x is d)
    md = os.path.join(root, "world", "examples", d["flow"], f"{n:02d}-{d['doc']}.md")
    return f"example-{d['flow']}-{n:02d}-{d['doc']}.html" if os.path.exists(md) else None

def entry(d, pid, kind):
    doc = f"[**{world_docs.words(d['doc'])}**]({world_docs.spec_link(d['doc'])})"
    if kind == "sends":
        head = f"{doc} to {link(d['to'])}"
    elif kind == "receives":
        head = f"{doc} from {link(d['from'])}"
    else:
        head = f"{doc} from {link(d['from'])} to {link(d['to'])}"
    ex = example_of(d)
    lines = [f"- {head}: {d['why']}" + (f" [See the example document]({ex})." if ex else ""), ""]
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
    lines += [meta, "", p["what"], ""] + identity(p) + sells(p) + ["## How UBL helps", "", p["how"], ""]
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
# The examples: an index of the flows that have example documents
ex_lines = ["# Example documents", "",
            "Real UBL 2.5 documents from the example world. Every document is valid against the UBL 2.5 schemas of "
            "the endorsed document types and against the world's code lists, and every value in it comes with the "
            "reason why it is that value. The documents are generated from the world's layers, so the parties, items, "
            "currencies and taxes in them agree with the rest of the world.", "",
            "These examples are kept apart from the examples of the OASIS UBL Technical Committee, whose history is "
            "in this repository's `xml/` folder.", "",
            "Each document names the specifications it follows in `CustomizationID` and `ProfileID`: see "
            "[the world's specifications](world-specifications.html).", ""]
for f in world["flows"]:
    same = [x for x in world["documents"] if x["flow"] == f["id"]]
    rows = [(n, x) for n, x in enumerate(same, 1) if example_of(x)]
    if not rows:
        continue
    ex_lines += [f"## {f['title']}", "", f["text"], "", "| | Document | From | To |", "|---|---|---|---|"]
    for n, x in rows:
        ex_lines.append(f"| {n} | [{world_docs.words(x['doc'])}]({example_of(x)}) | {link(x['from'])} | {link(x['to'])} |")
    ex_lines.append("")
open(os.path.join(mddir, "examples.md"), "w", encoding="utf-8").write("\n".join(ex_lines))

# The specifications the documents claim (world/specifications.json): an index and a short page for each
import glob  # noqa: E402
import world_specs  # noqa: E402
from lxml import etree  # noqa: E402
LEVELS = {"transaction": "Transactions of the Trade Accord", "national": "National specifications",
          "community": "Community specifications", "profile": "Process profiles"}
used = {}
for path in sorted(glob.glob(os.path.join(root, "world", "examples", "*", "*.xml"))):
    flow, name = path.split(os.sep)[-2], os.path.basename(path)[:-4]
    for e in etree.parse(path).getroot().iter("{*}CustomizationID", "{*}ProfileID"):
        for part in e.text.split(world_specs.COMPLIANT):
            used.setdefault(part, []).append((flow, name))


def spec_page(level, key):
    return f"world-spec-{level}-{key.replace(':', '-')}"


specs = world_specs.described()
idx = ["# Specifications", "",
       "Every document of the world says which specifications it follows. `CustomizationID` names the transaction "
       "specification at up to three levels, chained with `#compliant#`, as EN 16931, Peppol and XRechnung do: the "
       "Trade Accord's transaction, a national specification built on it, and a community's specification. "
       "`ProfileID` names the Accord's process profile the document belongs to. These are the specifications of the "
       "world; the world claims no compliance with real ones such as EN 16931.", ""]
for level, title in LEVELS.items():
    idx += [f"## {title}", "", "| Specification | Identifier | Document types |", "|---|---|---|"]
    for u, (lv, key, spec) in specs.items():
        if lv != level:
            continue
        kinds = ", ".join(spec.get("documents", [])) or "every document type the members exchange"
        idx.append(f"| [{spec['name']}]({spec_page(lv, key)}.html) | `{u}` | {kinds} |")
        single = {"transaction": "Transaction of the Trade Accord", "national": "National specification",
                  "community": "Community specification", "profile": "Process profile of the Trade Accord"}[level]
        lines = [f"# {spec['name']}", "", f"*{single} in the UBL example world · "
                 "[all specifications](world-specifications.html)*", "",
                 f"Identifier: `{u}`", "", spec["purpose"], ""]
        if level == "national":
            lines += [f"Owner: {spec['owner']}. It applies to {', '.join(spec['documents'])} "
                      + ("from a seller in " + world['countries'][spec['country']]['name'] if spec['when'].get('seller_country')
                         else "to a public body of " + world['countries'][spec['country']]['name'])
                      + ", on top of the Trade Accord's transaction, and is chained after it.", ""]
        elif level == "community":
            lines += ["Members: " + ", ".join(link(m) for m in spec["members"]) + ". It applies "
                      + ("to the documents the members exchange among themselves" if spec["when"] == "between_members"
                         else f"to the documents of these types in the flows {', '.join(spec['flows'])}")
                      + ", chained after the transaction and any national specification.", ""]
        else:
            owner = world_specs.load()["owner"][level]
            lines += [f"Owner: {owner}. Version {world_specs.load()['version']}.", ""]
        lines += [f"Document types: {kinds}.", ""]
        ex = used.get(u, [])
        if ex:
            lines += ["Examples that claim it:", ""] + [f"- [{f} {n}](example-{f}-{n}.html)" for f, n in ex] + [""]
        open(os.path.join(mddir, spec_page(lv, key) + ".md"), "w", encoding="utf-8").write("\n".join(lines))
    idx.append("")
open(os.path.join(mddir, "world-specifications.md"), "w", encoding="utf-8").write("\n".join(idx))
print(f"world: map, {len(world['parties'])} party pages, {len(world['documents'])} documents")
