# LLM review: 17-RemittanceAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/17-RemittanceAdvice.xml`, Git blob `9bee7dcb73c7b573cbe5ebbd0a5552954365dc02` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
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

### road/17#F1 · Medium · Language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats `Language/ID` and names no locale (section 6: Medium). Recounted: 364 occurrences in 213 files (`grep -rh --include='*.xml' 'LocaleCode listID="ISO 639">en<'`); the parts said 362.
- Condition: `LocaleCode` is absent or holds a locale from a list of locales named in its listID.
- Options: (a, preferred: broad, parties) drop `LocaleCode`; (b, context's preference) `en-XB` with a locale list as listID.
- Needs decision: no (parties said yes; encoding only, as in all earlier flows)
- From: broad (F1), parties (F1), context (F2)

### road/17#F2 · Medium · Gate number in AdditionalStreetName of Lumeway's postal address
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is an entrance for vehicles, not a street name; a remittance advice has no use for it. Recounted: 79 occurrences in 76 files.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop the gate from the party address; (b) keep it only in delivery addresses, in a location description.
- Needs decision: no
- From: broad (F2), parties (F2)

### road/17#F3 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran addresses in the same document use `CountrySubentity` (`/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`; the payer's bank: `Coastal State`). Recounted: 219 occurrences in 104 files.
- Condition: no Urvanian address of this example holds the province in `Region`; it is in `CountrySubentity` (with a code where a list exists).
- Options: (a, preferred) move it to `CountrySubentity`, as Bayvarra does; (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules.
- Needs decision: no
- From: broad (F3), parties (F3), context (F1)

### road/17#F4 · Low · Contacts that do not fit a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: a remittance advice goes from the payer's accounts payable to the payee's accounts receivable; Lumeway gives its customer service desk in Sales, Valdara its order desk in Sales. Each party carries one fixed contact in every role of the flow.
- Condition: the accounting parties' contacts are their payment / accounts functions.
- Options: (a, preferred) accounts payable and accounts receivable contacts; (b) drop job titles and departments that do not fit.
- Needs decision: no
- From: broad (F4), parties (F4), context (F5, contact part)

### road/17#F5 · Low · Italian street names tagged as English, with the issuer's region subtag
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: both renderings carry `languageID` `en-XB` but are Italian text; the same addresses are tagged `en-XU` in `15-Invoice.xml` (e.g. `15-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`, tagged en-XU). The parties part refuted it: English keeps foreign street names unchanged, and the subtag follows the sender. Against that: `languageID` names the language of the content, and the same address is tagged differently by issuer. The merge cannot settle the convention; aligned with the utilities, rail and packaging merges (Low, decision). 217 such street renderings in 102 files.
- Condition: the world has one stated rule for the language tag of Urvanian names rendered in English, and every rendering of the same address follows it.
- Options: (a, preferred) the party's own variety (en-XU) whoever sends the document, documented; (b) document that the tag follows the issuer, as now.
- Needs decision: yes
- From: merge (from the parties' "Considered and refuted")

### road/17#F6 · Low · Valdara's legal form in one untagged rendering
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: in the documents Valdara issues its legal form comes in two tagged renderings (`qau` and `en-XU`, e.g. `15-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`); here there is one, without `languageID`, while the address is rendered in both languages. No part raised it; added by the merge for consistency with the rail, air, wood and plastics merges.
- Condition: the legal form is rendered as the address is (both renderings, tagged), or the difference is a stated convention.
- Options: (a, preferred) both renderings with `languageID`; (b) one rendering, tagged.
- Needs decision: no
- From: merge

### road/17#F7 · Low · Party master data the remittance does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: section 4.8: the payee's stock-exchange listing and its logistics provider play no part in a payment.
- Condition: every optional party aggregate present has a reason in the remittance's purpose.
- Options: (a, preferred) leave listing and service provider out; (b) state a reason if the story gives one.
- Needs decision: no
- From: parties (F5), context (F5, party part)

### road/17#F8 · Low · The account the payment is made from carries the alias "receivables"
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:AliasName` = `Lumeway receivables`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:Name` = `Lumeway Distribution Ltd`
- XPath: `sea/06-OrderResponse.xml:/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AliasName` = `Lumeway receivables`
- Why: `AliasName` is "An alias for the name of this financial account, to be used in place of the actual account name for security reasons". The account is the payer's, from which Lumeway pays its supplier, yet the alias calls it the receivables account, apparently from its use as a payee account in the sea flow (the only other file with this alias). The actual name is given next to it, so the alias is not used "in place of" the name, and no security reason appears.
- Condition: the payer account carries no alias, or one that fits an account payments are made from and stands in for the name.
- Options: (a, preferred: broad, money) drop the alias here, since the name is given; (b, context) a neutral or payables alias (e.g. "Lumeway payments"), in all examples carrying the account if it serves both directions.
- Needs decision: no
- From: broad (F5), money (F1), context (F3)

### road/17#F9 · Low · Line-level accounting parties repeat the header
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: `RemittanceAdviceLine/AccountingSupplierParty` is "The Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line" (likewise the customer). They serve remittances that settle invoices of several parties; here the only line settles `15-Invoice.xml` between the same two parties as the header, so they repeat it without a reason (IND5).
- Condition: line-level accounting parties are present only where they differ from the header's.
- Options: (a, preferred) drop them from the line; (b) keep them only if the story adds a line for another party's invoice (e.g. Trasvia's freight invoice).
- Needs decision: no
- From: parties (F6)

### road/17#F10 · Low · Invoice referred to twice in the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0166`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `VI-INV-26-0166`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:DocumentTypeCode` = `Invoice`
- Why: the line names the paid invoice in its billing reference, the element meant for the invoice being settled, and again as a generic document reference with type `Invoice` and the same issue date. Broad refuted it: the document reference adds the document type and is harmless. Not followed: `InvoiceDocumentReference` is itself a document reference and can carry the type code, so the second reference repeats the first (IND5).
- Condition: the paid invoice is referred to once in the line, in the billing reference.
- Options: (a, preferred) drop the generic `DocumentReference` (adding the type code to the invoice reference if wanted); (b) keep it only for another document, e.g. the invoice response `16-ApplicationResponse.xml`.
- Needs decision: no
- From: context (F4); refuted by broad (its "Considered and refuted")

## Checked and consistent
- Arithmetic (redone): `/RemittanceAdvice/cbc:TotalDebitAmount` = `4862160` − `/RemittanceAdvice/cbc:TotalCreditAmount` = `0` = `/RemittanceAdvice/cbc:TotalPaymentAmount` = `4862160`; the single line `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `4862160` with `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:BalanceAmount` = `0`, equal to the invoice's `15-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `4862160` (96 × 49 900 + 12 × 5 980).
- Terms: issued 2026-04-22, after the discount period (`15-Invoice.xml:/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-03`) and before the due date (`15-Invoice.xml:/Invoice/cbc:DueDate` = `2026-04-23`), so the full amount without the 2 % discount (97 243) and without penalty interest is right.
- References: invoice `VI-INV-26-0166` of 2026-03-24 resolves to `15-Invoice.xml`; the creditor reference `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF78VIINV260166` is the invoice's own; the payee account `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU790351041600000000209458` (XUF) is the invoice's; payer account `XB19BLUM38712001466206` at branch 387120 of the Bank of Lumeport; all pass `check_ids.py`.
- Means and purpose: credit transfer (`30`), as the invoice asks; `SUPP` (supplier payment) fits a goods invoice.
- Parties: accounting customer Lumeway pays accounting supplier Valdara, as in the invoice.

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL` against XUF amounts: suspected the remittance should state the conversion — refuted because the remittance advises the amount remitted in the invoice currency; the payer's conversion is between Lumeway and its bank, and an exchange rate is optional (from money, broad).
- `/RemittanceAdvice/cbc:PayerReference` = `LD-0149` beside `/RemittanceAdvice/cbc:PaymentOrderReference` = `LD-PAY-26-0149`: suspected two values for one reference — refuted because UBL distinguishes the payer's internal reference to its order for payment from the order for payment to the payer's bank, which may differ; the second also identifies the instruction (`/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `LD-PAY-26-0149`) (from money, context).
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF78VIINV260166`: suspected misuse of a payment reference — refuted because the definition names a reference "requested of the payer by the payee to accompany the payer's remittance", which the creditor reference is (from context).
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:IssueDate` = `2026-03-24` duplicating the billing reference — refuted by broad (adds the document type, harmless); not followed, kept as F10.
- `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian street name tagged as English — refuted by parties; not followed, made F5.
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: a GLN that could be real — refuted because prefix 952 is reserved by GS1 for examples and the check digit is correct (from parties).
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone`: telephone numbers could be real — refuted because +999 is reserved in ITU-T E.164 (from parties).
- `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: looks like a contract number — refuted because the definition does not say who assigns the identifier (from parties).

## Changed in the merge
- broad/F1, parties/F1, context/F2 → F1: parties' "Needs decision: yes" set to no; count corrected to 364.
- context/F5 split: contacts → F4 (with broad/F4, parties/F4), party data → F7 (with parties/F5), as in the utilities merges.
- broad/F5, money/F1, context/F3 → F8: combined; preferred option is broad's and money's (drop), context's alias kept as (b).
- context/F4 → F10: kept against broad's refutation, with the counter-argument.
- F5 and F6 added by the merge (F5 from a refutation of the parties part not followed).

## Outside this review
- The freight invoice `14-Invoice.xml` (Trasvia, due 2026-04-24) is not paid in the flow; whether the flow should show its payment is a question of the flow's scope (from broad).
