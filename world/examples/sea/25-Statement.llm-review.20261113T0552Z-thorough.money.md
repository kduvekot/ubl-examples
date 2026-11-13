# LLM review: 25-Statement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/25-Statement.xml`, Git blob `a032666792c16cd3abc0420251a04e56790287b6` (committed)
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

### sea/25#F1 · Medium · Freight and insurance charge stated a second time at statement level and not reflected in the totals
- XPath: `/Statement/cac:AllowanceCharge/cbc:Amount` = `3090.00`
- XPath: `/Statement/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Freight and insurance of the CIF invoice`
- XPath: `/Statement/cac:StatementLine[1]/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`
- XPath: `/Statement/cac:StatementLine[1]/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`
- XPath: `/Statement/cbc:TotalDebitAmount` = `53778.00`
- Why: The statement-level `AllowanceCharge` is "a discount or charge that applies to a price component". The 3090.00 is the sum of the two charges already shown on statement line 1 (2950.00 + 140.00) and already contained in that line's debit of 53778.00. As a statement-level charge it would add a further 3090.00, but the totals do not include it (total debit 53778.00 = the line's debit; balance 43778.00). So it either double-counts or is a charge that is not applied. A statement of account debits billing documents; it does not itself price anything.
- Condition: Each charge appears once in the statement, and every charge present is reflected in the debit and balance totals.
- Options: (a) preferred: drop the statement-level charge and keep the line-level breakdown (or drop both and let the invoice reference carry the detail); (b) keep only the statement-level charge and drop the line's, if the breakdown is wanted at document level, without changing the totals (then explain it as information).
- Needs decision: no

### sea/25#F2 · Medium · Statement line exchange rate between two documents in the same currency
- XPath: `/Statement/cac:StatementLine[1]/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Statement/cac:StatementLine[1]/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/Statement/cbc:DocumentCurrencyCode` = `XBL`
- Why: The line's `ExchangeRate` is "the rate of exchange between the currency of the Statement and the currency of the document described in the BillingReference". The statement is in XBL and the invoice it references is in XBL (`22-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`), so there is no exchange between them; the XBL→XLC rate is the invoice's payment alternative rate, a different thing.
- Condition: A statement line carries an exchange rate only if the referenced document's currency differs from the statement's, and then between those two currencies.
- Options: (a) preferred: drop the rate; (b) if the payer's XLC equivalent is wanted, give it as information elsewhere (e.g. a note), not in this element.
- Needs decision: no

### sea/25#F3 · Low · Tax total of 0.00 in a statement of account
- XPath: `/Statement/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- Why: A statement of account reports debits, credits and the balance of billing documents; the tax was settled in the invoice (export, category G). A tax total of 0.00 without subtotal adds nothing and can be read as "no tax applied" on the statement, which is implied by absence anyway.
- Condition: The statement carries a tax total only if it reports tax of the listed documents with its basis.
- Options: (a) preferred: leave the tax total out; (b) give the subtotal with category G and the taxable amount of the invoice, if the factor reports tax.
- Needs decision: no

### sea/25#F4 · Low · Invoice period on the statement line of the deposit payment
- XPath: `/Statement/cac:StatementLine[2]/cac:InvoicePeriod/cbc:StartDate` = `2026-05-08`
- XPath: `/Statement/cac:StatementLine[2]/cac:InvoicePeriod/cbc:EndDate` = `2026-05-09`
- Why: `InvoicePeriod` is "an invoice period to which this statement line applies". Line 2 records the deposit of 10000.00, paid on 2026-05-08 and received on 2026-05-09; it is a payment, not an invoice, and 2026-05-08 to 2026-05-09 is the payment's transit, not a period invoiced.
- Condition: The payment line carries no invoice period; its dates are in the collected payment.
- Options: (a) preferred: drop the invoice period (the collected payment already has the dates); (b) none better.
- Needs decision: no

## Checked and consistent
- Totals: debit 53778.00 (the invoice), credit 10000.00 (the deposit), balance 43778.00; line balances 53778.00 and 43778.00.
- The invoice line matches the invoice (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `53778.00`, issue date 2026-05-14); the deposit matches the invoice's prepaid payment (`22-Invoice.xml:/Invoice/cac:PrepaidPayment/cbc:PaidAmount` = `10000.00`, received 2026-05-09), and the note that it was paid to the distributor before the assignment agrees with the order response's payee account (Lumeway's own).
- Payment means: Harbourline's account `XB51BLUM38020502304038`, RF reference `RF20LDINV260147`, due 2026-06-28, as in the invoice (the due date itself is questioned in the invoice's review: `22-Invoice.xml:/Invoice/cbc:DueDate` = `2026-06-28`).
- The credit note (2026-06-15) and the remittance (2026-06-25) are after the statement date and correctly absent; the buyer's debit note to the seller (2026-05-22) is not a receivable held by the factor and correctly absent.

## Considered and refuted
- `/Statement/cac:StatementLine[1]/cbc:PaymentPurposeCode` = `GDDS`: suspected a conflict with the remittance advice's purpose `SUPP` (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:PaymentPurposeCode` = `SUPP`) — refuted because both are valid ISO 20022 purposes for the same payment, each party choosing its own view (sale of goods for the creditor, supplier payment for the payer).

## Outside this review
- The freight and insurance charged on top of a CIF price originate in the invoice (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `3090.00`) and are reviewed there; the statement follows the invoice.
