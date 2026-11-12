# LLM review: 08-Reminder.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/08-Reminder.xml`, Git blob `e24bac5879420244e021d7b208594e7ca88f789d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows
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

### energy/08#F1 · Medium · Reminder in lume, while the debt and the payment asked for are in ferra
- XPath: `/Reminder/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentTerms/cbc:Note` = `Please pay the invoice in ferra and the surcharge with it.`
- XPath: `/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `1344672.00`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:Note` = `Invoice of 132480000 ferra, due 2026-05-03.`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:DebitLineAmount` = `1324800.00`
- XPath: `06-Invoice.xml:/Invoice/cbc:PaymentCurrencyCode` = `XUF`
- XPath: `06-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `1987200`
- XPath: `09-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `134467200`
- Why: `LegalMonetaryTotal/PayableAmount` is "The amount of the monetary total to be paid". The reminder states it as 1344672.00 XBL. But the debt is in ferra: the invoice is priced and payable in XUF by contract, and its terms already fix the one-month surcharge in ferra (1987200 XUF). The reminder's own note asks for payment in ferra, and the debtor pays 134467200 XUF (09). The reminder has no `PaymentCurrencyCode` ("A code signifying the currency used for payment in the Reminder"), so its structured data say "pay 1344672 lume", which is not what is asked. The ferra amount to pay appears only in a line note for the invoice, and not at all for the surcharge, so the payer has to convert back. Converting at the rate of the reminder date also attaches a currency risk to an amount the contract fixed in ferra. The arithmetic itself holds at 0.01. If the reason is that Bayvarra's statutory surcharge is assessed in lume (the header note speaks of "Bayvarra's surcharge"), the document does not say so.
- Condition: the amount the reminder asks to be paid is in the currency of the debt and of the payment (XUF: 132480000 + 1987200 = 134467200); or the reminder states the payment currency and the amount in it, and says why it is kept in lume.
- Options: (a) preferred: the reminder in XUF (DocumentCurrencyCode XUF, lines 132480000 and 1987200, payable 134467200), with no exchange rate needed, so it matches the invoice and the remittance advice directly; (b) if the seller must issue reminders in its own currency, add `PaymentCurrencyCode` XUF and a `PaymentExchangeRate`, and say in a note why the surcharge is assessed in lume.
- Needs decision: no
- From: money (F1), broad (F3), context (F2)

### energy/08#F2 · Medium · Language code in LocaleCode
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". `en` with listID `ISO 639` is a language code that repeats `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 of the 250 XML examples (counted by the parts over `*.xml`).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB`, with a locale list ID; (b) leave it out.
- Needs decision: no
- From: broad (F1), parties (F1), context (F1)

### energy/08#F3 · Medium · Province held in Region
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division and belongs in `CountrySubentity`, as in the supplier's bank address in this reminder (`/Reminder/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). It is a world convention: 219 occurrences in 104 of the 250 XML examples.
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense, and record why.
- Needs decision: no
- From: broad (F2), parties (F2)

### energy/08#F4 · Low · Customs numbers and the plant location on a payment reminder
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412877`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-105918`
- Why: a reminder asks for payment of an overdue invoice. The customs trader numbers of both parties and the location of the seller's gas plant play no part in that; they look copied from master data. On the export invoices 06/07 the customs numbers have a reason (they link the invoice to the customs declarations), but a reminder is not evidence for customs. The `InformationURI` is also the company's home page rather than a document about the location. Context counted customs trader identifiers in 2 of 3 Reminder, 28 of 33 Invoice and 11 of 12 RemittanceAdvice examples (`grep -l customs-trader` over `world/examples/*/*-<Type>.xml`).
- Condition: the parties of the reminder carry only data the reminder uses.
- Options: (a) preferred: leave the customs trader identifiers and `PhysicalLocation` out of the reminder; (b) keep them only with a stated reason.
- Needs decision: no
- From: parties (F5), context (F3)

### energy/08#F5 · Low · The contacts of a payment reminder are the sales and trading desks
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Gas sales`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Gas sales manager`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Energy trading`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Energy trader`
- Why: a reminder chases an overdue payment and adds a late surcharge. It comes from the supplier's credit control or accounts receivable and is addressed to the customer's accounts payable. The gas sales manager and the energy trader are the parties' commercial contacts, copied unchanged from `06-Invoice.xml`.
- Condition: the supplier's contact handles receivables and the customer's contact handles payables.
- Options: (a) preferred: accounts contacts on both sides (also in the remittance advice 09); (b) leave the contacts out.
- Needs decision: no
- From: broad (F6), parties (F3)

