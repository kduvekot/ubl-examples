#!/usr/bin/env python3
"""Build the UBL world pages from the world layers (tools/world_data.py).

  * <out>/world.html          the map (site/world.html with the data filled in)
  * <md-dir>/world-<id>.md    one Markdown page per party; tools/build_site.sh
                              turns these into HTML with the site template

Usage: python3 tools/build_world.py <out-dir> <md-dir>
"""
import json
import os
import re
import sys

out, mddir = sys.argv[1], sys.argv[2]
root = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402
import world_ids  # noqa: E402
import world_facts  # noqa: E402
world = world_facts.fill_world(world_data.load())   # {fact:…} in the published texts (stage 7 B2)
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
data = json.dumps({"countries": world["countries"], "parties": world["parties"], "routes": world["routes"], "speeds": world["speeds"],
                   "towns": world["towns"], "platforms": world.get("platforms", []), "model": model}, ensure_ascii=False, separators=(",", ":"))
assert "/*WORLD_JSON*/ null" in page
# as a string for JSON.parse: a browser reads a large JSON string much faster than the same data as a JavaScript
# object literal (the map's first frame, O152); "</" is escaped so that the string cannot end the <script>
literal = json.dumps(data, ensure_ascii=False).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
page = page.replace("/*WORLD_JSON*/ null", "JSON.parse(" + literal + ")")
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
        pr = i["price"]
        price = (f"{pr['rate_percent']} % of the insured value ({pr['cover_percent']} % of the CIF value, premium "
                 f"included), in {pr['currency']}, per {unit}" if "rate_percent" in pr      # a premium rate (O173)
                 else f"{money(pr)} per {unit}")
        rows = [("Seller's item ID", f"`{i['sellers_id']}`"), ("Price", price)]
        if i.get("resale_of"):
            o = ITEMS[i["resale_of"]]
            maker = o
            while maker.get("resale_of"):        # follow the resale chain to the maker
                maker = ITEMS[maker["resale_of"]]
            via = f", bought from {link(o['seller'])}" if o is not maker else ""
            ids = f"item number `{maker['standard_id']}` (ISO/IEC 15459), " if maker.get("standard_id") else ""
            ids += f"GTIN `{maker['gtin']}`, " if maker.get("gtin") else ""
            rows.append(("Resale of", f"{maker['name']} made by {link(maker['seller'])}{via}: {ids}maker's ID "
                                      f"`{maker['sellers_id']}`"))
        if i.get("gtin"):
            rows.append(("GTIN", f"`{i['gtin']}` (GS1, under the company prefix "
                                 f"`{PARTIES[i['seller']]['identity']['identification']['company_prefix']}`)"))
        if i.get("standard_id"):
            rows.append(("Standard item number", f"`{i['standard_id']}` (ISO/IEC 15459: the issuing agency code KXU of "
                                                 f"{link(world_items.ISSUER)}, the company number "
                                                 f"`{PARTIES[i['seller']]['identity']['identification']['codana_cin']}` "
                                                 "and the company's own reference)"))
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
        same = sum(1 for j in mine if j["name"] == i["name"]) > 1        # variants of one item: told apart by the seller's ID
        out += [f"### {i['name']}" + (f" (`{i['sellers_id']}`)" if same else ""), "", i.get("description", ""), "",
                "| | |", "|---|---|"]
        out += [f"| {k} | {v} |" for k, v in rows] + [""]
    return out

from lxml import etree as _et_gc  # noqa: E402


def _gc_names(name):
    """Code -> name of a published world code list (world/codelists/gc/<name>.gc)."""
    t = _et_gc.parse(os.path.join(root, "world", "codelists", "gc", name + ".gc")).getroot()
    out = {}
    for row in t.iter("Row"):
        vals = {v.get("ColumnRef"): v.findtext("SimpleValue") for v in row.findall("Value")}
        out[vals.get("code")] = vals.get("name")
    return out


