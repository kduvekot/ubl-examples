# LLM review: 08-Reminder.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/08#F1 · Medium · A language code in LocaleCode
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` (ISO 639) repeats the language, not a locale. The same value occurs 362 times in 213 of 250 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: LocaleCode is absent or holds a locale (e.g. en-XB).
- Options: (a) preferred: `en-XB`; (b) leave it out.
- Needs decision: no

### energy/08#F2 · Low · Reminder stated in lume for an invoice and a surcharge to be paid in ferra
- XPath: `/Reminder/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentTerms/cbc:Note` = `Please pay the invoice in ferra and the surcharge with it.`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:DebitLineAmount` = `1324800.00`
- XPath: `06-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `1987200`
- XPath: `09-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:DebitLineAmount` = `1987200`
- Why: The invoice is in ferra, its payment terms already state the one-month surcharge in ferra (1987200 XUF), the reminder's own note asks for payment in ferra, and the remittance advice 09 pays the surcharge in ferra. The reminder nevertheless converts the invoice into lume (line 1, at 0.01) and states the surcharge in lume (19872 XBL), which the payer must convert back. The conversion serves no purpose stated in the document; if the reason is that Bayvarra's statutory surcharge is assessed in lume, the document does not say so.
- Condition: The currency of the reminder is the currency in which the reminder asks to be paid, or the document states why the surcharge is assessed in lume.
- Options: (a) preferred: state the reminder in ferra (invoice 132480000 XUF, surcharge 1987200 XUF as in the invoice's PenaltyAmount), without line exchange rates; (b) keep lume and say in a note that the statutory surcharge is assessed in lume.
- Needs decision: yes (how Bayvarra's surcharge is assessed)

### energy/08#F3 · Low · Customs numbers and plant location on a payment reminder
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412877`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-105918`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- Why: A reminder asks for payment of an overdue invoice. The customs trader numbers of both parties and the coordinates of the seller's gas plant play no part in that; they look copied from master data. Customs trader identifiers occur in 2 of 3 Reminder examples, 28 of 33 Invoice and 11 of 12 RemittanceAdvice examples (`grep -l customs-trader` over `world/examples/*/*-<Type>.xml`).
- Condition: The parties of the reminder carry only data the reminder uses.
- Options: (a) preferred: leave the customs trader identifiers and PhysicalLocation out of the reminder; (b) keep them only with a stated reason.
- Needs decision: no

## Checked and consistent
- Reference: InvoiceDocumentReference KG-INV-26-0157, issued 2026-04-03, resolves to 06-Invoice.xml (an invoice, same parties).
- Arithmetic: 132480000 XUF × 0.01 = 1324800 XBL; 1.5 % = 19872 XBL; 1324800 + 19872 = 1344672 = LineExtensionAmount = PayableAmount.
- Periods: ReminderPeriod starts 2026-05-04, the day after the invoice's due date (2026-05-03) and the start of the invoice's PenaltyPeriod; the note's "a month overdue" fits the issue date 2026-06-03.
- ReminderSequenceNumeric 1 fits a first reminder (no earlier reminder in the flow).

## Considered and refuted
- `/Reminder/cac:ReminderLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.01`: suspected misuse — refuted because ReminderLine ExchangeRate is defined as "The rate of exchange between the currency of the Reminder and the currency of the document described in the BillingReference", exactly this use (the question whether lume is the right reminder currency is F2).
- `/Reminder/cac:TaxTotal/cbc:TaxAmount` = `0.00`: suspected an empty total without a tax category — not kept in this lens; whether a surcharge is outside the tax scheme is a question for the money part.
- `/Reminder/cac:ReminderLine[2]/cbc:Amount` = `19872.00`: suspected a duplicate of DebitLineAmount — refuted because Amount ("The amount on this reminder line") and DebitLineAmount have different roles (the line's amount vs. its debit side) and agree.
