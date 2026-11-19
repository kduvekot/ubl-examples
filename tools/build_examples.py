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
# ---------------------------------------------------------------- which desk of a party a document names (worklist C02)
# A party has desks by function (world/parties.json identity.desks); the role it plays in a document picks the desk.
ROLE_DESK = {
    "SellerSupplierParty": "sales", "ProviderParty": "sales", "BuyerCustomerParty": "purchasing",
    "OriginatorCustomerParty": "purchasing", "RetailerCustomerParty": "purchasing",
    "AccountingSupplierParty": "receivables", "PayeeParty": "receivables", "AccountingCustomerParty": "payables",
    "DeliveryParty": "goods_in", "DeliveryCustomerParty": "goods_in", "ConsigneeParty": "goods_in",
    "NotifyParty": "goods_in", "DespatchSupplierParty": "despatch", "DespatchParty": "despatch",
    "ConsignorParty": "despatch", "ShipperParty": "despatch",
    "ExporterParty": "customs", "ImporterParty": "customs", "TransitExporterParty": "customs",
    "CustomsAgentParty": "customs", "HolderParty": "customs", "RepresentativeParty": "customs",
    "CarrierParty": "operations", "TransportServiceProviderParty": "operations", "FreightForwarderParty": "operations",
    "TerminalOperatorParty": "operations", "SubstituteCarrierParty": "operations",
    "SendingLogisticsOperatorParty": "operations", "TransportUserParty": "logistics",
    "TendererParty": "tenders", "EconomicOperatorParty": "tenders", "WinningParty": "tenders",
    "MainQualifyingParty": "tenders", "AdditionalQualifyingParty": "tenders", "SubcontractorParty": "tenders",
    "ContractingParty": "procurement", "SubscriberParty": "payables", "CustomerParty": "payables",
}
TRANSPORT_DOCS = {"TransportExecutionPlan", "TransportExecutionPlanRequest", "Waybill", "TransportationStatus",
                  "TransportationStatusRequest", "TransportProgressStatus", "TransportProgressStatusRequest",
                  "GoodsItemItinerary", "TransportServiceDescription", "TransportServiceDescriptionRequest",
                  "CommonTransportationReport", "WeightStatement", "ForwardingInstructions", "BillOfLading"}
BILLING_DOCS = {"UtilityStatement", "InvoiceStatusRequest", "InvoiceStatusResponse", "Statement"}
CUSTOMS_DOCS = {"ExportCustomsDeclaration": "customs_export", "ImportCustomsDeclaration": "customs_import",
                "TransitCustomsDeclaration": "customs_transit"}
DESK_ROLE = {"sales": "it sells", "purchasing": "it buys", "receivables": "it is owed the payment",
             "payables": "it pays", "goods_in": "it receives the goods", "despatch": "it sends the goods off",
             "logistics": "it books or uses the transport", "customs": "it deals with customs",
             "tenders": "it bids", "operations": "it carries or handles the goods", "procurement": "it buys",
             "customs_export": "an export", "customs_import": "an import", "customs_transit": "a transit",
             "carnet": "a carnet", "certificates": "a certificate",
             "export": "it handles the transport of goods between the countries"}
CHAMBER_DOCS = {"GoodsItemPassport": "carnet", "ProofOfReexportation": "carnet",
                "ProofOfReexportationRequest": "carnet", "ProofOfReexportationReminder": "carnet",
                "CertificateOfOrigin": "certificates", "GoodsCertificate": "certificates"}
GENERIC_ROLES = {"SenderParty", "ReceiverParty", "ReporterParty", "BusinessParty", "IssuerParty"}
CARRIER_ROLES = {"CarrierParty", "TransportServiceProviderParty", "TerminalOperatorParty", "FreightForwarderParty"}


def _role_index():
    sells, carriers = set(), set()
    for d in WORLD["documents"]:
        ps = {k.split("/")[-1]: v for k, v in d.get("parties", {}).items() if isinstance(v, str)}
        for s, b in (("SellerSupplierParty", "BuyerCustomerParty"), ("AccountingSupplierParty",
                                                                     "AccountingCustomerParty")):
            if s in ps and b in ps:
                sells.add((ps[s], ps[b]))
        carriers |= {v for k, v in ps.items() if k in CARRIER_ROLES}
    return sells, carriers


SELLS, CARRIERS = _role_index()


def desk_for(doc, path, pid):
    """The function of the desk that speaks for party pid in its role at path of document doc. A party with an
    export desk names it for its transport work on goods that cross a border: a document whose parties, or the
    flow's transport legs those parties run, send or receive, are in more than one country; at home its main
    contact or its operations desk speaks (O224)."""
    fn = _desk_for(doc, path, pid)
    if fn in (None, "operations", "logistics") and "export" in PARTY[pid]["identity"].get("desks", {}):
        pids = {doc.get("from"), doc.get("to")} | {v for v in doc.get("parties", {}).values() if isinstance(v, str)}
        legs = [leg for fl in WORLD["flows"] if fl["id"] == doc["flow"] for leg in fl.get("legs", [])]
        pids |= {x for leg in legs if pids & {leg.get("from"), leg.get("to"), leg.get("carrier")}
                 for x in (leg.get("from"), leg.get("to"))}
        if len({PARTY[x]["c"] for x in pids if x in PARTY}) > 1:
            return "export"
    return fn


def _desk_for(doc, path, pid):
    role = path.split("/")[-1]
    kind = doc["doc"]
    if kind in CUSTOMS_DOCS and PARTY[pid]["kind"] == "customs":
        return CUSTOMS_DOCS[kind]
    if role in ROLE_DESK and not (role == "ConsigneeParty" and kind in CUSTOMS_DOCS):
        return ROLE_DESK[role]
    if role in ("ConsigneeParty", "ConsignorParty") and kind in CUSTOMS_DOCS:
        return "customs"
    if kind in CHAMBER_DOCS and PARTY[pid]["kind"] == "office" and PARTY[pid]["identity"]["kind"] == "public":
        return CHAMBER_DOCS[kind]
    if PARTY[pid]["identity"]["kind"] == "public" or role not in GENERIC_ROLES:
        return None
    other = doc.get("to") if pid == doc.get("from") else doc.get("from")
    if kind in TRANSPORT_DOCS:
        return "operations" if pid in CARRIERS or PARTY[pid]["kind"] in ("port", "airport", "terminal") \
            else "logistics"
    if kind in BILLING_DOCS:
        return "receivables" if (pid, other) in SELLS else "payables"
    if (pid, other) in SELLS:
        return "sales"
    if (other, pid) in SELLS:
        return "purchasing"
    return None


def party(pid, short=False, desk=None, lang=None):
    """The content of a cac:Party element, from the identity layer. short: identifier and name only, for a party
    referred to from inside another party's block (its service provider, shareholder or agent). desk: the function
    of the desk the party's role in the document calls for (desk_for); without one, or if the party has no such
    desk, its main contact."""
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
                                              f"{world_ids.register_of(WORLD, p)[1]['name']}; {src}. Later mentions "
                                              "of the same party in this document repeat only this identifier and the "
                                              "name.", schemeID=register_scheme(pid))}
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
        first = WORLD["countries"][p["c"]]["languages"][0]
        code = "en" if lang == "english" else first
        if code == "en":
            out["Language"] = {"ID": V("en", "English, the language the party writes in this document" + (
                                   ": documents between the countries of the Trade Accord are in English (O19)."
                                   if first != "en" else ".")),
                               "Name": V("English", "The language's name."),
                               "LocaleCode": V(f"en-{p['c']}", f"The English the party writes: the variety of "
                                                               f"{c['name']}, with the country as the region; English is "
                                                               "used in all three countries, so its locale says which "
                                                               "(decision D1).")}
        else:
            lang = WORLD["languages"][code]
            out["Language"] = {"ID": V(code, f"{lang['name']}, the language of {c['name']} and of the party; the code is "
                                             "from the range ISO 639 reserves for local use (qaa–qtz), as the world's "
                                             "languages are invented (world/countries.json)."),
                               "Name": V(lang["name"], f"The language's name in English; in the language itself: "
                                                       f"{lang['own_name']}.")}
    out["PostalAddress"] = address(pid, register=True)
    if desk and idn.get("address_desks") and desk not in idn["address_desks"]:
        # the lines of the address that name one office (the department's procurement office) go only with the
        # roles that office answers for; an invoice's accounting customer is the finance office (furniture/17#F6)
        for k in ("Department", "MarkAttention", "InhouseMail"):
            out["PostalAddress"].pop(k, None)
    if idn.get("site"):
        out["PhysicalLocation"] = location(pid)
    if idn.get("endpoint"):
        out["ElectronicAddress"] = {   # new in UBL 2.5; Party/EndpointID is deprecated
            "ExchangeNetworkID": V("urn:ubl-examples:world:network", "The network in which the address is registered: "
                                   "the world's own exchange network."),
            "ElectronicAddressID": V(idn["endpoint"], "The party's electronic address in that network: its country code and "
                                     f"its number in the {world_ids.register_of(WORLD, p)[1]['name']}; {src}. UBL 2.5 "
                                     "carries it here; Party/EndpointID is deprecated.",
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
                tax["RegistrationAddress"] = {"CityName": city_names(p["c"], idn["tax_registration_office"],
                                                                     "Where the party is registered for the tax."),
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
        own = idn.get("desks", {}).get(desk)
        if own:
            ct = {**{k: v for k, v in ct.items() if k not in ("id", "mobile", "telefax")}, **own}
            desk_name = own["name"].lower().removesuffix(" desk")
            why = (f"The party's {desk_name} desk: the desk for its role in this document "
                   f"({DESK_ROLE[desk]}); {src}.")
        else:
            why = f"The party's main desk, which handles this document; {src}."
        contact = {"Name": V(ct["name"], why)}
        if ct.get("id"):
            contact = {"ID": V(ct["id"], "The desk's number in the party's own contact list."), **contact}
        if ct.get("job_title"):
            contact["JobTitle"] = V(ct["job_title"], f"The job of the person who answers at the desk; {src}.")
        if ct.get("department"):
            contact["Department"] = V(ct["department"], f"The department the desk belongs to; {src}.")
        if ct.get("telephone"):
            contact["Telephone"] = V(ct["telephone"], ("The party's switchboard, which puts the caller through to "
                                                       "the desk. " if own else "") + "Telephone under +999, a country code the ITU reserves for a "
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
                                                     "CertificateTypeCode": V(au.get("type_code", "PERMIT"),
                                                                              "A permit issued by an authority of the "
                                                                              "party's country." if "type_code" not in au
                                                                              else "A registration with an authority "
                                                                                   "of the party's country."),
                                                     "CertificateType": V(au.get("type", "Operating permit"),
                                                                          "The kind of certificate, in words.")}}
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
    public = idn["kind"] == "public"           # a public body is in no register of businesses (D46, worklist C04)
    farm = le.get("sole_proprietor") and c.get("farm_registry")
    reg = world_ids.register_of(WORLD, p)[1]   # a public body's own register, a grower's farm register (O142)
    out = {"RegistrationName": V(legal_name(pid), ("The name under which the party is registered, with its legal form; "
                                                   if not public else "The public body's official name; ") + f"{src}.")}
    out["CompanyID"] = V(idn["registry_id"], f"Number in the {reg['name']}" + (
        f", which gives every public body a number of its own ({reg['id_format']}), derived from no other register "
        "(O142)" if public else "") + f"; {src}.")
    if le.get("founded"):
        out["RegistrationDate"] = V(le["founded"], f"The day the company was entered in the register; {src}.")
    if le.get("form"):
        out["CompanyLegalFormCode"] = V(le["form"], f"The legal form, as a code of {c['name']}'s national list: "
                                                    "only the listID tells the forms of different countries apart.",
                                        listID=codelists.NATIONAL.format(p["c"], "CompanyLegalForm"))
        out["CompanyLegalForm"] = V(c["legal_forms"][le["form"]]["name"], "The legal form, in words, as the "
                                    "party's register writes it.", languageID=f"en-{p['c']}")
    if le.get("sole_proprietor"):
        out["SoleProprietorshipIndicator"] = V("true", f"The farm belongs to one farmer, who runs it in their own name; "
                                                       f"{src}.")
    if le.get("registration_expires"):
        out["RegistrationExpirationDate"] = V(le["registration_expires"], "The island renews a farm's registration "
                                                                          "every year: it runs until this date.")
    if not idn.get("person") and not public:
        out["CompanyLiquidationStatusCode"] = V("ACTIVE", "The register shows the company as active, not in "
                                                          "liquidation.")
    if le.get("headcount") and not public:
        t = le["turnover"]
        out["EntitySizeCode"] = V(codelists.entity_size(le["headcount"], t["amount"], t["currency"]),
                                  f"The size class follows from the company's {le['headcount']} persons and its turnover "
                                  f"of {t['amount']} {t['currency']} in {t['year']}, by the Trade Accord's limits; {src}.")
    if le.get("capital"):
        out["CorporateStockAmount"] = V(str(le["capital"]), f"The share capital, in {c['currency']['name'].lower()}, "
                                        f"as paid up: {c['name']}'s company law asks an {le.get('form')} to state it "
                                        f"on its invoices and business letters (world/countries.json); {src}.",
                                        currencyID=c["currency"]["code"])
        out["FullyPaidSharesIndicator"] = V("true", "All shares are paid up, so the amount stated is the whole "
                                                    "share capital.")
    out["RegistrationAddress"] = {"CityName": city_names(p["c"], idn["address"]["CityName"], "The registered office, "
                                                         "as entered in the register."),
                                  "Country": {"IdentificationCode": V(p["c"], "The country of registration.")}}
    if farm:
        out["CorporateRegistrationScheme"] = {
            "ID": V(farm["scheme"], "The identifier of the register in the world (world/countries.json)."),
            "Name": V(farm["name"], f"The register the farm is entered in, kept by "
                                    f"{'the ' + PARTY[farm['keeper']]['identity']['name'] if farm['keeper'] in PARTY else farm['keeper']}: "
                                    f"{farm['note']}"),
            "CorporateRegistrationTypeCode": V("FARM", "A register of farms, not the companies register."),
            "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V(p["c"], "The register covers the whole "
                                                                                      "country.")}}}
    elif public:
        out["CorporateRegistrationScheme"] = {
            "ID": V(reg["scheme"], "The identifier of the register in the world (world/countries.json)."),
            "Name": V(reg["name"], f"The register the public body is entered in, kept by "
                                   f"{'the ' + PARTY[reg['keeper']]['identity']['name'] if reg['keeper'] in PARTY else reg['keeper']}"
                                   ": a public body is set up by law and is in no register of businesses (D46, O142)."),
            "CorporateRegistrationTypeCode": V("PUBLIC", "A register of public bodies, not a register of businesses."),
            "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V(p["c"], "The register covers the whole "
                                                                                      "country.")}}}
    else:
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


def city_names(country, city, why):
    """A town's name in an address: in both official languages where the country is bilingual and the town has a name
    in each (world/countries.json): Urvania's towns have an Urvanian name beside the inherited Italian one, which counts
    as English; the island's towns have an English name beside the Lisavan one. Otherwise the one name."""
    code = WORLD["countries"][country]["languages"][0]
    if code == "en":
        return V(city, why)
    lang = WORLD["languages"][code]
    names = next((t.get("names", {}) for t in WORLD.get("localities", []) + WORLD.get("villages", [])
                  if t["name"] == city and t["country"] == country), {})
    if names.get(code) and code == "qau":        # a village or locality of the map, with its Urvanian name
        return [V(names[code], f"The place's {lang['name']} name, as the map gives it (world/map.json). {why}",
                  languageID=code),
                V(city, f"The place's English name, the Italian one. {why}", languageID=f"en-{country}")]
    if names.get(code):                           # a village of the island, with its Lisavan name
        return [V(names[code], f"The place's {lang['name']} name, as the map gives it (world/map.json). {why}",
                  languageID=code),
                V(city, f"The place's English name, which its English settlers gave it, official beside the "
                        f"{lang['name']} one. {why}", languageID=f"en-{country}")]
    if lang.get("place_names", {}).get(city):
        return [V(lang["place_names"][city], f"The town's {lang['name']} name, which its people have always used. "
                                             f"{why}", languageID=code),
                V(city, f"The town's English name, inherited from the Italian. {why}", languageID=f"en-{country}")]
    if lang.get("english_place_names", {}).get(city):
        return [V(city, f"The town's {lang['name']} name, its name on the island. {why}", languageID=code),
                V(lang["english_place_names"][city], f"The town's English name, which its English-speaking settlers "
                                                     f"gave it, official beside the {lang['name']} one "
                                                     f"(world/countries.json). {why}", languageID=f"en-{country}")]
    return V(city, why)


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
           "CitySubdivisionName": "The quarter of Lumeport the party is in: one of the town's districts on the "
                                  "map (world/map.json).",
           "CountrySubentityCode": "The state or territory as a code of Bayvarra's address scheme (world/countries.json).",
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
                              f"format ({c['address']['postal_zone']}).", "CountrySubentity": (f"The province, part of an address in {c['name']}: a "
                              "subdivision of the country (world/countries.json)." if c.get("province") else
                              f"The state or territory, part of an address in federal {c['name']}.")}.get(k, why.get(k, "")) + f" {src}.")
    code = c["languages"][0]
    if code != "en" and "en" in c["languages"] and isinstance(out.get("StreetName"), V):
        lang = WORLD["languages"][code]["name"]                 # a bilingual country names its streets twice
        st = out["StreetName"]
        out["StreetName"] = [V(translate(st.value, code, street=True), f"The street's name in {lang}: {c['name']} "
                               f"is officially bilingual, and street names are given in both languages "
                               f"(world/countries.json); {src}.", languageID=code),
                             V(st.value, "The street's name in English, the country's other official language"
                                         + ("; the Italian names the British kept are part of English now"
                                            if p["c"] == "XU" else "") + f"; {src}.", languageID=f"en-{p['c']}")]
    if a.get("CityName"):
        if idn.get("city_why"):                     # a party not in the town nearest to it (O152, 2026-11-18)
            out["CityName"] = V(a["CityName"], f"{idn['city_why']} {src}.")
        out["CityName"] = city_names(p["c"], a["CityName"], out["CityName"].why)
    out["AddressFormatCode"] = address_format_code(p["c"])
    out["TimezoneOffset"] = V(c["timezone"], f"The offset from UTC of {c['legal_time']}, {c['name']}'s legal time, "
                                             "all year: there is no summer time (D27, world/countries.json).")
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
    """Latitude and longitude of a map tile: the world lies in an empty part of the South Atlantic. The squares keep
    their size (km_per_tile) on both axes around the centre of their area; Lisavu, drawn nearer as an inset, is
    placed around its own true centre (world/countries.json, geography)."""
    import math
    g = WORLD["geography"]
    area = next((a for a in g.get("insets", []) if at[0] >= a["from_column"]), g["mainland"])
    (ci, cj), c = area["centre_tile"], area["centre"]
    km = g["km_per_tile"]
    lat_c, lon_c = c["latitude_south"], c["longitude_west"]
    lat_f = lat_c + km * (at[1] - cj) / 111.0
    lon_f = lon_c - km * (at[0] - ci) / (111.32 * math.cos(math.radians(lat_c)))
    lat, lon = Decimal(f"{lat_f:.6f}"), Decimal(f"{lon_f:.6f}")
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
    text, why = site["description"], "Where the party actually operates, apart from its postal address."
    if site.get("distance"):                    # a distance the text states, from the map (O152 stage 2 B)
        import world_map
        d = site["distance"]
        text = text.format(km=world_map.nearest(world_map.route_km(d["route"]), d.get("about", 1)))
        why += f" The distance is the length of the map's route {d['route']}, rounded to {d.get('about', 1)} km."
    out["Description"] = V(text, why)
    if site.get("conditions"):
        out["Conditions"] = V(site["conditions"], "What a visitor must know about getting there.")
    if site.get("information_uri"):     # a page about the place itself, not the company's home page (energy/04#F9)
        out["InformationURI"] = V(site["information_uri"], "A page about the place itself: the port's or the "
                                                           "airport's own site, with its access and services.")
    out["LocationCoordinate"] = coordinate(p["at"])
    if site.get("altitude") == "map":           # the level the 3D map gives the party's ground (O152 stage 2 B)
        import world_map
        out["LocationCoordinate"]["AltitudeMeasure"] = V(str(world_map.whole(world_map.fitted_height(pid))),
                                                         "The height of the place above sea level: the level its "
                                                         "ground stands at on the world's map.", unitCode="MTR")
    elif site.get("altitude"):
        out["LocationCoordinate"]["AltitudeMeasure"] = V(str(site["altitude"]), "The height of the place above sea "
                                                                               "level.", unitCode="MTR")
    if site.get("subsidiary"):
        out["SubsidiaryLocation"] = {"Name": V(site["subsidiary"], "A part of the port with its own location: where "
                                                                   "containers are handled.")}
    return out