ISIC, LANG = _gc_names("ISICRev4Code"), _gc_names("LanguageCode")


def fleet(p):
    """The party's vehicles, ships and aircraft as its documents name them (the people on board are not listed)."""
    if not p.get("fleet"):
        return []
    kinds = {"road": "Road vehicle", "rail": "Train", "inland": "Barge", "sea": "Ship", "air": "Aircraft"}
    rows = []
    for f in p["fleet"]:
        if f.get("vessel_id"):
            reg = f"`{f['vessel_id']}`" + (f", call sign `{f['call_sign']}`" if f.get("call_sign") else "")
        elif f.get("plate"):
            reg = f"`{f['plate']}`"
        elif isinstance(f.get("aircraft"), str):
            reg = f"`{f['aircraft']}`"
        elif f.get("train"):
            reg = f"train `{f['train']}`"
        else:
            reg = ""
        rows.append(f"| {f['name']} | {kinds.get(f['kind'], f['kind'])} | {reg} |")
        if f.get("ore_train"):          # the ore train shares the carrier's wagon record with its container train
            rows.append(f"| {f.get('ore_train_name', 'Ore train')} | {kinds['rail']} | train `{f['ore_train']}` |")
    return ["## Fleet", "", "| Name | Kind | Registration |", "|---|---|---|"] + rows + [""]


def identity(p):
    idn, c = p["identity"], world["countries"][p["c"]]
    rows = [("Name", idn["name"])]
    if idn.get("trade_name"):
        rows.append(("Trade name", idn["trade_name"]))
    lg = idn.get("legal") or {}
    if lg.get("form"):
        form = c.get("legal_forms", {}).get(lg["form"], {})
        rows.append(("Legal form", form.get("name", lg["form"])))
    if lg.get("founded"):
        rows.append(("Founded", lg["founded"]))
    if lg.get("headcount"):
        rows.append(("Employees", f"{lg['headcount']:,}"))
    if lg.get("capital") and c.get("legal_forms", {}).get(lg.get("form"), {}).get("capital_on_documents"):
        rows.append(("Share capital", f"{lg['capital']:,} {c['currency']['name']}"))
    if lg.get("listing"):
        rows.append(("Listed on", f"{lg['listing']['market']}, ISIN `{lg['listing']['id']}`"))
    if idn.get("industry"):
        rows.append(("Industry", f"`{idn['industry']}` {ISIC.get(idn['industry'], '')} (ISIC Rev.4)"))
    if idn.get("staff"):                                   # a public body's staff (OW031)
        rows.append(("Staff", f"about {idn['staff']:,}"))
    owner = ((p.get("wiki") or {}).get("facts") or {}).get("Owner")
    if owner:                                              # as the Encyclopedia's infobox gives it (SR2-09, B-15)
        rows.append(("Owner", re.sub(r"\[\[([^]|]+)(?:\|([^]]+))?\]\]", lambda m: m.group(2) or m.group(1), owner)))
    if idn.get("language"):
        langs = idn["language"] if isinstance(idn["language"], list) else [idn["language"]]
        names = [LANG.get(code, code) for code in langs]
        rows.append(("Language", names[0] if len(names) == 1 else
                     f"{names[0]} at home; {names[1]} with the other countries of the Accord and abroad"))
    ident = idn.get("identification") or {}
    if ident.get("convention") == "GS1":
        rows.append(("Identification", f"GS1 company prefix `{ident['company_prefix']}`, GLN `{ident['gln']}`"))
    elif ident.get("convention") == "ISO":
        rows.append(("Identification", f"company number `{ident['codana_cin']}` at {link(world_items.ISSUER)}, "
                                       "for item and package numbers under ISO/IEC 15459"))
    if idn.get("customs_id"):
        rows.append(("Customs trader number", f"`{idn['customs_id']}`"))
    if idn.get("website"):
        rows.append(("Website", idn["website"]))
    if idn.get("registry_id"):
        rows.append(("Registry number", f"`{idn['registry_id']}` ({world_ids.register_of(world, p)[1]['name']})"))
    if idn.get("tax_id"):
        scheme = c["tax"]["schemes"][0]
        rows.append(("Tax number", f"`{idn['tax_id']}` ({scheme['name']}, `{scheme['id']}`)"))
    for cc, tid in sorted(idn.get("tax_abroad", {}).items()):    # registered for the tax of another country
        abroad = world["countries"][cc]
        sch = abroad["tax"]["schemes"][0]
        rows.append((f"Tax number in {abroad['name']}", f"`{tid}` ({sch['name']}, `{sch['id']}`)"))
    rows.append(("Address", "<br>".join(address_lines(p))))
    if idn.get("endpoint"):
        rows.append(("Electronic address", f"`{idn['endpoint']}`"))
    if idn.get("contact"):
        rows.append(("Contact", f"{idn['contact']['name']}, `{idn['contact']['email']}`"))
    if idn.get("account"):
        acc = idn["account"]
        rows.append(("Account", f"`{acc['number']}` at {link(acc['bank'])}"))
    if idn.get("account_abroad"):
        acc = idn["account_abroad"]
        rows.append(("Account abroad", f"`{acc['number']}` at {link(acc['bank'])}: {acc['why']}"))
    if idn.get("bic"):
        rows.append(("Bank identifier", f"`{idn['bic']}` (ISO 9362 structure); branches: "
                                        + ", ".join(f"`{b['id']}` {b['name']}" for b in idn["branches"])))
    held = [q for q in world["parties"] if p["id"] in (q.get("identity", {}).get(k, {}).get("bank")
                                                         for k in ("account", "account_abroad"))]
    if held:
        rows.append(("Holds the accounts of", ", ".join(link(q["id"]) for q in held)))
    cur = c["currency"]
    rows.append((f"In {c['name']}", f"Currency: {cur['name']} (`{cur['code']}`). Taxes: {c['tax']['summary']}"))
    return ["## Identity", "", "| | |", "|---|---|"] + [f"| {k} | {v} |" for k, v in rows] + [""]

