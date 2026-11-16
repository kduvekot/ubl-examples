"""Minimal UBL 2.5 documents, built layer by layer.

Layer 0: only the elements (minOccurs >= 1) and attributes (use="required")
the schemas demand, plus the optional children chapter 4 makes necessary
(FILL). Layer 1 adds party identification (PARTY_SCHEMES).

Values: every value has a reason in its context, not a placeholder. Each
document has a locale (LOCALES: currency, country, language, time zone);
dates follow from D, the UBL 2.5 publication date (DATE_OFFSETS);
identifiers, names, texts, codes, quantities, measures and indicators are
chosen per element (id_for, ROLE_NAMES, TEXTS, NAMES, CODE_VALUES,
QUANTITY_UNITS, MEASURE_VALUES, INDICATOR_VALUES); identifier values
follow each scheme's format and check digit (ID_VALUES, TAX_VALUES).
A value type with no rule and no default stops the build, so a later
layer must choose it. The documents are unrelated to each other: values
are unique across the set, and references point outside it.
Each further layer is a table of decisions on top of the layers below it
(LAYERS); the same schema walk builds every layer, so element order,
required children, locales and checks follow automatically.

Fetches the UBL 2.5 package from OASIS into minimal/.ubl/ (not committed)
and writes <layer>/<DocType>.xml (endorsed) and <layer>/deprecated/.
Self-contained: uses nothing else from this repository.

After writing, every document is checked against the UBL 2.5 rules of
chapter 4, "Additional Document Constraints" (IND1-IND9, see check()).
The script exits with status 1 and lists every violation if one fails.

Usage: python3 minimal/gen_minimal.py               generate and check
       python3 minimal/gen_minimal.py --check FILE...  only check FILEs
"""
import os, re, sys, glob, io, subprocess, tempfile, urllib.request, zipfile
from lxml import etree

XS = "http://www.w3.org/2001/XMLSchema"
X = "{%s}" % XS
HERE = os.path.dirname(os.path.abspath(__file__))
ZIP_URL = "https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.zip"
UBL = os.path.join(HERE, ".ubl", "os-UBL-2.5")
if not os.path.isdir(UBL):
    with urllib.request.urlopen(ZIP_URL) as r:
        zipfile.ZipFile(io.BytesIO(r.read())).extractall(os.path.join(HERE, ".ubl"))
xsd_dir = os.path.join(UBL, "xsd")
endorsed = {os.path.basename(f) for f in glob.glob(os.path.join(UBL, "endorsed", "xsd", "maindoc", "*.xsd"))}

# One value per UDT data type (UBL's unqualified data types).
# A code, identifier, text or name without a chosen value gets this marker,
# and check() rejects it (as it rejects the old placeholder X): a later
# layer can never silently write a placeholder (ST#F5).
UNCHOSEN = "@UNCHOSEN@"
VALUES = {
    # Amounts: per document (AMOUNTS, amount_for). A layer that adds lines,
    # tax percentages or totals must make them add up (line = quantity x price,
    # total = sum of lines, tax = taxable x percent / 100, rounded to the
    # currency's minor unit, payable = total + tax).
    "BinaryObjectType": "(PDF_B64)",
    "CodeType": UNCHOSEN, "IdentifierType": UNCHOSEN, "NumericType": "1",
    "QuantityType": "10", "TextType": UNCHOSEN, "NameType": UNCHOSEN,
    # Date, time, measure, indicator: per element (date_for, UTC_OFFSETS,
    # MEASURE_VALUES, INDICATOR_VALUES). Percent, Rate, Value, Graphic,
    # Picture, Sound and Video have no default on purpose: a layer that first
    # needs one must choose a value per element (PH#F19).
}
# Amounts per document, fitting what the document is about (mostly 10
# ballpoint pens at a plausible unit price per currency), round, with the
# currency's minor unit (JPY none, the others two decimals); amounts in one
# document agree (line = total). No default: a new amount stops the build.
AMOUNTS = {
    "Invoice": 15, "PurchaseReceipt": 15, "RemittanceAdvice": 15,   # EUR 10 x 1.50
    "Reminder": 16, "Statement": 16,                                 # USD 10 x 1.60
    "CreditNote": 75, "SelfBilledCreditNote": 75, "Quotation": 75,   # BRL 10 x 7.50
    "CataloguePricingUpdate": 7.5,                                   # BRL one pen
    "DebitNote": 270, "SelfBilledInvoice": 270,                      # ZAR 10 x 27.00
    "FreightInvoice": 1200,                                          # BRL road freight
    "GuaranteeCertificate": 50000,                                   # INR bid bond
    "Tender": 500000,                                                # JPY office supplies bid
}
MINOR_UNITS = {"JPY": 0}  # ISO 4217; the other locale currencies have 2

def amount_for():
    return "%.*f" % (MINOR_UNITS.get(LOCALES[DOCNO % len(LOCALES)][0], 2), AMOUNTS[DOC])

# Indicator per element, no default. AcceptedIndicator: true, accepted; a
# rejection would need a RejectionNote (PH#F17).
INDICATOR_VALUES = {"AcceptedIndicator": "true",
                    # yes to "enrolled in a trade register?": needs no evidence
                    "ResponseIndicator": "true"}
# Attachment content: a minimal one-page PDF that shows the text "PDF"
# (built here byte by byte, with a correct cross-reference table).
def _pdf():
    import base64
    content = b"BT /F1 48 Tf 72 72 Td (PDF) Tj ET"
    objs = [b"<< /Type /Catalog /Pages 2 0 R >>",
            b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 240 160] "
            b"/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
            b"<< /Length %d >>\nstream\n" % len(content) + content + b"\nendstream",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"]
    out, offs = b"%PDF-1.4\n", []
    for i, o in enumerate(objs, 1):
        offs.append(len(out))
        out += b"%d 0 obj\n" % i + o + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    out += b"".join(b"%010d 00000 n \n" % o for o in offs)
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs) + 1, xref)
    return base64.b64encode(out).decode()
PDF_B64 = _pdf()

# Dates: D = 2026-08-12, the publication date of the UBL 2.5 OASIS Standard
# (its pubdate), after every identifier scheme used in the set started.
# Where D does not fit the context, an offset in days from D, chosen from the
# element's definition. Key: "Document:Parent/Element", "Parent/Element".
import datetime
D = datetime.date(2026, 8, 12)
DATE_OFFSETS = {
    "AwardDate": -2, "ResolutionDate": -2,      # decided before the notice, on a
                                                 # business day (Mon 2026-08-10)
    "SourceForecastIssueDate": -7,               # the revised forecast came first
    "ForecastPeriod/StartDate": 7, "ForecastPeriod/EndDate": 34,   # the future
    # observed or reported: before the issue date
    "ExceptionObservationPeriod/StartDate": -28, "ExceptionObservationPeriod/EndDate": -1,
    "ActivityPeriod/StartDate": -28, "ActivityPeriod/EndDate": -1,
    "ItemInformationRequest:Period/StartDate": -28, "ItemInformationRequest:Period/EndDate": -1,
    # valid or effective from the issue date, for a year
    "ValidityPeriod/EndDate": 364, "EffectivePeriod/EndDate": 364,
    "TradeItemLocationProfile:Period/EndDate": 364,
    # an announced retail event
    "RetailEvent:Period/StartDate": 14, "RetailEvent:Period/EndDate": 20,
}

# Times: 09:30 local, with the locale's UTC offset on D (midnight is the
# "time unknown" value, and without an offset the zone is implied, IND6).
TIME = "09:30:00"
UTC_OFFSETS = {"US": "-04:00", "DE": "+02:00", "JP": "+09:00",
               "IN": "+05:30", "BR": "-03:00", "ZA": "+02:00"}

# Identifiers (the documents are unrelated): the document's own ID is its
# type + "-1" (unique in the set); line IDs are 1 (local by convention);
# sequence and version identifiers are 1; every other identifier is its own
# label + a number, so no reference equals any document's ID (PH#F9, F10, F16).
def id_for(parent, name):
    p = etree.QName(parent).localname
    if name == "ID" and parent.getparent() is None:
        return DOC + "-1"
    # lines are numbered locally (1); a reference to a line in another
    # document is a line number too (VA#F9)
    if (name == "ID" and (p.endswith("Line") or p == "LineItem")) or name in ("LineID", "RevisedForecastLineID"):
        return "1"
    if name == "RegistrationNationalityID":  # the vehicle's country (ST#F3)
        return CTRY
    if name in ("SequenceNumberID", "VersionID"):
        return "1"
    if name == "ValidatedCriterionPropertyID":  # the question in this document
        return "TenderingCriterionProperty-1"
    label = p if name == "ID" else name
    IDS[label] = IDS.get(label, 0) + 1
    assert IDS[label] < 10, "identifier scheme supports at most 9 per label per document"
    # unique across the set (documents are unrelated): document position x 10 + n
    return "%s-%d" % (label, DOCNO * 10 + IDS[label])

