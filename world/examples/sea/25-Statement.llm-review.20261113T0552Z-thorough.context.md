# LLM review: 25-Statement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### sea/25#F1 · Medium · The invoice's freight and insurance repeated as charges of the statement
- XPath: `/Statement/cac:AllowanceCharge/cbc:Amount` = `3090.00`
- XPath: `/Statement/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Freight and insurance of the CIF invoice`
- XPath: `/Statement/cac:StatementLine[1]/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`
- XPath: `/Statement/cac:StatementLine[1]/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`
- XPath: `/Statement/cbc:TotalDebitAmount` = `53778.00`
- Why: A statement is "a statement of account, not a summary invoice". Its document-level `AllowanceCharge` is "A discount or charge that applies to a price component", and on a statement line "A charge or discount price component associated with this statement line". The freight (2950.00) and insurance (140.00) are already part of the invoice amount debited on line 1 (53778.00 = 50688.00 goods + 3090.00 charges, `22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `3090.00`). Stating them again, once on the document and once on the line, reads as charges levied by the statement itself, although the totals (debit 53778.00, credit 10000.00, balance 43778.00) do not include them a second time. The reader cannot tell whether 3090.00 is owed in addition.
- Condition: The statement reports the invoice amount once and carries no charge that is not a separate item of the account; any breakdown of an invoice's amount is clearly informative.
- Options: (a) preferred: remove the document-level and line-level allowance charges; the invoice reference gives the breakdown; (b) if the factor does add charges of its own (e.g. a factoring fee), state those and include them in the totals.
- Needs decision: no

### sea/25#F2 · Medium · Exchange rate on a statement line whose invoice is in the statement currency
- XPath: `/Statement/cac:StatementLine[1]/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/Statement/cac:StatementLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/Statement/cbc:DocumentCurrencyCode` = `XBL`
- Why: The statement line's `ExchangeRate` is "The rate of exchange between the currency of the Statement and the currency of the document described in the BillingReference". The statement is in Lume (XBL) and the referenced invoice is in Lume too (`22-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`), so there is no rate between them; the rate to Coral is the invoice's alternative payment currency rate, which is not what this element means.
- Condition: A statement line carries an exchange rate only when its billing document is in another currency than the statement.
- Options: (a) preferred: remove it.
- Needs decision: no

### sea/25#F3 · Medium · The deposit's payment window given as an invoice period
- XPath: `/Statement/cac:StatementLine[2]/cac:InvoicePeriod/cbc:StartDate` = `2026-05-08`
- XPath: `/Statement/cac:StatementLine[2]/cac:InvoicePeriod/cbc:EndDate` = `2026-05-09`
- Why: `InvoicePeriod` on a statement line is "An invoice period to which this statement line applies", the period an invoice covers. Line 2 is the deposit payment (`VT-DEP-26-0412`), paid 2026-05-08 and received 2026-05-09 (`22-Invoice.xml:/Invoice/cac:PrepaidPayment/cbc:PaidDate` = `2026-05-08`). The two dates are the payment's dates, not a period of supply or invoicing; the invoice itself (a one-off sale) has no invoice period.
- Condition: The deposit line carries no invoice period, or one that is an actual invoicing period.
- Options: (a) preferred: remove it; the collected payment already carries its received date (and could carry the paid date).
- Needs decision: no

### sea/25#F4 · Low · A payment received before the statement period, not marked as brought forward
- XPath: `/Statement/cac:StatementPeriod/cbc:StartDate` = `2026-05-14`
- XPath: `/Statement/cac:StatementLine[2]/cac:CollectedPayment/cbc:ReceivedDate` = `2026-05-09`
- Why: The statement covers 2026-05-14 to 2026-06-13, but line 2 credits a payment received on 2026-05-09, before the period. Line 1 states `BalanceBroughtForwardIndicator` false; line 2 has no indicator. Either the deposit belongs to an earlier period (and its effect is a balance brought forward), or the period should start earlier. As it stands, the period and the line contradict each other mildly.
- Condition: Every movement listed falls inside the statement period, or the line that carries an earlier movement is marked as brought forward.
- Options: (a) preferred: start the statement period with the account's first movement (the deposit, 2026-05-08/09); (b) mark line 2 as balance brought forward.
- Needs decision: no

### sea/25#F5 · Low · A zero tax total and the order's originator and beneficiary in a statement of account
- XPath: `/Statement/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Statement/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Statement/cac:StatementLine[1]/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Statement/cac:StatementLine[2]/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: The factor's statement tells Velumi what it owes on the assigned account. A tax total of 0.00 says nothing a statement needs (the statement levies no tax; the invoice's tax treatment is in the invoice). The Port of Selanu, which originated the order and benefits from the goods, has no role in the account between Velumi and the factor, yet it is repeated at document level and on both lines. These are values copied from the sale into a document that does not use them.
- Condition: The statement carries no tax total unless it states tax, and only the parties of the account (supplier/creditor, customer, payee).
- Options: (a) preferred: remove the tax total and the originator and beneficiary parties at all levels.
- Needs decision: no

## Checked and consistent
- Totals: debit 53778.00 − credit 10000.00 = balance 43778.00; line balances 53778.00 then 43778.00; the amounts match `22-Invoice.xml` (tax-exclusive 53778.00, prepaid 10000.00, payable 43778.00).
- Due date 2026-06-28 at document, payment means and line level agrees with the invoice's due date.
- The payee, payee account and RF reference are those of the invoice; the factoring agreement `HF-FA-2026-007` and assignment `HF-ASSIGN-26-0091` are the ones the invoice cites; the note explains why Harbourline issues a statement whose accounting supplier is Lumeway.
- The statement (2026-06-13) precedes the credit note that refers to it (`26-CreditNote.xml`, 2026-06-15).

## Considered and refuted
- `/Statement/cac:StatementLine[1]/cbc:PaymentPurposeCode`: GDDS "purchase sale of goods" suspected wrong for a line that also contains freight and insurance — refuted because the freight and insurance are part of a CIF sale of goods and do not change the purpose of the payment.
- `/Statement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name`: the factor signing a statement in which Lumeway is the accounting supplier suspected as the wrong signatory — refuted because the note states that Harbourline issues it on behalf of Lumeway as holder of the receivable.
