# LLM review: 05-ExportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/05-ExportCustomsDeclaration.xml`, Git blob `a5a3199bc1d430c4bdf148c1d2afa50b7ca50c54` (committed)
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

### plastics/05#F1 · Medium · Goods item quantity is a weight in tonnes, and the packages are not declared
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`
- Why: `GoodsItem/Quantity` is "the number of units making up this goods item". The value is 120 TNE, a mass, while the units of this goods item are 120 jumbo bags (item description "in jumbo bags of 1 tonne"; the waybill declares the bags, `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`). The net mass, which an export declaration needs next to the gross mass, is not given in `NetWeightMeasure`, and the number and kind of packages, a standard element of a customs declaration, are not declared at all. The same use occurs in 06 and 09.
- Condition: `Quantity` holds a count of units (or is absent), the net mass (120000 kg) is in `NetWeightMeasure`, and the 120 jumbo bags are declared (package count and type), consistent with 06 and 09.
- Options: (a) preferred: `NetWeightMeasure` = 120000 KGM, a `ContainingPackage` with type JB and the count of 120 expressed correctly (see 06#F5), and `Quantity` either dropped or 120 with a unit for bags; (b) keep `Quantity` in TNE only if it is moved to an element meant for a tariff quantity (`CustomsTariffQuantity`, as 09 does).
- Needs decision: no

### plastics/05#F2 · Low · Export declaration says nothing about the means of transport at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `RR-SH-26-0889`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`
- Why: The goods leave by barge through a river border post, but the declared shipment has no shipment stage: no mode of transport (inland water, 8) and no identity of the barge (`Fiumella IV`, in 04 and 06), which export declarations normally carry for the exit office to match the goods with the vessel (own knowledge of customs practice). The carrier is named, the vessel is not.
- Condition: The declared shipment states the mode and means of transport at the border, matching 04 and 06, or the story says why the exit office does not need them.
- Options: (a) preferred: add a `ShipmentStage` with `TransportModeCode` 8 and the barge (`TransportMeans/MaritimeTransport` with name and ID as in 06); (b) leave it out and record that the world's export procedure does not ask for it.
- Needs decision: no

### plastics/05#F3 · Low · Reference to the order carries no document type
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `RP-PO-26-0882`
- Why: An `AdditionalDocumentReference` with only an ID does not say what is referenced; a customs office reading it cannot tell that it is the buyer's order (01) rather than a contract, invoice or licence. The seller's invoice (10, `RR-INV-26-0894`), which is the usual commercial document for an export declaration, is not referenced; it is issued later (2026-04-20), so the order is the document available at declaration time.
- Condition: The reference says what it refers to (a document type code or description identifying the order).
- Options: (a) preferred: add `DocumentTypeCode` (e.g. the world's UBL document type code `Order`, as 06 and 11 use that list); (b) add `DocumentDescription`.
- Needs decision: no

## Checked and consistent
- Weights: shipment and goods item gross 120480 kg, same as 03, 04, 06, 08, 09. Shipment `GrossWeightMeasure` includes transport equipment by definition; there is none (loose bags in a barge hold), so equal values are correct.
- Declared customs value 9984000 XUF = order and invoice amount (01, 10).
- Shipment `RR-SH-26-0889` and consignment `RR-CS-26-0885` are the same IDs as in 06 and 08 (and 09 for the shipment).
- Timeline within the flow: declared 2026-04-19 16:08, after loading (13:30) and despatch (15:10, 06) and before the planned exportation event 2026-04-20 16:00 (04, 06), fitting the note "Declared electronically before the goods leave".
- HS 390110, density 0.92 g/cm³ and section VII are consistent.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`: suspected a location without identifier — refuted as a finding because no other example identifies the post either, so there is nothing it fails to match; an identifier would be an improvement, not a correction.
