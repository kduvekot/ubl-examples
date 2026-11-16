# Review of the structure of minimal/ (layer0, layer1)

## Reviewed version

- Repository `kduvekot/ubl-examples`, branch `claude/elegant-franklin-kk2dky`, commit `01f8672db560e38bf39ff4e0388672c1298a2f4f` ("minimal: findings on UBL 2.5 definitions, for the OASIS UBL TC").
- 202 documents: `minimal/layer0/` and `minimal/layer1/`, each with 93 endorsed documents and 8 in `deprecated/`.
- Generator `minimal/gen_minimal.py` (869 lines). Line numbers below refer to this version.
- Standard: UBL 2.5 OASIS Standard, local package `minimal/.ubl/os-UBL-2.5/`. That covers `xsd/` (normative runtime schemas), `endorsed/xsd/`, `val/` (Saxon 9 HE and `UBL-DefaultDTQ-2.5.xsl`) and `UBL-2.5.html` (chapters 3.4, 4, 5 and 7.2 quoted from it).

### How it was checked

None of this uses the generator's `check()`. Scripts are in `/tmp/claude-0/-home-user-ubl-examples/cf0e0c4e-4ca5-5fb4-92ba-ea1bf0fe6f57/scratchpad/review1/`.

- `walk.py` walks every instance element against its type's content model in `xsd/`. It reports each optional child that is present, and any required child that is missing.
- `xmllint --schema` validates every document against `xsd/maindoc/UBL-<Doc>-2.5.xsd`. The 93 endorsed documents are also validated against `endorsed/xsd/maindoc/`.
- Saxon with `val/UBL-DefaultDTQ-2.5.xsl` runs once per file (phase 2).
- `ind.py` checks IND2, IND3, IND5 and IND9. It also looks for null-like tokens, whitespace-padded values, mixed content, `xsi:nil`, comments and PIs.
- `dtcheck.py` checks that every Text/Name has a languageID, every Quantity/Measure a unitCode and every Time an offset. It also counts amounts per document.
- `dupids.py` lists identifier values that occur in more than one document.
- `diffl.py` checks that layer1 equals layer0 plus the party identification, compared after c14n.
- Every XPath value quoted below was read with `xmllint --xpath`.

## Findings

### ST#F1 · High · DebitNote is filed as endorsed but fails the endorsed schema: LegalMonetaryTotal is missing