def register_scheme(pid):
    """The schemeID of a party's register number: its companies register, its register of public bodies or the
    farm register (O142)."""
    return world_ids.national_scheme(PARTY[pid]["c"], world_ids.register_of(WORLD, PARTY[pid])[0])


def party_again(pid, first):
    """A later mention of a party already given in full in this document: its identifier and name only."""
    idn = PARTY[pid]["identity"]
    why = (f"The same party as at {first}, where its full details are given; only its identifier and name are repeated."
           if first else f"{PARTY[pid]['what']} Its identifier and name are enough (world/parties.json, referenced)."
           if pid in REFERENCED else "A party referred to from another party's details: its identifier and name are "
                                     "enough.")
    out = {"PartyName": {"Name": V(idn["name"], why)}}
    if idn.get("registry_id"):
        out["PartyIdentification"] = {"ID": V(idn["registry_id"], why, schemeID=register_scheme(pid))}
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
            "Address": {k: v for k, v in address(pid).items()      # the head office, from the address generator
                        if k in ("AddressFormatCode", "StreetName", "BuildingNumber", "CityName", "PostalZone",
                                 "CountrySubentity", "CountrySubentityCode", "Region", "Country")}}


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
                                         "Address": {"CityName": city_names(bank["c"], branch["city"],
                                                                            "The town the branch is in."),
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
    """The dangerous goods data of an item (world/items.json), as the UN Model Regulations describe it, and only
    what the document's carriage uses (D36, C79): the emergency schedules for ships (EmS) and the marine pollutant
    only where the flow goes by sea, the tunnel code only where it goes by road alone; a placard notation only for
    goods that carry a hazard label, and no placard endorsement that repeats the class or the label model. The
    despatch advice keeps the identification and the handling notes, for the receiver."""
    hz = it["hazard"]
    modes = FLOW_MODES or set()
    receiver = ITEM_KIND.get(DOC_TYPE) == "despatch"
    out = {"ID": V(f"{it['sellers_id']}-DG", "The seller's dangerous goods record of the item."),
           "UNDGCode": V(hz["un"][2:], "The UN number, from the Dangerous Goods List of the UN Model Regulations."),
           "ProperShippingName": V(hz["name"], "The proper shipping name of the UN entry; the build checks that UN "
                                               "number, name and class agree with the Dangerous Goods List."),
           "HazardClassID": V(hz["class"], "The UN hazard class of the entry."),
           "HazardousCategoryCode": V(hz["class"], "The hazard class of the goods as a code of the UN Model "
                                                    "Regulations' classes.")}
    if "sea" in modes and not receiver:
        out["EmergencyProceduresCode"] = V(hz["ems"], "The emergency schedules for ships (EmS) of the IMDG Code for "
                                                      "this UN entry: the fire schedule and the spillage schedule.")
    out["MedicalFirstAidGuideCode"] = V(hz["erg"], "The guide number of the Emergency Response Guidebook (ERG 2024) "
                                                   "for this UN number: the world's carriers and receivers use the "
                                                   "ERG, as the IMDG Code no longer gives medical first aid table "
                                                   "numbers per UN number.")
    if hz.get("note"):
        out["AdditionalInformation"] = V(hz["note"], "What the shipper adds about handling.")
    if hz.get("label") and not receiver:
        out["PlacardNotation"] = V(hz["class"], "The class shown on the hazard label of the packages.")
    out["MarkingID"] = V(hz["un"], "The UN number marked on each package.")
    out["UNPackingGroupCode"] = V(hz.get("pg", "NA"), "The packing group of the UN entry; NA where the entry has no "
                                                     "packing group, as for lithium batteries and radioactive material.")
    out["UNPackingGroup"] = V(hz.get("pg", "NA"), "In words.")
    if hz.get("tunnel") and modes == {"road"} and not receiver:
        out["TunnelRestrictionCode"] = V(hz["tunnel"], "The tunnel restriction code for road transport.")
    if hz.get("technical"):
        out["TechnicalName"] = V(hz["technical"], "The technical name, needed with an n.o.s. entry.")
    if hz.get("sub"):
        out["SecondaryHazard"] = {"ID": V(hz["sub"], "The subsidiary hazard: flammable."),
                                  "PlacardNotation": V(hz["sub"], "Shown on a second label."),
                                  "Extension": V("Subsidiary risk 3", "In words.")}
        if not receiver:
            out["SecondaryHazard"]["EmergencyProceduresCode"] = V(
                f"TEC{hz['sub']}", "UBL defines it as \"A code signifying the emergency procedures for this "
                "secondary hazard\": the Trade Accord's emergency card for class "
                f"{hz['sub']}. The IMDG Code gives one pair of emergency schedules for the whole UN entry, not one "
                "per hazard; the instructions in writing of road transport (ADR 5.4.3), which the Accord's cards "
                "follow, give the actions per danger label, the subsidiary hazard's label included.")
        out["FlashpointTemperature"] = {"AttributeID": V("FLASHPOINT", "Closed cup."),
                                        "Measure": V(hz["flash"], "The flashpoint.", unitCode="CEL")}
        if "sea" in modes:
            out["MaritimePollutantCode"] = V("N", "Not a marine pollutant.")
    if hz.get("radioactive"):
        r = hz["radioactive"]
        total = r["kbq_each"] * r["count"]
        out["RadioactiveMaterial"] = {
            "Name": V(f"{r['nuclide']}, {r['count']} × {r['kbq_each']} kBq ({total} kBq) in ionisation smoke "
                      "detectors", "The nuclide and the activity of the pack as carried, in the name: UBL defines "
                      "ApplicableRadioactiveIsotope for fissile contents only, and americium-241 is not fissile, so "
                      "the name is the only place left for them (D36, O127)."),
            "SpecialFormDescription": V(r["form"], "Its form.")}
    return out


def item_texts(it, text, what, src):
    """A text about an item (its name, description, warranty …): in the seller's language and in English when the
    seller's country speaks another language (Urvanian, Lisavan), each with its languageID; English only for a seller
    in Bayvarra. `what` names the text, as in "The item's name"."""
    code = WORLD["countries"][PARTY[it["seller"]]["c"]]["languages"][0]
    if code == "en":
        return V(text, f"{what}; {src}.")
    lang = WORLD["languages"][code]["name"]
    return [V(translate(text, code), f"{what} in {lang}, the seller's language; {src}.", languageID=code),
            V(text, f"{what} in English, the working language between the countries; {src}.", languageID="en")]


def item_names(it, src):
    """The item's name, in the seller's languages (item_texts)."""
    return item_texts(it, it["name"], "The item's name" if WORLD["countries"][PARTY[it["seller"]]["c"]]["languages"][0]
                      != "en" else "The item's short name", src)


def item(iid, tax=None, buyer=None, instance=None, catalogue=None, catalogue_ref=None):
    """The content of a cac:Item element, from the items layer. `catalogue` is (catalogue number, line) for a
    catalogue line; `catalogue_ref` the catalogue an order line was ordered from."""
    it = ITEM[iid]
    src = f"item {it['id']} of {PARTY[it['seller']]['identity']['name']} (world/items.json)"
    out = {"Description": item_texts(it, it["description"], "The seller's description", src),
           "Name": item_names(it, src)}
    maker = it
    while maker.get("resale_of"):
        maker = ITEM[maker["resale_of"]]
    msrc = f"item {maker['id']} of {PARTY[maker['seller']]['identity']['name']} (world/items.json)"
    if maker.get("pack"):
        out["PackQuantity"] = V(maker["pack"]["quantity"], "One pack of this item.", unitCode="EA")
        out["PackSizeNumeric"] = V(maker["pack"]["size"], f"The units in one pack: {maker['pack']['size']} in a "
                                                          f"bundle; {msrc}.")
    if maker.get("keywords"):
        out["Keyword"] = V(", ".join(maker["keywords"]), "The search string buyers find the item by, the maker's "
                                                          f"keywords in one element; {msrc}. A second Keyword would "
                                                          "have to be in another language (UBL rule IND7).")
    bowner = PARTY[maker["brand_owner"]]["identity"]["name"] if maker.get("brand_owner") else None
    if maker.get("brand") and bowner:      # a private label: the brand is the owner's, the maker makes it (D7)
        out["BrandName"] = V(maker["brand"], f"The brand the item is sold under: {maker['brand']}, the own label of "
                                             f"{bowner}, which {PARTY[maker['seller']]['identity']['name']} makes "
                                             f"for it; {msrc}.")
    elif maker.get("brand"):
        out["BrandName"] = V(maker["brand"], f"The brand the maker sells the item under; {msrc}.")
    if maker.get("model"):
        out["ModelName"] = V(maker["model"], f"The model; {msrc}.")
    if maker.get("additional_info"):
        out["AdditionalInformation"] = item_texts(it, maker["additional_info"], "What comes with the item", msrc)
    if maker.get("warranty"):
        out["WarrantyInformation"] = item_texts(it, maker["warranty"], "The maker's warranty", msrc)
    bid, bwhy = buyer_item_id(iid, buyer) if buyer else (None, None)
    if bid:
        out["BuyersItemIdentification"] = {"ID": V(bid, bwhy)}
    out["SellersItemIdentification"] = {"ID": V(it["sellers_id"], f"The seller's own item number; {src}.")}
    if catalogue:
        out["CatalogueItemIdentification"] = {"ID": V(f"{catalogue[0]}-{catalogue[1]}", "The item's place in the "
                                                      "catalogue: the catalogue number and the line.")}
    if it.get("resale_of"):        # a resold item carries the maker's identifiers, customs code and origin
        out["ManufacturersItemIdentification"] = {"ID": V(maker["sellers_id"], f"The item number of the maker, "
                                                          f"{PARTY[maker['seller']]['identity']['name']}: the "
                                                          f"reseller's item is resale of item {maker['id']}.")}
    # a variant of the maker's item: its item number, with the variant added. A reseller that numbers the model
    # once (Lumeway's LD-10442 for the bench in any colour) adds the variant to its own number; one that gives each
    # variant a number of its own (variant_numbers: the store's BM-551005 for the oak bench, O155) needs no
    # variant on it, and the variant goes with the maker's number
    if maker.get("version"):      # the version of the maker's part, on the maker's number (O216)
        mid = out["ManufacturersItemIdentification"] if it.get("resale_of") else out["SellersItemIdentification"]
        mid["ExtendedID"] = V(maker["version"]["extended"], f"{maker['version']['why']} {msrc}.")
    variant = maker.get("variant", {})
    vid = out["ManufacturersItemIdentification"] if it.get("variant_numbers") else out["SellersItemIdentification"]
    if variant.get("extended"):
        vid["ExtendedID"] = V(variant["extended"], f"The variant of the item: the {variant['what']}, added to the "
                                                   "item number.")
    if variant.get("attribute"):
        a_, code, desc = variant["attribute"]
        pa = {"AttributeID": V(a_, "The attribute the variant differs in.")}
        if variant.get("position"):
            pa["PositionCode"] = V(variant["position"], "The part of the item the attribute is on: the "
                                                        f"{variant['what'].split()[0]}.")
        vid["PhysicalAttribute"] = {
            **pa, "DescriptionCode": V(code, "The variant's code for it."),
            "Description": V(desc, "The variant in words.")}
    if variant.get("measure"):
        a_, v, u = variant["measure"]
        vid["MeasurementDimension"] = {
            "AttributeID": V(a_, "The seller numbers its slats by length: this number is for one length."),
            "Measure": V(v, "The length the number stands for.", unitCode=u)}
    gtin = it                          # the GTIN: the item's own, or one allocated further up the resale chain
    while gtin and not gtin.get("gtin"):
        gtin = ITEM.get(gtin.get("resale_of"))
    mname = PARTY[maker["seller"]]["identity"]["name"]
    codana = {"ID": V(maker["standard_id"], "The item's number in its globally unique form under ISO/IEC 15459, "
                      f"which {mname} gives it: the issuing agency code KXU of the Codana Identification Agency, the "
                      f"company number Codana gave {mname} and the company's own reference for the item, without a "
                      "check character. Codana gives a company its number; the company numbers its own items; "
                      f"{msrc}.",
                      schemeID="ISO 15459-6")} \
        if maker.get("standard_id") else None
    if gtin:
        owner = PARTY[gtin.get("brand_owner", gtin["seller"])]["identity"]["name"]
        poss = "'" if owner.endswith("s") else "'s"
        out["StandardItemIdentification"] = {"ID": V(gtin["gtin"], (
            f"The GTIN {owner} gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves "
            "that prefix for demonstrations and examples, so the number belongs to no real product"
            + (f"; the item is {owner}{poss} own label {gtin['brand']}, made for it by {mname}: under GS1 rules "
               f"the brand owner numbers the item, not the manufacturer, so the number is {owner}{poss}, whoever "
               "sells the item" if gtin.get("brand_owner") else
               f"; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate "
               "the GTIN where the brand owner has none" if gtin is not maker else
               f"; under GS1 rules the brand owner numbers the item, and the brand {maker['brand']} is {owner}{poss}"
               if maker.get("brand") else "")
            + f" (world/items.json)."), schemeID="GS1 GTIN")}
        if codana:
            out["AdditionalItemIdentification"] = {"ID": V(maker["standard_id"], "The maker's number for the item "
                                                           "in its globally unique form under ISO/IEC 15459 (KXU and "
                                                           f"the company number Codana gave {mname}), which travels "
                                                           "along with the GTIN, as an importer may carry it; "
                                                           f"{msrc}.",
                                                           schemeID="ISO 15459-6")}
    elif codana:
        out["StandardItemIdentification"] = codana
        if maker.get("barcode"):
            out["StandardItemIdentification"]["BarcodeSymbologyID"] = V(maker["barcode"], "The barcode the number "
                                                                        "is printed in on the label: Code 128 "
                                                                        "carries letters and digits.")
            prefix = "KXU" + PARTY[maker["seller"]]["identity"]["identification"]["codana_cin"]
            out["StandardItemIdentification"]["IssuerScopeID"] = V(prefix, f"The scope within which {mname} "
                                                                   "gives its item numbers: its company prefix, the "
                                                                   "issuing agency code KXU and its Codana company "
                                                                   "number; what follows is the company's own "
                                                                   "reference.")
    if catalogue_ref:
        out["CatalogueDocumentReference"] = {"ID": V(catalogue_ref, "The catalogue the item was ordered from.")}
    if maker.get("spec_doc"):
        out["ItemSpecificationDocumentReference"] = {"ID": V(maker["spec_doc"], "The maker's datasheet with drawings "
                                                                                "and assembly instructions.")}
    if it.get("lifecycle"):
        out["LifecycleStageCode"] = V(it["lifecycle"][0], "The stage of the product's life the item belongs to.")
        out["LifecycleStageDescription"] = item_texts(it, it["lifecycle"][1], "The stage of the item's life in words",
                                                      src)
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
    for pr in (ITEM[maker["content"]["item"]] if maker.get("content") else maker).get("properties", []):
        props.append(item_property(pr, msrc))
    for name, value, unit in maker.get("quantity_properties", []):
        props.append({"Name": V(name, "A measured property of the item."),
                      "ValueQuantity": V(value, f"Its measured value; {msrc}.", unitCode=unit)})
    if props:
        out["AdditionalItemProperty"] = props
    if it.get("resale_of") or maker.get("brand_owner"):    # a resold item, or a private label: who makes it
        out["ManufacturerParty"] = party(maker["seller"], short=True)
        if catalogue:
            out["InformationContentProviderParty"] = party(maker["seller"], short=True)
    if it.get("conditions"):
        tc = it["conditions"]
        out["TransactionConditions"] = {"ID": V(tc["id"], "The seller's number for these conditions of sale."),
                                        "Description": V(tc["description"], "The conditions in words."),
                                        "DocumentReference": {"ID": V(tc["doc"], "The seller's general terms of "
                                                                                 "trade.")}}
    if maker.get("origin_district"):
        out["OriginAddress"] = {"District": V(maker["origin_district"], "The district of the island where the cotton "
                                                                        "was grown, as the farm's address names it."),
                                "Country": {"IdentificationCode": V(maker["origin"], "The country of origin.")}}
    if instance:
        out["ItemInstance"] = instance
    facts = ITEM[maker["content"]["item"]] if maker.get("content") else maker   # a pack: the facts of its content
    if facts.get("certificate"):
        ce = facts["certificate"]
        reg = ce.get("register") and world_ids.national_scheme(maker["origin"], ce["register"])
        cert = {"ID": V(ce["id"], "The number of the certificate" + (
                    f", in the {SCHEMES[reg]['name']}, which keeps the certificates issued under each registration; "
                    "the schemeID names the register and its authority, so no issuer party is needed (decision "
                    "ID-Q10)." if reg else ", unique only with its issuer, who is named below (decision ID-Q10)."),
                    **({"schemeID": reg} if reg else {})),
                "CertificateTypeCode": V(ce["code"], "The kind of certificate, as a code."),
                "CertificateType": V(ce["type"], "The kind of certificate, in words.")}
        if ce.get("remarks"):       # a certificate's results are no applicant's remarks (C109): only real remarks
            cert["Remarks"] = V(ce["remarks"], "What the certificate states about the goods.")
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
            circ["RecycledContentPercent"] = V(ci["recycled"], ci.get("recycled_why", "The share of recycled material: "
                                                               "the film is made from the recycled granulate."))
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
    if maker.get("emissions"):
        def emission(em):
            out_ = {"EnvironmentalEmissionTypeCode": V(em["type"], "The emission reported: greenhouse gases as CO2 "
                                                                   "equivalent."),
                    "ValueMeasure": V(em["value"], "The emission of one item in this stage of its life: a figure "
                                                   "from the maker's footprint study, not an activity times a "
                                                   "factor, so no factor and base (worklist C09).",
                                      unitCode=em["unit"])}
            if em.get("factor"):      # only where the figure is an activity times a factor (C09)
                out_["ValueFactorNumeric"] = V(em["factor"], em["factor_why"])
                out_["ValueBaseMeasure"] = V(em["base"][0], em["base_why"], unitCode=em["base"][1])
            out_.update({
                "Description": V(em["description"], "What the figure includes, and what it leaves out."),
                "EmissionStandardReference": V(em["standard"], "The standard the footprint is calculated by."),
                "LifecycleStageCode": V(em["stage"], "The stage of the bench's life the figure covers (D10): the "
                                                     "footprint is stated stage by stage."),
                "LifecycleStageDescription": V(em["stage_desc"], "That stage in words, with the modules of EN 15804 "
                                                                 "it covers."),
                "EmissionCalculationMethod": {"CalculationMethodCode": V(em["method"]["code"], "Calculated, not "
                                                                                               "measured."),
                                              "EmissionFactorSource": V(em["method"]["source"], "Where the factors "
                                                                                                "come from."),
                                              "EmissionFactorDocumentReference": {"ID": V(em["method"]["doc"], "The "
                                                                                  "report with the emission "
                                                                                  "factors.")}},
                "MeasurementPeriod": {"StartDate": V(em["period"][0], "The year the figures are from."),
                                      "EndDate": V(em["period"][1], "Its last day.")}})
            return out_
        out["EnvironmentalEmission"] = [emission(em) for em in maker["emissions"]]
    if it.get("origin") or maker.get("origin"):
        out["OriginCountry"] = {"IdentificationCode": V(maker["origin"], f"Where the item was produced; {msrc}.")}
    out["_master"] = {k: id(v) for k, v in out.items()}     # the item's master data, for the item table (O20)
    if maker.get("certificate", {}).get("layer") == "lot":   # a certificate of the lot, not of the item type (D11)
        out["_lot"] = {"Certificate"}
    return out


def tax_category(code, percent, why, scheme="VAT", country="XU"):
    c = WORLD["countries"][country]
    return {"ID": V(code, why), "Percent": V(str(percent), f"The rate of {c['name']}'s "
                                             f"{c['tax']['schemes'][0]['name'].lower()} for this category (world/countries.json)."),
            "TaxScheme": {"ID": V(scheme, f"UN/EDIFACT 5153 code of {c['name']}'s {c['tax']['schemes'][0]['name'].lower()}.")}}


# ---------------------------------------------------------------- placing the world's parties
# ---------------------------------------------------------------- what a document says about a party (O86, O88)
DOC_CLASS = {}
for _cls, _docs in {
    "trade": "Order OrderResponse OrderChange OrderCancellation RequestForQuotation Quotation DespatchAdvice "
             "ReceiptAdvice DeliveryNote InstructionForReturns FulfilmentCancellation Forecast ForecastRevision "
             "InventoryReport ProductActivity RetailEvent TradeItemLocationProfile ItemInformationRequest "
             "ExceptionCriteria ExceptionNotification WorkReport",
    "catalogue": "Catalogue CataloguePricingUpdate CatalogueItemSpecificationUpdate CatalogueDeletion CatalogueRequest",
    "invoice": "Invoice CreditNote DebitNote SelfBilledInvoice SelfBilledCreditNote Reminder PurchaseReceipt",
    "payment": "RemittanceAdvice Statement UtilityStatement",
    "transport": "Waybill BillOfLading ForwardingInstructions TransportExecutionPlan TransportExecutionPlanRequest "
                 "TransportationStatus TransportationStatusRequest TransportProgressStatus "
                 "TransportProgressStatusRequest PackingList Manifest CommonTransportationReport WeightStatement "
                 "GoodsItemItinerary TransportServiceDescription TransportServiceDescriptionRequest",
    "customs": "ImportCustomsDeclaration ExportCustomsDeclaration TransitCustomsDeclaration CertificateOfOrigin "
               "GoodsItemPassport GoodsCertificate ProofOfReexportation ProofOfReexportationRequest "
               "ProofOfReexportationReminder",
    "waste": "WasteMovement WasteNotification",
    "notice": "PriorInformationNotice ContractNotice CallForTenders ContractAwardNotice AwardedNotification "
              "UnawardedNotification ProcurementStatus ProcurementStatusRequest ExpressionOfInterestRequest "
              "ExpressionOfInterestResponse UnsubscribeFromProcedureRequest UnsubscribeFromProcedureResponse "
              "TenderReceipt TenderWithdrawal TendererQualificationResponse GuaranteeCertificate "
              "QualificationApplicationRequest",
    "qualification": "Tender TendererQualification QualificationApplicationResponse",
    "contract": "TenderContract DigitalAgreement",
    "presentation": "BusinessCard BusinessInformation DigitalCapability",
    "message": "ApplicationResponse DocumentStatus DocumentStatusRequest InvoiceStatusRequest InvoiceStatusResponse",
}.items():
    for _d in _docs.split():
        DOC_CLASS[_d] = _cls

RESPONSES = set("OrderResponse Quotation TransportExecutionPlan Waybill BillOfLading Tender "
                "QualificationApplicationResponse Catalogue ReceiptAdvice ApplicationResponse DocumentStatus "
                "InvoiceStatusResponse ExpressionOfInterestResponse UnsubscribeFromProcedureResponse TenderReceipt "
                "TendererQualificationResponse ProcurementStatus TransportationStatus TransportProgressStatus "
                "TransportServiceDescription".split())

_TRADE = {"id", "lang", "addr", "site", "eaddr", "contact"}
PROFILE = {     # class -> (about yourself, about the other)
    "trade": (_TRADE, _TRADE - {"lang"}),
    "catalogue": (_TRADE | {"legal", "present"}, _TRADE - {"lang"}),
    "invoice": (_TRADE | {"tax", "legal", "capital", "account"}, _TRADE - {"lang", "site"} | {"legal-name"}),
    "payment": (_TRADE - {"site"}, _TRADE - {"lang", "site"}),
    "transport": (_TRADE | {"customs"}, _TRADE - {"lang"} | {"customs"}),
    "customs": (_TRADE | {"customs", "legal-name"}, {"id", "customs", "addr", "eaddr", "contact", "legal-name"}),
    "waste": (_TRADE | {"permit"}, _TRADE - {"lang"} | {"permit"}),
    "notice": (_TRADE - {"site"} | {"legal-name"}, {"id", "addr", "eaddr", "contact"}),
    "qualification": (_TRADE - {"site"} | {"legal", "legal-full", "present", "tax"},
                      {"id", "addr", "eaddr", "contact", "legal-name"}),
    "contract": (_TRADE - {"site"} | {"legal"}, _TRADE - {"lang", "site"} | {"legal"}),
    "presentation": (_TRADE | {"legal", "legal-full", "present", "service"}, {"id", "addr"}),
    "message": ({"id", "lang", "eaddr", "contact"}, {"id", "eaddr"}),
}
THIRD = {"trade": {"id", "addr", "contact"}, "transport": {"id", "addr", "contact", "customs"},
         "customs": {"id", "addr", "customs"}, "waste": {"id", "addr", "contact", "permit"}}

BLOCK_OF = {"_pid": None, "_keys": None,
            "PartyIdentification": "id", "PartyName": "id", "TradePartyName": "id", "Person": "id",
            "Language": "lang", "PostalAddress": "addr", "PhysicalLocation": "site", "ElectronicAddress": "eaddr",
            "Contact": "contact", "PartyTaxScheme": "tax", "PartyLegalEntity": "legal-name",
            "WebsiteURI": "present", "LogoReferenceID": "present", "IndustryClassificationCode": "present",
            "AdditionalWebSite": "present", "SocialMediaProfile": "present", "FinancialAccount": "account",
            "ServiceProviderParty": "service", "PartyAuthorization": "permit"}
LEGAL_OF = {"RegistrationName": "legal-name", "CompanyID": "legal-name",
            "CompanyLegalFormCode": "legal", "CompanyLegalForm": "legal", "RegistrationAddress": "legal",
            "CorporateRegistrationScheme": "legal", "SoleProprietorshipIndicator": "legal",
            "RegistrationExpirationDate": "legal",
            "RegistrationDate": "legal-full", "EntitySizeCode": "legal-full",
            "CompanyLiquidationStatusCode": "legal-full", "ShareholderParty": "legal-full",
            "HeadOfficeParty": "legal-full", "SecurityListing": "legal-full",
            "CorporateStockAmount": "capital", "FullyPaidSharesIndicator": "capital"}
CUSTOMER_TAX_CODES = {"RESALE", "PUBLIC", "SVCB2B", "SVCABROAD"}   # exemptions that rest on who the customer is


def _cross_border(doc):
    cs = {PARTY[x]["c"] for k, x in doc["parties"].items() if isinstance(x, str) and x in PARTY and
          any(r in k.split("/")[-1] for r in ("Consignor", "Consignee", "Exporter", "Importer", "Shipper"))}
    if len(cs) < 2:
        cs = {PARTY[doc["from"]]["c"], PARTY[doc["to"]]["c"]} if doc.get("to") in PARTY else cs
    return len(cs) > 1


def party_profile(top, path, pid, content):
    """The blocks of a party's description in this document (the story line "What a document says about a
    party"): the sender describes itself in full for the kind of document, the receiver is described with what the
    sender knows and needs, a third party with what the receiver needs to recognise or reach it."""
    kind = top["doc"]
    cls = DOC_CLASS.get(kind)
    if cls is None:
        raise SystemExit(f"{kind}: no party profile class (party_profile)")
    own, other = PROFILE[cls]
    if pid == top.get("from"):
        blocks = set(own)
    elif pid == top.get("to"):
        blocks = set(other) | ({"lang"} if kind in RESPONSES else set())
    else:
        blocks = set(THIRD.get(cls, {"id"}))
    role = path.split("/")[-1]
    if kind.startswith("SelfBilled") and role == "AccountingSupplierParty":
        blocks = set(own)                     # the buyer issues the seller's invoice: the seller's own data in it
    if cls == "qualification" and role in ("MainQualifyingParty", "AdditionalQualifyingParty", "SubcontractorParty"):
        blocks = set(own) - {"tax"} if pid != top.get("from") else blocks   # the parties the tender relies on
    if cls == "presentation" and role == "BusinessParty":
        blocks = set(own)                     # the business the document presents
    if cls == "invoice" and pid != top.get("from") and PARTY.get(pid, {}).get("identity", {}).get("person") and \
            kind != "CreditNote" and "PaymentMandate" not in str(content.get("PaymentMeans", "")):
        blocks.add("account")                 # the consumer's account the bills are collected from, unless the
        # mandate already names it or nothing is collected (utilities/09#F7, 11#F5)
    if "customs" in blocks and cls == "transport" and not _cross_border(top):
        blocks.discard("customs")
    if cls == "invoice" and pid != top.get("from") and set(_codes(content, "TaxExemptionReasonCode")) & CUSTOMER_TAX_CODES:
        blocks.add("tax")                     # the customer's registration that the exemption rests on
    if cls == "customs" and kind == "ImportCustomsDeclaration" and "Importer" in path:
        blocks.add("tax")                     # the import tax is accounted for under the importer's registration
    if "legal" in blocks or "legal-full" in blocks or "capital" in blocks:
        blocks.add("legal-name")
    if "legal-full" in blocks:
        blocks.add("legal")
    if "capital" in blocks and not capital_on_documents(pid):
        blocks.discard("capital")             # only where the company's law asks for it (O147)
    return blocks


def capital_on_documents(pid):
    p = PARTY.get(pid)
    if not p:
        return False
    form = p["identity"].get("legal", {}).get("form")
    return bool(form and WORLD["countries"][p["c"]]["legal_forms"].get(form, {}).get("capital_on_documents"))


def _codes(node, name):
    if isinstance(node, list):
        for x in node:
            yield from _codes(x, name)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k == name and isinstance(v, V):
                yield v.value
            else:
                yield from _codes(v, name)


def apply_profile(block, blocks, pid):
    """Keep of a full party description only the blocks of its profile."""
    out = {}
    for k, v in block.items():
        b = BLOCK_OF.get(k, "?")
        if b is None or b in blocks:
            out[k] = v
        elif k == "AdditionalPartyIdentification":
            keep = [x for x in v if ("customs" in blocks) or "customs-trader" not in str(x["ID"].attrs.get("schemeID"))]
            if keep:
                out[k] = keep
        elif b == "?":
            raise SystemExit(f"{pid}: party element {k} has no profile block")
    if "PartyLegalEntity" in out:
        out["PartyLegalEntity"] = {k: v for k, v in out["PartyLegalEntity"].items() if LEGAL_OF.get(k, "?") in blocks}
        if not out["PartyLegalEntity"]:
            del out["PartyLegalEntity"]
    if "Person" in out and "account" not in blocks:
        out["Person"] = {k: v for k, v in out["Person"].items() if k != "FinancialAccount"}
    return out



APPLY_PARTY_PROFILE = True     # the party table, approved by the owner 2026-11-17 (O88, analysis/party-profile.md)


def international(doc):
    """A document between the countries: its sender and its receiver are in different countries (O19). Such a
    document is in English, the working language of the Trade Accord."""
    to = doc.get("to")
    return to in PARTY and PARTY[to]["c"] != PARTY[doc["from"]]["c"]


def profiled(top, path, pid):
    """A party at its role in a document: in full, or, with the party table applied, with its profile's blocks.
    A party states the language of the exchange: English across a border, its own language at home (O19)."""
    full = party(pid, desk=desk_for(top, path, pid) if pid in PARTY else None,
                 lang="english" if international(top) else None)
    if not APPLY_PARTY_PROFILE:
        return full
    return apply_profile(full, party_profile(top, path, pid, CONTENT), pid)


CONTENT = {}

def place_parties(doc, content, top=None):
    """Put every party of the world's document at its path, as cac:Party or as a wrapper around it. The role at
    the end of the path picks the party's desk (desk_for); top is the world's document when called for a part."""
    top = top or doc
    for path, pid in doc["parties"].items():
        steps = path.split("/")
        node, abie = content, doc["doc"]
        for k, step in enumerate(steps):
            assoc = next(a for a in MODEL["abies"][abie]["asbies"] if a[0] == step)
            target = assoc[1]
            last = k == len(steps) - 1
            if isinstance(node.get(step), list) and not last:     # into every repetition, e.g. each catalogue line
                for sub in node[step]:
                    place_parties({"doc": target, "parties": {"/".join(steps[k + 1:]): pid}}, sub, top)
                break
            if last and isinstance(pid, list):                   # several parties in one role: one element each
                given = node.get(step) if isinstance(node.get(step), list) else []
                node[step] = [merge(given[i] if i < len(given) else {},
                                    profiled(top, path, x) if target == "Party"
                                    else {"Party": profiled(top, path, x)}) for i, x in enumerate(pid)]
                break
            if last:
                desk = desk_for(top, path, pid) if pid in PARTY else None
                if target == "Party" and step == "SenderParty" and DOC_CLASS.get(top["doc"]) == "presentation" \
                        and top["parties"].get("BusinessParty") == pid:
                    # the business presents itself: its full description goes under BusinessParty, the sender is
                    # only identified (sea/01#F5)
                    node[step] = party(pid, short=True)
                    break
                if target == "Party":
                    block = profiled(top, path, pid)
                elif target == "FinancialInstitution":
                    block = institution(pid)
                else:                                   # a wrapper such as SupplierParty, CustomerParty
                    block = {"Party": profiled(top, path, pid)}
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
INTERNATIONAL = False  # the document being built goes between the countries: English only (O19)
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
            own = given.attrs.get("languageID", "") if isinstance(given, V) else ""
            if own.startswith("en-"):      # a party's master data: in its own country's languages (D2)
                langs = [l for l in WORLD["countries"][own[3:]]["languages"] if l != "en"]
            else:                          # the issuer's text: at home in its languages, across a border English
                langs = [l for l in WORLD["countries"][PARTY[SENDER]["c"]]["languages"] if l != "en"] \
                    if SENDER and bbies[text][1].endswith("n") and not INTERNATIONAL else []
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
                            [V(words("en"), f"{why} In English.", languageID=own or "en")]
            else:
                out[text] = V(words("en"), why, **({"languageID": own} if own else {}))
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
    if rule == "ISO 11649" and not value.startswith("RF"):   # a payer's plain reference, such as a credit note's
        return None                                          # number for a refund (furniture/13#F5)
    if rule is None or rule in SCHEMES:
        return rule
    if rule == "register":           # a company's, a public body's or a grower's register, told by its shape (O142)
        hit = world_ids.register_kind_of(WORLD, value)
        if hit is None:
            raise SystemExit(f"{parent}/{element}: '{value}' fits no country's register format (world/countries.json)")
        return world_ids.national_scheme(*hit)
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
    check_codana(root, where)


CODANA_SCHEMES = {"ISO 6523": r"0990:(\d{5})", "ISO 15459": r"KXU(\d{5})", "ISO 15459-6": r"KXU(\d{5})"}
CODANA_PARTY = {p["identity"]["identification"]["codana_cin"]: pid for pid, p in PARTY.items()
                if (p["identity"].get("identification") or {}).get("convention") == "ISO"}


def check_codana(root, where):
    """O32: the prefix of every Codana identifier is the company number of the party that issued it. Every
    0990 organisation identifier, licence plate and KXU item number starts with the number of a party Codana has
    registered; an organisation identifier stands in the party it identifies (its register number beside it), and
    an item number in an item whose maker, where the document names one, is that party."""
    for e in root.iter(f"{{{NS_CBC}}}ID"):
        rx = CODANA_SCHEMES.get(e.get("schemeID"))
        if not rx:
            continue
        cin = re.match(rx, e.text).group(1)
        owner = CODANA_PARTY.get(cin)
        if not owner:
            raise SystemExit(f"{where}: {root.getroottree().getpath(e)} = {e.text}: {cin} is no party's Codana "
                             "company number (O32)")
        holder = e.getparent().getparent()
        if e.get("schemeID") == "ISO 6523":
            reg = holder.findtext(f"{{{NS_CAC}}}PartyIdentification/{{{NS_CBC}}}ID")
            if reg is not None and reg != PARTY[owner]["identity"]["registry_id"]:
                raise SystemExit(f"{where}: {root.getroottree().getpath(e)} = {e.text} is {owner}'s, but the party "
                                 f"is {reg} (O32)")
        elif e.get("schemeID") == "ISO 15459-6":
            maker = holder.findtext(f"{{{NS_CAC}}}ManufacturerParty/{{{NS_CAC}}}PartyIdentification/{{{NS_CBC}}}ID")
            if maker is not None and maker != PARTY[owner]["identity"]["registry_id"]:
                raise SystemExit(f"{where}: {root.getroottree().getpath(e)} = {e.text} is under {owner}'s prefix, "
                                 f"but the maker is {maker} (O32)")


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
    if code == "en" or "Note" not in content or international(doc):   # across a border: English only (O19)
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


# ---------------------------------------------------------------- the tax arithmetic of a document (worklist C24)
def _line_amounts(node, out):
    """(category ID, percent, amount) of every line with a tax category, anywhere below node."""
    if isinstance(node, list):
        for x in node:
            _line_amounts(x, out)
    elif isinstance(node, dict):
        cat = node.get("Item", {}).get("ClassifiedTaxCategory") if isinstance(node.get("Item"), dict) else None
        if isinstance(node.get("LineExtensionAmount"), V) and isinstance(node.get("Item"), dict):
            cid = cat["ID"].value if isinstance(cat, dict) and isinstance(cat.get("ID"), V) else None
            pct = cat.get("Percent").value if isinstance(cat, dict) and isinstance(cat.get("Percent"), V) else "0"
            out.append((cid, Decimal(pct), Decimal(node["LineExtensionAmount"].value)))
            return
        for k, v in node.items():         # a levy collected for someone else is no part of the supply
            if k not in ("AllowanceCharge", "TaxTotal", "CollectionInvoiceLine", "CollectionCreditNoteLine"):
                _line_amounts(v, out)


def tax_arithmetic(content, where):
    """A subtotal's taxable amount is the lines of its category plus the document's charges less its allowances
    of that category; an allowance or charge without a category, in a document with one category, takes it."""
    tt = content.get("TaxTotal")
    subs = tt.get("TaxSubtotal") if isinstance(tt, dict) else None
    subs = subs if isinstance(subs, list) else [subs] if isinstance(subs, dict) else []
    if not subs:
        return
    lines = []
    _line_amounts(content, lines)
    if not lines:
        return
    acs = content.get("AllowanceCharge")
    acs = acs if isinstance(acs, list) else [acs] if isinstance(acs, dict) else []
    if len(subs) == 1:                        # a line without a category belongs to the document's only one
        only = subs[0]["TaxCategory"]["ID"].value
        lines = [(c or only, p, a) for c, p, a in lines]
    cats = {x[0] for x in lines}
    for ac in acs:
        if "TaxCategory" not in ac and len(cats) == 1 and len(subs) == 1:
            ac["TaxCategory"] = {k: v for k, v in subs[0]["TaxCategory"].items()}
    for sub in subs:
        cid = sub["TaxCategory"]["ID"].value
        base = sum(a for c, _, a in lines if c == cid)
        for ac in acs:
            if isinstance(ac.get("TaxCategory"), dict) and ac["TaxCategory"]["ID"].value == cid:
                sign = 1 if ac["ChargeIndicator"].value == "true" else -1
                base += sign * Decimal(ac["Amount"].value)
        old = sub["TaxableAmount"]
        if Decimal(old.value) != base:
            pct = sub["TaxCategory"].get("Percent")
            if isinstance(pct, V) and Decimal(pct.value) != 0:
                raise SystemExit(f"{where}: taxable amount of category {cid} is {old.value}, the lines and charges "
                                 f"make {base}: the tax would change (worklist C24)")
            sub["TaxableAmount"] = V(f"{base:.{len(old.value.partition('.')[2])}f}", "The lines of this category "
                                     "plus the document's charges less its allowances of the category (worklist "
                                     "C24).", **old.attrs)


# ---------------------------------------------------------------- the invoice behind a customs value (worklist C12)
def declaration_invoices(content, doc):
    """A customs declaration refers to the commercial invoice its value rests on: an invoice of the same flow
    from the exporter to the importer, issued on or before the declaration."""
    if doc["doc"] not in ("ExportCustomsDeclaration", "ImportCustomsDeclaration"):
        return
    ps = doc.get("parties", {})
    exporter = ps.get("ExporterParty") or ps.get("CustomsDeclaration/ExporterParty")
    importer = ps.get("ImporterParty") or ps.get("CustomsDeclaration/ImporterParty")
    # an import without an exporter named: the consignor's invoice, not any invoice to the importer (energy/10:
    # the retail company also buys the grid operator's network service)
    exporter = exporter or (ps.get("ConsignorParty") if doc["doc"] == "ImportCustomsDeclaration" else None)
    day = content.get("IssueDate").value if isinstance(content.get("IssueDate"), V) else None
    doc_types()
    legs = [leg for fl in WORLD["flows"] if fl["id"] == doc["flow"] for leg in fl.get("legs", [])]
    carriers = {leg["carrier"] for leg in legs} - {leg["from"] for leg in legs}   # a seller may carry its own goods
    hits = [i for i, (d, w) in DOC_DATES.items()
            if w["flow"] == doc["flow"] and w["doc"] == "Invoice" and day and d <= day and w["from"] not in carriers
            and (w["from"] == exporter if exporter else w["to"] == importer)]
    if not hits:
        return
    holder = content["CustomsDeclaration"] if doc["doc"] == "ExportCustomsDeclaration" and \
        isinstance(content.get("CustomsDeclaration"), dict) else content
    refs = holder.get("AdditionalDocumentReference")
    refs = [refs] if isinstance(refs, dict) else list(refs or [])
    have = {r["ID"].value for r in refs if isinstance(r.get("ID"), V)}
    refs += [{"ID": V(i, "The commercial invoice the customs value rests on (worklist C12).")}
             for i in sorted(hits) if i not in have]
    holder["AdditionalDocumentReference"] = refs


# ---------------------------------------------------------------- the transport at the border (worklist C12)
MODE_CODES = {"sea": "1", "rail": "2", "road": "3", "air": "4", "pipeline": "7", "river": "8"}


def border_transport(content, doc):
    """A customs declaration says how the goods cross the border: the mode of the flow's leg that crosses it."""
    if not doc["doc"].endswith("CustomsDeclaration"):
        return
    ship = content.get("CustomsDeclaration", {}).get("Shipment") if doc["doc"] == "ExportCustomsDeclaration" \
        else content.get("Shipment")
    if not isinstance(ship, dict) or "ShipmentStage" in ship:
        return
    legs = next(fl for fl in WORLD["flows"] if fl["id"] == doc["flow"]).get("legs", [])
    cross = [leg for leg in legs if PARTY[leg["from"]]["c"] != PARTY[leg["to"]]["c"]]
    if not cross:
        return
    mode = cross[0]["mode"]
    ship["ShipmentStage"] = {"TransportModeCode": V(MODE_CODES[mode], f"The goods cross the border by {mode} "
                                                    "(worklist C12).",
                                                    listID="UNECE Recommendation 19 - Codes for Modes of Transport")}


# ---------------------------------------------------------------- a national tariff in its own country (worklist C29)
SELLER_ROLES = ("SellerSupplierParty", "AccountingSupplierParty", "DespatchSupplierParty", "ProviderParty")


def document_country(doc):
    """The country whose national rules a document follows: the declaring country of a customs declaration (the
    declarant, its sender), else the seller's (decision Q24: tariffs stay national)."""
    if doc["doc"].endswith("CustomsDeclaration"):
        return PARTY[doc["from"]]["c"]
    for role in SELLER_ROLES:
        pid = doc.get("parties", {}).get(role)
        if isinstance(pid, str) and pid in PARTY:
            return PARTY[pid]["c"]
    return PARTY[doc["from"]]["c"] if doc["from"] in PARTY else None


def national_tariffs(content, doc):
    """A national tariff subheading appears only in documents of the country whose tariff it is."""
    country = document_country(doc)

    def walk(node):
        if isinstance(node, list):
            for x in node:
                walk(x)
        elif isinstance(node, dict):
            ccs = node.get("CommodityClassification")
            if isinstance(ccs, list):
                keep = [cc for cc in ccs if not (isinstance(cc.get("CommodityCode"), V) and any(
                    cc["CommodityCode"].attrs.get("listID") == codelists.NATIONAL.format(c, "CustomsTariff")
                    for c in WORLD["countries"] if c != country))]
                node["CommodityClassification"] = keep if len(keep) > 1 else keep[0] if keep else ccs
            for v in node.values():
                walk(v)
    walk(content)


# ---------------------------------------------------------------- currencies with something to convert (worklist C11)
CURRENCY_PAIRS = {"PricingCurrencyCode": "PricingExchangeRate", "TaxCurrencyCode": "TaxExchangeRate",
                  "PaymentCurrencyCode": "PaymentExchangeRate",
                  "PaymentAlternativeCurrencyCode": "PaymentAlternativeExchangeRate",
                  "RequestedInvoiceCurrencyCode": None}
RATE_FREE_DOCS = {"ForwardingInstructions", "Waybill", "BillOfLading", "Statement", "RemittanceAdvice",
                  "InvoiceStatusResponse", "UtilityStatement"}


def _currencies(node, out, prices=None):
    if isinstance(node, list):
        for x in node:
            _currencies(x, out, prices)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k.endswith("ExchangeRate") or k == "ExchangeRate":
                continue
            if isinstance(v, V) and v.attrs.get("currencyID"):
                out.add(v.attrs["currencyID"])
                if prices is not None and k == "PriceAmount":
                    prices.add(v.attrs["currencyID"])
            _currencies(v, out, prices)


# ---------------------------------------------------------------- what a document says about an item (C48, D11, O20)
ITEM_BLOCK = {      # each element of cac:Item that the item's master data gives, by block
    "Name": "name", "Description": "desc",
    "SellersItemIdentification": "id", "BuyersItemIdentification": "id", "StandardItemIdentification": "id",
    "ManufacturersItemIdentification": "id", "AdditionalItemIdentification": "id",
    "CatalogueItemIdentification": "id", "CatalogueDocumentReference": "id",
    "ClassifiedTaxCategory": "tax", "CommodityClassification": "class",
    "OriginCountry": "origin", "OriginAddress": "origin", "ItemInstance": "instance",
    "HazardousItem": "dg", "BrandName": "brand", "WarrantyInformation": "warranty",
    "PackQuantity": "pack", "PackSizeNumeric": "pack",
    "Keyword": "type", "ModelName": "type", "AdditionalInformation": "type", "Dimension": "type",
    "AdditionalItemProperty": "type", "ItemSpecificationDocumentReference": "type", "LifecycleStageCode": "type",
    "LifecycleStageDescription": "type", "Certificate": "type", "EnvironmentalCertificate": "type",
    "CircularityProfile": "type", "EnvironmentalEmission": "type", "ManufacturerParty": "type",
    "InformationContentProviderParty": "type", "TransactionConditions": "type",
}
ITEM_KIND = {}
for _kind, _docs in {
    "catalogue": "Catalogue CatalogueItemSpecificationUpdate",
    "offer": "Tender Quotation",
    "order": "Order OrderResponse OrderChange OrderCancellation RequestForQuotation Forecast ForecastRevision "
             "InventoryReport ProductActivity RetailEvent TradeItemLocationProfile ItemInformationRequest "
             "CataloguePricingUpdate CatalogueDeletion CatalogueRequest ExceptionCriteria ExceptionNotification "
             "InstructionForReturns WorkReport DigitalAgreement TenderContract",
    "despatch": "DespatchAdvice ReceiptAdvice DeliveryNote PackingList FulfilmentCancellation",
    "invoice": "Invoice CreditNote DebitNote SelfBilledInvoice SelfBilledCreditNote Reminder Statement "
               "UtilityStatement RemittanceAdvice",
    "receipt": "PurchaseReceipt",
    "customs": "ImportCustomsDeclaration ExportCustomsDeclaration TransitCustomsDeclaration CertificateOfOrigin "
               "GoodsCertificate",
    "carnet": "GoodsItemPassport ProofOfReexportation ProofOfReexportationRequest ProofOfReexportationReminder",
    "transport": "Waybill BillOfLading ForwardingInstructions TransportExecutionPlan TransportExecutionPlanRequest "
                 "TransportationStatus TransportationStatusRequest TransportProgressStatus "
                 "TransportProgressStatusRequest Manifest CommonTransportationReport WeightStatement "
                 "GoodsItemItinerary TransportServiceDescription TransportServiceDescriptionRequest",
    "waste": "WasteMovement WasteNotification",
    "notice": "PriorInformationNotice ContractNotice CallForTenders ContractAwardNotice AwardedNotification "
              "UnawardedNotification ProcurementStatus ProcurementStatusRequest ExpressionOfInterestRequest "
              "ExpressionOfInterestResponse UnsubscribeFromProcedureRequest UnsubscribeFromProcedureResponse "
              "TenderReceipt TenderWithdrawal TendererQualification TendererQualificationResponse "
              "QualificationApplicationRequest QualificationApplicationResponse GuaranteeCertificate",
    "message": "ApplicationResponse DocumentStatus DocumentStatusRequest InvoiceStatusRequest InvoiceStatusResponse "
               "BusinessCard BusinessInformation DigitalCapability",
}.items():
    for _d in _docs.split():
        ITEM_KIND[_d] = _kind
_TYPE = {"name", "desc", "id", "class", "origin", "brand", "warranty", "pack", "type", "dg", "tax"}
ITEM_PROFILE = {
    "catalogue": _TYPE,             # a lot's certificate is no fact of the type: not in the catalogue
    "offer": _TYPE - {"tax"},
    "order": {"name", "desc", "id", "pack", "tax"},
    "despatch": {"name", "desc", "id", "instance", "lot", "dg", "pack"},
    "invoice": {"name", "desc", "id", "lot", "tax"},
    "receipt": {"name", "desc", "id", "brand", "warranty", "tax"},
    "customs": {"name", "desc", "class", "origin", "dg"},
    "carnet": {"name", "desc", "id", "class", "origin", "instance"},
    "transport": {"name", "desc", "class", "dg"},
    "waste": {"name", "desc", "class", "dg"},
    "notice": {"name", "desc", "class"},
    "message": {"name", "desc", "id"},
}
APPLY_ITEM_PROFILE = True     # the item table, approved by the owner 2026-11-17 (O20, analysis/item-profile.md)


def item_profiles(content, doc):
    """Every item in a document carries the facts of its kind of document (D11): a fact is stated first in the
    document of the moment it becomes known, and a later document repeats it only if its own transaction uses it.
    Only the item's master data is filtered; what the scenario adds for this transaction (a variant chosen, a
    colour made to order, a lot) stays."""
    kind = ITEM_KIND.get(doc["doc"])
    if kind is None:
        raise SystemExit(f"{doc['doc']}: no item profile kind (item_profiles)")
    keep = ITEM_PROFILE[kind]

    def walk(node):
        if isinstance(node, list):
            for x in node:
                walk(x)
            return
        if not isinstance(node, dict):
            return
        master = node.pop("_master", None)
        lot = node.pop("_lot", set())
        if master is not None and APPLY_ITEM_PROFILE:
            for k in list(node):
                block = "lot" if k in lot else ITEM_BLOCK.get(k, "id")
                if k in master and master[k] == id(node[k]) and block not in keep:
                    del node[k]
        for v in node.values():
            walk(v)
    walk(content)


# ---------------------------------------------------------------- customs value on each country's basis (C52, D16)
def world_rate(a, b):
    if a == b:
        return Decimal(1)
    r = WORLD["exchange_rates"]
    return Decimal(str(r[f"{a}/{b}"])) if f"{a}/{b}" in r else 1 / Decimal(str(r[f"{b}/{a}"]))


VALUATION = {   # flow -> what the declarations add to or take from the goods lines, by D16 and WTO Articles 1 and 8
    "wood": [("all", Decimal("240.00"), "XBL", "the export pallets the buyer pays for, part of the price paid")],
    "tender": [("all", Decimal("200.00"), "XBL", "the special colour, part of the price paid")],
    "plastics": [("all", Decimal("-1794.00"), "XBL", "less the river freight after loading, which the seller "
                                                     "distinguished from the price (179,400 ferra)")],
    # the CIF price holds the sea freight and the insurance (D30 point 1): it is Lisavu's landed value as it stands,
    # and Bayvarra's value at export is the price less them, which the seller's forwarder bills it (sea/18)
    "sea": [("XB", lambda: -(__import__("examples_scenarios").SEA_FREIGHT
                             + __import__("examples_scenarios").INSURANCE), "XBL",
             "less the sea freight and the cargo insurance to the island, which the CIF price holds")],
}


def customs_values(content, doc):
    """A customs declaration values the goods on the basis of the country it is lodged in (D16, after the WTO
    Valuation Agreement, Articles 1 and 8): Urvania the price paid with freight and insurance to its border,
    Bayvarra the price paid as the goods left the exporting country, Lisavu the price paid with freight and
    insurance to the island; charges that are part of the price belong to it, and carriage after the border
    stays out only where it is distinguished from the price (Note to Article 1). The goods lines carry the price
    of the goods; VALUATION adds the rest, shared over the goods items by their value."""
    if doc["doc"] not in ("ExportCustomsDeclaration", "ImportCustomsDeclaration"):
        return
    rules = VALUATION.get(doc["flow"])
    if not rules:
        return
    country = PARTY[doc["parties"].get("CustomsParty") or doc["to"]]["c"]
    holder = content.get("CustomsDeclaration", content) if doc["doc"] == "ExportCustomsDeclaration" else content
    goods = holder["Shipment"]["GoodsItem"]
    goods = goods if isinstance(goods, list) else [goods]
    vals = [Decimal(g["DeclaredCustomsValueAmount"].value) for g in goods]
    cur = goods[0]["DeclaredCustomsValueAmount"].attrs["currencyID"]
    minor = {"XUF": 0, "XBL": 2, "XLC": 3}[cur]
    q = Decimal(1).scaleb(-minor)
    adds = [((a() if callable(a) else a) * world_rate(c, cur), why) for scope, a, c, why in rules
            if scope in ("all", country)]
    if not adds:
        return
    extra = sum(a for a, _ in adds)
    base = sum(vals)
    shares = [(extra * v / base).quantize(q) for v in vals]
    shares[-1] = extra.quantize(q) - sum(shares[:-1])
    basis = {"XU": "Urvania values the goods with freight and insurance to its border",
             "XB": "Bayvarra values the goods as they left the exporting country",
             "XL": "Lisavu values the goods with freight and insurance to the island"}[country]
    text = "; ".join(f"{why} ({a.quantize(q):,} {cur})" for a, why in adds)
    for g, v, sh in zip(goods, vals, shares):
        old = g["DeclaredCustomsValueAmount"]
        g["DeclaredCustomsValueAmount"] = V(str((v + sh).quantize(q)), f"{basis} (D16): the goods at "
                                            f"{v.quantize(q):,} {cur}, with {text}, shared over the goods items by "
                                            "their value.", **old.attrs)


# ---------------------------------------------------------------- origin and the tax due at import (C57, D18)
def origin_notes(content):
    """The exporter's statement on origin (examples_kit.origin_statement) goes into the invoice's note."""
    stmt = content.pop("_origin", None)
    if not stmt:
        return
    why = ("The exporter's statement on origin: the proof of origin the buyer's import declaration refers to, "
           "to claim the Trade Accord's preference (D18).")
    note = content.get("Note")
    if note is None:
        content["Note"] = V(stmt, why)
    elif isinstance(note, V):
        content["Note"] = V(f"{note.value} {stmt}", f"{note.why} {why}", **note.attrs)
    else:
        raise SystemExit("origin_notes: a statement on origin and several notes")


ITEM_BY_NAME = {it["name"]: iid for iid, it in ITEM.items()}


def kit_maker(iid):
    """The item as its maker sells it: a resold item has the maker's origin."""
    it = ITEM[iid]
    while it.get("resale_of"):
        it = ITEM[it["resale_of"]]
    return it


def import_preference(content, doc):
    """An import declaration claims the Trade Accord's preference for goods of Accord origin, names the criterion
    and refers to its proof of origin, and states what is due at import by its country's rule (D18): in Urvania
    value added tax of 20 % on the customs value, which a business deducts again; in Bayvarra nothing; in Lisavu
    the import consumption tax of 10 % on the landed value. UBL's import declaration has no tax total, so the
    goods item carries the tax category and the note the amount."""
    if doc["doc"] != "ImportCustomsDeclaration":
        return
    c = PARTY[doc["parties"]["ImporterParty"]]["c"]
    country = WORLD["countries"][c]
    goods = content["Shipment"]["GoodsItem"]
    goods = goods if isinstance(goods, list) else [goods]
    total, cur = Decimal(0), None
    for g in goods:
        iid = ITEM_BY_NAME[g["Description"].value]
        mk = kit_maker(iid)
        if mk["origin"] == c:
            raise SystemExit(f"{doc['flow']}: import of goods of the importing country's own origin")
        g["PreferenceCriterionCode"] = V(mk["origin_criterion"], f"The goods are of {mk['origin']} origin under the "
                                         "Trade Accord, by this criterion: the preference claimed, free of duty "
                                         "(D18).")
        value = g["DeclaredCustomsValueAmount"]
        total += Decimal(value.value)
        cur = value.attrs["currencyID"]
        if c == "XU":
            g["Item"]["ClassifiedTaxCategory"] = {
                "ID": V("S", "Urvania's value added tax at import, at the standard rate."),
                "Percent": V(str(country["tax"]["schemes"][0]["rates"]["standard"]), "The standard rate."),
                "TaxScheme": {"ID": V("VAT", "UN/EDIFACT 5153 code VAT: value added tax.")}}
        elif c == "XL":
            imp = next(x for x in country["tax"]["schemes"] if x["id"] == "IMP")
            g["Item"]["ClassifiedTaxCategory"] = {
                "ID": V("S", "The island's import consumption tax applies."),
                "Percent": V(str(imp["rate"]), "Its rate, on the landed value."),
                "TaxScheme": {"ID": V("IMP", "The island's import consumption tax, as the world codes it."),
                              "TaxTypeCode": V("CONSUMPTION", "A tax on consumption, charged at import.")}}
    minor = 3 if cur == "XLC" else 2 if cur == "XBL" else 0
    q = Decimal(1).scaleb(-minor)
    money_name = next(x["currency"]["name"].lower() for x in WORLD["countries"].values()
                      if x["currency"]["code"] == cur) if cur else ""
    if c == "XU":
        rate = country["tax"]["schemes"][0]["rates"]["standard"]
        tax = (total * rate / 100).quantize(q)
        text = (f"No duty: goods of Accord origin. Import value added tax: {rate} % of the customs value of {total:,} "
                f"{money_name}, {tax:,} {money_name}, paid at the border; the importer deducts it again in its return.")
    elif c == "XL":
        tax = (total * 10 / 100).quantize(q)
        text = (f"No duty: goods of Accord origin. Import consumption tax: 10 % of the landed value of {total:,} "
                f"{money_name}, {tax:,} {money_name}.")
    else:
        text = ("No duty: goods of Accord origin. No tax is due at import: Bayvarra's sales tax is charged once, at "
                "the final retail sale.")
    content["Note"] = V(text, "What is due at import, by the importing country's rule (D18).")
    refs = content.get("AdditionalDocumentReference")
    refs = [refs] if isinstance(refs, dict) else list(refs or [])
    for r in refs:
        w = r["ID"].why
        if "commercial invoice" in w and not any(d["doc"] == "CertificateOfOrigin" for d in WORLD["documents"]
                                                 if d["flow"] == doc["flow"]):
            r["ID"] = V(r["ID"].value, w.rstrip(".") + "; its statement on origin is the proof of origin the "
                                                       "preference claim refers to (D18).", **r["ID"].attrs)
        elif "certificate of origin" in w.lower():
            r["ID"] = V(r["ID"].value, w.rstrip(".") + "; the proof of origin the preference claim refers to "
                                                       "(D18).", **r["ID"].attrs)


# ---------------------------------------------------------------- a Lisavan sale has no tax section (C50, D15)
SELLER_ROLES = ("AccountingSupplierParty", "SellerSupplierParty", "SupplierParty", "ProviderParty")


def untaxed_sales(content, doc):
    """Lisavu has no sales tax or value added tax, so a Lisavan seller's document carries no tax section at all: no
    TaxTotal, no tax category on a line, an item or a charge, no tax scheme; its totals with and without tax are
    the same. The island's own taxes keep theirs: the presumptive tax withheld on farm produce
    (WithholdingTaxTotal) and the duty and import tax of the customs declarations (D18)."""
    if DOC_CLASS.get(doc["doc"]) == "customs":
        return
    seller = next((doc["parties"][r] for r in SELLER_ROLES if isinstance(doc["parties"].get(r), str)), None)
    if seller is None and (DOC_CLASS.get(doc["doc"]) == "invoice" or doc["doc"] == "UtilityStatement"):
        seller = doc["from"]
    if seller not in PARTY or PARTY[seller]["c"] != "XL":
        return

    def strip(node):
        if isinstance(node, list):
            for x in node:
                strip(x)
            return
        if not isinstance(node, dict):
            return
        for k in list(node):
            if k in ("TaxTotal", "ClassifiedTaxCategory", "TaxCategory", "TaxCurrencyCode", "TaxExchangeRate",
                     "TaxPointDate"):
                del node[k]
            elif k != "WithholdingTaxTotal":
                strip(node[k])
    strip(content)
    for total in ("LegalMonetaryTotal", "RequestedMonetaryTotal", "AnticipatedMonetaryTotal"):
        t = content.get(total)
        if isinstance(t, dict) and isinstance(t.get("TaxInclusiveAmount"), V):
            v = t["TaxInclusiveAmount"]
            t["TaxInclusiveAmount"] = V(v.value, "The same as the total without tax: Lisavu has no sales tax or "
                                                 "value added tax, so no tax is due and the document has no tax "
                                                 "section (D15).", **v.attrs)


# ---------------------------------------------------------------- party roles that only repeat another (worklist C08)
def _party_key(node):
    """Who a party element names: its first identifier, else its name. A wrapper (CustomerParty and the like) is
    looked into."""
    if not isinstance(node, dict):
        return None
    if "Party" in node and isinstance(node["Party"], dict):
        node = node["Party"]
    ids = node.get("PartyIdentification")
    ids = ids[0] if isinstance(ids, list) and ids else ids
    if isinstance(ids, dict) and isinstance(ids.get("ID"), V):
        return ids["ID"].value
    name = node.get("PartyName")
    name = name[0] if isinstance(name, list) and name else name
    if isinstance(name, dict) and isinstance(name.get("Name"), V):
        return name["Name"].value
    return None


def _own_contact(node, base):
    """A role that repeats a party but gives it a contact of its own (a helpdesk, a tender box) says something."""
    def contact(n):
        n = n.get("Party", n) if isinstance(n, dict) else {}
        return str(n.get("Contact", "")) + str(n.get("EndpointID", ""))
    return contact(node) and contact(node) != contact(base)


ROLE_EQUALS = {      # a role that adds nothing when it names the same party as one of these
    "OriginatorCustomerParty": ("BuyerCustomerParty", "ContractingParty", "AccountingCustomerParty"),
    "BeneficiaryParty": ("BuyerCustomerParty", "ContractingParty", "AccountingCustomerParty", "CollectedForParty"),
    "OriginatorParty": ("OriginatorCustomerParty", "BuyerCustomerParty", "ContractingParty",
                        "AccountingCustomerParty"),
    "CustomerParty": ("ReceiverParty",),
    "NotifierParty": ("ImporterParty", "ExporterParty", "DeclarantParty"),
    "SourceIssuerParty": ("SenderParty",),
    "PerformingCarrierParty": ("CarrierParty",),
    "FreightForwarderParty": ("CarrierParty",),
    "AdditionalInformationParty": ("ContractingParty",),
    "DocumentProviderParty": ("ContractingParty",),
    "TenderRecipientParty": ("ContractingParty",),
    "ContractResponsibleParty": ("ContractingParty",),
    "TenderEvaluationParty": ("ContractingParty",),
    "QualificationRequestRecipientParty": ("ContractingParty",),
}
TENDER_ROLES = {"AdditionalInformationParty", "DocumentProviderParty", "TenderRecipientParty",
                "ContractResponsibleParty", "TenderEvaluationParty", "QualificationRequestRecipientParty"}


def _consignments(node):
    """The node itself, its consignments and its shipment's consignments: where the carrier of the goods is."""
    out = [node]
    for holder in (node, node.get("Shipment", {})):
        for c in (holder.get("Consignment", []) if isinstance(holder, dict) else []):
            out.append(c)
        if isinstance(holder, dict) and isinstance(holder.get("Consignment"), dict):
            out.append(holder["Consignment"])
    return [x for x in out if isinstance(x, dict)]


LINE_REPEATS = {        # roles a line repeats needlessly when the header or the line above names the same party
    "OriginatorParty", "OriginatorCustomerParty", "BeneficiaryParty", "ContractorCustomerParty",
    "SellerSupplierParty", "ManufacturerParty", "PerformingParty"}
NOT_THEIR_PARTIES = {   # documents whose subject is not the order: its originator and beneficiary do not belong
    "FulfilmentCancellation", "Statement", "RemittanceAdvice"}


def redundant_roles(content, doc):
    """Drop every party role that only names a party the document already gives in a role that covers it (worklist
    C08): originator and beneficiary equal to the buyer or contracting party, the customer equal to the receiver, the
    importer as its own notifier, the sender as source issuer, the carrier as performing carrier or forwarder, the
    contracting party repeated in each tendering role, a line party equal to the same party of the header or of the
    line above, and a distribution copy to the document's own addressee."""
    def walk(node, scope):
        if isinstance(node, list):
            for x in node:
                walk(x, scope)
            return
        if not isinstance(node, dict):
            return
        here = dict(scope)
        for k, v in node.items():
            key = _party_key(v) if k.endswith("Party") else None
            if key:
                here.setdefault(k, (key, v))
        if "FreightForwarderParty" in node and "FreightForwarderParty" not in scope:   # the consignment's carrier
            carriers = {_party_key(c.get("CarrierParty")) for c in _consignments(node)}
            if _party_key(node["FreightForwarderParty"]) in carriers:
                del node["FreightForwarderParty"]
        for k in list(node):
            v = node[k]
            if not k.endswith("Party") or not isinstance(v, dict):
                continue
            key = _party_key(v)
            if not key:
                continue
            if doc["doc"] in NOT_THEIR_PARTIES and k in ("OriginatorCustomerParty", "BeneficiaryParty",
                                                         "OriginatorParty"):
                del node[k]
                continue
            same = [scope[k]] if k in scope and k in LINE_REPEATS else []   # the same role higher up
            same += [here[b] for b in ROLE_EQUALS.get(k, ()) if b in here and b != k]
            if any(b[0] == key and not (k in TENDER_ROLES and _own_contact(v, b[1])) for b in same):
                del node[k]
                if k == "PerformingCarrierParty":
                    node.pop("PerformingCarrierAssignedID", None)
        if "DocumentDistribution" in node:
            roles = ("ReceiverParty", "FreightForwarderParty") if doc["doc"] == "ForwardingInstructions" \
                else ("ReceiverParty",)                        # forwarding instructions go to the forwarder
            addressees = {here[r][0] for r in roles if r in here}
            dd = node["DocumentDistribution"]
            keep = [x for x in (dd if isinstance(dd, list) else [dd]) if _party_key(x) not in addressees]
            if keep:
                node["DocumentDistribution"] = keep if isinstance(dd, list) else keep[0]
            else:
                del node["DocumentDistribution"]
        for k, v in node.items():
            if isinstance(v, (dict, list)) and not k.endswith("Party"):
                walk(v, {r: x for r, x in here.items()})
    walk(content, {})


def currency_cleanup(content, doc):
    """Every currency code and exchange rate converts something the document states (worklist C11): no currency
    equal to the document's, no rate from a currency to itself, no pricing currency the prices are not in, no
    alternative payment currency without an amount in it, and no free-standing rate in a transport document, a
    statement, a remittance or a status response when no amount is in the other currency."""
    dc = content.get("DocumentCurrencyCode")
    dc = dc.value if isinstance(dc, V) else None
    used, prices = set(), set()
    _currencies(content, used, prices)
    for code, rate in CURRENCY_PAIRS.items():
        v = content.get(code)
        if not isinstance(v, V):
            continue
        drop = v.value == dc
        if code == "PricingCurrencyCode" and prices and v.value not in prices:
            drop = True
        if code == "PaymentAlternativeCurrencyCode" and "PayableAlternativeAmount" not in str(content.get(
                "LegalMonetaryTotal", "")):
            drop = True
        if drop:
            del content[code]
            if rate:
                content.pop(rate, None)
    if "PricingExchangeRate" in content and "PricingCurrencyCode" not in content:
        del content["PricingExchangeRate"]

    def walk(node, free):
        if isinstance(node, list):
            for x in node:
                walk(x, free)
            return
        if not isinstance(node, dict):
            return
        for k in list(node):
            v = node[k]
            if (k == "ExchangeRate" or k.endswith("ExchangeRate")) and isinstance(v, dict):
                src, tgt = v.get("SourceCurrencyCode"), v.get("TargetCurrencyCode")
                src, tgt = (src.value if isinstance(src, V) else None), (tgt.value if isinstance(tgt, V) else None)
                other = {src, tgt} - {dc, None}
                idle = not (other & used) if dc else not ({src, tgt} <= used)   # no amount in the other currency
                cites = "BillingReference" in node and src not in (dc, None) and tgt == dc   # paying a document
                #                                                         in another currency, into this one
                if src == tgt or (free and k == "ExchangeRate" and idle and not cites):
                    del node[k]
                    continue
            walk(v, free)
    walk(content, doc["doc"] in RATE_FREE_DOCS)


# ---------------------------------------------------------------- items ordered from a catalogue (worklist C25)
def catalogue_items(content, doc):
    """An order placed from the seller's catalogue, which it cites, marks its items as ordered from it: the place
    of CatalogueIndicator, not the catalogue itself."""
    if doc["doc"] not in ("Order", "OrderChange"):
        return
    lines = content.get("OrderLine")
    for line in lines if isinstance(lines, list) else [lines] if lines else []:
        it = line.get("LineItem", {}).get("Item")
        if isinstance(it, dict) and ("CatalogueDocumentReference" in it or "CatalogueReference" in line or
                                     "CatalogueDocumentReference" in content):
            it.setdefault("CatalogueIndicator", V("true", "The item is ordered from the seller's catalogue, which "
                                                          "the order cites."))


# ---------------------------------------------------------------- when an order wants its goods (worklist C28)
def requested_delivery(content, doc, n):
    """Every order and order change states when the goods are wanted (or, ex works, when they are collected); where
    the scenario states nothing, the flow's table gives the period."""
    if doc["doc"] not in ("Order", "OrderChange"):
        return
    deliveries = content.get("Delivery")
    for d in deliveries if isinstance(deliveries, list) else [deliveries] if deliveries else []:
        if any(k in d for k in ("RequestedDeliveryPeriod", "LatestDeliveryDate", "PromisedDeliveryPeriod")) or \
                any(k in d.get("Despatch", {}) for k in ("RequestedDespatchDate", "RequestedDespatchPeriod")):
            return
    import examples_kit
    import examples_scenarios
    hit = examples_scenarios.REQUESTED_DELIVERY.get((doc["flow"], n))
    if not hit:
        raise SystemExit(f"{doc['flow']} {n} {doc['doc']}: the order does not say when the goods are wanted "
                         "(worklist C28; REQUESTED_DELIVERY in tools/examples_scenarios.py)")
    flow = next(v for v in vars(examples_scenarios).values()
                if isinstance(v, examples_kit.Flow) and v.id == doc["flow"])
    period = {"RequestedDeliveryPeriod": {"StartDate": V(flow.date(hit[0]), hit[2]),
                                          "EndDate": V(flow.date(hit[1]), "The last day it is wanted.")}}
    if isinstance(deliveries, list):
        deliveries[0].update(period)
    elif isinstance(deliveries, dict):
        deliveries.update(period)
    else:
        content["Delivery"] = period


# ---------------------------------------------------------------- places with their identifiers (worklist C23)
def known_places():
    """Every place the world identifies, by its name: the UN/LOCODE-form towns, ports and airports, and the named
    places at the ends of the transport legs (world/documents.json) with their GLN or code."""
    import examples_kit
    out = {name: ("UN/LOCODE", code) for code, (name, _) in examples_kit.PLACES.items()}
    for fl in WORLD["flows"]:
        for leg in fl.get("legs", []):
            for end in ("from_place", "to_place"):
                pl = leg.get(end) or {}
                if pl.get("gln"):
                    pid, key = pl["gln"].split(":")
                    out[pl["name"]] = ("GS1 GLN", PARTY[pid]["identity"]["identification"]["locations"][key]["gln"])
                elif pl.get("locode"):
                    out.setdefault(pl["name"], ("UN/LOCODE", pl["locode"]))
    for p in WORLD["parties"]:                  # the GS1 parties' own places, by the names they give them
        for loc in p["identity"].get("identification", {}).get("locations", {}).values():
            out.setdefault(loc["name"], ("GS1 GLN", loc["gln"]))
    for alias, name in PLACE_ALIASES.items():   # the same places under the names the documents use
        out.setdefault(alias, out[name])
    return out


# names the documents give places the world identifies under another name
PLACE_ALIASES = {"Lumeport": "Port of Lumeport", "Selanu": "Port of Selanu",
                 "Rail siding of Lumeway Distribution, Marrowdale": "Rail siding of the distribution centre, Marrowdale",
                 "Brightmarket Stores, goods-in": "Goods-in of the Lumeport store",
                 "Brightmarket Stores, goods-in, Lumeport": "Goods-in of the Lumeport store",
                 "Valdara Industries, goods-in, Ferrano": "Valdara Industries works, Ferrano",
                 "Selanu airport": "Selanu airport, cargo terminal", "Lumeport airport": "Lumeport airport, cargo terminal"}


def identify_places(content):
    """A location the world identifies elsewhere carries its identifier wherever it is given by name only."""
    places = known_places()

    def walk(node):
        if isinstance(node, list):
            for x in node:
                walk(x)
        elif isinstance(node, dict):
            for k, v in node.items():
                text = v.get("Name") if isinstance(v, dict) else None
                if not isinstance(text, V) and isinstance(v, dict):
                    text = v.get("Description")
                if k.endswith("Location") and isinstance(v, dict) and "ID" not in v and isinstance(text, V):
                    hit = places.get(text.value.rstrip("."))
                    if hit:
                        node[k] = {"ID": V(hit[1], "The place's identifier, as the world gives it wherever the "
                                                   f"place appears ({'a GLN' if hit[0] == 'GS1 GLN' else 'a code in the form of a UN/LOCODE'}; "
                                                   "worklist C23).", schemeID=hit[0]), **v}
                walk(v)
    walk(content)


# ---------------------------------------------------------------- what a transport document carries (worklist C21)
TRANSPORT_GOODS_DOCS = {"TransportExecutionPlanRequest", "TransportExecutionPlan", "Waybill",
                        "ForwardingInstructions", "BillOfLading"}


def transport_goods(content, doc):
    """A transport request, plan, consignment note, forwarding instruction or bill of lading says what it carries:
    its consignment gets the goods items of the flow's deal where the scenario gives none."""
    if doc["doc"] not in TRANSPORT_GOODS_DOCS:
        return
    import examples_kit
    import examples_scenarios
    flow = next((v for v in vars(examples_scenarios).values()
                 if isinstance(v, examples_kit.Flow) and v.id == doc["flow"]), None)
    if flow and flow.deal:
        examples_kit.with_transport_goods(flow, shipment=content.get("Shipment"), consignment=content.get("Consignment"))


# ---------------------------------------------------------------- shipment weights (worklist C15)
def _equipment(node, out):
    """The transport equipment of a shipment, as (tare, gross) pairs: each piece once, not again where a goods item
    names its container."""
    if isinstance(node, list):
        for x in node:
            _equipment(x, out)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k == "TransportEquipment":
                for eq in v if isinstance(v, list) else [v]:
                    if isinstance(eq, dict):
                        out.append((eq.get("TareWeightMeasure"), eq.get("GrossWeightMeasure")))
            elif k not in ("GoodsItem", "GoodsItemContainer"):
                _equipment(v, out)


def shipment_weights(content, flow_id):
    """Shipment/GrossWeightMeasure includes the transport equipment by its definition, Consignment/GrossWeightMeasure
    excludes it (worklist C15). Where a document states its equipment, the shipment's weight is the goods plus the
    tares, or the equipment's gross weights, and the goods' weight is the consignment's; where it does not, the
    goods' weight stays only on the consignment or the goods item."""
    if flow_id == "waste":                     # the weighbridge weight is the loaded truck: the waste flow (D42)
        return

    def walk(node):
        if isinstance(node, list):
            for x in node:
                walk(x)
            return
        if not isinstance(node, dict):
            return
        for k, v in list(node.items()):
            if k == "Shipment" and isinstance(v, dict) and isinstance(v.get("GrossWeightMeasure"), V):
                g = v["GrossWeightMeasure"]
                cons = v.get("Consignment")
                equipment = []
                _equipment(v, equipment)
                if isinstance(cons, dict) and "GrossWeightMeasure" not in cons:
                    cons["GrossWeightMeasure"] = V(g.value, "The gross weight of the goods with their packaging, "
                                                   "without the transport equipment, as a consignment's weight is "
                                                   f"defined (worklist C15). {g.why}", **g.attrs)
                goods_item = any(isinstance(x, dict) and "GrossWeightMeasure" in x
                                 for x in (v.get("GoodsItem") if isinstance(v.get("GoodsItem"), list)
                                           else [v.get("GoodsItem")]))
                if equipment and all(isinstance(t, V) for t, _ in equipment):
                    total = Decimal(g.value) + sum(Decimal(t.value) for t, _ in equipment)
                    v["GrossWeightMeasure"] = V(f"{total:f}".rstrip("0").rstrip("."), f"The goods ({g.value} kg) and "
                                                f"the tare of the transport equipment ({' + '.join(t.value for t, _ in equipment)} "
                                                "kg): a shipment's gross weight includes the equipment (worklist C15).",
                                                **g.attrs)
                elif equipment and all(isinstance(w, V) for _, w in equipment):
                    total = sum(Decimal(w.value) for _, w in equipment)
                    v["GrossWeightMeasure"] = V(f"{total:f}".rstrip("0").rstrip("."), "The gross weights of the "
                                                f"transport equipment with the goods in it ({' + '.join(w.value for _, w in equipment)} "
                                                "kg): a shipment's gross weight includes the equipment (worklist C15).",
                                                **g.attrs)
                elif isinstance(cons, dict) or goods_item:
                    del v["GrossWeightMeasure"]
            walk(v)
    walk(content)


# ---------------------------------------------------------------- the kind of every referenced document (worklist C06)
# A reference in a generic or role-only element (AdditionalDocumentReference, DocumentReference, the supporting,
# evidence, originator … references) says what kind of document it points to, with DocumentTypeCode or
# DocumentType (decision Q29). Where it points to an example of the world, the build gives it the example's UBL
# document type; any other reference must be typed in the scenario. Elements that name the kind themselves
# (OrderReference, InvoiceDocumentReference, DespatchDocumentReference …) need no type.
GENERIC_REFERENCES = {"AdditionalDocumentReference", "DocumentReference", "SupportingDocumentReference",
                      "EvidenceDocumentReference", "OriginatorDocumentReference", "ParentDocumentReference",
                      "PreviousDocumentReference", "OriginalDocumentReference", "RequiredDocumentReference",
                      "ProvidedDocumentReference", "RequestedDocumentReference", "ShipmentDocumentReference"}
DOC_DATES = {}      # document ID -> (issue date, world document) of every example
DOC_TYPES = {}      # document ID -> (flow, file number, UBL document type) of every example of the world
DOC_TYPE = None     # the type of the document being built (its payment note names it, worklist C39)
FLOW_MODES = None   # the modes of the transport legs of the flow being built (dangerous goods data by mode, D36)
INDEXING = False    # True while doc_types() runs the scenarios to collect the IDs
UNTYPED = []        # references that are neither typed nor an example of the world: (file, element, ID)


def doc_types():
    """The ID and type of every example of the world, from the scenarios, so a reference to any of them, also
    to one of another flow or a later one, can say what kind of document it is."""
    global INDEXING
    if not DOC_TYPES:
        import examples_scenarios
        INDEXING = True                 # the scenarios run out of order here: references are not checked
        import copy
        import examples_kit
        flows = [v for v in vars(examples_scenarios).values() if isinstance(v, examples_kit.Flow)]
        saved = [copy.deepcopy(fl.__dict__) for fl in flows]    # the run must leave the flows as it found them
        for flow_id in FLOWS_WITH_EXAMPLES:
            docs = [d for d in WORLD["documents"] if d["flow"] == flow_id]
            for doc in docs:
                n = doc["nn"]
                content = examples_scenarios.SCENARIOS[flow_id](n, doc)
                if isinstance(content.get("ID"), V):
                    DOC_TYPES.setdefault(content["ID"].value, (flow_id, n, doc["doc"]))
                    if isinstance(content.get("IssueDate"), V):
                        DOC_DATES[content["ID"].value] = (content["IssueDate"].value, doc)
        for fl, state in zip(flows, saved):
            fl.__dict__.clear()
            fl.__dict__.update(state)
        INDEXING = False
    return DOC_TYPES


def type_references(content, where):
    """Give every untyped reference in a generic element the type of the example it points to (worklist C06)."""
    if isinstance(content, list):
        for x in content:
            type_references(x, where)
        return
    if not isinstance(content, dict):
        return
    for key, val in content.items():
        if key in GENERIC_REFERENCES:
            for ref in val if isinstance(val, list) else [val]:
                if not isinstance(ref, dict) or "DocumentTypeCode" in ref or "DocumentType" in ref:
                    continue
                rid = ref.get("ID").value if isinstance(ref.get("ID"), V) else None
                hit = doc_types().get(rid)
                cited = WORLD["cited"].get(rid)
                if hit:
                    ref["DocumentTypeCode"] = V(hit[2], f"The kind of document referred to: {rid} is the example "
                                                        f"{hit[0]}/{hit[1]:02d}, a {hit[2]}; a generic reference names "
                                                        "the UBL document type (decision Q29).")
                elif cited and cited.get("type_code"):
                    ref["DocumentTypeCode"] = V(cited["type_code"], f"The kind of document referred to, "
                                                f"{cited['what']}, a document outside the examples (world/documents.json, "
                                                "cited; decision Q29).")
                elif cited:
                    ref["DocumentType"] = V(cited["type"], f"The kind of document referred to, {cited['what']}, a "
                                            "document outside the examples, in words: no list has an exact code for it "
                                            "(world/documents.json, cited; decision Q29).")
                else:
                    UNTYPED.append((where, key, rid))
        if key != "Signature":                  # signatures wait for their own stage (D6)
            type_references(val, where)


DOC_UUIDS = {}      # (flow, document ID) -> the UUID the document carries, for references to it


def document_uuid(flow_id, n, doc_type):
    """The UUID of document n of a flow: version 5, derived from its place in the world, so stable."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:ubl-examples:world:{flow_id}:{n}:{doc_type}"))


def referenced_uuid(flow_id, doc_id):
    """The UUID of an earlier document of the flow, as that document states it: a reference quotes it."""
    if INDEXING:
        return "00000000-0000-0000-0000-000000000000"
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


def check_utility_statements(flow_id, roots):
    """The statements of one bill add up to it, and the tax arithmetic of a tax per unit holds (worklist C94): every
    tax subtotal per unit taxes a whole quantity (amount / rate per unit); the energy tax of an invoice is the sum
    of the energy tax its statements report, and its tiers tax exactly the quantity those statements bill on their
    consumption lines (an estimate correction's credit included, O159); a
    statement's consumption is payable at its line amount plus its taxes, and its consumption line likewise; an
    estimate correction is its unit amount times its quantity."""
    def num(e):
        return Decimal(e.text) if e is not None and e.text else None
    c, b = f"{{{NS_CAC}}}", f"{{{NS_CBC}}}"
    invoices = {r.findtext(f"{b}ID"): (name, r) for name, r in roots if etree.QName(r).localname == "Invoice"}
    for name, root in roots:
        at = f"world/examples/{flow_id}/{name}"
        for st in root.iter(f"{c}TaxSubtotal"):
            rate_, amt = num(st.find(f"{b}PerUnitAmount")), num(st.find(f"{b}TaxAmount"))
            if rate_ and amt is not None and (amt / rate_) != (amt / rate_).to_integral_value():
                raise SystemExit(f"{at}: a tax of {amt} at {rate_} per unit taxes no whole quantity")
        for corr in root.iter(f"{c}EnergyWaterConsumptionCorrection"):
            u, q, a = (num(corr.find(f"{b}{t}")) for t in ("CorrectionUnitAmount", "ConsumptionEnergyQuantity",
                                                            "CorrectionAmount"))
            if None not in (u, q, a) and u * q != a:
                raise SystemExit(f"{at}: correction {a}, but {u} x {q} is {u * q}")
        if etree.QName(root).localname != "UtilityStatement":
            continue
        for cons in root.findall(f"{c}SubscriberConsumption/{c}Consumption") + \
                root.findall(f"{c}SubscriberConsumption/{c}SupplierConsumption/{c}Consumption"):
            lmt = cons.find(f"{c}LegalMonetaryTotal")
            if lmt is None or lmt.find(f"{b}AllowanceTotalAmount") is not None or cons.find(f"{c}TaxTotal") is None:
                continue
            want = num(lmt.find(f"{b}LineExtensionAmount")) + sum(num(t.find(f"{b}TaxAmount"))
                                                                  for t in cons.findall(f"{c}TaxTotal"))
            if num(lmt.find(f"{b}PayableAmount")) != want:
                raise SystemExit(f"{at}: consumption payable {lmt.findtext(f'{b}PayableAmount')}, but its line "
                                 f"amount and taxes make {want}")
        for line in root.iter(f"{c}ConsumptionLine"):
            incl = num(line.find(f"{b}TaxInclusiveLineExtensionAmount"))
            if incl is not None and line.find(f"{c}TaxTotal") is not None and line.find(f"{c}AllowanceCharge") is None:
                want = num(line.find(f"{b}LineExtensionAmount")) + sum(num(t.find(f"{b}TaxAmount"))
                                                                       for t in line.findall(f"{c}TaxTotal"))
                if incl != want:
                    raise SystemExit(f"{at}: consumption line with tax {incl}, but its amount and taxes make {want}")
    for name, root in roots:     # the parts of each supplier add up to the invoice lines they explain (D31 p. 2)
        inv = invoices.get(root.findtext(f"{c}ParentDocumentReference/{b}ID"))
        if etree.QName(root).localname != "UtilityStatement" or inv is None:
            continue
        parts = {}
        for cl in root.iter(f"{c}ConsumptionLine"):
            k = cl.findtext(f"{b}ParentDocumentLineReferenceID")
            parts[k] = parts.get(k, Decimal(0)) + num(cl.find(f"{b}LineExtensionAmount"))
        billed = {ln.findtext(f"{b}ID"): num(ln.find(f"{b}LineExtensionAmount"))
                  for t in ("InvoiceLine", "CollectionInvoiceLine") for ln in inv[1].findall(f"{c}{t}")}
        for k, a in parts.items():
            if billed.get(k) != a:
                raise SystemExit(f"world/examples/{flow_id}/{name}: its consumption lines for line {k} of "
                                 f"{inv[0]} make {a}, the invoice line {billed.get(k)}")
    for inv_id, (name, inv) in invoices.items():
        tiers = [st for t in inv.findall(f"{c}TaxTotal") for st in t.findall(f"{c}TaxSubtotal")
                 if st.findtext(f"{c}TaxCategory/{c}TaxScheme/{b}ID") == "EXC" and st.find(f"{b}PerUnitAmount") is not None]
        if not tiers:
            continue
        stmts = [(n_, r) for n_, r in roots if etree.QName(r).localname == "UtilityStatement"
                 and r.findtext(f"{c}ParentDocumentReference/{b}ID") == inv_id]
        reported = sum(num(e) for _, r in stmts for e in r.iter(f"{b}TaxEnergyAmount"))
        metered = sum(num(cl.find(f"{b}InvoicedQuantity")) for _, r in stmts      # an estimate correction credits
                      for sc in r.findall(f"{c}SubscriberConsumption/{c}SupplierConsumption")   # its kWh on a line
                      if sc.find(f"{c}Consumption/{c}EnergyWaterSupply/{c}EnergyTaxReport") is not None  # of its own;
                      for cl in sc.iter(f"{c}ConsumptionLine"))              # the energy supplier's part (D31 p. 2)
        excise = sum(num(st.find(f"{b}TaxAmount")) for st in tiers)
        taxed = sum(num(st.find(f"{b}TaxAmount")) / num(st.find(f"{b}PerUnitAmount")) for st in tiers)
        if reported != excise:
            raise SystemExit(f"world/examples/{flow_id}/{name}: energy tax {excise}, but its statements report "
                             f"{reported}")
        if taxed != metered:
            raise SystemExit(f"world/examples/{flow_id}/{name}: the energy tax tiers tax {taxed}, but its statements "
                             f"bill {metered} with energy tax")


def check_packages(flow_id, roots):
    """Where the world lists a flow's packages piece by piece (world/documents.json, the flow's "packages": the
    cotton's bales, D12 and O26), the pieces, the totals and every document agree: the pieces' net weights sum to
    the quantity of the deal, and with the standard tare of each piece to the item's gross weight; every package
    count of the flow is the number of pieces; every goods item of the item says what package it travels in and
    gives the totals; every order or invoice line of the item has the deal's quantity; a document that lists the
    pieces lists each one once, with its net weight and its gross weight (net plus tare), and a container's gross
    weight less its tare is the pieces' gross weight."""
    import examples_scenarios
    pk = next(f for f in WORLD["flows"] if f["id"] == flow_id).get("packages")
    if not pk:
        return
    where = f"flow {flow_id} (world/documents.json packages)"
    it = ITEM[pk["item"]]
    tare = Decimal(str(pk["tare_kg"]))
    pieces = {p["id"]: Decimal(str(p["net_kg"])) for p in pk["pieces"]}
    if len(pieces) != len(pk["pieces"]):
        raise SystemExit(f"{where}: a package number is listed twice")
    count, net = len(pieces), sum(pieces.values())
    gross = net + count * tare
    deal = [d for d in examples_scenarios.FLOWS[flow_id].deal if d["item"] == pk["item"]]
    if len(deal) != 1:
        raise SystemExit(f"{where}: the deal has {len(deal)} lines of {pk['item']}, not one")
    q = Decimal(str(deal[0].get("delivered", deal[0]["ordered"])))
    if net != q:
        raise SystemExit(f"{where}: the {count} packages hold {net} {it['unit']}, but the deal is {q}")
    if net * Decimal(str(it["gross_kg"])) != gross:
        raise SystemExit(f"{where}: net {net} kg plus {count} x {tare} kg tare is {gross} kg, but the item's gross "
                         f"weight (world/items.json gross_kg) makes it {net * Decimal(str(it['gross_kg']))} kg")

    def num(e):
        return Decimal(e.text) if e is not None and e.text else None
    listed = False
    for name, root in roots:
        at = f"world/examples/{flow_id}/{name}"
        for tag in ("TotalPackagesQuantity", "TotalPackageQuantity"):
            for e in root.iter(f"{{{NS_CBC}}}{tag}"):
                if num(e) != count:
                    raise SystemExit(f"{at}: {tag} {e.text}, but the flow's goods are {count} packages")
        goods = [g for g in root.iter(f"{{{NS_CAC}}}GoodsItem")
                 if g.findtext(f"{{{NS_CBC}}}Description") == it["name"]
                 or g.findtext(f"{{{NS_CAC}}}Item/{{{NS_CBC}}}Name") == it["name"]]
        for g in goods:
            if g.findtext(f"{{{NS_CAC}}}ContainingPackage/{{{NS_CBC}}}PackagingTypeCode") != pk["type"]:
                raise SystemExit(f"{at}: the goods item of {it['name']} does not say it travels in packages of "
                                 f"type {pk['type']}")
            for tag, want in (("Quantity", net), ("GrossWeightMeasure", gross)):
                got = num(g.find(f"{{{NS_CBC}}}{tag}"))
                if got is not None and got != want:
                    raise SystemExit(f"{at}: goods item {tag} {got}, but the {count} packages make {want}")
        if goods and root.find(f".//{{{NS_CBC}}}TotalPackagesQuantity") is None:
            raise SystemExit(f"{at}: the goods of {it['name']} without their package count")
        for c in root.iter(f"{{{NS_CAC}}}Consignment"):
            got = num(c.find(f"{{{NS_CBC}}}GrossWeightMeasure"))
            if got is not None and got != gross:
                raise SystemExit(f"{at}: consignment gross weight {got}, but the {count} packages weigh {gross} kg")
        for line in root.iter(f"{{{NS_CAC}}}LineItem", f"{{{NS_CAC}}}InvoiceLine"):
            if line.findtext(f"{{{NS_CAC}}}Item/{{{NS_CAC}}}SellersItemIdentification/{{{NS_CBC}}}ID") == it["sellers_id"]:
                got = num(line.find(f"{{{NS_CBC}}}Quantity")) or num(line.find(f"{{{NS_CBC}}}InvoicedQuantity"))
                if got != net:
                    raise SystemExit(f"{at}: a line of {it['name']} for {got}, but the {count} packages hold {net}")
        listed_here = {}
        for p in root.iter(f"{{{NS_CAC}}}Package"):
            pid = p.findtext(f"{{{NS_CBC}}}ID")
            if p.findtext(f"{{{NS_CBC}}}PackagingTypeCode") != pk["type"] or pid is None:
                continue
            if pid not in pieces or pid in listed_here:
                raise SystemExit(f"{at}: package {pid} is not one of the flow's packages, or is listed twice")
            got = num(p.find(f"{{{NS_CBC}}}Quantity"))
            pg = [num(d.find(f"{{{NS_CBC}}}Measure")) for d in p.iter(f"{{{NS_CAC}}}MeasurementDimension")
                  if d.findtext(f"{{{NS_CBC}}}AttributeID") == "GROSSWEIGHT"]
            if got != pieces[pid] or pg != [pieces[pid] + tare]:
                raise SystemExit(f"{at}: package {pid} holds {got} kg and weighs {pg}, but the world gives "
                                 f"{pieces[pid]} kg net and {pieces[pid] + tare} kg gross")
            listed_here[pid] = True
        if listed_here:
            listed = True
            if len(listed_here) != count:
                raise SystemExit(f"{at}: lists {len(listed_here)} of the {count} packages")
            for eq in root.iter(f"{{{NS_CAC}}}TransportEquipment"):
                g, t = num(eq.find(f"{{{NS_CBC}}}GrossWeightMeasure")), num(eq.find(f"{{{NS_CBC}}}TareWeightMeasure"))
                if g is not None and t is not None and g - t != gross:
                    raise SystemExit(f"{at}: container {g} kg less its tare {t} kg is {g - t} kg, but the "
                                     f"{count} packages weigh {gross} kg")
    if not listed:
        raise SystemExit(f"{where}: no document of the flow lists the packages with their weights")


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


DUE_DATE_WAITS = {}   # due dates settled with a later decision


def check_payment_terms(root, where, payee_country=None):
    """O70: one terms ID means one text and one period everywhere (D23); the due dates of a document agree with each
    other, and where it cites standard or Accord terms, with the period those terms give from the issue date,
    moved to the next business day of the payee's country where it ends on none (O180)."""
    import datetime as _dt
    short = "/".join(where.split("/")[-2:])
    q = lambda e, p: [x.text for x in e.iterfind(p, {"cac": NS_CAC, "cbc": NS_CBC})]
    dues = set(q(root, "cbc:DueDate") + q(root, "cac:PaymentMeans/cbc:PaymentDueDate") +
               [d for t in root.iterfind(f"{{{NS_CAC}}}PaymentTerms") if t.find(f"{{{NS_CBC}}}InstallmentDueDate") is None
                for d in q(t, "cbc:PaymentDueDate")])
    if len(dues) > 1 and short not in DUE_DATE_WAITS:
        raise SystemExit(f"{where}: due dates {sorted(dues)} disagree (O70)")
    known = {f"{k}-STD": (c["payment"]["terms"], c["payment"]["due_days"]) for k, c in WORLD["countries"].items()}
    known.update({k: (t["terms"], t["due_days"]) for k, t in WORLD.get("payment_terms_accord", {}).items()})
    issue = root.findtext(f"{{{NS_CBC}}}IssueDate")
    for t in root.iterfind(f"{{{NS_CAC}}}PaymentTerms"):
        tid = t.findtext(f"{{{NS_CBC}}}ID")
        if tid not in known:
            continue
        text, days = known[tid]
        note = t.findtext(f"{{{NS_CBC}}}Note") or ""
        if not note.startswith(text):
            raise SystemExit(f"{where}: terms {tid} with the text {note!r}, not {text!r} (O70)")
        due = t.findtext(f"{{{NS_CBC}}}PaymentDueDate")
        if due and issue and short not in DUE_DATE_WAITS and t.find(f"{{{NS_CBC}}}InstallmentDueDate") is None:
            want = (_dt.date.fromisoformat(issue) + _dt.timedelta(days=days)).isoformat()
            while payee_country and not business_day(payee_country, want):
                want = (_dt.date.fromisoformat(want) + _dt.timedelta(days=1)).isoformat()
            if due != want:
                raise SystemExit(f"{where}: terms {tid} make it due on {want}, the document says {due} (O70)")


# ---------------------------------------------------------------- the calendar (C53, D27, O79)
def working_day(pid, day):
    """Whether party pid works on `day` (an ISO date): its working week (office, shop or every day) and, unless it
    works every day, the public holidays of its country, its state and its town."""
    import datetime as _dt
    p = PARTY[pid]
    week = WORLD["working_weeks"][p["identity"].get("week", "office")]
    d = _dt.date.fromisoformat(day)
    if d.weekday() not in week["days"]:
        return False
    if len(week["days"]) == 7:
        return True
    hol = WORLD["countries"][p["c"]].get("holidays", {})
    addr = p["identity"]["address"]
    days = dict(hol.get(str(d.year), {}))
    days.update(hol.get("states", {}).get(addr.get("CountrySubentity"), {}))
    days.update(hol.get("towns", {}).get(addr.get("CityName"), {}))
    return day not in days


def business_day(country, day):
    """Whether `day` (an ISO date) is a business day in the calendar of a country: Monday to Friday and no public
    holiday of the country (world/countries.json holidays). A payment falls due on one (O180)."""
    import datetime as _dt
    d = _dt.date.fromisoformat(day)
    return d.weekday() < 5 and day not in WORLD["countries"][country].get("holidays", {}).get(str(d.year), {})


def payee_of(root, doc):
    """The party a document's amount is paid to (O180): its payee where it names one; for a credit note the
    customer, who gets the credit back; for an invoice, a self-billed invoice, an order response or a reminder
    the supplier or seller; for any other document its issuer."""
    p = doc.get("parties", {})
    kind = etree.QName(root).localname
    if "PayeeParty" in p:
        return p["PayeeParty"]
    if kind in ("CreditNote", "SelfBilledCreditNote"):
        return p.get("AccountingCustomerParty")
    if kind in ("Invoice", "SelfBilledInvoice", "OrderResponse", "Reminder"):
        return p.get("AccountingSupplierParty") or p.get("SellerSupplierParty")
    return doc["from"]


def check_due_dates(root, doc, where):
    """O180: no stated due date falls on a weekend or a holiday of the payee's country."""
    dues = [e for e in root.iter(f"{{{NS_CBC}}}DueDate", f"{{{NS_CBC}}}PaymentDueDate",
                                 f"{{{NS_CBC}}}InstallmentDueDate") if e.text]
    payee = payee_of(root, doc) if dues else None
    if dues and payee not in PARTY:
        raise SystemExit(f"{where}: states a due date but its payee is unknown (O180)")
    for e in dues:
        country = PARTY[payee]["c"]
        if not business_day(country, e.text):
            raise SystemExit(f"{where}: {etree.QName(e.getparent()).localname}/{etree.QName(e).localname} "
                             f"{e.text} is no business day in {WORLD['countries'][country]['name']}, the payee's "
                             "country (O180)")


CALENDAR_WAITS = {   # (flow, file) -> the flow decision whose dates the document waits for (O78, stage 6)
    ('contest', '12-TendererQualification.xml'): 'D29',
    ('contest', '11-QualificationApplicationResponse.xml'): 'D29',
    ('retail', '09-DocumentStatusRequest.xml'): 'D34',
    ('retail', '10-DocumentStatus.xml'): 'D34',
    ('retail', '11-TransportExecutionPlanRequest.xml'): 'D34',
    ('retail', '19-CreditNote.xml'): 'D34',
    ('tender', '04-ExpressionOfInterestRequest.xml'): 'D28',
    ('tender', '05-ExpressionOfInterestResponse.xml'): 'D28',
    ('tender', '09-ProcurementStatus.xml'): 'D28',
    ('tender', '10-UnsubscribeFromProcedureRequest.xml'): 'D28',
    ('tender', '25-Catalogue.xml'): 'D28',
    ('tender', '33-CreditNote.xml'): 'D28',
    ('carnet', '03-ProofOfReexportationReminder.xml'): 'D40',
    ('utilities', '04-RemittanceAdvice.xml'): 'D31',
    ('utilities', '07-RemittanceAdvice.xml'): 'D31',
    ('utilities', '14-RemittanceAdvice.xml'): 'D31',
    ('plastics', '05-ExportCustomsDeclaration.xml'): 'D41',
    ('plastics', '08-DespatchAdvice.xml'): 'D41',
    ('contest', '08-ContractNotice.xml'): 'D29',
    ('contest', '09-CallForTenders.xml'): 'D29',
    ('contest', '10-QualificationApplicationRequest.xml'): 'D29',
    ('contest', '14-BusinessInformation.xml'): 'D29',
    ('contest', '16-ContractAwardNotice.xml'): 'D29',
}


def check_calendar(flow_id, roots, docs):
    """O79: a document is dated on a day its issuer works, unless it waits for its flow's dates (CALENDAR_WAITS)."""
    for (name, root), doc in zip(roots, docs):
        day = root.findtext(f"{{{NS_CBC}}}IssueDate")
        if day and doc["from"] in PARTY and not working_day(doc["from"], day) and \
                (flow_id, name) not in CALENDAR_WAITS:
            raise SystemExit(f"world/examples/{flow_id}/{name}: issued on {day}, a day its issuer "
                             f"{PARTY[doc['from']]['identity']['name']} does not work (D27, O79)")


def issue_time_offset(content, doc):
    """The issue time is the issuer's local time, written with its offset from UTC (D27)."""
    t = content.get("IssueTime")
    if isinstance(t, V) and re.fullmatch(r"\d\d:\d\d:\d\d", str(t.value)):
        tz = WORLD["countries"][PARTY[doc["from"]]["c"]]["timezone"]
        content["IssueTime"] = V(f"{t.value}{tz}", f"{t.why.rstrip('.')}; in the issuer's local time, with its "
                                                   "offset from UTC (D27).", **t.attrs)


# ---------------------------------------------------------------- issue times follow what a document reports (C72)
ISSUED = {}            # document ID -> [(flow, file, issue moment)] of every example built so far in this run
CITED_LATER = {}       # document ID -> [(moment, where)] of documents that cite it before it was built
# Documents that still report or cite something after their issue, each waiting for its flow decision (stage 6):
# (flow, file) -> the reason. Each entry goes when its flow is implemented.
ISSUE_ORDER_WAITS = {
}


def moment(day, time, offset):
    """An issue or event moment: (date, aware datetime or None). A time without offset is in the given offset,
    the issuer's local time (D27)."""
    if not day:
        return None
    d = datetime.date.fromisoformat(day[:10])
    if not time:
        return (d, None)
    m = re.fullmatch(r"(\d\d:\d\d:\d\d)(Z|[+-]\d\d:\d\d)?", time)
    off = {"Z": "+00:00", None: offset}.get(m.group(2), m.group(2))
    return (d, datetime.datetime.fromisoformat(f"{d.isoformat()}T{m.group(1)}{off}"))


def is_after(a, b):
    """Whether moment a lies after moment b: by the clock where both have a time, else by the day."""
    if a[1] is not None and b[1] is not None:
        return a[1] > b[1]
    return a[0] > b[0]


def issue_moment(root, doc):
    tz = WORLD["countries"][PARTY[doc["from"]]["c"]]["timezone"]
    return moment(root.findtext(f"{{{NS_CBC}}}IssueDate"), root.findtext(f"{{{NS_CBC}}}IssueTime"), tz)


def reported_facts(root, tz):
    """What a document states as done, each with its moment: actual events and dates, receipts and payments,
    verified signatures, revisions, comments made and exchange rates established (C72). Events not completed
    (CompletionIndicator false) are left out."""
    out = []
    for e in root.iter(f"{{{NS_CBC}}}*"):
        name, parent = etree.QName(e).localname, e.getparent()
        pname = etree.QName(parent).localname
        if name == "OccurrenceDate" and pname.startswith("Actual"):
            if parent.findtext(f"{{{NS_CBC}}}CompletionIndicator") == "false":
                continue
            out.append((f"{pname}/{name}", moment(e.text, parent.findtext(f"{{{NS_CBC}}}OccurrenceTime"), tz)))
        elif re.fullmatch(r"(Actual\w*|Paid|Received|Validation|Revision|Response)Date", name) and \
                (parent is not root or name in ("RevisionDate", "ResponseDate")):
            out.append((f"{pname}/{name}", moment(e.text, parent.findtext(f"{{{NS_CBC}}}{name[:-4]}Time"), tz)))
        elif name == "RevisionDate" and parent is root:
            out.append((name, moment(e.text, root.findtext(f"{{{NS_CBC}}}RevisionTime"), tz)))
        elif name == "IssueDate" and pname == "EventComment":
            out.append((f"{pname}/{name}", moment(e.text, parent.findtext(f"{{{NS_CBC}}}IssueTime"), tz)))
        elif name == "Date" and pname == "ExchangeRate":
            out.append((f"{pname}/{name}", moment(e.text, None, tz)))
    return out


def cited_examples(root, flow_id, name):
    """The examples a document cites by their document ID: (element, cited ID, [(flow, file, moment)])."""
    own = root.findtext(f"{{{NS_CBC}}}ID")
    for e in root.iter(f"{{{NS_CBC}}}*"):
        if e.getparent() is root and etree.QName(e).localname == "ID":
            continue
        if etree.QName(e).localname.endswith("ID") and e.text and e.text != own and e.text in ISSUED:
            yield etree.QName(e.getparent()).localname + "/" + etree.QName(e).localname, e.text, \
                [x for x in ISSUED[e.text] if (x[0], x[1]) != (flow_id, name)]


ANSWERS = {"Quotation": {"RequestForQuotation"}, "Catalogue": {"CatalogueRequest"}}


def answered_request(doc, earlier):
    """The request a document answers: the last earlier document of the flow, sent the other way between the same
    two parties, whose type asks for this one (DocumentStatusRequest -> DocumentStatus, Order -> OrderResponse,
    TransportExecutionPlanRequest -> TransportExecutionPlan ...). earlier: [(world document, root)]."""
    t = doc["doc"]
    asks = {t + "Request"} | ANSWERS.get(t, set())
    if t.endswith("Response"):
        asks |= {t[:-8], t[:-8] + "Request"}
    hits = [(d, r) for d, r in earlier if d["doc"] in asks and (d["from"], d["to"]) == (doc["to"], doc["from"])]
    return hits[-1] if hits else None


def issue_floor(root, doc, flow_id, name, request=None):
    """The latest moment on the document's issue day that it reports or cites, or the request it answers: its issue
    time must follow it."""
    tz = WORLD["countries"][PARTY[doc["from"]]["c"]]["timezone"]
    day = issue_moment(root, doc)[0]
    times = [m[1] for _, m in reported_facts(root, tz) if m and m[0] == day and m[1] is not None]
    if request is not None and request[0] == day and request[1] is not None:
        times.append(request[1])
    for _, _, hits in cited_examples(root, flow_id, name):
        if hits and all(h[2][0] == day and h[2][1] is not None for h in hits):
            times.append(min(h[2][1] for h in hits))
    return max(times) if times else None


def issue_ceiling(doc_id, day):
    """The earliest moment on the issue day at which an example built before this one cites it."""
    times = [m[1] for m, _ in CITED_LATER.get(doc_id, []) if m[0] == day and m[1] is not None]
    return min(times) if times else None


def derived_issue_time(header, root, doc, flow_id, name, doc_id, request=None):
    """The issue time of a document whose scenario gives none (C72): the sender's system issues it a few minutes
    after the last thing on its issue day that it reports or cites, or the request it answers, and before the
    documents that cite it."""
    tz = WORLD["countries"][PARTY[doc["from"]]["c"]]["timezone"]
    own = issue_moment(root, doc)
    floor, ceiling = issue_floor(root, doc, flow_id, name, request), issue_ceiling(doc_id, own[0])
    gap = datetime.timedelta(minutes=4 + zlib.crc32(f"{flow_id}:{name}".encode()) % 17)
    if floor is not None and not own[1] > floor:
        t, why = floor + gap, ("Issued a few minutes after the last thing of its day that it reports, cites or "
                               "answers, in the sender's local time (C72).")
    elif ceiling is not None and not own[1] < ceiling:
        t, why = ceiling - gap, ("Issued a few minutes before the document that cites it, in the sender's local "
                                 "time (C72).")
    else:
        return False
    local = t.astimezone(datetime.timezone(datetime.timedelta(hours=int(tz[:3]), minutes=int(tz[0] + tz[4:]))))
    if local.date() != own[0]:
        raise SystemExit(f"world/examples/{flow_id}/{name}: no issue time on {own[0]} fits what the document "
                         "reports or cites, and the documents that cite it (C72): give its day in the scenario")
    header["IssueTime"] = V(local.strftime("%H:%M:%S"), why)
    return True


def check_issue_order(flow_id, name, root, doc, request=None):
    """C72: no document reports as done, or cites as existing, anything after its own issue, and none answers a
    request issued after it."""
    if (flow_id, name) in ISSUE_ORDER_WAITS:
        return
    own = issue_moment(root, doc)
    if own is None:
        return
    if request is not None and is_after(request, own):
        raise SystemExit(f"world/examples/{flow_id}/{name}: issued {own[1] or own[0]}, before the request it answers, "
                         f"issued {request[1] or request[0]} (C72)")
    tz = WORLD["countries"][PARTY[doc["from"]]["c"]]["timezone"]
    for what, m in reported_facts(root, tz):
        if m and is_after(m, own):
            raise SystemExit(f"world/examples/{flow_id}/{name}: {what} {m[1] or m[0]} lies after the document's "
                             f"issue {own[1] or own[0]} (C72)")
    for what, rid, hits in cited_examples(root, flow_id, name):
        if hits and all(is_after(h[2], own) for h in hits if h[2]):
            h = hits[0]
            raise SystemExit(f"world/examples/{flow_id}/{name}: {what} cites {rid}, the example {h[0]}/{h[1]} "
                             f"issued {h[2][1] or h[2][0]}, after this document's issue {own[1] or own[0]} (C72)")


# ---------------------------------------------------------------- references resolve (C73)
UNRESOLVED = []        # references to a kind of document the examples have, under an ID no example has: (file, el, ID)
# References to documents the flow decisions add (D38), each waiting for its flow (stage 6): ID -> the document.
REFERENCE_WAITS = {"PWD-RCPT-BF-1": "tender/40, the department's receipt of Brackenmere's first tender (D38, with "
                                    "D28)"}
REFERENCE_ALIASES = {"CallForTender": "CallForTenders", "Despatch": "DespatchAdvice", "Receipt": "ReceiptAdvice",
                     "Remittance": "RemittanceAdvice", "TenderNotification": "TenderReceipt",
                     "Notice": "ContractNotice"}


def reference_kind(name):
    """The kind of document a specific reference element names (OrderReference -> Order, StatementDocumentReference
    -> Statement, RequestedCatalogueReference -> Catalogue ...), when the examples have documents of that kind."""
    base = re.sub(r"(Document)?Reference$", "", name)
    base = re.sub(r"^(Requested|Source|Related|Deleted|Replaced)(?=[A-Z])", "", base)
    base = REFERENCE_ALIASES.get(base, base)
    return base if base in {d["doc"] for d in WORLD["documents"]} else None


def check_reference_targets(root, where):
    """C73: a reference to a kind of document the examples have resolves to an example, or is declared a document
    outside the examples (world/documents.json, cited), or waits for the document its flow adds (REFERENCE_WAITS)."""
    for e in root.iter(f"{{{NS_CAC}}}*"):
        name = etree.QName(e).localname
        rid = e.findtext(f"{{{NS_CBC}}}ID")
        if not name.endswith("Reference") or rid is None or not reference_kind(name):
            continue
        if rid not in doc_types() and rid not in WORLD["cited"] and rid not in REFERENCE_WAITS:
            UNRESOLVED.append((where, name, rid))


PARTY_SAYS = {}        # pid -> {"self": element paths it gives about itself, "other": paths others give about it}


def check_party_profiles(flow_id, roots, docs):
    """The party table at work (C01, O90): a customs trader number only in a customs document or a cross-border
    transport document; share capital only in its issuer's own invoice-kind document, and only where the issuer's
    company law asks for it; and what each document says about each party is gathered for the check across flows."""
    by_reg = {p["identity"].get("registry_id"): pid for pid, p in PARTY.items() if p["identity"].get("registry_id")}
    for (name, root), doc in zip(roots, docs):
        cls, where = DOC_CLASS[doc["doc"]], f"world/examples/{flow_id}/{name}"
        for e in root.iter():
            if not isinstance(e.tag, str):
                continue
            pid = by_reg.get(e.findtext(f"{{{NS_CAC}}}PartyIdentification/{{{NS_CBC}}}ID"))
            if not pid or e.find(f"{{{NS_CAC}}}PartyName") is None:
                continue
            for x in e.iterfind(f"{{{NS_CAC}}}AdditionalPartyIdentification/{{{NS_CBC}}}ID"):
                if "customs-trader" in x.get("schemeID", "") and not (
                        cls == "customs" or (cls == "transport" and _cross_border(doc))):
                    raise SystemExit(f"{where}: customs trader number of {pid} outside a customs or cross-border "
                                     "transport document (C01)")
            if e.find(f"{{{NS_CAC}}}PartyLegalEntity/{{{NS_CBC}}}CorporateStockAmount") is not None and not (
                    cls == "invoice" and pid == doc["from"] and capital_on_documents(pid)):
                raise SystemExit(f"{where}: share capital of {pid} outside its own invoice, or not asked for by its "
                                 "company law (C01, O147)")
            said = set()
            for d in e.iter():                          # every leaf value, by its path below the party
                if not isinstance(d.tag, str) or len(d) or d.text is None:
                    continue
                steps, x = [], d
                while x is not e:
                    name = etree.QName(x).localname
                    if name == "PartyTaxScheme":       # a party may be registered for several taxes: per scheme
                        name += "[" + (x.findtext(f"{{{NS_CAC}}}TaxScheme/{{{NS_CBC}}}ID") or "") + "]"
                    steps.append(name)
                    x = x.getparent()
                if "Contact" in steps:                  # the desk differs with the role (C02)
                    continue
                said.add(("/".join(reversed(steps)) + "@" + d.get("schemeID", ""), d.text))
            side = "self" if pid == doc["from"] else "other"
            PARTY_SAYS.setdefault(pid, {"self": set(), "other": set()})[side] |= said


def check_party_knowledge():
    """O90: what one party says about another may be less than what that party says about itself, but never
    contradicts it: wherever both give a value at the same place (the same element below the party, with the same
    scheme), the other's value is one the party gives itself. Contacts are left out: the desk follows the role."""
    out = []
    for pid, said in sorted(PARTY_SAYS.items()):
        own = {}
        for path, value in said["self"]:
            own.setdefault(path, set()).add(value)
        for path, value in sorted(said["other"]):
            if path in own and value not in own[path]:
                out.append(f"{pid}: another document gives {path} = {value!r}, the party itself {sorted(own[path])}")
    return out

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
    global DOC_TYPE, FLOW_MODES
    FLOW_MODES = {leg["mode"] for leg in flow.get("legs", [])}
    for doc in docs:
        n = doc["nn"]               # the example number in the flow, removed numbers left out (D28)
        DOC_TYPE = doc["doc"]
        content = scenario(n, doc)
        global CONTENT
        CONTENT = content
        content = place_parties(doc, content)
        item_profiles(content, doc)
        redundant_roles(content, doc)
        untaxed_sales(content, doc)
        declaration_invoices(content, doc)
        customs_values(content, doc)
        import_preference(content, doc)
        origin_notes(content)
        border_transport(content, doc)
        type_references(content, f"{flow_id}/{xmlname(n, doc)}")
        requested_delivery(content, doc, n)
        catalogue_items(content, doc)
        currency_cleanup(content, doc)
        national_tariffs(content, doc)
        tax_arithmetic(content, f"{flow_id} {n} {doc['doc']}")
        transport_goods(content, doc)
        identify_places(content)
        shipment_weights(content, flow_id)
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
        global SENDER, INTERNATIONAL
        SENDER, INTERNATIONAL = doc["from"], international(doc)
        full = merge(header, content)
        issue_time_offset(full, doc)
        root, reasons = build(doc["doc"], full)
        doc_id = content["ID"].value if isinstance(content.get("ID"), V) else None
        asked = answered_request(doc, list(zip(docs, [r for _, r in roots])))
        asked = issue_moment(asked[1], asked[0]) if asked else None
        if "IssueTime" in header and derived_issue_time(header, root, doc, flow_id, xmlname(n, doc), doc_id, asked):
            full = merge(header, content)          # the issue time follows what the document reports (C72)
            issue_time_offset(full, doc)
            root, reasons = build(doc["doc"], full)
        set_ubl_version(root, reasons)
        here = issue_moment(root, doc)
        if doc_id and here:
            for m, where in CITED_LATER.get(doc_id, []):
                if is_after(here, m):
                    raise SystemExit(f"world/examples/{flow_id}/{xmlname(n, doc)}: issued {here[1] or here[0]}, after "
                                     f"{where}, which cites it at {m[1] or m[0]} (C72)")
            ISSUED.setdefault(doc_id, []).append((flow_id, xmlname(n, doc), here))
        check_issue_order(flow_id, xmlname(n, doc), root, doc, asked)
        check_reference_targets(root, f"{flow_id}/{xmlname(n, doc)}")
        if here and (flow_id, xmlname(n, doc)) not in ISSUE_ORDER_WAITS:
            for e in root.iter(f"{{{NS_CBC}}}*"):        # citations of examples not built yet: checked when they are
                if etree.QName(e).localname.endswith("ID") and e.text and e.text != doc_id and \
                        e.text in doc_types() and e.text not in ISSUED:
                    CITED_LATER.setdefault(e.text, []).append((here, f"{flow_id}/{xmlname(n, doc)}"))
        check_specifications(root, f"world/examples/{flow_id}/{xmlname(n, doc)}")
        if "UUID" in header and isinstance(content.get("ID"), V):
            DOC_UUIDS[(flow_id, content["ID"].value)] = header["UUID"].value
        roots.append((xmlname(n, doc), root))
        for e in root.iter():                  # every transport event says where, and what if generic (C18)
            if isinstance(e.tag, str) and etree.QName(e).localname.endswith("TransportEvent"):
                if e.find(f"{{{NS_CAC}}}Location") is None:
                    raise SystemExit(f"{flow_id} {n} {doc['doc']}: {etree.QName(e).localname} without a place "
                                     "(worklist C18)")
                if etree.QName(e).localname == "TransportEvent" and e.find(f"{{{NS_CBC}}}TransportEventTypeCode") is None:
                    raise SystemExit(f"{flow_id} {n} {doc['doc']}: TransportEvent without a type code (worklist C18)")
        for e in root.iter():                  # a status that only says there is none is a filler (worklist C16)
            if isinstance(e.tag, str) and e.text == "NoStatus":
                raise SystemExit(f"{flow_id} {n} {doc['doc']}: {etree.QName(e).localname} NoStatus states nothing "
                                 "(UBL IND5/IND6)")
        check_addresses(root, f"{flow_id} {n} {doc['doc']}")
        check_payment_means(root, f"{flow_id} {n} {doc['doc']}")
        check_dangerous_goods(root, f"{flow_id} {n} {doc['doc']}")
        check_classifications(root, f"{flow_id} {n} {doc['doc']}")
        check_formats(root, f"{flow_id} {n} {doc['doc']}")
        check_schemes(root, f"{flow_id} {n} {doc['doc']}")
        check_tax_exemption_lists(root, f"{flow_id} {n} {doc['doc']}", doc)
        check_instance_rules(root, f"world/examples/{flow_id}/{xmlname(n, doc)}")
        check_payment_terms(root, f"world/examples/{flow_id}/{xmlname(n, doc)}",
                            PARTY.get(payee_of(root, doc), {}).get("c"))
        check_due_dates(root, doc, f"world/examples/{flow_id}/{xmlname(n, doc)}")
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
    check_party_profiles(flow_id, roots, docs)
    check_calendar(flow_id, roots, docs)
    check_unit_ids(flow_id, roots)
    check_packages(flow_id, roots)
    check_utility_statements(flow_id, roots)
    produced = {xmlname(d["nn"], d) for d in docs} | {xmlname(d["nn"], d).replace(".xml", ".md") for d in docs}
    for name in sorted(os.listdir(out)):                 # files of documents that are no longer in the flow
        if name not in produced and ".llm-review." not in name:   # reviews are not generated: keep them
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
    if not args:
        for problem in build_examples.check_party_knowledge():
            print(f"party table (O90): {problem}", file=sys.stderr)
            ok = False
    for note in world_items.NOTES:         # HS 2022 subheadings the HS 2017 -> CPC table does not have
        print(f"note: {note}", file=sys.stderr)
    if build_examples.UNTYPED:
        print(f"references without a document type that point to no example and are not in world/documents.json "
              f"cited ({len(build_examples.UNTYPED)}):",
              "; ".join(f"{w} {e} {i}" for w, e, i in build_examples.UNTYPED), file=sys.stderr)
        ok = False
    if build_examples.UNRESOLVED:
        print(f"references to a kind of document the examples have, under an ID no example has and not in "
              f"world/documents.json cited (C73, {len(build_examples.UNRESOLVED)}):",
              "; ".join(f"{w} {e} {i}" for w, e, i in build_examples.UNRESOLVED), file=sys.stderr)
        ok = False
    if build_examples.UNBOUND:
        print(f"code elements without a code list in world/codelists/lists.json ({len(build_examples.UNBOUND)}):",
              ", ".join(f"{e} in {p}" for e, p in sorted(build_examples.UNBOUND)), file=sys.stderr)
    if build_examples.MISSING_WORDS:
        print("words missing from the vocabularies of the world's languages (world/countries.json; save the list as missing.json and run python3 tools/lexicon.py missing.json qau|qal):",
              json.dumps(sorted(build_examples.MISSING_WORDS)), file=sys.stderr)
        ok = False
    sys.exit(0 if ok else 1)
