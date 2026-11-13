# LLM review: 09-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/09-Invoice.xml`, Git blob `ee49a007b8043177d29c63f3b1b0c8223f117844` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### furniture/09#F1 · Medium · Delivery note reference to a document the flow does not have
- XPath: `/Invoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `BF-DN-26-0320`
- Why: UBL: "A reference to a Delivery Note associated with this document." No example of any flow has this ID (searched over `world/examples/*/*.xml` for `BF-DN-`: only this invoice), and the furniture flow has no Despatch Advice or Receipt Advice, the UBL documents that play the delivery note's part. The number also falls outside the seller's numbering in this flow (BF documents 0568 to 0583 in March and April 2026; 0320 would be far earlier). The invoice is thus the only trace of the delivery of the 20 sets: when they left Marrowdale, when they arrived at goods-in, and that they arrived complete cannot be checked anywhere, although the flow later depends on that stock (sales, return of 6 sets).
- Condition: the delivery note reference either resolves to a despatch document of the flow, or is removed, or is explicitly described as a paper delivery note outside the exchange (with a type and date).
- Options: (preferred) add a Despatch Advice for the 20 sets (and the 20 care kits) to the flow, with this ID or one in the flow's numbering, since the flow's later documents rely on the delivered stock; or describe the reference (`DocumentTypeCode`, `IssueDate`) as a paper delivery note; or remove it.
- Needs decision: yes

### furniture/09#F2 · Low · Invoice for goods without the delivery date
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `20`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `20`
- Why: The invoice bills delivered goods but has no `Delivery` (no `ActualDeliveryDate`, no delivery location) and no invoice period, so neither the date of supply nor the place of delivery is stated. The order (`08-Order.xml`) has no delivery date either, and the referenced delivery note does not exist (F1), so the flow nowhere says when the stock that `06-ProductActivity.xml` starts counting on 2026-03-23 arrived.
- Condition: the invoice states the actual delivery date of the goods (and preferably the goods-in location 9522610900019).
- Options: (preferred) add `Delivery/ActualDeliveryDate` (a date between the order of 2026-03-16 and the invoice of 2026-03-22, e.g. 2026-03-20) and the delivery location; or rely on a Despatch Advice added under F1 and reference it.
- Needs decision: no

## Checked and consistent
- References: `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0574` resolves to `08-Order.xml`; quantity 20 sets, price 610, sub-lines (20 benches at 380, 40 chairs at 115) and item identifiers match the order.
- Arithmetic: 20 × 610 = 12200.00; 7600.00 + 4600.00 = 12200.00; free line 20 × 0 = 0.00.
- Check digits: GLNs, GTIN, RF reference RF74BFINV260575 and the account pass (`check_ids.py`).
- Codes: 380, SET, EA resolve.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[2]`: suspected goods invoiced that were never ordered (20 care kits, not in `08-Order.xml`) — refuted because the line is free of charge and its note explains it as a give-away supplied with the sets; a seller may add free goods to a delivery.
- `/Invoice/cac:InvoiceLine[2]/cac:Item`: suspected an item without any identifier — refuted because a free give-away that is not stocked or resold by item number needs none for this invoice.
