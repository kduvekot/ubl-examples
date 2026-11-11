#!/usr/bin/env python3
"""Extract what the example world needs from the UBL 2.5 semantic model.

Reads the UBL 2.5 entity model (mod/UBL-Entities-2.5.gc, the source of the
schemas) and writes world/ubl-model.json:

  * every aggregate (ABIE) with its basic properties (name, cardinality) and its associations
    (ASBIEs: name, target aggregate, cardinality, definition), so that a
    path such as Order/Delivery/Despatch/DespatchParty can be checked;
  * which aggregates, associations and basic properties are deprecated (their
    definition starts with "(Deprecated)", or, for a document type, it has no
    endorsed schema: the endorsed schemas leave out everything deprecated);
    the world uses none of them;
  * which basic properties are of a text type (data type Text or Name, the
    two whose schema types derive from udt:TextType and so carry languageID),
    for the UBL instance rules IND7 and IND8 that the build checks;
  * per document type: its definition, its document-level party elements,
    and which of these elements sends the document and which receives it.

Who sends and who receives comes from the model where it says so: the
SenderParty and ReceiverParty elements, or a definition of the document or
of a party element ("The Party who submits this Tender"). Where the model
does not say it, the party role table of the UBL specification
(UBL-Party-summary-information.xml) is used, and where neither says it the
choice is marked "inferred" with the definitions it rests on. Every quote in
the table below is checked word for word against its source.

Usage: python3 tools/extract_ubl_model.py
"""
import hashlib
import json
import os
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

MODEL = "https://docs.oasis-open.org/ubl/os-UBL-2.5/mod/UBL-Entities-2.5.gc"
MODEL_SHA256 = "c7df070e1a2927792a8a85103665924973d2559552ea87aa495ea7248fe988d1"
# oasis-tcs/ubl branch ubl-2.5-os; the role table last changed on 2025-08-06
ROLES = ("https://raw.githubusercontent.com/oasis-tcs/ubl/345386aa0504488aebdbec1c7d629ce9b7d08826/"
         "UBL-Party-summary-information.xml")
DEPRECATED = "(Deprecated)"   # how the model marks what is no longer endorsed
ENDORSED = "https://docs.oasis-open.org/ubl/os-UBL-2.5/endorsed/xsdrt/maindoc/"
OUT = os.path.join(os.path.dirname(__file__), "..", "world", "ubl-model.json")

