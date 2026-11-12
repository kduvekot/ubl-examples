# LLM review: 09-ImportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/09-ImportCustomsDeclaration.xml`, Git blob `f2d4fcae7f399f23e32926db94e2eab6ad1dd2dc` (committed)
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

### plastics/09#F1 · Medium · Goods item quantity is a weight in tonnes, and the packages are not declared
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsTariffQuantity` = `120000`
- Why: `GoodsItem/Quantity` is "the number of units making up this goods item"; the value is 120 TNE, the same mass that `CustomsTariffQuantity` already gives as 120000 KGM. The units of the goods item are 120 jumbo bags (06), and neither their number nor their type is declared, nor the net mass in `NetWeightMeasure`. Import declarations carry the number and kind of packages and the net mass as standard data (own knowledge of customs practice). Same use as in 05 and 06.
- Condition: `Quantity` counts units (bags) or is absent; the packages (120 × JB) and the net mass are declared, consistent with 05 and 06.
- Options: (a) preferred: drop `Quantity` (the tariff quantity covers the mass), add `NetWeightMeasure` = 120000 KGM and a `ContainingPackage` of type JB with the count expressed as in 06#F5; (b) keep `Quantity` as a count of bags.
- Needs decision: no

### plastics/09#F2 · Low · Procedure "no previous procedure" next to a previous declaration and a bonded store
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsProcedureCode` = `1000`
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `RR-CD-26-0888`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cbc:Name` = `Bonded store at the river quay, Lumeport`
- Why: The procedure code means "Release for free circulation, no previous procedure". At the same time the declaration names a `PreviousCustomsDeclaration` ("a reference to a previously sent customs declaration"), which is the Urvanian export declaration (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `RR-CD-26-0888`), and places the goods in a bonded store "where this goods item is temporarily stored". If the goods were stored under a customs warehousing procedure, the previous procedure is not "none"; if they were only in temporary storage at the quay, "no previous procedure" is right but the element and the store's licence type (bonded store) suggest more. The export declaration of another customs territory is not a previous procedure of Bayvarra's customs. I could not settle which the story intends.
- Condition: The procedure code, the previous declaration and the storage location tell one story: either temporary storage only (no previous procedure; the previous declaration, if kept, is clearly the exporting country's), or customs warehousing (procedure code naming it as the previous procedure, and the warehousing declaration referenced).
- Options: (a) preferred: temporary storage at the quay with code 1000, and the export declaration moved to an `AdditionalDocumentReference` with its type, because the flow has no warehousing declaration; (b) a warehousing story with a matching procedure code and declaration.
- Needs decision: yes

### plastics/09#F3 · Low · Reference to the waybill carries no document type
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890`
- Why: The transport document produced at import is referenced by ID only; the declaration does not say that it is the CMNI consignment note (06), and the seller's invoice (10, `RR-INV-26-0894`), on which the declared customs value is based, is not referenced at all.
- Condition: The waybill reference says what it refers to; the commercial invoice the customs value rests on is referenced, or the story says why not.
- Options: (a) preferred: add `DocumentTypeCode` `Waybill` and a second reference to `RR-INV-26-0894` with type `Invoice`; (b) a `DocumentDescription` on the existing reference only.
- Needs decision: no

## Checked and consistent
- Weights: gross 120480 kg as in 03–06 and 08; tariff quantity 120000 kg = waybill net weight (06).
- Values: 9984000 XUF ÷ 100 = 99840.00 XBL customs value; FOB 98046.00 = 99840.00 − 1794.00, the freight 179400 XUF ÷ 100 (06, 07); the same rate 1:100 is used for both, so the conversion is consistent within the example.
- Timeline within the flow: declared 2026-04-22 10:35, after the planned discharge at 08:00 (04, 06).
- `CustomsExitOfficeLocation` = the same river border post as in 05; the Import Customs Declaration in the UBL 2.5 model has only this office element, so its use for the exporting country's exit office is the model's.
- Shipment `RR-SH-26-0889` matches 05, 06 and 08; consignor and consignee match 06.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`: suspected that an import declaration should name the entry office instead — refuted because `ImportCustomsDeclaration` in UBL 2.5 offers only `CustomsExitOfficeLocation` ("Customs exit office of the goods being declared"), and the value is that office.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:DangerousGoodsApprovedIndicator` = `false`: suspected storage data copied without use — left to the context lens; for logistics, the storage conditions (5–35 °C, not refrigerated) fit PE granulate, which needs no special storage.
