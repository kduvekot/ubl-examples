# Review of document meaning, round 3: minimal/layer1 P to Z and deprecated/

## Reviewed version

- Run: `20261116T1711Z-round3`
- Source: branch `claude/elegant-franklin-kk2dky`, commit `6f3c96249f32ccee9c469666e3a3e4db6ccca635`. In scope: the 49 files `minimal/layer1/[P-Z]*.xml` (PackingList ... WorkReport) and the 8 files `minimal/layer1/deprecated/*.xml`, plus the parts of `minimal/gen_minimal.py` (1158 lines) that produce them.
- Baseline: round 2 (`meaning-p-z.llm-review.20261116T1418Z-minimal.md`, commit `01f8672`). I read `git diff 01f8672..6f3c962 -- minimal/` for every file in scope and the commits that made the changes.
- Model: UBL 2.5 OASIS Standard at `minimal/.ubl/os-UBL-2.5/`. Document definitions are the `ccts:Definition` of each root element in `xsd/maindoc/UBL-<Doc>-2.5.xsd`. Child definitions come from `xsd/common/UBL-CommonAggregateComponents-2.5.xsd`. For comparison I also used the OASIS sample `xml/UBL-RemittanceAdvice-2.0-Example.xml`.
- Method: I read each document as a whole against its root definition. All XPaths were run with lxml (`scratchpad/round3/meaning-p-z/xp.py`, definitions with `defs.py`). In the XPaths, `d:` is the document's own namespace.
- Out of scope, not repeated: `ubl-findings.md`, the decisions in the brief, and the round-2 findings that are fixed.

## Findings

### Procurement

#### DM3#F101 · High · QualificationApplicationResponse: the answer refers to a question that does not exist (regression)

