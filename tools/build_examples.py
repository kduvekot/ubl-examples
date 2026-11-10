#!/usr/bin/env python3
"""Generate the example UBL documents of the world, with the reason for every value.

For each document of a flow in world/documents.json this writes, into
world/examples/<flow>/:

  NN-<DocumentType>.xml   the UBL 2.5 instance
  NN-<DocumentType>.md    the same document with, for every value, its place
                          in the structure, the value and why it is that value

The documents are built from the world's layers, so they agree with them by
construction: the parties sit at the places world/documents.json gives them,
with the content of their identity (world/parties.json); items come from
world/items.json; amounts are computed and rounded to the minor unit of the
currency (world/countries.json). What a flow adds on top (dates, document
numbers, quantities) is in its scenario below, each value with its reason.

The structure follows the UBL 2.5 model (world/ubl-model.json): an element
the model does not know, or a deprecated one, stops the build; children are
written in the order of the model (basic properties before associations, as
the UBL naming and design rules require); every value must have a reason.

Usage: python3 tools/build_examples.py [flow...]            (write; default: every flow with examples)
       python3 tools/build_examples.py --check [flow...]    (are the committed examples up to date?)
"""
import datetime
import os
import sys
from decimal import ROUND_HALF_UP, Decimal

from lxml import etree

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402
import world_docs  # noqa: E402
import world_items  # noqa: E402

NS_CAC = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
NS_CBC = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
CUSTOMIZATION = "urn:ubl-examples:world"
DEPRECATED = "(Deprecated)"

WORLD = world_data.load()
MODEL = world_docs.load_model()
PARTY = {p["id"]: p for p in WORLD["parties"]}
ITEM = {i["id"]: i for i in WORLD["items"]}
CUR = {c["currency"]["code"]: c["currency"] for c in WORLD["countries"].values()}


# ---------------------------------------------------------------- values with reasons
class V:
    """A value with its reason, and optional attributes (currencyID, unitCode, schemeID ...)."""
    def __init__(self, value, why, **attrs):
        self.value, self.why, self.attrs = value, why, attrs


def money(amount, currency):
    """Round an amount to the minor unit of its currency."""
    q = Decimal(1).scaleb(-CUR[currency]["minor_units"])
    return Decimal(amount).quantize(q, rounding=ROUND_HALF_UP)


def amount(value, currency, why):
    return V(str(money(value, currency)), why, currencyID=currency)


def price(value, currency, why):
    """A unit price keeps its own decimals; it may be finer than the currency."""
    return V(format(Decimal(str(value)).normalize(), "f"), why, currencyID=currency)


def qty(value, unit, why):
    return V(format(Decimal(str(value)).normalize(), "f"), why, unitCode=unit)


