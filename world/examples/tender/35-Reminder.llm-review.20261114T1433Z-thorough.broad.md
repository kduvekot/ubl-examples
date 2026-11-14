# LLM review: 35-Reminder.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/35-Reminder.xml`, Git blob `8b2cb94295900deac8a0b1f1c5bdbbc86ecb0cc1` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 5660045 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/35#F1 · High · Multiplier × base is not the interest amount
- XPath: `/Reminder/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.08`
- XPath: `/Reminder/cac:AllowanceCharge/cbc:BaseAmount` = `20286.32`
- XPath: `/Reminder/cac:AllowanceCharge/cbc:Amount` = `22.23`
- Why: MultiplierFactorNumeric is "A number by which the base amount is multiplied to calculate the actual amount of this allowance or charge". 0.08 × 20286.32 = 1622.91, not 22.23. The amount is 8 % per year for five days: 20286.32 × 0.08 × 5 / 365 = 22.23 (the five days of `/Reminder/cac:ReminderPeriod/cbc:StartDate` = `2026-05-01` to `/Reminder/cac:ReminderPeriod/cbc:EndDate` = `2026-05-05`). The factor given is the annual rate, not the number that turns the base into the amount, and nothing in the charge says "per year" or "five days".
- Condition: MultiplierFactorNumeric × BaseAmount = Amount (within rounding), or the factor is absent and the rate and days are stated in text.
- Options: (a) factor 0.0010959 (0.08 × 5 / 365) with the reason text "8 % p.a. for 5 days" (preferred); (b) drop the factor and explain the calculation in AllowanceChargeReason.
- Needs decision: no

### tender/35#F2 · High · Under the contract's payment terms the invoice was not yet overdue
- XPath: `/Reminder/cbc:Note[2]` = `The balance of the first release is overdue; Urvania's statutory interest applies.`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:Note` = `The release's invoice, due on 2026-04-30.`
- XPath: `/Reminder/cac:ReminderPeriod/cbc:StartDate` = `2026-05-01`
- Why: the reminder counts default from the due date of the invoice's own terms (30 days from 2026-03-31). The framework contract says `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` The release cannot have been accepted before its installation was finished, which the department's debit note of 2026-04-06 treats as late (34); 30 days after an acceptance on or after 6 April ends on or after 6 May, after this reminder (2026-05-05) and after the day from which interest is charged. The interest is also called "Urvania's statutory interest", though the contract is a Bayvarran public contract under Bayvarra's procurement act, and its rate (8 %) is the one in the seller's standard terms on the invoice.
- Condition: the due date the reminder relies on is the one that follows from the contract, and interest is claimed under the law or clause that governs the contract.
- Options: (a) align with the decision on the invoice's terms (32 F5): if the contract's terms stand, date the reminder and the interest period after acceptance + 30 days and name the applicable interest (preferred); (b) if the invoice's terms are made the contract's, only the governing law of the interest needs settling.
- Needs decision: yes (payment terms and governing law of the contract)

### tender/35#F3 · Medium · The withholding tax remitted to the treasury is shown as a prepaid payment
- XPath: `/Reminder/cac:PrepaidPayment/cbc:ID` = `XB-WHT-26-04-1187`
- XPath: `/Reminder/cac:PrepaidPayment/cbc:PaidAmount` = `69.48`
- XPath: `/Reminder/cac:PrepaidPayment/cbc:PaidDate` = `2026-05-02`
- Why: PrepaidPayment is "A prepaid payment", i.e. money the debtor has already paid to the creditor towards the amounts reminded. 69.48 is the net withholding tax of the release (72.00 − 1.80 − 0.72 from 32, 33 and 34), and the ID is a Bayvarran withholding-tax reference: it was paid by the department to the tax authority, not to Valdara, and the reminded amounts (20808.00, 515.20, 6.48) are already net of it, so it is not deducted here (20286.32 + 22.23 = 20308.55). A reader who takes it for a payment on account would expect 69.48 less to be due. It was also remitted on 2 May, before the payment from which it is withheld was made (36, 2026-05-08).
- Condition: PrepaidPayment holds only payments made to the creditor on the reminded debt; the withholding remittance, if mentioned, is identified as such outside the payments.
- Options: (a) remove PrepaidPayment and mention the withholding certificate in a note or document reference (preferred); (b) none other seen.
- Needs decision: no

