# LLM review: 04-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/04#F1 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VI-BANK-26-04`
- Why: the reference has no type code, description or issuer, so the receiver (Ferrano Energy) cannot tell what VI-BANK-26-04 is (a bank statement? the payment order? a batch?). The payment order itself is already referenced (PaymentOrderReference and InstructionID VI-PAY-26-0313). A reference with only an ID must say what it refers to where that is not obvious. The same pattern occurs in 07 (BS-BANK-26-04) and 14 (VT-BANK-26-04).
- Condition: the reference states what kind of document it is (type code and/or description), or it is absent if the remittance does nothing with it.
- Options: (a, preferred) add a DocumentTypeCode or DocumentDescription that says what the document is and why the payee needs it; (b) remove it.
- Needs decision: no

## Checked and consistent
- BillingReference and line DocumentReference FE-INV-26-0313 (issue date 2026-04-02) resolve to 02-Invoice.xml, an invoice, as the DocumentTypeCode says.
- Payment reference RF58FEINV260313 (PaymentID, InvoicingPartyReference at header and line) is the invoice's PaymentID; check digit OK (check_ids.py).
- Payee account XU080351041600000004084431 is the invoice's PayeeFinancialAccount; payer account XU790351041600000000209458 check digit OK.
- Dates: issued 2026-04-10, within the invoice's settlement period 2026-04-02 to 2026-04-12, so the discount note is consistent in time; invoice period 2026-03-01 to 2026-03-31 as in the invoice.
- Amounts: 15,096,168 − 301,923 = 14,794,245; 2 % of 15,096,168 = 301,923.36; tax 2,516,028 = the invoice's VAT.
- Document number VI-RM-26-0316 follows the flow's sequence (invoice 0313, statements 0314, 0315).

## Considered and refuted
- `/RemittanceAdvice/cbc:PayerReference`: a second reference (VI-0313) for the same payment order as PaymentOrderReference VI-PAY-26-0313 — refuted because PayerReference may be the payer's own internal reference (e.g. its payables voucher), distinct from the order to its bank.
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID`: the invoice referenced twice in the line (BillingReference and DocumentReference) — refuted for this lens: both resolve to the same existing invoice and agree in ID and date; whether the duplication is needed is a question for the context part.
