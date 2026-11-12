# LLM review: 02-WasteMovement.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: broad

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

### waste/02#F1 · High · Weight statement referenced that does not exist
- XPath: `/WasteMovement/cac:WeightStatementDocumentReference/cbc:ID` = `RR-WB-26-0412`
- Why: `WeightStatementDocumentReference` is "A reference to a Weight Statement document", a UBL 2.5 document type (an example exists in another flow: `cotton/12-WeightStatement.xml`). No example in the repository has the ID `RR-WB-26-0412` (`grep -rl --include='*.xml' 'RR-WB-26-0412'` finds only this file), so the weight the movement reports (`/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`) cannot be traced to the statement it is said to come from. This also matters for `03-Invoice.xml`, which bills per tonne.
- Condition: the reference resolves to a Weight Statement example of the flow whose weights agree with this movement and with the invoiced quantity, or the reference is not a `WeightStatementDocumentReference`.
- Options: (a) add a Weight Statement (Rinova's weighbridge ticket, gross/tare/net) to the flow (preferred: it settles the gross/net question raised in `03-Invoice.xml`); (b) describe the weighbridge ticket as a plain `DocumentReference` with type, if the world's weighbridge does not issue UBL weight statements.
- Needs decision: yes

### waste/02#F2 · Medium · Waste movement report without when and where the waste moved
- XPath: `/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- Why: the document is "used to report the transport of waste". The report gives parties and a weight but no date or time of departure from Valdara and of receipt at Rinova (e.g. `Shipment/Delivery/ActualDeliveryDate`, "The actual date of delivery") and no place of loading or delivery; the only date is the issue date 2026-04-02. Whether the movement happened within the notified period and when the facility took over the waste is what this report is for (own knowledge of Basel Annex V B / movement documents).
- Condition: the shipment states at least the actual date of shipment and of receipt (delivery) of the waste, and the places of loading and delivery where they are not the parties' addresses.
- Options: add `Shipment/Delivery` with `ActualDeliveryDate`/`ActualDeliveryTime` and a despatch date or pickup (preferred: dedicated elements); alternatively `Shipment/Consignment` transport events.
- Needs decision: no

### waste/02#F3 · Medium · Movement of a domestic shipment reported to the customs administration
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- Why: the movement goes from Valdara in Ferrano (`/WasteMovement/cac:NotifierParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`) to Rinova in Ferrano (`/WasteMovement/cac:SenderParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`), both in Urvania; no border is crossed, yet the movement is reported to the customs administration's border office. It carries over the contradiction of the notification it refers to (`01-WasteNotification.xml:/WasteNotification/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`, see that review).
- Condition: the receiver is the authority the notification names as competent for this movement, and that authority fits the movement (domestic or transboundary).
- Options: follow the decision taken for the notification (cross-border facility, or a domestic environmental authority); this finding resolves with it.
- Needs decision: yes

### waste/02#F4 · Medium · Disposal facility given for a recovery operation
- XPath: `/WasteMovement/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteMovement/cac:RecoveryFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteMovement/cbc:WasteMovementTypeCode` = `RECOVERY`
- Why: `DisposalFacilityParty` is "The Party disposing of the waste material"; the movement is for recovery and Rinova's only authorisation is R3 recovery (`/WasteMovement/cac:SenderParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`). Nothing is disposed of.
- Condition: `DisposalFacilityParty` is present only if a disposal operation is part of the movement.
- Options: remove it (preferred), consistent with the notification.
- Needs decision: no

### waste/02#F5 · Medium · Province in Region
- XPath: `/WasteMovement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is what `CountrySubentity` is for ("The political or administrative division of a country … such as the name of its county, province, or state"). 219 occurrences in 104 examples (`grep -rc --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of this example carries a province in `Region`.
- Options: move to `CountrySubentity` (preferred); or drop.
- Needs decision: no

### waste/02#F6 · Low · Shipment and consignment IDs of the notification reused for the first of twelve movements
- XPath: `/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`
- XPath: `/WasteMovement/cbc:SequenceNumberID` = `1`
- Why: the notification plans 12 shipments (`01-WasteNotification.xml:/WasteNotification/cbc:ConsignmentQuantity` = `12`) under the shipment `01-WasteNotification.xml:/WasteNotification/cac:Shipment/cbc:ID` = `VI-SH-26-0205` with an estimated 40000 kg; this movement, number 1 of 12, uses the same shipment and consignment IDs with 38200 kg. Either the notification's shipment is the planned shipment pattern for all twelve (then movements 2–12 would share these IDs and the ID does not identify this movement), or it is this actual shipment (then the notification described only one of twelve).
- Condition: the shipment ID of this movement identifies this movement, and its relation to the notification is carried by `WasteNotificationDocumentReference` and `SequenceNumberID`.
- Options: give the movement its own shipment/consignment ID (preferred); or state in the notification that its shipment describes the typical planned shipment.
- Needs decision: no

### waste/02#F7 · Low · Recovery certificate (?) referenced by ID only
- XPath: `/WasteMovement/cac:DocumentReference/cbc:ID` = `RR-REC-26-0412`
- Why: a reference with only an ID; nothing says what it is (the ID suggests a certificate of recovery or of receipt). No example has this ID (`grep -rl --include='*.xml' 'RR-REC-26-0412'`). If it is the certificate of recovery, it would normally follow the recovery, later than receipt; with no dates in the document this cannot be checked.
- Condition: the reference states what kind of document it is (and its date).
- Options: add `DocumentTypeCode`/`DocumentType` and `IssueDate` (preferred); or remove it if the document has no role here.
- Needs decision: no

### waste/02#F8 · Low · Contacts and master data that do not fit the movement report
- XPath: `/WasteMovement/cac:NotifierParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/WasteMovement/cac:NotifierParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/WasteMovement/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/WasteMovement/cac:NotifierParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: the notifier's contact for a waste movement is its sales order desk, the reporting facility's contact is its customer service in Sales; an authority needs the people responsible for the waste and the plant. Valdara's listed shares, share capital and warehousing provider play no role in the movement (the carrier is Trasvia). Same values in 87 (`Order desk`), 75 (`XU0001042501`) and 75 (`VI-SP-2026-01`) examples (`grep -rl --include='*.xml'`).
- Condition: contacts fit the roles in a waste movement; parties carry no data the movement does not use.
- Options: environmental/operations contacts and removal of the copied master data (preferred).
- Needs decision: no

## Checked and consistent
- `WasteNotificationDocumentReference` `VI-DOC-26-0204` resolves to `01-WasteNotification.xml` (a Waste Notification, issued 2026-03-23, before this movement of 2026-04-02).
- `ConsignmentQuantity` `12` matches the notification; `SequenceNumberID` `1` is the first movement.
- Parties: notifier, producer, facility and carrier have the same identifiers and names as in `01-WasteNotification.xml`; the goods description and `HazardousRiskIndicator` are the same.
- `WasteMovementTypeCode` `RECOVERY` is in the world list `WasteOperationCategoryCode`, which `lists.json` binds to this element.
- `DocumentDistribution` to Valdara (the producer keeps a copy with the notification) has a reason in the story.
- `check_ids.py`: ISIN check digit correct.
- Physics: 38200 kg gross including the vehicle (definition of `GrossWeightMeasure`) is below the 40 t combination limit; with a tare of about 14–15 t for a tractor and curtainsider (own knowledge) the load would be about 23–24 t, plausible for dense PE production scrap in big bags at about 0.3 t/m³ in a ~90 m³ trailer. Whether 38200 kg is in fact gross or the net waste weight is the question raised in `03-Invoice.xml`.

## Considered and refuted
- `/WasteMovement/cac:SenderParty/cac:PartyName/cbc:Name`: the facility, not the notifier or carrier, sends the movement report — refuted because the consignee/facility confirms receipt in the movement document (Basel Annex V B), so it is a legitimate sender.
- `/WasteMovement/cbc:WasteMovementTypeCode`: uses a different list (`WasteOperationCategoryCode`) than the notification's `WasteNotificationTypeCode` — refuted because `lists.json` binds each element to its list and both lists contain `RECOVERY` with the same meaning.
- `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure`: 38200 kg differs from the notification's 40000 kg — refuted as a contradiction because the notification gives an estimate and this movement an actual weight.

## Outside this review
- Whether the movement on or before 2026-04-02 could follow consent to a notification of 2026-03-23 is a timeline question across documents.