# ---------------------------------------------------------------- blocks from the world's layers
def party(pid):
    """The content of a cac:Party element, from the identity layer."""
    p = PARTY[pid]
    idn, c = p["identity"], WORLD["countries"][p["c"]]
    src = f"identity of {idn['name']} (world/parties.json)"
    a = idn["address"]
    address = {"StreetName": V(a["StreetName"], f"Street of the postal address; {src}."),
               "BuildingNumber": V(a["BuildingNumber"], f"Building number of the postal address; {src}."),
               "CityName": V(a["CityName"], f"The town or locality nearest to the party's place on the map, in its "
                                            f"own country and state; {src}.")}
    if a.get("PostalZone"):
        address["PostalZone"] = V(a["PostalZone"], f"Postal code in {c['name']}'s format ({c['address']['postal_zone']}); {src}.")
    if a.get("CountrySubentity"):
        address["CountrySubentity"] = V(a["CountrySubentity"], f"The state, part of an address in federal {c['name']}; {src}.")
    address["Country"] = {"IdentificationCode": V(p["c"], f"{c['name']}: a user-assigned ISO 3166-1 code, in the world's "
                                                          "country code list (world/codelists).")}
    out = {"_pid": pid}
    if idn.get("registry_id"):
        out["PartyIdentification"] = {"ID": V(idn["registry_id"], f"The party's preferred identifier: its number in the "
                                              f"{c['registry']['name']}; {src}. Later mentions of the same party in "
                                              "this document repeat only this identifier and the name.",
                                              schemeID=register_scheme(p["c"]))}
    if idn.get("endpoint"):
        out["ElectronicAddress"] = {   # new in UBL 2.5; Party/EndpointID is deprecated
            "ExchangeNetworkID": V("urn:ubl-examples:world:network", "The network in which the address is registered: "
                                   "the world's own exchange network."),
            "ElectronicAddressID": V(idn["endpoint"], "The party's electronic address in that network: its country code and "
                                     f"registry number; {src}. UBL 2.5 carries it here; Party/EndpointID is deprecated.",
                                     schemeID="urn:ubl-examples:world:endpoint")}
    out["PartyName"] = {"Name": V(idn["name"], f"The trading name; {src}.")}
    out["PostalAddress"] = address
    if idn.get("tax_id"):
        scheme = c["tax"]["schemes"][0]
        out["PartyTaxScheme"] = {
            "CompanyID": V(idn["tax_id"], f"Tax number under {c['name']}'s {scheme['name'].lower()} "
                                          f"({c['tax_id']['format']}); {src}."),
            "TaxScheme": {"ID": V(scheme["id"], f"UN/EDIFACT 5153 code of {c['name']}'s {scheme['name'].lower()}.")}}
    if idn.get("registry_id"):
        out["PartyLegalEntity"] = {
            "RegistrationName": V(idn["name"], f"The name under which the party is registered; {src}."),
            "CompanyID": V(idn["registry_id"], f"Number in the {c['registry']['name']}; {src}.")}
    if idn.get("contact"):
        out["Contact"] = {"Name": V(idn["contact"]["name"], f"The department that handles this document; {src}."),
                          "ElectronicMail": V(idn["contact"]["email"], "E-mail under the reserved .example domain "
                                                                       f"(RFC 2606), so it cannot reach anyone; {src}.")}
    return out


def register_scheme(country):
    return f"urn:ubl-examples:world:{country}:register"


def party_again(pid, first):
    """A later mention of a party already given in full in this document: its identifier and name only."""
    idn = PARTY[pid]["identity"]
    why = f"The same party as at {first}, where its full details are given; only its identifier and name are repeated."
    out = {"PartyName": {"Name": V(idn["name"], why)}}
    if idn.get("registry_id"):
        out["PartyIdentification"] = {"ID": V(idn["registry_id"], why, schemeID=register_scheme(PARTY[pid]["c"]))}
    return out


def institution(pid):
    """The content of a cac:FinancialInstitution element, for a bank of the world."""
    p = PARTY[pid]
    idn = p["identity"]
    src = f"identity of {idn['name']} (world/parties.json)"
    return {"_bank": pid,
            "ID": V(idn["bank_code"], f"The bank code, the part of every account number that names the bank; {src}."),
            "Name": V(idn["name"], f"The bank; {src}.")}


def institution_again(pid, first):
    return {"ID": V(PARTY[pid]["identity"]["bank_code"], f"The same bank as at {first}, where its name is given; "
                                                          "only its code is repeated.")}


def account(pid, why):
    """The content of a cac:FinancialAccount element for the account of a party."""
    acc = PARTY[pid]["identity"]["account"]
    return {"ID": V(acc["number"], f"{why} The number follows the structure of ISO 13616 with its check digits, with the "
                                   "world's country code; it is not called an IBAN, because the world's countries are "
                                   "not registered IBAN countries.", schemeID="urn:ubl-examples:world:account"),
            "FinancialInstitutionBranch": {"FinancialInstitution": institution(acc["bank"])}}