- **Where:** `layer0/DebitNote.xml` and `layer1/DebitNote.xml`.
  - `count(/DebitNote/cac:LegalMonetaryTotal)` = `0`.
  - The only amount is `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `100` (`currencyID="ZAR"`).
  - `xmllint --schema endorsed/xsd/maindoc/UBL-DebitNote-2.5.xsd layer1/DebitNote.xml` reports: "Element 'cac:DebitNoteLine': This element is not expected. Expected is one of ( cac:AccountingCustomerParty, … cac:PaymentTerms )" and "fails to validate". The layer0 file fails the same way.
  - The other 92 endorsed documents per layer pass the endorsed schemas.
- **Why:**
  - In `xsd/maindoc/UBL-DebitNote-2.5.xsd:1047`, `cac:LegalMonetaryTotal` is `minOccurs="0"`, but it is annotated `<ccts:EndorsedCardinality>1</ccts:EndorsedCardinality>` with the rationale "Required to indicate the total debit amount."
  - Its sibling `cac:RequestedMonetaryTotal` (l. 1028) has EndorsedCardinality `0`: "Use LegalMonetaryTotal to represent the total legal monetary impact of the Debit Note instead."
  - `endorsed/xsd/maindoc/UBL-DebitNote-2.5.xsd:990` has `minOccurs="1"`.
  - UBL 2.5 §5: "Deprecation applies to: … Element cardinalities". §3.4: endorsed schemas "may be used for validation or tooling purposes to ensure that a UBL instance does not include deprecated content."
  - So the endorsed DebitNote relies on a deprecated cardinality. IND1 still holds, because §3.4 says the endorsed schemas' "use is optional and does not affect conformance". But the folder split (`gen_minimal.py:757`, endorsed vs `deprecated/`) promises documents without deprecated content.
  - This is the only place where an endorsed cardinality raises a minOccurs. A diff of every particle in `xsd/` against `endorsed/xsd/` finds only this one. The other five changes only lower maxOccurs (PartyIdentification, PartyName, PeriodType/DescriptionCode, ElectronicPaymentUsageIndicator, OpenTenderEvent), and the documents respect them.
- **Why the checker misses it:**
  - `generate()` builds every document from `xsd/maindoc` (l. 688).
  - `check()` validates only against `xsd_for()` = `xsd/maindoc` (l. 844–849).
  - `python3 minimal/gen_minimal.py --check layer0/DebitNote.xml layer1/DebitNote.xml` reports "2 documents, 0 with violations".
- **Condition:** every document outside `deprecated/` validates against `endorsed/xsd/maindoc/UBL-<Doc>-2.5.xsd`.
- **Options:**
  1. Walk `endorsed/xsd` for endorsed document types and `xsd/` for deprecated ones, and validate each against the schema it was built from. This also enforces endorsed maxOccurs automatically. With that, DebitNote gains `cac:LegalMonetaryTotal/cbc:PayableAmount` (the only required child of MonetaryTotal).
  2. Add DebitNote's `cac:LegalMonetaryTotal` to FILL, and add an endorsed-schema validation to `check()`.

  Either way, the VALUES comment (l. 47–52, "Every document has one amount") must allow the DebitNote's second amount, which follows the comment's own "total = sum of lines" rule: PayableAmount 100 = LineExtensionAmount 100.
- **Needs decision:** no. It is a fix to apply; option 1 is the general one.

### ST#F2 · Medium · Reference identifiers repeat across unrelated documents, against the "values are unique across the set" decision

- **Where:** `dupids.py` over `layer1/` (layer0 is the same). Each value below occurs in more than one document:
  - `ContractFolderID-1` in 13 procurement documents, e.g.:
    - `layer1/CallForTenders.xml:/CallForTenders/cbc:ContractFolderID`
    - `layer1/Tender.xml:/Tender/cbc:ContractFolderID`
    - `layer1/TenderReceipt.xml:/TenderReceipt/cbc:ContractFolderID`
    - `layer1/AwardedNotification.xml:/AwardedNotification/cbc:ContractFolderID`

    The contracting authority differs in each of them, e.g. CallForTenders `0199` `999900MINIMAL0006105`, ContractNotice `999900MINIMAL0015126`.
  - `Shipment-1` in 11 documents (`…/cac:Shipment/cbc:ID`, e.g. `layer1/Waybill.xml`, `layer1/GoodsItemPassport.xml`, `layer1/deprecated/FreightInvoice.xml`).
  - `OrderReference-1` in 4 documents: `/OrderCancellation/cac:OrderReference/cbc:ID`, `/OrderChange/…`, `/OrderResponse/…` and `deprecated/OrderResponseSimple`. Each has a different buyer and seller.
  - `GoodsItemPassportCounterfoil-1` in GoodsItemPassport, ProofOfReexportation and ProofOfReexportationReminder (`/*/cac:GoodsItemPassportCounterfoil/cbc:ID`).
  - Two documents each:
    - `Consignment-1` (TransportExecutionPlan, TransportExecutionPlanRequest)
    - `LicensePlateID-1` (TransportProgressStatus, TransportProgressStatusRequest)
    - `RelatedCatalogueReference-1` (CatalogueItemSpecificationUpdate, CataloguePricingUpdate)
    - `DocumentReference-1` (InvoiceStatusResponse, ProofOfReexportation)
    - `ParentDocumentReference-1` (UtilityStatement, deprecated/EnquiryResponse)
  - Also the name of a particular thing: `/*/cac:ProcurementProject/cbc:Name` = `Office supplies 2026` in both CallForTenders and ContractNotice, with the same ContractFolderID.
  - Line IDs `1`, VersionID `1` and SequenceNumberID `1` repeat by design ("local by convention", l. 116–117). They are not counted here.
- **Why:**
  - The docstring (l. 15–16) says "The documents are unrelated to each other: values are unique across the set, and references point outside it." Party values follow this (k = position × 10 + n; no duplicates found).
  - Reference IDs do not. `generate()` resets the counter per document (`IDS = {}`, l. 694–695), so `id_for()` (l. 129–131) restarts each label at 1 in every document.
  - The FILL reason for ShipmentType (l. 240–243) calls the ID "a transaction reference like the document's own ID", but unlike the document's own ID it is not unique.
  - Read together, the documents relate to each other:
    - three documents cancel, change and respond to one order `OrderReference-1`, between different parties;
    - 13 procurement documents belong to one procedure (`ContractFolderID`: "An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs") run by 13 different contracting authorities;
    - two status documents are about the same vehicle.

    That contradicts the decision and the parties in the same documents. (PH#F9 offered "one shared value … if they are meant to be one procedure"; the decision taken since is that documents are unrelated.)
- **Condition:** every identifier value, except line, sequence and version IDs that are local by convention, and the in-document reference `ValidatedCriterionPropertyID` → `TenderingCriterionProperty/ID`, occurs in exactly one document of a layer. Every name of a particular thing (project, location, person) occurs in one document only.
- **Options:**
  1. Keep `IDS` across documents within a layer: create it once per `generate()` call, not per document. This gives `OrderReference-1` … `-4` and `ContractFolderID-1` … `-13`. The values stay the same in layer0 and layer1, because the documents are generated in the same order.
  2. Number by the document's position, as party values do (e.g. `OrderReference-49`).
  3. Make ProcurementProject/Name distinct per document, e.g. by numbering it as party names are.
- **Needs decision:** no. The decision exists; it needs applying.

### ST#F3 · Low · Licence plate without its registering country, while tax numbers state theirs (IND6 applied inconsistently)

- **Where:**
  - `layer1/TransportProgressStatus.xml:/TransportProgressStatus/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `LicensePlateID-1`. Locale JP: IssueTime `09:30:00+09:00`.
  - The same in `layer1/TransportProgressStatusRequest.xml` (locale IN, `+05:30`).
  - `count(//cac:TransportMeans/cbc:RegistrationNationalityID | //cac:TransportMeans/cbc:RegistrationNationality)` = `0` in both. Layer0 is the same.
