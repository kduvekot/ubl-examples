# LLM review: 08-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/08-Order.xml`, Git blob `01257b4f8b6e604e5ea78070a814e95bca35ab3d` (committed)
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

## Findings

### furniture/08#F1 · Low · The order says neither when nor exactly where to deliver
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- Why: The order's `Delivery` names only the receiving party; it has no `DeliveryLocation` and no requested delivery date or period. The place appears only as free text under the delivery terms, although the request for quotation identified it by GLN (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`) and the store's other orders do the same (`retail/08-Order.xml`). The delivery time is left to the lead time of the profile (5 days, `04-TradeItemLocationProfile.xml`), which the order does not refer to. The goods were delivered within a week (the invoice `09-Invoice.xml` is dated 2026-03-22), so the information existed.
- Condition: the order's delivery identifies the goods-in location by its GLN, and either carries a requested delivery date or period or refers to the agreed lead time.
- Options: (preferred) add `Delivery/DeliveryLocation` with GLN 9522610900019 and a `RequestedDeliveryPeriod` (e.g. 2026-03-19 to 2026-03-21, inside the 5-day lead time); or keep the text and add a note that delivery follows the agreed lead time.
- Needs decision: no

### furniture/08#F2 · Low · Initial order of twice the target inventory
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:MaximumQuantity` = `20`
- Why: The replenishment profile that takes effect on the order day (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cac:EffectivePeriod/cbc:StartDate` = `2026-03-16`) sets a target inventory of 10 sets and a reorder point of 4 (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:TargetInventoryQuantity` = `10`). The first order brings the store to 20 sets, twice the target. Opening stock for a season can exceed the running target, but neither document says so, and the later story (slow sales, a repeat order cancelled, six sets taken back so that 11 remain) reads as a consequence of exactly this overstock.
- Condition: the initial quantity and the target inventory are consistent, or a note explains why the opening order exceeds the target (e.g. stock for a promotion, cf. `06-ProductActivity.xml` "after the promotion ended").
- Options: (preferred) add a note to the order or the profile that the opening order covers a launch promotion, which keeps the story and its amounts; or lower the initial quantity to the target (10 sets), which changes the invoice, the return and the credit note.
- Needs decision: yes

## Checked and consistent
- References: `/Order/cac:QuotationDocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`; quotation line 1 exists; item, quantity (20 sets) and price (610) match. The order (2026-03-16) lies within the quotation's validity (to 2026-05-05).
- Bill of materials: sub-lines 20 benches and 40 chairs = 20 sets × (1 bench + 2 chairs), as the note says; 20 × 380 = 7600.00, 40 × 115 = 4600.00, sum 12200.00 = 20 × 610 = line extension = item price extension.
- Quantities: minimum 10 ≤ quantity 20 ≤ maximum 20; back-order minimum 5 ≤ maximum 10; both multiples of the order multiple 2 of the profile.
- Codes: OrderTypeCode 220, DAP, SET, EA, ANN resolve; GS1 check digits pass.