def item(iid, tax=None):
    """The content of a cac:Item element, from the items layer."""
    it = ITEM[iid]
    src = f"item {it['id']} of {PARTY[it['seller']]['identity']['name']} (world/items.json)"
    out = {"Description": V(it["description"], f"The seller's description; {src}."),
           "Name": V(it["name"], f"The item's short name; {src}."),
           "SellersItemIdentification": {"ID": V(it["sellers_id"], f"The seller's own item number; {src}.")}}
    if it.get("resale_of"):        # a resold item carries the maker's identifiers, customs code and origin
        orig = ITEM[it["resale_of"]]
        while orig.get("resale_of"):
            orig = ITEM[orig["resale_of"]]
        maker = PARTY[orig["seller"]]["identity"]["name"]
        out["ManufacturersItemIdentification"] = {"ID": V(orig["sellers_id"], f"The item number of the maker, {maker}: "
                                                          f"the reseller's item is resale of item {orig['id']} "
                                                          "(world/items.json).")}
        it = {**it, "standard_id": orig.get("standard_id"), "hs": orig.get("hs"), "origin": orig.get("origin")}
        src = f"item {orig['id']} of {maker}, which this item resells (world/items.json)"
    if it.get("standard_id"):
        out["StandardItemIdentification"] = {"ID": V(it["standard_id"], "The world item number issued by the identifier "
                                                     "issuing agency, twelve digits with a check digit; a scheme of the "
                                                     f"world, not a GTIN; {src}.", schemeID="urn:ubl-examples:world:item")}
    if it.get("hs"):
        out["CommodityClassification"] = {"ItemClassificationCode": V(it["hs"], "Harmonized System subheading of the "
                                                                      f"World Customs Organization; {src}.", listID="HS")}
    if tax:
        out["ClassifiedTaxCategory"] = tax
    if it.get("origin"):
        out["OriginCountry"] = {"IdentificationCode": V(it["origin"], f"Where the item was produced; {src}.")}
    return out


def tax_category(code, percent, why, scheme="VAT", country="XU"):
    c = WORLD["countries"][country]
    return {"ID": V(code, why), "Percent": V(str(percent), f"The rate of {c['name']}'s "
                                             f"{c['tax']['schemes'][0]['name'].lower()} for this category (world/countries.json)."),
            "TaxScheme": {"ID": V(scheme, f"UN/EDIFACT 5153 code of {c['name']}'s {c['tax']['schemes'][0]['name'].lower()}.")}}


# ---------------------------------------------------------------- placing the world's parties
def place_parties(doc, content):
    """Put every party of the world's document at its path, as cac:Party or as a wrapper around it."""
    for path, pid in doc["parties"].items():
        steps = path.split("/")
        node, abie = content, doc["doc"]
        for k, step in enumerate(steps):
            assoc = next(a for a in MODEL["abies"][abie]["asbies"] if a[0] == step)
            target = assoc[1]
            last = k == len(steps) - 1
            if isinstance(node.get(step), list) and not last:     # into every repetition, e.g. each catalogue line
                for sub in node[step]:
                    place_parties({"doc": target, "parties": {"/".join(steps[k + 1:]): pid}}, sub)
                break
            if last and isinstance(pid, list):                   # several parties in one role: one element each
                node[step] = [party(x) if target == "Party" else {"Party": party(x)} for x in pid]
                break
            if last:
                if target == "Party":
                    block = party(pid)
                elif target == "FinancialInstitution":
                    block = institution(pid)
                else:                                   # a wrapper such as SupplierParty, CustomerParty
                    block = {"Party": party(pid)}
                node[step] = merge(node.get(step, {}), block)
            else:
                node = node.setdefault(step, {})
            abie = target
    return content