def date_for(parent, name):
    pn = etree.QName(parent).localname
    for key in (DOC + ":" + pn + "/" + name, pn + "/" + name, name):
        if key in DATE_OFFSETS:
            return (D + datetime.timedelta(days=DATE_OFFSETS[key])).isoformat()
    return D.isoformat()

# mimeCode: the embedded binary is a real PDF (see _pdf), so application/pdf.
ATTRS = {"mimeCode": "application/pdf"}

# Locale: every document has one, by turns in alphabetical document order, so
# a document keeps its locale in every layer. It is used for every currency
# code, currencyID, country code and national identifier in the document (no
# cross-country minimal documents), and is visible only where one is needed.
# EUR has many countries; Germany stands for it.
LOCALES = [("USD", "US"), ("EUR", "DE"), ("JPY", "JP"),
           ("INR", "IN"), ("BRL", "BR"), ("ZAR", "ZA")]
CUR = "@CURRENCY@"  # placeholders, replaced per document
CTRY = "@COUNTRY@"

# Unit per Measure element, chosen from the element's UBL definition. No
# default: a Measure not listed here stops the build until a unit is chosen.
UNITS = {
    # ExceptionNotificationLine: the compared value and the source value it
    # is compared with count the line's SupplyItem, so the same unit: piece.
    "ComparedValueMeasure": "H87",
    "SourceValueMeasure": "H87",
    "GrossWeightMeasure": "KGM",   # a weight: kilogram
}

# Code values chosen per element (others stay X until a code-list layer).
# ThresholdValueComparisonCode: the definition lists the allowed values
# ("EXCEEDS_EXCEPTION_VALUE FALLS_BELOW_EXCEPTION_VALUE"); a shortfall.
# AdmissionCode: a Code whose definition reads like an Indicator ("accepted
# ... (true) or rejected ... (false)"; a UBL finding): true, admitted, since
# a rejection would need a reason.
CODE_VALUES = {"ThresholdValueComparisonCode": "FALLS_BELOW_EXCEPTION_VALUE",
               "AdmissionCode": "true",
               # Codes without a UBL default list get a descriptive value in
               # UBL's own style (as in its definitions, e.g. FALLS_BELOW_...),
               # without listID: the value states its meaning (IND6), and no
               # UN/EDIFACT list is used. ResponseCode: the invoice is approved.
               "ResponseCode": "ACCEPTED", "OrderResponseCode": "ACCEPTED",
               # the definition's examples (BASE PROMOTIONAL SEASONAL TOTAL); one
               # line, no promotion or season in the document: the whole demand
               "ForecastTypeCode": "TOTAL",
               # UBL: a forecast purpose "is either Sales forecast or Order
               # Forecast" (ForecastException/ForecastPurposeCode); the whole
               # demand reads as sales
               "ForecastPurposeCode": "SALES_FORECAST",
               # values listed for the same element elsewhere in UBL (CANCELED_
               # ORDERS ... SALES SHIPMENTS); a store's sales item over a period
               "SupplyChainActivityTypeCode": "SALES",
               # a falls-below threshold on stock: a stock-out warning
               "ExceptionCriteria:SupplyChainActivityTypeCode": "ON_HAND",
               # UBL default list LineStatusCode (Added, Cancelled, ..., Revised)
               "OrderChange:LineStatusCode": "Revised",
               "ExceptionNotification:SupplyChainActivityTypeCode": "ON_HAND",
               # "the logical state of the discrete activity": an event announced
               # two weeks ahead, nothing about a proposal or agreement
               "RetailEventStatusCode": "PLANNED",
               # the services the document type names (electricity, gas, water,
               # telephone); a later layer with consumption must match (KWH)
               "UtilityStatementTypeCode": "ELECTRICITY",
               # "the procedure under which this reminder was sent": the customs
               # procedure of the ATA Carnet, temporary admission
               "ProcedureCode": "TEMPORARY_ADMISSION",
               # TransportServiceCode, "the extent of this transportation service
               # (e.g., door-to-door, port-to-port)": a segment of an itinerary is
               # part of the route; a service (description) is the whole service
               "GoodsItemItinerary:TransportServiceCode": "PORT_TO_PORT",
               "TransportServiceDescriptionRequest:TransportServiceCode": "DOOR_TO_DOOR",
               "TransportServiceDescription:TransportServiceCode": "DOOR_TO_DOOR",
               "TransportExecutionPlan:TransportServiceCode": "DOOR_TO_DOOR",
               "TransportExecutionPlanRequest:TransportServiceCode": "DOOR_TO_DOOR",
               # "the overall status of transport service execution": under way
               "TransportExecutionStatusCode": "IN_TRANSIT"}

# Value per Measure, no default. ExceptionNotificationLine: the compared value
# must differ from the source value, or there is no exception (PH#F3).
MEASURE_VALUES = {"SourceValueMeasure": "10", "ComparedValueMeasure": "8",
                  "GrossWeightMeasure": "12000"}  # a loaded 20-foot container, kg

# Unit per Quantity ("Parent/Element"): its unitCode is optional, but without
# it the unit is implied by absence (IND6). No default, as for Measures.
QUANTITY_UNITS = {
    "WorkReportLine/Quantity": "HUR",   # "the quantity of work": hours
    # goods: pieces of the line's item
    "InstructionForReturnsLine/Quantity": "H87", "InventoryReportLine/Quantity": "H87",
    "StockAvailabilityReportLine/Quantity": "H87", "SalesItem/Quantity": "H87",
    "ExceptionCriteriaLine/ThresholdQuantity": "H87",
    "DespatchLine/DeliveredQuantity": "H87", "LineItem/Quantity": "H87",
    "ReceiptLine/ReceivedQuantity": "H87",
}

