# LLM review: 02-WasteMovement.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: logistics

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### waste/02#F1 · High · The weight statement the movement refers to does not exist in the flow
- XPath: `/WasteMovement/cac:WeightStatementDocumentReference/cbc:ID` = `RR-WB-26-0412`
- Why: `WeightStatementDocumentReference` is "a reference to a Weight Statement document", a UBL 2.5 document type of which the repository has an example (`cotton/12-WeightStatement.xml`). No example has the ID `RR-WB-26-0412` (searched over `*.xml`; `flow_index.py` resolves it to `?`). The weight statement is the source of the only weight in this document and, through it, of the quantity billed in `03-Invoice.xml` (see F3 and `03-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`), so the figure cannot be traced.
- Condition: The reference resolves to a Weight Statement example of the flow whose weights agree with this shipment, or the reference is removed.
- Options: (preferred) add a Weight Statement to the waste flow (weighbridge at the recovery facility, gross, tare and net), since the flow bills by weight; alternatively remove the reference and state the weights in this document.
- Needs decision: yes

### waste/02#F2 · Medium · The movement report gives no date or event of the transport
- XPath: `/WasteMovement/cac:Shipment`
- XPath: `/WasteMovement/cbc:IssueDate` = `2026-04-02`
- Why: A Waste Movement is "a document used to report the transport of waste". The shipment has no `ShipmentStage` (with loading, departure or arrival events), no `Delivery` (actual delivery date and place), no transport means (vehicle registration) and no place of loading. The only date is the issue date, so the document does not say when the waste was collected at Valdara and received at Rinova, which is what the report is for (and what the referenced weight statement and `RR-REC-26-0412` presumably record).
- Condition: The shipment states at least when and where the waste was taken over and when it was delivered at the recovery facility, all no later than the issue time 2026-04-02 12:34, and preferably the vehicle used.
- Options: (preferred) add `cac:Shipment/cac:Delivery` with `cbc:ActualDeliveryDate`/`Time` and `DeliveryLocation`, and a main-carriage `ShipmentStage` with the road vehicle and loading/departure events; alternatively at least the delivery.
- Needs decision: no

### waste/02#F3 · Medium · Only a gross weight is reported; the net quantity of waste is missing
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- XPath: `/WasteMovement/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- Why: `GrossWeightMeasure` is "the total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The quantity of waste moved, which the movement report exists to state and which the invoice bills ("per tonne collected", `03-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste, per tonne collected.`), is the weight without packaging and equipment: `cac:Shipment/cbc:NetWeightMeasure` or `NetNetWeightMeasure`, or the goods item's net weight. None is given, nor the number of big bags (`TotalTransportHandlingUnitQuantity` or a `TransportHandlingUnit`/package count). The invoice bills exactly 38.2 t, i.e. the gross figure (finding in `03-Invoice.xml`).
- Condition: The document states the net weight of the waste (and preferably the number of bags), and the net weight is lower than the gross weight by the weight of bags and transport equipment.
- Options: (preferred) add `NetWeightMeasure` (and `GrossWeightMeasure`/`NetWeightMeasure` on the goods item) taken from the weight statement, plus the bag count; alternatively, if 38 200 kg is in fact the net weight of the waste, move it to the net element and give a gross weight that includes the bags.
- Needs decision: no

### waste/02#F4 · Medium · The second document reference cannot be linked and does not say what it is
- XPath: `/WasteMovement/cac:DocumentReference/cbc:ID` = `RR-REC-26-0412`
- Why: The reference carries only an ID, no `DocumentTypeCode` or `DocumentType`, and no example has this ID (searched over `*.xml`; `flow_index.py`: `?`). From the prefix it may be a receipt (Receipt Advice, a UBL document type) or a certificate of recovery; neither exists in the flow. A reader cannot tell what the movement relies on.
- Condition: The reference states its document type, and either resolves to an example of the flow or is a document type the flow does not model (e.g. a certificate of recovery), said so in `cbc:DocumentType`.
- Options: (preferred) state the type (`cbc:DocumentType`, e.g. certificate of receipt/recovery) and its issue date; if it is a Receipt Advice, add it to the flow; or remove the reference.
- Needs decision: yes

### waste/02#F5 · Low · 38 200 kg gross for one road load of bagged polyethylene waste is not physically plausible
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `4923`
- Why: One movement by a road haulier (ISIC 4923) is one lorry load. Figures used (own knowledge): gross combination weight limit 40 t (44 t in some countries), tractor about 7.5 t and curtain-side semi-trailer about 7 t, so about 25 t payload; trailer inner space 13.6 x 2.45 x 2.7 m = 90 m3; big bag about 0.9 x 0.9 x 1.1 m = 0.89 m3; bulk density of sorted PE production waste 0.05-0.2 t/m3 (film, offcuts) to 0.25-0.45 t/m3 (regrind, lumps). Calculation: 30 bags per layer (15 x 2 on 13.6 x 2.45 m), two layers = 60 bags = 53 m3, x 0.45 t/m3 = 24 t of waste at most. 38.2 t gross less a 7 t trailer (if counted as transport equipment) leaves 31.2 t of bagged waste: above the payload, and at 0.45 t/m3 it needs 69 m3, i.e. 78 bags where 60 fit. If the 38.2 t is the net waste (as the invoice treats it), it needs 85 m3 even at 0.45 t/m3, practically the whole trailer volume, and 38.2 t + 14.5 t vehicle = 52.7 t exceeds the 40/44 t limit. At the more typical 0.3 t/m3 the 53 m3 of bags hold 16 t.
- Condition: The weights of one movement fit one road vehicle's payload and loading space at the bulk density of the described waste (for bagged PE waste roughly 10-24 t net), and the invoice quantity follows the corrected net weight.
- Options: (preferred) lower the weights to about 20 t net with a consistent gross, and adjust `03-Invoice.xml` accordingly; alternatively describe the waste as something denser (e.g. baled or compacted) and give the bag/bale count that makes the weight fit.
- Needs decision: no

### waste/02#F6 · Low · Shipment and consignment IDs are those of the notification's planned shipment, with a different weight
- XPath: `/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- XPath: `01-WasteNotification.xml:/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- Why: The notification announces twelve shipments (`ConsignmentQuantity` = 12 in both documents) and this movement is number 1 (`/WasteMovement/cbc:SequenceNumberID` = `1`), yet it reuses the shipment and consignment IDs of the notification's planned shipment (`01-WasteNotification.xml:/WasteNotification/cac:Shipment/cbc:ID` = `VI-SH-26-0205`). The same shipment ID then carries 40 000 kg in one document and 38 200 kg in the other. The IDs are also assigned by the notifier (`VI-` prefix) in a movement sent by the facility, which is plausible, but the remaining eleven movements could not have distinct IDs under this pattern.
- Condition: Each movement can be told apart from the notification's planned shipment and from the other movements by its shipment/consignment identifier, or the documents say that the notification's weight is a planned value for this same load.
- Options: (preferred) give the movement its own shipment ID (keeping the link through `WasteNotificationDocumentReference` and `SequenceNumberID`); alternatively keep the IDs and mark the notification's weight as planned.
- Needs decision: yes

### waste/02#F7 · Low · The goods item does not identify the waste by code
- XPath: `/WasteMovement/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- Why: The goods item description is "text describing this goods item to identify it for customs, statistical, or transport purposes"; a waste movement document identifies the waste by its classification code (own knowledge: Basel/national waste list), which the facility checks against its R3 permit. Only free text is given, here and in the notification (`01-WasteNotification.xml`, finding there).
- Condition: The goods item carries the same structured waste code as the notification.
- Options: (preferred) add `cac:Item/cac:CommodityClassification` with the waste code, identical in both documents.
- Needs decision: no