- **Why:**
  - FILL (l. 216–218) adds RoadTransport because "only the mode-specific aggregates identify the vehicle". But a licence plate identifies a vehicle only within the country that registered it.
  - UBL provides `TransportMeans/cbc:RegistrationNationalityID`: "An identifier for the country in which this means of transport is registered."
  - LAYER1 makes the same point for tax numbers: "the jurisdiction is stated, not implied by the number's format (IND6)" (l. 546–547, `AddressType@JurisdictionRegionAddress: cac:Country`).
  - Nothing else in these two documents names a country, so the plate's jurisdiction is implied by absence. IND6: "The absence of a construct or data in a UBL instance document SHALL NOT carry meaning."
- **Condition:** every nationally issued identifier in the set states its jurisdiction, or the set says why it doesn't need to.
- **Options:**
  1. Add `cbc:RegistrationNationalityID` to FILL for TransportMeansType, with the locale's ISO 3166-1 alpha-2 code. This is one element, but it is an Identifier: it needs a schemeID decision, or none, as with `Country/IdentificationCode`.
  2. Add `cbc:RegistrationNationality` (Text, with languageID). It needs no scheme, but it is less exact.
  3. Record why a plate is exempt.
- **Needs decision:** yes (option 1 needs a schemeID choice).

### ST#F4 · Low · Stale and misplaced reasons in the generator's comments

The generator's comments are the decision record, so they must match the code.

