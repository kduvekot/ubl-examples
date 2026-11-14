# LLM review: 35-Reminder.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/35-Reminder.xml`, Git blob `8b2cb94295900deac8a0b1f1c5bdbbc86ecb0cc1` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/35#F1 · High · Under the contract's payment terms the invoice was not overdue from 1 May; interest is claimed as "Urvania's statutory interest"
- XPath: `/Reminder/cbc:Note[2]` = `The balance of the first release is overdue; Urvania's statutory interest applies.`
- XPath: `/Reminder/cac:ReminderPeriod/cbc:StartDate` = `2026-05-01`
- XPath: `/Reminder/cac:ReminderLine[1]/cbc:Note` = `The release's invoice, due on 2026-04-30.`
- XPath: `/Reminder/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Statutory interest`
- Why: A reminder is "A document used to remind a customer of payments past due". The due date it relies on (30 April) is the invoice's own: 31 March + 30 days under the seller's standard terms (32/F5). The framework contract says `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` The release cannot have been accepted on 31 March (goods in transit, a bench damaged, 33; installation late, 34 of 6 April); 30 days after an acceptance on or after 6 April end on or after 6 May, after this reminder (5 May) and after the first interest day. The interest of 8 % a year is the rate of the seller's standard terms, called "Urvania's statutory interest", against a Bayvarran public body under a contract governed by Bayvarra's procurement act, which names no interest. Counter-argument (logistics): the reminder follows the invoice's due date consistently; that is true, which is why the problem has to be decided with 32/F5.
- Condition: The day from which interest is charged is the day after the due date the contract yields, and the rate is one the contract or its governing law gives the supplier.
- Options: (a) decide the due date with 32/F5 (acceptance + 30 days, with the acceptance date in the flow), and recalculate the reminder period, days and interest here and in 36 (preferred by broad, money, context); (b) change the contract's term to "30 days after the invoice" and add the interest clause, which makes this reminder right; (c) base the interest on a stated Bayvarran statutory rate.
- Needs decision: yes
- From: broad (F2), money (F2), context (F1); refuted by logistics (carried as counter-argument)

