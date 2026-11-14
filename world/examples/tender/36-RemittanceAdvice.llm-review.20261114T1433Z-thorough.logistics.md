# LLM review: 36-RemittanceAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/36-RemittanceAdvice.xml`, Git blob `0d67d6237dbe199fe762a5dccb67b4360d07c700` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/36#F1 · Low · Additional document reference with only an ID, repeated on the interest line
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `PWD-PAY-AUTH-26-0412`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `PWD-PAY-AUTH-26-0412`
- Why: "A reference to an additional document associated with this document", without type, description or date; the document is not in the flow (grep for `>PWD-PAY-AUTH-26-0412<` over `world/examples/**/*.xml`: this example only). From the identifier it is the department's internal payment authorisation, which means nothing to the receiving supplier unless it is named. It is repeated inside the billing reference of line 4 (the interest) only, without a visible reason why the authorisation concerns that line and not the others.
- Condition: The reference states what the document is; it appears on a line only if it concerns that line in particular.
- Options: add `cbc:DocumentType` "Payment authorisation" at the header and remove the copy on line 4 (preferred), or say on line 4 that the interest needed a separate authorisation.
- Needs decision: no

### tender/36#F2 · Low · The advice does not say when the payment was or will be made
- XPath: `/RemittanceAdvice/cac:PaymentMeans`
- Why: A remittance advice notifies a payment; the supplier matches it to its bank statement by amount, reference and date. Amount (20308.55) and reference (RF48VIINV260221) are given, the date is not: there is no `cbc:PaymentDueDate` in the payment means and no payment period, only the issue date of the advice. The interest in line 4 was calculated to 5 May (`35-Reminder.xml`), so the value date also decides whether more interest is due. Missing detail the document could carry.
- Condition: The advice states the date on which the payment is executed.
- Options: `cac:PaymentMeans/cbc:PaymentDueDate` 2026-05-08 (preferred).
- Needs decision: no

## Checked and consistent
- `check_ids.py`: creditor reference RF48VIINV260221 and both account numbers pass their checks.
- All four billing references exist and are of the kind their elements name: invoice VI-INV-26-0221 (20808.00), credit note VI-CN-26-0222 (515.20), debit note LPWD-DOC-26-0223 (6.48), reminder VI-DOC-26-0224 with issue date 2026-05-05, which is the reminder's issue date; the interest 22.23 is the reminder's charge.
- Totals: debit 20808.00 + 22.23 = 20830.23; credit 515.20 + 6.48 = 521.68; payment 20830.23 − 521.68 = 20308.55 = the reminder's payable amount. `cbc:LineCountNumeric` 4 = four lines.
- Issue date 8 May is after the reminder (5 May) and before its due date (12 May). The payment reference is the one the invoice asked to quote; the payee account is the invoice's.
- PaymentMeansCode 30 = credit transfer.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cac:BillingReference/cac:DebitNoteDocumentReference/cbc:ID`: a debit note on the credit side — refuted here: the reference resolves; the direction of the debit note is a finding of `34-DebitNote.xml` (F2).
- `/RemittanceAdvice/cbc:ID`: `LPWD-RM-26-0225` continues the flow-wide running number — refuted: an identifier of the kind the element names, in the payer's own prefix.
