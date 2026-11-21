# LLM review: 09-RemittanceAdvice.xml

Flow: modification (MDS-TX-26-0047) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/09-RemittanceAdvice.xml`, Git blob `6b1dcd2af772083f5c1e8748155890d108e11cfb` (committed)
- Last commit changing the example: 0cee647c 2026-11-20 Stage 5, C74, C75, C76: issuers' own numbering, one code per company, collaborations
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

### modification/09#F1 · Low · The payer's contact is the sawmill's sales office
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The remittance advice is sent by the payer's accounts; the payee's contact is "Accounts receivable" in Finance, and the sawmill's sales office is not the desk that pays. Same as 08#F1.
- Condition: Marrowdale's contact here is an accounts-payable or finance contact, the same as in 08.
- Options: follow 08#F1.
- Needs decision: no

## Checked and consistent
- 1295040 − 25901 = 1269139 = `/RemittanceAdvice/cbc:TotalPaymentAmount` = `1269139`; debit and credit agree with 08's payable amount and settlement discount; balance 0.
- Paid on 2026-03-06, within 08's discount period (to 2026-03-08).
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `2026/0065` resolves to 08 with the same issue date; RF reference and both accounts pass `check_ids.py`; the payee account agrees with 08.

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL` while the payment is in ferra — refuted: a payer pays a foreign-currency invoice from its home-currency account; the bank converts.