ABROAD = {p["id"]: p for p in world.get("abroad", [])}     # makers outside the world (O229): no page, no map


def link(pid):
    if pid in ABROAD:
        p = ABROAD[pid]
        return f"{label(p)} ({world['abroad_countries'][p['c']]['name']})"
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
    n = d["nn"]
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
    meta = (f"*{p['name']} · {c['name']} ({p['c']}) · "
            f"<span class=\"kind kind-{p['cat']}\">{CATEGORY[p['cat']]}</span>*")
    lines += [meta, "", p["what"], ""] + identity(p) + fleet(p) + sells(p) + ["## How UBL helps", "", p["how"], ""]
    n = lambda k: len(v[k])
    if n("sends") or n("receives") or n("mentioned"):
        cnt = lambda k, verb: f"{verb} {n(k)} document{'s' if n(k) != 1 else ''}" if n(k) else ""
        parts_ = [x for x in (cnt("sends", "sends"), cnt("receives", "receives")) if x]
        named = (f"is named in {n('mentioned')} document{'s' if n('mentioned') != 1 else ''} between other parties"
                 if n("mentioned") else "")
        said = " and ".join(parts_) + (", and " if parts_ and named else "") + named
        lines += [f"In this world it {said}. They are listed per flow below.", ""]
        lines += by_flow(v, p["id"])
    if v["elements"]:
        lines += ["## UBL party elements", "", "The party elements in which this party appears:", "",
                  " ".join(f"`{e}`" for e in v["elements"]), ""]
    if v["partners"]:
        lines += ["## Trading partners in the world", "",
                  "The parties it exchanges documents with:", ""]
        lines += [f"- {link(q)}" + ("" if q in ABROAD else f", {world['countries'][parties[q]['c']]['name']}") for q in v["partners"]] + [""]
    lines += ["## In the world", "",
              f"[See {p['name']} on the map](world.html#{p['id']}) · "
              f"{c['name']}: {c['note']}", "",
              "*Who sends and who receives each document follows the UBL 2.5 model of the documents and their "
              "party elements.*", ""]
    open(os.path.join(mddir, f"world-{p['id']}.md"), "w", encoding="utf-8").write("\n".join(lines))
