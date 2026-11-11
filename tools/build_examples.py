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
import json
import os
import re
import sys
import uuid
import zlib
from decimal import ROUND_HALF_UP, Decimal

from lxml import etree

sys.path.insert(0, os.path.dirname(__file__))
import codelists  # noqa: E402
import world_data  # noqa: E402
import world_docs  # noqa: E402
import world_ids  # noqa: E402
import world_parties  # noqa: E402
import world_specs  # noqa: E402
import world_items  # noqa: E402

NS_CAC = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
NS_CBC = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
DEPRECATED = "(Deprecated)"

WORLD = world_data.load()
MODEL = world_docs.load_model()
REFERENCED = {p["id"] for p in WORLD.get("referenced", [])}      # parties only referred to: identifier and name
PARTY = {p["id"]: p for p in WORLD["parties"] + WORLD.get("referenced", [])}
ITEM = {i["id"]: i for i in WORLD["items"]}
CUR = {c["currency"]["code"]: c["currency"] for c in WORLD["countries"].values()}


# ---------------------------------------------------------------- values with reasons
class V:
    """A value with its reason, and optional attributes (currencyID, unitCode, schemeID ...)."""
    def __init__(self, value, why, **attrs):
        self.value, self.why, self.attrs = value, why, attrs


class Detail(V):
    """The specific detail of the case for the text partner of a code (RejectReason beside RejectReasonCode): the
    builder writes the code's meaning from its list, ": " and this detail (decision P6). A text partner given as a
    plain V gets the meaning alone."""


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
        conv = idn.get("identification", {})
        if conv.get("convention") == "GS1":
            out["AdditionalPartyIdentification"] = [{"ID": V(
                conv["gln"], "A further identifier, the party's Global Location Number (the endorsed "
                "PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, "
                "under its company prefix, which starts with 952, the prefix GS1 reserves for examples "
                f"(decision ID-Q7); {src}.", schemeID="GS1 GLN")}]
        elif conv.get("convention") == "ISO":
            out["AdditionalPartyIdentification"] = [{"ID": V(
                f"0990:{conv['codana_cin']}", "A further identifier (the endorsed PartyIdentification holds one "
                "only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code "
                "designator 0990 of the Codana Identification Agency and the party's Codana "
                "company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code "
                f"designator 0990; {src}.", schemeID="ISO 6523")}]
    if idn.get("customs_id"):
        out["AdditionalPartyIdentification"] = out.get("AdditionalPartyIdentification", []) + [{"ID": V(
            idn["customs_id"], "A further identifier: the party's customs trader number, because it imports or exports "
            f"({c['customs_trader_format']}); {src}.", schemeID=f"urn:ubl-examples:world:{p['c']}:customs-trader")}]
    out["PartyName"] = {"Name": V(idn["name"], f"The trading name; {src}.")}
    if idn.get("trade_name"):
        out["TradePartyName"] = {"Name": V(idn["trade_name"], f"The name the shops trade under, shorter than the company's "
                                                             f"name; {src}.")}
    if idn.get("language"):
        code = WORLD["countries"][p["c"]]["languages"][0]
        if code == "en":
            out["Language"] = {"ID": V("en", "English, the language the party does business in."),
                               "Name": V("English", "The language's name."),
                               "LocaleCode": V(idn["language"], "The language as a lower-case code of the world's ISO 639 list "
                                                                "(ISO 639).")}
        else:
            lang = WORLD["languages"][code]
            out["Language"] = {"ID": V(code, f"{lang['name']}, the language of {c['name']} and of the party; the code is "
                                             "from the range ISO 639 reserves for local use (qaa–qtz), as the world's "
                                             "languages are invented (world/countries.json)."),
                               "Name": V(lang["name"], f"The language's name in English; in the language itself: "
                                                       f"{lang['own_name']}.")}
    out["PostalAddress"] = address(pid, register=True)
    if idn.get("site"):
        out["PhysicalLocation"] = location(pid)
    if idn.get("endpoint"):
        out["ElectronicAddress"] = {   # new in UBL 2.5; Party/EndpointID is deprecated
            "ExchangeNetworkID": V("urn:ubl-examples:world:network", "The network in which the address is registered: "
                                   "the world's own exchange network."),
            "ElectronicAddressID": V(idn["endpoint"], "The party's electronic address in that network: its country code and "
                                     f"registry number; {src}. UBL 2.5 carries it here; Party/EndpointID is deprecated.",
                                     schemeID="urn:ubl-examples:world:endpoint")}
    if idn.get("tax_id"):
        scheme = c["tax"]["schemes"][0]
        tax = {"RegistrationName": V(legal_name(pid), f"The name under which the party is registered for "
                                                      f"{scheme['name'].lower()}; {src}."),
               "CompanyID": V(idn["tax_id"], f"Tax number under {c['name']}'s {scheme['name'].lower()} "
                                             f"({c['tax_id']['format']}); {src}."),
               "TaxLevelCode": V("STATE" if scheme.get("levied_by") == "state" else "NATIONAL",
                                 f"The level of government that levies the tax: {c['name']}'s "
                                 f"{scheme['name'].lower()} is levied by the "
                                 f"{'states' if scheme.get('levied_by') == 'state' else 'country'}.")}
        if idn.get("tax_exemption"):
            tax["ExemptionReason"] = Detail(idn["tax_exemption"][0].lower() + idn["tax_exemption"][1:],
                                            f"why purchases by this party carry no sales tax; {src}.")
            code = next((v for k, v in c["tax"].get("exemption_codes", {}).items()
                         if idn.get("tax_exemption_kind") == k), None)
            if code:
                tax["ExemptionReasonCode"] = V(code, f"The exemption as a code of {c['name']}'s national list of "
                                                     f"exemption reasons: {idn['tax_exemption_kind'].lower()}.",
                                               listID=codelists.NATIONAL.format(p["c"], "TaxExemptionReason"))
            if idn.get("tax_registration_office"):
                tax["RegistrationAddress"] = {"CityName": V(idn["tax_registration_office"], "Where the party is "
                                                                                            "registered for the tax."),
                                              "CountrySubentity": V(idn["address"]["CountrySubentity"], "Its state or territory."),
                                              "Country": {"IdentificationCode": V(p["c"], "Its country.")}}
        juris = {"Country": {"IdentificationCode": V(p["c"], "The country whose tax this is.")}}
        if scheme.get("levied_by") == "state":
            juris = {"CountrySubentity": V(idn["address"]["CountrySubentity"], "The state or territory whose sales tax "
                                           "the party is registered for."), **juris}
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
        if ct.get("id"):
            contact = {"ID": V(ct["id"], "The desk's number in the party's own contact list."), **contact}
        if ct.get("job_title"):
            contact["JobTitle"] = V(ct["job_title"], f"The job of the person who answers at the desk; {src}.")
        if ct.get("department"):
            contact["Department"] = V(ct["department"], f"The department the desk belongs to; {src}.")
        if ct.get("telephone"):
            contact["Telephone"] = V(ct["telephone"], "Telephone under +999, a country code the ITU reserves for a "
                                                      "future global service (ITU-T E.164), so the number reaches no "
                                                      f"one; then the country digit and a number in {c['name']}'s own "
                                                      f"plan: {c['phone_plan']['note']} {src}.")
        if ct.get("telefax"):
            contact["Telefax"] = V(ct["telefax"], f"The customs office still lists a fax number; {src}.")
        contact["ElectronicMail"] = V(ct["email"], "E-mail under the reserved .example domain (RFC 2606), so it cannot "
                                                   f"reach anyone; {src}.")
        if ct.get("hours"):
            contact["Note"] = V(ct["hours"], f"When the desk can be reached; {src}.")
        if ct.get("mobile"):
            contact["OtherCommunication"] = {"ChannelCode": V("AL", "UN/EDIFACT 3155 code AL: cellular phone."),
                                             "Value": V(ct["mobile"], "The sales desk's mobile number, also under the "
                                                                      "reserved +999.")}
        out["Contact"] = contact
    if idn.get("person_name"):
        out["Person"] = {"FirstName": V(idn["person_name"]["first"], f"The consumer's first name; {src}."),
                         "FamilyName": V(idn["person_name"]["family"], f"The consumer's family name; {src}.")}
        if idn.get("account"):
            out["Person"]["FinancialAccount"] = account(pid, "The consumer's own account, from which the bills are "
                                                             "paid.")
    if idn.get("party_account_shown"):
        out["FinancialAccount"] = account(pid, "The party's account, given with its details so that payments can be "
                                               "sent to it.")
    if idn.get("service_provider"):
        sp = idn["service_provider"]
        out["ServiceProviderParty"] = {"ID": V(sp["contract"], f"The number of the service contract between the two; {src}."),
                                       "ServiceTypeCode": V("LOGISTICS", "The kind of service, as a code."),
                                       "ServiceType": V(sp["type"], f"What the service provider does for the party; "
                                                                    f"{src}."),
                                       "SellerContact": {"Name": V("Key account desk", "The provider's contact for "
                                                                                       "this customer.")},
                                       "Party": party(sp["party"], short=True)}
    if idn.get("authorization"):
        au = idn["authorization"]
        out["PartyAuthorization"] = {**({"PurposeCode": V(au["purpose_code"], "The purpose as a code.")}
                                        if au.get("purpose_code") else {}),
                                     "Purpose": V(au["purpose"], f"What the authority has authorized the party to do; "
                                                                 f"{src}."),
                                     "ValidityPeriod": {"EndDate": V(au["valid_until"], "The authorization expires on "
                                                                                        "this date.")},
                                     "Certificate": {"ID": V(au["certificate"], "The number of the permit in the "
                                                             f"{c['identifiers'][au['register']]['name']}; the schemeID "
                                                             "names the register, and with it the authority that keeps "
                                                             "it, so no issuer party is needed (decision ID-Q10).",
                                                             schemeID=world_ids.national_scheme(p["c"], au["register"])),
                                                     "CertificateTypeCode": V("PERMIT", "A permit issued by an authority "
                                                                                        "of the party's country."),
                                                     "CertificateType": V("Operating permit", "The kind of certificate, "
                                                                                              "in words.")}}
    if idn.get("shop_website"):
        out["AdditionalWebSite"] = {"Name": V("Online shop", "The store's second website, where consumers buy."),
                                    "URI": V(idn["shop_website"], "Under the reserved .example domain.")}
    if idn.get("social"):
        so = idn["social"]
        out["SocialMediaProfile"] = {**({"ID": V(so["id"], "The profile's number on the medium.")} if so.get("id")
                                        else {}),
                                     "Name": V(so["name"], "The store's profile name."),
                                     "SocialMediaTypeCode": V(so["type"], "The kind of social medium."),
                                     "URI": V(so["uri"], "The profile's address, under the reserved .example domain.")}
    out["_keys"] = set(out)
    return out


