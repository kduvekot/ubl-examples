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
def party(pid, short=False):
    """The content of a cac:Party element, from the identity layer. short: identifier and name only, for a party
    referred to from inside another party's block (its service provider, shareholder or agent)."""
    if short:
        return party_again(pid, None)
    p = PARTY[pid]
    idn, c = p["identity"], WORLD["countries"][p["c"]]
    src = f"identity of {idn['name']} (world/parties.json)"
    out = {"_pid": pid}
    if idn.get("website"):
        out["WebsiteURI"] = V(idn["website"], f"The party's website, under the reserved .example domain (RFC 2606); {src}.")
    if idn.get("logo"):
        out["LogoReferenceID"] = V(idn["logo"], f"The reference of the logo the store prints on its documents; {src}.")
    if idn.get("industry"):
        out["IndustryClassificationCode"] = V(idn["industry"], f"What the party does, as an ISIC Rev. 4 class of the "
                                                               f"United Nations' industry classification; {src}.",
                                              listID="ISIC Rev.4")
    if idn.get("registry_id"):
        out["PartyIdentification"] = {"ID": V(idn["registry_id"], f"The party's preferred identifier: its number in the "
                                              f"{c['registry']['name']}; {src}. Later mentions of the same party in "
                                              "this document repeat only this identifier and the name.",
                                              schemeID=register_scheme(p["c"]))}
    if idn.get("customs_id"):
        out["AdditionalPartyIdentification"] = {"ID": V(idn["customs_id"], "A second identifier: the party's customs "
                                                        f"trader number, because it imports or exports ({c['customs_trader_format']}); "
                                                        f"{src}.", schemeID=f"urn:ubl-examples:world:{p['c']}:customs-trader")}
    out["PartyName"] = {"Name": V(idn["name"], f"The trading name; {src}.")}
    if idn.get("trade_name"):
        out["TradePartyName"] = {"Name": V(idn["trade_name"], f"The name the shops trade under, shorter than the company's "
                                                             f"name; {src}.")}
    if idn.get("language"):
        out["Language"] = {"ID": V("en", "English, the language the party does business in."),
                           "Name": V("English", "The language's name."),
                           "LocaleCode": V(idn["language"], "The language as a code of UBL's language code list (ISO 639).")}
    out["PostalAddress"] = address(pid)
    if idn.get("site"):
        out["PhysicalLocation"] = location(pid)
    if idn.get("tax_id"):
        scheme = c["tax"]["schemes"][0]
        tax = {"RegistrationName": V(legal_name(pid), f"The name under which the party is registered for "
                                                      f"{scheme['name'].lower()}; {src}."),
               "CompanyID": V(idn["tax_id"], f"Tax number under {c['name']}'s {scheme['name'].lower()} "
                                             f"({c['tax_id']['format']}); {src}."),
               "TaxLevelCode": V("State" if scheme.get("levied_by") == "state" else "National",
                                 f"The level of government that levies the tax: {c['name']}'s "
                                 f"{scheme['name'].lower()} is levied by the "
                                 f"{'states' if scheme.get('levied_by') == 'state' else 'country'}.")}
        if idn.get("tax_exemption"):
            tax["ExemptionReason"] = V(idn["tax_exemption"], f"Why purchases by this party carry no sales tax; {src}.")
        juris = {"Country": {"IdentificationCode": V(p["c"], "The country whose tax this is.")}}
        if scheme.get("levied_by") == "state":
            juris = {"CountrySubentity": V(idn["address"]["CountrySubentity"], "The state whose sales tax the party is "
                                           "registered for."), **juris}
        tax["TaxScheme"] = {"ID": V(scheme["id"], f"UN/EDIFACT 5153 code of {c['name']}'s {scheme['name'].lower()}."),
                            "CurrencyCode": V(c["currency"]["code"], "The tax is accounted for in the country's "
                                                                     "currency."),
                            "JurisdictionRegionAddress": juris}
        out["PartyTaxScheme"] = tax
    if idn.get("registry_id"):
        out["PartyLegalEntity"] = legal_entity(pid)
    if idn.get("contact"):
        ct = idn["contact"]
        contact = {"Name": V(ct["name"], f"The desk that handles this document; {src}.")}
        if ct.get("department"):
            contact["Department"] = V(ct["department"], f"The department the desk belongs to; {src}.")
        if ct.get("telephone"):
            contact["Telephone"] = V(ct["telephone"], "Telephone under +999, a country code the ITU keeps in reserve "
                                                      f"(ITU-T E.164), so the number reaches no one; {src}.")
        if ct.get("telefax"):
            contact["Telefax"] = V(ct["telefax"], f"The customs office still lists a fax number; {src}.")
        contact["ElectronicMail"] = V(ct["email"], "E-mail under the reserved .example domain (RFC 2606), so it cannot "
                                                   f"reach anyone; {src}.")
        if ct.get("hours"):
            contact["Note"] = V(ct["hours"], f"When the desk can be reached; {src}.")
        out["Contact"] = contact
    if idn.get("person_name"):
        out["Person"] = {"FirstName": V(idn["person_name"]["first"], f"The consumer's first name; {src}."),
                         "FamilyName": V(idn["person_name"]["family"], f"The consumer's family name; {src}.")}
    if idn.get("service_provider"):
        sp = idn["service_provider"]
        out["ServiceProviderParty"] = {"ServiceType": V(sp["type"], f"What the service provider does for the party; "
                                                                    f"{src}."),
                                       "Party": party(sp["party"], short=True)}
    if idn.get("authorization"):
        au = idn["authorization"]
        out["PartyAuthorization"] = {"Purpose": V(au["purpose"], f"What the authority has authorized the party to do; "
                                                                 f"{src}."),
                                     "ValidityPeriod": {"EndDate": V(au["valid_until"], "The authorization expires on "
                                                                                        "this date.")},
                                     "Certificate": {"ID": V(au["certificate"], "The number of the permit."),
                                                     "CertificateTypeCode": V("Permit", "A permit issued by an authority "
                                                                                        "of the party's country."),
                                                     "CertificateType": V("Operating permit", "The kind of certificate, "
                                                                                              "in words.")}}
    if idn.get("shop_website"):
        out["AdditionalWebSite"] = {"Name": V("Online shop", "The store's second website, where consumers buy."),
                                    "URI": V(idn["shop_website"], "Under the reserved .example domain.")}
    if idn.get("social"):
        so = idn["social"]
        out["SocialMediaProfile"] = {"Name": V(so["name"], "The store's profile name."),
                                     "SocialMediaTypeCode": V(so["type"], "The kind of social medium."),
                                     "URI": V(so["uri"], "The profile's address, under the reserved .example domain.")}
    out["_keys"] = set(out)
    return out