### tender/35#F2 · High · Multiplier factor × base is 1622.91, not the 22.23 charged
- XPath: `/Reminder/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.08`
- XPath: `/Reminder/cac:AllowanceCharge/cbc:BaseAmount` = `20286.32`
- XPath: `/Reminder/cac:AllowanceCharge/cbc:Amount` = `22.23`
- Why: `MultiplierFactorNumeric` is "A number by which the base amount is multiplied to calculate the actual amount of this allowance or charge". Recomputed: 0.08 × 20286.32 = 1622.91. The amount is 8 % a year for the five days of the reminder period: 20286.32 × 0.08 × 5 / 365 = 22.23. The element carries the annual rate, not the factor; the factor that yields the amount is 0.08 × 5 / 365 = 0.0010959. Arithmetic that does not hold (section 6 High).
- Condition: `MultiplierFactorNumeric` × `BaseAmount` = `Amount` (to the cent), or there is no factor and rate and days are stated in the reason.
- Options: (a) drop the factor and state "8 % a year, 5 days, 1 to 5 May" in the reason (preferred by money: the rate is in the invoice's `PenaltyInterestRate`); (b) factor 0.0010959 with that text (preferred by broad).
- Needs decision: no
- From: broad (F1), money (F1); context noted it under "Outside this review"

### tender/35#F3 · High · The debit note is entered as a credit, while the debit note makes the department the debtor
- XPath: `/Reminder/cac:ReminderLine[3]/cbc:CreditLineAmount` = `6.48`
- XPath: `/Reminder/cac:ReminderLine[3]/cac:BillingReference/cac:DebitNoteDocumentReference/cbc:ID` = `LPWD-DOC-26-0223`
- XPath: `/Reminder/cac:ReminderLine[3]/cbc:Note` = `The department's penalty, set off.`
- Why: The line reduces the customer's balance by the amount of a debit note. The debit note referenced names the supplier as creditor and the department as debtor (`34-DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`), so by that document the 6.48 would be a further debt of the customer and belong in `DebitLineAmount`. The reminder follows the debit note's intention, not its encoding: one of the two documents is wrong. Counter-argument (broad, logistics, context): the amount is in the department's favour, which is what a credit line says; the mismatch lies in the debit note's roles. The merge keeps it as a finding because the two examples contradict each other, but the fix belongs in 34: with 34/F1 option (a) this line stands unchanged.
- Condition: The reminder line's side (debit or credit) agrees with who is creditor and debtor in the referenced document.
- Options: (a) correct the roles of the debit note (34/F1 (a)); this line then stands (preferred); (b) if the penalty becomes a credit note (supplier's or self-billed), reference it here as a credit note.
- Needs decision: yes (decided with 34/F1)
- From: money (F3); refuted by broad, logistics and context (carried as counter-argument)

### tender/35#F4 · Medium · The withholding tax paid to the tax office is listed as a prepaid payment, but the balance is not reduced by it
- XPath: `/Reminder/cac:PrepaidPayment/cbc:ID` = `XB-WHT-26-04-1187`
- XPath: `/Reminder/cac:PrepaidPayment/cbc:PaidAmount` = `69.48`
- XPath: `/Reminder/cac:PrepaidPayment/cbc:PaidDate` = `2026-05-02`
- XPath: `/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20308.55`
- Why: `PrepaidPayment` is "A prepaid payment": money already paid towards the amounts of the document. 69.48 = 72.00 − 1.80 − 0.72 is the net withholding of invoice, credit note and debit note, paid by the department to the Bayvarran tax office (the ID is a withholding-tax reference), not to Valdara. The reminded amounts are already net of it and the total does not deduct it (20286.32 + 22.23 = 20308.55, no `PrepaidAmount`); a reader who deducts prepaid payments, as the element invites, arrives at 20239.07. It was also remitted on 2 May, before the payment from which it is withheld (36, 8 May), and how the supplier knows the customer's tax reference is unexplained.
- Condition: Every `PrepaidPayment` is a payment received on the reminded amounts and is reflected in the monetary total; withholding information is carried where it does not read as a payment on account.
- Options: (a) remove the prepaid payment (the withholding is already in 32–34), or mention the withholding certificate in a note or document reference (preferred); (b) remind the gross amounts and show the withholding as prepaid, with `PrepaidAmount` 69.48.
- Needs decision: no
- From: broad (F3), money (F4), context (F2)

### tender/35#F5 · Medium · A province in `Region`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Reminder/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity`. 219 occurrences in 104 files.
- Condition: The province is in `CountrySubentity`.
- Options: move it to `CountrySubentity` (preferred); or record a postal-region convention.
- Needs decision: no
- From: broad (F5), parties (F1), context (F3)

### tender/35#F6 · Medium · A language code as locale
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code. 362 occurrences in 213 files.
- Condition: No `LocaleCode` holds a bare language code.
- Options: (a) remove it (preferred by parties and context); (b) a real locale from a locale list (broad).
- Needs decision: no
- From: broad (F5), parties (F2), context (F4)

### tender/35#F7 · Medium · The department described as a company in a commercial register, with a liquidation status
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: A municipal department (ISIC 8411) has no liquidation status and is not in a commercial register as a company; the register number itself is not questioned.
- Condition: The department carries no liquidation status, and its register is not typed as commercial.
- Options: (a) drop the status and type the register neutrally (preferred); (b) reduce the legal entity to name and identifier.
- Needs decision: no
- From: parties (F7), context (F7), broad (F6)

### tender/35#F8 · Low · Currency codes and exchange rates with nothing to convert, one from the lume to the lume
- XPath: `/Reminder/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Reminder/cbc:TaxCurrencyCode` = `XUF`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode` = `XBL`
- XPath: `/Reminder/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/Reminder/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- Why: `PricingCurrencyCode` is "A code signifying the currency used for prices in the Reminder"; a reminder has no prices, so the pricing currency, the pricing rate and the buyer's forward contract of 2 January behind it (32/F14) convert nothing. The only tax amount is a bare 0.00 in lume, so the tax currency and tax rate convert nothing either. `PaymentAlternativeExchangeRate` is "The exchange rate between the document currency and the payment alternative currency"; both are the lume, so it states that one lume is one lume. Only the payment currency (ferra, the payee account's) and its rate have a use. Low, as the earlier merges rated identity and unused rates (analysis/review-merge-decisions.md; sea D for 28); broad rated it Medium.
- Condition: A currency code and its rate are present only if the document has an amount in, or a conversion into, that currency; no rate has the same source and target.
- Options: (a) keep `PaymentCurrencyCode`, `PaymentAlternativeCurrencyCode` and `PaymentExchangeRate`; remove the pricing and tax currency codes, the pricing, tax and alternative rates and the forward contract (preferred, all parts); (b) none seen.
- Needs decision: no
- From: broad (F4), money (F5), context (F5), broad (F6, forward contract)

### tender/35#F9 · Low · A tax total of 0.00 without scheme or category, with a tax point date
- XPath: `/Reminder/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Reminder/cbc:TaxPointDate` = `2026-05-05`
- Why: The reminder's only new amount is interest. The tax total names no scheme or category, so it does not say which tax was considered for the interest or why none applies; a tax point is given for it. Counter-argument (broad, context): the tax point is harmless and dates the interest charge, a supply of that date. The merge keeps the finding for the unexplained zero total; the tax point stands or falls with it.
- Condition: A tax is stated only if one applies to the interest, with scheme, category and reason (e.g. outside the scope of VAT); a tax point date only with such a tax.
- Options: (a) remove the tax total and the tax point date (preferred by money); (b) a subtotal for the interest (22.23, outside the scope).
- Needs decision: no
- From: money (F6); the tax point refuted by broad and context (carried as counter-argument)

### tender/35#F10 · Low · A tax representative on a payment reminder
- XPath: `/Reminder/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: As 32/F15: register number and name only, no tax registration; the reminder charges no tax and asks for a balance and interest.
- Condition: As 32/F15.
- Options: (a) remove it (preferred); decided together with 32/F15.
- Needs decision: yes
- From: broad (F6), money (F6), parties (F8), context (F6)

### tender/35#F11 · Low · The same Urvanian party is described with different language tags and legal-form renderings across the flow
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/Reminder/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: Here tagged `en-XU`, with the legal form in `qau` and `en-XU`; in the Bayvarran-issued examples `en-XB` and one untagged legal form (`03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`). The tag follows the issuer; could not be settled.
- Condition: The same rendering carries the same `languageID` in every example, or the rule is stated.
- Options: (a) `en-XU` everywhere (preferred); (b) the issuer's tag, applied uniformly and documented.
- Needs decision: yes
- From: parties (F3)

### tender/35#F12 · Low · A reminder from the sales order desk to the procurement office
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention` = `Head of procurement`
- Why: A payment reminder concerns credit control and accounts payable; the invoice names the department's unit for that (`32-Invoice.xml:/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`).
- Condition: Receivables and payables contacts, or none.
- Options: (a) accounts contacts (preferred); (b) drop `Contact`, `Department` and `MarkAttention`.
- Needs decision: no
- From: parties (F4), broad (F6)

### tender/35#F13 · Low · Supplier's master data that a reminder does not use
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: A reminder identifies the creditor and where to pay; listing, fully-paid shares and the warehouse provider (whose contact has no means of contact) are not used (section 4.8); the issuer's own share capital is accepted by earlier merges and listed for completeness. Counter-argument (parties): the listing describes a listed company's legal entity.
- Condition: These appear only in documents whose purpose uses them.
- Options: (a) remove them (preferred); (b) keep those for which a use can be stated.
- Needs decision: no
- From: parties (F5), context (F8)

### tender/35#F14 · Low · Party tax exemption reason worded as a transaction
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: Under `PartyTaxScheme` "A reason for the party's exemption from tax"; the text begins with a kind of sale. Only its second half is the party's status.
- Condition: The party-level reason states the party's status.
- Options: (a) reword the text to the party's status and keep the code, whose list definition is "A body of the federation, a state or a city buys free of sales tax." (preferred, aligned with the other tender merges); (b) also a code that names the status alone (parties' preference).
- Needs decision: no
- From: parties (F6)