def legal_name(pid):
    idn = PARTY[pid]["identity"]
    form = idn.get("legal", {}).get("form")
    if not form or form == "SP":
        return idn["name"]
    return f"{idn['name']} {WORLD['countries'][PARTY[pid]['c']]['legal_forms'][form]['abbreviation']}"


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
        out["CompanyLegalFormCode"] = V(le["form"], f"The legal form, as a code of {c['name']}'s national list: "
                                                    "only the listID tells the forms of different countries apart.",
                                        listID=codelists.NATIONAL.format(p["c"], "CompanyLegalForm"))
        out["CompanyLegalForm"] = V(c["legal_forms"][le["form"]]["name"], "The legal form, in words.")
    if le.get("sole_proprietor"):
        out["SoleProprietorshipIndicator"] = V("true", f"The farm belongs to one farmer, who runs it in their own name; "
                                                       f"{src}.")
    if le.get("registration_expires"):
        out["RegistrationExpirationDate"] = V(le["registration_expires"], "The island renews a farm's registration "
                                                                          "every year: it runs until this date.")
    if not idn.get("person"):
        out["CompanyLiquidationStatusCode"] = V("ACTIVE", "The register shows the company as active, not in "
                                                          "liquidation.")
    if le.get("headcount"):
        t = le["turnover"]
        out["EntitySizeCode"] = V(codelists.entity_size(le["headcount"], t["amount"], t["currency"]),
                                  f"The size class follows from the company's {le['headcount']} persons and its turnover "
                                  f"of {t['amount']} {t['currency']} in {t['year']}, by the Trade Accord's limits; {src}.")
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
        "CorporateRegistrationTypeCode": V("COMMERCIAL", "A register of businesses, not a register of charities or "
                                                         "associations."),
        "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V(p["c"], "The register covers the whole "
                                                                                  "country.")}}}
    if le.get("shareholder"):
        sh = le["shareholder"]
        out["ShareholderParty"] = {"ParticipationPercent": V(str(sh["percent"]), "The share it holds in this company; "
                                                                                 f"{src}."),
                                   "Party": party(sh["party"], short=True)}
    if le.get("head_office"):
        out["HeadOfficeParty"] = party(le["head_office"], short=True)
    if le.get("listing"):
        li = le["listing"]
        out["SecurityListing"] = {"ID": V(li["id"], "The identifier of the listed shares, in the form of an ISIN with the "
                                                    "world's country code."),
                                  "MarketName": V(li["market"], "The regulated market where the shares are listed."),
                                  "MarketCode": V(li["code"], "The market's code.")}
        if li.get("description"):
            out["SecurityListing"]["Description"] = V(li["description"], "What is listed.")
    return out


def address_format_code(code):
    c = WORLD["countries"][code]
    return V(code, f"The address follows {c['name']}'s address format (world/countries.json), one line after the "
                   f"other, a line left out when the address has none of its fields: "
                   f"{'; '.join(c['address']['lines'])}. {c['address']['line_rule']}")


def check_addresses(root, where):
    """Every address agrees with its country's format: a structured address (street, building number or post box)
    has an AddressFormatCode, it is the code of the address's country, and its AddressLine elements are the lines
    the format makes of the structured fields."""
    for e in root.iter():
        if not isinstance(e.tag, str):
            continue
        kids = {}
        for k in e:
            if isinstance(k.tag, str):
                kids.setdefault(etree.QName(k).localname, []).append(k)
        if not kids.keys() & {"StreetName", "BuildingNumber", "Postbox"}:
            continue
        name = f"{where}: {etree.QName(e).localname} of {etree.QName(e.getparent()).localname}"
        country = kids["Country"][0].find("{*}IdentificationCode").text
        if "AddressFormatCode" not in kids:
            raise SystemExit(f"{name} has no AddressFormatCode")
        if kids["AddressFormatCode"][0].text != country:
            raise SystemExit(f"{name}: AddressFormatCode {kids['AddressFormatCode'][0].text} is not its country {country}")
        if "ID" in kids and kids["ID"][0].get("schemeID", "").endswith(("address-register", "delivery-point")):
            fields = {n: v[-1].text for n, v in kids.items() if not len(v[-1])}
            kind, spec = world_parties.address_register(WORLD, country, fields)
            if not kind or kids["ID"][0].get("schemeID") != world_ids.national_scheme(country, kind):
                raise SystemExit(f"{name}: address number from {kids['ID'][0].get('schemeID')}, but the address is "
                                 f"in the area of {kind and world_ids.national_scheme(country, kind)}")
        if "AddressLine" in kids:
            fields = {n: [k.text for k in v] for n, v in kids.items() if n not in world_data.NOT_ON_A_LINE}
            want = world_data.address_lines(WORLD["countries"][country]["address"], fields)
            got = [l.find("{*}Line").text for l in kids["AddressLine"]]
            if got != want:
                raise SystemExit(f"{name}: AddressLine {got} differs from the lines of the format {want}")


def check_payment_means(root, where):
    """Every payment means agrees with its payment system (world/countries.json, decision Q18): the clearing channel
    is one the system in PaymentRailID has, and the service level fits it (URGP only over a real-time gross
    settlement system, NURG not over one)."""
    rails = {c["payment"]["system"]["id"]: c["payment"]["system"]["clearing_channels"] for c in WORLD["countries"].values()}
    rails[WORLD["payment_cross_border"]["system"]] = WORLD["payment_cross_border"]["clearing_channels"]
    for pm in root.iter(f"{{{NS_CAC}}}PaymentMeans"):
        rail, channel = pm.findtext(f"{{{NS_CBC}}}PaymentRailID"), pm.findtext(f"{{{NS_CBC}}}PaymentChannelCode")
        level = pm.findtext(f"{{{NS_CBC}}}ServiceLevelCode")
        if rail and rail not in rails:
            raise SystemExit(f"{where}: PaymentRailID {rail} is not a payment system of the world")
        if channel and (not rail or channel not in rails[rail]):
            raise SystemExit(f"{where}: PaymentChannelCode {channel} is not a clearing channel of {rail}")
        if level and ((level == "URGP") != (channel == "RTGS") and level in ("URGP", "NURG")):
            raise SystemExit(f"{where}: ServiceLevelCode {level} does not fit the clearing channel {channel}")


def check_formats(root, where):
    """A file's PRONOM format agrees with its media type (decision Q19)."""
    pronom = codelists.load()["lists"]["PRONOM"]["codes"]
    for ref in root.iter(f"{{{NS_CAC}}}ExternalReference"):
        fmt, mime = ref.findtext(f"{{{NS_CBC}}}FormatCode"), ref.findtext(f"{{{NS_CBC}}}MimeCode")
        if fmt and mime and pronom[fmt]["mime"] != mime:
            raise SystemExit(f"{where}: FormatCode {fmt} is {pronom[fmt]['mime']} in PRONOM, but MimeCode is {mime}")


def check_tax_exemption_lists(root, where, doc):
    """A tax exemption reason code is from the national list of the seller's country (decision Q28); one on a
    party's tax scheme from the list of that party's country."""
    sellers = {PARTY[pid]["c"] for path, pid in doc["parties"].items() if isinstance(pid, str)
               and path.split("/")[0] in ("AccountingSupplierParty", "SellerSupplierParty")}
    for e in root.iter(f"{{{NS_CBC}}}TaxExemptionReasonCode", f"{{{NS_CBC}}}ExemptionReasonCode"):
        cc = e.get("listID", "").split(":")[3]
        if etree.QName(e).localname == "ExemptionReasonCode":
            own = e.getparent().getparent().find(f"{{{NS_CAC}}}PostalAddress/{{{NS_CAC}}}Country/"
                                                  f"{{{NS_CBC}}}IdentificationCode")
            if own is not None and own.text != cc:
                raise SystemExit(f"{where}: ExemptionReasonCode from {cc}'s list for a party in {own.text}")
        elif sellers and cc not in sellers:
            raise SystemExit(f"{where}: TaxExemptionReasonCode from {cc}'s list, but the seller is in "
                             f"{', '.join(sorted(sellers))}")


def address(pid, register=False):
    """A party's address. register: the address's number in its address register goes with it, as it does on a
    party's postal address and a delivery address (decision ID-Q8), not where the address only says where something
    is."""
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
           "CountrySubentityCode": "The state or territory as a code of Bayvarra's address scheme (world/countries.json).",
           "Region": "The province, part of an address in Urvania.",
           "District": "The district of the island, used to find a farm off the main roads.",
           "Description": "How to find the farm, which has no house number on a street."}
    out = {}
    if a.get("ID") and register:
        kind, spec = world_parties.address_register(WORLD, p["c"], a)
        out["ID"] = V(a["ID"], f"The address's number in the {spec['name']} ({spec['format']}); {src}.",
                      schemeID=world_ids.national_scheme(p["c"], kind))
    out["AddressTypeCode"] = V("POSTAL" if a.get("Postbox") else "RESIDENTIAL" if idn.get("person") else "BUSINESS",
                               "The kind of address.")
    for k in ("Postbox", "Floor", "Room", "StreetName", "AdditionalStreetName", "BlockName", "BuildingName",
              "BuildingNumber", "Description", "InhouseMail", "Department", "MarkAttention", "PlotIdentification",
              "CitySubdivisionName", "CityName", "PostalZone", "CountrySubentity", "CountrySubentityCode", "Region",
              "District"):
        if a.get(k):
            out[k] = V(a[k], {"StreetName": "Street of the postal address.", "BuildingNumber": "Building number of "
                              "the postal address.", "CityName": "The town or locality nearest to the party's place on "
                              "the map, in its own country and state.", "PostalZone": f"Postal code in {c['name']}'s "
                              f"format ({c['address']['postal_zone']}).", "CountrySubentity": f"The state or territory, "
                              f"part of an address in federal {c['name']}."}.get(k, why.get(k, "")) + f" {src}.")
    code = c["languages"][0]
    if code != "en" and "en" in c["languages"] and isinstance(out.get("StreetName"), V):
        lang = WORLD["languages"][code]["name"]                 # a bilingual country names its streets twice
        st = out["StreetName"]
        out["StreetName"] = [V(translate(st.value, code, street=True), f"The street's name in {lang}: {c['name']} "
                               f"is officially bilingual, and street names are given in both languages "
                               f"(world/countries.json); {src}.", languageID=code),
                             V(st.value, "The street's name in English, the country's other official language"
                                         + ("; the Italian names the British kept are part of English now"
                                            if p["c"] == "XU" else "") + f"; {src}.", languageID="en")]
        local = WORLD["languages"][code].get("place_names", {}).get(a.get("CityName"))
        if local:
            out["CityName"] = [V(local, f"The town's {lang} name, which its people have always used; {src}.",
                                 languageID=code),
                               V(a["CityName"], f"The town's English name, inherited from the Italian; {src}.",
                                 languageID="en")]
    out["AddressFormatCode"] = address_format_code(p["c"])
    out["TimezoneOffset"] = V(c["timezone"], "The party's time zone, one hour behind UTC, where the world lies "
                                             "(world/countries.json).")
    if idn.get("address_lines"):
        fields = {k: [x.value for x in v] if isinstance(v, list) else [v.value] for k, v in out.items()}
        out["AddressLine"] = [{"Line": V(line, f"One line of the address as the farm writes it, made from the fields "
                                               f"above in {c['name']}'s address format (world/countries.json), so "
                                               "that lines and fields agree. A name in both languages is given in "
                                               "both on the line, the national language first.")}
                              for line in world_data.address_lines(c["address"], fields)]
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
    return {"CoordinateSystemCode": V("4326", "The World Geodetic System 1984, as used by satellite navigation."),
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
    if site.get("altitude"):
        out["LocationCoordinate"]["AltitudeMeasure"] = V(str(site["altitude"]), "The height of the place above sea "
                                                                               "level.", unitCode="MTR")
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
           if first else f"{PARTY[pid]['what']} Its identifier and name are enough (world/parties.json, referenced)."
           if pid in REFERENCED else "A party referred to from another party's details: its identifier and name are "
                                     "enough.")
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
            "ID": V(idn["bic"], "The bank's identifier in the Trade Accord's payment link, in the structure of ISO 9362 "
                                f"(a BIC) with the world's country codes: the bank code {idn['bank_code']}, the country "
                                f"{p['c']} and the location {idn['bic'][6:8]}; {src}.",
                    schemeID="urn:ubl-examples:world:bank-identifier"),
            "Name": V(idn["name"], f"The bank; {src}."),
            "Address": {"StreetName": V(a["StreetName"], f"The bank's head office; {src}."),
                        "BuildingNumber": V(a["BuildingNumber"], f"Its building number; {src}."),
                        "CityName": V(a["CityName"], f"Its town; {src}."),
                        "AddressFormatCode": address_format_code(p["c"]),
                        "Country": {"IdentificationCode": V(p["c"], "The bank's country.")}}}


