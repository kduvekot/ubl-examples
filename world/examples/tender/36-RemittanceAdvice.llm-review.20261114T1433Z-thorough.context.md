# LLM review: 36-RemittanceAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/36-RemittanceAdvice.xml`, Git blob `0d67d6237dbe199fe762a5dccb67b4360d07c700` (committed)
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

### tender/36#F1 · Medium · A province in `Region`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/36#F2 · Medium · A language code as locale
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/36#F3 · Low · The advice of an actual payment gives neither its date nor the amount in the currency that was asked for
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `/RemittanceAdvice/cbc:TotalPaymentAmount` = `20308.55`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XUF`
- Why: A remittance advice is "A document that specifies details of an actual payment". It gives the means (credit transfer), both accounts, the creditor reference and the amount in lume. It has no payment date (no date in the payment means; only the document's issue date), and although the invoice and the reminder ask for payment in ferra (`35-Reminder.xml:/Reminder/cbc:PaymentCurrencyCode` = `XUF`) into a ferra account, from a lume account, it states neither a payment currency nor the ferra amount nor the rate used (no currency or exchange rate element in the document; searched the annotated listing). The payee cannot tell from the advice how many ferra to expect and on which day, which is what the advice is for when the currencies differ.
- Condition: The remittance advice states the date of the payment and, where the payment is made in another currency than the document's, that currency, the amount in it or the exchange rate.
- Options: (a) preferred: a payment date in the payment means, `PaymentCurrencyCode` ferra and a payment exchange rate (100, as in the reminder); (b) pay and advise in lume and say so, using the reminder's alternative payment currency.
- Needs decision: no

### tender/36#F4 · Low · The interest is paid in full although its basis is open
- XPath: `/RemittanceAdvice/cbc:Note` = `Payment of the first release, with the interest.`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cbc:DebitLineAmount` = `22.23`
- Why: The department pays the interest the reminder claims as "Urvania's statutory interest" for five days after 2026-04-30. Under the contract that the department itself wrote, payment is due "30 days after each accepted release" (`24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note`), and the release, whose installation the department itself penalised as late on 2026-04-06, cannot have been accepted 30 days before 2026-04-30. A public body paying interest under a foreign statute for a delay that, by its own contract, did not exist is not plausible; the payment authorisation referenced (`PWD-PAY-AUTH-26-0412`) would be where that is checked. The finding stands or falls with the decision on the payment terms raised for `32-Invoice.xml` and `35-Reminder.xml`.
- Condition: The remittance advice pays interest only if the reminder's claim holds under the contract's payment terms; otherwise it pays the balance and says why the interest is not paid.
- Options: (a) preferred: once the due date follows the contract, drop the interest line (and the reminder, or move both later); (b) if the contract's terms are changed to "30 days after the invoice" with an interest clause, keep it.
- Needs decision: yes

### tender/36#F5 · Low · The payment authorisation referenced twice, once as a billing document of the interest line
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `PWD-PAY-AUTH-26-0412`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `PWD-PAY-AUTH-26-0412`
- Why: At document level the reference says the payment rests on an internal authorisation, which fits. Inside the billing reference of line 4 the same document appears again; a `BillingReference` is "A reference to a billing document associated with this remittance advice line", and a payer's internal authorisation is not a billing document of the interest (the reminder is, and is referenced). If the authorisation covers the whole payment, the line-level copy is redundant; if it covers only the interest, the document-level one is too broad.
- Condition: The payment authorisation is referenced once, at the level it applies to, and not as a billing document.
- Options: (a) preferred: keep the document-level reference only; (b) keep only the line-level one if the authorisation is for the interest, outside the billing reference if the model allows.
- Needs decision: no

### tender/36#F6 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/36#F7 · Low · Master data of a party that the document does not use
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). A remittance advice tells the supplier what was paid for which documents; the supplier's share capital, listing and warehouse provider are not used. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example (both account numbers, creditor reference `RF48VIINV260221`).
- Lines against the documents they reference: invoice `VI-INV-26-0221` 20808.00 (its payable amount), credit note `VI-CN-26-0222` 515.20, the department's penalty `LPWD-DOC-26-0223` 6.48, interest of reminder `VI-DOC-26-0224` 22.23 (issue date 2026-05-05 as quoted).
- Totals: debits 20808.00 + 22.23 = 20830.23; credits 515.20 + 6.48 = 521.68; payment 20830.23 − 521.68 = 20308.55 = the reminder's payable amount; `LineCountNumeric` 4 with four lines.
- The payment (2026-05-08) lies within the reminder's seven days (to 2026-05-12); the creditor reference is the one the invoice asked to quote; the payee account is the invoice's.
- Sender is the accounting customer (the department), which pays from an account at the Bank of Lumeport in Lumeport; no tax representative is carried here.
- The credit note is set off against this payment, as its document-level terms say.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cbc:CreditLineAmount`: a debit note taken as a credit — refuted for this document: the amount reduces what the department pays, which is what the department's penalty means; the mismatch of roles lies in the debit note and is raised there.
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount`: the payer's full bank details — refuted, in an advice of a payment the paying account identifies the transfer for the payee.
- `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cac:BillingReference/cac:ReminderDocumentReference/cbc:IssueDate`: an issue date only on this reference — refuted, it is correct and harmless.

## Outside this review
- Whether 20308.55 lume arrive as 2030855 ferra at the rate of 100, and who bears the charges (`SHAR` in the invoice): money part.
