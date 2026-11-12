# LLM review: 04-ExportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/04-ExportCustomsDeclaration.xml`, Git blob `d23054c9c05d2dbe62a877d4d23f4891f2983d71` (committed)
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
- Customs value against the two export sales: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200` MWh = 36800 MWh (energy/06) + 2400 MWh (energy/07). Both invoices price at 3600 XUF/MWh with the pricing rate 1 XBL = 100 XUF, i.e. 36 XBL/MWh; 39200 × 36 = 1411200 = `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1411200.00` XBL; equivalently (132480000 + 8640000) / 100 = 1411200.
- The rate 1 XBL = 100 XUF of 2026-01-02 is the same as in other flows (e.g. `tender/32-Invoice.xml:/Invoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01` in the opposite direction).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1411200.00`: declared in lume while the sales invoices are in ferra — refuted: an export declaration to Bayvarra's customs states the value in the exporting country's currency, and the figure agrees exactly with the invoices at the stated rate.
- The export covers also the 2400 MWh sold to Ferrano Energy (energy/07) while its only consignee is Montebrio Power (`/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`) — not a money finding of this example: a consignee may differ from the buyer. The consequence for the tax treatment and import of the 07 gas is reported in the money review of 07-Invoice.