def institution_again(pid, first):
    return {"ID": V(PARTY[pid]["identity"]["bic"], f"The same bank as at {first}, where its name is given; only its "
                                                    "identifier is repeated.",
                    schemeID="urn:ubl-examples:world:bank-identifier")}


def account(pid, why, note=None):
    """The content of a cac:FinancialAccount element for the account of a party."""
    acc = PARTY[pid]["identity"]["account"]
    bank = PARTY[acc["bank"]]
    out = {"ID": V(acc["number"], f"{why} The number follows the structure of ISO 13616 with its check digits, with the "
                                  "world's country code, and holds the codes of the bank and the branch that keep it; "
                                  "it is not called an IBAN, because the world's countries are not registered IBAN "
                                  "countries.", schemeID="urn:ubl-examples:world:account"),
           "Name": V(legal_name(pid), "The account holder, as the bank knows it."),
           **({"AliasName": V(acc["alias"], "The short name the holder gave the account, shown in its bank's "
                                             "app.")} if acc.get("alias") else {}),
           **({"BlockchainID": V(acc["ledger"], "The account holds tokenised coral deposits on the Bank of Selanu's "
                                                "ledger, which Coral net settles on (world/countries.json).")}
              if acc.get("ledger") else {}),
           "AccountTypeCode": V("CACC", "A current account, for payments in and out."),
           "AccountFormatCode": V("ISO13616", "The account number has the structure of ISO 13616."),
           "CurrencyCode": V(WORLD["countries"][bank["c"]]["currency"]["code"], "The account is kept in the currency of "
                                                                               "the bank's country.")}
    if note:
        out["PaymentNote"] = V(note, "What the payer is asked to quote with the transfer, so the payment is matched.")
    branch = next(b for b in bank["identity"]["branches"] if b["id"] == acc["branch"])
    spec = WORLD["countries"][bank["c"]]["identifiers"]["bank-branch"]
    out["FinancialInstitutionBranch"] = {"ID": V(branch["id"], f"The branch that keeps the account, by its national "
                                                               f"code: the {spec['name']} ({spec['format']}). The "
                                                               "account number holds it.",
                                                 schemeID=world_ids.national_scheme(bank["c"], "bank-branch")),
                                         "Name": V(branch["name"], "The branch's name."),
                                         "FinancialInstitution": institution(acc["bank"]),
                                         "Address": {"CityName": V(branch["city"], "The town the branch is in."),
                                                     "Country": {"IdentificationCode": V(bank["c"], "Its country.")}}}
    out["Country"] = {"IdentificationCode": V(bank["c"], "The country where the account is kept.")}
    return out


def buyer_item_id(iid, buyer):
    """The buyer's own number for an item: its own item when it resells it, or the number it keeps for it."""
    it = ITEM[iid]
    own = next((i for i in WORLD["items"] if i["seller"] == buyer and i.get("resale_of") == iid), None)
    if own:
        return own["sellers_id"], f"The buyer's own item number: it resells this item as its item {own['id']}."
    if buyer in it.get("buyer_ids", {}):
        return it["buyer_ids"][buyer], "The number the buyer keeps for this item in its own system (world/items.json)."
    return None, None


def item_property(pr, src):
    """A cac:AdditionalItemProperty from a property of the items layer: [name, value], or a dict with the details."""
    if isinstance(pr, list):
        return {"Name": V(pr[0], "A property buyers ask about."), "Value": V(pr[1], f"Its value; {src}.")}
    out = {"Name": V(pr["name"], pr.get("why", "A property buyers ask about."))}
    if pr.get("id"):
        out["ID"] = V(pr["id"], "The maker's identifier for the property.")
    if pr.get("name_code"):
        out["NameCode"] = V(pr["name_code"], "The property's name as a code.")
    if pr.get("test"):
        out["TestMethod"] = V(pr["test"], "How the value is tested.")
    if pr.get("value"):
        out["Value"] = V(pr["value"], f"Its value; {src}.")
    if pr.get("value_qty"):
        out["ValueQuantity"] = V(pr["value_qty"][0], f"Its measured value; {src}.", unitCode=pr["value_qty"][1])
    if pr.get("qualifier"):
        out["ValueQualifier"] = [V(q, "What the value stands for.") for q in pr["qualifier"]]
    if pr.get("importance"):
        out["ImportanceCode"] = V(pr["importance"], "How much the property matters in describing the item.")
    if pr.get("list"):
        out["ListValue"] = V(pr["list"][0], "The property's value, taken from the maker's list of values ("
                                            f"{', '.join(pr['list'])}; {src}). One ListValue only: UBL rule IND7 "
                                            "allows a second one only in another language.")
    if pr.get("usable"):
        n_, unit, why = pr["usable"]
        out["UsabilityPeriod"] = {"DurationMeasure": V(n_, why, unitCode=unit)}
    if pr.get("group"):
        gid, gname, gimp = pr["group"]
        out["ItemPropertyGroup"] = {"ID": V(gid, "The group of properties this one belongs to."),
                                    "Name": V(gname, "The group's name."),
                                    "ImportanceCode": V(gimp, "How much the group matters.")}
    if pr.get("range_dim"):
        a_, v, lo, hi, u = pr["range_dim"]
        out["RangeDimension"] = {"AttributeID": V(a_, "The dimension the tolerance is for."),
                                 "Measure": V(v, "Its nominal size.", unitCode=u),
                                 "MinimumMeasure": V(lo, "The smallest size accepted.", unitCode=u),
                                 "MaximumMeasure": V(hi, "The largest size accepted.", unitCode=u)}
    if pr.get("range"):
        out["ItemPropertyRange"] = {"MinimumValue": V(pr["range"][0], "The lowest value accepted."),
                                    "MaximumValue": V(pr["range"][1], "The highest value accepted.")}
    if pr.get("standard"):
        sid, scope, issuer = pr["standard"]
        out["StandardPropertyIdentification"] = {"ID": V(sid, "The property's number in the property standard of the "
                                                               "identification agency."),
                                                 "IssuerScopeID": V(scope, "The part of the agency's property "
                                                                           "standard it is taken from (SF street "
                                                                           "furniture, WD wood), as the number "
                                                                           "itself shows."),
                                                 "IssuerParty": party(issuer, short=True)}
    if pr.get("sub"):
        out["SubItemProperty"] = [item_property(x, src) for x in pr["sub"]]
    return out


PACKAGING_DANGER_LEVEL = {"I": "1", "II": "2", "III": "3", "NA": "4"}   # UN packing group -> UN/EDIFACT 8339


def dangerous_goods_problem(un, name, cls, sub=None):
    """Whether a UN number, its proper shipping name and its class agree with the Dangerous Goods List of the UN Model
    Regulations (world/codelists/lists.json, UNModelRegsUN; decision P2). The proper shipping name is compared without
    case, with a dash for an en dash and without the entry's lower-case additions in brackets, such as "(including
    lithium ion polymer batteries)". None if they agree, else the problem."""
    lst = codelists.load()["lists"]["UNModelRegsUN"]
    if un not in lst["codes"]:
        return f"UN {un} is not in the world's Dangerous Goods List"

    def norm(t):
        return re.sub(r"\s+", " ", re.sub(r"\s*\([^)]*\)", "", t.replace("\u2013", "-"))).strip().casefold()
    if norm(name) != norm(lst["codes"][un]["name"]):
        return f"UN {un}: proper shipping name '{name}' is not the entry's '{lst['codes'][un]['name']}'"
    if cls != lst["classes"][un]:
        return f"UN {un}: class {cls}, but the entry is class {lst['classes'][un]}"
    if sub != lst["subsidiary"].get(un):
        return f"UN {un}: subsidiary hazard {sub}, but the entry has {lst['subsidiary'].get(un)}"
    return None


def check_dangerous_goods_items():
    """Every dangerous item of world/items.json has the class and proper shipping name of its UN number."""
    for it in WORLD["items"]:
        hz = it.get("hazard")
        if hz:
            why = dangerous_goods_problem(hz["un"][2:], hz["name"], hz["class"], hz.get("sub"))
            if why:
                raise SystemExit(f"world/items.json: {it['id']}: {why}")