def legal_name(pid):
    idn = PARTY[pid]["identity"]
    form = idn.get("legal", {}).get("form")
    return f"{idn['name']} {form}" if form and form != "SP" else idn["name"]


def legal_entity(pid):
    p = PARTY[pid]
    idn, c = p["identity"], WORLD["countries"][p["c"]]
    src = f"identity of {idn['name']} (world/parties.json)"
    le = idn.get("legal", {})
    out = {"RegistrationName": V(legal_name(pid), "The name under which the party is registered, with its legal form; "
                                                  f"{src}."),
           "CompanyID": V(idn["registry_id"], f"Number in the {c['registry']['name']}; {src}.")}
    if le.get("founded"):
        out["RegistrationDate"] = V(le["founded"], f"The day the company was entered in the register; {src}.")
    if le.get("form"):
        out["CompanyLegalFormCode"] = V(le["form"], f"The legal form, as abbreviated in {c['name']} (world/countries.json).")
        out["CompanyLegalForm"] = V(c["legal_forms"][le["form"]], "The legal form, in words.")
    if le.get("sole_proprietor"):
        out["SoleProprietorshipIndicator"] = V("true", f"The farm belongs to one farmer, who runs it in their own name; "
                                                       f"{src}.")
    if le.get("size"):
        out["EntitySizeCode"] = V(le["size"], f"The size class of the company (micro, small, medium or large); {src}.")
    if le.get("capital"):
        out["CorporateStockAmount"] = V(str(le["capital"]), f"The share capital, in {c['currency']['name'].lower()}; "
                                                            f"{src}.", currencyID=c["currency"]["code"])
        out["FullyPaidSharesIndicator"] = V("true", "All shares are paid up.")
    out["RegistrationAddress"] = {"CityName": V(idn["address"]["CityName"], "The registered office, as entered in the "
                                                                            "register."),
                                  "Country": {"IdentificationCode": V(p["c"], "The country of registration.")}}
    out["CorporateRegistrationScheme"] = {
        "ID": V(c["register_scheme"], "The identifier of the register in the world (world/countries.json)."),
        "Name": V(c["registry"]["name"], "The register the company is entered in."),
        "CorporateRegistrationTypeCode": V("Commercial", "A register of businesses, not a register of charities or "
                                                         "associations."),
        "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V(p["c"], "The register covers the whole "
                                                                                  "country.")}}}
    if le.get("shareholder"):
        sh = le["shareholder"]
        out["ShareholderParty"] = {"ParticipationPercent": V(str(sh["percent"]), "The share it holds in this company; "
                                                                                 f"{src}."),
                                   "Party": party(sh["party"], short=True)}
    if le.get("listing"):
        li = le["listing"]
        out["SecurityListing"] = {"ID": V(li["id"], "The identifier of the listed shares, in the form of an ISIN with the "
                                                    "world's country code."),
                                  "MarketName": V(li["market"], "The regulated market where the shares are listed."),
                                  "MarketCode": V(li["code"], "The market's code.")}
    return out


