# LLM review: 07-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/07-Invoice.xml`, Git blob `0e28c5a596e22d95a0c87b535ac9b772716f3863` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### ore/07#F1 · Low · Item number in the world's item scheme is a valid GTIN-12 in the real UPC range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: as in 01-Order.xml: twelve digits with a correct GTIN-12 check digit (3); read as GTIN-13
  `0771010000013` it has the GS1 US prefix 077, so without the schemeID it can be mistaken for a real
  GTIN (own knowledge of GS1 prefix ranges, no register lookup). 64 examples use the world item
  scheme.
- Condition: the item number cannot be read as a valid GTIN in a real prefix range, or a decision
  records why it is safe.
- Options: (a, preferred) change the world scheme's number form; (b) record the decision.
- Needs decision: yes

## Checked and consistent
- References: `VI-PO-26-0304` → 01-Order.xml (order line `1` exists), `SM-DA-26-0308` →
  04-DespatchAdvice.xml; both resolve, and both are referenced in their dedicated elements.
- Quantity: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `1788.4` t equals the despatched
  quantity in 04-DespatchAdvice.xml and the freight quantity in 06-Invoice.xml; 1788.4 × 8060 =
  14 414 504 = the price extension.
- Item: description, names, seller's and standard IDs, origin, HS `260111`, CPC `14100` and iron content
  62 % agree with 01 and 04.
- Times: issued 2026-03-11 14:59, after the despatch advice (2026-03-10 15:37). Under FCA the goods
  were delivered when handed to the carrier at the mine siding, so invoicing before arrival at the
  factory is consistent.
