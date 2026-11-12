# LLM review: 17-RemittanceAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/17-RemittanceAdvice.xml`, Git blob `9bee7dcb73c7b573cbe5ebbd0a5552954365dc02` (committed)
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

### road/17#F1 · Medium · Province given as Region
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/17#F2 · Medium · LocaleCode holds a language code
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/17#F3 · Low · The account the payment is made from is called "receivables"
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:AliasName` = `Lumeway receivables`
- Why: `AliasName` is "An alias for the name of this financial account, to be used in place of the actual account name for security reasons". The account is the payer's (`PayerFinancialAccount`), from which Lumeway pays its supplier; calling it "receivables" says it is the account Lumeway collects its own customers' payments on, which contradicts its role here.
- Condition: the alias of the payer's account fits an account Lumeway pays from (e.g. a payables or operating account), or is absent.
- Options: (a) an alias such as "Lumeway payables" (preferred); (b) drop the alias.
- Needs decision: no

### road/17#F4 · Low · Invoice referred to twice in the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0166`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `VI-INV-26-0166`
- Why: the line names the paid invoice in its billing reference, the element meant for the invoice being settled, and again as a generic document reference with type `Invoice`. The second reference says nothing the first does not (IND5).
- Condition: the paid invoice is referred to once in the line, in the billing reference.
- Options: (a) drop the generic `DocumentReference` (preferred); (b) keep it only for another document (e.g. the invoice response).
- Needs decision: no

### road/17#F5 · Low · Contacts and master data that do not fit a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: a remittance advice goes from the payer's accounts payable to the payee's accounts receivable; Lumeway's customer service in Sales and Valdara's order desk do not handle payments. The payee's stock-exchange listing and logistics provider play no part in a payment (section 4.8, IND5).
- Condition: the contacts are the payment functions of both parties; no party data without a use in the remittance.
- Options: (a) accounts payable / receivable contacts, drop listing and service provider (preferred); (b) drop the contacts.
- Needs decision: no

## Checked and consistent
- Invoice `VI-INV-26-0166` of 2026-03-24 resolves to `15-Invoice.xml`; the debit amount 4 862 160 XUF equals its payable amount; total payment = total debit − total credit (4 862 160 − 0); balance 0.
- The creditor reference `RF78VIINV260166` (check digits valid per `check_ids.py`) is the invoice's `PaymentID`; the payee account `XU790351041600000000209458` and the bank are those of the invoice.
- Issued 2026-04-22, before the invoice's due date 2026-04-23; the settlement discount period (to 2026-04-03) has passed, so paying the full amount is consistent.
- `PaymentPurposeCode` `SUPP` (supplier payment) fits a payment for goods.

## Considered and refuted
- `/RemittanceAdvice/cbc:PayerReference` = `LD-0149` next to `/RemittanceAdvice/cbc:PaymentOrderReference` = `LD-PAY-26-0149`: suspected two values for the same order for payment — refuted because UBL distinguishes "the order for payment from the payer to the payer's bank" (payment order) from "An internal reference to the payer's order for payment" (the payer's internal payment run), which may differ.
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF78VIINV260166`: suspected misuse of a payment reference — refuted because the definition names a reference "requested of the payer by the payee to accompany the payer's remittance", which is what the creditor reference on the invoice is.
