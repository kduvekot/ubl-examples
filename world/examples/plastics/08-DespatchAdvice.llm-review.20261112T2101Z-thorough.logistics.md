# LLM review: 08-DespatchAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/08-DespatchAdvice.xml`, Git blob `40cea0e7c3b5f742441038658c674f3f93c6cc68` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### plastics/08#F1 · Medium · The despatch advice states neither when the goods left nor when they arrive
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `RR-SH-26-0889`
- XPath: `/DespatchAdvice/cbc:DespatchAdviceTypeCode` = `DELIVERY`
- Why: A despatch advice is "used to describe the despatch or delivery of goods". This one has no despatch date or time (no `Shipment/Delivery/cac:Despatch` or `ActualDespatchDate`), no estimated delivery (`Delivery/EstimatedDeliveryPeriod`) and no delivery location; the shipment has only an ID, a gross weight and the carrier. The consignee, asked to "check the goods on arrival", is not told that the barge left on 2026-04-19 at 15:10 (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchTime` = `15:10:00`) and is due at the river quay in Lumeport on 2026-04-22 (04, 06). The issue date is not a despatch date (nothing implied by absence).
- Condition: The despatch advice states the actual despatch (date, time) and the expected delivery (period or date, and place), consistent with 04 and 06.
- Options: (a) preferred: `Shipment/cac:Delivery` with `cac:Despatch/cbc:ActualDespatchDate`/`Time` = 2026-04-19 15:10, `EstimatedDeliveryPeriod` ending 2026-04-22 and `DeliveryLocation` = the river quay; (b) at least the actual despatch date and the estimated delivery date.
- Needs decision: no

### plastics/08#F2 · Low · No reference to the consignment note and no package count
- XPath: `/DespatchAdvice/cbc:Note[2]` = `Please check the goods on arrival and report any damage on the consignment note.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One barge load of recycled granulate in jumbo bags.`
- Why: The note sends the consignee to "the consignment note", but the despatch advice does not identify it (`FB-WB-26-0890`, 06). And the goods are described only as "in jumbo bags"; the advice does not say how many packages to check on arrival (120, from 06), which is what a receiving check counts. "One barge load" is also not quite what happened: the consignment is a part load of the barge (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` = `FB4-26-031/2`).
- Condition: The advice references the consignment note and states the number and type of packages (120 × JB); the line note does not claim a full barge load unless it is one.
- Options: (a) preferred: an `AdditionalDocumentReference` to `FB-WB-26-0890` with its type, and the 120 bags as `Shipment/TotalTransportHandlingUnitQuantity` or a `Shipment/cac:TransportHandlingUnit`/`Package` with the count; change the line note to "120 jumbo bags of recycled granulate"; (b) the package count in `DespatchLine/cac:Shipment` or the note only.
- Needs decision: no

### plastics/08#F3 · Low · Lot number differs from the waybill's trace ID for the same goods
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `RR-PE-0416`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-04-16`
- Why: The despatch advice identifies the lot as `RR-PE-0416` (made on 2026-04-16). The waybill traces the same goods item with `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cbc:TraceID` = `RR-PE-LOT-26-0416`, and the bags with `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ID` = `RR-JB-0416`. Three different forms all point to the 0416 lot; a receiver matching the advice with the consignment note finds no common identifier. It is either the same lot written two ways, or two identifiers whose relation is not stated.
- Condition: The lot is identified the same way in 06 and 08, or the two identifiers are evidently different things (e.g. a trace ID of the shipment vs a production lot) and both documents say which.
- Options: (a) preferred: use the lot number `RR-PE-0416` as the waybill's trace ID too, because the lot is the seller's identifier for recall; (b) keep both, and let the waybill carry the lot in its item (`Item/ItemInstance/LotIdentification`).
- Needs decision: no

## Checked and consistent
- Delivered quantity 120 TNE = order line 1 (01) and invoice line (10); gross weight 120480 kg as in 05, 06, 09.
- Shipment `RR-SH-26-0889`, consignment `RR-CS-26-0885` and carrier Fiumella Barges match 05 and 06.
- Order reference `RP-PO-26-0882` and order line 1 resolve to 01; the despatch advice is referenced by the invoice 10.
- Issued 2026-04-19 17:57, after the actual despatch at 15:10 (06).
- Lot made 2026-04-16, three days before despatch.
