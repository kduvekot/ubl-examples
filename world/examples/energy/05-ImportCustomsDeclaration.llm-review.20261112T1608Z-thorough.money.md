# LLM review: 05-ImportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/05-ImportCustomsDeclaration.xml`, Git blob `7a7660d1d073ae04f45f02effa30b140182e1c33` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

## Checked and consistent
- Customs value against the sales invoice: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `132480000` XUF = `06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `132480000`, for the same quantity (`/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800` MWh = 06's invoiced quantity); the gas is priced "measured at the border station", so the invoice price is a value at the border.
- Against the export declaration: 36800 of the 39200 MWh exported under energy/04; the value is that share (36800 × 3600 XUF), and the gross weight is the same share (2940000 × 36800 / 39200 = 2760000 kg).

## Considered and refuted
- Import VAT and duty for the gas are not stated — refuted: UBL 2.5 ImportCustomsDeclaration has no tax total or duty element; the declaration carries the customs value on which customs assess them.
- The remaining 2400 MWh of the export declaration (sold to Ferrano Energy, energy/07, 8640000 XUF) are not in this import declaration — refuted for this example: the declaration is Montebrio Power's own and matches its own purchase exactly. The missing import of the 07 gas is reported in the money review of 07-Invoice.
