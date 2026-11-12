# LLM review: 05-ExportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/05-ExportCustomsDeclaration.xml`, Git blob `485e09ca0ec698fc71593b783ad60898b71c45fd` (committed)
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

### wood/05#F1 · Low · Supporting document given by ID only; the commercial invoice is not referred to
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `VI-PO-26-0627`
- XPath: `08-Invoice.xml:/Invoice/cbc:ID` = `MS-INV-26-0635`
- Why: the only supporting document is the buyer's order `03-Order.xml`, referenced by ID without `DocumentTypeCode` or `DocumentType`, so the declaration does not say what `VI-PO-26-0627` is. The commercial invoice, which is the document a customs value and an export sale are normally evidenced with, already exists when the declaration is made (`08-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-02-26` at `08:56:00`, the declaration at `/ExportCustomsDeclaration/cbc:IssueTime` = `09:25:00`) and is not referenced. The declared value `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `34560.00` is the order line value (whether it should include the pallet charge is for the money part).
- Condition: every document reference of the declaration says what kind of document it is, and the declaration references the commercial invoice of the sale it declares (or the story says why not).
- Options: (a) preferred: add a type to the order reference and an additional reference to `MS-INV-26-0635` typed as commercial invoice; (b) replace the order reference by the invoice reference.
- Needs decision: no

### wood/05#F2 · Low · No packages, transport mode or means of transport at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `4800`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `21600`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Bayvarran side`
- Why: the goods item gives the number of slats and the gross weight but not the number and kind of packages (96 bundles, per `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.`), and the shipment states neither the mode of transport nor the identity of the truck that will present the goods at the exit office (own knowledge: packages, mode at the border and identity of the means of transport are standard data of an export declaration, e.g. boxes 31, 21 and 25 of the Single Administrative Document). The exit office is identified only by a descriptive name, without a customs office identifier. The declaration can be understood without them, so this is a completeness remark.
- Condition: the declaration states the packages of the goods item, the transport mode at the border and the means of transport, and identifies the exit office, or the story explains why the world's export procedure does not need them.
- Options: (a) preferred: add a `TransportHandlingUnit` or package count to the goods item, a `ShipmentStage` with `TransportModeCode` road and the truck's registration, and an `ID` on the exit office location; (b) only the package count and transport mode.
- Needs decision: no

## Checked and consistent
- Shipment and consignment: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `MS-SH-26-0632` and `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cbc:ID` = `MS-CS-26-0629` are the shipment of `06-DespatchAdvice.xml` and `07-ImportCustomsDeclaration.xml` and the consignment of `04-TransportExecutionPlanRequest.xml`; gross weight 21 600 kg is the same in all that state it; the carrier is the haulier of the transport request (same ID and licence).
- Customs declaration `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `MS-CD-26-0631` is what the import declaration cites as previous declaration (`07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `MS-CD-26-0631`).
- Dates: declared on 2026-02-26 at 09:25, validity starting the same day, consistent with `/ExportCustomsDeclaration/cbc:Note` = `Declared electronically before the goods leave.` and the transport window starting on 2026-02-26. Exit office name equal to the one in the import declaration.
- Codes: HS `440799` with section `IX`, cargo type `GEN`, `PERMANENT`/`SALE` resolved and fit a sale of sawn timber.
- Physics (calculated): 4800 × 0.006498 m³ = 31.19 m³; 21 600 kg gross gives 692 kg/m³ including packaging, plausible for kiln-dried hardwood (650–750 kg/m³, own knowledge).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `21600`: Shipment gross weight is defined as "the weight of the goods plus packaging plus transport equipment", yet equals the goods item's gross weight — refuted because no transport equipment (container, swap body, trailer) is part of this shipment; the truck is the means of transport, whose weight is not included in either.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `4800` with unit `EA`: suspected that a customs quantity of sawn wood should be in m³ (own knowledge: the supplementary unit of HS 4407 is m³) — refuted for this lens because GoodsItem/Quantity is "The number of units making up this goods item", which 4800 slats are; a supplementary unit would be a separate statement.