### energy/08#F6 · Low · The customer's Urvanian address and legal form are tagged as Bayvarran English
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Montebrio Power's English address renderings carry `languageID="en-XB"`. The same texts are `en-XU` in `09-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`, in 03 and in 05. The legal form is given in `qau` and `en-XU` there, but is one untagged text here. The parts counted 107 Urvanian addresses with an `en-XB` rendering in 39 `*.xml` files.
- Condition: the renderings of an Urvanian party's address and legal form carry the same `languageID` values in every example, whoever issues the document.
- Options: (a) preferred: tag the English renderings of Urvanian names `en-XU` and keep the `qau` legal form; (b) record an issuer-locale rule and apply it consistently.
- Needs decision: no
- From: broad (F4), parties (F4)

### energy/08#F7 · Low · A tax total of zero that says nothing about the surcharge's tax treatment
- XPath: `/Reminder/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- Why: the reminder carries a `TaxTotal` of 0.00 without a subtotal or category. The tax on the invoice amount was settled in the invoice (an exempt export). A late-payment surcharge is commonly outside the scope of VAT or sales tax (own knowledge, money). A bare zero states neither, so it may be there only because the element exists, which the agreed rules treat as a filler (money). Against this, the broad part argued that the zero states explicitly that no tax is charged, so that nothing is implied by absence (IND6). The merge cannot settle which reading the world's rules want: a zero says that no tax is charged, but not why.
- Condition: either the `TaxTotal` states the tax category and reason that apply to the surcharge, or there is no `TaxTotal`, or the world records that a bare zero is how a reminder says "no tax on the surcharge".
- Options: (a) preferred: a `TaxSubtotal` for the surcharge with the category the world's STT gives penalties (for example O, outside scope, with an exemption reason), because it states the reason and avoids implying anything by absence; (b) drop the `TaxTotal` (money's preference); (c) keep it as it is and record the convention.
- Needs decision: yes (whether a bare zero is a filler or a required statement)
- From: money (F4); refuted by broad ("Considered and refuted"); context did not keep it in its lens

### energy/08#F8 · Low · The surcharge line does not say which invoice and period it is charged on
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Note` = `One month late at 1.5 %.`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `19872.00`
- XPath: `/Reminder/cac:ReminderLine[1]/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `KG-INV-26-0157`
- Why: line 2 charges 1.5 % for one month late, but carries no `BillingReference` and no `ReminderPeriod`. Line 1 has both (the period from 2026-05-04). Only the line's position after line 1, its note and the arithmetic (1.5 % of 1324800.00 = 19872.00) link it to invoice KG-INV-26-0157. A reminder may list several overdue invoices, and the surcharge line should identify its base. Logistics refuted this: the reminder concerns one invoice only, and 09 refers to the reminder for the surcharge. The merge keeps it as Low, because nothing is ambiguous today but nothing in the line's structure says so either.
- Condition: the surcharge line identifies the invoice it is charged on (a `BillingReference` to KG-INV-26-0157) and, where useful, the period it covers.
- Options: (a) preferred: `BillingReference/InvoiceDocumentReference` KG-INV-26-0157 on line 2, with `ReminderPeriod` 2026-05-04 to 2026-06-03; (b) one line that carries both the invoice amount and the surcharge (`PenaltySurchargePercent` on line 1), if the world's reminders work that way.
- Needs decision: no
- From: broad (F5, first part), money (F2); refuted by logistics

### energy/08#F9 · Low · Surcharge amount given twice on the same line
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `19872.00`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Amount` = `19872.00`
- Why: `DebitLineAmount` is "The amount debited on this reminder line", and `Amount` is "The amount on this reminder line". For a surcharge line the debited amount is the amount of the line, so the second element repeats it without adding information. Line 1 has only `DebitLineAmount`. A value without a business reason of its own is a filler (IND5/IND6). Context refuted this because the two elements have different roles and agree. The merge keeps it: two elements that always agree add no information here, and the difference between their definitions is not used.
- Condition: line 2 carries the surcharge once, or the two elements carry different, explained amounts.
- Options: (a) preferred: drop `Amount`; (b) use `Amount` for the base the 1.5 % is charged on (1324800.00), which stretches "the amount on this reminder line".
- Needs decision: no
- From: broad (F5, second part), money (F3); refuted by context