### tender/35#F4 · Medium · Pricing currency without prices; an "alternative" payment currency that is the document currency at rate 1
- XPath: `/Reminder/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Reminder/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `1`
- Why: PricingCurrencyCode is "the currency used for prices in the Reminder"; a reminder has no prices, and all its amounts are in XBL. PaymentAlternativeExchangeRate is "The exchange rate between the document currency and the payment alternative currency"; both are XBL, so the rate from lume to lume of 1 states nothing, and the pricing exchange rate with it converts nothing in this document.
- Condition: a pricing currency is given only with prices in it; an exchange rate has two different currencies.
- Options: (a) remove PricingCurrencyCode, PricingExchangeRate and PaymentAlternativeExchangeRate; keep the alternative currency code if payment in lume is offered (preferred).
- Needs decision: no

### tender/35#F5 · Medium · Language code in LocaleCode; provinces in Region
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Reminder/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; provinces are in CountrySubentity.
- Options: (a) a locale code, and move the provinces (preferred).
- Needs decision: no

### tender/35#F6 · Low · Tax representative, foreign exchange contract, seller master data, department as a company
- XPath: `/Reminder/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/Reminder/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- Why: as in the invoice (32): a tax representative without tax registration and without a tax to account for (the reminder's tax total is 0.00); the buyer's forward contract of 2026-01-02 quoted by the seller; the department with a company liquidation status. A payment reminder comes from the seller's order desk and goes to the department's procurement office, although the invoice names an accounts-payable routing (`32-Invoice.xml:/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`); credit control and accounts payable would be the fitting contacts.
- Condition: as stated for 32; contacts of a reminder are those who collect and pay.
- Options: (a) remove the representative and the contract; use receivables/payables contacts (preferred).
- Needs decision: yes (for the tax representative and the hedge, as in 32)

## Checked and consistent
- Arithmetic: 20808.00 (invoice payable) − 515.20 (credit note payable) − 6.48 (debit note payable) = 20286.32 = LineExtensionAmount = interest base; 20286.32 × 8 % × 5 / 365 = 22.23; 20286.32 + 22.23 = 20308.55 payable, the amount the remittance advice pays (36).
- Rate 8 % simple per year is the penalty interest rate of the invoice's payment terms; interest runs from the day after the invoice's due date (2026-05-01) to the reminder date, five days.
- References: VI-INV-26-0221 (32), VI-CN-26-0222 (33), LPWD-DOC-26-0223 (34) exist with these payable amounts; the debit note is correctly treated as the department's claim, set off.
- New due date 2026-05-12 = reminder date + seven days, as the terms say; the payment follows on 2026-05-08.
- First reminder (sequence 1); payee account and bank as on the invoice; payment currency XUF as on the invoice, with the rate 100.
- Charge reason 48 is "Interest on arrears" in the list given.
- check_ids.py: ISIN and IBAN-like account correct.

## Considered and refuted
- `/Reminder/cbc:TaxPointDate`: a tax point on a reminder without tax — refuted, harmless and it dates the interest charge.
- `/Reminder/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode`: a charge coded from the allowance list 5189 instead of 7161 — refuted, the code's meaning is exactly interest on arrears.
- `/Reminder/cac:ReminderLine[3]/cbc:CreditLineAmount`: a debit note shown as a credit — refuted, it is the customer's claim against the supplier (see 34 F3 for the roles).
- `/Reminder/cac:PaymentMeans/cbc:PaymentMeansCode`: no payment reference on the reminder — refuted, the remittance uses the invoice's RF reference.

## Outside this review
- Whether the release had been accepted, and when, is not in any example; it decides F2.
