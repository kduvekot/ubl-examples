# LLM review: 34-DebitNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/34-DebitNote.xml`, Git blob `b6bf3671341fe2437750245b0f5de26efdc18dc0` (committed)
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

### tender/34#F1 · Medium · The buyer's penalty is written as a debit that the supplier is owed
- XPath: `/DebitNote/cbc:ID` = `LPWD-DOC-26-0223`
- XPath: `/DebitNote/cbc:Note` = `Penalty for late installation under the contract's clause PEN-1.`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `6.48`
- Why: A UBL debit note is "A document used to specify debits due to the Creditor from the Debtor"; its structure follows the invoice: the accounting supplier is the creditor and the accounting customer the debtor, and the payable amount is what the customer owes the supplier in addition. Here the document is issued by the department (its identifier is from the department's series, and the reminder calls it `35-Reminder.xml:/Reminder/cac:ReminderLine[3]/cbc:Note` = `The department's penalty, set off.`) and claims a contractual penalty from Valdara. With Valdara as accounting supplier and the department as accounting customer, the document says the opposite of what is meant: that the department owes Valdara 6.48 more. The later documents treat it as a credit in favour of the department (`35-Reminder.xml:/Reminder/cac:ReminderLine[3]/cbc:CreditLineAmount` = `6.48`), which confirms the intended direction and contradicts the roles.
- Condition: The party that is owed the penalty is the creditor of the document that claims it, in the roles the document type defines; the reminder and the remittance advice refer to it by the kind of document it then is.
- Options: (a) preferred: a `SelfBilledCreditNote` issued by the department (customer-issued, reducing what it owes the supplier; my knowledge of the UBL document types), referenced as credit note downstream; (b) a debit note with the department as accounting supplier and Valdara as accounting customer; (c) keep the document and record as a finding that UBL has no buyer-issued debit note.
- Needs decision: yes (changes the document type or the roles, and the references in `35-Reminder.xml` and `36-RemittanceAdvice.xml`)

### tender/34#F2 · Medium · A province in `Region`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/34#F3 · Medium · A language code as locale
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/34#F4 · Low · The penalty states three days of delay without any date
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity` = `3`
- XPath: `/DebitNote/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `One day waived`
- Why: The claim rests on the installation being three days late. Neither this document nor any other of the flow says when the installation was due or when it was finished: the order has no requested delivery date and no installation line (see the review of `26-Order.xml`), the order response promises no date, and the invoice bills the installation on 2026-03-31, before it can have begun. The debit note has no period, no delivery and no reference to an acceptance or work report that would carry the dates. The supplier cannot check the claim from the documents, and the waiver of one day has nothing to be measured against either.
- Condition: The document that claims the penalty states the due date and the actual completion date of the installation (or references a document that does), and the flow contains the due date.
- Options: (a) preferred: an invoice period or note with both dates, and a requested installation date in the order; (b) a reference to the acceptance record of the release.
- Needs decision: yes (adds dates to the story)

### tender/34#F5 · Low · A tax representative in a penalty claim
- XPath: `/DebitNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for this Debit Note". The document claims a contractual penalty with a tax total of 0.00; the only tax effect is the buyer's own correction of its withholding. Valdara's tax representative in Bayvarra has no function in the buyer's penalty claim; the party looks carried over from the invoice.
- Condition: A tax representative is named only where the document charges or reports a tax the representative accounts for.
- Options: (a) preferred: remove it; (b) none seen.
- Needs decision: no

### tender/34#F6 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/34#F7 · Low · Master data of a party that the document does not use
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). A penalty claim identifies the supplier it is addressed to; the supplier's share capital, listing and warehouse provider have no part in it. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- Penalty against the contract's clause PEN-1 ("0.5 % per day late, at most 10 %."): installation price of the release 720.00 (invoice line 2); 3 × 0.5 % × 720.00 = 10.80; one day waived = 3.60; 7.20 remains, below the cap of 72.00; less 10 % withholding correction 0.72 = 6.48 payable.
- The withholding amounts follow the same 10 % as the invoice: 1.08 on the line's 10.80, 0.72 on the 7.20 after the waiver; the reminder's withholding payment (69.48 = 72.00 − 1.80 − 0.72) uses the 0.72.
- References: order `LPWD-PO-26-0212`, invoice `VI-INV-26-0221`, contract `PWD-2026-PARKS` exist and are the release's documents.
- Allowance: `ChargeIndicator` false, reason code 64 (special agreement) from the allowance list, with a text that says what was agreed.

## Considered and refuted
- `/DebitNote/cac:WithholdingTaxTotal`: a withholding tax on a penalty — refuted for this lens because the penalty reduces the price of the installation, on which the buyer withheld 10 %; reducing the withholding with it is consistent, and the reminder's figures follow it. Whether that is the right tax treatment is the money part's.
- `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity`: days as "quantity of Items debited" — refuted, the debited thing is days of delay and the unit says so.
- `/DebitNote/cac:OrderReference`: an order reference in a penalty claim — refuted, it identifies the release concerned.

## Outside this review
- The debit note is issued on 2026-04-06, two days after the credit note for a bench found damaged; whether 39 or 40 installations were late, and when, is a timeline question across the documents.
