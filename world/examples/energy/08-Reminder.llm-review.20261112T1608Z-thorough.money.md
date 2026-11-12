# LLM review: 08-Reminder.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/08-Reminder.xml`, Git blob `e24bac5879420244e021d7b208594e7ca88f789d` (committed)
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

## Findings

### energy/08#F1 · Medium · Reminder in lume while the debt and the payment asked for are in ferra
- XPath: `/Reminder/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `1344672.00`
- XPath: `/Reminder/cac:PaymentTerms/cbc:Note` = `Please pay the invoice in ferra and the surcharge with it.`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:Note` = `Invoice of 132480000 ferra, due 2026-05-03.`
- XPath: `06-Invoice.xml:/Invoice/cbc:PaymentCurrencyCode` = `XUF`
- XPath: `06-Invoice.xml:/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- XPath: `09-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `134467200`
- Why: `LegalMonetaryTotal/PayableAmount` is "The amount of the monetary total to be paid". The reminder states the amount to be paid as 1344672.00 XBL, but the debt is a ferra debt (the invoice is priced and payable in XUF by contract), the reminder itself asks for payment in ferra, and the debtor pays 134467200 XUF (energy/09). The reminder has no `PaymentCurrencyCode` ("A code signifying the currency used for payment in the Reminder"), so the structured data say "pay 1344672 lume", which is not what is asked; the ferra amount the debtor must pay appears nowhere as an amount, only in a line note (for the invoice) and not at all for the surcharge (1987200 XUF). The conversion to lume at the rate of the reminder date also puts a currency risk on an amount that the contract fixed in ferra: the amount due in ferra does not change when the rate moves, the lume figure does.
- Condition: the amount the reminder asks to be paid is in the currency of the debt and of the payment (XUF: 132480000 + 1987200 = 134467200), or the reminder states the payment currency and the amount in it.
- Options: (a) preferred: the reminder in XUF (DocumentCurrencyCode XUF, lines 132480000 and 1987200, payable 134467200), with no exchange rate needed, so it matches the invoice and the remittance advice directly; (b) if the seller must issue reminders in its own currency, add PaymentCurrencyCode XUF and a PaymentExchangeRate, so that the ferra amount follows from the document.
- Needs decision: no

### energy/08#F2 · Low · The surcharge line does not say which invoice it is charged on
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Note` = `One month late at 1.5 %.`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `19872.00`
- XPath: `/Reminder/cac:ReminderLine[1]/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `KG-INV-26-0157`
- Why: line 2 charges 1.5 % for one month late, but carries no BillingReference and no exchange rate; only its position after line 1 and the arithmetic (1.5 % of 1324800.00 = 19872.00) link it to invoice KG-INV-26-0157. A reminder may list several overdue invoices; the surcharge line should identify its base. It also has no ReminderPeriod, while line 1 has one (from 2026-05-04).
- Condition: the surcharge line identifies the invoice it is charged on (BillingReference to KG-INV-26-0157) and, where useful, the late period it covers.
- Options: (a) preferred: BillingReference/InvoiceDocumentReference KG-INV-26-0157 on line 2, with ReminderPeriod 2026-05-04 to 2026-06-03; (b) one line carrying both the invoice amount and the surcharge (PenaltySurchargePercent on line 1), if the world's reminders work that way.
- Needs decision: no

### energy/08#F3 · Low · Surcharge amount given twice on the same line
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `19872.00`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Amount` = `19872.00`
- Why: `DebitLineAmount` is "The amount debited on this reminder line", `Amount` is "The amount on this reminder line". For a surcharge line the debited amount is the amount of the line; the second element repeats it without adding information (line 1 has only DebitLineAmount). A value without its own business reason is a filler (IND5/IND6).
- Condition: line 2 carries the surcharge once, or the two elements carry different, explained amounts (e.g. the base amount and the surcharge).
- Options: (a) preferred: drop `Amount`; (b) use `Amount` for the base on which the 1.5 % is charged (1324800.00), if that is what the world wants to show — but then the definition "the amount on this reminder line" is stretched.
- Needs decision: no

### energy/08#F4 · Low · Tax total of zero that says nothing about the surcharge's tax treatment
- XPath: `/Reminder/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- Why: the reminder carries a TaxTotal of 0.00 without a subtotal or category. For the invoice amount, tax was settled in the invoice (exempt export); for the surcharge, a late-payment penalty is outside the scope of VAT/sales tax in common practice (own knowledge). A bare zero says neither; it is there because the element exists, which the agreed rules treat as a filler. If the world's STT has a treatment for late-payment surcharges, the reminder should state it (category and exemption reason); otherwise the TaxTotal has no business reason.
- Condition: either the TaxTotal states the tax category and reason that apply to the surcharge, or there is no TaxTotal.
- Options: (a) preferred: drop the TaxTotal; (b) a TaxSubtotal for the surcharge with the category the world's STT gives penalties (e.g. O, outside scope, with an exemption reason).
- Needs decision: no

## Checked and consistent
- Arithmetic: line 1, 132480000 XUF × 0.01 = 1324800.00 XBL (`/Reminder/cac:ReminderLine[1]/cbc:DebitLineAmount` = `1324800.00`, `/Reminder/cac:ReminderLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.01`); line 2, 1.5 % of 1324800.00 = 19872.00; total 1324800.00 + 19872.00 = 1344672.00 = `/Reminder/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `1344672.00` = PayableAmount.
- Against the invoice energy/06: amount 132480000 XUF, issue date 2026-04-03, due date 2026-05-03, surcharge 1.5 % per month = PenaltyAmount 1987200 XUF = 19872.00 XBL at 100; reminder period 2026-05-04 to 2026-06-03 = exactly the invoice's one-month penalty period, and the reminder is issued on 2026-06-03, so "a month overdue" holds.
- Exchange rate: XUF → XBL × 0.01 is the inverse of the rate 1 XBL = 100 XUF in energy/06, 07 and 09.
- Payee account: the same lume account of Kelpstone as in the invoices (check passes); the remittance advice energy/09 pays on 2026-06-06, before the new due date 2026-06-10, so no second month of surcharge arises.

## Considered and refuted
- `/Reminder/cbc:Note` = `The invoice for March's gas is a month overdue: Bayvarra's surcharge of 1.5 % a month applies.`: "Bayvarra's" surcharge (statutory?) against the contractual surcharge of the invoice — refuted: same rate and same period as the invoice's payment terms (XB-STD, Kelpstone's standard Bayvarran terms), so no contradiction.
- `/Reminder/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `1344672.00`: "amount of an extended transaction line" used for the sum of overdue amounts — refuted: in a reminder the lines are the debited amounts, and the sum of the lines is the natural reading.
- `/Reminder/cac:ReminderLine[1]/cbc:PaymentPurposeCode` = `SUPP`: supplier payment — refuted: fits a payment for a supply of gas.