# The parties: an index by country and kind
TOWN = lambda p: p["identity"].get("address", {}).get("CityName", "")
pt = ["# Parties", "",
      "The companies, carriers, ports, banks and public bodies of the world, and the people who trade with them. "
      "Each page tells what the party does, how it identifies itself, and every document it sends, receives or is "
      "named in. On [the map](world.html) each one stands in its town.", ""]
for cc, c in world["countries"].items():
    ps = [p for p in world["parties"] if p["c"] == cc]
    if not ps:
        continue
    pt += [f"## {c['name']}", "", "| Party | Role | Town | Kind |", "|---|---|---|---|"]
    for p in sorted(ps, key=lambda p: (list(CATEGORY).index(p["cat"]), label(p))):
        pt.append(f"| [{label(p)}](world-{p['id']}.html) | {p['name']} | {TOWN(p)} | "
                  f"<span class=\"kind kind-{p['cat']}\">{CATEGORY[p['cat']]}</span> |")
    pt.append("")
open(os.path.join(mddir, "parties.md"), "w", encoding="utf-8").write("\n".join(pt))

# The code lists of the world: an index of the published genericode files
from lxml import etree as _et  # noqa: E402
cl = ["# Code lists", "",
      "The code lists the documents of the world use, each published as a genericode file at the address its "
      "documents give. Where a document uses a real external list (UN/EDIFACT, ISO, the WCO's Harmonized System and "
      "others), the world's file holds the codes it uses, with the list's own identifier; the Trade Accord's and the "
      "countries' own lists are the world's. "
      "[The context/value association](codelists/UBL-World-2.5.cva) binds each code element of UBL 2.5 to its list, "
      "as UBL's own validation does.", "",
      "The lists of countries and currencies extend UBL's default lists of version 2.4 with the codes of the "
      "world's three countries and their currencies.", "",
      "| List | listID | Agency | Codes | File |", "|---|---|---|---:|---|"]
_gc = "{http://docs.oasis-open.org/codelist/ns/genericode/1.0/}"
_files = sorted(os.path.join("codelists", f) for f in os.listdir(os.path.join(root, "world", "codelists")) if f.endswith(".gc"))
_files += sorted(os.path.join("codelists", "gc", f) for f in os.listdir(os.path.join(root, "world", "codelists", "gc"))
                 if f.endswith(".gc"))
for rel in _files:
    t = _et.parse(os.path.join(root, "world", rel)).getroot()
    ident = t.find("Identification")
    names = ident.findall("LongName")
    name = next((n.text for n in names if n.get("Identifier") is None), ident.findtext("ShortName"))
    lid = next((n.text for n in names if n.get("Identifier") == "listID"), ident.findtext("CanonicalUri"))
    agency = ident.findtext("Agency/LongName") or ""
    codes = len(t.findall("SimpleCodeList/Row"))
    cl.append(f"| {name} | `{lid}` | {agency} | {codes} | [{os.path.basename(rel)}]({rel}) |")
cl.append("")
open(os.path.join(mddir, "world-codelists.md"), "w", encoding="utf-8").write("\n".join(cl))

# The examples: an index of the flows that have example documents
ex_lines = ["# Trade", "",
            "The flows of trade in the world, from the ore at the mine to the bench in the park, the cotton bale and the "
            "power on the grid. Each flow is told as a story, with the documents its parties exchange, in UBL 2.5. "
            "Every document is valid against the UBL 2.5 schemas and the world's code lists, and every value in it "
            "comes with the reason why it is that value. The parties, items, currencies and taxes agree from one "
            "document to the next and with the rest of the world.", "",
            "Each document names the specifications it follows in `CustomizationID` and `ProfileID`: see "
            "[the rules of the Trade Accord](world-specifications.html).", ""]