- **Where and why:**
  1. `gen_minimal.py:277–281` (FILL, TenderingCriterionResponseType) says: "The answer is a neutral text placeholder, not an Indicator: 'true' would state a real answer; a later layer fills it."
     - The next line (l. 282) adds `ResponseValueType: {cbc:ResponseIndicator}`, and `INDICATOR_VALUES["ResponseIndicator"] = "true"` (l. 65).
     - The document has `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseIndicator` = `true`.
     - The comment contradicts the code (changed in a510807).
  2. `gen_minimal.py:265–268` (FILL, ResponseType) says: "Its code list is left to the code-list layer, like the other required codes."
     - The code is now chosen: `CODE_VALUES["ResponseCode"] = "ACCEPTED"` (l. 174).
     - By decision it has no listID and no later code-list layer.
  3. `gen_minimal.py:162` says "(others stay X until a code-list layer)", and `gen_minimal.py:497–499` (TEXTS) says "Not listed: stays X (e.g. the criterion answer, which waits for a real criterion)".
     - No `X` remains in any of the 202 documents (verified).
     - The criterion answer is no longer a text.
  4. `gen_minimal.py:181–186`: the reason for TransportServiceCode ("the extent of this transportation service (e.g., door-to-door, port-to-port)": a segment … the whole service) runs straight into the reason for SupplyChainActivityTypeCode ("values listed for the same element elsewhere in UBL …").
     - Both sit above `"SupplyChainActivityTypeCode": "SALES"`.
     - The two TransportServiceCode entries are at l. 196–197, away from their reason.
- **Condition:** every comment states the reason for the value or element that follows it, as it is now.
- **Options:** rewrite the four comments. For 1, e.g. "the answer is an Indicator, true, to the yes/no property in the same document (QualificationApplicationResponseType)". Move the TransportServiceCode reason to l. 196.
- **Needs decision:** no.

### ST#F5 · Low · The checker cannot catch null-like values, and the generator still has `X` fallbacks

- **Where:**
  - `VALUES` (l. 53–55) keeps the defaults `"CodeType": "X"`, `"IdentifierType": "X"`, `"TextType": "X"` and `"NameType": "X"`.
  - `text_for()` and `name_for()` fall back to them when an element has no TEXTS or NAMES entry (l. 520–535). `build()` falls back to `VALUES["CodeType"]` for codes (l. 615–616).
  - `check()` tests IND5 only as "no children and no non-blank text" (l. 802), and IND9 only as "blank" (l. 805).
  - Today no document contains `X` or any other null-like token: `ind.py` tested X, N/A, null, nil, none, -, 0, ?, TBD, unknown, test, dummy and placeholder.