def check_classifications(root, where):
    """An item's CPC Ver.2.1 code (ItemClassificationCode) is the one the official correspondence gives for its HS
    subheading (CommodityCode), as in world/items.json (tools/world_items.py, decision P5)."""
    for it in root.iter(f"{{{NS_CAC}}}Item"):
        cpc = [e.text for e in it.findall(f"{{{NS_CAC}}}CommodityClassification/{{{NS_CBC}}}ItemClassificationCode")
               if e.get("listID") == "UN CPC Ver.2.1"]
        hs = [e.text for e in it.findall(f"{{{NS_CAC}}}CommodityClassification/{{{NS_CBC}}}CommodityCode")
              if e.get("listID") == "WCO HS 2022"]
        for c in cpc:
            for h in hs:
                why = world_items.cpc_hs_problem(c, h, where)
                if why:
                    raise SystemExit(why)


def check_dangerous_goods(root, where):
    """The dangerous goods data agree within a document: the packaging danger level (UN/EDIFACT 8339) of a UN number
    is its packing group (I-1, II-2, III-3, NA-4), the hazardous category is the class, and an emergency card is the
    card of a class of the goods in the document (decisions Q11, Q23)."""
    groups, classes = {}, set()
    for hi in root.iter(f"{{{NS_CAC}}}HazardousItem"):
        un, pg = hi.findtext(f"{{{NS_CBC}}}UNDGCode"), hi.findtext(f"{{{NS_CBC}}}UNPackingGroupCode")
        cls, cat = hi.findtext(f"{{{NS_CBC}}}HazardClassID"), hi.findtext(f"{{{NS_CBC}}}HazardousCategoryCode")
        groups[un] = pg
        sub = hi.findtext(f"{{{NS_CAC}}}SecondaryHazard/{{{NS_CBC}}}ID")
        why = dangerous_goods_problem(un, hi.findtext(f"{{{NS_CBC}}}ProperShippingName") or "", cls, sub)
        if why:
            raise SystemExit(f"{where}: {why}")
        if cat is not None and cat != cls:
            raise SystemExit(f"{where}: HazardousCategoryCode {cat} is not the class {cls} of UN {un}")
    for e in root.iter(f"{{{NS_CBC}}}HazardClassID"):
        classes.add(e.text.split(".")[0])
    for li in root.iter(f"{{{NS_CAC}}}LoadedHazardousItem"):
        un, level = li.findtext(f"{{{NS_CBC}}}UNDGCode"), li.findtext(f"{{{NS_CBC}}}PackagingDangerLevelCode")
        if un in groups and level is not None and PACKAGING_DANGER_LEVEL[groups[un]] != level:
            raise SystemExit(f"{where}: UN {un}: packaging danger level {level} does not match packing group {groups[un]}")
    for sh in root.iter(f"{{{NS_CAC}}}SecondaryHazard"):
        card, cls = sh.findtext(f"{{{NS_CBC}}}EmergencyProceduresCode"), sh.findtext(f"{{{NS_CBC}}}ID")
        if card is not None and card != f"TEC{cls.split('.')[0]}":
            raise SystemExit(f"{where}: emergency procedures {card} of a secondary hazard of class {cls} are not the "
                             "card of that class")
    for e in root.iter(f"{{{NS_CBC}}}TransportEmergencyCardCode"):
        if e.text != "TECGEN" and e.text[3:] not in classes:
            raise SystemExit(f"{where}: emergency card {e.text} is not the card of a class of the goods "
                             f"({', '.join(sorted(classes))})")


def hazardous_item(it):
    """The dangerous goods data of an item (world/items.json), as the UN Model Regulations describe it."""
    hz = it["hazard"]
    out = {"ID": V(f"{it['sellers_id']}-DG", "The seller's dangerous goods record of the item."),
           "UNDGCode": V(hz["un"][2:], "The UN number, from the Dangerous Goods List of the UN Model Regulations."),
           "ProperShippingName": V(hz["name"], "The proper shipping name of the UN entry; the build checks that UN "
                                               "number, name and class agree with the Dangerous Goods List."),
           "HazardClassID": V(hz["class"], "The UN hazard class of the entry."),
           "HazardousCategoryCode": V(hz["class"], "The hazard class of the goods as a code of the UN Model "
                                                    "Regulations' classes."),
           "EmergencyProceduresCode": V(hz["ems"], "The emergency schedules for ships (EmS) of the IMDG Code for this "
                                                   "UN entry: the fire schedule and the spillage schedule."),
           "MedicalFirstAidGuideCode": V(hz["erg"], "The guide number of the Emergency Response Guidebook (ERG 2024) "
                                                    "for this UN number: the world's carriers use the ERG, as the IMDG "
                                                    "Code no longer gives medical first aid table numbers per UN number."),
           "AdditionalInformation": V(hz.get("note", "Packed as the rules require."), "What the shipper adds."),
           "PlacardNotation": V(hz["class"], "The class shown on the placard."),
           "MarkingID": V(hz["un"], "The UN number marked on each package.")}
    if hz.get("label"):
        out["PlacardEndorsement"] = V(hz["label"], "The hazard label on the package.")
    out["UNPackingGroupCode"] = V(hz.get("pg", "NA"), "The packing group of the UN entry; NA where the entry has no "
                                                     "packing group, as for lithium batteries and radioactive material.")
    out["UNPackingGroup"] = V(hz.get("pg", "NA"), "In words.")
    if hz.get("tunnel"):
        out["TunnelRestrictionCode"] = V(hz["tunnel"], "The tunnel restriction code for road transport.")
    if hz.get("technical"):
        out["TechnicalName"] = V(hz["technical"], "The technical name, needed with an n.o.s. entry.")
    if hz.get("sub"):
        out["SecondaryHazard"] = {"ID": V(hz["sub"], "The subsidiary hazard: flammable."),
                                  "PlacardNotation": V(hz["sub"], "Shown on a second label."),
                                  "PlacardEndorsement": V("3", "The flammable liquid label."),
                                  "Extension": V("Subsidiary risk 3", "In words."),
                                  "EmergencyProceduresCode": V(f"TEC{hz['sub']}", "The emergency procedures for the "
                                                               "subsidiary hazard: the Trade Accord's emergency card "
                                                               f"for class {hz['sub']}. The IMDG Code gives one pair "
                                                               "of emergency schedules for the whole UN entry (on the "
                                                               "item above), not one per hazard; the instructions in "
                                                               "writing of road transport (ADR 5.4.3), which the "
                                                               "Accord's cards follow, give the actions per danger "
                                                               "label, the subsidiary hazard's label included.")}
        out["FlashpointTemperature"] = {"AttributeID": V("FLASHPOINT", "Closed cup."),
                                        "Measure": V(hz["flash"], "The flashpoint.", unitCode="CEL")}
        out["MaritimePollutantCode"] = V("N", "Not a marine pollutant.")
    if hz.get("isotope"):
        name, act, unit = hz["isotope"]
        out["RadioactiveMaterial"] = {"Name": V("Americium-241 sources in smoke detectors", "The material."),
                                      "SpecialFormDescription": V("Sealed source, not special form.", "Its form."),
                                      "TransportIndexNumeric": V("0", "Excepted package: no dose rate to "
                                                                      "speak of."),
                                      "FissileCriticalitySafetyIndexNumeric": V("0", "Not fissile."),
                                      "ApplicableRadioactiveIsotope": {"Name": V(name, "The isotope."),
                                                                       "ActivityLevelMeasure": V(act, "Per detector.",
                                                                                                 unitCode=unit)}}
    return out


def item_names(it, src):
    """The item's name: in the seller's language and in English when the seller's country speaks another language
    (Urvanian, Lisavan), each with its languageID; English only for a seller in Bayvarra."""
    code = WORLD["countries"][PARTY[it["seller"]]["c"]]["languages"][0]
    if code == "en":
        return V(it["name"], f"The item's short name; {src}.")
    lang = WORLD["languages"][code]["name"]
    return [V(translate(it["name"], code), f"The item's name in {lang}, the seller's language; {src}.",
              languageID=code),
            V(it["name"], f"The item's name in English, the working language between the countries; {src}.",
              languageID="en")]


