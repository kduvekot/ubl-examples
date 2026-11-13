# LLM review: 10-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/10-Order.xml`, Git blob `4c325d25cd05fed989cbd0f6f69ef7970de5cb48` (committed)
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

### furniture/10#F1 · High · Repeat order of 20 sets while about 17 sets are in stock
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20`
- XPath: `/Order/cbc:IssueDate` = `2026-04-16`
- Why: Stock calculated from the flow: 20 sets delivered before 2026-03-22 (`09-Invoice.xml`), and 3 sets sold from 2026-03-23 to 2026-04-20 (`06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cbc:Quantity` = `3`). On 2026-04-16 the store therefore held between 17 and 20 sets. The replenishment profile in force says to reorder when stock falls to 4 sets and to replenish up to 10 (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:MinimumInventoryQuantity` = `4`, target 10). With at least 17 sets on hand no reorder is due, and 20 more would bring stock to 37 or more, nearly four times the target. The order date is also off the agreed 14-day rhythm (2026-03-16 + 28 days = 2026-04-13). The cancellation (`11-OrderCancellation.xml`) gives slow sales as its reason, but these were already visible on the order day.
- Condition: the repeat order is consistent with the stock the flow implies and the profile in force (stock at or below the reorder point, quantity bringing it to about the target), or the order states why it departs from the profile.
- Options: (preferred) change the story so that the repeat order is a forward order for the summer peak placed under the profile's frozen period (and say so in a note), which keeps the cancellation's logic; or lower the quantity and move the order to a date on which stock has fallen to the reorder point, which requires higher sales in `06-ProductActivity.xml` and changes the exception story.
- Needs decision: yes

### furniture/10#F2 · Low · The repeat order says neither when nor exactly where to deliver
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- Why: As in the first order: no `Delivery/DeliveryLocation` (the goods-in GLN 9522610900019 of `01-RequestForQuotation.xml` is not used) and no requested delivery date or period. For this order the missing date matters more, because the cancellation (`11-OrderCancellation.xml`) turns on whether the second delivery was still ahead ("cancelled before production"), which cannot be checked without a requested date.
- Condition: the order's delivery identifies the goods-in location by its GLN and states a requested delivery date or period.
- Options: (preferred) add `Delivery/DeliveryLocation` with GLN 9522610900019 and a `RequestedDeliveryPeriod` that lies after the cancellation date of 2026-04-22; or refer to the lead time in a note.
- Needs decision: no

### furniture/10#F3 · Low · Quotation line reference without the quotation
- XPath: `/Order/cac:OrderLine/cac:QuotationLineReference/cbc:LineID` = `1`
- Why: UBL: "A reference to a quotation line associated with this order line." The line reference carries only a line number; it has no `DocumentReference`, and the order has no `QuotationDocumentReference` (it refers only to the earlier order, `/Order/cac:OrderDocumentReference/cbc:ID` = `BS-PO-26-0574`). Which quotation's line 1 is meant must be inferred through `08-Order.xml`, which does name `02-Quotation.xml`.
- Condition: the quotation line reference can be resolved from this order alone.
- Options: (preferred) add `QuotationDocumentReference` BF-DOC-26-0568, as in `08-Order.xml`; or add the document reference inside the line reference.
- Needs decision: no

## Checked and consistent
- Reference: `/Order/cac:OrderDocumentReference/cbc:ID` = `BS-PO-26-0574` resolves to `08-Order.xml`, an order of the same buyer, seller and item.
- Bill of materials: 20 benches + 40 chairs = 20 sets; 7600.00 + 4600.00 = 12200.00 before the 3 % allowance.
- The quotation is still valid on 2026-04-16 (validity to 2026-05-05).
- Quantities: minimum 10 ≤ 20 ≤ maximum 20; back order 5 to 10; multiples of 2.
