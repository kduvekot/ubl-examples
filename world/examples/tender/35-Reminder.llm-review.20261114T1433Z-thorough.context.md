# LLM review: 35-Reminder.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/35#F1 · High · The invoice is reminded as overdue since 30 April, although under the contract it cannot have been due then
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:Note` = `The release's invoice, due on 2026-04-30.`
- XPath: `/Reminder/cbc:Note[2]` = `The balance of the first release is overdue; Urvania's statutory interest applies.`
- XPath: `/Reminder/cac:ReminderPeriod/cbc:StartDate` = `2026-05-01`
- XPath: `/Reminder/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Statutory interest`
- Why: A reminder is "A document used to remind a customer of payments past due". Whether the payment is past due is governed by the framework contract, whose terms are `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` The due date 2026-04-30 is the invoice date plus 30 days, from the supplier's standard terms. The release cannot have been accepted on the invoice date (2026-03-31): the goods were still in transit, a bench was found damaged around 2026-04-02 to 04-04 (`33-CreditNote.xml`), and the department's penalty of 2026-04-06 is for an installation finished late (`34-DebitNote.xml`). Thirty days from any acceptance after the installation end after 2026-04-30, so the balance was not overdue from 2026-05-01 and interest for those days has no basis in the contract. The interest itself is claimed as "Urvania's statutory interest", the law of the supplier's country, against a Bayvarran public body under a contract governed by Bayvarra's procurement act (`XB-PPA-2019`), which provides no interest at all in its documents.
- Condition: The reminder is issued only after the due date that follows from the contract (30 days after acceptance of the release), counts overdue days from that date, and claims interest only on a basis the contract or the applicable law of the world gives.
- Options: (a) preferred: fix the acceptance date in the flow, derive the due date from it, and move the reminder (and the remittance advice) after it; (b) change the contract's payment terms to "30 days after the invoice" in all documents that carry them and add an interest clause.
- Needs decision: yes (same decision as for the payment terms of `32-Invoice.xml`)

### tender/35#F2 · Medium · The withholding tax paid to the tax office listed as a prepaid payment
- XPath: `/Reminder/cac:PrepaidPayment/cbc:ID` = `XB-WHT-26-04-1187`
- XPath: `/Reminder/cac:PrepaidPayment/cbc:PaidAmount` = `69.48`
- XPath: `/Reminder/cac:PrepaidPayment/cbc:PaidDate` = `2026-05-02`
- Why: `PrepaidPayment` is "A prepaid payment": a payment already made towards the amount the document claims, which therefore reduces what remains to be paid. 69.48 is the withholding tax of the release (72.00 − 1.80 − 0.72), which the department paid to the Bayvarran tax authority, as the identifier suggests; it is not a payment to the supplier. The amounts reminded are already net of the withholding (the invoice's payable amount 20808.00 is 20880.00 less 72.00), and the reminder does not deduct the 69.48 from its total (20286.32 + 22.23 = 20308.55). The element thus holds something that is neither prepaid to the creditor nor used in the balance; a reader applying the definition would deduct it a second time.
- Condition: `PrepaidPayment` holds only payments made to the creditor towards the reminded amounts and is reflected in the total, or is absent.
- Options: (a) preferred: remove it from the reminder (the withholding belongs to the invoice's and credit note's withholding totals); (b) mention the remitted withholding in a note.
- Needs decision: no

### tender/35#F3 · Medium · A province in `Region`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Reminder/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/35#F4 · Medium · A language code as locale
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/35#F5 · Low · An exchange rate from lume to lume, a pricing currency without prices, and the buyer's forward contract
- XPath: `/Reminder/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/Reminder/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Reminder/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- Why: `PaymentAlternativeExchangeRate` is "The exchange rate between the document currency and the payment alternative currency". Both are lume, so the rate is 1 by necessity and states nothing; the alternative payment currency itself only says that payment may also be made in the document currency. The reminder contains no price, so a pricing currency and a pricing exchange rate have nothing to apply to, and the foreign exchange contract behind that rate is the buyer's forward purchase of ferra of 2026-01-02 (`26-Order.xml`), which the supplier has no reason to cite when it reminds.
- Condition: The reminder carries an exchange rate only between two different currencies that it uses, and no pricing currency, pricing rate or foreign exchange contract of the buyer.
- Options: (a) preferred: remove the alternative exchange rate, the pricing currency and the pricing exchange rate with its contract; keep the payment and tax rates if payment is in ferra; (b) none seen.
- Needs decision: no

### tender/35#F6 · Low · A tax representative in a payment reminder
- XPath: `/Reminder/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for the taxpayer". The reminder charges no tax (tax total 0.00); it asks for payment of a balance and interest. The representative has no function in it and looks carried over from the invoice.
- Condition: A tax representative is named only where the document charges or reports a tax the representative accounts for.
- Options: (a) preferred: remove it; (b) none seen.
- Needs decision: no

### tender/35#F7 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/35#F8 · Low · Master data of a party that the document does not use
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). A reminder identifies the creditor and where to pay; the creditor's share capital, listing and warehouse provider are not used. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- The three lines refer to existing documents with their payable amounts: invoice `VI-INV-26-0221` 20808.00 (debit), credit note `VI-CN-26-0222` 515.20 (credit), the department's penalty `LPWD-DOC-26-0223` 6.48 (credit); 20808.00 − 515.20 − 6.48 = 20286.32 = `LineExtensionAmount` = base of the interest.
- Interest: 8 % a year (the invoice's penalty interest rate, simple, per year) on 20286.32 for the five days of the reminder period (2026-05-01 to 2026-05-05): 20286.32 × 0.08 × 5 / 365 = 22.23; total 20286.32 + 22.23 = 20308.55.
- Line 1's note "due on 2026-04-30" equals the invoice's due date; the reminder is issued on 2026-05-05; new due date 2026-05-12 = seven days later, as the terms say; first reminder, sequence 1; type payment reminder.
- The remittance advice of 2026-05-08 answers the reminder within that period (`36-RemittanceAdvice.xml`).
- Withholding figure: 72.00 − 1.80 − 0.72 = 69.48.
- Notes in Urvanian and English, tagged `qau` and `en-XU`; signature and payee account of the supplier.

## Considered and refuted
- `/Reminder/cac:ReminderLine[3]/cbc:CreditLineAmount`: a debit note listed as a credit — refuted for the reminder: the amount is in the department's favour, which is what a credit line says; the mismatch lies in the debit note's roles and is raised there.
- `/Reminder/cbc:TaxPointDate`: a tax point on a reminder without tax — refuted, the element is defined for the reminder and the interest charge is a supply of that date.
- `/Reminder/cac:ReminderPeriod`: five days — refuted, "The periods to which the Reminder applies" read as the overdue period on which interest is computed.
- `/Reminder/cbc:PaymentCurrencyCode`: ferra although all amounts are in lume — refuted, as in the invoice the payment is to be made in ferra to a ferra account, with a payment exchange rate.

## Outside this review
- `/Reminder/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.08` times `/Reminder/cac:AllowanceCharge/cbc:BaseAmount` = `20286.32` is 1622.91, not `/Reminder/cac:AllowanceCharge/cbc:Amount` = `22.23`; the factor is an annual rate applied for five days. Factor arithmetic of allowances and charges is the money part's lens; recorded so it is not lost.
