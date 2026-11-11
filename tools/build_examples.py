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
        code = WORLD["countries"][p["c"]]["languages"][0]
        if code == "en":
            out["Language"] = {"ID": V("en", "English, the language the party does business in."),
                               "Name": V("English", "The language's name."),
                               "LocaleCode": V(idn["language"], "The language as a code of UBL's language code list "
                                                                "(ISO 639).")}
        else:
            lang = WORLD["languages"][code]
            out["Language"] = {"ID": V(code, f"{lang['name']}, the language of {c['name']} and of the party; the code is "
                                             "from the range ISO 639 reserves for local use (qaa–qtz), as the world's "
                                             "languages are invented (world/countries.json)."),
                               "Name": V(lang["name"], f"The language's name in English; in the language itself: "
                                                       f"{lang['own_name']}.")}
    out["PostalAddress"] = address(pid)
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
               "TaxLevelCode": V("State" if scheme.get("levied_by") == "state" else "National",
                                 f"The level of government that levies the tax: {c['name']}'s "
                                 f"{scheme['name'].lower()} is levied by the "
                                 f"{'states' if scheme.get('levied_by') == 'state' else 'country'}.")}
        if idn.get("tax_exemption"):
            tax["ExemptionReason"] = V(idn["tax_exemption"], f"Why purchases by this party carry no sales tax; {src}.")
            code = next((v for k, v in c["tax"].get("exemption_codes", {}).items()
                         if idn.get("tax_exemption_kind") == k), None)
            if code:
                tax["ExemptionReasonCode"] = V(code, f"The exemption as a code of the world's exemption list "
                                                     f"(world/countries.json): {idn['tax_exemption_kind'].lower()}.")
            if idn.get("tax_registration_office"):
                tax["RegistrationAddress"] = {"CityName": V(idn["tax_registration_office"], "Where the party is "
                                                                                            "registered for the tax."),
                                              "CountrySubentity": V(idn["address"]["CountrySubentity"], "Its state."),
                                              "Country": {"IdentificationCode": V(p["c"], "Its country.")}}
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
        if ct.get("id"):
            contact = {"ID": V(ct["id"], "The desk's number in the party's own contact list."), **contact}
        if ct.get("job_title"):
            contact["JobTitle"] = V(ct["job_title"], f"The job of the person who answers at the desk; {src}.")
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
        out["ServiceProviderParty"] = {"ID": V(f"{pid}-SP-{sp['party']}", "The service contract between the two."),
                                       "ServiceTypeCode": V("Logistics", "The kind of service, as a code."),
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
    if le.get("registration_expires"):
        out["RegistrationExpirationDate"] = V(le["registration_expires"], "The island renews a farm's registration "
                                                                          "every year: it runs until this date.")
    if not idn.get("person"):
        out["CompanyLiquidationStatusCode"] = V("Active", "The register shows the company as active, not in "
                                                          "liquidation.")
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
    if a.get("ID"):
        out["ID"] = V(a["ID"], f"The address's number in the city's address register; {src}.")
    out["AddressTypeCode"] = V("Postal" if a.get("Postbox") else "Residential" if idn.get("person") else "Business",
                               "The kind of address.")
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
    code = c["languages"][0]
    if code != "en" and "en" in c["languages"] and isinstance(out.get("StreetName"), V):
        lang = WORLD["languages"][code]["name"]                 # a bilingual country names its streets twice
        st = out["StreetName"]
        out["StreetName"] = [V(translate(st.value, code, street=True), f"The street's name in {lang}: {c['name']} "
                               f"is officially bilingual, and street names are given in both languages "
                               f"(world/countries.json); {src}.", languageID=code),
                             V(st.value, f"The street's name in English, the island's other official language; "
                                         f"{src}.", languageID="en")]
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
           **({"AliasName": V(acc["alias"], "The short name the holder gave the account, shown in its bank's "
                                             "app.")} if acc.get("alias") else {}),
           **({"BlockchainID": V(acc["ledger"], "The account holds tokenised coral deposits on the Bank of Selanu's "
                                                "ledger, which Coral net settles on (world/countries.json).")}
              if acc.get("ledger") else {}),
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
                                             "FinancialInstitution": institution(acc["bank"]),
                                             "Address": {"CityName": V(bank["identity"]["address"]["CityName"],
                                                                       "The branch is at the bank's head office."),
                                                         "Country": {"IdentificationCode": V(bank["c"], "Its "
                                                                                                       "country.")}}}
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
        out["NameCode"] = V(pr["name_code"], "The property's name as a code, as the property standard lists it.")
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
        out["ListValue"] = [V(v, "One of the values the property can take.") for v in pr["list"]]
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
                                                 "IssuerScopeID": V(scope, "The part of the agency's standards it is "
                                                                           "taken from."),
                                                 "IssuerParty": party(issuer, short=True)}
    if pr.get("sub"):
        out["SubItemProperty"] = [item_property(x, src) for x in pr["sub"]]
    return out


