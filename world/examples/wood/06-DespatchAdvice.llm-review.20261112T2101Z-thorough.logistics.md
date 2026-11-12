# LLM review: 06-DespatchAdvice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/06-DespatchAdvice.xml`, Git blob `e24fe891b1bc7348a4d9bc77947476a40bc1b949` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### wood/06#F1 · Medium · Despatch advice states neither despatch nor expected delivery
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `MS-SH-26-0632`
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-02-26`
- XPath: `/DespatchAdvice/cbc:DespatchAdviceTypeCode` = `DELIVERY`
- Why: a Despatch Advice is "A document used to describe the despatch or delivery of goods and services". The shipment carries no `Delivery` (no `EstimatedDeliveryDate`, `PromisedDeliveryPeriod`, `ActualDeliveryDate`) and no `Despatch/ActualDespatchDate`, so the document does not say when the goods leave Marrowdale or when Valdara can expect them at goods-in; the reader has to assume that despatch is on the issue date (implied by absence, which the repository's rules exclude). This matters here because the delivery the despatch advice announces falls outside the window agreed in `02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02` (see the review of `04-TransportExecutionPlanRequest.xml`, this run): the receiving party needs the expected arrival to plan goods-in.
- Condition: the despatch advice states the despatch date (and time) and the expected delivery date or period at the consignee.
- Options: (a) preferred: add `Shipment/Delivery` with `Despatch/ActualDespatchDate` (and time) and `EstimatedDeliveryDate` consistent with the transport window of `04-TransportExecutionPlanRequest.xml`; (b) at least `Shipment/Delivery/EstimatedDeliveryDate`.
- Needs decision: no

### wood/06#F2 · Low · Packaging (bundles, pallets) only in a line note
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.`
- XPath: `03-Order.xml:/Order/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Heat-treated export pallets`
- Why: the despatch advice is where the receiver learns how the goods arrive. The 96 bundles appear only in a free-text note, and the heat-treated pallets that the buyer pays a charge for (also `08-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Heat-treated export pallets`) appear nowhere in the logistics data of the flow: no `TransportHandlingUnit`, `Package` or package count, no packaging type, no marks. The goods-in check the note asks for (`/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`) has nothing structured to check the number of packages against.
- Condition: the shipment states its handling units or packages (number and kind, bundles and the pallets they are on), consistent with the 4800 slats in bundles of 50 and with the pallet charge.
- Options: (a) preferred: add `Shipment/TransportHandlingUnit` (pallets, with packaging type and count) containing `Package` (bundles of 50), or at least `Consignment/TotalTransportHandlingUnitQuantity` and a package count; (b) if the bundles are not palletised, remove the pallet charge from quotation, order and invoice (money part) — needs the story to say which.
- Needs decision: no

## Checked and consistent
- Reference `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VI-PO-26-0627` resolves to `03-Order.xml` (an order); `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1` matches its only line; quantity `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `4800` equals the ordered quantity.
- Arithmetic of the note: 960 benches × 5 slats = 4800; 96 bundles × 50 = 4800; 50 is the item's `PackSizeNumeric`.
- Shipment `MS-SH-26-0632` and consignment `MS-CS-26-0629` and the gross weight 21 600 kg agree with `04-TransportExecutionPlanRequest.xml` and `05-ExportCustomsDeclaration.xml`; carrier `Trasvia Haulage` is the haulier of the transport request.
- Dates: issued 2026-02-26 08:31, the first day of the transport window; the lot `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `MS-L26-0223` agrees with `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-02-23`, before despatch.
- Physics (calculated): 21 600 kg / 96 bundles = 225 kg per bundle including packaging; one bundle is 50 × 0.006498 m³ = 0.325 m³, which at 650–750 kg/m³ (kiln-dried hardwood, own knowledge) is 211–244 kg. Consistent.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `21600`: Shipment gross weight includes "transport equipment" by definition, yet equals the consignment's gross weight — refuted because the shipment has no transport equipment (container, trailer); the truck is a means of transport.
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-02-23`: suspected too short after the order of 2026-02-22 for kiln drying a 38 mm hardwood (weeks, own knowledge) — refuted because the manufacture date of the item instance can be the date the slats were cut and planed from timber kiln-dried earlier; the lot and the kiln charge are separate statements.

## Outside this review
- Whether the truck could leave Marrowdale on the morning of 2026-02-26 and the goods be cleared in Urvania by 11:05 on 2026-02-27 is a timeline question for the consistency review.
