# Review of the structure of minimal/ (layer0, layer1), round 3

## Reviewed version

- Repository `kduvekot/ubl-examples`, branch `claude/elegant-franklin-kk2dky`, commit `6f3c96249f32ccee9c469666e3a3e4db6ccca635` ("minimal: UtilityStatement shows its consumption (DM#F116)").
- Focus: the changes since `01f8672` (round 2), 40 commits; regressions checked against the round-2 structure review (`structure.llm-review.20261116T1422Z-minimal.md`, ST#F1–F6).
- 202 documents: `minimal/layer0/` and `minimal/layer1/`, each 93 endorsed + 8 in `deprecated/`.
- Generator `minimal/gen_minimal.py` (1158 lines). Line numbers refer to this version.
- Standard: UBL 2.5 OASIS Standard, local package `minimal/.ubl/os-UBL-2.5/` (`xsd/`, `endorsed/xsd/`, `val/` with Saxon 9 HE and `UBL-DefaultDTQ-2.5.xsl`, `UBL-2.5.html` §4 quoted from it).

### How it was checked

Independently of the generator's `check()`. Scripts are in `/tmp/claude-0/-home-user-ubl-examples/cf0e0c4e-4ca5-5fb4-92ba-ea1bf0fe6f57/scratchpad/round3/structure/`.

- `xmllint --schema` on every file: the 93 endorsed types of each layer against `endorsed/xsd/maindoc/UBL-<Doc>-2.5.xsd` **and** against `xsd/maindoc/`; the 8 deprecated types against `xsd/maindoc/` (none of them has an endorsed schema).
- Saxon `val/UBL-DefaultDTQ-2.5.xsl` over all 202 files (phase 2).
- `walk3.py`: walks every element against its type's content model, taken from `endorsed/xsd` for endorsed documents and from `xsd/` for deprecated ones. It reports missing required children, maxOccurs violations, any repeated sibling, and every optional child present.
- `fillcmp.py`: loads FILL, LAYER1 and REPEAT from the generator source (without running it) and compares them both ways with the optional children found by `walk3.py`, honouring the `Document:Type` and `Type@Role` keys.
- `ind.py` (IND2, IND3, IND5, IND9, null-like tokens, whitespace padding, mixed content, `xsi:*`, comments/PIs), `dtcheck.py` (languageID, unitCode, time offsets, amounts per document), `dupids.py` (identifier values in more than one document), `diffl.py` (layer1 = layer0 + party identification, after c14n).
- The generator was copied to the scratchpad (with a symlink to `.ubl`) and run there. Its output is byte-identical to the committed `layer0/` and `layer1/`, so the committed documents are what the generator now produces.
- `python3 minimal/gen_minimal.py --check` (read-only mode) on all 202 files: "202 documents, 0 with violations".
- Every XPath value quoted below was read with `xmllint --xpath`.

## Findings

### ST3#F1 · High · QualificationApplicationResponse answers a criterion property that does not exist (regression)

- **Where:** `layer0/QualificationApplicationResponse.xml` and `layer1/QualificationApplicationResponse.xml`.
  - `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `TenderingCriterionProperty-1`.
  - `/QualificationApplicationResponse/cac:TenderingCriterion/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:ID` = `TenderingCriterionProperty-631`.
  - `TenderingCriterionProperty-1` occurs in no document of either layer (`grep -r`). At 01f8672 both values were `TenderingCriterionProperty-1`.
- **Why:**
  - Commit 5664959 ("identifiers unique across the set … ST#F2") changed `id_for()` to number every label as `DOCNO * 10 + n` (l. 159–160). The property's own ID went from `-1` to `-631`, but the special case for the reference, `return "TenderingCriterionProperty-1"` (l. 154–155), stayed hard-coded.
  - The generator's own reason for the structure (l. 328–337) is that the answer refers to "the yes/no property repeated in the same document". The reference no longer points to it. The answer `ResponseIndicator` = `true` now answers no question in the document. This is the one reference that is meant to point inside its own document (the exception to "references point outside the set"), and it now points nowhere.
  - TenderingCriterionResponse/ValidatedCriterionPropertyID: "An identifier for this item of criterion support". TenderingCriterionProperty/ID: "An identifier to refer to the criterion property." The reference is the only thing that ties the answer to the question (§7.2 semantic conformance).
- **Why the checker misses it:** `check()` has no referential-integrity test. It cannot see that an in-document reference fails to resolve. The round-2 condition for ST#F2 named this exception explicitly ("and the in-document reference `ValidatedCriterionPropertyID` → `TenderingCriterionProperty/ID`").
- **Condition:** in every QualificationApplicationResponse, `cbc:ValidatedCriterionPropertyID` equals the `cbc:ID` of a `cac:TenderingCriterionProperty` in the same document.
- **Options:**
  1. In `id_for()`, return the same value as the property ID: `"TenderingCriterionProperty-%d" % (DOCNO * 10 + 1)`. This works only while the property is built first and is the first of its label.
  2. Better: fill the reference after the build, from the property's ID, as is already done for the CertificateOfOrigin issuer's name (l. 1033–1038).
  3. Add a test to `check()`: every `ValidatedCriterionPropertyID` must resolve in its own document.
- **Needs decision:** no.

### ST3#F2 · Medium · DebitNoteLine says how much but not what, while CreditNoteLine got its Item for exactly that reason

- **Where:** `layer0/DebitNote.xml` and `layer1/DebitNote.xml`.
  - `count(/DebitNote/cac:DebitNoteLine/cac:Item)` = `0`. The line has only `cbc:ID` = `1` and `cbc:LineExtensionAmount` = `270.00` (`currencyID="ZAR"`).
  - In contrast: `/CreditNote/cac:CreditNoteLine/cac:Item/cbc:Description` = `Caneta esferográfica, azul`, and the same in SelfBilledCreditNote.
- **Why:**
  - The rule added since round 2 (FILL l. 396–404): "commercial documents say what they concern: … what is credited". It was applied to CreditNoteLineType (`{"cac:Item"}`, l. 404) and is recorded as UBL finding E33: "a credit line must say what is credited".
  - DebitNoteLineType gets nothing. DebitNoteLine/Item is 0..1 (`xsd/common/UBL-CommonAggregateComponents-2.5.xsd:13450`): "The item associated with this debit note line." So the debit note, like the credit note before the fix, states an amount and does not state what it is for.
  - AMOUNTS (l. 73) gives the DebitNote "ZAR 10 x 27.00", i.e. ten pens, but nothing in the document says so. A line amount without a subject leaves its subject to be implied (IND6: "The absence of a construct or data in a UBL instance document SHALL NOT carry meaning").
  - The two lines now mirror each other. The credit line has the item but no amount, and the debit line has the amount (required) but no item. The reminder, remittance and statement lines have both. The "what and how much" rule is applied three different ways.
- **Condition:** every line of a commercial document states its subject, by one rule. DebitNoteLine is the only one that still lacks it.
- **Options:**
  1. Add `"DebitNoteLineType": {"cac:Item"}` to FILL. Item/Description follows from ItemType's FILL entry. Then add the matching E-entry to `ubl-findings.md` (DebitNote, `cac:Item` (DebitNoteLine), 0..1).
  2. Record why a debit line needs no subject (e.g. that a debit note line is a pure amount adjustment), and say why the same does not hold for a credit line.
- **Needs decision:** no (option 1 applies the rule already taken).

### ST3#F3 · Medium · TransportProgressStatus names a location but reports no status there (IND6)

- **Where:** `layer0/TransportProgressStatus.xml` and `layer1/TransportProgressStatus.xml`.
  - `/TransportProgressStatus/cac:TransportSchedule` has exactly 2 children: `cbc:SequenceNumeric` = `1` and `cac:StatusLocation/cbc:Name` = `Sanpuru Tāminaru 1` (`languageID="ja-Latn-hepburn"`).
  - None of the six optional TransportEvent children (Actual/Estimated/Planned Arrival/Departure) is present, and no ReferenceDate, ReferenceTime or Remarks either.
- **Why:**
  - FILL (l. 416–417): "a progress status shows progress: the transport is at a terminal". Commit 4922d1d: "the StatusLocation reached".
  - But nothing in the document says *reached*. TransportSchedule/StatusLocation is only "The location for which status is reported". The status itself sits in the sibling events: ActualArrivalTransportEvent ("The actual arrival at a location"), EstimatedArrivalTransportEvent, and so on.
  - With only the location, a reader cannot tell whether the vehicle has arrived, has left, or is expected there. "Is at the terminal" is implied by the absence of the alternatives. That is what IND6 forbids, and the document still does not "show progress", which was the DM#F122 condition.
- **Condition:** the TransportSchedule entry states a status at its StatusLocation, not only the location.
- **Options:**
  1. Add `cac:ActualArrivalTransportEvent` to FILL for TransportScheduleType, with one constituent, because TransportEventType has no required child and IND5 forbids an empty container. The minimal one is `cbc:OccurrenceDate` (D), plus `cbc:OccurrenceTime` (09:30 + offset) if the time matters.
  2. Use `cbc:ReferenceDate` / `cbc:ReferenceTime` ("The reference date for the transport schedule status"). This is weaker, because it dates the status without saying what it is.
  3. Record that a StatusLocation alone means "current location". This needs a source, because the UBL definition does not say it.
- **Needs decision:** yes (which event, and whether a time is needed).

### ST3#F4 · Low · RegistrationNationalityID holds an ISO 3166-1 code with no scheme stated

- **Where:**
  - `layer1/TransportProgressStatus.xml:/TransportProgressStatus/cac:TransportMeans/cbc:RegistrationNationalityID` = `JP`.
  - `layer1/TransportProgressStatusRequest.xml:…/cbc:RegistrationNationalityID` = `IN`.
  - Neither has a `schemeID` (`//cbc:RegistrationNationalityID/@*` is empty). Layer0 is the same.
- **Why:**
  - This fixes ST#F3 (option 1, commit e84fbdc), but the schemeID decision that ST#F3 flagged ("it is an Identifier: it needs a schemeID decision, or none") is not recorded. The comment (l. 266–269) and `id_for()` (l. 150–151) say only "the vehicle's country".
  - The element is an Identifier ("An identifier for the country in which this means of transport is registered"). Neither `cva/` nor `UBL-DefaultDTQ-2.5.xsl` gives it a default list. That `JP` is an ISO 3166-1 alpha-2 code, and not, say, a UN distinguishing sign for vehicles (Japan is `J` there), follows only from the value's format.
  - The generator itself rejects that reasoning for tax numbers: "the jurisdiction is stated, not implied by the number's format (IND6)" (l. 798).
  - This is the only identifier in the set whose value is a code from an external list. The decision "codes without a UBL default list: descriptive values … no listID" covers codes, not identifiers that hold an external code.
- **Condition:** the scheme of RegistrationNationalityID is stated in the document, or the generator records why it is not needed.
- **Options:**
  1. Add a schemeID naming ISO 3166-1 alpha-2. UBL has no agreed scheme string for it, so the string itself must be chosen and recorded.
  2. Record next to l. 150 that, as with `Country/IdentificationCode`, the ISO 3166-1 alpha-2 code is assumed, with the reason why IND6 does not apply.
- **Needs decision:** yes.

### ST3#F5 · Low · Generator comments still stale or newly stale (ST#F4 partly not fixed)

The generator's comments are the decision record. Commit 17dd527 fixed ST#F4 items 1 and 4. Items 2 and 3 remain, and later commits made further comments stale.

- **Where and why:**
  1. l. 192: "Code values chosen per element (others stay X until a code-list layer)." This was ST#F4.3 and is still there. Since 4f6b7b1 an unchosen code is `@UNCHOSEN@` and `check()` rejects it (l. 46–50, 1090), so no code "stays X", and by decision there is no code-list layer.
  2. l. 316–319 (ResponseType): "only in InvoiceStatusResponse … Its code list is left to the code-list layer, like the other required codes." This was ST#F4.2 and is still there.
     - ResponseType/ResponseCode now also occurs in `/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode` and `/DocumentStatus/cac:DocumentResponse/cac:Response/cbc:ResponseCode` (both `ACCEPTED`).
     - The code is chosen without a listID (l. 200–204).
  3. l. 311 (BillingReferenceType): "only in InvoiceStatusRequest". It now also occurs in ReminderLine, RemittanceAdviceLine and StatementLine (`walk3.py`: 4 documents).
  4. l. 321 (LocationType): "only ActivityOriginLocation so far". It now also covers `/TransportProgressStatus/cac:TransportSchedule/cac:StatusLocation/cbc:Name` (4922d1d).
  5. l. 223–224 (UtilityStatementTypeCode): "a later layer with consumption must match (KWH)". Consumption is now in layer 0 (`/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `350`, `unitCode="KWH"`, 6f3c962).
  6. l. 719–723 (TEXTS): "terms added after that review … are not yet reviewed". Commits a7d89c5, 7a6c810 and d684198 ("round-2 translations by majority of three translators") have reviewed them since. The same holds for l. 665–666 ("checked against two independent human translations"), now a majority of three.
  7. l. 338–340: "Document level (IND6): optional elements that carry a document's defined purpose … Each is also a UBL finding (ubl-findings.md, 'essential but optional')". The block that follows includes entries with no E-number in `ubl-findings.md`: EnquiryType and EnquiryResponseType `cbc:Description`, OrderLineReferenceType `cac:OrderReference`, ReceiptLineType `cac:Item`, GoodsItemType `cac:Item`, ItemLocationQuantityType `cac:Price` and SubscriberConsumptionType `cbc:TotalMeteredQuantity`. Some of these are sub-elements of a listed entry (e.g. E24 GoodsItem, E42 RequiredItemLocationQuantity), and the Enquiry pair is deprecated. Either way, "each" is not true as written.
  8. l. 14 (docstring): "A value type with no rule and no default stops the build". For Code, Identifier, Text and Name the build now completes and writes `@UNCHOSEN@`, which `check()` then rejects (exit status 1). The effect is the same, but the wording describes the old mechanism.
- **Condition:** every comment states the reason for the value or element that follows it, as it is now.
- **Options:** rewrite items 1–8. For 7, either say "most are also UBL findings", or add the missing E-entries (or a note that sub-elements of an E-entry are covered by it).
- **Needs decision:** no.

## Checked and consistent

- **Round-2 findings fixed and not regressed:**
  - ST#F1: the generator now builds endorsed types from `endorsed/xsd` (l. 819–830, 961–963), and `xsd_for()` validates them against it. DebitNote has `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `270.00` = the line amount.
  - ST#F2: no identifier value except the local `1` (line, sequence and version IDs, and `LineID`/`RevisedForecastLineID` per VA#F9) occurs in more than one document of a layer (`dupids.py`). ProcurementProject/Name is distinct per document. The fix broke the one in-document reference (ST3#F1).
  - ST#F3: RegistrationNationalityID is present (see ST3#F4 for the scheme).
  - ST#F5: the `X` defaults are gone; `UNCHOSEN` is rejected by `check()`. No `@UNCHOSEN@` or `X` is in any document.
  - ST#F6: content-free lines now state their subject (CreditNoteLine Item, ForecastLine and ForecastRevisionLine SalesItem, Reminder, Remittance and Statement lines BillingReference + amount, ApplicationResponse and DocumentStatus DocumentResponse, and so on), except DebitNoteLine (ST3#F2).
- **IND1:** all 202 documents validate with xmllint, the 93 endorsed types of each layer against both `endorsed/xsd` and `xsd`, and the 8 deprecated types against `xsd`.
- **Phase 2:** Saxon `UBL-DefaultDTQ-2.5.xsl` gives 0 failed assertions on 202 files. Rules fired: country IdentificationCode, unitCode on quantities and measures, currencyID, currency codes, LineStatusCode and mimeCode.
- **Structure equals the generator's tables, both ways:**
  - Layer0: every optional child present is covered by a FILL key (plain, `Document:Type` or `Type@Role`), and every FILL entry occurs at least once. None of them is a child that is required anyway.
  - Layer1: the additional optional children are exactly LAYER1 plus the `party_extra()` choices: PartyIdentification, PartyTaxScheme, and PartyLegalEntity for BR TAX roles.
  - No required child is missing.
  - The only repeated sibling is `/DigitalAgreement/cac:ParticipantParty` (2), which is the one REPEAT entry. All endorsed maxOccurs restrictions (PartyName, PartyIdentification 0..1, etc.) hold.
- **Layer1 = layer0 + party identification:** all 101 pairs are c14n-identical after removing PartyIdentification, PartyTaxScheme and PartyLegalEntity.
- **No deprecated content:** no element whose definition starts "(Deprecated)" (85 in `xsd/`) occurs in any document, the 8 deprecated document types included.
- **IND2 / IND3:** every file starts with exactly `<?xml version="1.0" encoding="UTF-8"?>`, with no BOM, valid UTF-8 and no CR.
- **IND5 / IND9:** there is no empty element or attribute, and no whitespace-only or padded value. There is no mixed content, `xsi:*`, comment or PI. There is no null-like token (x, n/a, null, nil, none, -, 0, ?, tbd, unknown, test, dummy, placeholder, ".", `@UNCHOSEN@`).
- **IND7 / IND8:** no sibling Text/Name elements of the same name, so both hold trivially. Every Text/Name has a languageID. The `Response` hits in `dtcheck.py` are the aggregate `cac:Response`.
- **IND6 proxies:** every Quantity/Measure has a unitCode, every Time an offset, every Period both dates. Every amount has its currency, and amounts within a document agree:
  - Reminder 16.00 = line 16.00;
  - RemittanceAdvice TotalPaymentAmount 15.00 = line 15.00;
  - Statement TotalBalanceAmount 16.00 = line 16.00;
  - DebitNote 270.00 = line 270.00.
- **New FILL entries checked against their definitions and found sound and minimal:**
  - OriginAddress/Country (E25);
  - SubscriberConsumption + TotalMeteredQuantity (UtilityConsumptionPoint follows from the schema);
  - OperatingYearsQuantity;
  - WinningParty (only in ContractAwardNotice; AwardedNotification is addressed to the winner by definition);
  - ImporterParty;
  - GoodsCertificate/Description;
  - GoodsItem/Item for PackingList and the waste documents;
  - OrderLineReference/OrderReference;
  - LineItem/Quantity;
  - CataloguePricingUpdateLine → RequiredItemLocationQuantity → Price/PriceAmount (the line ID is "An identifier for the catalogue line to be updated", so no Item is needed: the type has none);
  - RetailEvent Description + IssueDate;
  - MainTransportationService;
  - ContractFolderID for the procurement messages;
  - the Enquiry/EnquiryResponse question and answer.
- **The `Document:Type` keys** (WeightStatement, CertificateOfOrigin, PackingList, WasteMovement and WasteNotification `ShipmentType`; OrderChange `LineItemType`; TendererQualification `QualifyingPartyType`; ContractAwardNotice `TenderResultType`) each hit only the document named. The `Type@Role` keys (`AddressType@OriginAddress`, `AddressType@JurisdictionRegionAddress`) hit only that role.
- **Reproducibility:** regenerating in the scratchpad gives byte-identical layer0 and layer1.

## Considered and refuted

- **UtilityStatement: 350 kWh without a consumption period.** SubscriberConsumption/Consumption/MainPeriod ("The period of consumption") is absent. But a UtilityStatement is "A supplement to an Invoice or Credit Note", and it has a ParentDocumentReference. The period is that of the parent bill, which is outside the set by decision, so it is not implied by absence. Adding Consumption would also bring its required LegalMonetaryTotal, which is more than minimal.
- **ItemInformationRequestLine/SalesItem/Quantity = 10 in a request.** It is required (SalesItem 1..n, Quantity 1..1: "The quantity the given information are related to"), so the schema forces it, not the generator. The definition makes it the reference quantity for the requested information, which is consistent.
- **ExportCustomsDeclaration without a Shipment, while Import and Transit have one.** ExportCustomsDeclarationType has no Shipment element. Its goods are reached through the required `cac:CustomsDeclaration`.
- **Reminder, RemittanceAdvice and Statement lines repeat the document total.** The line amount belongs to the referenced invoice. The total is defined for the whole document ("total = sum of lines", l. 52–55), so the total does not make the line amount redundant.
- **Quotation, RequestForQuotation, OrderChange, Enquiry, EnquiryResponse and PriorInformationNotice have no document ID.** ID is optional in these types, and no definition makes the document's own identifier part of its purpose. References point outside the set, so nothing has to refer to them.
- **TransportProgressStatus StatusLocation is named, not identified.** This is consistent with the LocationType rule (one particular place gets a name; an ID would need a scheme).

## Not verified

- Whether the OASIS UBL TC would read a TransportSchedule with only a StatusLocation as "currently at" (ST3#F3). The definitions do not say so, and no UBL sample was found that settles it.
- Which scheme identifier practice uses for RegistrationNationalityID (ST3#F4). Verified only: UBL has no default list for it (`cva/` and `UBL-DefaultDTQ-2.5.xsl` do not mention it), and the UN distinguishing sign for Japan is `J` (domain knowledge, not checked against the UNECE register).
- Values, translations and party identifiers are outside this structural review.
