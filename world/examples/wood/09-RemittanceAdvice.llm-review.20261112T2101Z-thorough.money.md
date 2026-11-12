# LLM review: 09-RemittanceAdvice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/09-RemittanceAdvice.xml`, Git blob `41a5df331d4ec5f08a936109c93263e9b39bd319` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

## Checked and consistent
- Amounts: TotalDebitAmount 34800.00 = the one DebitLineAmount = `08-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `34800.00`; TotalCreditAmount 0.00; TotalPaymentAmount = 34800.00 − 0.00; BalanceAmount 0.00 (paid in full).
- The invoice reference MS-INV-26-0635 with issue date 2026-02-26 resolves to 08-Invoice.xml; the payment (2026-03-26) is before its due date 2026-03-28, so no penalty applies.
- PaymentID and InvoicingPartyReference RF83MSINV260635 are the creditor reference the invoice asked to be quoted (valid ISO 11649 check).
- Payee account XB78BLUM38712004398618, branch 387120, bank BLUMXBLX and account currency XBL are those of the invoice. Payer account XU790351041600000000209458 (valid check digits) agrees with branch 03510-41600 and bank CREVXUFR; its name is the customer's registration name.
- PaymentPurposeCode SUPP (ISO 20022 "SupplierPayment") fits paying a supplier invoice.
- Debit/credit: an invoice is a debit line and a credit note would be a credit line, as here.

## Considered and refuted
- `/RemittanceAdvice/cbc:PayerReference` = `VI-0625` and `/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0625`: suspected two different values for the same payment order, since both definitions speak of the payer's order for payment — refuted because PaymentOrderReference is defined as the reference "to the order for payment from the payer to the payer's bank" (equal to `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VI-PAY-26-0625`), while PayerReference is the payer's internal reference to its own payment order (e.g. the payment run); a payer can have both.
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XUF`: suspected that a payment in XBL from an XUF account needs an exchange rate in the remittance advice — refuted because the remittance advice tells the payee what it receives (34800.00 XBL, the invoice currency); the conversion is between the payer and its bank and does not change the amounts the payee reconciles.
