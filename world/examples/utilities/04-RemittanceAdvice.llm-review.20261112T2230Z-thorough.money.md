# LLM review: 04-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/04-RemittanceAdvice.xml`, Git blob `ed53a13de1ca0b9a4d9a62d8bc6c094c15743208` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/04#F1 · Low · Tax total: only the invoice's VAT, unadjusted for the discount taken, with no scheme
- XPath: `/RemittanceAdvice/cac:TaxTotal/cbc:TaxAmount` = `2516028`
- XPath: `/RemittanceAdvice/cbc:TotalCreditAmount` = `301923`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:Note` = `2 % discount taken: paid within the discount period of the invoice's terms.`
- Why: `TaxTotal` is "the total amount of a specific type of tax", but carries no subtotal or scheme, so the reader has to infer that 2,516,028 is the VAT of invoice 02 (`02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cbc:TaxAmount` = `2516028`); the invoice's other tax, the energy tax of 288,840, is not mentioned. The payer has also taken a 2 % discount on the gross amount (301,923, which contains 2 % of the VAT, 50,320.56, and of the energy tax, 5,776.80). Whether the tax total of the remittance should be the invoice's tax or the tax on the amount actually paid depends on the world's rule for settlement discounts (in EU VAT the taxable amount is reduced when the discount is taken). As it stands, the remittance's tax figure is neither clearly the invoice's nor the paid amount's, and the remittance does nothing with it.
- Condition: The remittance either carries no TaxTotal, or one per scheme with a TaxSubtotal and TaxScheme, whose amount follows the world's stated rule for discounts taken.
- Options: (a, preferred) leave TaxTotal out: a remittance advice of a single invoice needs no tax figure, and the invoice carries the tax; (b) VAT and excise totals with their schemes, adjusted for the discount if the world's VAT law reduces the base.
- Needs decision: yes

### utilities/04#F2 · Low · Purpose "supplier payment" for the payment of an electricity and gas bill
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- Why: In ISO 20022 ExternalPurpose1Code, SUPP is "SupplierPayment", the generic code; the invoice paid gives its lines the specific purposes ELEC and GASB (`02-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:PaymentPurposeCode` = `ELEC`, `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:PaymentPurposeCode` = `GASB`). The ISO list also has UBIL (utilities), which covers a payment for both (checked in `world/codelists/sources/iso20022/2Q2026_externalcodesets_v3.json`; the world's subset in `world/codelists/gc/ISO20022PurposeCode.gc` does not contain it). The same SUPP is used in 07 (water) and 14 (telephone), whose invoices use WTER and PHON.
- Condition: The remittance line's purpose code is consistent with the purposes of the invoice it pays.
- Options: (a, preferred) ELEC, the main purpose of the invoice (or UBIL, added to the world's subset); (b) keep SUPP and drop the specific purposes from the invoice lines.
- Needs decision: no

## Checked and consistent
- 15,096,168 − 301,923 = 14,794,245 = TotalPaymentAmount; line: debit 15,096,168, credit 301,923, balance 0.
- The debit equals the invoice's PayableAmount (`02-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `15096168`); the credit equals the invoice's SettlementDiscountAmount; the advice is issued 2026-04-10, inside the settlement period ending 2026-04-12.
- PaymentID and InvoicingPartyReference RF58FEINV260313 equal the invoice's PaymentID (ISO 11649 check passes).
- Payee account XU080351041600000004084431 equals the invoice's PayeeFinancialAccount; payer account XU790351041600000000209458 passes the IBAN-like check; both accounts in XUF, the document currency.
- Payment means 30 (credit transfer) as requested by the invoice.

## Considered and refuted
- `/RemittanceAdvice/cbc:PaymentOrderReference`: VI-PAY-26-0313 was checked against the payment means' InstructionID — the same value, consistent; the number 0313 follows the invoice number.
