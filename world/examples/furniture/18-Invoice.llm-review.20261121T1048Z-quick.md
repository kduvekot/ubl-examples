# LLM review: 18-Invoice.xml

Flow: furniture (9900336121) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/furniture/18-Invoice.xml`, Git blob `72324b2adb2f7f73b39c027f10572e8a4f466c50` (committed)
- Last commit changing the example: 1b71959a 2026-11-20 O260: every document belongs to the collaboration it is exchanged in
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### furniture/18#F1 · Low · The return transport is booked to the buyer's timber account
- XPath: `/Invoice/cbc:AccountingCostCode` = `1100`
- XPath: `/Invoice/cbc:AccountingCost` = `Timber and materials`
- Why: AccountingCost is "the buyer's accounting code, applied to the Invoice as a whole". The buyer here is Brackenmere Furniture, and 1100 "Timber and materials" is its account for buying timber (`wood/11-Invoice.xml:/Invoice/cbc:AccountingCost` = `Timber and materials`, likewise `wood/10-Order.xml`). This invoice bills the transport of unsold benches and chairs back from a retailer under the sale-or-return clause; that is a selling or distribution cost of the maker, not a purchase of timber. Brackenmere's own freight costs elsewhere in the examples would be the comparable account; a retailer would also only quote a code the buyer gave it for this kind of charge.
- Condition: the accounting cost on the invoice is a buyer's account that fits the return transport (or is left out if the buyer gave none for such charges).
- Options: (a) use a Brackenmere account for freight or sales costs (preferred: the charge is the maker's transport cost under the own-label agreement); (b) remove AccountingCost/AccountingCostCode, as the retailer has no reason to know the maker's chart of accounts.
- Needs decision: no

## Checked and consistent
- Amounts: 1 × 85.00 = 85.00 = line extension = tax exclusive = tax inclusive = payable; tax category E with exemption "service to a business", as in other Bayvarran service invoices (e.g. `retail/16-Invoice.xml`).
- Late payment: 1.5 % × 85.00 = 1.275, rounded 1.28 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `1.28`; due date 17 July = 30 days after 17 June (a Friday); penalty from the next day.
- The line note's seven benches, ten chairs and seven care kits are the quantities of `12-InstructionForReturns.xml` (4 + 3 benches, 5 + 5 chairs, 7 kits); delivery on Monday 15 June to GLN `9523710900015` lies in the requested window 12–15 June there and is the location named there.
- The note agrees with `12-InstructionForReturns.xml` ("the stock above the target goes back at the maker's cost … The store's van brings it"). Roles are reversed correctly: Brightmarket is supplier, Brackenmere customer; the GLNs, IBAN-like account and RF reference pass their checks.
- `BM-SVC-RT` follows Brightmarket's own item numbering (`BM-551005` … in `08-Order.xml`).