# Documents without SenderParty and ReceiverParty: (senders, receivers, basis, evidence).
# basis "document": the quote is from the definition of the document;
#       "element":  the quotes are from definitions of the party elements;
#       "role table": the quote names a role, and the role table lists the
#                   document under that role's "sends" (first) and "receives" (second);
#       "inferred": neither says it; the quotes are the definitions it rests on.
# A sender or receiver may be a deeper path; an empty list means the document
# does not name that party.
DIRECTION = {
    "BillOfLading": (["CarrierParty"], ["ConsignorParty", "FreightForwarderParty"], "document",
                     ["A document issued by the party who acts as an agent for a transportation carrier or other "
                      "agents to the party who gives instructions for the transportation services (shipper, consignor, etc.)"]),
    "CallForTenders": (["ContractingParty"], ["ReceiverParty"], "document",
                       ["A document used by a Contracting Party to define a procurement project"]),
    "Catalogue": (["ProviderParty"], ["ReceiverParty"], "element",
                  ["The Party who provides this Catalogue.", "The Party who receives this Catalogue."]),
    "CatalogueDeletion": (["ProviderParty"], ["ReceiverParty"], "element",
                          ["The Party who sends the Catalogue Deletion.", "The Party who receives the Catalogue Deletion."]),
    "CatalogueItemSpecificationUpdate": (["ProviderParty"], ["ReceiverParty"], "element",
                                         ["The Party who sends the Catalogue Item Specification Update.",
                                          "The Party who receives the Catalogue Item Specification Update."]),
    "CataloguePricingUpdate": (["ProviderParty"], ["ReceiverParty"], "element",
                               ["The Party who sends the Catalogue Pricing Update.",
                                "The Party who receives the Catalogue Pricing Update."]),
    "CatalogueRequest": (["ProviderParty"], ["ReceiverParty"], "element",
                         ["The Party who sends the Catalogue Request.", "The Party who receives the Catalogue Request."]),
    "CertificateOfOrigin": (["ExporterParty", "EndorserParty"], ["EndorserParty", "ImporterParty"], "role table",
                            ["Exporter", "Endorser", "Importer"]),
    "ContractAwardNotice": (["ContractingParty"], ["ReceiverParty"], "document",
                            ["A document published by a Contracting Party to announce the awarding of a procurement project."]),
    "ContractNotice": (["ContractingParty"], ["ReceiverParty"], "document",
                       ["A document used by a Contracting party to announce a project"]),
    "PriorInformationNotice": (["ContractingParty"], ["ReceiverParty"], "document",
                               ["A document used by a contracting party to declare the intention to buy"]),
    "CreditNote": (["AccountingSupplierParty"], ["AccountingCustomerParty"], "role table",
                   ["Accounting Supplier", "Accounting Customer"]),
    "DebitNote": (["AccountingCustomerParty"], ["AccountingSupplierParty"], "role table",
                  ["Accounting Customer", "Accounting Supplier"]),
    "DeliveryNote": (["DespatchSupplierParty"], ["DeliveryCustomerParty"], "inferred",
                     ["The Party that executed the delivery.", "The Party to whom the goods or services were delivered."]),
    "DespatchAdvice": (["DespatchSupplierParty"], ["DeliveryCustomerParty"], "role table", ["Despatch", "Delivery"]),
    "DigitalAgreement": (["ParticipantParty"], ["ParticipantParty"], "role table", ["Participant"]),
    "Enquiry": (["RequestorParty"], ["ResponderParty"], "document",
                ["A document sent by a requestor to a responder"]),
    "EnquiryResponse": (["ResponderParty"], ["RequestorParty"], "document",
                        ["A document sent by a responder to a requester"]),
    "ExportCustomsDeclaration": (["ExporterParty"], ["CustomsDeclaration/CustomsParty"], "role table",
                                 ["Exporter", "Exporting Customs"]),
    "ExpressionOfInterestRequest": (["EconomicOperatorParty"], ["ContractingParty"], "document",
                                    ["issuing an Expression Of Interest document to the contracting party"]),
    "ExpressionOfInterestResponse": (["ContractingParty"], ["EconomicOperatorParty"], "document",
                                     ["An expression of interest confirmation issued by a Contracting Party"]),
    "ForwardingInstructions": (["ConsignorParty", "FreightForwarderParty"], ["FreightForwarderParty", "CarrierParty"],
                               "document",
                               ["The parties who issue this document are commonly referred to as the shipper or consignor, "
                                "while the parties who receive this document are forwarders, carriers, shipping agents, etc."]),
    "FreightInvoice": (["AccountingSupplierParty"], ["AccountingCustomerParty"], "inferred",
                       ["A document stating the charges incurred for a logistics service.",
                        "The accounting supplier party.", "The accounting customer party."]),
    "FulfilmentCancellation": (["SellerSupplierParty", "BuyerCustomerParty"], ["BuyerCustomerParty", "SellerSupplierParty"],
                               "role table", ["Seller", "Buyer"]),
    "GoodsCertificate": (["IssuerParty"], ["ApplicantParty"], "element",
                         ["The Party who issues this Goods Certificate.", "The Party who applies for this Goods Certificate."]),
    "GoodsItemPassport": (["IssuerParty"], ["HolderParty"], "element",
                          ["The Party who issues this Goods Item Passport.",
                           "The Party who holds the Goods Item Passport."]),
    "GuaranteeCertificate": (["GuarantorParty"], ["BeneficiaryParty", "InterestedParty"], "inferred",
                             ["A document to notify the deposit of a Guarantee, such as a bid bond.",
                              "The guarantee creditor organisation who has the authority to charge bid bond guarantee credit.",
                              "The recipient who benefits from the bid bond guarantee."]),
    "ImportCustomsDeclaration": (["ImporterParty"], ["CustomsParty"], "role table", ["Importer"]),
    "InstructionForReturns": (["SellerSupplierParty"], ["RetailerCustomerParty"], "document",
                              ["The producer is requesting the return of products"]),
    "InventoryReport": (["RetailerCustomerParty"], ["SellerSupplierParty"], "document",
                        ["This document is sent by a Buyer (for example a retailer) to a Seller (for example a producer)."]),
    "Invoice": (["AccountingSupplierParty"], ["AccountingCustomerParty"], "role table",
                ["Accounting Supplier", "Accounting Customer"]),
    "Manifest": (["SendingLogisticsOperatorParty"], ["AuthorityParty"], "element",
                 ["The Party who issues this Manifest.", "The Authority or regulator who receives this Manifest."]),
    "Order": (["BuyerCustomerParty"], ["SellerSupplierParty"], "role table", ["Buyer", "Seller"]),
    "OrderCancellation": (["BuyerCustomerParty"], ["SellerSupplierParty"], "role table", ["Buyer", "Seller"]),
    "OrderChange": (["BuyerCustomerParty"], ["SellerSupplierParty"], "role table", ["Buyer", "Seller"]),
    "OrderResponse": (["SellerSupplierParty"], ["BuyerCustomerParty"], "role table", ["Seller", "Buyer"]),
    "OrderResponseSimple": (["SellerSupplierParty"], ["BuyerCustomerParty"], "role table", ["Seller"]),
    "PackingList": (["ConsignorParty"], ["FreightForwarderParty"], "role table", ["Consignor", "Freight Forwarder"]),
    "ProcurementStatus": (["ContractingParty"], ["EconomicOperatorParty"], "document",
                          ["A document sent by a Contracting Party to an Economic Operator"]),
    "ProcurementStatusRequest": (["EconomicOperatorParty"], ["ContractingParty"], "document",
                                 ["A document sent by an Economic Operator to a Contracting Party"]),
    "ProofOfReexportation": (["ExportingGuarantorParty"], ["ImportingGuarantorParty"], "role table",
                             ["Exporting Guarantor", "Importing Guarantor"]),
    "ProofOfReexportationReminder": (["ImportingGuarantorParty"], ["ExportingGuarantorParty"], "element",
                                     ["The Party who on behalf of their Customs Authority issues this Document.",
                                      "The Party who is fiscally responsible for the Goods Item Passport counterfoils"]),
    "ProofOfReexportationRequest": (["ImportingGuarantorParty"], ["ExportingGuarantorParty"], "role table",
                                    ["Importing Guarantor", "Exporting Guarantor"]),
    "PurchaseReceipt": (["AccountingSupplierParty"], ["AccountingCustomerParty"], "inferred",
                        ["A receipt for a purchase made with cash or cash equivalents.",
                         "The accounting supplier party.", "The accounting customer party."]),
    "QualificationApplicationRequest": (["ContractingParty"], ["EconomicOperatorParty"], "element",
                                        ["The Economic Operator receiving the Qualification Application Resquest."]),
    "QualificationApplicationResponse": (["EconomicOperatorParty"], ["ContractingParty"], "element",
                                         ["The Economic Operator issuing the Qualification Application Response."]),
    "Quotation": (["SellerSupplierParty"], ["OriginatorCustomerParty", "BuyerCustomerParty"], "role table",
                  ["Seller", "Originator"]),
    "ReceiptAdvice": (["DeliveryCustomerParty"], ["DespatchSupplierParty"], "role table", ["Delivery", "Despatch"]),
    "Reminder": (["AccountingSupplierParty"], ["AccountingCustomerParty"], "document",
                 ["A document used to remind a customer of payments past due."]),
    "RemittanceAdvice": (["AccountingCustomerParty"], ["AccountingSupplierParty", "PayeeParty"], "role table",
                         ["Accounting Customer", "Accounting Supplier", "Payee"]),
    "RequestForQuotation": (["OriginatorCustomerParty", "BuyerCustomerParty"], ["SellerSupplierParty"], "role table",
                            ["Originator", "Seller"]),
    "SelfBilledCreditNote": (["AccountingCustomerParty"], ["AccountingSupplierParty"], "role table",
                             ["Accounting Customer", "Accounting Supplier"]),
    "SelfBilledInvoice": (["AccountingCustomerParty"], ["AccountingSupplierParty"], "role table",
                          ["Accounting Customer", "Accounting Supplier"]),
    "Statement": (["AccountingSupplierParty"], ["AccountingCustomerParty"], "role table",
                  ["Accounting Supplier", "Accounting Customer"]),
    "StockAvailabilityReport": (["SellerSupplierParty"], ["RetailerCustomerParty"], "document",
                                ["This document is sent by a Seller (for example a producer) to a Buyer (for example a retailer)."]),
    "Tender": (["TendererParty"], ["ContractingParty"], "element",
               ["The Party who submits this Tender.", "The contracting party."]),
    "TenderContract": (["ContractingParty"], ["EconomicOperatorParty", "ReceiverParty"], "role table",
                       ["Contracting Authority", "Tenderer"]),
    "TenderStatus": (["ContractingParty"], ["EconomicOperatorParty"], "document",
                     ["A document sent by the Contracting Party to an Economic Operator"]),
    "TenderStatusRequest": (["EconomicOperatorParty"], ["ContractingParty"], "element",
                            ["The Economic Operator issuing the inquiry on the status of a tendering process.",
                             "The Contracting Party eceiving the tender status inquiry."]),
    "TenderWithdrawal": (["TendererParty"], ["ContractingParty"], "document",
                         ["A document sent by an Economic Operator to a Contracting Party"]),
    "TendererQualification": (["TendererPartyQualification/MainQualifyingParty"], ["ContractingParty"], "inferred",
                              ["A document declaring the qualifications of a tenderer.", "The contracting party."]),
    "TransitCustomsDeclaration": (["TransitExporterParty"], ["CustomsParty"], "element",
                                  ["The Party who makes the Transit Customs Declaration",
                                   "The Authority who is legally responsible for processing the Declaration."]),
    "UnsubscribeFromProcedureRequest": (["EconomicOperatorParty"], ["ContractingParty"], "element",
                                        ["The Economic Operator issuing this unsubscribe request."]),
    "UnsubscribeFromProcedureResponse": (["ContractingParty"], ["EconomicOperatorParty"], "document",
                                         ["A document sent from a Contracting Party to the Economic Operator"]),
    "WorkReport": (["SellerSupplierParty"], ["BuyerCustomerParty"], "inferred",
                   ["A document used to report work performed.", "The party providing the work."]),
}


