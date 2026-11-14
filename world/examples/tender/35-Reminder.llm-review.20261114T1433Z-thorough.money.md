# LLM review: 35-Reminder.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

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

## Findings

### tender/35#F1 · High · Multiplier factor × base amount is 1622.91, not the 22.23 charged
- XPath: `/Reminder/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.08`
- XPath: `/Reminder/cac:AllowanceCharge/cbc:BaseAmount` = `20286.32`
- XPath: `/Reminder/cac:AllowanceCharge/cbc:Amount` = `22.23`
- Why: `MultiplierFactorNumeric` is "a number by which the base amount is multiplied to calculate the actual amount of this allowance or charge". 0.08 × 20286.32 = 1622.91. The amount charged, 22.23, is 8 % a year for the five days of the reminder period (20286.32 × 0.08 × 5 / 365 = 22.23): the element carries the annual interest rate, not the factor. The factor that yields the amount is 0.08 × 5 / 365 = 0.0010959.
- Condition: `MultiplierFactorNumeric` × `BaseAmount` = `Amount` (to the cent), or there is no multiplier factor and the rate and the days are stated where UBL has elements for them.
- Options: (a, preferred) remove the multiplier factor and state rate and days in the charge's reason ("8 % a year, 5 days, 1 to 5 May"); the rate itself is in the invoice's `PenaltyInterestRate`; (b) set the factor to 0.0010959 (which gives 22.23).
- Needs decision: no