### waste/02#F8 · Low · The movement shows no consent of the competent authority
- XPath: `/WasteMovement/cac:WasteNotificationDocumentReference/cbc:ID` = `VI-DOC-26-0204`
- Why: A movement under a notification takes place only after the competent authority has consented to the notification (own knowledge of Basel/OECD procedure). The movement refers to the notification only; no document of the flow, and no reference here, records a consent or its number, so the movement 10 days after the notification has no visible authorisation.
- Condition: Either the flow shows the consent (a referenced document or authorisation with its ID and validity covering 2026-04-02), or the story states that no consent is needed (e.g. a domestic movement or green-listed waste for which information suffices).
- Options: (preferred) add a `DocumentReference` to the consent with `cbc:DocumentType` and issue date; alternatively make the story explicit.
- Needs decision: yes

## Checked and consistent
- `/WasteMovement/cac:WasteNotificationDocumentReference/cbc:ID` = `VI-DOC-26-0204` resolves to `01-WasteNotification.xml` (a Waste Notification, as the element requires), issued 2026-03-23, before this document (2026-04-02).
- `/WasteMovement/cbc:ConsignmentQuantity` = `12` equals `01-WasteNotification.xml:/WasteNotification/cbc:ConsignmentQuantity` = `12`; `SequenceNumberID` 1 is within 1..12.
- `/WasteMovement/cbc:WasteMovementTypeCode` = `RECOVERY` with list `WasteOperationCategoryCode`, which the world's CVA binds to this element; it agrees with the notification's type and the facility's R3 authorisation.
- Goods description, hazardous indicator (`false`), carrier (`XU-R-104822`) and its licence `XU-HAUL-2020-0877` (valid to 2030-06-30) are the same as in `01-WasteNotification.xml`.
- Gross weight 38 200 kg equals 38.2 t in `03-Invoice.xml` (unit conversion KGM to TNE checked); see F3 for the gross/net question.
- `/WasteMovement/cac:DocumentDistribution/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274` is the waste producer and notifier, which agrees with the distribution text that the producer keeps the copy with the notification.
- `check_ids.py`: ISIN `XU0001042501` check digit OK.
- Physics: see F5 (figures and calculation there).

## Considered and refuted
- `/WasteMovement/cbc:WasteMovementTypeCode`: suspected a code from another list, since the notification uses `WasteNotificationTypeCode` — refuted because `world/codelists/UBL-World-2.5.cva` binds `cbc:WasteMovementTypeCode` to `WasteOperationCategory`, and RECOVERY is in it.
- `/WasteMovement/cbc:ConsignmentQuantity`: suspected it should count this movement's consignments — refuted because in Waste Movement it is defined as "Estimated total number of shipments for the Waste Notification document", and 12 matches the notification.
- `/WasteMovement/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`: suspected a consignment ID used as a document number — refuted: it is used only as the consignment's identifier (F6 is about reuse, not misuse).

## Outside this review
- Whether Trasvia Haulage's vehicles, as described in the road flow, could carry this load on the movement date is a cross-flow capacity and timeline question.
