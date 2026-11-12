# LLM review: 08-Reminder.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

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

### energy/08#F1 · Medium · Language code in LocaleCode
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` is the language. 362 occurrences in 213 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'`).
- Condition: LocaleCode holds a locale (e.g. `en-XB`) or is absent.
- Options: (a, preferred) `en-XB`; (b) omit.
- Needs decision: no

### energy/08#F2 · Medium · Province given in Region
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries…"; a province is an administrative division (`CountrySubentity`). World convention; 219 occurrences in 104 of 250 XML examples.
- Condition: the province of an Urvanian address is in `CountrySubentity`, or the world states why it is an economic region.
- Options: (a, preferred) move to `CountrySubentity`; (b) document the convention.
- Needs decision: yes

### energy/08#F3 · Low · Reminder in lume, but asks for payment in ferra
- XPath: `/Reminder/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `1344672.00`
- XPath: `/Reminder/cac:PaymentTerms/cbc:Note` = `Please pay the invoice in ferra and the surcharge with it.`
- Why: `PayableAmount` is "The amount of the monetary total to be paid", here 1 344 672 XBL, while the payment terms ask for payment in ferra, the invoice 06 is in ferra and its terms fix the surcharge in ferra (1 987 200 XUF). The payer has to convert back at a rate of the reminder's date to find the amount actually due; it pays 134 467 200 XUF (09-RemittanceAdvice.xml). The arithmetic holds at 0.01, but the reminder states the amount to pay in a currency in which it is not to be paid.
- Condition: the amount the reminder asks to be paid is stated in the currency in which it is to be paid, or the reminder says why it is in lume.
- Options: (a, preferred) issue the reminder in ferra (document currency XUF; no exchange rate needed), as the invoice; (b) keep lume and state the ferra amounts in the payment terms.
- Needs decision: no

### energy/08#F4 · Low · Urvanian address renderings tagged en-XB, elsewhere en-XU
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- Why: Montebrio Power's address carries `en-XU` in 03, 05 and 09, `en-XB` here and in 04, 06, 07.
- Condition: the renderings of one address carry the same language tag in every example.
- Options: (a, preferred) `en-XU`; (b) document the rule.
- Needs decision: no

### energy/08#F5 · Low · Surcharge line repeats its amount and is not tied to the invoice
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `19872.00`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Amount` = `19872.00`
- Why: the surcharge line carries the same amount as `DebitLineAmount` and as `Amount`, and has no `BillingReference` or `ReminderPeriod` saying which invoice and which period the 1.5 % is charged on (only the note "One month late at 1.5 %."). Line 1 has both.
- Condition: each amount of the line has its own meaning, and the surcharge line can be linked to the invoice and period it is charged on.
- Options: (a, preferred) keep `DebitLineAmount` only and add the invoice reference and the period 2026-05-04 – 2026-06-03; (b) keep `Amount` as the base of the surcharge (1 324 800) if that is what is meant.
- Needs decision: no

### energy/08#F6 · Low · Contacts are sales and trading desks on a payment reminder
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Gas sales`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Energy trading`
- Why: a payment reminder goes from the creditor's accounts receivable to the debtor's accounts payable; the gas sales manager and the energy trader are the contract contacts of the invoices.
- Condition: the contacts are those who deal with the overdue payment.
- Options: (a, preferred) receivables / payables contacts; (b) keep with a reason.
- Needs decision: no

## Checked and consistent
- 132 480 000 XUF × 0.01 = 1 324 800 XBL (line 1); 1.5 % of 1 324 800 = 19 872 XBL (line 2); total 1 344 672 XBL = LineExtensionAmount = PayableAmount.
- In ferra: 19 872 × 100 = 1 987 200 = 06-Invoice.xml `PenaltyAmount` and 09-RemittanceAdvice.xml line 2.
- Due date 2026-05-03, reminder 2026-06-03: one month late, ReminderPeriod 2026-05-04 – 2026-06-03 as in the invoice's PenaltyPeriod; ReminderSequenceNumeric 1, first reminder.
- Invoice reference KG-INV-26-0157 with issue date 2026-04-03 resolves to 06-Invoice.xml; payee account as in 06.

## Considered and refuted
- `/Reminder/cac:TaxTotal/cbc:TaxAmount`: suspected a filler tax total of 0 without subtotal — refuted: it states explicitly that no tax is charged on the surcharge, which avoids implying it by absence.