- **Where:**
  - `QualificationApplicationResponse.xml:/d:QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `TenderingCriterionProperty-1`.
  - The only question in the document: `/d:QualificationApplicationResponse/cac:TenderingCriterion/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:ID` = `TenderingCriterionProperty-631`.
  - `count(//cbc:ID[. = /d:QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID])` = 0.
  - Cause: `gen_minimal.py` l. 154–155 hard-codes `"TenderingCriterionProperty-1"`. Commit `5664959` ("identifiers unique across the set") renumbered all other IDs to `DOCNO*10+n` (l. 156–161), so the property ID moved and the reference did not.
  - The same mismatch is in `minimal/layer0/QualificationApplicationResponse.xml`.
- **Why:**
  - The root definition is "A self-declaration of an economic operator, stating that it does not fall under the Exclusion Grounds and that it meets the Selection Criteria".
  - The generator's own reasoning (l. 328–331, 433–436): "the answer refers to a question in the same document".
  - In round 2 the two IDs were equal (`-1`/`-1`), and DM#F107 recorded the document as coherent. Now the `true` answers a property that is defined nowhere, so the self-declaration says yes to nothing. Its one statement is lost. `check()` does not test this reference.
- **Condition:** `ValidatedCriterionPropertyID` equals the ID of the TenderingCriterionProperty in the same document.
- **Options:**
  1. In `id_for`, return the value already assigned to `TenderingCriterionProperty` in this document, e.g. `"TenderingCriterionProperty-%d" % (DOCNO*10 + 1)`, or look it up in the built tree.
  2. In addition, a `check()` rule: every `ValidatedCriterionPropertyID` resolves to a `TenderingCriterionProperty/cbc:ID` in the same document.
- **Needs decision:** no. It restores the stated rule.

#### DM3#F102 · Low · ProcurementStatus and TenderStatus (deprecated): a status without any status

- **Where:**
  - `count(/d:ProcurementStatus/*)` = 4 in `ProcurementStatus.xml`: ContractFolderID `ContractFolderID-551`, IssueDate, ContractingParty, EconomicOperatorParty.
  - The same four in `deprecated/TenderStatus.xml` (`ContractFolderID-771`).
- **Why:**
  - ProcurementStatus is "A document sent by a Contracting Party to an Economic Operator describing the status of a procurement procedure, Project, or Lot". TenderStatus is "(Deprecated) ... describing the status of a tendering procedure".
  - Round 2 (DM#F103) asked only for identification and left "the status itself (periods, ProcedureCode)" for a later layer. That is now done: the procedure is identified. But the document describes nothing about it.
  - The same reasoning ("a status with no status") was accepted for TransportProgressStatus (DM#F122, fixed with a TransportSchedule). The two status documents are now treated differently.
  - The two Requests are fine as they are: asking about an identified procedure is a complete request.
- **Condition (if accepted):** The status document states at least one element of the procedure's status.
- **Options:**
  1. `cac:TenderSubmissionDeadlinePeriod` (a future period from D, with the existing PeriodType fill).
  2. `cbc:ProcedureCode` (needs a descriptive value).
  3. Record in the generator that identification alone counts as the status for these two types.
- **Needs decision:** yes.

### Customs and transport

#### DM3#F103 · Medium · TransitCustomsDeclaration: the declared shipment is only an ID

- **Where:**
  - `TransitCustomsDeclaration.xml`: `count(/d:TransitCustomsDeclaration/cac:Shipment/*)` = 1. Only `cbc:ID` = `Shipment-831` is present.
  - Also `count(/d:TransitCustomsDeclaration/cbc:IssueDate)` = 0.
  - Generator: `"TransitCustomsDeclarationType": {"cac:TransitExporterParty", "cac:Shipment"}` (l. 415), with the comment "a transit declaration has a declarant and what is declared" (l. 410).
- **Why:**
  - TransitExporterParty is "The Party who makes the Transit Customs Declaration ... This Party is the owner of the Goods". The declarant is now present (round-2 DM#F121 is half fixed).
  - "What is declared", the condition of DM#F121 and the generator's own comment, is only a shipment reference. Customs declares goods, and no goods are named.
  - The same fix was applied to PackingList (`PackingList:ShipmentType` → GoodsItem, l. 412) and to both waste documents (l. 419–420), but not here.
- **Condition:** The declared shipment names its goods.
- **Options:** `"TransitCustomsDeclaration:ShipmentType": {"cac:GoodsItem"}`. The existing `GoodsItemType` → Item and `Item/Description` ("Ballpoint pen, blue", en) then apply.
- **Needs decision:** yes.

#### DM3#F104 · Low · Waybill: "describing a shipment" with an empty shipment

- **Where:**
  - `Waybill.xml`: `count(/d:Waybill/cac:Shipment/*)` = 1, i.e. only `cbc:ID` = `Shipment-981`.
  - CarrierParty and ConsignorParty have been added (l. 414).
- **Why:**
  - The definition begins "A transport document describing a shipment". It goes on: "It is issued by the party who undertakes to provide transportation services ... to the party who gives instructions".
  - The round-2 condition (the issuer) is met, so the parties fit. The described shipment, though, has no content.
  - Severity is Low because a carrier's waybill with a shipment reference is a credible stub, and round 2 asked only for the issuer.
- **Condition (if accepted):** The waybill's shipment names its goods.
- **Options:** `"Waybill:ShipmentType": {"cac:GoodsItem"}`. The same text as PackingList applies.
- **Needs decision:** yes.

#### DM3#F105 · Low · TransportationStatus: an undated status

- **Where:**
  - `TransportationStatus.xml:/d:TransportationStatus/cbc:TransportExecutionStatusCode` = `IN_TRANSIT`.
  - `count(/d:TransportationStatus/cbc:IssueDate | .../cbc:IssueTime | .../cac:StatusPeriod | .../cac:TransportEvent)` = 0.
- **Why:**
  - TransportationStatus is "A document to circulate reports of transportation status or changes in status (events)".
  - "In transit" is a state at a moment, and here the moment is implied (IND6).
  - The set's other status-like documents are dated for this reason. RetailEvent got its IssueDate so that `PLANNED` can be read against it (DM#F117). TransportProgressStatus has IssueDate and IssueTime with offset.
- **Condition (if accepted):** The status report says when the status applies.
- **Options:**
  1. `cbc:IssueDate` + `cbc:IssueTime`, as in TransportProgressStatus.
  2. `cac:StatusPeriod`.
- **Needs decision:** yes.

### Deprecated

#### DM3#F106 · Medium · Enquiry: "the item" with no item (new text)

- **Where:**
  - `deprecated/Enquiry.xml:/d:Enquiry/cbc:Description` = `Is the item available from stock?`.
  - `count(/d:Enquiry/cbc:ID | /d:Enquiry/cac:AdditionalDocumentReference | /d:Enquiry/cac:Attachment)` = 0.
  - Source: `TEXTS["Enquiry/Description"]` (l. 735), added in `775897a` for DM#F126.
- **Why:**
  - Enquiry is "A document sent by a requestor to a responder requesting information about a particular business process".
  - The question now exists, but "the item" has no antecedent. EnquiryType has no item element, nothing else in the document names one, and the documents are unrelated by decision.
  - The responder could not answer it, so the fix for DM#F126 traded "no question" for an unanswerable one.
  - The EnquiryResponse ("Ja, der Artikel ist ab Lager lieferbar.") is acceptable as it is: its ParentDocumentReference points to the enquiry that carries the context.
- **Condition:** The question names what it asks about.
- **Options:**
  1. Name the set's item in the text: "Is the blue ballpoint pen available from stock?" (en). For consistency the response could also say "Ja, der blaue Kugelschreiber ist ab Lager lieferbar." These are new texts and need the translation round.
  2. `cac:AdditionalDocumentReference` to a document outside the set. This is weaker: the item is still not named.
- **Needs decision:** yes (the wording).

### Generator comments

#### DM3#F107 · Low · UtilityStatementTypeCode comment says consumption comes in a later layer

- **Where:** `gen_minimal.py` l. 223–224: "the services the document type names ...; a later layer with consumption must match (KWH)".
- **Why:** Since `6f3c962`, layer 1 itself carries the consumption: `UtilityStatement.xml:/d:UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `350`, `unitCode="KWH"` (l. 256, 261, 429–432). The document is consistent: ELECTRICITY matches kWh. But the stated reason is out of date, and the generator's contract is "every decision and its reason is a comment".
- **Condition:** The comment matches the current layer.
- **Options:** e.g. "...; the consumption (SubscriberConsumption, in KWH) matches it".
- **Needs decision:** no.

## Checked and consistent

Round-2 findings in scope that are now fixed are marked with their round-2 number.

- **PackingList (US):** GoodsItem with the pen describes what is packed (DM#F120).
- **PriorInformationNotice (US):** the authority names the project "Office supplies 2026 (54)" (DM#F102).
- **ProcurementStatusRequest (JP), TenderStatusRequest (deprecated, en):** the economic operator asks about an identified folder (DM#F103). For the status documents, see DM3#F102.
- **ProductActivity (en):** sales of 10 pens over the four weeks before issue, at a named store.
- **ProofOfReexportation, ProofOfReexportationRequest, ProofOfReexportationReminder:** guarantor roles and counterfoil/passport as in UBL 2.5 §2.3.5.6.6.5. The IDs are now unique (DM#F101).
- **PurchaseReceipt (DE):** seller with VAT number, a line with an item, 15.00 EUR (10 × 1.50).
- **QualificationApplicationRequest (JP):** now defines the yes/no criterion (DM#F106). For the Response, see DM3#F101.
- **Quotation (BR) / RequestForQuotation (JP):** the seller is issuer or addressee, a line of 10 pens, and the Quotation totals 75.00 BRL.
- **ReceiptAdvice (en):** the consignee receives 10 pens from the shipper (DM#F113).
- **Reminder (US):** a line references the overdue invoice, with 16.00 USD = total (DM#F110).
- **RemittanceAdvice (DE):** TotalPaymentAmount 15.00 EUR = DebitLineAmount of the referenced invoice (DM#F109). Paying an invoice as a debit line matches the OASIS 2.0 sample (`DebitLineAmount` 107.50 = `TotalPaymentAmount`).
- **RetailEvent (IN):** dated, `PLANNED` two weeks ahead, "Monsoon sale" 26 Aug – 1 Sep, sender to receiver (DM#F117). The change from "Back-to-school" fits the locale.
- **SelfBilledCreditNote (BR):** the customer credits the pen, 75.00 BRL (DM#F112).
- **SelfBilledInvoice (ZA):** the customer issues the invoice, both parties have VAT numbers, 270.00 ZAR.
- **Statement (US):** TotalBalanceAmount 16.00 = line balance of a referenced invoice (DM#F111).
- **Tender (JP):** the tenderer bids 500000 JPY in an identified folder. This is now a plausible bid (VA#F6).
- **TenderContract (en), UnawardedNotification (JP):** award on Mon 2026-08-10, before the issue date.
- **TenderReceipt (BR):** the authority acknowledges with registered date and time.
- **TenderWithdrawal (DE):** the tenderer withdraws in an identified folder (DM#F104).
- **TendererQualification (JP):** 12 operating years (DM#F108).
- **TendererQualificationResponse (en):** admission resolved on D−2.
- **TradeItemLocationProfile (BR):** a one-year profile for one item.
- **TransportExecutionPlan / Request:** the provider, DOOR_TO_DOOR service and consignment (DM#F125 partly; the TransportUserParty is still absent, which round 2 rated Low).
- **TransportProgressStatus (JP):** a named vehicle at a named terminal, dated and timed (DM#F122).
- **TransportProgressStatusRequest (IN):** a dated request about a named vehicle.
- **TransportServiceDescription (BR):** the provider announces a DOOR_TO_DOOR service (DM#F119).
- **TransportServiceDescriptionRequest (DE):** asks about a DOOR_TO_DOOR service.
- **TransportationStatusRequest (ZA):** asks about a consignment (DM#F119).
- **UnsubscribeFromProcedureRequest / Response:** identified folder, right parties (DM#F105).
- **UtilityStatement (ZA):** 350 kWh at a consumption point, supplementing a referenced invoice, ELECTRICITY (DM#F116). Only the comment is stale (DM3#F107).
- **WasteMovement (US) / WasteNotification (DE):** used lead-acid batteries, all waste roles present, and customs in the notification (DM#F124).
- **WeightStatement (en):** gross weight 12000 KGM for a shipment (DM#F123).
- **WorkReport (BR):** 10 hours of office-equipment maintenance (DM#F115).
- **AttachedDocument (deprecated):** a real PDF with its parent ID, sender and receiver.
- **EnquiryResponse (deprecated):** answers a referenced enquiry (DM#F126).
- **FreightInvoice (deprecated, BR):** invoices "Frete rodoviário", 1200.00 BRL, for an identified shipment (DM#F114).
- **OrderResponseSimple (deprecated):** the seller accepts a referenced order.
- **StockAvailabilityReport (deprecated):** the seller reports 10 pens to the branch ("Beispielfiliale", DM#F118).
- **Round-2 DM#F101 (unique IDs):** no reference value in scope recurs across documents. The only break is internal: DM3#F101.

## Considered and refuted

- **UtilityStatement without a consumption period:** the statement is "a supplement to an Invoice", and the referenced parent invoice carries the period.
- **SelfBilledCreditNote without a reference to the credited invoice:** the credited item is named, and that was the round-2 condition. A reference would only refine it.
- **TransportProgressStatus without arrival or departure times:** the timed issue plus the StatusLocation say where the vehicle is at issue.
- **PriorInformationNotice name suffix "(54)":** it follows the "values unique across the set" decision (l. 776–777). Its form is a values question, not one of meaning.
- **Tender without a description of what is offered:** the folder identifies the project (generator l. 272–275). Round 2 accepted this.
- **Amounts on lines without quantity** (PurchaseReceipt, SelfBilled*, FreightInvoice): round 2 refuted this, and nothing changed.

## Not verified

- Whether a monsoon sale from 26 Aug to 1 Sep is typical Indian retail practice. It is plausible (the season runs June–September), but no source was checked.
- The texts proposed in DM3#F106 have not been checked by translators.
- Process chapters of the specification other than re-exportation (§2.3.5.6.6.5) were not re-read for this round.
- Layer 0 is out of scope. A grep shows only that it has the same QualificationApplicationResponse mismatch as DM3#F101.
- No option has been generated or validated.