def merge(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = merge(out[k], v) if isinstance(out.get(k), dict) and isinstance(v, dict) else v
    return out


# ---------------------------------------------------------------- writing XML in the order of the model
def build(doc_type, content):
    nsmap = {None: f"urn:oasis:names:specification:ubl:schema:xsd:{doc_type}-2", "cac": NS_CAC, "cbc": NS_CBC}
    root = etree.Element(f"{{{nsmap[None]}}}{doc_type}", nsmap=nsmap)
    reasons = []
    fill(root, doc_type, content, doc_type, reasons, {})
    return root, reasons


def fill(el, abie, content, path, reasons, seen):
    """Write content under el. seen records where each party and bank was first given in full: in document
    order, a later mention of the same party (or bank) holds only its identifier and name (or code)."""
    spec = MODEL["abies"][abie]
    bbies = {b[0]: b for b in spec["bbies"]}
    asbies = {a[0]: a for a in spec["asbies"]}
    content = {k: v for k, v in content.items() if not k.startswith("_")}
    for name in content:
        if name not in bbies and name not in asbies:
            raise SystemExit(f"{path}/{name}: not in the UBL 2.5 model")
    for name, card in [(b[0], b[1]) for b in spec["bbies"]] + [(a[0], a[2]) for a in spec["asbies"]]:
        if card.startswith("1") and name not in content and name not in ("UBLVersionID",):
            raise SystemExit(f"{path}/{name}: mandatory in UBL 2.5 ({card}) but missing")
    for name in [b[0] for b in spec["bbies"]]:                    # basic properties first, in model order
        if name not in content:
            continue
        if bbies[name][2]:
            raise SystemExit(f"{path}/{name}: deprecated in UBL 2.5")
        for v in content[name] if isinstance(content[name], list) else [content[name]]:
            if not isinstance(v, V) or not v.why:
                raise SystemExit(f"{path}/{name}: every value needs a reason")
            e = etree.SubElement(el, f"{{{NS_CBC}}}{name}", {k: str(x) for k, x in v.attrs.items()})
            e.text = str(v.value)
            reasons.append((f"{path}/{name}", e.text, v.attrs, v.why))
    for name in [a[0] for a in spec["asbies"]]:                   # then the associations, in model order
        if name not in content:
            continue
        a = asbies[name]
        if a[3].startswith(DEPRECATED) or MODEL["abies"][a[1]]["deprecated"]:
            raise SystemExit(f"{path}/{name}: deprecated in UBL 2.5")
        for sub in content[name] if isinstance(content[name], list) else [content[name]]:
            here = f"{path}/{name}"
            for key, again in (("_pid", party_again), ("_bank", institution_again)):
                if key in sub:
                    if sub[key] in seen:
                        sub = again(sub[key], seen[sub[key]].split("/", 1)[1])
                    else:
                        seen[sub[key]] = here
            e = etree.SubElement(el, f"{{{NS_CAC}}}{name}")
            fill(e, a[1], sub, here, reasons, seen)
            if len(e) == 0:
                raise SystemExit(f"{path}/{name}: empty element (UBL rule IND5)")


# ---------------------------------------------------------------- the reason pages
def page(n, doc, root, reasons, flow):
    sender, receiver = PARTY[doc["from"]]["identity"]["name"], PARTY[doc["to"]]["identity"]["name"]
    title = f"{world_docs.words(doc['doc'])}: {sender} to {receiver}"
    xml = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8").decode()
    lines = [f"# {title}", "",
             f"*Example {n} of the flow \"{flow['title']}\" · [{world_docs.words(doc['doc'])} in the UBL 2.5 "
             f"specification]({world_docs.spec_link(doc['doc'])})*", "",
             doc["why"], "",
             f"[The XML file]({os.path.basename(xmlname(n, doc))}) is valid against the UBL 2.5 schemas and the world's "
             "code lists. Below, every value with its place in the document and the reason for it.", "",
             "## Values and their reasons", ""]
    # grouped by the part of the document they belong to: the header, then each association at the top level
    groups = {}
    for path, value, attrs, why in reasons:
        steps = path.split("/")[1:]
        key = steps[0] if len(steps) > 1 else ""
        groups.setdefault(key, []).append(("/".join(steps[1:]) if key else steps[0], value, attrs, why))
    for key, rows in groups.items():
        lines += [f"### {world_docs.words(key) if key else 'The document itself'}", ""]
        if key:
            lines += [f"Inside `{key}`:", ""]
        for place, value, attrs, why in rows:
            extra = "".join(f" ({k} `{x}`)" for k, x in attrs.items())
            lines.append(f"- `{place}` = **{value}**{extra}  ")
            lines.append(f"  {why}")
        lines.append("")
    lines += ["## The document", "", "```xml", xml.rstrip(), "```", ""]
    return "\n".join(lines)


def xmlname(n, doc):
    return f"{n:02d}-{doc['doc']}.xml"


def main(flow_id, check=False):
    import examples_scenarios
    flow = next(f for f in WORLD["flows"] if f["id"] == flow_id)
    docs = [d for d in WORLD["documents"] if d["flow"] == flow_id]
    scenario = examples_scenarios.SCENARIOS[flow_id]
    out = os.path.join(world_data.ROOT, "world", "examples", flow_id)
    os.makedirs(out, exist_ok=True)
    stale = []
    for n, doc in enumerate(docs, 1):
        content = scenario(n, doc)
        content = place_parties(doc, content)
        for path, value in doc.get("values", {}).items():   # the world's manifest values must be what the scenario says
            node = content
            for step in path.split("/")[:-1]:
                node = node[step]
            got = node.get(path.split("/")[-1])
            if not isinstance(got, V) or got.value != value:
                raise SystemExit(f"{flow_id} {n} {doc['doc']}: {path} must be {value} (world/documents.json)")
        header = {"UBLVersionID": V("2.5", "The documents of the world use UBL 2.5."),
                  "CustomizationID": V(CUSTOMIZATION, "The example world is a customization of UBL: it uses its own "
                                                      "code lists for countries and currencies.")}
        root, reasons = build(doc["doc"], merge(header, content))
        files = {xmlname(n, doc): etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8"),
                 xmlname(n, doc).replace(".xml", ".md"): page(n, doc, root, reasons, flow).encode("utf-8")}
        for name, data in files.items():
            path = os.path.join(out, name)
            if check:
                if not os.path.exists(path) or open(path, "rb").read() != data:
                    stale.append(f"world/examples/{flow_id}/{name}")
            else:
                with open(path, "wb") as f:
                    f.write(data)
        if not check:
            print(f"world/examples/{flow_id}/{xmlname(n, doc)}: {len(reasons)} values")
    produced = {xmlname(n, d) for n, d in enumerate(docs, 1)} | {xmlname(n, d).replace(".xml", ".md")
                                                                  for n, d in enumerate(docs, 1)}
    for name in sorted(os.listdir(out)):                 # files of documents that are no longer in the flow
        if name not in produced:
            if check:
                stale.append(f"world/examples/{flow_id}/{name} (no longer a document of the flow)")
            else:
                os.remove(os.path.join(out, name))
    if check:
        print("\n".join(f"out of date: {s} (run tools/build_examples.py {flow_id})" for s in stale)
              or f"examples of flow {flow_id}: up to date")
        return not stale
    return True


FLOWS_WITH_EXAMPLES = ["ore", "road", "rail", "plastics", "retail", "sea", "air", "cotton", "tender", "carnet",
                       "waste", "utilities", "wood", "furniture", "packaging"]


if __name__ == "__main__":
    import build_examples        # run through the module, so the scenarios share its classes
    args = [a for a in sys.argv[1:] if a != "--check"]
    ok = all([build_examples.main(f, check="--check" in sys.argv) for f in (args or FLOWS_WITH_EXAMPLES)])
    sys.exit(0 if ok else 1)
