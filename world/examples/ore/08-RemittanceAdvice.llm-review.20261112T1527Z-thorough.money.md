# LLM review: 08-RemittanceAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/08-RemittanceAdvice.xml`, Git blob `ba4a236a16cc3b9d330f7fd945ee82d84e44ac69` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/08#F1 · Low · Two different references for the same payer's payment order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0304`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VI-0304`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VI-PAY-26-0304`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to the payer's bank" and PayerReference "An internal reference to the payer's order for payment". Both name the payer's own order for this payment, yet they carry two different values; the instruction ID agrees with the first. A reader cannot tell what `VI-0304` identifies that `VI-PAY-26-0304` does not.
- Condition: each payer-side reference identifies a distinguishable object (or the two that mean the same carry the same value, or one is left out).
- Options: (a) preferred: drop PayerReference, since PaymentOrderReference and InstructionID already identify the payment order; (b) give PayerReference a value that is clearly a different payer-side object (e.g. the payer's payment run) if the story has one.
- Needs decision: no

### ore/08#F2 · Low · The paid invoice referenced twice on the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SM-INV-26-0312`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SM-INV-26-0312`
- Why: the line already identifies the settled invoice through BillingReference/InvoiceDocumentReference ("A reference to an invoice"); the general DocumentReference ("A reference to a document associated with this remittance advice line") repeats the same invoice with the same issue date and adds only a type code. It tells the payee nothing more about what is settled.
- Condition: the settled invoice is referenced once on the line, unless the second reference carries a different document.
- Options: (a) preferred: keep the BillingReference, which is the dedicated element, and drop the DocumentReference; (b) use DocumentReference only for another document the payment relates to (e.g. the order).
- Needs decision: no

## Checked and consistent
- `/RemittanceAdvice/cbc:TotalPaymentAmount` = `17037943` = `/RemittanceAdvice/cbc:TotalDebitAmount` = `17037943` − `/RemittanceAdvice/cbc:TotalCreditAmount` = `0` = `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `17037943` = `07-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `17037943`; balance `0`.
- Issued 2026-04-09: after the end of the settlement-discount period (`07-Invoice.xml:/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-03-21`), so no discount is taken, and before the due date 2026-04-10 — consistent.
- Invoice ID and issue date agree with 07-Invoice.xml; the RF reference quoted (`/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF73SMINV260312`) is the one the invoice requested, and passes its check.
- Payee account `XU420351041700000000104729` is the account named in the invoice; payer account `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XU790351041600000000209458` passes the IBAN-style check, is held in XUF in Valdara's name at the Ferrano main branch (`03510-41600`, embedded in the account number), and is Valdara's account in all 10 XML examples that carry it (`grep -rl --include='*.xml'`), always with the name Valdara Industries SUA.
- Purpose code `SUPP` (SupplierPayment) and credit transfer (4461 code 30) fit the payment of a supplier invoice.

## Considered and refuted
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF73SMINV260312`: suspected misuse of an element meant for a payer-side reference — refuted: its definition ("…This may have been requested of the payer by the payee to accompany the payer's remittance") fits the creditor reference the invoice asked to be quoted.
- No remittance advice for the freight invoice 06-Invoice.xml in the flow — refuted as a finding of this example: the flow need not show every payment.
