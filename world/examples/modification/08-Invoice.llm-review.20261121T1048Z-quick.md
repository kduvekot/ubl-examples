# LLM review: 08-Invoice.xml

Flow: modification (MDS-TX-26-0047) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/08-Invoice.xml`, Git blob `3f50a28dd1dd35f0acd3ee20aaa5f7e0d1a24c77` (committed)
- Last commit changing the example: fd97400c 2026-11-20 O255: wood and modification, story and XML brought into line
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 1d8c94f3 2026-11-21 Reviews of the examples added since the November run (quick run 20261121T1048Z), first files
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

### modification/08#F1 · Low · The accounting customer's contact is the sawmill's sales office
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting customer's contact receives and settles the invoice; the supplier side uses "Accounts receivable" in Finance. A sales office is the wrong desk for an incoming invoice. Same contact in 09 as payer.
- Condition: Marrowdale's contact as accounting customer is an accounts-payable or finance contact.
- Options: (a) preferred: an accounts-payable contact of the sawmill, mirroring Tostara's accounts receivable; (b) keep it and say why.
- Needs decision: no

## Checked and consistent
- Arithmetic: 96 × 13250 = 1272000; 4 × 5760 = 23040; 1272000 + 23040 = 1295040 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `1295040`; 2 % of 1295040 = 25900.8, rounded to `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `25901`.
- Storage: 4 weeks begun from the week of 4 February (ready in store, 02 and 06) to the week of 26 February (collection, 07) — weeks of 2, 9, 16 and 23 February; 24 pallet places = 96 bundles at four to a pallet (07).
- The settlement period 26 February to 8 March is 10 days, as the note says; 09 pays on 6 March, within it.
- `/Invoice/cac:OrderReference/cbc:ID` = `MDS-PO-26-0047` resolves to 01; the contract reference agrees with 01; prices and item agree with 01.
- RF reference and the payee account pass `check_ids.py`; the account, bank and branch agree with 09.
- Customer tax registration: Bayvarra's state sales tax (`STT`), which supports the outside-scope treatment for a business customer abroad.

## Considered and refuted
- `/Invoice/cbc:DueDate` = `2026-03-30` against "30 days net": 30 days from 2026-02-26 is 2026-03-28, a Saturday — refuted: moved to the next working day, Monday 30 March.
- `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O` for storage of goods in Urvania — refuted: a B2B service to a business established abroad, under the same rule as line 1; storage is not tied to immovable property.
- `/Invoice/cac:InvoiceLine[2]`: the order 01 has no storage line — refuted: storage until call-off was asked in 01's note and is priced under the season agreement.
