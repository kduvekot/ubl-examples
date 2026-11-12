# LLM review: 02-WasteMovement.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/02-WasteMovement.xml`, Git blob `32c42c37c829fb72899a0b9b0b8748b5caf542d9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns)
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### waste/02#F1 · Medium · A report of the transport of waste that says neither when the waste was shipped nor when it was received
- XPath: `/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- XPath: `/WasteMovement/cbc:IssueDate` = `2026-04-02`
- Why: UBL defines the WasteMovement as "A document used to report the transport of waste". The document is issued by the recovery facility and references a weighbridge statement (`RR-WB-26-0412`) and a further document `RR-REC-26-0412`, so it reports a movement that has taken place, but the shipment carries no date of departure from the producer, no date of receipt at the facility, and no pickup or delivery place (`Shipment/cac:Delivery`, `Consignment/cac:CarrierParty` alone do not say it). In the Basel movement document these dates (shipment, receipt, recovery) are the core of what is reported (own knowledge). The issue date alone does not say when the waste moved.
- Condition: The movement document states when the waste left the producer and when it was received at the recovery facility (and from where to where), or it is clear from its type that it is issued before the transport and those dates are planned ones.
- Options: (a) preferred: add a `Shipment/cac:Delivery` with the actual delivery date/time and place at Rinova Recovery, and the despatch (pickup) date at Valdara Industries. (b) If the document is meant to be the accompanying document issued before departure, give planned dates and drop the references to weighing and receipt.
- Needs decision: no

### waste/02#F2 · Medium · A province in `Region`
- XPath: `/WasteMovement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country and belongs in `CountrySubentity`. The same value is in `Region` in 104 examples (219 occurrences; `grep -r --include='*.xml' -o '<cbc:Region>Province of'` over `world/examples`).
- Condition: No `Address/Region` holds a province; the province, where needed, is in `CountrySubentity`.
- Options: (a) preferred: move the value to `CountrySubentity`. (b) Drop it.
- Needs decision: no

### waste/02#F3 · Medium · A domestic movement reported to the customs border office, with an international haulage authorization
- XPath: `/WasteMovement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteMovement/cac:SenderParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: The waste moves from Valdara Industries (Ferrano, XU) to Rinova Recovery (Ferrano, XU); no border is crossed and nothing in the document names another country. Yet the movement is reported to the customs "Border office", and the carrier is shown with an authorization for "International road haulage", which this movement does not use. The same story problem is in the notification it refers to (`01-WasteNotification.xml:/WasteNotification/cac:CustomsParty`, "The competent authority granting a permit to export or import the waste").
- Condition: Either the movement crosses a border (the facility or the route is in another country) and the customs border office is the right receiver; or the movement is domestic, the receiver is the authority that supervises domestic waste movements, and no element claims international carriage.
- Options: (a) preferred: as in the notification, make the movement transboundary, so the document type, the receiver and the authorization fit. (b) Keep it domestic and name an environmental authority as receiver; drop "International" from the carrier authorization.
- Needs decision: yes

### waste/02#F4 · Low · `DisposalFacilityParty` in a movement for recovery
- XPath: `/WasteMovement/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteMovement/cbc:WasteMovementTypeCode` = `RECOVERY`
- Why: `DisposalFacilityParty` is "The Party disposing of the waste material". The movement is of type `RECOVERY` ("Recovery operations (Basel Convention Annex IV B, R1 to R13)") and the facility's authorization is R3; no disposal takes place, so naming the recovery facility also as disposal facility contradicts the type. Same in `01-WasteNotification.xml:/WasteNotification/cac:DisposalFacilityParty`.
- Condition: `DisposalFacilityParty` is absent, or names a party that actually disposes of (part of) the waste, with that disposal stated.
- Options: (a) preferred: drop it. (b) Keep it only with a stated disposal of residues.
- Needs decision: no

### waste/02#F5 · Low · Notifier and sender carry master data the movement document does nothing with
- XPath: `/WasteMovement/cac:NotifierParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/WasteMovement/cac:NotifierParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/WasteMovement/cac:NotifierParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/WasteMovement/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: The notifier's warehousing provider takes no part in this movement (the carrier is Trasvia Haulage), and its stock-exchange listing and share capital have no role in reporting a waste transport. The contacts given for the notifier ("Order desk", Sales) and for the reporting recovery facility ("Customer service", Sales) are sales desks, not the people who answer for the waste, its shipment or its receipt. These values recur as master data: the same service provider and security listing appear in 75 examples each, "Order desk" in 87 (`grep -rl --include='*.xml' -F` over `world/examples`).
- Condition: Every element under the parties has a reason in the waste movement report; the contacts are responsible for the waste shipment or its receipt.
- Options: (a) preferred: drop `ServiceProviderParty`, `SecurityListing`, `CorporateStockAmount` and `FullyPaidSharesIndicator` under `NotifierParty`; give notifier and sender contacts for waste shipment/receipt (e.g. environmental officer, weighbridge/goods-in). (b) Reduce `NotifierParty` to identification and name, as for `WasteProducerParty`.
- Needs decision: no