def item(iid, tax=None, buyer=None, instance=None, catalogue=None, catalogue_ref=None):
    """The content of a cac:Item element, from the items layer. `catalogue` is (catalogue number, line) for a
    catalogue line; `catalogue_ref` the catalogue an order line was ordered from."""
    it = ITEM[iid]
    src = f"item {it['id']} of {PARTY[it['seller']]['identity']['name']} (world/items.json)"
    out = {"Description": V(it["description"], f"The seller's description; {src}."),
           "Name": item_names(it, src)}
    maker = it
    while maker.get("resale_of"):
        maker = ITEM[maker["resale_of"]]
    msrc = f"item {maker['id']} of {PARTY[maker['seller']]['identity']['name']} (world/items.json)"
    if maker.get("pack"):
        out["PackQuantity"] = V(maker["pack"]["quantity"], "One pack of this item.", unitCode="EA")
        out["PackSizeNumeric"] = V(maker["pack"]["size"], f"The units in one pack: {maker['pack']['size']} "
                                                          f"{'kg in a bale' if maker['unit'] == 'KGM' else 'in a bundle'}; "
                                                          f"{msrc}.")
    if maker.get("keywords"):
        out["Keyword"] = V(", ".join(maker["keywords"]), "The search string buyers find the item by, the maker's "
                                                          f"keywords in one element; {msrc}. A second Keyword would "
                                                          "have to be in another language (UBL rule IND7).")
    if maker.get("brand"):
        out["BrandName"] = V(maker["brand"], f"The brand the maker sells the item under; {msrc}.")
    if maker.get("model"):
        out["ModelName"] = V(maker["model"], f"The model; {msrc}.")
    if maker.get("additional_info"):
        out["AdditionalInformation"] = V(maker["additional_info"], f"What comes with the item; {msrc}.")
    if catalogue:
        out["CatalogueIndicator"] = V("true", "The item is described as it appears in the seller's catalogue.")
    if maker.get("warranty"):
        out["WarrantyInformation"] = V(maker["warranty"], f"The maker's warranty; {msrc}.")
    bid, bwhy = buyer_item_id(iid, buyer) if buyer else (None, None)
    if bid:
        out["BuyersItemIdentification"] = {"ID": V(bid, bwhy)}
    out["SellersItemIdentification"] = {"ID": V(it["sellers_id"], f"The seller's own item number; {src}.")}
    variant = maker.get("variant", {})
    if variant.get("extended"):
        out["SellersItemIdentification"]["ExtendedID"] = V(variant["extended"], "The variant of the item: the "
                                                                                "frame colour, added to the item number.")
    if variant.get("attribute"):
        a_, code, desc = variant["attribute"]
        out["SellersItemIdentification"]["PhysicalAttribute"] = {
            "AttributeID": V(a_, "The attribute the variant differs in."),
            "PositionCode": V("FRM", "The part of the item the attribute is on: the frame."),
            "DescriptionCode": V(code, "The variant's code for it."),
            "Description": V(desc, "The variant in words.")}
    if variant.get("measure"):
        a_, v, u = variant["measure"]
        out["SellersItemIdentification"]["MeasurementDimension"] = {
            "AttributeID": V(a_, "The seller numbers its slats by length: this number is for one length."),
            "Measure": V(v, "The length the number stands for.", unitCode=u)}
    if catalogue:
        out["CatalogueItemIdentification"] = {"ID": V(f"{catalogue[0]}-{catalogue[1]}", "The item's place in the "
                                                      "catalogue: the catalogue number and the line.")}
    if it.get("resale_of"):        # a resold item carries the maker's identifiers, customs code and origin
        out["ManufacturersItemIdentification"] = {"ID": V(maker["sellers_id"], f"The item number of the maker, "
                                                          f"{PARTY[maker['seller']]['identity']['name']}: the "
                                                          f"reseller's item is resale of item {maker['id']}.")}
    gtin = it                          # the GTIN: the item's own, or one allocated further up the resale chain
    while gtin and not gtin.get("gtin"):
        gtin = ITEM.get(gtin.get("resale_of"))
    codana = {"ID": V(maker["standard_id"], "The Codana item number of the maker, issued by the Codana "
                      "Identification Agency, Urvania's public numbering body: twelve digits with a check digit, a "
                      f"number of the world, not a GTIN; {msrc}.", schemeID="urn:ubl-examples:world:item")} \
        if maker.get("standard_id") else None
    if gtin:
        owner = PARTY[gtin["seller"]]["identity"]["name"]
        out["StandardItemIdentification"] = {"ID": V(gtin["gtin"], (
            f"The GTIN {owner} gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves "
            "that prefix for demonstrations and examples, so the number belongs to no real product"
            + (f"; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate "
               "the GTIN where the brand owner has none" if gtin is not maker else "")
            + f" (world/items.json)."), schemeID="GS1 GTIN")}
        if codana:
            out["AdditionalItemIdentification"] = {"ID": V(maker["standard_id"], "The maker's own number for the "
                                                           "item, its Codana item number, which travels along with "
                                                           f"the GTIN; {msrc}.", schemeID="urn:ubl-examples:world:item")}
    elif codana:
        out["StandardItemIdentification"] = codana
        if maker.get("barcode"):
            out["StandardItemIdentification"]["BarcodeSymbologyID"] = V(maker["barcode"], "The barcode the number "
                                                                        "is printed in on the label.")
            out["StandardItemIdentification"]["IssuerScopeID"] = V(maker["standard_id"][:3], "The range of item "
                                                                   "numbers the agency gives out in the maker's "
                                                                   "country.")
    if catalogue_ref:
        out["CatalogueDocumentReference"] = {"ID": V(catalogue_ref, "The catalogue the item was ordered from.")}
    if maker.get("spec_doc"):
        out["ItemSpecificationDocumentReference"] = {"ID": V(maker["spec_doc"], "The maker's datasheet with drawings "
                                                                                "and assembly instructions.")}
    if it.get("lifecycle"):
        out["LifecycleStageCode"] = V(it["lifecycle"][0], "The stage of the product's life the item belongs to.")
        out["LifecycleStageDescription"] = V(it["lifecycle"][1], "The stage in words.")
    if maker.get("hs"):
        ccs = [{"ItemClassificationCode": V(maker["cpc"], "What the item is, as a subclass of the UN Central Product "
                                                          f"Classification (CPC), the trade classification for goods and "
                                                          f"services; {msrc}."),
                "CommodityCode": V(maker["hs"], "The Harmonized System subheading of the World Customs Organization, "
                                                f"six digits, for customs and trade statistics; {msrc}.")}]
        if maker.get("national_tariff"):
            cc = WORLD["countries"][maker["origin"]]
            ccs.append({"CommodityCode": V(maker["national_tariff"], f"The national tariff code of {cc['name']}, two "
                                                                     "digits below the HS subheading, as its customs "
                                                                     f"uses it: a second classification; {msrc}.",
                                           listID=codelists.NATIONAL.format(maker["origin"], "CustomsTariff"))})
        out["CommodityClassification"] = ccs
    if tax:
        out["ClassifiedTaxCategory"] = tax
    props = []
    for pr in maker.get("properties", []):
        props.append(item_property(pr, msrc))
    for name, value, unit in maker.get("quantity_properties", []):
        props.append({"Name": V(name, "A measured property of the item."),
                      "ValueQuantity": V(value, f"Its measured value; {msrc}.", unitCode=unit)})
    if props:
        out["AdditionalItemProperty"] = props
    if it.get("resale_of"):
        out["ManufacturerParty"] = party(maker["seller"], short=True)
        if catalogue:
            out["InformationContentProviderParty"] = party(maker["seller"], short=True)
    if it.get("conditions"):
        tc = it["conditions"]
        out["TransactionConditions"] = {"ID": V(tc["id"], "The seller's number for these conditions of sale."),
                                        "Description": V(tc["description"], "The conditions in words."),
                                        "DocumentReference": {"ID": V(tc["doc"], "The seller's general terms of "
                                                                                 "trade.")}}
    if maker.get("origin_region"):
        out["OriginAddress"] = {"Region": V(maker["origin_region"], "Where on the island the cotton was grown."),
                                "Country": {"IdentificationCode": V(maker["origin"], "The country of origin.")}}
    if instance:
        out["ItemInstance"] = instance
    if maker.get("certificate"):
        ce = maker["certificate"]
        reg = ce.get("register") and world_ids.national_scheme(maker["origin"], ce["register"])
        cert = {"ID": V(ce["id"], "The number of the certificate" + (
                    f", in the {SCHEMES[reg]['name']}, which keeps the certificates issued under each registration; "
                    "the schemeID names the register and its authority, so no issuer party is needed (decision "
                    "ID-Q10)." if reg else ", unique only with its issuer, who is named below (decision ID-Q10)."),
                    **({"schemeID": reg} if reg else {})),
                "CertificateTypeCode": V(ce["code"], "The kind of certificate, as a code."),
                "CertificateType": V(ce["type"], "The kind of certificate, in words."),
                "Remarks": V(ce["remarks"], "What the certificate states about the goods.")}
        if ce.get("issuer"):
            cert["IssuerParty"] = party(ce["issuer"], short=True)
        if ce.get("valid_until"):
            cert["CertificateValidityPeriod"] = {"EndDate": V(ce["valid_until"], "The certificate is valid until then.")}
        if ce.get("reference_id"):
            cert["CertificateReferenceID"] = V(ce["reference_id"], "The registration the certificate is issued under: "
                                                                   "the sawmill's own number in the same register, "
                                                                   "which the certificate's number repeats after its "
                                                                   "year.", **({"schemeID": reg} if reg else {}))
        if ce.get("category"):
            cert["ApplicableCategoryCode"] = V(ce["category"][0], "The category of goods the certificate covers.")
            cert["ApplicableCategory"] = V(ce["category"][1], "The category in words.")
        if ce.get("uri"):
            cert["CertificateURI"] = V(ce["uri"], "Where the certificate can be checked.")
        if ce.get("document"):
            cert["DocumentReference"] = {"ID": V(ce["document"], "The audit report the certificate is based on.")}
        if ce.get("signature"):
            sg = ce["signature"]
            cert["Signature"] = {"ID": V(sg["id"], "The signature's identifier."),
                                 "Note": V(sg["note"], "Who signed."),
                                 "ValidationDate": V(sg["date"], "The day the signature was placed."),
                                 "SignatoryParty": party(sg["signatory"], short=True)}
        out["Certificate"] = cert
    if maker.get("env_certificate"):
        ce = maker["env_certificate"]
        out["EnvironmentalCertificate"] = {"ID": V(ce["id"], "The number of the environmental certificate, unique "
                                                             "only with its issuer, who is named with it (decision "
                                                             "ID-Q10)."),
                                           "CertificateTypeCode": V(ce["code"], "The kind of claim, as "
                                                                                                 "a code."),
                                           "CertificateType": V(ce["type"], "The environmental claim certified."),
                                           "Remarks": V(ce["remarks"], "What the certificate states."),
                                           "IssuerParty": party(ce["issuer"], short=True)}
    if maker.get("dimensions"):
        dims = []
        for dm in maker["dimensions"]:
            a_, v, u = dm[:3]
            x = {"AttributeID": V(a_, "Which dimension."), "Measure": V(v, "Its size.", unitCode=u)}
            if len(dm) > 3:
                x["Description"] = V(dm[3], "Where it is measured.")
            if len(dm) > 4:
                x["MinimumMeasure"] = V(dm[4], "The lowest it can be set to.", unitCode=u)
                x["MaximumMeasure"] = V(dm[5], "The highest it can be set to.", unitCode=u)
            dims.append(x)
        out["Dimension"] = dims
    if maker.get("circularity"):
        ci = maker["circularity"]
        circ = {}
        if ci.get("type"):
            circ["CircularityTypeCode"] = V(ci["type"], "The circular strategy behind the item.")
        if ci.get("recycled"):
            circ["RecycledContentPercent"] = V(ci["recycled"], "The share of recycled material: the film is made from "
                                                               "the recycled granulate.")
        if ci.get("recyclable"):
            circ["RecyclabilityPercent"] = V(ci["recyclable"], "The share that can be recycled again.")
        if ci.get("maintenance"):
            circ["MaintenanceFrequencyCode"] = V(ci["maintenance"], "How often the item needs maintenance.")
            circ["MaintenanceFrequencyDescription"] = V(ci["maintenance_description"], "What the maintenance is.")
        if ci.get("resources"):
            circ["ResourceConsumption"] = [{"ResourceTypeCode": V(r, "A material the item is made of."),
                                            "ConsumptionMeasure": V(q, "How much of it one item uses.", unitCode=u),
                                            "ResourceOriginDescription": V(o, "Where the material comes from."),
                                            "MeasurementPeriod": {"StartDate": V("2025-01-01", "Measured over the "
                                                                                               "production of 2025."),
                                                                  "EndDate": V("2025-12-31", "Its last day.")}}
                                           for r, q, u, o in ci["resources"]]
        if ci.get("repairability"):
            circ["RepairabilityScore"] = {"ScoreNumeric": V(ci["repairability"], "Side frames and slats can be "
                                                            "replaced one by one, which is why the spare side frame "
                                                            "exists."),
                                          "ScoringSystemCode": V(ci["repairability_system"], "The scale of the score.")}
        if ci.get("waste"):
            wt, wd, wq, wu = ci["waste"]
            circ["WasteGenerated"] = {"WasteTypeCode": V(wt, "The kind of waste the item leaves."),
                                      "WasteTypeDescription": V(wd, "The waste in words."),
                                      "WasteMeasure": V(wq, "How much of it per item.", unitCode=wu),
                                      "MeasurementPeriod": {"StartDate": V("2025-01-01", "Measured over the "
                                                                                       "deliveries of 2025."),
                                                            "EndDate": V("2025-12-31", "Its last day.")}}
        if ci.get("product_doc"):
            circ["ProductDocumentationDocumentReference"] = {"ID": V(ci["product_doc"], "The repair and maintenance "
                                                                                        "manual.")}
        if ci.get("end_of_life"):
            circ["EndOfLifeTreatment"] = {"TreatmentPathwayCode": V(ci["end_of_life"], "What happens to the item "
                                                                                       "after use.")}
            if ci.get("end_of_life_detail"):
                d = ci["end_of_life_detail"]
                circ["EndOfLifeTreatment"].update({
                    "ProcessingTypeCode": V(d["processing"], "How the used item is processed."),
                    "ImpactCode": V(d["impact"], "The environmental impact of that end of life: "
                                                   f"{d['impact_note']}."),
                    "TreatmentLocation": {"Name": V(d["where"], "Where it is treated."),
                                          "Address": {"Country": {"IdentificationCode": V(d["country"], "Its "
                                                                                                       "country.")}}}})
        out["CircularityProfile"] = circ
    if maker.get("hazard"):
        out["HazardousRiskIndicator"] = V("true", "The item is dangerous goods.")
        out["HazardousItem"] = hazardous_item(maker)
    if maker.get("emission"):
        em = maker["emission"]
        out["EnvironmentalEmission"] = {
            "EnvironmentalEmissionTypeCode": V(em["type"], "The emission reported: greenhouse gases as CO2 equivalent."),
            "ValueMeasure": V(em["value"], "The emission of one item.", unitCode=em["unit"]),
            "ValueFactorNumeric": V(em["factor"], "The share of the footprint the steel frame accounts for."),
            "ValueBaseMeasure": V(em["base"][0], "The emission is per one bench.", unitCode=em["base"][1]),
            "Description": V(em["description"], "What the figure includes."),
            "EmissionStandardReference": V(em["standard"], "The standard the footprint is calculated by."),
            "LifecycleStageCode": V(em["stage"], "The part of the bench's life the figure covers."),
            "LifecycleStageDescription": V(em["stage_desc"], "That part in words."),
            "EmissionCalculationMethod": {"CalculationMethodCode": V(em["method"]["code"], "Calculated, not measured."),
                                          "FullnessIndicationCode": V(em["method"]["fullness"], "How much of the "
                                                                      "chain is included."),
                                          "EmissionFactorSource": V(em["method"]["source"], "Where the factors come "
                                                                                            "from."),
                                          "EmissionFactorDocumentReference": {"ID": V(em["method"]["doc"], "The "
                                                                              "report with the emission factors.")}},
            "MeasurementPeriod": {"StartDate": V(em["period"][0], "The year the figures are from."),
                                  "EndDate": V(em["period"][1], "Its last day.")}}
    if it.get("origin") or maker.get("origin"):
        out["OriginCountry"] = {"IdentificationCode": V(maker["origin"], f"Where the item was produced; {msrc}.")}
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
                given = node.get(step) if isinstance(node.get(step), list) else []
                node[step] = [merge(given[i] if i < len(given) else {},
                                    party(x) if target == "Party" else {"Party": party(x)}) for i, x in enumerate(pid)]
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
    if abie == "AllowanceCharge" and "AllowanceChargeReasonCode" not in content:
        raise SystemExit(f"{path}: every allowance and charge carries its reason as a code (decision Q3)")
    content = with_code_lists(content, path, bbies)
    content = with_schemes(content, path)
    for name in [b[0] for b in spec["bbies"]]:                    # basic properties first, in model order
        if name not in content:
            continue
        if bbies[name][2]:
            raise SystemExit(f"{path}/{name}: deprecated in UBL 2.5")
        for v in content[name] if isinstance(content[name], list) else [content[name]]:
            if not isinstance(v, V) or not v.why:
                raise SystemExit(f"{path}/{name}: every value needs a reason")
            attrs = {k: language_tag(x) if k == "languageID" else str(x) for k, x in v.attrs.items()}
            e = etree.SubElement(el, f"{{{NS_CBC}}}{name}", attrs)
            e.text = str(v.value)
            reasons.append((f"{path}/{name}", e.text, attrs, v.why))
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