# Each flow in the order of its story: by the documents' issue date and time (the file numbers are internal)
from lxml import etree as _etree  # noqa: E402


def issued(d):
    """When the document was issued, from its XML: (date, time)."""
    xml = os.path.join(root, "world", "examples", d["flow"], f"{d['nn']:02d}-{d['doc']}.xml")
    r = _etree.parse(xml).getroot()
    date = r.findtext("{*}IssueDate") or r.findtext("{*}RequestDate") or ""
    return date, r.findtext("{*}IssueTime") or ""


import world_specs as _ws  # noqa: E402
story = {}         # flow id -> its documents with an example page, in story order
for f in world["flows"]:
    docs = [x for x in world["documents"] if x["flow"] == f["id"] and example_of(x)]
    story[f["id"]] = sorted(docs, key=lambda x: (*issued(x), x["nn"]))
ex_lines += ["## Contents", "", "| Flow | Documents |", "|---|---:|"]   # a contents list, in the page's order
ex_lines += [f"| [{f['title']}](#flow-{f['id']}) | {len(story[f['id']])} |" for f in world["flows"] if story[f["id"]]]
ex_lines += [""]
for f in world["flows"]:
    rows = story[f["id"]]
    if not rows:
        continue
    ex_lines += [f'<a id="flow-{f["id"]}"></a>', "", f"## {f['title']}", "", f["text"], "",
                 "| Issued | Document | From | To |", "|---|---|---|---|"]
    for x in rows:
        ex_lines.append(f"| {issued(x)[0].replace('-', '\u2011')} | [{world_docs.words(x['doc'])}]({example_of(x)}) | {link(x['from'])} | "
                        f"{link(x['to'])} |")
    ex_lines.append("")

# The example pages: each document's page (world/examples/<flow>/NN-Doc.md) with its place in the story, the way to
# the documents before and after it, its parties and the specification it claims
# A party's own data (its identifiers, name, language, address, legal entity, tax scheme, contact and electronic
# address) is the same in every document: on an example page it is folded under one line that says whose data it is,
# and each value keeps its reason without repeating whose it is. The document's own values stay in view.
PARTY_DATA = {"PartyIdentification", "AdditionalPartyIdentification", "PartyName", "Language", "PostalAddress",
              "PartyLegalEntity", "PartyTaxScheme", "Contact", "ElectronicAddress", "EndpointID", "WebsiteURI",
              "LogoReferenceID", "IndustryClassificationCode"}
BY_NAME = {label(p): p["id"] for p in world["parties"]}


def fold_party_data(lines):
    """Fold the party's own data in every block of an example page: the values under a party (the block's own party,
    `Party/…` under a customer or supplier party, or `DeliveryParty/…` inside another aggregate)."""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        i += 1
        if not re.match(r"Inside `[^`]*`:$", line):
            continue
        items, cur = [], None                    # the block's bullets, each with its continuation lines
        while i < len(lines) and not lines[i].startswith("#") and not lines[i].startswith("Inside `"):
            l = lines[i]
            if l.startswith("- `"):
                cur = [l]; items.append(cur)
            elif cur is not None and l.startswith("  "):
                cur.append(l)
            elif l.strip():
                items.append([l]); cur = None
            i += 1

        def owner(it):
            """The path of the party a value belongs to ("" for the block's own party), or None."""
            mm = re.match(r"- `([^`=]+)`", it[0])
            segs = mm.group(1).split("/") if mm else []
            for k, seg in enumerate(segs):
                if seg in PARTY_DATA:
                    pre = segs[:k]
                    return "/".join(pre) if all(x.endswith("Party") for x in pre) else None
            return None
        groups = {}
        for it in items:
            o = owner(it)
            if o is not None:
                groups.setdefault(o, []).append(it)
        placed, body = set(), [""]
        for it in items:
            o = owner(it)
            grp = groups.get(o) if o is not None else None
            name = next((re.search(r"\*\*(.+?)\*\*", x[0]).group(1) for x in grp
                         if re.match(r"- `([^`]*/)?PartyName/Name`", x[0])), None) if grp else None
            if grp is None or len(grp) < 3 or not name:
                body += it
                continue
            if o in placed:
                continue
            placed.add(o)
            gives = re.compile(rf"(?:;\s*as|\.?\s*As) {re.escape(name)} gives it\.?")
            tidy = lambda l: re.sub(r"\.\.", ".", gives.sub(".", l))
            who = f"[{name}](world-{BY_NAME[name]}.html)" if name in BY_NAME else name
            where = f" in <code>{o}</code>" if o else ""
            body += ["", "<details>", f"<summary>The party's own data{where}, as {name} gives it ({len(grp)} values)</summary>", ""]
            for x in grp:
                body += [tidy(l) for l in x]
            body += ["", f"The same in every document {who} is named in.", "", "</details>", ""]
        out += body + [""]
    return out


