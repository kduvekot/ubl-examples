# LLM review: 11-CreditNote.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/11-CreditNote.xml`, Git blob `831c5f12acb5889efdae887718f56b4fd27594fc` (committed)
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

### utilities/11#F1 · Low · Credit for a meter over-reading without the meter, the test or the period it covers
- XPath: `/CreditNote/cbc:Note` = `The meter test found the meter over-reading by two cubic metres.`
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `2`
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cbc:CreditedQuantity` = `2`
- XPath: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `CSWC-INV-26-0319`
- Why: the credit rests on a meter test, but the credit note does not say which meter was tested (the flat's meter is CSW-W-71844 in `08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterNumber` = `CSW-W-71844`), when, or over which period the meter over-read. A meter that over-reads does so on every reading since the fault began, not only in one month; crediting exactly 2 m³ against the March invoice implies that the whole error fell into March (14 m³ billed, so the meter read 14 % high in that month). The lines carry no invoice period and no line reference to the invoice's line 1 (meter) and line 2 (levy), so the credit cannot be matched to the readings it corrects.
- Condition: the credit note identifies the meter (and the test) the credit rests on and the period of the over-reading, and the credited quantity is consistent with that period's readings.
- Options: (a, preferred) add the invoice period 2026-03-01 to 2026-03-31 and the meter (e.g. in the note or as a line reference to the invoice line that carries it), and say that the 2 m³ is the over-reading of March; (b) if the fault covered several months, credit the share of each billed month, referencing the invoices concerned.
- Needs decision: no

## Checked and consistent
- 2 m³ × 2.35 = 4.70; 2 m³ × 0.42 = 0.84; total 5.54; tax categories (E water, O levy) as in the invoice 09.
- BillingReference CSWC-INV-26-0319 (2026-04-02) resolves to 09-Invoice.xml; credited quantity 2 m³ is less than the 14 m³ billed there.
- Issued 2026-05-05, after the invoice and after the reminder 10-Reminder.xml (2026-05-01).

## Considered and refuted
- `/CreditNote/cbc:Note`: an over-reading of 2 m³ in 14 m³ (14 %) looks incompatible with the accuracy class 1 and the 2024 calibration stated in 08-UtilityStatement.xml — refuted because a meter test is done exactly when a meter is suspected of failing; a fault found by the test does not contradict the earlier calibration.

## Outside this review
- Timeline across documents: the reminder 10 (2026-05-01) demands the full 38.78 plus a fee four days before this credit of 5.54 is issued; whether the meter test was already pending when the reminder was sent is a question for the cross-flow review.