# Optional children added to an aggregate type on purpose (UBL 2.5 chapter 4).
# PeriodType: both StartDate and EndDate. A period with only a start would be
# "open-ended" by absence of its end, which IND6 forbids.
# TransportMeansType ("a particular vehicle or vessel"): only the mode-specific
# aggregates identify the vehicle; road is the simplest (its required
# LicensePlateID follows from the schema). RegistrationNationalityID states
# the country that registered the plate (the locale), not left implied (ST#F3).
FILL = {"PeriodType": {"cbc:StartDate", "cbc:EndDate"},
        "TransportMeansType": {"cac:RoadTransport", "cbc:RegistrationNationalityID"},
        # TenderedProjectType: the project is identified by the Tender's
        # ContractFolderID; the content is the bid, "the total amount for
        # this tendered project" (its PayableAmount follows from the schema).
        "TenderedProjectType": {"cac:LegalMonetaryTotal"},
        # Party wrappers: the other children are accounts, contacts or
        # features *of* the party; cac:Party is "the ... Party itself". In
        # TendererQualification nothing else says who the tenderer is.
        "SupplierPartyType": {"cac:Party"},
        "CustomerPartyType": {"cac:Party"},
        "QualifyingPartyType": {"cac:Party"},
        # PartyType ("an organization, sub-organization, or individual
        # fulfilling a role"): who it is. A name stands on its own; an ID
        # would need a schemeID, which is a later layer's decision (IND6).
        "PartyType": {"cac:PartyName"},
        # ItemType: "an item of trade. It includes a generic description
        # applicable to all examples of the item"; a Name is only "optionally
        # given". Identification depends on the document's perspective
        # (buyer, seller, standard): a later layer.
        "ItemType": {"cbc:Description"},
        # ShipmentType: "an identifiable collection of one or more goods
        # items". Its ID is a transaction reference like the document's own
        # ID, assigned within the exchange, not taken from a register.
        "ShipmentType": {"cbc:ID"},
        # ProcurementProjectType ("an overall definition of this procurement
        # project"): a particular undertaking gets a name, as a Party does
        # (a kind of thing, like an Item, gets a description).
        "ProcurementProjectType": {"cbc:Name"},
        # DigitalProcessType: the processes in scope of an agreement or
        # supported by a party are kinds of process, so a description. (Its
        # ID is defined for "the digital collaboration"; ProfileID would need
        # a scheme decision.)
        "DigitalProcessType": {"cbc:Description"},
        # ContactType: only SignatoryContact so far, "the individual ... who
        # signs". A signature needs the person's name, despite UBL's advice to
        # use a functional rather than a personal name.
        "ContactType": {"cbc:Name"},
        # CountryType: the ISO 3166-1 code is exact and language-neutral; the
        # value comes from the document's locale.
        "CountryType": {"cbc:IdentificationCode"},
        # BillingReferenceType: only in InvoiceStatusRequest, "a reference to
        # the Invoice for which a status update is requested"; the typed
        # reference needs no DocumentTypeCode, and the issuer follows from the
        # exchange's own parties (its required ID follows from the schema).
        "BillingReferenceType": {"cac:InvoiceDocumentReference"},
        # ResponseType: only in InvoiceStatusResponse, "a response to the
        # document as a whole"; the sibling DocumentReference says which
        # document, the code is the answer ("the type of response"). Its code
        # list is left to the code-list layer, like the other required codes.
        "ResponseType": {"cbc:ResponseCode"},
        # LocationType: only ActivityOriginLocation so far, one particular
        # place, so a name (an ID such as a GLN would need a scheme).
        "LocationType": {"cbc:Name"},
        # EvidenceType: only ReexportationEvidence so far, "references to
        # evidence supporting that goods have been re-exported" (the type
        # itself is defined for tendering only).
        "EvidenceType": {"cac:DocumentReference"},
        # TenderingCriterionResponseType: what is answered (ValidatedCriterion-
        # PropertyID, the yes/no property repeated in the same document, see
        # QualificationApplicationResponseType) and the answer (ResponseValue/
        # ResponseIndicator true).
        "TenderingCriterionResponseType": {"cbc:ValidatedCriterionPropertyID", "cac:ResponseValue"},
        "ResponseValueType": {"cbc:ResponseIndicator"},
        # QualificationApplicationResponse repeats the question it answers
        # ("the criterion as described in the Qualification Application
        # Request"), so the answer refers to a question in the same document:
        # one simple yes/no criterion property, answered true.
        # Document level (IND6): optional elements that carry a document's
        # defined purpose, without which the document says nothing. Each is
        # also a UBL finding (ubl-findings.md, "essential but optional").
        # ApplicationResponse: "the application's response to a transaction".
        "ApplicationResponseType": {"cac:DocumentResponse"},
        # BillOfLading "evidences a contract of carriage": who carries, for
        # whom, and what.
        "BillOfLadingType": {"cac:CarrierParty", "cac:ConsignorParty", "cac:Shipment"},
        # DocumentStatus / DocumentStatusRequest: the document concerned (and
        # for DocumentStatus its status, as for InvoiceStatusResponse).
        "DocumentStatusType": {"cac:DocumentResponse"},
        "DocumentStatusRequestType": {"cac:RequestedDocumentReference"},
        # Expressions of interest concern a tendering process; forecast and
        # revision lines forecast an item and a quantity; a fulfilment
        # cancellation cancels a despatch (spec 2.3.5.1.4).
        "ExpressionOfInterestRequestType": {"cbc:ContractFolderID"},
        "ExpressionOfInterestResponseType": {"cbc:ContractFolderID"},
        "ForecastLineType": {"cac:SalesItem"},
        "ForecastRevisionLineType": {"cac:SalesItem"},
        "FulfilmentCancellationType": {"cac:DespatchDocumentReference"},
        # a manifest lists its cargo; an order response states its answer
        "ManifestType": {"cac:Shipment"},
        "OrderResponseType": {"cbc:OrderResponseCode"},
        # the request defines the criterion its response repeats; a remittance
        # advice states the amount paid
        "QualificationApplicationRequestType": {"cac:TenderingCriterion"},
        "RemittanceAdviceType": {"cbc:TotalPaymentAmount"},
        # a service announcement: what service, by which provider
        "TransportServiceDescriptionType": {"cac:TransportationService", "cac:TransportServiceProviderParty"},
        # a status report: the status, and the consignment it is about; the
        # request: the consignment it asks about
        "TransportationStatusType": {"cbc:TransportExecutionStatusCode", "cac:Consignment"},
        "TransportationStatusRequestType": {"cac:Consignment"},
        # WeightStatement: the weight. GrossWeightMeasure is "goods plus
        # packaging plus transport equipment", the verified gross mass idea.
        "WeightStatement:ShipmentType": {"cbc:GrossWeightMeasure"},
        # a certificate of origin states the origin (the locale country: a CoO
        # is issued in the country of origin)
        "CertificateOfOrigin:ShipmentType": {"cac:OriginAddress"},
        "AddressType@OriginAddress": {"cac:Country"},
        # a report to authorities: what kind of report, and for which authority
        "CommonTransportationReportType": {"cbc:ReportType", "cac:AuthorityParty"},
        # exception lines say what they count (operational exception)
        "ExceptionCriteriaLineType": {"cbc:SupplyChainActivityTypeCode"},
        "ExceptionNotificationLineType": {"cbc:SupplyChainActivityTypeCode"},
        # an information request says which information: sales data
        "ItemInformationRequestLineType": {"cbc:SupplyChainActivityTypeCode"},
        # forwarding instructions: who instructs (consignor) which forwarder
        "ForwardingInstructionsType": {"cac:ConsignorParty", "cac:FreightForwarderParty"},
        # an order change says that its line is changed
        "OrderChange:LineItemType": {"cbc:LineStatusCode"},
        # procurement documents identify their procedure; a prior information
        # notice names what is to be bought
        **{d + "Type": {"cbc:ContractFolderID"} for d in (
            "ProcurementStatus", "ProcurementStatusRequest", "TenderStatus",
            "TenderStatusRequest", "TenderWithdrawal",
            "UnsubscribeFromProcedureRequest", "UnsubscribeFromProcedureResponse")},
        "PriorInformationNoticeType": {"cac:ProcurementProject"},
        # commercial documents say what they concern: the overdue invoice and
        # its amount (= the total), the balance, what is credited, what was
        # received, what work was done
        "ReminderLineType": {"cac:BillingReference", "cbc:DebitLineAmount"},
        "StatementType": {"cbc:TotalBalanceAmount"},
        "CreditNoteLineType": {"cac:Item"},
        "ReceiptAdviceType": {"cac:ReceiptLine"},
        "ReceiptLineType": {"cbc:ReceivedQuantity", "cac:Item"},
        "WorkReportLineType": {"cbc:WorkItemDescription"},
        # a retail event says what it is and is dated; a packing list
        # describes goods; a waybill names its issuer (carrier) and consignor;
        # a transit declaration has a declarant and what is declared
        "RetailEventType": {"cbc:Description", "cbc:IssueDate"},
        "PackingList:ShipmentType": {"cac:GoodsItem"},
        "GoodsItemType": {"cac:Item"},
        "WaybillType": {"cac:CarrierParty", "cac:ConsignorParty"},
        "TransitCustomsDeclarationType": {"cac:TransitExporterParty", "cac:Shipment"},
        # a progress status shows progress: the transport is at a terminal
        "TransportProgressStatusType": {"cac:TransportSchedule"},
        # the waste documents name the waste shipped
        "WasteMovement:ShipmentType": {"cac:GoodsItem"},
        "WasteNotification:ShipmentType": {"cac:GoodsItem"},
        # an enquiry asks something, its response answers it
        "EnquiryType": {"cbc:Description"},
        "EnquiryResponseType": {"cbc:Description"},
        # an award notice names the winner; an import declaration its
        # declarant; a transport execution plan (request) its service
        "ContractAwardNotice:TenderResultType": {"cac:WinningParty"},
        "ImportCustomsDeclarationType": {"cac:ImporterParty"},
        "GoodsCertificateType": {"cbc:Description"},  # what kind of certificate
        "TransportExecutionPlanType": {"cac:MainTransportationService"},
        "TransportExecutionPlanRequestType": {"cac:MainTransportationService"},
        # bills name the customer they are addressed to; lines that despatch,
        # deliver or order state their quantity, and an order-line reference
        # names its order
        "InvoiceType": {"cac:AccountingCustomerParty"},
        "CreditNoteType": {"cac:AccountingCustomerParty"},
        "DebitNoteType": {"cac:AccountingCustomerParty"},
        "DespatchLineType": {"cbc:DeliveredQuantity"},
        "OrderLineReferenceType": {"cac:OrderReference"},
        "LineItemType": {"cbc:Quantity"},
        # CataloguePricingUpdate updates prices: each line carries the price.
        "CataloguePricingUpdateLineType": {"cac:RequiredItemLocationQuantity"},
        "ItemLocationQuantityType": {"cac:Price"},
        "QualificationApplicationResponseType": {"cac:TenderingCriterion"},
        "TenderingCriterionType": {"cac:TenderingCriterionPropertyGroup"},
        "TenderingCriterionPropertyType": {"cbc:ID", "cbc:Description"},
        # AttachmentType: only in AttachedDocument ("a document of any kind to
        # be packaged with"), "containing the document content": embedded,
        # and binary because any kind of document must fit.
        "AttachmentType": {"cbc:EmbeddedDocumentBinaryObject"}}