def language_tag(code):
    """The languageID of a text: the sender tags its English with its own country as the region (BCP 47 en-XU, en-XB,
    en-XL; RFC 5646 reserves the region subtags XA to XZ for private use); the national languages stay qau and qal."""
    return f"en-{PARTY[SENDER]['c']}" if code == "en" and SENDER else code


# ---------------------------------------------------------------- code lists
SENDER = None          # the sender of the document being built: its country decides the languages of code names
UNBOUND = {}           # code elements no binding covers yet: (element, parent) -> first place


def unlisted(element, parent):
    return next((u for u in codelists.load()["unlisted"] if u["element"] == element
                 and (not u.get("parents") or parent in u["parents"])), None)


def with_code_lists(content, path, bbies):
    """Every code of an element gets its list (world/codelists/lists.json): the value must be a code of the list,
    exactly; the element gets the list's listID, and its reason says what the code means in the list. A text
    partner of the code (CertificateType beside CertificateTypeCode) carries the list's name for the code, in the
    languages of the sender's country where the element may repeat."""
    parent = path.split("/")[-1]
    siblings = {k: v.value for k, v in content.items() if isinstance(v, V)}
    out = dict(content)
    for name, val in content.items():
        if name not in bbies or unlisted(name, parent):
            continue
        if not name.endswith("Code") and not codelists.id_bound(name):
            continue
        b = codelists.binding(name, parent, siblings)
        if b is None:
            if name.endswith("Code"):
                UNBOUND.setdefault((name, parent), f"{path}/{name}")
            continue
        key = b.get("attribute", "listID")      # a code held in an identifier names its list in schemeID (ID-Q2)
        coded = []
        for v in val if isinstance(val, list) else [val]:
            lst = codelists.choose(b, v.value, v.attrs.get(key))
            if lst is None:
                raise SystemExit(f"{path}/{name}: '{v.value}' is not a code of "
                                 f"{' or '.join(codelists.load()['lists'][k]['listID'] or k for k in b['lists'])} "
                                 "(world/codelists/lists.json)")
            attrs = {key: lst["listID"], **{k: x for k, x in v.attrs.items() if k != key}}
            if not lst["listID"]:
                raise SystemExit(f"{path}/{name}: the list {lst['key']} has no listID")
            meaning = lst["codes"][v.value]["name"]
            held = (f" An identifier that holds a code names the code's list in its schemeID." if key == "schemeID"
                    else "")
            coded.append(V(v.value, f"{v.why} The code is from {codelists.describe(lst)}: {v.value}"
                                    + (f" = {meaning}." if meaning and meaning != v.value else ".") + held, **attrs))
        out[name] = coded if isinstance(val, list) else coded[0]
        text = b.get("text")
        if text and text in content and not isinstance(val, list):
            lst = codelists.choose(b, val.value, out[name].attrs["listID"])
            given = content[text]
            detail = given.value if isinstance(given, Detail) else None
            case = given.why[0].lower() + given.why[1:] if given.why[1:2].islower() else given.why
            why = f"The name of code {val.value} in {codelists.describe(lst)}" + (
                f", followed by the detail of this case: {case.rstrip('.')}." if detail else ".")
            langs = [l for l in WORLD["countries"][PARTY[SENDER]["c"]]["languages"] if l != "en"] \
                if SENDER and bbies[text][1].endswith("n") else []
            langs = [l for l in langs if l in codelists.LANGS.get(lst["scope"], [])]

            def words(lang):
                t = codelists.name_in(lst, val.value, lang)
                if not detail:
                    return t
                d = detail if lang == "en" else translate(detail, lang)
                return f"{t}: {d[0].lower() + d[1:] if detail[0].islower() else d}"
            if langs:
                out[text] = [V(words(l), f"{why} In {WORLD['languages'][l]['name']}, the sender's language.",
                               languageID=l) for l in langs] + \
                            [V(words("en"), f"{why} In English.", languageID="en")]
            else:
                out[text] = V(words("en"), why)
    return out


# ---------------------------------------------------------------- identifier schemes (decisions ID-Q1 to ID-Q4)
# identifiers that come from a scheme: (element, parent) -> the scheme, a schemeID of world/countries.json or a kind
# of national scheme (the country whose format the value fits); a code held in an identifier is not here: its
# schemeID is its code list's listID (with_code_lists)
SCHEME_RULES = {
    ("CompanyID", "PartyLegalEntity"): "register", ("BusinessIdentityEvidenceID", "MainQualifyingParty"): "register",
    ("CompanyID", "PartyTaxScheme"): "tax",
    ("ParticipantID", "DigitalDeliveryChannel"): "urn:ubl-examples:world:endpoint",
    ("PaymentID", "PaymentMeans"): "ISO 11649",
    ("ID", "SecurityListing"): "ISO 6166", ("SecurityID", "ImmobilizedSecurity"): "ISO 6166",
    ("ID", "StandardPropertyIdentification"): "property",
    ("LicensePlateID", "RoadTransport"): "vehicle-register", ("TrailerLicensePlateID", "RoadTransport"): "vehicle-register",
    ("ID", "AttachedTransportEquipment"): "vehicle-register",
    ("AircraftID", "AirTransport"): "aircraft-register",
    ("RailCarID", "RailTransport"): "rail-vehicle-register", ("ID", "ContainedInTransportEquipment"): "rail-vehicle-register",
}
CONTAINERS = ("TransportEquipment", "ContainingTransportEquipment", "ReferencedTransportEquipment", "GoodsItemContainer")
SCHEMES = world_ids.registry(WORLD)


def scheme_for(element, parent, value):
    """The schemeID an identifier takes, or None for a local identifier."""
    rule = SCHEME_RULES.get((element, parent))
    if element == "ID" and parent in CONTAINERS and re.fullmatch(SCHEMES["ISO6346"]["pattern"], value):
        rule = "ISO6346"
    if rule is None or rule in SCHEMES:
        return rule
    cc = world_ids.country_of(WORLD, rule, value)
    if cc is None:
        raise SystemExit(f"{parent}/{element}: '{value}' fits no country's {rule} format (world/countries.json)")
    return world_ids.national_scheme(cc, rule)