- **Why:**
  - IND5 forbids elements "devoid of content or containing null values", and IND9 forbids the same for attributes.
  - `X` is exactly the placeholder the earlier review removed (PH#F12, PH#F14, PH#F18).
  - The docstring (l. 14–15) promises "A value type with no rule and no default stops the build", but for Code, Text and Name there is still a default. A later layer that adds a new text, name or code would silently emit `X`, and the checker would pass it.
- **Condition:** a value with no rule stops the build, or `check()` rejects it.
- **Options:**
  1. Remove the four `X` defaults so `KeyError` stops the build, as for Measures and Indicators. `IdentifierType` `X` is already unreachable, because `id_for()` always returns a value.
  2. Keep them, but have `check()` report any element or attribute whose value equals a VALUES placeholder.
- **Needs decision:** no.

### ST#F6 · Low · Lines and documents that consist only of their identifier

- **Where (layer1; layer0 is the same):**
  - `count(/CreditNote/cac:CreditNoteLine/*)` = `1`: only `cbc:ID` = `1`. The same in SelfBilledCreditNote, ReminderLine, StatementLine, RemittanceAdviceLine and CataloguePricingUpdateLine.
  - `/Forecast/cac:ForecastLine` has only ID and `ForecastTypeCode` = `TOTAL`: no item, no quantity.
  - `count(/ApplicationResponse/cac:DocumentResponse)` = `0`.
  - `/DocumentStatus` has only ID and IssueDate. So do TransportationStatus, TransportationStatusRequest, TransportServiceDescription and BillOfLading, each with only `cbc:ID`.
- **Why:**
  - These are schema-minimal, and they meet IND5: each container has a constituent.
  - FILL's own rule for optional containers goes further. It picks the child that says *what the thing is*: PartyName ("who it is"), RoadTransport ("identify the vehicle"), Item/Description.
  - For containers the schema already fills with a line number, that rule is not applied, so a line states its position but not its subject.
  - §7.2 asks that "the instance conveys information that is consistent with the business semantics intended by the UBL data model".
  - A credit note line with neither an item nor an amount, or a forecast line without an item, could be read as "all items" or "the whole amount". That would be meaning by absence (IND6).
- **Condition:** either layer 0 states that it is schema-minimal and makes no §7.2 claim for content-free lines, or each line and response states its subject. Examples: CreditNoteLine with `cac:Item/cbc:Description`, as InvoiceLine has; ForecastLine with `cac:SalesItem`.
- **Options:**
  1. Document this as the layer's scope, with no change.
  2. Extend FILL per line type, choosing the minimal subject: Item/Description where the line has an Item, SalesItem for forecast lines.
  3. Leave it for a "lines" layer.
- **Needs decision:** yes.

## Checked and consistent

- **Optional elements present are exactly the intended ones.** In both layers, every optional child present (minOccurs 0 in `xsd/`) is in FILL, in LAYER1 or in `party_extra()`, and every entry of these tables occurs at least once:
  - layer0: 27 (type, child) pairs;
  - layer1: those 27 plus AddressType/Country, CorporateRegistrationScheme Name and JurisdictionRegionAddress, PartyLegalEntity CompanyID and CorporateRegistrationScheme, PartyTaxScheme/CompanyID, Party PartyIdentification, PartyTaxScheme and PartyLegalEntity, and TaxScheme Name and JurisdictionRegionAddress.
- **No required element is missing:** `walk.py` found none, and xmllint validates all 202 documents against `xsd/`.
- **No sibling repeats at all**, so endorsed maxOccurs 0..1 for PartyName and PartyIdentification is respected.
- **Layer1 = layer0 + party identification:** after removing PartyIdentification, PartyTaxScheme and PartyLegalEntity, all 101 layer1 documents are c14n-identical to layer0.
- **IND1:** all 202 are valid against the full schemas. The 93 endorsed documents pass `endorsed/xsd` except DebitNote (ST#F1). The 8 deprecated document types have no endorsed schema, as expected.
- **Phase 2 (§F):** Saxon `UBL-DefaultDTQ-2.5.xsl` gives 0 failed assertions on 202 files (76 fired rules: currencyID, unitCode, mimeCode, country and currency codes).
- **IND2 / IND3:** every file starts with exactly `<?xml version="1.0" encoding="UTF-8"?>`, with no BOM, valid UTF-8 and no CR.
- **IND5:**
  - no empty element;
  - no whitespace-only or padded value;
  - no mixed content, no `xsi:nil`, no comments or PIs;
  - no null-like token;
  - no `X` left.
- **IND7 / IND8:** there are no repeated sibling Text/Name elements, so both hold trivially. Every Text/Name element carries a languageID. A flagged `Response` was the aggregate `cac:Response`, not `cbc:Response`.
- **IND9:** no empty, padded or null-like attribute.
- **IND6 proxies:**
  - every Quantity and Measure has a unitCode;
  - every Time has a UTC offset;
  - every Period has both StartDate and EndDate;
  - every Text and Name states its language;
  - tax and registration schemes state their country (except the licence plate, ST#F3).
- **"One amount, no tax":** 22 documents have exactly one Amount element each.
- **FILL reasons checked against the definitions and found sound and minimal:**
  - Party wrappers: Party ("the … Party itself");
  - PartyType: PartyName (a name needs no scheme);
  - ItemType: Description ("Text describing this item"; Name is "optionally given");
  - Shipment: ID (the minimal single child, apart from the uniqueness issue in ST#F2);
  - ProcurementProject: Name;
  - DigitalProcess: Description (the ID definition is wrong, ubl-findings F2);
  - SignatoryContact: Name;
  - IssuingCountry: IdentificationCode;
  - BillingReference: InvoiceDocumentReference;
  - Response: ResponseCode ("the type of response");
  - ActivityOriginLocation: Name;
  - ReexportationEvidence: DocumentReference;
  - TenderedProject: LegalMonetaryTotal ("The total amount for this tendered project");
  - Attachment: EmbeddedDocumentBinaryObject (with a real PDF and the required mimeCode);
  - the criterion chain TenderingCriterion → PropertyGroup → Property (ID, Description), answered by ValidatedCriterionPropertyID + ResponseValue/ResponseIndicator ("An indicator used as a reply to the criterion requirement").
- **LAYER1 structure:**
  - PartyTaxScheme with CompanyID and TaxScheme (Name, JurisdictionRegionAddress/Country);
  - PartyLegalEntity (BR only) with CompanyID and CorporateRegistrationScheme (Name, JurisdictionRegionAddress/Country);
  - PartyIdentification at most once per party;
  - party identifier and tax values unique across the set.

## Considered and refuted

- **CertificateOfOrigin, "Alex Example" signs for both endorsers:** `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty/cac:SignatoryContact/cbc:Name` and `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` are both `Alex Example`.
  - EndorserParty.SignatoryContact is defined as "The individual representing the exporter who signs the Certificate of Origin application …" in every context.
  - So by definition both signatories represent the one exporter, and one person is consistent. That the definition fits only one context is ubl-findings F3.
- **Tender without ProcurementProjectLot (IND6?):** the definition says "If there are no lots, this ought not be defined." So absence is the prescribed form, not implied meaning.
- **Dates without a zone while times have one:** a business date is the issuer's calendar date. Every document that has a time gives it with an offset, and no date is combined with a time in another zone.
- **Invoice / CreditNote / Reminder totals without line amounts:** this follows the explicit rule "Every document has one amount and no tax yet" (l. 47–52), applied to all 22 documents. The schema puts the one required amount at document level, except in DebitNote, where it sits at line level (and see ST#F1).
- **The same item description "Ballpoint pen, blue" in many documents:** ItemType describes a kind of item ("a generic description applicable to all examples"), not a particular thing, so the uniqueness decision does not apply.
- **TenderingCriterionProperty without TypeCode / ValueDataTypeCode:** TypeCode is "A mutually agreed code" with no UBL default list. The Description is a yes/no question and the answer is an Indicator, so nothing depends on their absence.
- **Deprecated elements in endorsed documents:** none. The endorsed schemas reject nothing but the DebitNote cardinality.
- **InvoiceStatusResponse names no document type:** the DocumentReference sits in a document whose type is defined for invoice status, and the definition of BillingReference / DocumentResponse needs no type code.

## Not verified

- Whether the OASIS UBL TC regards an instance that is valid only against the full schema, but omits an EndorsedCardinality-1 element, as "including deprecated content". §3.4 and §5 suggest so; the specification does not say it in those words.
- Whether readers would in practice infer "all items" or "the whole amount" from content-free lines (ST#F6). This is a judgement of risk, not a verified behaviour.
- The scheme a RegistrationNationalityID would need (ST#F3). Verified: neither `cva/` nor `val/UBL-DefaultDTQ-2.5.xsl` mentions RegistrationNationalityID, so UBL has no default list for it. Not verified: which external list (e.g. ISO 3166-1, or the UN distinguishing signs for vehicles) practice uses there.
- Translations and values (names, tax numbers, ICDs) are out of scope for this structural review. See the layer-1 and placeholder reviews.
