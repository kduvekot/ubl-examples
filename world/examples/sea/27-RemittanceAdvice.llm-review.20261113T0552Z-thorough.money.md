# LLM review: 27-RemittanceAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/27-RemittanceAdvice.xml`, Git blob `a83f4a9e20f100a4540611eef91ece79f8f5dfa3` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/27#F1 · High · The factor named as accounting supplier of the invoice line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: The line's `AccountingSupplierParty` is "the Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line", i.e. the supplier of invoice LD-INV-26-0147. That is Lumeway Distribution, both in the invoice (`22-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`) and at the head of this remittance advice. Harbourline Factoring is the payee and is already named as such (`/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`). The line contradicts both the invoice and the document head.
- Condition: The line's accounting supplier is the invoice's accounting supplier (Lumeway Distribution); the factor appears only as payee.
- Options: (a) preferred: Lumeway as the line's accounting supplier, keeping Harbourline as payee; (b) drop the line-level accounting supplier, as the head already names it.
- Needs decision: no

### sea/27#F2 · Medium · Exchange rate between the remittance advice and an invoice in the same currency
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/RemittanceAdvice/cbc:DocumentCurrencyCode` = `XBL`
- Why: The line's `ExchangeRate` is "the rate of exchange between the currency of the Remittance Advice and the currency of the document described in the BillingReference". Both are XBL (`22-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`). The XBL→XLC rate describes the conversion from the payer's XLC account (`/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XLC`), which this element does not carry.
- Condition: The line carries an exchange rate only between the remittance currency and a referenced document in another currency.
- Options: (a) preferred: drop the rate; (b) if the XLC debit is to be shown, state it as information (e.g. a note with the XLC amount 43714.00 × 0.4 = 17485.600), not in this element.
- Needs decision: no

## Checked and consistent
- Totals: debit 43778.00 (the invoice balance after the deposit, `22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `43778.00`), credit 64.00 (the credit note, `26-CreditNote.xml:/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `64.00`), payment 43714.00 = 43778.00 − 64.00.
- Payee account `XB51BLUM38020502304038` (Harbourline Factoring, XBL) is the account the invoice and the statement name for the assigned receivable; RF reference `RF20LDINV260147` as required by the invoice.
- Payment on 2026-06-25 is before the stated due date 2026-06-28 (the due date itself is questioned in the invoice's review).
- Payer account `XL40BSEL0010003665515` is Velumi's own Lisavan account (the same as the payee account in the buyer's debit note).

## Considered and refuted
- Buyer's debit note VT-DOC-26-0153 (51.250 XLC, `28-DebitNote.xml:/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `51.250`) not deducted: suspected an incomplete settlement — refuted because the invoice's receivable belongs to the factor, and a buyer's counterclaim against the seller cannot simply be set off against a payment to the factor; leaving it to be settled separately is consistent.
