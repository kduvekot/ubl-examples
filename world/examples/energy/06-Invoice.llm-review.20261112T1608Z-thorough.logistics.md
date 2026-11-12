# LLM review: 06-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/06-Invoice.xml`, Git blob `7c0dad8fdbb0040b1dab2a0e3035fb59f281af39` (committed)
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
- Quantity against the customs declarations: 36800 MWh = `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`; with the 2400 MWh of `07-Invoice.xml` it makes up the 39200 MWh of `04-ExportCustomsDeclaration.xml` (the consignee question that raises is a finding in the reviews of 04, 05 and 07).
- Quantity × price, calculated: 36800 × 3600 XUF per 1 MWh = 132 480 000 XUF; price 3600 XUF = 36 XBL × 100, as the pricing exchange rate states.
- Item: the same item (KG-NG, 772060000015, HS 271121, CPC 12020, origin XB) and the same field coordinates (39°49.80′ S 15°16.20′ W) as `04-ExportCustomsDeclaration.xml` and `07-Invoice.xml`.
- Dates: `InvoicePeriod` March 2026 before the issue date 2026-04-03; due date 2026-05-03; penalty period from 2026-05-04, the day after the due date, which `08-Reminder.xml` uses.
- `check_ids.py`: RF41KGINV260157 and the payee account check digits OK.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.`: suspected that the invoice should identify the delivery (border station, shipment KG-SH-26-0154 or the import declaration) — refuted because a monthly invoice for one gas flow to one buyer is unambiguous with the period and the measuring point named in the item; a link to the shipment is not needed to bill it.