# Layer 1: identification of parties, by role in its document's context
# (several schemes per document where the roles differ; no scheme dominant).
# - An ISO/IEC 6523 ICD code (official ICD list, Farance Inc. for ISO/IEC,
#   2026-07-26) goes in PartyIdentification/ID/@schemeID: 0088 GLN (as GS1's
#   ratified ICD 0209 standard prescribes), 0199 LEI, 0060 D-U-N-S.
# - "TAX": the national tax number, in PartyTaxScheme/CompanyID ("assigned for
#   tax purposes by the taxation authority"); most national numbers have no
#   ICD, and this element says whose number it is without a schemeID.
# GLN: GS1 defines it for parties and locations; here it is used only for
# location-bound roles and in GS1's own domains (catalogue data, CPFR/
# forecasting, retail, logistics), so that GS1 does not dominate. Generic
# roles (Sender, Receiver, Seller, Buyer) follow the document's domain.
# A key "Document/Role" overrides the key "Role".
# Roles not listed (authorities, chambers of commerce, certificate issuers)
# are identified by name only: no scheme has a real reason there yet. So is
# the CoO PreparationParty: "normally an individual, a group or a body", who
# may have no tax or company number.
# Convention (L1#F11): schemeID holds an ISO/IEC 6523 ICD, as EN 16931 and
# Peppol do; nothing else in the document says so. For example
#   <cbc:ID schemeID="0088">9520000000011</cbc:ID>
# reads: ICD 0088 = "GLN, Global Location Number", so the ID is a GS1 GLN.
# Likewise 0199 = LEI, 0060 = D-U-N-S, 0188 = Japanese Corporate Number.
GLN, LEI, DUNS, TAX = "0088", "0199", "0060", "TAX"
PARTY_SCHEMES = {
    # tax and accounting: the tax registration is what matters on a bill
    "AccountingSupplierParty": TAX, "AccountingCustomerParty": TAX,
    # ordering and quoting between businesses: D-U-N-S, long used in EDI
    "SellerSupplierParty": DUNS, "BuyerCustomerParty": DUNS,
    # ship-from and ship-to: locations
    "DespatchSupplierParty": GLN, "DeliveryCustomerParty": GLN,
    # retail stores and stock locations
    "RetailerCustomerParty": GLN, "InventoryReportingParty": GLN,
    "InstructionForReturns/SellerSupplierParty": GLN,
    "StockAvailabilityReport/SellerSupplierParty": GLN,
    # catalogue data (GS1's data synchronisation domain)
    "ProviderParty": GLN,
    # logistics operators and reports
    "SendingLogisticsOperatorParty": GLN, "ReporterParty": GLN,
    # a transport contract's provider, as a legal entity
    "TransportServiceProviderParty": LEI, "CarrierParty": LEI,
    # the consignor is a commercial shipper (a business): D-U-N-S; the freight
    # forwarder is the counterparty of a forwarding contract: LEI, as the
    # carrier. GLN stays for real locations and GS1 domains (not dominant).
    "ConsignorParty": DUNS, "FreightForwarderParty": LEI,
    # public procurement: the buyer as a legal entity; suppliers as businesses
    # whose identity and standing buyers verify
    "ContractingParty": LEI,
    "EconomicOperatorParty": DUNS, "TendererParty": DUNS,
    "MainQualifyingParty": DUNS, "InterestedParty": DUNS,
    # finance: the guarantee creditor (a bank) as a legal entity
    "GuarantorParty": LEI,
    # agreements between legal entities
    "ParticipantParty": LEI,
    # business registration, business cards, enquiries
    "BusinessParty": DUNS, "RequestorParty": DUNS, "ResponderParty": DUNS,
    # customs and waste: the legally responsible trader, by tax registration.
    # Waste roles have their own national registers (e.g. US EPA ID, German
    # waste-register numbers), but these have no ICD and no safe test range,
    # so the tax number is used.
    "ExporterParty": TAX, "HolderParty": TAX, "TransitExporterParty": TAX,
    "ImporterParty": TAX, "WinningParty": DUNS,
    "NotifierParty": TAX, "WasteProducerParty": TAX,
    # Sender and Receiver, by the document's domain:
    # generic business messages
    "SenderParty": DUNS, "ReceiverParty": DUNS,
    # GS1 domains: catalogue, item information, CPFR and forecasting
    **{d + "/" + r: GLN for r in ("SenderParty", "ReceiverParty") for d in (
        "Catalogue", "CatalogueDeletion", "CatalogueItemSpecificationUpdate",
        "CataloguePricingUpdate", "CatalogueRequest", "ItemInformationRequest",
        "Forecast", "ForecastRevision", "ExceptionCriteria", "ExceptionNotification",
        "ProductActivity", "RetailEvent", "TradeItemLocationProfile",
        "WeightStatement", "CommonTransportationReport")},
    # procurement: the contracting authority sends to the economic operator
    **{d + "/SenderParty": LEI for d in (
        "AwardedNotification", "UnawardedNotification", "TenderReceipt",
        "TendererQualificationResponse")},
    **{d + "/ReceiverParty": DUNS for d in (
        "AwardedNotification", "UnawardedNotification", "TenderReceipt",
        "TendererQualificationResponse")},
    # about invoices, utility bills and waste: the legally responsible parties
    **{d + "/" + r: TAX for r in ("SenderParty", "ReceiverParty") for d in (
        "InvoiceStatusRequest", "UtilityStatement", "WasteMovement", "WasteNotification")},
    # a utility customer is often not tax-registered
    "UtilityStatement/ReceiverParty": DUNS,
}

JPCN = "0188"  # Japan: Corporate Number (法人番号, National Tax Agency), an ICD

def scheme_for(party):
    """The scheme for a party's role. In Japanese documents the national
    Corporate Number replaces D-U-N-S, the LEI of contracting authorities
    (ContractingParty, procurement SenderParty), the LEI of agreement
    participants (businesses) and the tax number of the
    carnet holder: Japanese buyers, authorities and customs identify
    businesses and public bodies by it."""
    r = role(party)
    s = SCHEMES.get(DOC + "/" + r, SCHEMES.get(r))
    if COUNTRY == "JP" and (s == DUNS or (s == LEI and r in ("ContractingParty", "SenderParty", "ParticipantParty"))
                            or (s == TAX and r == "HolderParty")):
        return JPCN  # JP authorities and customs traders also have Corporate Numbers
    return s

# Identifier values: the scheme's own format and check digit, except where a
# deliberately invalid value is the only proof of non-assignment (ZA: fails
# Luhn; US: unassigned prefix 00) or the algorithm is unpublished (D-U-N-S);
# unique across the set; from official demonstration ranges where a scheme
# has one; checked not to be registered where a register can be queried
# (GLEIF, VIES, NTA, BrasilAPI for CNPJ; identification review, 2026-11-16).
def _gs1(d):  # GS1 mod 10
    t = sum(int(c) * (3 if i % 2 == 0 else 1) for i, c in enumerate(reversed(d)))
    return d + str((10 - t % 10) % 10)
def _lei(b):  # ISO 7064 MOD 97-10 (ISO 17442)
    return b + "%02d" % (98 - int("".join(str(int(c, 36)) for c in b + "00")) % 97)
def _jpcn(d):  # NTA: check digit first, 9 - (sum Pn*Qn mod 9), Qn = 1 odd, 2 even
    return str(9 - sum(int(c) * (1 if n % 2 else 2) for n, c in enumerate(reversed(d), 1)) % 9) + d
