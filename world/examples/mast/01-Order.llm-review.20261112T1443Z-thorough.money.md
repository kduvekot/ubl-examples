# LLM review: 01-Order.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/01-Order.xml`, Git blob `a15e986388f03b87c705a9a004911992c536b517` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
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
- Line arithmetic: 6 × 2,400 = 14,400.00 (`/Order/cac:OrderLine[1]/cac:LineItem/cbc:LineExtensionAmount` = `14400.00`); 1 × 180 = 180.00; 20 × 9.5 = 190.00, each with base quantity 1 in the line's unit. Sum 14,770.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `14770.00` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `14770.00` = `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `14770.00`.
- Tax: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G` (free export item) with `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP` ("Export outside Bayvarra") under the seller's state sales tax (STT, Upland State): the seller is in Bayvarra and the goods go to Selanu Telecom on Lisavu, so an export; rate 0 and tax 0.00 agree.
- Prices, quantities and tax treatment are the same in the invoice (`05-Invoice.xml`), line by line.
- `/Order/cac:DeliveryTerms/cbc:ID` = `CPT`: the seller pays the carriage to the mast site, and neither the order nor the invoice has a freight charge, which agrees.

## Considered and refuted
- `/Order/cac:TaxTotal`: suspected that a buyer's order should not state the seller's tax — refuted because AnticipatedMonetaryTotal and TaxTotal give the buyer's expectation of the amounts, and an export exemption is known to the buyer at ordering; the values agree with the invoice.
- `/Order`: suspected missing payment terms, since the invoice applies terms `XB-STD` — refuted because the order is not where the seller's standard terms must be stated; nothing in the order contradicts them.
