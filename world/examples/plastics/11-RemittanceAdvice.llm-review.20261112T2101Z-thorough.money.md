# LLM review: 11-RemittanceAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/11-RemittanceAdvice.xml`, Git blob `d0c26e7bbd846569482f83cb92b801d665bd1d34` (committed)
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

## Findings

### plastics/11#F1 · Low · Two different payer references for the same payment order
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `RP-0882`
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `RP-PAY-26-0882`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `RP-PAY-26-0882`
- Why: `PaymentOrderReference` is "An internal reference to the order for payment from the payer to the payer's bank" and `PayerReference` is "An internal reference to the payer's order for payment". Both name the payer's own payment order; the document gives that order two different references. `RP-PAY-26-0882` is consistent with the instruction ID; `RP-0882` matches no other identifier in the flow and reads like an abbreviation of the purchase order `01-Order.xml:/Order/cbc:ID` = `RP-PO-26-0882`, which would be a different kind of reference.
- Condition: `PayerReference` either is absent or holds a payer reference that is distinct in meaning from the payment order reference and is explained by the story; it is not an order number.
- Options: (a, preferred) drop `PayerReference` (the payment order is already identified twice); (b) give it a value of its own kind, e.g. the payer's payment-run or batch reference.
- Needs decision: no

## Checked and consistent
- Amounts: `/RemittanceAdvice/cbc:TotalDebitAmount` = `9984000` − `/RemittanceAdvice/cbc:TotalCreditAmount` = `0` = `/RemittanceAdvice/cbc:TotalPaymentAmount` = `9984000` = `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `9984000` = the payable amount of the invoice (`10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9984000`); balance 0.
- Timing against the terms: issued 2026-05-19, after the discount period (ended 2026-04-30, `10-Invoice.xml:/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-30`) and before the due date (`10-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-20`): no discount taken, no penalty interest due. Consistent.
- Invoice reference: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `RR-INV-26-0894`, issue date `2026-04-20`, as in `10-Invoice.xml`.
- Payment data: RF reference `RF89RRINV260894` as payment ID and invoicing-party reference, equal to `10-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF89RRINV260894`; payee account equals the invoice's payee account; payer account is Rivermouth's own account; credit transfer `30` as requested. Check digits OK (`check_ids.py`).
- Purpose code `SUPP` (SupplierPayment) fits payment of a supplier invoice.
- Currency `XUF` as invoiced; the payer account is held in `XBL`, an ordinary bank conversion.