## Checked and consistent
- Arithmetic: 132480000 XUF × 0.01 = 1324800.00 XBL (`/Reminder/cac:ReminderLine[1]/cbc:DebitLineAmount` = `1324800.00`, `/Reminder/cac:ReminderLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.01`); 1.5 % of 1324800.00 = 19872.00; 1324800.00 + 19872.00 = 1344672.00 = `/Reminder/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `1344672.00` = PayableAmount (all parts; recalculated in the merge).
- In ferra: 19872 × 100 = 1987200 = the invoice's `PenaltyAmount` = line 2 of 09. The rate XUF → XBL × 0.01 is the inverse of 1 XBL = 100 XUF in 06, 07 and 09 (broad, money).
- Reference: `ReminderLine[1]` refers to KG-INV-26-0157 of 2026-04-03, which is `06-Invoice.xml` (an invoice from Kelpstone Gas to Montebrio Power, issued 2026-04-03, due 2026-05-03, for March's gas, as the note says) (logistics, context, broad).
- Periods: `ReminderPeriod` 2026-05-04 → 2026-06-03 starts the day after the invoice's due date and equals its one-month penalty period. The reminder is issued on 2026-06-03 09:46, so "a month overdue" holds. The new due date 2026-06-10 lies after the issue date and after the remittance of 2026-06-06 in 09, so no second month of surcharge arises. `ReminderSequenceNumeric` 1 fits a first reminder (logistics, money, context).
- Parties: the accounting parties are the supplier and customer of 06, with the same identifiers, legal entities and tax schemes. The payee account XB45BLUM38522004817534 is the one named in 06, held by Kelpstone Gas Ltd, and its check digits pass (parties, logistics).

## Considered and refuted
- `/Reminder/cac:ReminderLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.01`: suspected misuse. Refuted because `ReminderLine/ExchangeRate` is "The rate of exchange between the currency of the Reminder and the currency of the document described in the BillingReference", which is exactly this use. Whether lume is the right reminder currency is F1 (from context).
- `/Reminder/cbc:Note` = `The invoice for March's gas is a month overdue: Bayvarra's surcharge of 1.5 % a month applies.`: suspected a contradiction between "Bayvarra's" (statutory?) surcharge and the invoice's contractual one. Refuted because the rate and period are those of the invoice's payment terms (XB-STD, Kelpstone's standard Bayvarran terms) (from money).
- `/Reminder/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `1344672.00`: suspected misuse of "the amount of an extended transaction line" for a sum of overdue amounts. Refuted because in a reminder the lines are the debited amounts, and their sum is the natural reading (from money).
- `/Reminder/cac:ReminderLine[1]/cbc:PaymentPurposeCode` = `SUPP`: suspected the wrong purpose. Refuted because "supplier payment" fits a payment for a supply of gas (from money).

## Changed in the merge
- money/F1 (Medium), broad/F3 (Low), context/F2 (Low, needs decision yes) → F1, Medium, needs decision no. Medium, because `PayableAmount` ("the amount … to be paid") holds an amount in a currency the reminder itself says is not the payment currency, and the ferra amount of the surcharge, which the purpose of the reminder depends on, appears nowhere. Needs decision is no, because both options keep the story (the same debt and surcharge). Context's point about a lume-assessed statutory surcharge is included in option (b).
- broad/F1, parties/F1, context/F1 → F2: combined, no change.
- broad/F2, parties/F2 → F3: Needs decision is no (broad said yes), because this is an encoding change; the same choice is made across the flow.
- parties/F5, context/F3 → F4: combined into one finding of copied master data; the InformationURI point comes from parties.
- broad/F6, parties/F3 → F5: combined, no change.
- broad/F4, parties/F4 → F6: combined; the untagged legal form comes from parties.
- money/F4 → F7: Needs decision is now yes, and an option (a) is added that states the category. Broad's refutation (IND6) is given as the counter-argument, and the merge cannot settle between the two.
- broad/F5 split into F8 (no link to the invoice and period; with money/F2) and F9 (`Amount` repeats `DebitLineAmount`; with money/F3), because they are two different problems with different conditions.
- The parts' refutations of candidates that other parts kept as findings (broad on the TaxTotal, logistics on the surcharge line's reference, context on `Amount`) are not carried over to "Considered and refuted": the merge disagrees with them, and they are answered in F7, F8 and F9.