def hazardous_item(it):
    """The dangerous goods data of an item (world/items.json), as the UN Model Regulations describe it."""
    hz = it["hazard"]
    out = {"ID": V(f"{it['sellers_id']}-DG", "The seller's dangerous goods record of the item."),
           "UNDGCode": V(hz["un"][2:], "The UN number of the UN Model Regulations.", listID="UNCL8273"),
           "ProperShippingName": V(hz["name"], "The proper shipping name."),
           "HazardClassID": V(hz["class"], "The UN hazard class."),
           "HazardousCategoryCode": V("UN", "Classified under the UN Model Regulations."),
           "EmergencyProceduresCode": V(hz.get("ems", "None"), "The emergency schedules for ships (EmS)."),
           "MedicalFirstAidGuideCode": V(hz["erg"], "The emergency response guide number."),
           "AdditionalInformation": V(hz.get("note", "Packed as the rules require."), "What the shipper adds."),
           "PlacardNotation": V(hz["class"], "The class shown on the placard."),
           "MarkingID": V(hz["un"], "The UN number marked on each package.")}
    if hz.get("label"):
        out["PlacardEndorsement"] = V(hz["label"], "The hazard label on the package.")
    if hz.get("pg"):
        out["UNPackingGroupCode"] = V(hz["pg"], "The packing group: medium danger.")
        out["UNPackingGroup"] = V("Medium danger", "In words.")
    if hz.get("tunnel"):
        out["TunnelRestrictionCode"] = V(hz["tunnel"], "The tunnel restriction code for road transport.")
    if hz.get("technical"):
        out["TechnicalName"] = V(hz["technical"], "The technical name, needed with an n.o.s. entry.")
    if hz.get("sub"):
        out["SecondaryHazard"] = {"ID": V(hz["sub"], "The subsidiary hazard: flammable."),
                                  "PlacardNotation": V(hz["sub"], "Shown on a second label."),
                                  "PlacardEndorsement": V("3", "The flammable liquid label."),
                                  "EmergencyProceduresCode": V("F-E", "The fire schedule."),
                                  "Extension": V("Subsidiary risk 3", "In words.")}
        out["FlashpointTemperature"] = {"AttributeID": V("Flashpoint", "Closed cup."),
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
        out["PackQuantity"] = V(maker["pack"]["quantity"], "One pack of this item.", unitCode="H87")
        out["PackSizeNumeric"] = V(maker["pack"]["size"], f"The units in one pack: {maker['pack']['size']} "
                                                          f"{'kg in a bale' if maker['unit'] == 'KGM' else 'in a bundle'}; "
                                                          f"{msrc}.")
    if maker.get("keywords"):
        out["Keyword"] = [V(k, "A word buyers search the item by.") for k in maker["keywords"]]
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
    if maker.get("standard_id"):
        out["StandardItemIdentification"] = {"ID": V(maker["standard_id"], "The world item number issued by the "
                                                     "identifier issuing agency, twelve digits with a check digit; a "
                                                     f"scheme of the world, not a GTIN; {msrc}.",
                                                     schemeID="urn:ubl-examples:world:item")}
        if maker.get("barcode"):
            out["StandardItemIdentification"]["BarcodeSymbologyID"] = V(maker["barcode"], "The barcode the number "
                                                                        "is printed in on the label.")
            out["StandardItemIdentification"]["IssuerScopeID"] = V(maker["standard_id"][:3], "The range of item "
                                                                   "numbers the agency gives out in the maker's "
                                                                   "country.")
    if maker.get("pack_standard_id"):
        out["AdditionalItemIdentification"] = {"ID": V(maker["pack_standard_id"], "The world item number of the "
                                                       f"pack of {maker['pack']['size']}, the unit the item is traded "
                                                       "in; the item number above is for one piece.",
                                                       schemeID="urn:ubl-examples:world:item")}
    if catalogue_ref:
        out["CatalogueDocumentReference"] = {"ID": V(catalogue_ref, "The catalogue the item was ordered from.")}
    if maker.get("spec_doc"):
        out["ItemSpecificationDocumentReference"] = {"ID": V(maker["spec_doc"], "The maker's datasheet with drawings "
                                                                                "and assembly instructions.")}
    if it.get("lifecycle"):
        out["LifecycleStageCode"] = V(it["lifecycle"][0], "The stage of the product's life the item belongs to.")
        out["LifecycleStageDescription"] = V(it["lifecycle"][1], "The stage in words.")
    if maker.get("hs"):
        cc = {"ItemClassificationCode": V(maker["hs"], "Harmonized System subheading of the World Customs "
                                                       f"Organization; {msrc}.", listID="HS")}
        if maker.get("national_tariff"):
            cc["CommodityCode"] = V(maker["national_tariff"], "The national tariff code below the HS subheading, as the "
                                                              "customs of the maker's country uses it.")
        out["CommodityClassification"] = cc
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
                                        "ActionCode": V(tc["action"], "To whom the conditions apply."),
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
        cert = {"ID": V(ce["id"], "The number of the certificate."),
                "CertificateTypeCode": V(ce["type"].replace(" ", ""), "The kind of certificate, as a code."),
                "CertificateType": V(ce["type"], "The kind of certificate, in words."),
                "Remarks": V(ce["remarks"], "What the certificate states about the goods.")}
        if ce.get("issuer"):
            cert["IssuerParty"] = party(ce["issuer"], short=True)
        if ce.get("valid_until"):
            cert["CertificateValidityPeriod"] = {"EndDate": V(ce["valid_until"], "The certificate is valid until then.")}
        if ce.get("reference_id"):
            cert["CertificateReferenceID"] = V(ce["reference_id"], "The certificate's number in the issuer's public "
                                                                   "register.")
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
        out["EnvironmentalCertificate"] = {"ID": V(ce["id"], "The number of the environmental certificate."),
                                           "CertificateTypeCode": V(ce["type"].replace(" ", ""), "The kind of claim, as "
                                                                                                 "a code."),
                                           "CertificateType": V(ce["type"], "The environmental claim certified."),
                                           "Remarks": V(ce["remarks"], "What the certificate states.")}
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
                    "ImpactCode": V(d["impact"], "The environmental impact of that end of life."),
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


MISSING_WORDS = set()


def translate(text, code, street=False):
    """A text in Urvanian (qau) or Lisavan (qal): the world's invented languages, word by word from their fixed
    vocabularies (world/countries.json). Names, numbers and codes stay as they are; Lisavan has no articles."""
    lex = WORLD["languages"][code].get("lexicon", {})
    out, start = [], True
    for tok in re.findall(r"[A-Za-z][A-Za-z'’]*|\S|\s+", text):
        if not tok[0].isalpha():
            out.append(tok)
            if tok in ".:;!?":
                start = True
            continue
        low = tok.lower()
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
    """Words of names, which a translation keeps: parties, places, countries, currencies, languages."""
    global PROPER
    if PROPER is None:
        names = [p["identity"]["name"] for p in WORLD["parties"]] + [t["name"] for t in WORLD["towns"]] + \
                [t["name"] for t in WORLD.get("localities", [])] + \
                [c["name"] for c in WORLD["countries"].values()] + \
                [c["currency"]["name"] for c in WORLD["countries"].values()] + \
                [x["name"] for x in WORLD["languages"].values()]
        PROPER = {w for n in names for w in re.findall(r"[A-Z][A-Za-z'’]*", n)} - COMMON_NAME_WORDS
    return PROPER


PROPER = None
COMMON_NAME_WORDS = set("""Accord Administration Agency Air Airport Bank Barges Board Border Brokers Cargo Chamber Coastal
Commerce Company Cotton Council Customs Department Distribution Energy Engineering Factoring Farm Forwarding Furniture
Gas Ginnery Grid Haulage Hub Identification Industries Information Insurance Intermodal Island Lines Logistics Maritime
Mill Mining Ocean Packaging Port Power Procurement Public Rail Recovery Review Sawmill Service State Stores Telecom
Terminal Textile Trade Trading Warehousing Water Works Coral Lume Ferra English""".split())   # ordinary words in names


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
        bilingual_notes(doc, content)
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
        own = {b[0] for b in MODEL["abies"][doc["doc"]]["bbies"]}
        if "ProfileID" in own:
            header["ProfileID"] = V(f"urn:ubl-examples:world:process:{flow_id}", "The business process the document "
                                    f"belongs to: the flow \"{flow['title']}\".")
        if "ProfileExecutionID" in own:
            header["ProfileExecutionID"] = V(f"{flow_id.upper()}-2026-01", "This run of the process: the same in "
                                                                          "every document of the flow.")
        if "IssueTime" in own and "IssueTime" not in content:
            minutes = 8 * 60 + zlib.crc32(f"{flow_id}:{n}".encode()) % 600
            header["IssueTime"] = V(f"{minutes // 60:02d}:{minutes % 60:02d}:00", "The time the sender's system "
                                    "issued the document, in the sender's local time.")
        if "UUID" in own:
            header["UUID"] = V(str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:ubl-examples:world:{flow_id}:{n}:"
                                                                  f"{doc['doc']}")),
                               "A universally unique identifier of the document, derived from its place in the world "
                               "(UUID version 5), so it stays the same on every build.")
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
                       "waste", "utilities", "wood", "furniture", "packaging", "mast", "energy"]


if __name__ == "__main__":
    import build_examples        # run through the module, so the scenarios share its classes
    args = [a for a in sys.argv[1:] if a != "--check"]
    ok = all([build_examples.main(f, check="--check" in sys.argv) for f in (args or FLOWS_WITH_EXAMPLES)])
    if build_examples.MISSING_WORDS:
        print("words missing from the vocabularies of the world's languages (world/countries.json):",
              json.dumps(sorted(build_examples.MISSING_WORDS)), file=sys.stderr)
        ok = False
    sys.exit(0 if ok else 1)