def _cnpj(b):  # Receita Federal mod 11, alphanumeric (value = ASCII - 48)
    def dv(x, w):
        r = sum((ord(c) - 48) * k for c, k in zip(x, w)) % 11
        return "0" if r < 2 else str(11 - r)
    d1 = dv(b, [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    return b + d1 + dv(b + d1, [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
def _de_vat(d):  # ISO 7064 MOD 11,10
    p = 10
    for c in d:
        p = (2 * ((int(c) + p) % 10 or 10)) % 11
    return "DE" + d + str((11 - p) % 10)
def _gstin(b):  # mod 36
    cs, t = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0
    for i, c in enumerate(b):
        v = cs.index(c) * (2 if i % 2 else 1)
        t += v // 36 + v % 36
    return b + cs[(36 - t % 36) % 36]

# k = document position in the set x 10 + party n: values are unique across the
# whole set (the documents are unrelated, so no two share a party).
def _luhn_bad(d):  # a digit that makes the number fail the Luhn check
    t = sum((int(c) * 2 - 9 if int(c) * 2 > 9 else int(c) * 2) if i % 2 == 0 else int(c)
            for i, c in enumerate(reversed(d)))
    return d + str((10 - t % 10 + 1) % 10)
# Source: https://docs.dnb.com/direct/2.0/en-US/duns-testing ("Test D-U-N-S
# Numbers ... for a fictitious company"), fetched 2026-11-16, 123 numbers.
# They show no simple check digit (no Luhn or weighted mod 10/11 rule fits),
# although the ICD 0060 entry speaks of one.
DUNS_TEST = [  # (D-U-N-S, country of the fictitious test company)
    ("214567885", "GB"), ("231634267", "GB"), ("239337363", "GB"), ("241018923", "CA"), ("241019160", "CA"), ("241019210", "CA"),
    ("241019251", "CA"), ("241019293", "CA"), ("241019335", "CA"), ("241019343", "CA"), ("241019368", "CA"), ("241019384", "CA"),
    ("241019426", "CA"), ("241019467", "CA"), ("241019509", "CA"), ("251930517", "CA"), ("302150375", "AT"), ("302150433", "AT"),
    ("302150557", "AT"), ("302150672", "AT"), ("302150730", "AT"), ("302150854", "AT"), ("302150912", "AT"), ("302150979", "AT"),
    ("302151035", "AT"), ("362152907", "US"), ("362179884", "US"), ("362185022", "US"), ("362212164", "US"), ("362217981", "US"),
    ("362221561", "US"), ("362223542", "US"), ("362229937", "US"), ("362241676", "US"), ("362241718", "US"), ("362242799", "US"),
    ("362248101", "US"), ("362248622", "US"), ("362253754", "US"), ("362257557", "US"), ("362264934", "US"), ("362267465", "US"),
    ("362267986", "US"), ("362272945", "US"), ("362277019", "US"), ("362288719", "US"), ("362301025", "US"), ("362301223", "US"),
    ("362304136", "US"), ("362312238", "US"), ("362313236", "US"), ("362315272", "US"), ("362338589", "US"), ("362343068", "US"),
    ("362344348", "US"), ("362348448", "US"), ("362353612", "US"), ("362353661", "US"), ("362368859", "US"), ("362372034", "US"),
    ("362379732", "US"), ("362380904", "US"), ("362381043", "US"), ("362383429", "US"), ("362398385", "US"), ("362399722", "US"),
    ("362403953", "US"), ("362417987", "US"), ("362425501", "US"), ("362428687", "US"), ("610788163", "US"), ("610788171", "US"),
    ("610796604", "US"), ("610796612", "US"), ("610796620", "US"), ("656251469", "TW"), ("662983733", "HK"), ("673054128", "AZ"),
    ("673054149", "RO"), ("673054180", "IS"), ("673054193", "AZ"), ("673054206", "BY"), ("673054222", "LV"), ("673054268", "RO"),
    ("673054300", "IS"), ("673054305", "UA"), ("673054359", "BY"), ("673054370", "LV"), ("673054412", "RO"), ("673054417", "RU"),
    ("673054446", "IS"), ("673054453", "UA"), ("680332202", "HK"), ("680332207", "HK"), ("680332210", "HK"), ("680332215", "HK"),
    ("680332223", "HK"), ("680332228", "HK"), ("680332231", "HK"), ("680332236", "HK"), ("680332244", "HK"), ("680332249", "HK"),
    ("914580993", "BR"), ("914581004", "BR"), ("914581009", "BR"), ("914581012", "BR"), ("914581017", "BR"), ("934994976", "PE"),
    ("934994984", "PE"), ("934994989", "PE"), ("934994992", "PE"), ("934994997", "PE"), ("978705614", "AR"), ("978705622", "AR"),
    ("978705627", "AR"), ("978705630", "AR"), ("978705635", "AR"), ("978705643", "AR"), ("978705697", "AR"), ("978705700", "AR"),
    ("978705705", "AR"), ("978705713", "AR"), ("978705718", "AR"),
]

_duns_used = []
def next_duns():
    n = DUNS_TEST[len(_duns_used)][0]
    _duns_used.append(n)
    return n

ID_VALUES = {
    GLN: lambda k: _gs1("952000%06d" % k),   # GS1 Prefix 952: "for demonstrations and examples"
    LEI: lambda k: _lei("999900MINIMAL%05d" % k),   # not in GLEIF
    # D-U-N-S: Dun & Bradstreet's official test numbers (DUNS_TEST), which
    # return data "for a fictitious company"; each party takes the next unused
    # one, so values are unique across the set. The test company's country
    # often differs from the document's locale: that keeps them visibly
    # fictitious (decision on ID#F1).
    DUNS: lambda k: next_duns(),
    JPCN: lambda k: _jpcn("9999%08d" % k),   # not in the NTA register
}
# National tax numbers (PartyTaxScheme/CompanyID) and the tax scheme's name.
TAX_VALUES = {
    "US": lambda k: "00%07d" % k,   # EIN prefix 00 is not assigned by the IRS
    "DE": lambda k: _de_vat("99%06d" % k),   # VIES: not valid
    "JP": lambda k: "T" + _jpcn("9999%08d" % k),   # qualified invoice issuer number
    "IN": lambda k: _gstin("97ZZZCZ%04dZ1Z" % k),   # 97 "Other Territory"; UNVERIFIED
    # one root per party (the root is the legal entity), head office 0001;
    # alphanumeric roots starting ZZ: UNVERIFIED as never assigned
    "BR": lambda k: _cnpj("ZZ%06d0001" % k),
    # deliberately fails the Luhn check (secondary sources: SARS uses Luhn), so
    # it cannot be a registered vendor; UNVERIFIED
    "ZA": lambda k: _luhn_bad("4%08d" % k),
}
# Official names: ZA "Value-Added Tax Act"; IN "Goods and Services Tax"; the
# EIN is the federal income tax identifier; the CNPJ is used for all federal
# taxes, so for BR it goes in PartyLegalEntity (the register).
# In the locale's language (languageID set, IND6): DE Umsatzsteuer (UStG),
# JP Shōhizei (consumption tax, romanized as other Japanese texts).
TAX_NAMES = {"US": "Federal Income Tax", "DE": "Umsatzsteuer", "JP": "Shōhizei",
             "IN": "Goods and Services Tax", "ZA": "Value-Added Tax"}

# Party names: "example" + the role, in the locale's language and in Latin
# script (Japanese in Hepburn romanization), + the party's number k as in its
# identifier; no legal form (that would claim a registration). The language is
# stated in languageID (IND6). Translations: checked against two independent
# human translations; agreed points applied, differences decided one by one.
# BCP 47 tags that state exactly what is used: Brazilian Portuguese (pt-BR)
# and Japanese in Latin script, Hepburn romanization (IANA variant
# "hepburn": ja-Latn-hepburn).
LANG = {"US": "en", "IN": "en", "ZA": "en", "DE": "de", "BR": "pt-BR", "JP": "ja-Latn-hepburn"}
EXAMPLE = {"en": "Example", "de": "Beispiel", "pt-BR": "Exemplo", "ja-Latn-hepburn": "Sanpuru"}
ROLE_NAMES = {  # role: (en, de, pt-BR, ja-Latn-hepburn)
    "AccountingSupplierParty": ("Supplier", "Lieferant", "Fornecedor", "Shiiresaki"),
    "AccountingCustomerParty": ("Customer", "Kunde", "Cliente", "Tokuisaki"),
    "SellerSupplierParty": ("Seller", "Verkäufer", "Vendedor", "Urite"),
    "BuyerCustomerParty": ("Buyer", "Käufer", "Comprador", "Kaite"),
    "DespatchSupplierParty": ("Shipper", "Versender", "Expedidor", "Niokurinin"),
    "DeliveryCustomerParty": ("Consignee", "Warenempfänger", "Destinatário", "Niukenin"),
    "RetailerCustomerParty": ("Retailer", "Einzelhändler", "Varejista", "Kourigyōsha"),
    "InventoryReportingParty": ("Inventory Reporter", "Bestandsmelder", "Informante de Estoque", "Zaiko Hōkokusha"),
    "ProviderParty": ("Provider", "Anbieter", "Provedor", "Teikyōsha"),
    "SenderParty": ("Sender", "Absender", "Remetente", "Sōshinsha"),
    "ReceiverParty": ("Receiver", "Empfänger", "Destinatário", "Jushinsha"),
    "RequestorParty": ("Requester", "Anfragender", "Solicitante", "Iraisha"),
    "ResponderParty": ("Responder", "Antwortender", "Respondente", "Kaitōsha"),
    "ParticipantParty": ("Participant", "Teilnehmer", "Participante", "Sankasha"),
    "TransportServiceProviderParty": ("Carrier", "Frachtführer", "Transportadora", "Unsō Gyōsha"),
    # StockAvailabilityReport: the receiving branch (DM#F118)
    "StockAvailabilityReport/InventoryReportingParty": ("Branch", "Filiale", "Filial", "Shiten"),
    "AuthorityParty": ("Authority", "Behörde", "Autoridade", "Tōkyoku"),
    "ImporterParty": ("Importer", "Einführer", "Importador", "Yunyūsha"),
    "WinningParty": ("Winning Tenderer", "Zuschlagsempfänger", "Licitante Vencedor", "Rakusatsusha"),
    "TransitExporterParty": ("Exporter", "Ausführer", "Exportador", "Yushutsusha"),
    "CarrierParty": ("Carrier", "Frachtführer", "Transportadora", "Unsō Gyōsha"),
    "ConsignorParty": ("Consignor", "Versender", "Expedidor", "Niokurinin"),
    "FreightForwarderParty": ("Freight Forwarder", "Spediteur", "Agente de Carga", "Fōwādā"),
    "SendingLogisticsOperatorParty": ("Logistics Operator", "Logistikdienstleister", "Operador Logístico", "Butsuryū Jigyōsha"),
    "ReporterParty": ("Reporter", "Berichterstatter", "Relator", "Hōkokusha"),
    "ContractingParty": ("Contracting Authority", "Öffentlicher Auftraggeber", "Órgão Contratante", "Hatchū Kikan"),
    "EconomicOperatorParty": ("Economic Operator", "Wirtschaftsteilnehmer", "Fornecedor", "Jigyōsha"),
    "TendererParty": ("Tenderer", "Bieter", "Licitante", "Nyūsatsusha"),
    "MainQualifyingParty": ("Main Tenderer", "Hauptbieter", "Licitante Principal", "Daihyō Nyūsatsusha"),
    "InterestedParty": ("Depositor", "Hinterleger", "Depositante", "Kyōtakusha"),
    "GuarantorParty": ("Guarantor", "Garantiegeber", "Garantidor", "Hoshōnin"),
    "BusinessParty": ("Business", "Unternehmen", "Empresa", "Kigyō"),
    "ExporterParty": ("Exporter", "Ausführer", "Exportador", "Yushutsusha"),
    "HolderParty": ("Holder", "Inhaber", "Titular", "Meiginin"),
    "NotifierParty": ("Notifier", "Notifizierender", "Notificante", "Tsūkokusha"),
    "WasteProducerParty": ("Waste Producer", "Abfallerzeuger", "Gerador de Resíduos", "Haishutsu Jigyōsha"),
    "CustomsParty": ("Customs", "Zollbehörde", "Alfândega", "Zeikan"),
    "ImportingGuarantorParty": ("Importing Guarantor", "Einfuhrbürge", "Garantidor de Importação", "Yunyū Hoshō Dantai"),
    "ExportingGuarantorParty": ("Exporting Guarantor", "Ausfuhrbürge", "Garantidor de Exportação", "Yushutsu Hoshō Dantai"),
    "IssuerParty": ("Issuer", "Aussteller", "Emissor", "Hakkōsha"),
    "EndorserParty": ("Endorser", "Beglaubigungsstelle", "Endossante", "Shōmeisha"),
    "PreparationParty": ("Preparer", "Ersteller", "Preparador", "Sakuseisha"),
}
LANG_INDEX = {"en": 0, "de": 1, "pt-BR": 2, "ja-Latn-hepburn": 3}

# Texts in the locale's language, Latin script, with languageID; key
# "Document:Parent/Element", "Parent/Element" or "Element". Translations:
# checked against two independent human translations; terms added after that
# review (e.g. report type, work item, retail event, waste, enquiry) are not
# yet reviewed.
TEXTS = {  # (en, de, pt-BR, ja-Latn-hepburn)
    "Item/Description": ("Ballpoint pen, blue", "Kugelschreiber, blau", "Caneta esferográfica, azul", "Bōrupen, ao"),
    # a freight invoice invoices a transport service, not goods (DM#F114)
    "FreightInvoice:Item/Description": ("Road freight", "Straßentransport", "Frete rodoviário", "Rikujō yusō"),
    "WorkItemDescription": ("Maintenance of office equipment", "Wartung der Büroausstattung",
                            "Manutenção de equipamentos de escritório", "Jimu kiki no hoshu"),
    # the period (late August) fits a back-to-school promotion
    "RetailEvent/Description": ("Back-to-school promotion", "Schulanfangsaktion",
                                "Promoção de volta às aulas", "Shingakki kyanpēn"),
    "Enquiry/Description": ("Is the item available from stock?", "Ist der Artikel ab Lager verfügbar?",
                            "O item está disponível em estoque?", "Shōhin wa zaiko ga arimasu ka?"),
    "EnquiryResponse/Description": ("Yes, the item is available from stock.",
                                    "Ja, der Artikel ist ab Lager verfügbar.",
                                    "Sim, o item está disponível em estoque.", "Hai, zaiko ga arimasu."),
    "GoodsCertificate/Description": ("Certificate of conformity", "Konformitätsbescheinigung",
                                     "Certificado de conformidade", "Tekigō shōmeisho"),
    "ReportType": ("Pre-arrival notification", "Voranmeldung der Ankunft",
                   "Notificação de pré-chegada", "Nyūkō mae tsūhō"),
    # a hazardous waste shipped across borders for recycling (Basel A1160)
    **{d + ":Item/Description": ("Used lead-acid batteries", "Gebrauchte Blei-Säure-Batterien",
                                 "Baterias de chumbo-ácido usadas", "Shiyōzumi namari chikudenchi")
       for d in ("WasteMovement", "WasteNotification")},
    "SupplyItem/Description": ("Ballpoint pen, blue", "Kugelschreiber, blau", "Caneta esferográfica, azul", "Bōrupen, ao"),
    "CancellationNote": ("Ordered in error", "Irrtümlich bestellt", "Pedido feito por engano", "Gohatchū"),
    "CertificateType": ("Ordinary", "Nichtpräferenziell", "Comum", "Ippan"),   # from the definition's examples
    "ApprovalStatus": ("Approved", "Genehmigt", "Aprovado", "Shōninzumi"),
    "TenderingCriterionProperty/Description": (
        "Is the economic operator enrolled in a trade register?",
        "Ist der Wirtschaftsteilnehmer in einem Handelsregister eingetragen?",
        "O operador econômico está inscrito em um registro comercial?",
        "Jigyōsha wa shōgyō tōki sarete imasu ka?"),
    "DigitalProcess/Description": ("Ordering", "Bestellung", "Pedidos", "Hatchū"),
}

NAMES = {  # (en, de, pt-BR, ja-Latn-hepburn); visibly fictitious
    "SignatoryContact/Name": ("Alex Example", "Alex Beispiel", "Alex Exemplo", "Sanpuru Tarō"),
    "StatusLocation/Name": ("Example Terminal 1", "Beispielterminal 1", "Terminal Exemplo 1", "Sanpuru Tāminaru 1"),
    "ActivityOriginLocation/Name": ("Example Store 1", "Beispielfiliale 1", "Loja Exemplo 1", "Sanpuru Tenpo 1"),
    "ProcurementProject/Name": ("Office supplies 2026", "Büromaterial 2026", "Material de escritório 2026", "Jimu Yōhin 2026"),
}

SECOND_SIGNATORY = ("Sam Example", "Sam Beispiel", "Sam Exemplo", "Sanpuru Hanako")

def name_for(e, parent, name):
    key = etree.QName(parent).localname + "/" + name
    t = NAMES.get(key)
    if t is None:
        return VALUES["NameType"]
    lang = LANG[COUNTRY]
    e.set("languageID", lang)
    if key == "ProcurementProject/Name":  # unique across the set
        return "%s (%d)" % (t[LANG_INDEX[lang]], DOCNO)
    return t[LANG_INDEX[lang]]

def text_for(e, parent, name):
    pn = etree.QName(parent).localname
    t = TEXTS.get(DOC + ":" + pn + "/" + name) or TEXTS.get(pn + "/" + name) or TEXTS.get(name)
    if t is None:
        return VALUES["TextType"]
    lang = LANG[COUNTRY]
    e.set("languageID", lang)
    return t[LANG_INDEX[lang]]

LAYER1 = {
    "PartyTaxSchemeType": {"cbc:CompanyID"},
    # BR: the CNPJ is "an identifier for the party as registered within a
    # company registration scheme"; the scheme is named and states its country
    "PartyLegalEntityType": {"cbc:CompanyID", "cac:CorporateRegistrationScheme"},
    "CorporateRegistrationSchemeType": {"cbc:Name", "cac:JurisdictionRegionAddress"},
    # TaxScheme is required in PartyTaxScheme: the particular tax scheme gets
    # a name, as other particular things do.
    "TaxSchemeType": {"cbc:Name", "cac:JurisdictionRegionAddress"},
    # the jurisdiction is stated, not implied by the number's format (IND6)
    "AddressType@JurisdictionRegionAddress": {"cac:Country"},
}

# Repetition where the meaning needs more than one occurrence (DM#F12): an
# agreement needs at least two participants ("bi-lateral and multi-lateral").
REPEAT = {"DigitalAgreementType/cac:ParticipantParty": 2}

# Planned for a later layer (each layer stays valid on its own):
# - UtilityStatement consumption (DM#F116): SubscriberConsumption ->
#   UtilityConsumptionPoint -> consumed quantity in KWH (ELECTRICITY). Until
#   then the statement does not show its consumption.

# Layers: (folder, additions {aggregate type[@role]: optional children},
# schemeIDs by role). Each layer includes everything of the layers before it.
LAYERS = [("layer0", FILL, {}),
          ("layer1", LAYER1, PARTY_SCHEMES)]

def layer_fills():
    total, schemes = {}, {}
    for name, add, sch in LAYERS:
        for t, kids in add.items():
            total[t] = total.get(t, set()) | kids
        schemes.update(sch)
        yield name, {t: set(k) for t, k in total.items()}, dict(schemes)

# Two schema sets: the endorsed ones (stricter endorsed cardinalities) build
# and validate the 93 endorsed document types; the full ones the 8 deprecated
# document types, which are not in the endorsed set (ST#F1).
endorsed_dir = os.path.join(UBL, "endorsed", "xsd")
def load_schemas(d):
    out = {}  # targetNamespace -> list of schema roots
    for f in glob.glob(os.path.join(d, "common", "*.xsd")) + glob.glob(os.path.join(d, "maindoc", "*.xsd")):
        r = etree.parse(f).getroot()
        out.setdefault(r.get("targetNamespace"), []).append(r)
    return out
FULL_SCHEMAS, ENDORSED_SCHEMAS = load_schemas(xsd_dir), load_schemas(endorsed_dir)
schemas = FULL_SCHEMAS

QDT = "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDataTypes-2"
CBC = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
CAC = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"

def qname(node, ref):
    p, _, local = ref.rpartition(":")
    return node.nsmap.get(p or None), local

def find(kind, ns, name):
    for r in schemas.get(ns, []):
        for d in r.findall(X + kind):
            if d.get("name") == name:
                return d
    raise KeyError((kind, ns, name))

def udt_name(ctype_ns, ctype):
    """Follow derivation until a UDT type is reached."""
    udt = "urn:oasis:names:specification:bdndr:schema:xsd:UnqualifiedDataTypes-1"
    while ctype_ns != udt:
        t = find("complexType", ctype_ns, ctype)
        base = t.find(".//" + X + "restriction") if t.find(".//" + X + "extension") is None else t.find(".//" + X + "extension")
        ctype_ns, ctype = qname(base, base.get("base"))
    return ctype

def required_attrs(t):
    out = {}
    for a in t.iter(X + "attribute"):
        if a.get("use") == "required":
            out[a.get("name")] = ATTRS.get(a.get("name"))
    return out

def build(parent, el_decl):
    """el_decl: a global xsd:element. Append an instance to parent."""
    ns = el_decl.getparent().get("targetNamespace")
    e = etree.SubElement(parent, "{%s}%s" % (ns, el_decl.get("name")))
    tns, tname = qname(el_decl, el_decl.get("type"))
    t = find("complexType", tns, tname)
    if t.find(X + "simpleContent") is not None:
        u = udt_name(tns, tname)
        e.text = (date_for(parent, el_decl.get("name")) if u == "DateType"
                  else amount_for() if u == "AmountType"
                  else id_for(parent, el_decl.get("name")) if u == "IdentifierType"
                  else text_for(e, parent, el_decl.get("name")) if u == "TextType"
                  else name_for(e, parent, el_decl.get("name")) if u == "NameType"
                  else TIME + UTC_OFFSETS[COUNTRY] if u == "TimeType"
                  else D.isoformat() + "T" + TIME + UTC_OFFSETS[COUNTRY] if u == "DateTimeType"
                  else MEASURE_VALUES[el_decl.get("name")] if u == "MeasureType"
                  else INDICATOR_VALUES[el_decl.get("name")] if u == "IndicatorType"
                  else CODE_VALUES.get(DOC + ":" + el_decl.get("name"),
                                  CODE_VALUES.get(el_decl.get("name"), VALUES[u])) if u == "CodeType"
                  else PDF_B64 if u == "BinaryObjectType" else VALUES[u])
        attrs = {}
        cur_ns, cur = tns, tname
        while True:  # collect required attributes along the derivation chain
            if (cur_ns, cur) == (QDT, "CurrencyCodeType"):
                e.text = CUR
            if (cur_ns, cur) == (QDT, "CountryIdentificationCodeType"):
                e.text = CTRY
            ct = find("complexType", cur_ns, cur)
            attrs.update(required_attrs(ct))
            der = ct.find(".//" + X + "extension")
            if der is None: der = ct.find(".//" + X + "restriction")
            b_ns, b = qname(der, der.get("base"))
            if b_ns == XS: break
            cur_ns, cur = b_ns, b
        if "currencyID" in attrs:
            attrs["currencyID"] = CUR
        if "unitCode" in attrs:
            if el_decl.get("name") not in UNITS:
                raise KeyError("no unit chosen for " + el_decl.get("name"))
            attrs["unitCode"] = UNITS[el_decl.get("name")]
        if u == "QuantityType":
            key = etree.QName(parent).localname + "/" + el_decl.get("name")
            if key not in QUANTITY_UNITS:
                raise KeyError("no unit chosen for " + key)
            attrs["unitCode"] = QUANTITY_UNITS[key]
        for k, v in attrs.items(): e.set(k, v)
    else:
        content(e, t)
    return e

def role(e):
    """The role an element plays: its own name, or for a Party inside a
    wrapper (SupplierParty, ContractingParty ...) the wrapper's name."""
    q = etree.QName(e).localname
    if q == "Party" and e.getparent() is not None:
        return etree.QName(e.getparent()).localname
    return q

def party_extra(e, t):
    """Layer 1: the identification a Party gets for its role."""
    if t.get("name") != "PartyType":
        return ()
    s = scheme_for(e)
    if s == TAX and COUNTRY == "BR":
        return ("cac:PartyLegalEntity",)  # the CNPJ registers the legal entity
    return () if s is None else ("cac:PartyTaxScheme",) if s == TAX else ("cac:PartyIdentification",)

def content(e, t):
    for child in t:
        if child.tag in (X + "sequence", X + "choice"):
            if child.get("minOccurs") == "0": continue
            if child.tag == X + "choice":
                raise NotImplementedError("required choice in %s" % t.get("name"))
            for p in child:
                if p.tag == X + "element" and (p.get("minOccurs", "1") != "0"
                                               or p.get("ref") in FILL.get(t.get("name"), ())
                                               or p.get("ref") in FILL.get(t.get("name") + "@" + role(e), ())
                                               or p.get("ref") in FILL.get(DOC + ":" + t.get("name"), ())
                                               or p.get("ref") in party_extra(e, t)):
                    ns, name = qname(p, p.get("ref"))
                    for _ in range(REPEAT.get(t.get("name") + "/" + p.get("ref"), 1)):
                        build(e, find("element", ns, name))
                elif p.tag in (X + "sequence", X + "choice", X + "any") and p.get("minOccurs", "1") != "0":
                    raise NotImplementedError(p.tag)

def generate(layer, fill, schemes):
    global FILL, SCHEMES, DOC
    FILL, SCHEMES = fill, schemes
    out = os.path.join(HERE, layer)
    os.makedirs(os.path.join(out, "deprecated"), exist_ok=True)
    global COUNTRY
    _duns_used.clear()  # the same assignment in every layer
    written = []
    for f in sorted(glob.glob(os.path.join(xsd_dir, "maindoc", "UBL-*-2.5.xsd"))):
        global schemas
        is_endorsed = os.path.basename(f) in endorsed
        if is_endorsed:
            f = os.path.join(endorsed_dir, "maindoc", os.path.basename(f))
        schemas = ENDORSED_SCHEMAS if is_endorsed else FULL_SCHEMAS
        r = etree.parse(f).getroot()
        ns = r.get("targetNamespace")
        root_decl = r.find(X + "element")
        name = DOC = root_decl.get("name")
        currency, COUNTRY = LOCALES[len(written) % len(LOCALES)]
        global IDS, DOCNO
        IDS, DOCNO = {}, len(written)
        nsmap = {None: ns,
                 "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
                 "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"}
        doc = etree.Element("{%s}%s" % (ns, name), nsmap=nsmap)
        t = find("complexType", *qname(root_decl, root_decl.get("type")))
        content(doc, t)
        etree.cleanup_namespaces(doc)  # drop cac/cbc where unused
        parties = [p for p in doc.iter("{*}*") if p.find("{%s}PartyName" % CAC) is not None]
        for n, party in enumerate(parties, 1):
            assert n < 10, "value scheme supports at most 9 parties per document"
            k = len(written) * 10 + n
            lang = LANG[COUNTRY]
            nm = party.find("{%s}PartyName/{%s}Name" % (CAC, CBC))
            r_name = (ROLE_NAMES.get(DOC + "/" + role(party)) or ROLE_NAMES[role(party)])[LANG_INDEX[lang]]
            # Portuguese puts the modifier after the noun: "Comprador Exemplo 492"
            # German compounds one-word roles ("Beispielkäufer 492"); multi-word
            # roles stay separate ("Beispiel Öffentlicher Auftraggeber 1")
            if lang == "pt-BR":
                nm.text = "%s %s %d" % (r_name, EXAMPLE[lang], k)
            elif lang == "de" and " " not in r_name:
                nm.text = "%s%s %d" % (EXAMPLE[lang], r_name[0].lower() + r_name[1:], k)
            else:
                nm.text = "%s %s %d" % (EXAMPLE[lang], r_name, k)
            nm.set("languageID", lang)
            pid = party.find("{%s}PartyIdentification/{%s}ID" % (CAC, CBC))
            if pid is not None:
                s = scheme_for(party)
                pid.set("schemeID", s)
                pid.text = ID_VALUES[s](k)
            ple = party.find("{%s}PartyLegalEntity" % CAC)
            if ple is not None:
                ple.find("{%s}CompanyID" % CBC).text = TAX_VALUES[COUNTRY](k)
                crn = ple.find("{%s}CorporateRegistrationScheme/{%s}Name" % (CAC, CBC))
                crn.text = "Cadastro Nacional da Pessoa Jurídica"
                crn.set("languageID", "pt-BR")
            pts = party.find("{%s}PartyTaxScheme" % CAC)
            if pts is not None:
                pts.find("{%s}CompanyID" % CBC).text = TAX_VALUES[COUNTRY](k)
                tsn = pts.find("{%s}TaxScheme/{%s}Name" % (CAC, CBC))
                tsn.text = TAX_NAMES[COUNTRY]
                tsn.set("languageID", LANG[COUNTRY])
        # SequenceNumeric: "the order ... in the sequence", from 1, numbered
        # through the document among things of the same kind (PH#F11)
        seq = {}
        for e in doc.iter("{%s}SequenceNumeric" % CBC):
            kind = etree.QName(e.getparent()).localname
            seq[kind] = seq.get(kind, 0) + 1
            e.text = str(seq[kind])
        # EndorserParty RoleCode ("e.g., issuer, embassy, insurance"): the
        # issuer endorses first, an embassy legalizes after it, so the order
        # of endorsement (SequenceNumeric) follows that, not document order.
        ENDORSERS = {"IssuerEndorsement": ("ISSUER", "1"),
                     "CertificateOfOriginApplication": ("EMBASSY", "2")}
        for ep in doc.iter("{%s}EndorserParty" % CAC):
            code, seqno = ENDORSERS[etree.QName(ep.getparent()).localname]
            ep.find("{%s}RoleCode" % CBC).text = code
            ep.find("{%s}SequenceNumeric" % CBC).text = seqno
        # the issuer's endorsement is signed by its own person, not by the
        # embassy's signatory (VA#F3)
        sig = doc.find(".//{%s}IssuerEndorsement//{%s}SignatoryContact/{%s}Name" % (CAC, CAC, CBC))
        if sig is not None:
            sig.text = SECOND_SIGNATORY[LANG_INDEX[LANG[COUNTRY]]]
        # the issuer's endorsement is given by the issuer itself (DM#F4)
        issuer = doc.find(".//{%s}IssuerParty/{%s}PartyName/{%s}Name" % (CAC, CAC, CBC))
        ie = doc.find(".//{%s}IssuerEndorsement/{%s}EndorserParty/{%s}Party/{%s}PartyName/{%s}Name"
                      % (CAC, CAC, CAC, CAC, CBC))
        if issuer is not None and ie is not None:
            ie.text = issuer.text
        for e in doc.iter():
            if e.text == CUR: e.text = currency
            if e.text == CTRY: e.text = COUNTRY
            if e.get("currencyID") == CUR: e.set("currencyID", currency)
        path = os.path.join(out, "" if is_endorsed else "deprecated", name + ".xml")
        with open(path, "wb") as fh:  # declaration exactly as the IND2/IND3 example
            fh.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            fh.write(etree.tostring(doc, encoding="UTF-8", pretty_print=True))
        written.append((path, f))
    return written

# --- Checks: UBL 2.5 chapter 4, Additional Document Constraints -------------
# IND6 (absence carries no meaning) cannot be tested by machine; it is
# handled where values are chosen (see FILL).
TEXT_ELEMENTS = {  # cbc elements of "Text. Type" (TextType and NameType)
    d.get("name") for d in schemas[CBC][0].findall(X + "element")
    if udt_name(*qname(d, d.get("type"))) in ("TextType", "NameType")}

def check(path, xsd):
    errors = []
    raw = open(path, "rb").read()
    decl = re.match(rb'<\?xml[^>]*\?>', raw)
    enc = decl and re.search(rb'encoding=["\']([^"\']+)', decl.group(0))
    if not enc:  # IND2
        errors.append("IND2 no character encoding in the XML declaration")
    elif enc.group(1).upper() != b"UTF-8":  # IND3
        errors.append("IND3 encoding is %s, not UTF-8" % enc.group(1).decode())
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError as ex:
        errors.append("IND3 not valid UTF-8: %s" % ex)
    try:
        doc = etree.parse(path)
    except etree.XMLSyntaxError as ex:
        return errors + ["IND1 not well-formed: %s" % ex]
    schema = etree.XMLSchema(etree.parse(xsd))
    if not schema.validate(doc):  # IND1
        errors += ["IND1 %s" % e for e in schema.error_log]
    def path_of(e):
        steps = []
        while e is not None:
            q = etree.QName(e)
            pre = {CBC: "cbc:", CAC: "cac:"}.get(q.namespace, "")
            sib = [s for s in (e.getparent() if e.getparent() is not None else []) if s.tag == e.tag]
            steps.append(pre + q.localname + ("[%d]" % (sib.index(e) + 1) if len(sib) > 1 else ""))
            e = e.getparent()
        return "/" + "/".join(reversed(steps))
    for e in doc.iter(etree.Element):
        where = path_of(e)
        if len(e) == 0 and not (e.text or "").strip():  # IND5
            errors.append("IND5 empty element %s" % where)
        elif len(e) == 0 and (e.text or "").strip() in (UNCHOSEN, "X"):  # IND5 null-like
            errors.append("IND5 placeholder value %r in %s" % (e.text.strip(), where))
        for k, v in e.attrib.items():  # IND9
            if not v.strip():
                errors.append("IND9 empty attribute %s/@%s" % (where, k))
        seen = {}  # IND7, IND8: repeated Text siblings of the same name
        for c in e:
            q = etree.QName(c)
            if q.namespace == CBC and q.localname in TEXT_ELEMENTS:
                seen.setdefault(q.localname, []).append(c.get("languageID"))
        for n, langs in seen.items():
            if len(langs) > 1:
                if langs.count(None) > 1:
                    errors.append("IND8 %s/cbc:%s: more than one without languageID" % (where, n))
                dup = {l for l in langs if l is not None and langs.count(l) > 1}
                if dup:
                    errors.append("IND7 %s/cbc:%s: languageID repeated: %s" % (where, n, ", ".join(sorted(dup))))
    return errors

def phase2(paths):
    """IND1 section's recommended second phase: UBL default code lists,
    with the package's own XSLT and Saxon, as in val/validate.sh."""
    val = os.path.join(UBL, "val")
    errors = {}
    with tempfile.TemporaryDirectory() as tmp:
        src, res = os.path.join(tmp, "in"), os.path.join(tmp, "out")
        os.makedirs(src); os.makedirs(res)
        for i, p in enumerate(paths):  # one Saxon run for all files
            os.symlink(os.path.abspath(p), os.path.join(src, "%04d.xml" % i))
        r = subprocess.run(["java", "-jar", os.path.join(val, "saxon9he.jar"), "-s:" + src,
                            "-o:" + res, "-xsl:" + os.path.join(val, "UBL-DefaultDTQ-2.5.xsl")],
                           capture_output=True, text=True)
        for i, p in enumerate(paths):
            o = os.path.join(res, "%04d.xml" % i)
            if not os.path.exists(o):
                errors[p] = ["code list: not checked: " + (r.stderr.strip().splitlines() or ["?"])[-1]]
                continue
            msgs = re.findall(r"<svrl:text>(.*?)</svrl:text>", open(o, encoding="utf-8").read(), re.S)
            if msgs:
                errors[p] = ["code list: " + " ".join(m.split()) for m in msgs]
    return errors

def xsd_for(path):
    try:
        name = etree.QName(etree.parse(path).getroot()).localname
    except etree.XMLSyntaxError:
        name = "Invoice"  # not parseable; check() reports it
    e = os.path.join(endorsed_dir, "maindoc", "UBL-%s-2.5.xsd" % name)
    return e if os.path.exists(e) else os.path.join(xsd_dir, "maindoc", "UBL-%s-2.5.xsd" % name)

if sys.argv[1:2] == ["--check"]:
    written = [(p, xsd_for(p)) for p in sys.argv[2:]]
else:
    written = []
    for layer, fill, schemes in layer_fills():
        written += generate(layer, fill, schemes)
failed = {}
for path, xsd in written:
    errs = check(path, xsd)
    if errs:
        failed[path] = errs
for p, errs in phase2([p for p, _ in written]).items():
    failed.setdefault(p, []).extend(errs)
for p in sorted(failed):
    print(os.path.relpath(p))
    for e in failed[p]:
        print("  " + e)
print("%d documents, %d with violations" % (len(written), len(failed)))
sys.exit(1 if failed else 0)