def camel(name):
    return "".join(w[:1].upper() + w[1:] for w in name.split())


def fetch(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read()


def main():
    raw = fetch(MODEL)
    if hashlib.sha256(raw).hexdigest() != MODEL_SHA256:
        raise SystemExit("the UBL 2.5 model differs from the one this script was written for")
    rows = []
    for el in ET.fromstring(raw).iter():
        if el.tag.rsplit("}", 1)[-1] == "Row":
            rows.append({v.get("ColumnRef"): (v.findtext("{*}SimpleValue") or v.findtext("SimpleValue") or "")
                         for v in el})
    abies, by_den, docs, current = {}, {}, [], None
    text_bbies = sorted({r["ComponentName"] for r in rows
                         if r["ComponentType"] == "BBIE" and r["DataType"] in ("Text. Type", "Name. Type")})
    for r in rows:
        if r["ComponentType"] == "ABIE":
            current = r["ComponentName"]
            abies[current] = {"definition": r["Definition"], "bbies": [], "asbies": [],
                              "deprecated": r["Definition"].startswith(DEPRECATED)}
            by_den[r["DictionaryEntryName"].rsplit(". Details", 1)[0]] = current
            if not r["ModelName"].startswith("UBL-CommonLibrary"):
                docs.append(current)
        elif r["ComponentType"] == "BBIE":
            abies[current]["bbies"].append([r["ComponentName"], r["Cardinality"],
                                            r["Definition"].startswith(DEPRECATED)])
        else:
            abies[current]["asbies"].append([r["ComponentName"], r.get("AssociatedObjectClassQualifier", ""),
                                             r["AssociatedObjectClass"], r["Cardinality"], r["Definition"]])
    for a in abies.values():
        a["asbies"] = [[n, by_den[f"{q}_ {o}" if q else o], c, d] for n, q, o, c, d in a["asbies"]]

    xml = fetch(ROLES)
    table = ET.fromstring(re.sub(rb"<!DOCTYPE.*?\]>", b"", xml, flags=re.S))
    text = lambda e: " ".join("".join(e.itertext()).split()) if e is not None else ""
    lists = lambda e: {camel(text(s)) for s in e.findall("schema")} if e is not None else set()
    role_sends, role_receives = {}, {}
    for e in table.findall("entry"):
        role_sends.setdefault(text(e.find("role")), set()).update(lists(e.find("sends")))
        role_receives.setdefault(text(e.find("role")), set()).update(lists(e.find("receives")))

    def resolve(doc, path):
        a = doc
        for step in path.split("/"):
            hit = [x for x in abies[a]["asbies"] if x[0] == step]
            if not hit:
                raise SystemExit(f"{doc}: no {path} in the model")
            a, last = hit[0][1], hit[0]
        return last

    # UBL 2.5 also deprecates document types whose definition does not say so (the specification marks
    # Enquiry and Enquiry Response "Deprecated since UBL 2.5"); the endorsed schemas leave every deprecated
    # document type out (UBL 2.5, 3.4 Endorsed Schemas), so a document type without one is deprecated too
    endorsed_missing = set()
    for d in docs:
        req = urllib.request.Request(f"{ENDORSED}UBL-{d}-2.5.xsd", method="HEAD")
        try:
            urllib.request.urlopen(req, timeout=60)
        except urllib.error.HTTPError as e:
            if e.code != 404:
                raise
            endorsed_missing.add(d)
            abies[d]["deprecated"] = True
    # ... and the same for properties: what the endorsed schemas leave out of an aggregate is deprecated,
    # also where its definition does not say so (DebitNote/RequestedMonetaryTotal, for example)
    XS = "{http://www.w3.org/2001/XMLSchema}"

    def schema_types(url):
        root = ET.fromstring(fetch(url))
        return {ct.get("name"): {e.get("ref").split(":")[-1] for e in ct.iter(XS + "element") if e.get("ref")}
                for ct in root.iter(XS + "complexType")}
    library = schema_types(ENDORSED.replace("maindoc/", "common/") + "UBL-CommonAggregateComponents-2.5.xsd")
    for name, a in abies.items():
        if a["deprecated"]:
            continue
        endorsed = (schema_types(f"{ENDORSED}UBL-{name}-2.5.xsd").get(f"{name}Type") if name in docs
                    else library.get(f"{name}Type"))
        if endorsed is None:
            a["deprecated"] = True
            continue
        a["not_endorsed"] = sorted({b[0] for b in a["bbies"]} - endorsed |
                                   {x[0] for x in a["asbies"]} - endorsed)
        for b in a["bbies"]:
            if b[0] in a["not_endorsed"]:
                b[2] = True
    out = {}
    problems = []
    for d in docs:
        parties = [{"element": n, "cardinality": c, "definition": df} for n, t, c, df in abies[d]["asbies"]
                   if t == "Party" or (t.endswith("Party") and t not in docs)]
        names = {p["element"] for p in parties}
        if {"SenderParty", "ReceiverParty"} <= names:
            senders, receivers, basis = ["SenderParty"], ["ReceiverParty"], "element"
            evidence = [p["definition"] for p in parties if p["element"] in ("SenderParty", "ReceiverParty")]
        elif d in DIRECTION:
            senders, receivers, basis, evidence = DIRECTION[d]
            defs = [abies[d]["definition"]] + [resolve(d, p)[3] for p in senders + receivers] + \
                   [p["definition"] for p in parties]
            for path in senders + receivers:
                resolve(d, path)
            for q in evidence:
                if basis == "role table":
                    if not (d in role_sends.get(q, set()) or d in role_receives.get(q, set())):
                        problems.append(f"{d}: the role table does not list it for {q}")
                elif not any(q in x for x in defs):
                    problems.append(f"{d}: quote not in the model: {q}")
        else:
            problems.append(f"{d}: no sender and receiver known")
            continue
        out[d] = {"definition": abies[d]["definition"], "deprecated": abies[d]["deprecated"], "parties": parties, "senders": senders,
                  "receivers": receivers, "basis": basis, "evidence": evidence}
    for d in DIRECTION:
        if d not in docs:
            problems.append(f"{d}: not a UBL 2.5 document")
    if problems:
        raise SystemExit("\n".join(problems))
    result = {"source": MODEL, "sha256": MODEL_SHA256, "roles": ROLES, "documents": out, "text_bbies": text_bbies,
              "abies": {k: {"deprecated": v["deprecated"], "bbies": v["bbies"], "asbies": v["asbies"],
                            **({"not_endorsed": v["not_endorsed"]} if v.get("not_endorsed") else {})}
                        for k, v in abies.items()}}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")
    print(f"{len(out)} documents, {len(abies)} aggregates -> {os.path.relpath(OUT)}")


if __name__ == "__main__":
    main()
