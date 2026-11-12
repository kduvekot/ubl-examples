# LLM review: 17-RemittanceAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/17-RemittanceAdvice.xml`, Git blob `9bee7dcb73c7b573cbe5ebbd0a5552954365dc02` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/17#F1 · Low · The account the payment is made from carries the alias "receivables"
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:AliasName` = `Lumeway receivables`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:Name` = `Lumeway Distribution Ltd`
- XPath: `sea/06-OrderResponse.xml:/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AliasName` = `Lumeway receivables`
- Why: Financial Account. Alias Name is "An alias for the name of this financial account, to be used in place of the actual account name for security reasons." Here the account is the payer's account, the one Lumeway pays from, yet its alias calls it the receivables account; the alias comes from the account's use as a payee account in the sea flow. Moreover the actual name is given next to it, so the alias is not used "in place of" the name, and the remittance gives no reason why it needs the alias at all. Data copied from the party's master data into a document that does not use it.
- Condition: The payer account in the remittance carries either no alias or one that fits an account payments are made from, and the alias is only present where it stands in for the name.
- Options: (a) drop the alias here (preferred: the remittance has no need for it, and the name is given); (b) if Lumeway really has one current account for both directions, give it a neutral alias in all examples that carry it.
- Needs decision: no

## Checked and consistent
- Amounts: `/RemittanceAdvice/cbc:TotalDebitAmount` = `4862160`, `/RemittanceAdvice/cbc:TotalCreditAmount` = `0` and `/RemittanceAdvice/cbc:TotalPaymentAmount` = `4862160` agree with the single line (`/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `4862160`, `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:BalanceAmount` = `0`) and with the invoice paid (`15-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `4862160`).
- Timing against the terms: issued 2026-04-22, after the discount period of the invoice (`15-Invoice.xml:/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-03`) and before its due date (`15-Invoice.xml:/Invoice/cbc:DueDate` = `2026-04-23`), so paying the full amount without the 2 % discount and without penalty interest is right.
- The referenced invoice exists with that ID and issue date (`/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:IssueDate` = `2026-03-24`); the creditor reference quoted (`/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF78VIINV260166`) is the invoice's own, with a valid check; the payee account (`/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU790351041600000000209458`) is the one the invoice gives, in XUF; the payer account has a valid IBAN-style check.
- Means and purpose: credit transfer (`30`), as the invoice asks; purpose SUPP (supplier payment) fits a goods invoice.

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL` against the XUF amounts: suspected that the remittance should state the conversion — refuted because the remittance advises the amount remitted to the payee in the invoice currency; the conversion on the payer's side is between the payer and its bank, and an exchange rate is optional.
- `/RemittanceAdvice/cbc:PayerReference` = `LD-0149` beside `/RemittanceAdvice/cbc:PaymentOrderReference` = `LD-PAY-26-0149`: suspected two values for one reference — refuted because the definitions differ ("An internal reference to the payer's order for payment" against "An internal reference to the order for payment from the payer to the payer's bank"), and the second also identifies the instruction (`/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `LD-PAY-26-0149`).
