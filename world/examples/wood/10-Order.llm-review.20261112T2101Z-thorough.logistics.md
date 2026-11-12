# LLM review: 10-Order.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/10-Order.xml`, Git blob `9ace6d42e7deb8a74ae8c2e901f90885e501c883` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### wood/10#F1 · Low · Ex-works order without a collection date
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `EXW`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Marrowdale Sawmill, timber yard`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`
- Why: under EXW the seller delivers by making the goods available at its premises, and the buyer collects them. The order names the place (as text only) and the despatch party, but `Delivery` has no `RequestedDeliveryPeriod` and `Despatch` no `RequestedDespatchPeriod`, so the order does not say when the 12 m³ are to be ready for collection. No other document of the flow records the collection (the invoice `11-Invoice.xml` follows the next morning without delivery data; see its review, this run).
- Condition: the order states when the goods are to be made available for collection (date or period).
- Options: (a) preferred: add `Delivery/Despatch/RequestedDespatchPeriod` (or `Delivery/RequestedDeliveryPeriod`, which under EXW is the same moment); (b) state it in the line's `Delivery`.
- Needs decision: no

## Checked and consistent
- No transport document exists for this order, consistent with EXW (the buyer carries); the despatch party is the seller, whose yard is the delivery location.
- Quantity `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `12` in `MTQ` with a price base quantity `1` `MTQ`: the unit fits sawn timber sold by volume. Physics: 12 m³ of kiln-dried hardwood at 650–750 kg/m³ (own knowledge) is 7.8–9.0 t, which a buyer from the same town can collect in a few loads; the order states no weight, so there is nothing to contradict.
- The order is referenced as `BF-PO-26-0637` by `11-Invoice.xml`; it resolves.
