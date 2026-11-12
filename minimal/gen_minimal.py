"""Minimal UBL 2.5 documents, built layer by layer.

Layer 0: only the elements (minOccurs >= 1) and attributes (use="required")
the schemas demand, plus the optional children chapter 4 makes necessary
(FILL), with one fixed value per unqualified data type.
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
VALUES = {
    # 100: a whole number, valid for every currency (JPY has no decimals). Every
    # document has one amount and no tax yet; a layer that adds lines, tax
    # percentages or totals must make them add up (line = quantity x price,
    # total = sum of lines, tax = taxable x percent / 100, rounded to the
    # currency's minor unit, payable = total + tax).
    "AmountType": "100", "BinaryObjectType": "(PDF_B64)",
    "CodeType": "X", "IdentifierType": "X", "NumericType": "1",
    "QuantityType": "10", "TextType": "X", "NameType": "X",
    # Date, time, measure, indicator: per element (date_for, UTC_OFFSETS,
    # MEASURE_VALUES, INDICATOR_VALUES). Percent, Rate, Value, Graphic,
    # Picture, Sound and Video have no default on purpose: a layer that first
    # needs one must choose a value per element (PH#F19).
}
# Indicator per element, no default. AcceptedIndicator: true, accepted; a
# rejection would need a RejectionNote (PH#F17).
INDICATOR_VALUES = {"AcceptedIndicator": "true"}
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
    "AwardDate": -3, "ResolutionDate": -3,      # decided before the notice
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
    if (name == "ID" and (p.endswith("Line") or p == "LineItem")) or name == "LineID":
        return "1"
    if name in ("SequenceNumberID", "VersionID"):
        return "1"
    label = p if name == "ID" else name
    IDS[label] = IDS.get(label, 0) + 1
    return "%s-%d" % (label, IDS[label])

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
               "ResponseCode": "ACCEPTED",
               # the definition's examples (BASE PROMOTIONAL SEASONAL TOTAL); one
               # line, no promotion or season in the document: the whole demand
               "ForecastTypeCode": "TOTAL",
               # CPFR purposes SALES_FORECAST / ORDER_FORECAST (domain knowledge,
               # not verified against GS1): the whole demand reads as sales
               "ForecastPurposeCode": "SALES_FORECAST",
               # "the extent of this transportation service (e.g., door-to-door,
               # port-to-port)": a segment of an itinerary is part of the route;
               # a service description request is about the whole service
               # values listed for the same element elsewhere in UBL (CANCELED_
               # ORDERS ... SALES SHIPMENTS); a store's sales item over a period
               "SupplyChainActivityTypeCode": "SALES",
               # "the logical state of the discrete activity": an event announced
               # two weeks ahead, nothing about a proposal or agreement
               "RetailEventStatusCode": "PLANNED",
               # the services the document type names (electricity, gas, water,
               # telephone); a later layer with consumption must match (KWH)
               "UtilityStatementTypeCode": "ELECTRICITY",
               "GoodsItemItinerary:TransportServiceCode": "PORT_TO_PORT",
               "TransportServiceDescriptionRequest:TransportServiceCode": "DOOR_TO_DOOR"}

# Value per Measure, no default. ExceptionNotificationLine: the compared value
# must differ from the source value, or there is no exception (PH#F3).
MEASURE_VALUES = {"SourceValueMeasure": "10", "ComparedValueMeasure": "8"}

# Unit per Quantity ("Parent/Element"): its unitCode is optional, but without
# it the unit is implied by absence (IND6). No default, as for Measures.
QUANTITY_UNITS = {
    "WorkReportLine/Quantity": "HUR",   # "the quantity of work": hours
    # goods: pieces of the line's item
    "InstructionForReturnsLine/Quantity": "H87", "InventoryReportLine/Quantity": "H87",
    "StockAvailabilityReportLine/Quantity": "H87", "SalesItem/Quantity": "H87",
    "ExceptionCriteriaLine/ThresholdQuantity": "H87",
}

# Optional children added to an aggregate type on purpose (UBL 2.5 chapter 4).
# PeriodType: both StartDate and EndDate. A period with only a start would be
# "open-ended" by absence of its end, which IND6 forbids.
# TransportMeansType ("a particular vehicle or vessel"): only the mode-specific
# aggregates identify the vehicle; road is the simplest (its required
# LicensePlateID follows from the schema).
FILL = {"PeriodType": {"cbc:StartDate", "cbc:EndDate"},
        "TransportMeansType": {"cac:RoadTransport"},
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
        # TenderingCriterionResponseType: nothing else says what is answered,
        # so both what (ValidatedCriterionPropertyID) and the answer
        # (ResponseValue). The answer is a neutral text placeholder, not an
        # Indicator: "true" would state a real answer; a later layer fills it.
        "TenderingCriterionResponseType": {"cbc:ValidatedCriterionPropertyID", "cac:ResponseValue"},
        "ResponseValueType": {"cbc:Response"},
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
# GLN is a Global *Location* Number: only for location-bound roles and GS1's
# own domains (catalogue data, CPFR/forecasting, retail, logistics). Generic
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
    "TransportServiceProviderParty": LEI,
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
    "ExporterParty": TAX, "HolderParty": TAX,
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
    """The scheme for a party's role; in Japanese documents the national
    Corporate Number takes D-U-N-S's place (it is how Japanese public and
    private buyers identify a business)."""
    r = role(party)
    s = SCHEMES.get(DOC + "/" + r, SCHEMES.get(r))
    if COUNTRY == "JP" and (s == DUNS or (s == LEI and r in ("ContractingParty", "SenderParty"))
                            or (s == TAX and r == "HolderParty")):
        return JPCN  # JP authorities and customs traders also have Corporate Numbers
    return s

# Identifier values: the scheme's own format and check digit, distinct per
# party in a document (n = 1, 2 ...), from official demonstration ranges where
# a scheme has one, and checked not to be real registrations where a public
# register can be queried (GLEIF, VIES, NTA; see the commit history).
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
ID_VALUES = {
    GLN: lambda k: _gs1("952000%06d" % k),   # GS1 Prefix 952: "for demonstrations and examples"
    LEI: lambda k: _lei("999900MINIMAL%05d" % k),   # not in GLEIF
    # D-U-N-S has a check digit (ICD 0060: "eight digits and a check digit"),
    # but D&B publishes neither the algorithm nor a test range: UNVERIFIED.
    DUNS: lambda k: "99%07d" % k,
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
# Official names: EU Directive 2006/112/EC "value added tax"; ZA "Value-Added Tax
# Act"; the EIN is the federal income tax identifier; the CNPJ is used for all
# federal taxes, so for BR it goes in PartyLegalEntity (the register).
TAX_NAMES = {"US": "Federal income tax", "DE": "Value added tax", "JP": "Consumption tax",
             "IN": "Goods and Services Tax", "ZA": "Value-Added Tax"}

# Party names: "example" + the role, in the locale's language and in Latin
# script (Japanese in Hepburn romanization), + the party's number k as in its
# identifier; no legal form (that would claim a registration). The language is
# stated in languageID (IND6). Translations: not reviewed by native speakers.
LANG = {"US": "en", "IN": "en", "ZA": "en", "DE": "de", "BR": "pt", "JP": "ja-Latn"}
EXAMPLE = {"en": "Example", "de": "Beispiel", "pt": "Exemplo", "ja-Latn": "Mihon"}
ROLE_NAMES = {  # role: (en, de, pt, ja-Latn)
    "AccountingSupplierParty": ("Supplier", "Lieferant", "Fornecedor", "Kyōkyūsha"),
    "AccountingCustomerParty": ("Customer", "Kunde", "Cliente", "Kokyaku"),
    "SellerSupplierParty": ("Seller", "Verkäufer", "Vendedor", "Hanbaisha"),
    "BuyerCustomerParty": ("Buyer", "Käufer", "Comprador", "Kōnyūsha"),
    "DespatchSupplierParty": ("Shipper", "Versender", "Expedidor", "Shukkasha"),
    "DeliveryCustomerParty": ("Consignee", "Warenempfänger", "Destinatário", "Uketorinin"),
    "RetailerCustomerParty": ("Retailer", "Einzelhändler", "Varejista", "Kourigyōsha"),
    "InventoryReportingParty": ("Inventory Reporter", "Bestandsmelder", "Informante de Estoque", "Zaiko Hōkokusha"),
    "ProviderParty": ("Provider", "Anbieter", "Provedor", "Teikyōsha"),
    "SenderParty": ("Sender", "Absender", "Remetente", "Sōshinsha"),
    "ReceiverParty": ("Receiver", "Empfänger", "Receptor", "Jushinsha"),
    "RequestorParty": ("Requester", "Anfragender", "Solicitante", "Iraisha"),
    "ResponderParty": ("Responder", "Antwortender", "Respondente", "Kaitōsha"),
    "ParticipantParty": ("Participant", "Teilnehmer", "Participante", "Sankasha"),
    "TransportServiceProviderParty": ("Carrier", "Frachtführer", "Transportador", "Unsō Gyōsha"),
    "SendingLogisticsOperatorParty": ("Logistics Operator", "Logistikdienstleister", "Operador Logístico", "Butsuryū Gyōsha"),
    "ReporterParty": ("Reporter", "Berichterstatter", "Relator", "Hōkokusha"),
    "ContractingParty": ("Contracting Authority", "Öffentlicher Auftraggeber", "Órgão Contratante", "Hatchū Kikan"),
    "EconomicOperatorParty": ("Economic Operator", "Wirtschaftsteilnehmer", "Operador Econômico", "Jigyōsha"),
    "TendererParty": ("Tenderer", "Bieter", "Licitante", "Nyūsatsusha"),
    "MainQualifyingParty": ("Main Tenderer", "Hauptbieter", "Licitante Principal", "Shu Nyūsatsusha"),
    "InterestedParty": ("Depositor", "Hinterleger", "Depositante", "Kitakusha"),
    "GuarantorParty": ("Guarantor", "Bürge", "Garantidor", "Hoshōnin"),
    "BusinessParty": ("Business", "Unternehmen", "Empresa", "Kigyō"),
    "ExporterParty": ("Exporter", "Ausführer", "Exportador", "Yushutsusha"),
    "HolderParty": ("Holder", "Inhaber", "Titular", "Shojisha"),
    "NotifierParty": ("Notifier", "Notifizierender", "Notificante", "Tsūchisha"),
    "WasteProducerParty": ("Waste Producer", "Abfallerzeuger", "Gerador de Resíduos", "Haikibutsu Haishutsusha"),
    "CustomsParty": ("Customs", "Zollbehörde", "Alfândega", "Zeikan"),
    "ImportingGuarantorParty": ("Importing Guarantor", "Einfuhrbürge", "Garantidor de Importação", "Yunyū Hoshōnin"),
    "ExportingGuarantorParty": ("Exporting Guarantor", "Ausfuhrbürge", "Garantidor de Exportação", "Yushutsu Hoshōnin"),
    "IssuerParty": ("Issuer", "Aussteller", "Emissor", "Hakkōsha"),
    "EndorserParty": ("Endorser", "Beglaubiger", "Endossante", "Shōmeisha"),
    "PreparationParty": ("Preparer", "Ersteller", "Preparador", "Sakuseisha"),
}
LANG_INDEX = {"en": 0, "de": 1, "pt": 2, "ja-Latn": 3}

# Texts in the locale's language, Latin script, with languageID; key
# "Parent/Element" or "Element". Not listed: stays X (e.g. the criterion
# answer, which waits for a real criterion). Not reviewed by native speakers.
TEXTS = {  # (en, de, pt, ja-Latn)
    "Item/Description": ("Ballpoint pen, blue", "Kugelschreiber, blau", "Caneta esferográfica azul", "Bōrupen, ao"),
    "SupplyItem/Description": ("Ballpoint pen, blue", "Kugelschreiber, blau", "Caneta esferográfica azul", "Bōrupen, ao"),
    "CancellationNote": ("Ordered in error", "Irrtümlich bestellt", "Pedido feito por engano", "Ayamatte chūmon"),
    "CertificateType": ("Ordinary", "Gewöhnlich", "Comum", "Ippan"),   # from the definition's examples
    "ApprovalStatus": ("Approved", "Genehmigt", "Aprovado", "Shōnin-zumi"),
    "DigitalProcess/Description": ("Ordering", "Bestellung", "Pedido", "Hatchū"),
}

NAMES = {  # (en, de, pt, ja-Latn); visibly fictitious
    "SignatoryContact/Name": ("Alex Example", "Alex Beispiel", "Alex Exemplo", "Mihon Tarō"),
    "ActivityOriginLocation/Name": ("Example Store 1", "Beispiel Filiale 1", "Exemplo Loja 1", "Mihon Tenpo 1"),
    "ProcurementProject/Name": ("Office supplies 2026", "Büromaterial 2026", "Material de escritório 2026", "Jimu Yōhin 2026"),
}

def name_for(e, parent, name):
    t = NAMES.get(etree.QName(parent).localname + "/" + name)
    if t is None:
        return VALUES["NameType"]
    lang = LANG[COUNTRY]
    e.set("languageID", lang)
    return t[LANG_INDEX[lang]]

def text_for(e, parent, name):
    pn = etree.QName(parent).localname
    t = TEXTS.get(pn + "/" + name) or TEXTS.get(name)
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

schemas = {}  # targetNamespace -> list of schema roots
for f in glob.glob(os.path.join(xsd_dir, "common", "*.xsd")) + glob.glob(os.path.join(xsd_dir, "maindoc", "*.xsd")):
    r = etree.parse(f).getroot()
    schemas.setdefault(r.get("targetNamespace"), []).append(r)

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
                                               or p.get("ref") in party_extra(e, t)):
                    ns, name = qname(p, p.get("ref"))
                    build(e, find("element", ns, name))
                elif p.tag in (X + "sequence", X + "choice", X + "any") and p.get("minOccurs", "1") != "0":
                    raise NotImplementedError(p.tag)

def generate(layer, fill, schemes):
    global FILL, SCHEMES, DOC
    FILL, SCHEMES = fill, schemes
    out = os.path.join(HERE, layer)
    os.makedirs(os.path.join(out, "deprecated"), exist_ok=True)
    global COUNTRY
    written = []
    for f in sorted(glob.glob(os.path.join(xsd_dir, "maindoc", "UBL-*-2.5.xsd"))):
        r = etree.parse(f).getroot()
        ns = r.get("targetNamespace")
        root_decl = r.find(X + "element")
        name = DOC = root_decl.get("name")
        currency, COUNTRY = LOCALES[len(written) % len(LOCALES)]
        global IDS
        IDS = {}
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
            nm.text = "%s %s %d" % (EXAMPLE[lang], ROLE_NAMES[role(party)][LANG_INDEX[lang]], k)
            nm.set("languageID", lang)
            pid = party.find("{%s}PartyIdentification/{%s}ID" % (CAC, CBC))
            if pid is not None:
                s = scheme_for(party)
                pid.set("schemeID", s)
                pid.text = ID_VALUES[s](k)
            ple = party.find("{%s}PartyLegalEntity" % CAC)
            if ple is not None:
                ple.find("{%s}CompanyID" % CBC).text = TAX_VALUES[COUNTRY](k)
                ple.find("{%s}CorporateRegistrationScheme/{%s}Name" % (CAC, CBC)).text = \
                    "Cadastro Nacional da Pessoa Jurídica"
            pts = party.find("{%s}PartyTaxScheme" % CAC)
            if pts is not None:
                pts.find("{%s}CompanyID" % CBC).text = TAX_VALUES[COUNTRY](k)
                pts.find("{%s}TaxScheme/{%s}Name" % (CAC, CBC)).text = TAX_NAMES[COUNTRY]
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
        for e in doc.iter():
            if e.text == CUR: e.text = currency
            if e.text == CTRY: e.text = COUNTRY
            if e.get("currencyID") == CUR: e.set("currencyID", currency)
        path = os.path.join(out, "" if os.path.basename(f) in endorsed else "deprecated", name + ".xml")
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
    return os.path.join(xsd_dir, "maindoc", "UBL-%s-2.5.xsd" % name)

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
