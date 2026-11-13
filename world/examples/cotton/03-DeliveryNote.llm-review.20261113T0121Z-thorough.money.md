# LLM review: 03-DeliveryNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/03-DeliveryNote.xml`, Git blob `82936eac57b6612b28fe4c2e5e37c1c570ac7654` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

## Checked and consistent
- The delivered quantity `/DeliveryNote/cac:DespatchLine/cbc:DeliveredQuantity` = `18000` kg is the quantity the ginnery self-bills in `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `18000` and the basis of the haulage charge there (0.010 × 18 000 = 180.000).
- The cost centre `/DeliveryNote/cbc:AccountingCostCode` = `200` is the same as in the self-billed invoices 01 and 04 (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cbc:AccountingCostCode` = `200`).
- The delivery note carries no price, amount or tax, as its purpose (confirming delivery) does not need them.

## Considered and refuted
- `/DeliveryNote/cbc:AccountingCost` = `Seed cotton purchases`: the farm issues the delivery note, so a cost centre named after the ginnery's purchases was suspected of being the wrong party's — refuted because the definition ("the accounting cost centre, applied to the Delivery Note as a whole") does not say whose centre it is, and a supplier quoting the buyer's cost centre on its delivery note, so that the buyer can post the receipt, is an ordinary use; it matches the buyer's own self-billed invoices.