def address(pid):
    p = PARTY[pid]
    idn, c = p["identity"], WORLD["countries"][p["c"]]
    src = f"identity of {idn['name']} (world/parties.json)"
    a = idn["address"]
    why = {"Postbox": "The customs office receives its post in a post box.",
           "Floor": "The floor of the trade services desk in the bank's building.",
           "Room": "The room of the trade services desk.",
           "AdditionalStreetName": "The gate of the business park to use.",
           "BlockName": "The business park the distribution centre stands in.",
           "BuildingName": "The bank's building, known by its name.",
           "InhouseMail": "The internal mail code of the procurement office.",
           "Department": "The department the post is for.",
           "MarkAttention": "For the attention of the head of procurement.",
           "PlotIdentification": "The plot of the distribution centre in the business park.",
           "CitySubdivisionName": "The quarter of Lumeport the party is in.",
           "CountrySubentityCode": "The state as a code of Bayvarra's address scheme (world/countries.json).",
           "Region": "The province, part of an address in Urvania.",
           "District": "The district of the island, used to find a farm off the main roads.",
           "Description": "How to find the farm, which has no house number on a street."}
    out = {}
    for k in ("Postbox", "Floor", "Room", "StreetName", "AdditionalStreetName", "BlockName", "BuildingName",
              "BuildingNumber", "Description", "InhouseMail", "Department", "MarkAttention", "PlotIdentification",
              "CitySubdivisionName", "CityName", "PostalZone", "CountrySubentity", "CountrySubentityCode", "Region",
              "District"):
        if a.get(k):
            out[k] = V(a[k], {"StreetName": "Street of the postal address.", "BuildingNumber": "Building number of "
                              "the postal address.", "CityName": "The town or locality nearest to the party's place on "
                              "the map, in its own country and state.", "PostalZone": f"Postal code in {c['name']}'s "
                              f"format ({c['address']['postal_zone']}).", "CountrySubentity": f"The state, part of an "
                              f"address in federal {c['name']}."}.get(k, why.get(k, "")) + f" {src}.")
    out["AddressFormatCode"] = V(p["c"], f"The address follows {c['name']}'s address format (world/countries.json): "
                                         f"{' / '.join(c['address']['lines'])}.")
    out["TimezoneOffset"] = V(c["timezone"], "The party's time zone, one hour behind UTC, where the world lies "
                                             "(world/countries.json).")
    if idn.get("address_lines"):
        out["AddressLine"] = [{"Line": V(line, "The address as the farm writes it, line by line: rural addresses on "
                                               "the island are not fully structured.")} for line in idn["address_lines"]]
    out["Country"] = {"IdentificationCode": V(p["c"], f"{c['name']}: a user-assigned ISO 3166-1 code, in the world's "
                                                      "country code list (world/codelists)."),
                      "Name": V(c["name"], "The country's name, for readers of the address.")}
    if idn.get("site") and pid == "38-xl":
        out["LocationCoordinate"] = coordinate(p["at"])
    return out


def coordinate(at):
    """Latitude and longitude of a map tile: the world lies in an empty part of the South Atlantic."""
    g = WORLD["geography"]
    lat = Decimal(str(g["origin"]["latitude_south"])) + Decimal(str(g["degrees_per_tile"])) * at[1]
    lon = Decimal(str(g["origin"]["longitude_west"])) - Decimal(str(g["degrees_per_tile"])) * at[0]
    why = "Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is " \
          "open sea on a real map (world/countries.json)."
    def dm(x):
        return int(x), (x - int(x)) * 60
    (la, lam), (lo, lom) = dm(lat), dm(lon)
    return {"CoordinateSystemCode": V("WGS84", "The World Geodetic System 1984, as used by satellite navigation."),
            "LatitudeDegreesMeasure": V(str(la), why, unitCode="DD"),
            "LatitudeMinutesMeasure": V(str(lam.quantize(Decimal("0.01"))), "The minutes of the latitude.", unitCode="D61"),
            "LatitudeDirectionCode": V("South", "South of the equator."),
            "LongitudeDegreesMeasure": V(str(lo), why, unitCode="DD"),
            "LongitudeMinutesMeasure": V(str(lom.quantize(Decimal("0.01"))), "The minutes of the longitude.",
                                         unitCode="D61"),
            "LongitudeDirectionCode": V("West", "West of the Greenwich meridian.")}


