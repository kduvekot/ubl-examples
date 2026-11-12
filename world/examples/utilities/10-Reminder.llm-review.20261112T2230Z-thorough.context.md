# LLM review: 10-Reminder.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/10-Reminder.xml`, Git blob `11e7db92f151d2164c7a773e47dfe430253bad7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### utilities/10#F1 · Medium · The supplier's ledger accounts given as the buyer's cost codes
- XPath: `/Reminder/cbc:AccountingCostCode` = `1210`
- XPath: `/Reminder/cbc:AccountingCost` = `Household receivables`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:AccountingCostCode` = `8320`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:AccountingCost` = `Reminder fees`
- Why: Reminder/AccountingCost is "The buyer's accounting code, applied to the Reminder as a whole", and on the line "The buyer's accounting cost centre for this reminder line". The buyer is a private household (Robin Ashdale), which keeps no cost centres. "Household receivables" is the water company's receivables account, and "Reminder fees" its income from fees: the seller's accounts in elements defined for the buyer's.
- Condition: The accounting cost elements hold the buyer's cost codes, or are absent.
- Options: (a, preferred) remove them; the seller's own ledger accounts have no place in these elements.
- Needs decision: no

### utilities/10#F2 · Low · The fee is a return fee, but its tax reason says compensation for late payment
- XPath: `/Reminder/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Compensation for late payment`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Note` = `The fee for the returned direct debit.`
- Why: The 5.00 is described as the fee for the returned direct debit (the bank's charge passed on), while the tax reason calls it compensation for late payment. The two texts give different reasons for the same amount.
- Condition: Note and exemption reason describe the same charge.
- Options: (a, preferred) align the reason with the note ("Return fee passed on", if out of scope for that reason), or the note with the reason.
- Needs decision: no

### utilities/10#F3 · Low · Penalty surcharge stated as 0 % although the invoice's terms apply 1.5 %
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:PenaltySurchargePercent` = `0`
- XPath: `09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`
- Why: PenaltySurchargePercent is "The penalty for late payment, expressed as a percentage". The invoice's terms charge 1.5 % per month from 2026-04-24, and the reminder is issued on 2026-05-01, inside that period. A 0 % on the fee line neither applies those terms nor says they are waived; on the fee line a percentage has nothing to apply to.
- Condition: The reminder either applies the invoice's surcharge (on line 1) or states that it is waived; the fee line carries no 0 % filler.
- Options: (a, preferred) remove the 0 % and, if the surcharge is waived for this first reminder, say so in a note; (b) charge the surcharge on line 1.
- Needs decision: yes

### utilities/10#F4 · Low · Tax point date on a reminder without tax
- XPath: `/Reminder/cbc:TaxPointDate` = `2026-05-01`
- Why: TaxPointDate is "the point at which tax becomes applicable". The only charge, the 5.00 fee, is outside the scope of tax with tax 0.00, so there is no tax point to state; the value equals the issue date and adds nothing.
- Condition: TaxPointDate only when the reminder charges something taxable.
- Options: (a, preferred) remove.
- Needs decision: no

### utilities/10#F5 · Medium · A language code in LocaleCode
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" (ISO 639) is a language code. World-wide pattern (362 elements in 213 examples, grep over `*.xml`).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a, preferred) remove.
- Needs decision: no

### utilities/10#F6 · Low · Customer's account in a reminder that asks for a credit transfer
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: The reminder asks the customer to pay by credit transfer to the company's account; the customer's own account (the mandate account) is not used.
- Condition: The reminder carries no customer account, or uses it.
- Options: (a, preferred) remove.
- Needs decision: no

## Checked and consistent
- Line 1 reminds of `09-Invoice.xml` (38.78, issued 2026-04-02); the return notice BLUM-RTN-26-04-0193 of 2026-04-24 follows the debit of 2026-04-23; total 38.78 + 5.00 = 43.78; due 2026-05-11 = ten days after issue, as the terms say.
- ReminderSequenceNumeric 1: first reminder; ReminderPeriod from the due date to the reminder date.
- The bank's register ID 20411370 and name agree with the bank in the flow's accounts (BLUMXBLX, Bank of Lumeport).

## Considered and refuted
- `/Reminder/cac:PayeeParty`: payee equals the supplier — refuted because "The Party who receives the Payment" has no "if different" condition.
- `/Reminder/cac:PaymentMeans/cbc:PaymentMeansCode`: credit transfer instead of direct debit — refuted because the terms explain it ("the next collection will be by direct debit again").

## Outside this review
- `11-CreditNote.xml` credits 2 m³ of the reminded invoice four days later; whether the reminded amount should then be reduced is a timeline question across documents.
