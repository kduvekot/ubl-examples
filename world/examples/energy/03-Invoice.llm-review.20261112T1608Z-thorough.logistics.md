# LLM review: 03-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/03-Invoice.xml`, Git blob `80f13e4ce6ede50f2dc64b8d628230f6cf1de513` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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
- Quantity × price, calculated: 18400 MWh × 9800 XUF per 1 MWh = 180 320 000 XUF = the line amount.
- Physics, calculated: Montebrio Power imports 36800 MWh of gas in March (`05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`, billed in `06-Invoice.xml`) and sells 18400 MWh of electricity in the same month: 18400 / 36800 = 50.0 % efficiency, plausible for a combined-cycle gas power station (about 50–60 %, own knowledge). Average output 18400 MWh / 744 h = 24.7 MW.
- Downstream use: Ferrano Energy resells 412800 + 18600 kWh = 431.4 MWh of this month's electricity in `utilities/02-Invoice.xml`, well within the 18400 MWh bought.
- Dates: `InvoicePeriod` March 2026 before the issue date 2026-04-03; due date 2026-05-03.
- Unit MWH on quantity and base quantity, consistent with the item description ("sold by the megawatt hour").

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Electricity fed into the grid at the power station, sold by the megawatt hour.`: suspected that the delivery point (the power station's feed-in) should be identified, since the invoice has no delivery or metering reference — refuted because a wholesale invoice for a month's feed-in of one station to one buyer is unambiguous; the place is named in the description and the period in `InvoicePeriod`.
