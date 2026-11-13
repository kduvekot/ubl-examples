# LLM review: 27-RemittanceAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### sea/27#F1 · High · The factor named as accounting supplier of the invoice line, while the header names the distributor
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- Why: The line's `AccountingSupplierParty` is "The Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line". The line pays invoice `LD-INV-26-0147`, whose accounting supplier is Lumeway Distribution (`22-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`), as the remittance advice's own header says. Harbourline is the payee of the assigned receivable, which the line already states in `PayeeParty`. The line and the header contradict each other on who the accounting supplier is.
- Condition: The line's accounting supplier is the invoice's accounting supplier (Lumeway Distribution), or is absent; the factor appears only as payee.
- Options: (a) preferred: Lumeway as the line's accounting supplier, Harbourline as payee; (b) drop the line's accounting supplier, since the header gives it.
- Needs decision: no

### sea/27#F2 · High · This payment does not match the payment the invoice status response reports with this remittance advice
- XPath: `/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00`
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0123`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0123`
- Why: The invoice status response cites this remittance advice (`24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cac:RemittanceDocumentReference/cbc:ID` = `VT-RM-26-0150`) for a payment of `24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00` under instruction `24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cbc:InstructionID` = `VT-PAY-26-0199`. This remittance advice reports 43714.00 (the balance less the credit note of 64.00) under payment order and instruction `VT-PAY-26-0123`. The two documents describe the same payment of the same invoice to the same payee differently in amount and identifier.
- Condition: The payment of `LD-INV-26-0147` has one amount and one payment instruction identifier in every document of the flow that reports it.
- Options: (a) preferred: keep this remittance advice as it is (it accounts for the credit note) and align or remove the payment in `24-InvoiceStatusResponse.xml` (see its review); (b) if the status response's figures are the intended ones, change this document, which would drop the credit note set-off.
- Needs decision: no

### sea/27#F3 · Medium · Exchange rate on a line whose invoice is in the remittance currency
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/RemittanceAdvice/cbc:DocumentCurrencyCode` = `XBL`
- Why: The line's `ExchangeRate` is "The rate of exchange between the currency of the Remittance Advice and the currency of the document described in the BillingReference". Both are Lume (XBL): the remittance advice's document currency and the invoice's (`22-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`). The rate to Coral probably reflects that Velumi pays from its Coral account (payer account currency XLC), but that conversion is the bank's, between the payer's account and the payment, and not what this element means.
- Condition: A remittance line carries an exchange rate only when its billing document's currency differs from the remittance advice's currency.
- Options: (a) preferred: remove it; (b) if the debit of Velumi's Coral account matters, state it in a way that fits (e.g. a note), not as the line's exchange rate.
- Needs decision: no

### sea/27#F4 · Low · The order's originator and beneficiary on every remittance line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: A remittance advice "specifies details of an actual payment" so the payee can apply it. The Port of Selanu, which originated the order and benefits from the goods, plays no part in Velumi's payment to the factor; repeating it on both lines (and the buyer and seller on line 1) is data copied from the sale into a document that does not use it.
- Condition: The remittance lines carry the billing references, amounts and the parties needed to apply the payment.
- Options: (a) preferred: remove the originator and beneficiary from both lines.
- Needs decision: no

## Checked and consistent
- Totals: debit 43778.00 − credit 64.00 = payment 43714.00; the debit is the invoice's payable amount after the deposit (`22-Invoice.xml`), the credit the credit note's payable amount (`26-CreditNote.xml`, 2026-06-15).
- The payment goes to the account the invoice names (`XB51BLUM38020502304038`, Harbourline Factoring) with the invoice's RF reference, as the factoring clause requires; it is made on 2026-06-25, before the due date 2026-06-28.
- The payee to receive the remittance advice is the one the invoice's remittance distribution names (Harbourline Factoring).

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:DocumentReference/cbc:ID`: the invoice referenced twice on line 1 (billing reference and document reference) suspected as redundant — refuted because the second reference adds the document type code, which the billing reference does not carry; redundant but not wrong.
- `/RemittanceAdvice/cbc:Note[2]`: "Payment of the invoice below" suspected incomplete, since a credit note is set off too — refuted because the payment is indeed for the invoice and the credit note line is the deduction from it.
