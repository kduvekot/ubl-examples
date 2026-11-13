# LLM review: 22-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/22-Order.xml`, Git blob `99761f3da8d912c9ddd379e499bc58fce3343fa8` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

## Findings

### retail/22#F1 · Low · "Ready from Tuesday", requested from Monday
- XPath: `/Order/cbc:Note` = `Click and collect: ready in the garden department from Tuesday; bring the card used for the order.`
- XPath: `/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-06-01`
- XPath: `/Order/cbc:IssueDate` = `2026-05-30`
- Why: The order is placed on Saturday 2026-05-30; the next Tuesday is 2026-06-02, but the requested collection period starts on Monday 2026-06-01 (calculated). RequestedDeliveryPeriod is "The period requested for delivery", i.e. what the buyer asks for; if the note states what the store promises, the buyer requests a day before the goods can be ready.
- Condition: the requested collection period and the readiness stated in the note agree (the period does not start before the day the goods are ready), or the note's day is the day the period starts.
- Options: (a, preferred) StartDate `2026-06-02`; (b) note "from Monday".
- Needs decision: no

### retail/22#F2 · Low · Delivery-terms location given as text only, although the place has a GLN
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Garden department of the Lumeport store`
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900026`
- Why: For EXW the named place is where the goods are made available; it is the same garden department as the delivery location, which has GLN `9522610900026`, but here it has only a description.
- Condition: the EXW named place identifies the same location (by its GLN).
- Options: DeliveryTerms/DeliveryLocation/ID `9522610900026`, or drop the terms' location.
- Needs decision: no

## Checked and consistent
- Item `BM-551004` "Garden bench set Marrow" is the complementary item offered in 02 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:ComplementaryRelatedItem/cbc:ID` = `BM-551004`) and the store's own article from the furniture flow (`furniture/10-Order.xml`); manufacturer ID `BF-GS-01` and GTIN `9523710000012` (check digit OK) are those used in `furniture/02-Quotation.xml`.
- Delivery location GLN `9522610900026` (check digit OK) is the garden department of the Lumeport store, as in `furniture/06-ProductActivity.xml`.
- EXW fits click and collect (the goods are made available at the seller's premises; own knowledge of Incoterms 2020).
- Quantity 1 SET at 899 XBL per SET = 899.00.
- Buyer's address Gull Lane 57 (LUM-ADR-934215) equals the delivery address in 21.