exdir = os.path.join(out, ".example-md")
for f in world["flows"]:
    rows = story[f["id"]]
    for i, x in enumerate(rows):
        name = f"{x['nn']:02d}-{x['doc']}"
        src = open(os.path.join(root, "world", "examples", f["id"], name + ".md"), encoding="utf-8").read()
        head = f"*Example {x['nn']} of the flow \"{f['title']}\" · "
        assert head in src, (f["id"], name)
        flow_link = f"[{f['title']}](examples.html#flow-{f['id']})"
        prev = (f"[← {world_docs.words(rows[i - 1]['doc'])}]({example_of(rows[i - 1])})" if i else "")
        nxt = (f"[{world_docs.words(rows[i + 1]['doc'])} →]({example_of(rows[i + 1])})" if i + 1 < len(rows) else "")
        nav = " · ".join(v for v in (prev, f"all documents of the flow", nxt) if v)
        nav = nav.replace("all documents of the flow", f"[all documents of the flow](examples.html#flow-{f['id']})")
        t = _ws.transaction(x)
        spec = f"[{_ws.load()['transactions'][t]['name']}](world-spec-transaction-{t}.html)"
        src = src.replace(head, f"*Document {i + 1} of {len(rows)} in the flow {flow_link} · ", 1)
        lines = src.split("\n")
        at = next(k for k, l in enumerate(lines) if l.startswith("*Document "))
        lines[at + 1:at + 1] = ["", f"From {link(x['from'])} to {link(x['to'])}, under the Trade Accord's "
                                    f"transaction {spec}.", "", nav]
        lines = fold_party_data(lines)
        lines += ["", "---", "", nav, ""]
        os.makedirs(os.path.join(exdir, f["id"]), exist_ok=True)
        open(os.path.join(exdir, f["id"], name + ".md"), "w", encoding="utf-8").write("\n".join(lines))
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
    # the document's own claims only: the root's children, not the specifications a digital agreement or capability
    # names inside it
    for e in etree.parse(path).getroot().iterchildren("{*}CustomizationID", "{*}ProfileID"):
        for part in e.text.split(world_specs.COMPLIANT):
            used.setdefault(part, []).append((flow, name))


DOC_OF = {(d["flow"], f"{d['nn']:02d}-{d['doc']}"): d for d in world["documents"]}


def example_label(flow, name):
    d = DOC_OF[(flow, name)]
    nm = lambda pid: label(parties[pid]) if pid in parties else label(ABROAD[pid]) if pid in ABROAD else pid
    return (f"[{world_docs.words(d['doc'])}, {nm(d['from'])} to {nm(d['to'])}](example-{flow}-{name}.html) "
            f"({flows[flow]['title'] if flow in flows else flow})")


