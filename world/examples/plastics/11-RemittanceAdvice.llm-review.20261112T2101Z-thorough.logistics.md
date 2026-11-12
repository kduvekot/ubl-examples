# LLM review: 11-RemittanceAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

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

### plastics/11#F1 · Low · The invoice is referenced twice in the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `RR-INV-26-0894`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `RR-INV-26-0894`
- Why: The line already refers to the invoice through `BillingReference/InvoiceDocumentReference`, the element meant for "a reference to an invoice". The generic `DocumentReference` ("a reference to a document associated with this remittance advice line") repeats the same invoice with the same issue date, adding only a document type code. A second reference to the same document has no business reason of its own (no fillers).
- Condition: The invoice is referenced once in the line; any `DocumentReference` refers to another document.
- Options: (a) preferred: drop the `DocumentReference`, because `InvoiceDocumentReference` already says what it refers to; (b) keep only the `DocumentReference` (less specific, so less good).
- Needs decision: no

## Checked and consistent
- `InvoiceDocumentReference` `RR-INV-26-0894`, issued 2026-04-20, resolves to the invoice 10 with the same issue date.
- `InvoicingPartyReference` `RF89RRINV260894` is the invoice's creditor reference (10, `PaymentID`), check digits valid (ISO 11649).
- Debit 9984000 XUF = invoice 10 payable amount; balance 0.
- Issued 2026-05-19, one day before the due date 2026-05-20 (10).

## Considered and refuted
- `/RemittanceAdvice/cbc:PaymentOrderReference` = `RP-PAY-26-0882`: suspected that the payer's payment order reuses the order number 0882 — refuted as a finding because the payer's own numbering may tie the payment to its purchase order; it is not used as an order reference.
