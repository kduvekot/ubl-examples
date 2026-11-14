# LLM review: 35-Reminder.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/35-Reminder.xml`, Git blob `8b2cb94295900deac8a0b1f1c5bdbbc86ecb0cc1` (committed)
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

## Checked and consistent
- `check_ids.py`: the payee account passes its check; no failures.
- All three billing references exist and are of the kind their elements name: invoice VI-INV-26-0221 (payable 20808.00, due 2026-04-30 as the line note says), credit note VI-CN-26-0222 (payable 515.20), debit note LPWD-DOC-26-0223 (payable 6.48).
- Dates: issue 5 May 15:23, five days after the due date; reminder period 2026-05-01 to 2026-05-05 = the five days overdue; new due date 2026-05-12 = issue + 7 days, as the terms say; exchange-rate dates of the issue day; the remittance advice (8 May) falls before the new due date.
- Arithmetic of the period: 20808.00 − 515.20 − 6.48 = 20286.32; 20286.32 × 0.08 × 5 / 365 = 22.23; total 20308.55, the amount paid in `36-RemittanceAdvice.xml`. The rate of 8 % a year is the penalty interest of the invoice.
- `cbc:ReminderSequenceNumeric` 1: the only reminder of the flow. ReminderTypeCode PAYMENT, PaymentMeansCode 30, AllowanceChargeReasonCode 48 (UNCL 5189): in their lists.

## Considered and refuted
- `/Reminder/cac:PrepaidPayment/cbc:ID`: `XB-WHT-26-04-1187` reads as a withholding-tax remittance for April, paid on 2 May (`cbc:PaidDate`) — refuted as a date problem: a remittance for the April period paid on 2 May is in order, and 69.48 = 72.00 − 1.80 − 0.72, the withholding of invoice, credit note and debit note. Whether a tax remittance is a "prepaid payment" of this reminder is for the money lens.
- `/Reminder/cac:ReminderLine[3]/cac:BillingReference/cac:DebitNoteDocumentReference/cbc:ID`: a debit note listed as a credit — refuted for this lens: the reference resolves and is a debit note; the direction of that document is a finding of `34-DebitNote.xml` (F2).
- `/Reminder/cac:ReminderPeriod/cbc:StartDate`: interest from 1 May although the contract's term counts from the accepted release — refuted here: the reminder follows the invoice's own due date consistently.
- `/Reminder/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate`: see the review of `26-Order.xml` (F8).