## Checked and consistent
- Balance (re-done): 20808.00 (32, payable after withholding) − 515.20 (33) − 6.48 (34) = 20286.32 = `LineExtensionAmount` = interest base; 20286.32 × 0.08 × 5 / 365 = 22.2316 → 22.23 = `ChargeTotalAmount`; 20286.32 + 22.23 = 20308.55 = `PayableAmount`, the amount 36 pays. Each line equals the payable amount of the document it references.
- Interest: 8 % a year, simple, the invoice's `PenaltyInterestRate`; five days 1–5 May = the reminder period; reason code 48 ("Interest on arrears", UNTDID 5189) with `ChargeIndicator` true.
- Withholding: 72.00 − 1.80 − 0.72 = 69.48.
- New due date 12 May = 5 May + 7 days ("Please pay within seven days."); 36 pays on 8 May.
- First reminder (`ReminderSequenceNumeric` 1), type PAYMENT; no earlier reminder in the flow. Payee account XU79…9458 the same account, holder, branch and bank as in 27, 32 and 36, held in ferra like the payment currency; `check_ids.py` (re-run): account and ISIN correct.
- Parties: those of the invoice, credit note and debit note; Valdara signs (VI-SIG-REM).

## Considered and refuted
- `/Reminder/cbc:TaxPointDate`: a tax point on a reminder without tax — refuted by broad and logistics (harmless; dates the interest charge); money raised it with the zero tax total: F9.
- `/Reminder/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode`: a charge coded from the allowance list 5189 instead of 7161 — refuted, the code's meaning is exactly interest on arrears (from broad).
- `/Reminder/cac:ReminderLine[3]/cbc:CreditLineAmount`: a debit note shown as a credit — refuted by broad, logistics and context (the mismatch is in 34's roles); money raised it: F3, with their argument.
- `/Reminder/cac:PaymentMeans/cbc:PaymentMeansCode`: no payment reference on the reminder — refuted, the invoice's RF reference stays valid and 36 quotes it (from broad, money).
- `/Reminder/cac:AllowanceCharge/cbc:BaseAmount`: interest on the balance after the credit and the penalty — refuted, both were issued before the due date (from money).
- `/Reminder/cac:PaymentTerms/cbc:PaymentDueDate`: interest stops on 5 May although payment is asked by 12 May — refuted, a reminder charges what has accrued at its date (from money).
- `/Reminder/cbc:PaymentAlternativeCurrencyCode`: an alternative payment currency equal to the document currency — refuted as to the code itself, it offers payment in lume; its rate is F8 (from money).
- `/Reminder/cac:PrepaidPayment/cbc:ID`: a withholding remittance for April paid on 2 May — refuted as a date problem, a remittance for the April period paid on 2 May is in order (from logistics); whether it is a prepaid payment is F4.
- `/Reminder/cac:ReminderPeriod/cbc:StartDate`: interest from 1 May although the contract counts from the accepted release — refuted by logistics (the reminder follows the invoice's due date consistently); broad, money and context raised it: F1, with logistics' argument.
- `/Reminder/cac:ReminderPeriod`: five days — refuted, "The periods to which the Reminder applies" read as the overdue period (from context).
- `/Reminder/cbc:PaymentCurrencyCode`: ferra although all amounts are in lume — refuted, payment into a ferra account with a payment rate (from context).
- `/Reminder/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate`: raised by logistics only in 26; here in F8 (from logistics).
- `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` (`-1`), `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`, `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`, `/Reminder/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID` = `CREVXUFR`: malformed offset, real country code, real ICD, real BIC — each refuted (text offset used throughout; +999 not assigned; 0990 not allocated; XU is user-assigned) (from parties).
- `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: master data — refuted by parties; kept in F13; check digit and fictional prefix confirmed.

## Changed in the merge
- broad/F2 + money/F2 + context/F1 → F1: combined; numbered before the multiplier finding by position (`Note[2]`), all High.
- broad/F1 + money/F1 → F2: combined; both options kept.
- money/F3 → F3: kept High, yes, although three parts refuted it, because 35 and 34 contradict each other; tied to 34/F1 so that one decision settles both.
- broad/F4 (Medium) + money/F5 + context/F5 (Low) + broad/F6 (forward contract) → F8: Low, aligned with the earlier merges on identity and unused rates.
- broad/F6 split into F8 (forward contract), F10 (tax representative), F12 (contacts), F7 (department, raised to Medium as analysis).
- context/F6 (Low, no) → F10: Needs decision yes, as 32/F15.
- parties/F7 + context/F7 (Low) → F7: Medium, as analysis.
- parties/F6 → F14: preferred option changed to keeping the code and rewording the text, aligned with the other tender merges.

## Outside this review
- Whether and when the release was accepted is in no example; it decides F1 (broad).
