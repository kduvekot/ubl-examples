# LLM review: 06-ProductActivity.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/06-ProductActivity.xml`, Git blob `b8bd3b68d78e4195bf7df8c905e21d85b0c22321` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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
- Retail prices: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxExclusivePrice/cbc:PriceAmount` = `899` × 1.065 = 957.435, rounded to `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxInclusivePrice/cbc:PriceAmount` = `957.44`. 6.5 % is the state sales tax rate applied to consumer sales in Lumeport elsewhere in the world (the standard-rated STT category with `Percent` 6.5 in packaging/08-PurchaseReceipt and packaging/09-PurchaseReceipt).
- The retail price (899 per set) lies above the purchase price of 610 per set in 08-Order and 09-Invoice, a plausible retail margin.
- Currency `XBL` matches the purchase documents of the flow.

## Considered and refuted
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxInclusivePrice/cbc:PriceAmount`: suspected that the tax-inclusive price implies a tax rate the document never states (IND6). Refuted because `SalesItem` has no element for the tax category or rate; the pair tax-exclusive/tax-inclusive price is how UBL expresses the retail price here, and the rate it implies (6.5 %) is the world's rate for such sales.
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cac:TaxExclusivePrice`: suspected data the document does nothing with (the maker does not need the store's retail price). Refuted because sales reporting to a supplier under a sell-through threshold (05-ExceptionCriteria, 07-ExceptionNotification) commonly carries the selling price, so the supplier can judge whether the price explains the low sales.