def transaction_detail(ex):
    """What the examples of a transaction show: who sends it to whom, the code lists and identifier schemes its
    documents use. Made from the examples at every build."""
    pairs, lists, schemes = {}, {}, {}
    for flow, name in ex:
        d = DOC_OF[(flow, name)]
        role = lambda pid: parties[pid]["name"] if pid in parties else "a supplier abroad"
        pairs.setdefault((role(d["from"]), role(d["to"])), []).append((flow, name))
        root_el = etree.parse(os.path.join(root, "world", "examples", flow, name + ".xml")).getroot()
        for e in root_el.iter():
            if not isinstance(e.tag, str):
                continue
            local = etree.QName(e).localname
            if e.get("listID"):
                lists.setdefault(e.get("listID"), set()).add(local)
            if e.get("schemeID"):
                schemes.setdefault(e.get("schemeID"), set()).add(local)
    out = ["## Who sends it to whom", "", "| From | To | Examples |", "|---|---|---:|"]
    out += [f"| {a} | {b} | {len(v)} |" for (a, b), v in sorted(pairs.items())] + [""]
    if lists:
        out += ["## Code lists its documents use", "", "Each list is published on [the code lists page](world-codelists.html).",
                "", "| List (listID) | In the elements |", "|---|---|"]
        out += [f"| `{k}` | {', '.join(f'`{x}`' for x in sorted(v))} |" for k, v in sorted(lists.items())] + [""]
    if schemes:
        out += ["## Identifier schemes its documents use", "", "| Scheme (schemeID) | In the elements |", "|---|---|"]
        out += [f"| `{k}` | {', '.join(f'`{x}`' for x in sorted(v))} |" for k, v in sorted(schemes.items())] + [""]
    return out


def spec_page(level, key):
    return f"world-spec-{level}-{key.replace(':', '-')}"


specs = world_specs.described()
idx = ["# Rules of the Trade Accord", "",
       "How the documents of the world are made: the specifications they claim, below, and "
       "[the code lists](world-codelists.html) their codes come from.", "",
       "Every document of the world says which specifications it follows. `CustomizationID` names the transaction "
       "specification at up to three levels, chained with `#compliant#`: the Trade Accord's transaction, a national "
       "specification built on it, and a community's specification. `ProfileID` names the Accord's process profile "
       "the document belongs to.", ""]
for level, title in LEVELS.items():
    idx += [f"## {title}", "", "| Specification | Identifier | Document types |", "|---|---|---|"]
    for u, (lv, key, spec) in sorted(specs.items(), key=lambda kv: kv[1][2]["name"].lower()):   # by name
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
            if spec["when"] == "between_members":
                applies = "to the documents the members exchange among themselves"
            elif spec["when"] == "in_port":
                applies = ("to the documents of these types for goods that pass through the port, exchanged in "
                           f"{world['countries'][spec['country']]['name']} with a member taking part")
            else:
                applies = "to the documents of these types that a member sends or receives: every party of its procedures"
            lines += ["Members: " + ", ".join(link(m) for m in spec["members"]) + f". It applies {applies}"
                      + ", chained after the transaction and any national specification.", ""]
            lines += [f"Owner: {world_specs.load()['owner']['community']}. Version {world_specs.load()['version']}.", ""]
        else:
            owner = world_specs.load()["owner"][level]
            lines += [f"Owner: {owner}. Version {world_specs.load()['version']}.", ""]
        lines += [f"Document types: {kinds}.", ""]
        ex = used.get(u, [])
        if level == "transaction" and ex:
            lines += transaction_detail(ex)
        if ex:
            lines += ["## Examples that claim it", ""] + [f"- {example_label(f, n)}" for f, n in ex] + [""]
        open(os.path.join(mddir, spec_page(lv, key) + ".md"), "w", encoding="utf-8").write("\n".join(lines))
    idx.append("")
open(os.path.join(mddir, "world-specifications.md"), "w", encoding="utf-8").write("\n".join(idx))
print(f"world: map, {len(world['parties'])} party pages, {len(world['documents'])} documents")