def with_schemes(content, path):
    """Every identifier from a scheme names it in schemeID; its reason says which scheme it is."""
    parent = path.split("/")[-1]
    out = dict(content)
    for name, val in content.items():
        vals = val if isinstance(val, list) else [val]
        if not all(isinstance(v, V) for v in vals) or not name.endswith("ID"):
            continue
        new = []
        for v in vals:
            sid = v.attrs.get("schemeID") or scheme_for(name, parent, str(v.value))
            if sid and "schemeID" not in v.attrs and sid in SCHEMES:
                v = V(v.value, f"{v.why} The schemeID names the scheme it is from: the {SCHEMES[sid]['name']} "
                               f"({SCHEMES[sid].get('format', '')}).", **{**v.attrs, "schemeID": sid})
            new.append(v)
        out[name] = new if isinstance(val, list) else new[0]
    return out


def check_schemes(root, where):
    """Every identifier with a schemeID fits its scheme (world/countries.json): its format and check digit. A
    schemeID that is a code list's listID (a code in an identifier) is checked by the code list validation."""
    list_ids = {l["listID"] for l in codelists.load()["lists"].values()}
    for e in root.iter(f"{{{NS_CBC}}}*"):
        sid = e.get("schemeID")
        if sid is None or sid in list_ids:
            continue
        if sid not in SCHEMES:
            raise SystemExit(f"{where}: {etree.QName(e).localname} = {e.text}: schemeID {sid} is not a scheme of the "
                             "world (world/countries.json)")
        why = world_ids.problem(SCHEMES[sid], e.text)
        if why:
            raise SystemExit(f"{where}: {root.getroottree().getpath(e)}: {why}")


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


MISSING_WORDS = world_data.MISSING_WORDS
translate = world_data.translate


def bilingual_notes(doc, content):
    """Documents from Urvania and the island give their notes in the country's language and in English, the working
    language between the countries: one cbc:Note per language, each with its languageID."""
    code = WORLD["countries"][PARTY[doc["from"]]["c"]]["languages"][0]
    if code == "en" or "Note" not in content:
        return
    notes = content["Note"] if isinstance(content["Note"], list) else [content["Note"]]
    name = WORLD["languages"][code]["name"]
    out = []
    for v in notes:
        if not isinstance(v, V):
            out.append(v)
            continue
        out.append(V(translate(v.value, code), f"The note in {name}, the sender's language (world/countries.json): "
                                               f"{v.why}", languageID=code))
        out.append(V(v.value, f"The same note in English, the working language between the countries: {v.why}",
                     languageID="en"))
    content["Note"] = out


TEXT_BBIES = set(MODEL["text_bbies"])     # cbc elements of a text type (Text or Name): they carry languageID


def check_instance_rules(root, where):
    """The UBL 2.5 instance rules of section 4 that a schema cannot check:
    IND5  no element is devoid of content: an aggregate needs a child, a basic element text (whitespace alone is
          empty);
    IND7  no two sibling elements of a text type with the same name have the same languageID;
    IND8  no two sibling elements of a text type with the same name both have no languageID;
    IND9  no attribute is empty.
    The text types are the basic properties whose data type in the UBL 2.5 model is Text or Name: their schema
    types (udt:TextType, udt:NameType) are the ones that derive from the CCTS TextType and carry languageID
    (world/ubl-model.json, text_bbies)."""
    for el in root.iter():
        if not isinstance(el.tag, str):
            continue
        path = root.getroottree().getpath(el)
        if len(el) == 0 and not (el.text or "").strip():
            raise SystemExit(f"{where}: {path}: empty element (UBL rule IND5)")
        for k, v in el.attrib.items():
            if not v.strip():
                raise SystemExit(f"{where}: {path}/@{etree.QName(k).localname}: empty attribute (UBL rule IND9)")
        seen = {}
        for c in el:
            if not isinstance(c.tag, str):
                continue
            q = etree.QName(c)
            if q.namespace != NS_CBC or q.localname not in TEXT_BBIES:
                continue
            lang = c.get("languageID")
            key = (q.localname, lang)
            if key in seen:
                rule = "IND8: both without languageID" if lang is None else f"IND7: both with languageID {lang}"
                raise SystemExit(f"{where}: {path}: two {q.localname} elements (UBL rule {rule})")
            seen[key] = c


DOC_UUIDS = {}      # (flow, document ID) -> the UUID the document carries, for references to it


