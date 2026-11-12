# LLM review: 11-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/11-Invoice.xml`, Git blob `d14230a475262f9f8b47c7b7e1cbf9ab963fc61a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### wood/11#F1 · Low · Invoice for an ex-works sale with no delivery (collection) data
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `BF-PO-26-0637`
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-09`
- XPath: `10-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `EXW`
- Why: the invoice bills 12 m³ of timber sold ex works (`10-Order.xml`, issued the evening before, `10-Order.xml:/Order/cbc:IssueDate` = `2026-03-08`). It has no `Delivery` (no actual delivery date, no place) and no despatch reference, and the flow has no despatch advice or other document recording that the buyer collected the goods. Nothing in the flow therefore says that or when the goods were delivered, which the invoice is the last chance to state.
- Condition: the invoice (or another document of the flow) states the delivery under EXW: the date the goods were made available or collected at the sawmill's yard.
- Options: (a) preferred: add `Delivery` with `ActualDeliveryDate` and the delivery location `Marrowdale Sawmill, timber yard`; (b) add a despatch advice to the flow and reference it (changes the flow, needs a decision).
- Needs decision: no

## Checked and consistent
- Reference `/Invoice/cac:OrderReference/cbc:ID` = `BF-PO-26-0637` resolves to `10-Order.xml` (an order); quantity `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `12` in m³ and the item (`MS-TB`, HS `440799`) equal the ordered ones.
- Dates: issued 2026-03-09 09:54, after the order of 2026-03-08 16:20.
