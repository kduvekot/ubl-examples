# LLM review: 10-Reminder.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/10-Reminder.xml`, Git blob `11e7db92f151d2164c7a773e47dfe430253bad7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/10#F1 · Medium · The water company's own ledger accounts given as the buyer's accounting codes
- XPath: `/Reminder/cbc:AccountingCostCode` = `1210`
- XPath: `/Reminder/cbc:AccountingCost` = `Household receivables`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:AccountingCostCode` = `8320`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:AccountingCost` = `Reminder fees`
- Why: In a Reminder, UBL defines these as "The buyer's accounting code, applied to the Reminder as a whole" and, on the line, "The buyer's accounting cost centre for this reminder line". The buyer is a private household, Robin Ashdale, which keeps no cost centres. "Household receivables" and "Reminder fees" are the water company's own accounts (a receivables account and a fee income account): the seller's bookkeeping in elements defined for the buyer's.
- Condition: The Reminder carries no accounting cost, or it carries a code of the buyer's.
- Options: (a, preferred) remove both pairs; a household has no cost accounts.
- Needs decision: no
- From: broad (F1), money (F1), context (F1)

### utilities/10#F2 · Medium · A language code in LocaleCode
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. Recounted in the merge: 362 occurrences in 213 files over `world/examples/*/*.xml`.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale value such as `en-XB` with a list that defines it.
- Needs decision: no
- From: broad (F2), parties (F1), context (F5)

### utilities/10#F3 · Low · Tax point date on a reminder without tax
- XPath: `/Reminder/cbc:TaxPointDate` = `2026-05-01`
- Why: TaxPointDate is "the point at which tax becomes applicable". The only charge, the 5.00 fee, is outside the scope of tax with tax 0.00, so there is no tax point to state; the value equals the issue date and adds nothing.
- Condition: TaxPointDate only when the reminder charges something taxable.
- Options: (a, preferred) remove it.
- Needs decision: no
- From: context (F4)

### utilities/10#F4 · Low · Signature without method or reason
- XPath: `/Reminder/cac:Signature/cbc:ID` = `CSWC-SIG-26-REM`
- Why: Only an ID and the signatory; nothing says how or why the reminder is signed (no fillers). A convention across the world: 137 of the 147 Signature aggregates in `world/examples/*/*.xml` hold only ID and SignatoryParty (counted with lxml in the merge).
- Condition: A signature with a reason and the data that make it one, or none.
- Options: (a, preferred) remove it; (b) add the signature method and reason.
- Needs decision: yes
- From: broad (F4)

### utilities/10#F5 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: A water utility serving a state's capital is a large organisation; `SMALL` ("Small enterprise") is implausible. 25 companies of the world are registered on 1 January 1996 (parties' count); recounted in the merge: 271 occurrences in 181 files over `world/examples/*/*.xml`. Both look like a default description (no fillers).
- Condition: Size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a, preferred) a size that fits a state water utility and a registration date of its own; (b) drop the two elements where the documents do not need them.
- Needs decision: yes
- From: parties (F2)

### utilities/10#F6 · Low · The household's bank account in a reminder that asks for a credit transfer
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: The reminder asks the household to pay by credit transfer to the company's account; the household's own account plays no part in that, and reads as copied master data. The parties part refuted it: it is the account from which the returned direct debit was taken, which the reminder is about, and from which the next debit will be taken. The merge keeps it Low: the reminder identifies the returned debit through the bank's return notice and the invoice, and does nothing with the account itself.
- Condition: The account is present only if the reminder uses it.
- Options: (a, preferred) remove it.
- Needs decision: no
- From: money (F5), context (F6); refuted by parties (argument above)

### utilities/10#F7 · Low · Credit transfer requested without the payment reference
- XPath: `/Reminder/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `/Reminder/cac:PaymentTerms/cbc:Note` = `Please pay within ten days by credit transfer; the next collection will be by direct debit again.`
- Why: The reminder asks the household to pay 43.78 by credit transfer, but gives no PaymentID or instruction note; the invoice's creditor reference (`09-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF46CSWCINV260319`) is not repeated, so the company cannot match the incoming payment automatically. That matching is what the reminder's payment means are for.
- Condition: The reminder's payment means carry the reference the payer is to quote.
- Options: (a, preferred) PaymentID with RF46CSWCINV260319, or a new RF reference for the 43.78.
- Needs decision: no
- From: money (F4)

### utilities/10#F8 · Low · The tax exemption reason calls the fee compensation for late payment; the line calls it a returned-debit fee
- XPath: `/Reminder/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Compensation for late payment`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Note` = `The fee for the returned direct debit.`
- Why: The only taxable item is the 5.00 fee, which the line describes as the fee for the returned direct debit (notice BLUM-RTN-26-04-0193), i.e. a charge for the bank's return and its handling, not compensation for lateness; the two texts give different reasons for the same amount. TaxExemptionReason ("The reason for tax being exempted") is also used for category O, which is not an exemption (as in 06 and 09).
- Condition: The exemption reason (if any is kept for O) and the line note describe the same charge.
- Options: (a, preferred) a reason that names the returned-debit fee, e.g. "Fee for a returned direct debit, outside the scope of tax" (or none for O); (b) the note aligned with the reason, if the 5.00 is meant as late-payment compensation.
- Needs decision: no
- From: broad (F3, part), money (F3), context (F2)

