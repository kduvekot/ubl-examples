# LLM review: 07-ImportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/07-ImportCustomsDeclaration.xml`, Git blob `45419bf3fd0c23bb1b64bfa1ca0140c26025be7e` (committed)
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

### wood/07#F1 · Low · Import declaration describes the shipment without weight, packages, consignment or transport
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `MS-SH-26-0632`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `4800`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `21600`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cbc:ID` = `MS-CS-26-0629`
- Why: the import declaration declares the same shipment as the export declaration, but its shipment and goods item carry no gross (or net) weight, no packages, no consignment, no carrier and no transport mode, all of which the export declaration and the transport documents of the flow state for the same goods. Gross mass and packages are standard data of an import declaration (own knowledge: boxes 35 and 31 of the Single Administrative Document), and the consignment is what links the declaration to the transport (`04-TransportExecutionPlanRequest.xml`) and the despatch advice. No value contradicts another example; the declaration is only incomplete against them.
- Condition: the import declaration's shipment states the gross weight (21 600 kg) and the packages of the goods item, and identifies the consignment `MS-CS-26-0629` (and the transport mode or means), consistent with the export declaration.
- Options: (a) preferred: add `GrossWeightMeasure` to the goods item and the shipment, a package or handling unit count, and `Consignment/ID` with the carrier; (b) at least the gross weight and the consignment ID.
- Needs decision: no

## Checked and consistent
- Previous declaration `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `MS-CD-26-0631` is the customs declaration of `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `MS-CD-26-0631` (an export declaration of the same shipment, issued the day before).
- Shipment `MS-SH-26-0632`, quantity 4800 slats, item (`MS-SL-1800`, HS `440799`, origin `XB`) and the forestry certificate `XB-FOR-2025-0118` agree with the export declaration and the despatch advice.
- Dates: issued 2026-02-27 11:05, after the export declaration (2026-02-26 09:25) and within the transport window of `04-TransportExecutionPlanRequest.xml` (2026-02-26 to 2026-03-01); validity starts on the issue date.
- Exit office `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Bayvarran side` is the same text as in the export declaration.
- Codes: `IMPORT`/`FREECIRC`/`PURCHASE`, HS section `IX`, cargo type `GEN` resolved and fit the release of purchased timber.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Bayvarran side`: suspected that an import declaration should name the office of entry (Urvanian side), not the exit office — refuted because the UBL 2.5 ImportCustomsDeclaration has no entry-office element; `CustomsExitOfficeLocation` is defined as "Customs exit office of the goods being declared", and the Bayvarran post is that office.

## Outside this review
- Whether the goods can be cleared at 11:05 on 2026-02-27 after leaving Marrowdale on 2026-02-26 is a timeline question for the consistency review. The contradiction between the transport window and the agreed delivery window is a finding of `04-TransportExecutionPlanRequest.xml` (this run).