def location(pid):
    p = PARTY[pid]
    site = p["identity"]["site"]
    out = {}
    if site.get("locode"):
        out["ID"] = V(site["locode"], "The place's code in the form of a UN/LOCODE, with the world's country code.",
                      schemeID="UN/LOCODE")
    out["Description"] = V(site["description"], "Where the party actually operates, apart from its postal address.")
    if site.get("conditions"):
        out["Conditions"] = V(site["conditions"], "What a visitor must know about getting there.")
    if p["identity"].get("website"):
        out["InformationURI"] = V(p["identity"]["website"], "Where to find more about the place.")
    out["LocationCoordinate"] = coordinate(p["at"])
    if site.get("subsidiary"):
        out["SubsidiaryLocation"] = {"Name": V(site["subsidiary"], "A part of the port with its own location: where "
                                                                   "containers are handled.")}
    return out


def register_scheme(country):
    return f"urn:ubl-examples:world:{country}:register"


def party_again(pid, first):
    """A later mention of a party already given in full in this document: its identifier and name only."""
    idn = PARTY[pid]["identity"]
    why = (f"The same party as at {first}, where its full details are given; only its identifier and name are repeated."
           if first else "A party referred to from another party's details: its identifier and name are enough.")
    out = {"PartyName": {"Name": V(idn["name"], why)}}
    if idn.get("registry_id"):
        out["PartyIdentification"] = {"ID": V(idn["registry_id"], why, schemeID=register_scheme(PARTY[pid]["c"]))}
    return out


def institution(pid):
    """The content of a cac:FinancialInstitution element, for a bank of the world."""
    p = PARTY[pid]
    idn = p["identity"]
    src = f"identity of {idn['name']} (world/parties.json)"
    a = idn["address"]
    return {"_bank": pid,
            "ID": V(idn["bank_code"], f"The bank code, the part of every account number that names the bank; {src}."),
            "Name": V(idn["name"], f"The bank; {src}."),
            "Address": {"StreetName": V(a["StreetName"], f"The bank's head office; {src}."),
                        "BuildingNumber": V(a["BuildingNumber"], f"Its building number; {src}."),
                        "CityName": V(a["CityName"], f"Its town; {src}."),
                        "Country": {"IdentificationCode": V(p["c"], "The bank's country.")}}}


def institution_again(pid, first):
    return {"ID": V(PARTY[pid]["identity"]["bank_code"], f"The same bank as at {first}, where its name is given; "
                                                          "only its code is repeated.")}


def account(pid, why, note=None):
    """The content of a cac:FinancialAccount element for the account of a party."""
    acc = PARTY[pid]["identity"]["account"]
    bank = PARTY[acc["bank"]]
    out = {"ID": V(acc["number"], f"{why} The number follows the structure of ISO 13616 with its check digits, with the "
                                  "world's country code; it is not called an IBAN, because the world's countries are "
                                  "not registered IBAN countries.", schemeID="urn:ubl-examples:world:account"),
           "Name": V(legal_name(pid), "The account holder, as the bank knows it."),
           "AccountTypeCode": V("Current", "A current account, for payments in and out."),
           "AccountFormatCode": V("ISO13616", "The account number has the structure of ISO 13616."),
           "CurrencyCode": V(WORLD["countries"][bank["c"]]["currency"]["code"], "The account is kept in the currency of "
                                                                               "the bank's country.")}
    if note:
        out["PaymentNote"] = V(note, "What the payer is asked to quote with the transfer, so the payment is matched.")
    branch = bank["identity"].get("branch")
    out["FinancialInstitutionBranch"] = {"FinancialInstitution": institution(acc["bank"])}
    if branch:
        out["FinancialInstitutionBranch"] = {"ID": V(branch["id"], "The branch that keeps the account."),
                                             "Name": V(branch["name"], "The branch's name."),
                                             "FinancialInstitution": institution(acc["bank"])}
    out["Country"] = {"IdentificationCode": V(bank["c"], "The country where the account is kept.")}
    return out


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
        if a[3].startswith(DEPRECATED) or MODEL["abies"][a[1]]["deprecated"] or name in spec.get("not_endorsed", []):
            raise SystemExit(f"{path}/{name}: deprecated in UBL 2.5")
        for sub in content[name] if isinstance(content[name], list) else [content[name]]:
            here = f"{path}/{name}"
            for key, again in (("_pid", party_again), ("_bank", institution_again)):
                if key in sub:
                    if sub[key] in seen:
                        extra = {k: v for k, v in sub.items() if k not in sub.get("_keys", ()) and not k.startswith("_")}
                        sub = {**again(sub[key], seen[sub[key]].split("/", 1)[1]), **extra}
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