### utilities/10#F9 · Low · The invoice's late-payment surcharge neither charged nor said to be waived; a 0 % surcharge on the fee line
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:PenaltySurchargePercent` = `0`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:DebitLineAmount` = `38.78`
- XPath: `09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`
- Why: PenaltySurchargePercent is "The penalty for late payment, expressed as a percentage". Invoice 09 sets 1.5 % (PenaltyAmount 0.58) for payment after 2026-04-23, and the reminder of 2026-05-01 lies inside that penalty period. It claims the overdue 38.78 without the surcharge and does not say it is waived; instead it puts 0 % on the line of the return fee, where no lateness applies and a percentage has nothing to apply to (no fillers). The broad part refuted the missing surcharge (the invoice says penalties "may apply", and waiving is legitimate); that is right for the waiver itself, but the reminder does not say it waives, and the 0 % on the fee line stays a filler. Whether the company waives the surcharge for a first reminder is a story question.
- Condition: The reminder either charges the invoice's surcharge on the overdue line or states that it is waived, and the fee line carries no surcharge percent.
- Options: (a, preferred) remove the 0 % from line 2 and add a note that the surcharge is waived for this first reminder; (b) charge the surcharge (0.58) on line 1.
- Needs decision: yes
- From: broad (F3, part), money (F2), context (F3); broad's refutation of the missing surcharge answered above

### utilities/10#F10 · Low · Line amount repeated on the fee line
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:Amount` = `5.00`
- XPath: `/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `5.00`
- Why: ReminderLine/Amount ("The amount on this reminder line") repeats the debit line amount; line 1 has only the debit amount. One of the two is redundant, and the two lines state their amount differently.
- Condition: Each line states its amount once, in the same way on both lines.
- Options: (a, preferred) drop Amount on line 2.
- Needs decision: no
- From: broad (F5)

## Checked and consistent
- Amounts (redone in the merge): 38.78 (`09-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`) + 5.00 = 43.78 = LineExtensionAmount = PayableAmount; LineCountNumeric 2; fee outside the scope of tax (O), taxable 5.00, tax 0.00.
- Story: debit due 2026-04-23 (09), bank return notice BLUM-RTN-26-04-0193 of 2026-04-24, reminder 2026-05-01 (ReminderSequenceNumeric 1, ReminderPeriod from the invoice's due date); new due date 2026-05-11 = 2026-05-01 + 10 days, as the note says.
- Reference CSWC-INV-26-0319 of 2026-04-02 is `09-Invoice.xml`; payee account XB21BLUM38010004189160 is the company's account, as in 06 and 09.
- The return notice's IssuerParty is the Bank of Lumeport (`20411370`), the bank of Robin Ashdale's debited account (BLUMXBLX), with the same register number elsewhere in the world; SignatoryParty is the water company, the issuer.
- Supplier and customer are those of `09-Invoice.xml`, described the same way.
- check_ids.py: both accounts correct.

## Considered and refuted
- `/Reminder/cac:PayeeParty/cac:PartyName/cbc:Name` = `Coastal State Water Company`: payee repeats the supplier — refuted, Reminder/PayeeParty ("The Party who receives the Payment") has no "if different" condition, and the reminder changes the payment means to a credit transfer (from broad, parties, context).
- `/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount`: late-payment surcharge of the invoice not charged — refuted by broad, waiving it is legitimate; the merge keeps the missing statement of the waiver and the 0 % filler as F9 (from broad).
- `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID`: refuted by parties (the account of the returned debit) — the merge keeps it as F6 (from parties).
- `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`: a receivables contact was expected — refuted, customer service is a usual addressee for a household's questions about a returned payment (from parties).
- `/Reminder/cac:PaymentMeans/cbc:PaymentMeansCode`: credit transfer instead of direct debit — refuted, the terms explain it ("the next collection will be by direct debit again") (from context).

## Changed in the merge
- broad/F3 split: the tax-reason part joined money/F3 and context/F2 as F8; the penalty part joined money/F2 and context/F3 as F9 (different elements and decision status).
- broad/F4 → F4: Needs decision no → yes, aligned with the air, rail and utilities 01–07 merges (signature convention).
- money/F3 (Needs decision no) and context/F2 (no) → F8: no; broad's yes for its combined finding applies to F9.
- parties/F2 → F5: count recalculated (271 in 181 files).

## Outside this review
- `11-CreditNote.xml` (2026-05-05) credits 5.54 against invoice 09 four days after this reminder demanded the full 43.78 by 2026-05-11; whether the reminded amount should then be reduced (to 38.24) is a timeline question across documents (broad, money, context).