### waste/02#F6 · Low · A public authority described as a VAT-registered company in the commercial register
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: The receiver is the Customs Administration (ISIC 8411, public administration). It is not in the commercial register and has no liquidation status; its VAT registration is not used by a waste movement report.
- Condition: The customs administration carries no commercial-register scheme, liquidation status or (unused) tax scheme.
- Options: (a) preferred: drop them; keep name and identifier.
- Needs decision: no

### waste/02#F7 · Low · Two references whose documents the flow does not contain, one of them without saying what it is
- XPath: `/WasteMovement/cac:DocumentReference/cbc:ID` = `RR-REC-26-0412`
- XPath: `/WasteMovement/cac:WeightStatementDocumentReference/cbc:ID` = `RR-WB-26-0412`
- Why: `DocumentReference` ("A reference to a relevant document associated with this Waste Movement") carries only an ID; whether `RR-REC-26-0412` is a receipt, a certificate of recovery or something else the reader has to guess from the "REC" in the ID. `WeightStatementDocumentReference` names a UBL WeightStatement, a document type the flow could contain, but no example of the flow has this ID (`flow_index.py waste` resolves it to `?`). The invoice bills the weighed quantity (`03-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`), so the weight statement is the basis of the money in the flow.
- Condition: The document reference states its kind (code or description); the weight statement either exists in the flow or is acknowledged as external.
- Options: (a) preferred: add a `DocumentTypeCode`/`DocumentDescription` to `RR-REC-26-0412` (e.g. "Certificate of recovery"), and an issue date to both references. (b) Add a WeightStatement example to the flow (changes the flow, hence the decision).
- Needs decision: yes

## Checked and consistent
- `WasteMovementTypeCode` uses `WasteOperationCategoryCode`, which the CVA binds to `cbc:WasteMovementTypeCode`; `RECOVERY` is in it and agrees with `01-WasteNotification.xml:/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`.
- `WasteNotificationDocumentReference` resolves to `01-WasteNotification.xml` (ID VI-DOC-26-0204), a WasteNotification, issued 2026-03-23, before this document.
- `SequenceNumberID` = 1 and `ConsignmentQuantity` = 12 agree with the notification's 12 estimated shipments.
- Notifier, producer and recovery facility are the same parties as in the notification (XU-R-104274, XU-R-104548); the shipment and consignment IDs are the same (see 01's review for whether the notification should carry them).
- `DocumentDistribution` to the producer, "Electronic copy: the producer must keep it with the notification", fits a distribution of this document to an interested party; `DocumentTypeCode` = WasteMovement names this document.
- `HazardousRiskIndicator` = false agrees with the authorization purpose "non-hazardous plastic waste".

## Considered and refuted
- `/WasteMovement/cbc:WasteMovementTypeCode`: listID differs from the notification's type code list — refuted because the CVA binds a different list (`WasteOperationCategory`) to this element and the meanings agree.
- `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200` against the notification's 40 000 kg — refuted as a contradiction here: the notification states a planned figure, this one a weighed figure; the question of what the notification's figure covers is in 01's review.
- `/WasteMovement/cac:SenderParty/cac:PartyAuthorization`: the facility's permit in a movement document — refuted as master-data filler, because a movement report shows that the receiving facility is authorised for the operation.
- `/WasteMovement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Rinova Recovery`: signed by the facility rather than the notifier — refuted because the sender of this report is the facility confirming receipt.
- `/WasteMovement/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`: a distribution to the notifier who is already a party — refuted because the distribution states a distinct purpose (the producer's record-keeping).

## Outside this review
- Whether the movement on or before 2026-04-02 could take place only 10 days after the notification of 2026-03-23 (time for the authority's consent) is a timeline question across documents.
- Whether 38 200 kg is the waste or the loaded vehicle/equipment, and whether it fits one road vehicle, is for the logistics and money parts; its use in the invoice is in 03's review.