def document_uuid(flow_id, n, doc_type):
    """The UUID of document n of a flow: version 5, derived from its place in the world, so stable."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:ubl-examples:world:{flow_id}:{n}:{doc_type}"))


def referenced_uuid(flow_id, doc_id):
    """The UUID of an earlier document of the flow, as that document states it: a reference quotes it."""
    if (flow_id, doc_id) not in DOC_UUIDS:
        raise SystemExit(f"{flow_id}: a reference quotes the UUID of {doc_id}, which is not an earlier document "
                         "of the flow")
    return DOC_UUIDS[(flow_id, doc_id)]


def check_reference_uuids(flow_id, roots):
    """Every reference (an element with an ID and a UUID) to a document of the same flow carries that document's
    UUID."""
    own = {}
    for name, root in roots:
        own.setdefault(root.findtext(f"{{{NS_CBC}}}ID"), set()).add(root.findtext(f"{{{NS_CBC}}}UUID"))
    for name, root in roots:
        for el in root.iter(f"{{{NS_CAC}}}*"):
            rid, ruuid = el.findtext(f"{{{NS_CBC}}}ID"), el.findtext(f"{{{NS_CBC}}}UUID")
            if rid in own and ruuid is not None and ruuid not in own[rid]:
                raise SystemExit(f"world/examples/{flow_id}/{name}: {etree.QName(el).localname} refers to {rid} "
                                 f"with UUID {ruuid}, but that document's UUID is {', '.join(sorted(own[rid] - {None}))}")


VERSIONS = json.load(open(os.path.join(world_data.ROOT, "world", "ubl-versions.json"), encoding="utf-8"))
VERSION_ORDER = ["2.0", "2.1", "2.2", "2.3", "2.4", "2.5"]


def ubl_version(root):
    """The earliest UBL 2 version that defines every element of the document (UBLVersionID: "Identifies the earliest
    version of the UBL 2 schema for this document type that defines all of the elements that might be encountered in
    the current instance"), from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json), and the element
    that needs it."""
    doc = etree.QName(root).localname
    best, why = VERSIONS["documents"][doc], f"the document type {doc}"

    def walk(el, abie, path):
        nonlocal best, why
        for c in el:
            if not isinstance(c.tag, str):
                continue
            name = etree.QName(c).localname
            v = VERSIONS["children"].get(abie, {}).get(name)
            if v is None:
                raise SystemExit(f"{path}/{name}: not in any published UBL 2 model (world/ubl-versions.json)")
            if VERSION_ORDER.index(v) > VERSION_ORDER.index(best):
                best, why = v, f"{abie}/{name}"
            if etree.QName(c).namespace == NS_CAC:
                walk(c, next(a[1] for a in MODEL["abies"][abie]["asbies"] if a[0] == name), f"{path}/{name}")
    walk(root, doc, doc)
    return best, why


def set_ubl_version(root, reasons):
    version, why = ubl_version(root)
    el = root.find(f"{{{NS_CBC}}}UBLVersionID")
    el.text = version
    k = next(i for i, r in enumerate(reasons) if r[0].endswith("/UBLVersionID"))
    reasons[k] = (reasons[k][0], version, reasons[k][2],
                  f"The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: "
                  f"computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); {why} first "
                  f"appears in UBL {version}.")


def check_specifications(root, where):
    """Every CustomizationID and ProfileID the document uses, at every level of a #compliant# chain, is a
    specification the world describes (world/specifications.json)."""
    known = world_specs.described()
    for e in root.iter(f"{{{NS_CBC}}}CustomizationID", f"{{{NS_CBC}}}ProfileID"):
        for part in e.text.split(world_specs.COMPLIANT):
            if part not in known:
                raise SystemExit(f"{where}: {etree.QName(e).localname} {part} is not described in "
                                 "world/specifications.json")


UNIT_SCHEMES = ("GS1 SSCC", "ISO 15459")


def check_unit_ids(flow_id, roots):
    """A logistic unit has one identifier in its maker's convention (decision ID-Q7), and every document of the flow
    that mentions it agrees: the same value always carries the same schemeID, and where two documents give the
    unit's package count, the counts agree."""
    seen, counts = {}, {}
    for name, root in roots:
        for e in root.iter(f"{{{NS_CBC}}}ID"):
            parent = e.getparent()
            sid = e.get("schemeID")
            if sid not in UNIT_SCHEMES and e.text not in seen:
                continue
            if seen.setdefault(e.text, (sid, name))[0] != sid:
                raise SystemExit(f"world/examples/{flow_id}/{name}: unit {e.text} with schemeID {sid}, but "
                                 f"{seen[e.text][1]} gives it {seen[e.text][0]}")
            total = parent.findtext(f"{{{NS_CBC}}}TotalPackageQuantity")
            if total is not None:
                if counts.setdefault(e.text, (total, name))[0] != total:
                    raise SystemExit(f"world/examples/{flow_id}/{name}: unit {e.text} holds {total} packages, but "
                                     f"{counts[e.text][1]} says {counts[e.text][0]}")


# ---------------------------------------------------------------- air legs: the aircraft's capacity, DG stowage
LITHIUM_IA = {"3480", "3090"}                        # PI 965 / PI 968, section IA or IB (IATA DGR 9.3.2.1.3)
LITHIUM_APART = ("1", "2.1", "3", "4.1", "5.1")      # labels lithium batteries are kept apart from (1.4S excepted)
NO_SEGREGATION = ("1.4S", "6", "7", "9")             # not in IATA DGR Table 9.3.A (note 1)


def labels(it):
    """The hazard labels of an item's package: its class and its subsidiary hazard."""
    hz = it.get("hazard")
    return [hz["class"]] + ([hz["sub"]] if hz.get("sub") else []) if hz else []


def air_load_problems(world, deals):
    """Every air leg's load fits the aircraft of its carrier (world/parties.json, fleet capacity and ULD types):
    payload, volume, LD3 positions, each ULD's maximum gross weight, the cargo door for bulk pieces, every item of the
    flow's deal loaded once; and the dangerous goods are stowed as the IATA DGR asks: lithium batteries of PI 965/968
    section IA apart from class 1 (not 1.4S), 2.1, 3, 4.1 and 5.1 labels, not in the same ULD nor in a position next to
    it (9.3.2.1.3), and two classes of Table 9.3.A in one ULD only where the world has checked the table (none yet)."""
    out = []
    party = {p["id"]: p for p in world["parties"]}
    for f in world["flows"]:
        for leg in f.get("legs", []):
            if leg["mode"] != "air":
                continue
            where = f"flow {f['id']}: air leg {leg['from']} -> {leg['to']}"
            plane = next(v for v in party[leg["carrier"]].get("fleet", []) if v["kind"] == "air")
            cap, types = plane["capacity"], plane["ulds"]
            load = leg.get("load")
            if load is None:
                out.append(f"{where}: no load (ulds, bulk) given")
                continue
            deal = {d["item"]: Decimal(str(d["ordered"])) for d in deals[f["id"]]}
            placed = [i for u in load["ulds"] for i in u["items"]] + load["bulk"]
            if sorted(placed) != sorted(deal):
                out.append(f"{where}: loads {sorted(placed)}, but the flow carries {sorted(deal)}")
                continue
            gross = {i: deal[i] * Decimal(str(maker_item(i, "gross_kg")["gross_kg"])) for i in deal}
            weight = sum(gross.values()) + sum(Decimal(types[u["type"]]["tare_kg"]) for u in load["ulds"])
            volume = Decimal("0")
            positions = [u["position"] for u in load["ulds"]]
            if len(positions) > len(cap["uld_positions"]) or len(set(positions)) != len(positions) or \
                    not set(positions) <= set(cap["uld_positions"]):
                out.append(f"{where}: ULD positions {positions} are not distinct positions of the aircraft")
            for u in load["ulds"]:
                t = types[u["type"]]
                g = sum(gross[i] for i in u["items"]) + t["tare_kg"]
                volume += Decimal(str(t["volume_m3"]))
                if g > t["max_gross_kg"]:
                    out.append(f"{where}: ULD {u['id']} weighs {g} kg, above its maximum of {t['max_gross_kg']} kg")
                if not u["id"].startswith(u["type"]):
                    out.append(f"{where}: ULD {u['id']} is not numbered as a {u['type']}")
            door = sorted(cap["door_mm"])
            for i in load["bulk"]:
                dims = {d[0]: Decimal(d[1]) for d in maker_item(i, "dimensions").get("dimensions", [])}
                if {"LENGTH", "DEPTH", "HEIGHT"} <= set(dims):
                    small = sorted([dims["LENGTH"], dims["DEPTH"], dims["HEIGHT"]])
                    if small[0] > door[0] or small[1] > door[1]:
                        out.append(f"{where}: {i} does not pass the cargo door {cap['door_mm']} mm")
                    volume += deal[i] * small[0] * small[1] * small[2] / Decimal(10 ** 9)
            if weight > cap["payload_kg"]:
                out.append(f"{where}: {weight} kg is above the payload of {cap['payload_kg']} kg")
            if volume > Decimal(str(cap["volume_m3"])):
                out.append(f"{where}: {volume} m³ is above the volume of {cap['volume_m3']} m³")
            index = {p: k for k, p in enumerate(cap["uld_positions"])}
            for u in load["ulds"]:
                table = {lb for i in u["items"] for lb in labels(ITEM[i]) if lb not in NO_SEGREGATION}
                if len({tuple(labels(ITEM[i])) for i in u["items"] if set(labels(ITEM[i])) & table}) > 1:
                    out.append(f"{where}: ULD {u['id']} mixes classes of IATA DGR Table 9.3.A; check the table")
                lithium = any(ITEM[i].get("hazard", {}).get("un", "")[2:] in LITHIUM_IA for i in u["items"])
                if not lithium:
                    continue
                for v in load["ulds"]:
                    near = v is u or abs(index[v["position"]] - index[u["position"]]) <= 1
                    bad = [i for i in v["items"] if any(lb == a or (a == "1" and lb[0] == "1" and lb != "1.4S")
                                                        for lb in labels(ITEM[i]) for a in LITHIUM_APART)]
                    if near and bad:
                        out.append(f"{where}: lithium batteries in {u['id']} next to {', '.join(bad)} in {v['id']} "
                                   "(IATA DGR 9.3.2.1.3)")
    return out


def maker_item(iid, key):
    """The item that carries a fact of the maker (its weight, its dimensions): the item itself, or the one it
    resells."""
    it = ITEM[iid]
    while it.get("resale_of") and key not in it:
        it = ITEM[it["resale_of"]]
    return it


def check_air_uld_ids(flow_id, roots):
    """A ULD a document of the flow names (a transport handling unit numbered as unit load devices are) is one of the
    ULDs its air legs load, and every ULD loaded is named where the flow lists handling units."""
    flow = next(f for f in WORLD["flows"] if f["id"] == flow_id)
    loaded = {u["id"] for leg in flow.get("legs", []) if leg.get("load") for u in leg["load"]["ulds"]}
    named = set()
    for name, root in roots:
        for thu in root.iter(f"{{{NS_CAC}}}TransportHandlingUnit"):
            tid = thu.findtext(f"{{{NS_CBC}}}ID")
            if tid and re.fullmatch(r"[A-Z]{3}\d{5}[A-Z0-9]{2}", tid):
                named.add(tid)
                if tid not in loaded:
                    raise SystemExit(f"world/examples/{flow_id}/{name}: ULD {tid} is not loaded on an air leg of the "
                                     "flow (world/documents.json)")
    if named and loaded - named:
        raise SystemExit(f"flow {flow_id}: ULDs {sorted(loaded - named)} are loaded but named in no document")


def xmlname(n, doc):
    return f"{n:02d}-{doc['doc']}.xml"


def main(flow_id, check=False):
    import examples_scenarios
    check_dangerous_goods_items()
    flow = next(f for f in WORLD["flows"] if f["id"] == flow_id)
    docs = [d for d in WORLD["documents"] if d["flow"] == flow_id]
    scenario = examples_scenarios.SCENARIOS[flow_id]
    out = os.path.join(world_data.ROOT, "world", "examples", flow_id)
    os.makedirs(out, exist_ok=True)
    stale, roots = [], []
    for n, doc in enumerate(docs, 1):
        content = scenario(n, doc)
        content = place_parties(doc, content)
        bilingual_notes(doc, content)
        for path, value in doc.get("values", {}).items():   # the world's manifest values must be what the scenario says
            node = content
            for step in path.split("/")[:-1]:
                node = node[step]
            got = node.get(path.split("/")[-1])
            if not isinstance(got, V) or got.value != value:
                raise SystemExit(f"{flow_id} {n} {doc['doc']}: {path} must be {value} (world/documents.json)")
        custom, levels = world_specs.customization(doc, WORLD)
        header = {"UBLVersionID": V("2.5", "Computed below from the elements the document uses."),
                  "CustomizationID": V(custom, "The specification the document follows, at each level it claims, "
                                       "chained with #compliant#: " + "; ".join(levels) + ". Each has a public "
                                       "description on the world's pages (world/specifications.json).")}
        own = {b[0] for b in MODEL["abies"][doc["doc"]]["bbies"]}
        if "ProfileID" in own:
            prof = world_specs.profile(doc)
            header["ProfileID"] = V(world_specs.urn("profile", prof), "The Trade Accord's process profile the document "
                                    f"belongs to: {world_specs.load()['profiles'][prof]['name'].lower()}, a generic, "
                                    "versioned profile, not the flow; the run of the process is the ProfileExecutionID.")
        if "ProfileExecutionID" in own:
            header["ProfileExecutionID"] = V(f"{flow_id.upper()}-2026-01", "This run of the process: the same in "
                                                                          "every document of the flow.")
        if "IssueTime" in own and "IssueTime" not in content:
            minutes = 8 * 60 + zlib.crc32(f"{flow_id}:{n}".encode()) % 600
            header["IssueTime"] = V(f"{minutes // 60:02d}:{minutes % 60:02d}:00", "The time the sender's system "
                                    "issued the document, in the sender's local time.")
        if "UUID" in own:
            header["UUID"] = V(document_uuid(flow_id, n, doc["doc"]),
                               "A universally unique identifier of the document, derived from its place in the world "
                               "(UUID version 5), so it stays the same on every build.")
        global SENDER
        SENDER = doc["from"]
        root, reasons = build(doc["doc"], merge(header, content))
        set_ubl_version(root, reasons)
        check_specifications(root, f"world/examples/{flow_id}/{xmlname(n, doc)}")
        if "UUID" in header and isinstance(content.get("ID"), V):
            DOC_UUIDS[(flow_id, content["ID"].value)] = header["UUID"].value
        roots.append((xmlname(n, doc), root))
        check_addresses(root, f"{flow_id} {n} {doc['doc']}")
        check_payment_means(root, f"{flow_id} {n} {doc['doc']}")
        check_dangerous_goods(root, f"{flow_id} {n} {doc['doc']}")
        check_classifications(root, f"{flow_id} {n} {doc['doc']}")
        check_formats(root, f"{flow_id} {n} {doc['doc']}")
        check_schemes(root, f"{flow_id} {n} {doc['doc']}")
        check_tax_exemption_lists(root, f"{flow_id} {n} {doc['doc']}", doc)
        check_instance_rules(root, f"world/examples/{flow_id}/{xmlname(n, doc)}")
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
    check_reference_uuids(flow_id, roots)
    check_air_uld_ids(flow_id, roots)
    check_unit_ids(flow_id, roots)
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


FLOWS_WITH_EXAMPLES = ["ore", "road", "rail", "plastics", "retail", "sea", "air", "cotton", "tender", "contest", "carnet",
                       "waste", "utilities", "wood", "furniture", "packaging", "mast", "energy"]


if __name__ == "__main__":
    import build_examples        # run through the module, so the scenarios share its classes
    args = [a for a in sys.argv[1:] if a != "--check"]
    ok = all([build_examples.main(f, check="--check" in sys.argv) for f in (args or FLOWS_WITH_EXAMPLES)])
    import examples_scenarios
    air = build_examples.air_load_problems(WORLD, {k: v.deal for k, v in examples_scenarios.FLOWS.items()})
    if air:
        print("\n".join(air), file=sys.stderr)
        ok = False
    for note in world_items.NOTES:         # HS 2022 subheadings the HS 2017 -> CPC table does not have
        print(f"note: {note}", file=sys.stderr)
    if build_examples.UNBOUND:
        print(f"code elements without a code list in world/codelists/lists.json ({len(build_examples.UNBOUND)}):",
              ", ".join(f"{e} in {p}" for e, p in sorted(build_examples.UNBOUND)), file=sys.stderr)
    if build_examples.MISSING_WORDS:
        print("words missing from the vocabularies of the world's languages (world/countries.json):",
              json.dumps(sorted(build_examples.MISSING_WORDS)), file=sys.stderr)
        ok = False
    sys.exit(0 if ok else 1)
