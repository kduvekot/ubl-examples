# LLM review: 12-RemittanceAdvice.xml

Flow: reefer (26-0214) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/12-RemittanceAdvice.xml`, Git blob `3b39b3c255d5877d9b361e8fbf39fb1e400f20a2` (committed)
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

## Checked and consistent
- Amounts: one debit line of 28,868.00 = `08-Invoice.xml` payable amount; total debit 28,868.00, credit 0.00, payment 28,868.00, balance 0.00; paid on the invoice's due date, Monday 25 May.
- References: invoice `HRW-INV-26-0772` with its issue date 2026-04-23 resolves; RF creditor reference `RF88HRWINV260772` (check digits pass) is the payment ID the invoice asked for; payment order `26-0027` = the payment means' instruction ID.
- Accounts: the payee account is the one in `08-Invoice.xml` (bank code and branch agree with the account number); the payer account's check digits pass and its bank `BSELXLSL` is in Selanu, the payer's town.
- Purpose GDDS (purchase or sale of goods) fits a payment for fruit.

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XLC`: an XBL payment from a coral account, with no exchange rate stated — refuted: a payer may pay a foreign-currency invoice from its home-currency account, its bank converting; the remittance advice reports the amount remitted in the invoice currency, which is what the payee reconciles.
