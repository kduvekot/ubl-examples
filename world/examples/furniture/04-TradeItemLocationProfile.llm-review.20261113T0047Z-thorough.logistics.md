# LLM review: 04-TradeItemLocationProfile.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/04-TradeItemLocationProfile.xml`, Git blob `666a857de25e67c953a50e5da8e5c010b96c5933` (committed)
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

### furniture/04#F1 · Low · Minimum quantity "to qualify for a specific price" without a price
- XPath: `/TradeItemLocationProfile/cac:ItemManagementProfile/cac:ItemLocationQuantity/cbc:MinimumQuantity` = `2`
- Why: UBL defines `ItemLocationQuantity/MinimumQuantity` as "The minimum quantity that can be ordered to qualify for a specific price". The item location quantity carries no `Price` (only `LeadTimeMeasure` and `MinimumQuantity`), so there is no price the minimum qualifies for. The value reads as a minimum order quantity, which the profile already expresses as the order multiple (`/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:MultipleOrderQuantity` = `2`); the orders of the flow (`08-Order.xml`, `10-Order.xml`) state their own minimum and maximum line quantities.
- Condition: either the item location quantity carries the price the minimum qualifies for, or the minimum quantity is absent.
- Options: (preferred) remove `MinimumQuantity`, since the order multiple of 2 sets already governs the order size; or add the price (610 XBL per set, from `02-Quotation.xml`) if the minimum is meant as a price condition.
- Needs decision: no

## Checked and consistent
- Replenishment arithmetic (values from this document): reorder point `MinimumInventoryQuantity` 4 sets < target `TargetInventoryQuantity` 10 sets; the replenishment from the reorder point to the target, 10 − 4 = 6 sets, is a whole multiple of the order multiple 2. A lead time of 5 days fits within the order interval of 14 days. The frozen period of 7 days is consistent with "the maker proposes": proposals become firm a week ahead.
- Periods: the document period and the effective period (2026-03-16 to 2026-08-29) agree, and agree with `05-ExceptionCriteria.xml`; the profile starts the day of the first order (`08-Order.xml`, 2026-03-16).
- Reference: `/TradeItemLocationProfile/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`.
- How the flow uses the profile (initial order of 20 sets, repeat order of 20 sets) is checked in `08-Order.xml` and `10-Order.xml`.

## Considered and refuted
- `/TradeItemLocationProfile/cac:ItemManagementProfile`: suspected a location profile without any location — refuted because UBL 2.5 gives this document no location element (the item location quantity only has an applicable territory), and the store's garden department is identified in `06-ProductActivity.xml`.
- `/TradeItemLocationProfile/cbc:Note` against `/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:ReplenishmentOwnerDescription`: suspected a contradiction ("the maker replenishes" vs "the store orders") — refuted because both hold together: the store places the orders, the maker supplies them.