### tender/35#F2 · High · Interest runs from 1 May, on a due date that the contract does not give
- XPath: `/Reminder/cac:ReminderPeriod/cbc:StartDate` = `2026-05-01`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:Note` = `The release's invoice, due on 2026-04-30.`
- XPath: `/Reminder/cbc:Note[2]` = `The balance of the first release is overdue; Urvania's statutory interest applies.`
- Why: the reminder treats the invoice as overdue since 30 April, the date the invoice computed from its own date (32#F3 of this part). The contract's term is `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` The release cannot have been accepted before the installation was complete, which was late (34-DebitNote.xml of 6 April charges three days); thirty days after an acceptance in April end in May, at the earliest a few days after 30 April and possibly after the reminder's own date. Under the contract the balance was not, or not for five days, overdue on 5 May, and the interest of 22.23 has no basis or a smaller one. The interest is also called Urvania's statutory interest, on a contract under Bayvarran procurement law that provides none (32#F6).
- Condition: the day from which the reminder charges interest is the day after the due date the contract yields, and the rate is one the contract or its governing law gives the supplier.
- Options: (a, preferred) decide the due date with 32#F3 and recalculate the reminder period, the days and the interest here and in 36; (b) change the contract's payment term to the invoice date, which makes this reminder right as it is.
- Needs decision: yes

### tender/35#F3 · High · The department's debit note is entered as a credit
- XPath: `/Reminder/cac:ReminderLine[3]/cbc:CreditLineAmount` = `6.48`
- XPath: `/Reminder/cac:ReminderLine[3]/cac:BillingReference/cac:DebitNoteDocumentReference/cbc:ID` = `LPWD-DOC-26-0223`
- Why: the line reduces the customer's balance by the amount of a debit note. The debit note referenced names the supplier as creditor and the department as debtor (`34-DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`), so by that document the 6.48 would be a further debt of the customer and belong in `DebitLineAmount`. The reminder follows the debit note's intention (a penalty owed by the supplier), not its encoding. One of the two documents is wrong; see 34#F1 of this part.
- Condition: the reminder line's side (debit or credit) agrees with who is creditor and debtor in the referenced document.
- Options: (a, preferred) correct the parties of the debit note (34#F1 option (a)); this line then stands; (b) if the penalty becomes a credit note of the supplier, reference it as a credit note here.
- Needs decision: yes

### tender/35#F4 · Medium · The withholding tax paid to the tax office is listed as a prepaid payment, but the balance is not reduced by it
- XPath: `/Reminder/cac:PrepaidPayment/cbc:PaidAmount` = `69.48`
- XPath: `/Reminder/cac:PrepaidPayment/cbc:ID` = `XB-WHT-26-04-1187`
- XPath: `/Reminder/cac:PrepaidPayment/cbc:PaidDate` = `2026-05-02`
- XPath: `/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20308.55`
- Why: `PrepaidPayment` is "a prepaid payment", i.e. a payment already made towards the amounts of the document. 69.48 is the withholding tax of the three billing documents (72.00 − 1.80 − 0.72), which the customer paid to the tax office, not to the supplier. The reminder's lines are already net of it (20808.00, 515.20 and 6.48 are the payable amounts after withholding), and the totals do not deduct it: 20808.00 − 515.20 − 6.48 + 22.23 = 20308.55, with no `PrepaidAmount`. So the document shows a prepaid payment that is not a payment on the reminded balance; a reader who deducts prepaid payments, as the element invites, arrives at 20239.07. That the supplier knows the customer's tax payment reference three days after it was made is also unexplained.
- Condition: every `PrepaidPayment` of the reminder is a payment received on the reminded amounts and is reflected in the monetary total (`PrepaidAmount`); information about withholding tax is carried where it does not read as a payment on account.
- Options: (a, preferred) remove the prepaid payment from the reminder (the withholding is already in the invoice, credit note and debit note); (b) remind the gross amounts and show the withholding as prepaid, with `PrepaidAmount` 69.48 in the total.
- Needs decision: no

### tender/35#F5 · Low · Currency codes and exchange rates with nothing to convert, one of them from the lume to the lume
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/Reminder/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Reminder/cbc:TaxCurrencyCode` = `XUF`
- XPath: `/Reminder/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- Why: `PaymentAlternativeExchangeRate` is "the exchange rate between the document currency and the payment alternative currency". Both are the lume, so the element states that one lume is one lume. The reminder has no price (pricing currency and pricing rate, with the forward contract of 2 January again, convert nothing) and no tax amount other than a bare 0.00 in lume (tax currency and tax rate convert nothing). Only the payment currency and its rate have a use: the balance is to be paid into a ferra account.
- Condition: a currency code and its exchange rate are present only if the document contains an amount in, or a conversion into, that currency, and no exchange rate has the same source and target.
- Options: (a, preferred) keep `PaymentCurrencyCode`, `PaymentAlternativeCurrencyCode` and `PaymentExchangeRate`; remove the alternative, pricing and tax exchange rates and the pricing and tax currency codes; (b) none seen.
- Needs decision: no

### tender/35#F6 · Low · Zero tax without scheme or category, and a tax representative, on a reminder
- XPath: `/Reminder/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Reminder/cbc:TaxPointDate` = `2026-05-05`
- XPath: `/Reminder/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: the reminder supplies nothing; its only new amount is interest. The tax total of 0.00 names no scheme or category, so it does not say which tax was considered for the interest or why none applies; a tax point date is given for it; and the supplier's Bayvarran tax representative is named although the document carries no Bayvarran tax of the supplier (32#F8 of this part).
- Condition: the reminder states a tax only if one applies to its interest, with scheme, category and reason; a tax point date and a tax representative only with such a tax.
- Options: (a, preferred) remove the tax total, the tax point date and the representative; (b) give the tax total a subtotal for the interest (22.23, outside the scope of VAT).
- Needs decision: no

## Checked and consistent
- Balance: 20808.00 (invoice, payable after withholding) − 515.20 (credit note) − 6.48 (penalty) = 20286.32 = `LineExtensionAmount` = interest base; + 22.23 = 20308.55 = `PayableAmount`; `ChargeTotalAmount` 22.23 = the one charge.
- Interest: 20286.32 × 8 % × 5 / 365 = 22.23 (22.2316); five days are 1 to 5 May, the reminder period; 8 % a year, simple, is the invoice's `PenaltyInterestRate`. Reason code 48 ("Interest on arrears") and the text "Statutory interest" agree; `ChargeIndicator` true.
- Each line's amount equals the payable amount of the document it references: 32 (20808.00), 33 (515.20), 34 (6.48).
- Withholding paid: 72.00 − 1.80 − 0.72 = 69.48.
- New due date 12 May = 5 May + 7 days, as the payment terms note says; the remittance advice of 8 May pays exactly 20308.55.
- Payee account XU79…9458: check digits correct (`check_ids.py`); same account, holder, branch and bank as in 27, 32 and 36, held in ferra like the payment currency. ISIN XU0001042501 correct.
- First reminder (`ReminderSequenceNumeric` 1), type PAYMENT: no earlier reminder exists in the flow.

## Considered and refuted
- `/Reminder/cac:AllowanceCharge/cbc:BaseAmount`: interest is charged on the balance after the credit and the penalty, although both were issued after the invoice — refuted: both were issued before the due date, so the amount outstanding on 1 May is 20286.32.
- `/Reminder/cac:PaymentTerms/cbc:PaymentDueDate`: interest stops on 5 May although payment is asked by 12 May and made on 8 May — refuted: a reminder can only charge what has accrued at its date; no later document claims more.
- `/Reminder/cac:PaymentMeans/cbc:PaymentMeansCode`: no payment reference in the reminder's payment means — refuted because the invoice's reference stays valid and is the one the remittance advice quotes.
- `/Reminder/cbc:PaymentAlternativeCurrencyCode`: an alternative payment currency equal to the document currency — refuted as a finding of the code itself: it says the customer may also pay in lume; only its exchange rate is empty (F5).
