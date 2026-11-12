# LLM review: 09-RemittanceAdvice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/09-RemittanceAdvice.xml`, Git blob `64ddc3389c441e3d1a8906ba4cb8cd22d97d45ce` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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
- Totals: 132480000 + 1987200 = 134467200 = `/RemittanceAdvice/cbc:TotalDebitAmount` = `134467200` = `/RemittanceAdvice/cbc:TotalPaymentAmount` = `134467200`; credits 0; LineCountNumeric 2 = number of lines.
- Line 1 against the invoice: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount` = `132480000` = `06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `132480000`, both in XUF, so no exchange rate is needed.
- Line 2 against the reminder: `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:DebitLineAmount` = `1987200` XUF = 19872.00 XBL × 100 (`/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:ExchangeRate/cbc:CalculationRate` = `100`), the surcharge line of energy/08; together the two lines equal the reminder's payable 1344672.00 XBL × 100 = 134467200 XUF. The rate is XBL → XUF, from the reminder's currency to the remittance advice's, as the element's definition asks.
- Payment means: PaymentID `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF41KGINV260157`, the RF reference of the invoice (check digits pass); payer account = Montebrio Power's ferra account (as payee in energy/03), payee account = Kelpstone's lume account of energy/06 and energy/08 (checks pass).
- Timing of the money: issued 2026-06-06, after the reminder (2026-06-03) and before its due date 2026-06-10, so one month's surcharge is the right amount.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:BillingReference/cac:ReminderDocumentReference/cbc:ID` = `KG-DOC-26-0159`: the line pays 1987200 XUF against a reminder whose payable amount is the whole debt (134467200 XUF) — refuted: line 1 pays the invoice part against the invoice itself, and the two lines together settle the reminder exactly; a `BillingReferenceLine` pointing at reminder line 2 would make it explicit, but nothing is ambiguous.
- `/RemittanceAdvice/cbc:DocumentCurrencyCode` = `XUF` against the lume reminder — refuted for this example: paying in ferra is what the invoice and the reminder's note ask; the currency mismatch lies in the reminder (see the money review of 08-Reminder).
- The same RF reference used for the invoice and for the surcharge — refuted: the surcharge belongs to that invoice, and the reminder asks to pay it with the invoice.
