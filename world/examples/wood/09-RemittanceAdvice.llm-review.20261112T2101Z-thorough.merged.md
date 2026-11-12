# LLM review: 09-RemittanceAdvice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/09-RemittanceAdvice.xml`, Git blob `41a5df331d4ec5f08a936109c93263e9b39bd319` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 83ce5da 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### wood/09#F1 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the flow do (e.g. `01-RequestForQuotation.xml:/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). Affected here: the addresses of Valdara Industries and Crevalto Bank. The same element and value occur 219 times in 104 examples (merge recount, `grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>'`).
- Condition: No Urvanian address carries an administrative division in `cbc:Region`; the province, where given, is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if the world has a list for it).
- Options: (a, preferred) move the province of every Urvanian address to `CountrySubentity`, at the source of the Urvanian address format; (b) if the Urvanian "provinces" are economic regions in the world, rename them without "Province", record that in the story, and give any administrative division in `CountrySubentity`.
- Needs decision: no (the name itself says "province"; option (b) only would change the world)
- From: broad/F1, parties/F1, context/F1

### wood/09#F2 · Medium · A language code in `Language/LocaleCode`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply. The value `en` with `listID="ISO 639"` is the language itself and only repeats `Language/ID`, so the element carries a meaning other than its definition (section 6 names "a language code in `LocaleCode`" as Medium). The examples already use locale-like tags (`en-XB`, `en-XU`) in `languageID`; the Urvanian party carries no `LocaleCode`. The same element and value occur 362 times in 213 examples (merge recount, `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cbc:LocaleCode` present holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: (a, preferred) drop `LocaleCode` where no locale matters; (b) carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47) and name that list in `listID`.
- Needs decision: no
- From: broad/F2, parties/F2, context/F2

### wood/09#F3 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in its role here. The payer's contact answers questions about the payment (accounts payable); the payee's contact reconciles it (accounts receivable). Neither is an order desk or sales office with a customer-service officer, which is a seller's function towards its customers. `Customer service officer` occurs 395 times in 229 examples (merge recount, `grep -rho --include='*.xml'`).
- Condition: Each contact has a name, job title and department that fit the party's role in this remittance advice (payables, receivables) and agree with each other.
- Options: (a, preferred) role-specific contacts per party in the world, picked per document; (b) drop job title and department (or the contact) where only a functional mailbox is known.
- Needs decision: no
- From: broad/F4, parties/F3, context/F5

### wood/09#F4 · Low · Valdara's master data the remittance advice does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: A remittance advice tells the payee which invoices a payment settles; it needs the parties' identities and the payment details (section 4.8, no fillers). Valdara's share capital, stock-exchange listing and logistics service provider Castrano Logistics are carried in full and nothing in the document uses them; Castrano has no role in the flow (in 9 of the 11 wood examples, never in a role of its own: `grep -l Castrano world/examples/wood/*.xml | wc -l`).
- Condition: Valdara's description in this remittance advice carries a service provider, share capital and security listing only if the document does something with them.
- Options: (a, preferred) leave them out of this document; fixing the party rendering per document type covers the flow.
- Needs decision: no
- From: broad/F5, parties/F4, context/F6

### wood/09#F5 · Low · English-tagged renderings of Urvanian names are Italian
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: The `en-XU` renderings of Urvanian street names and of Valdara's legal form are Italian; the world's languages are English, Urvanian and Lisavan. 219 English-tagged street names in 104 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (merge recount, `grep -rhoE --include='*.xml' '<cbc:StreetName languageID="en[^"]*">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) '`; the broad part counted 217 in 102). Parties part (refuted): proper names are commonly kept untranslated and the world uses Italianate names consistently. The merge accepts that for street names but not for the legal form, a descriptive term; it cannot settle whether Italian is an intended exonym layer.
- Condition: Every text tagged with an English `languageID` is English, or the world states that these Italian forms are the official English-language names and legal forms in Urvania.
- Options: (a, preferred if intended) record the convention in the world's story; (b) English renderings.
- Needs decision: yes
- From: broad/F6; parties considered and refuted it, carried here with its argument

### wood/09#F6 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Marrowdale Sawmill Ltd carries 1996-01-01; the date occurs 271 times in 181 examples (merge recount, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`) for about 25 companies of every kind in the registers of all three countries (parties part), while other dates are specific (Valdara: 1962-04-12). Counter-argument (context part of `10-Order.xml`): it may be the date a register began; nothing in the examples says so.
- Condition: Each company's registration date is its own plausible date in the world, or the world documents an event that put these companies on the register on 1996-01-01; otherwise it is absent.
- Options: (a, preferred) its own date from the company's history; (b) record a 1996 (re-)registration in the story; (c) leave the date out.
- Needs decision: yes
- From: broad/F7, parties/F5

### wood/09#F7 · Low · The invoice is referenced twice on the line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `MS-INV-26-0635`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `MS-INV-26-0635`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:DocumentTypeCode` = `Invoice`
- Why: `BillingReference/InvoiceDocumentReference` ("A reference to an invoice") is the dedicated element for what the line pays. `RemittanceAdviceLine/DocumentReference` ("A reference to a document associated with this remittance advice line") refers to the same invoice again, with the same issue date, adding only the type code. It adds no document and makes a reader look for a further associated document that does not exist (no fillers).
- Condition: The invoice is referenced once, in the dedicated element; any `DocumentReference` on the line refers to another document.
- Options: (a, preferred) drop the line's `DocumentReference`; (b) replace it by a reference to another document the payment relates to (none exists in the flow).
- Needs decision: no
- From: broad/F3, logistics/F1, context/F3

### wood/09#F8 · Low · The line repeats the header's accounting parties
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: The line's parties are "the Accounting Supplier (Customer) Party related to the remittance information reported on this Remittance Advice Line"; they are needed where a line concerns other parties than the document (a payment covering several suppliers or group companies). Here the only line is between the same two parties as the header and says nothing new.
- Condition: Line-level accounting parties are present only where they differ from the header's.
- Options: (a, preferred) leave both out of the line; (b) keep them in a remittance advice of the world that pays several suppliers' invoices.
- Needs decision: no
- From: parties/F6, context/F4

## Checked and consistent
- Amounts (recalculated): TotalDebitAmount 34 800.00 = the one DebitLineAmount = `08-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `34800.00`; TotalCreditAmount 0.00; TotalPaymentAmount 34 800.00; BalanceAmount 0.00 (broad, money, context).
- The invoice reference MS-INV-26-0635 with issue date 2026-02-26 resolves to `08-Invoice.xml`; payment on 2026-03-26 is before its due date 2026-03-28, so no penalty applies (broad, money, logistics, context).
- PaymentID and InvoicingPartyReference RF83MSINV260635 are the creditor reference the invoice asked to be quoted; payee account XB78BLUM38712004398618 (branch 387120, BLUMXBLX, XBL) is the invoice's; payer account XU790351041600000000209458 agrees with branch 03510-41600 and CREVXUFR and is held in the customer's registered name; all check digits pass (`check_ids.py`, re-run by the merge) (broad, money, parties).
- PaymentPurposeCode SUPP (ISO 20022 "SupplierPayment") fits paying a supplier invoice; the invoice is a debit line (broad, money).
- Parties are described as in the rest of the flow; identifiers, tax schemes and endpoints follow each party's country (parties).

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XUF` for a payment of 34 800.00 XBL, without an exchange rate — refuted because paying a foreign-currency invoice from a home-currency account is ordinary, and the remittance tells the payee what it receives in the invoice currency; the conversion is between payer and bank (from broad, money).
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF83MSINV260635` not "an internal reference to the order for payment by the invoicing party" — refuted because the definition continues that it "may have been requested of the payer by the payee to accompany the payer's remittance", which the RF reference is (from broad, context).
- `/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0625` equal to `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VI-PAY-26-0625` — refuted because the payment order to the bank and the payment instruction are the same order, seen from the document and from the payment means (from broad).
- `/RemittanceAdvice/cbc:PayerReference` = `VI-0625` and `PaymentOrderReference` two values for the same payment order — refuted because PayerReference is the payer's internal reference (e.g. the payment run), PaymentOrderReference the order to its bank; a payer can have both (from money).
- `PaymentOrderReference` and `PayerReference` sharing the serial 0625 with the request for quotation `VI-DOC-26-0625` — refuted because the prefixes name different number series of the buyer and nothing uses one as the other (from logistics, context).
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian under an English tag — refuted as a world convention (from parties). The merge keeps it as F5 with both arguments.
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: a real ICD — refuted because `0990` is not in `world/codelists/sources/peppol/ICD.xml` (from parties).
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER`: a real MIC — refuted because it is not in `world/codelists/sources/iso10383/ISO10383_MIC.csv` (from parties).
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: wrong ISIN check digit — refuted by `check_ids.py` (from parties).
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: "number of shares" against an amount — refuted because the element is of type Amount; whether it belongs here is F4 (from parties).

## Changed in the merge
- context/F1 "Needs decision: yes" → F1 "no", as in the other examples of this merge.
- context/F2, parties/F2, broad/F2 → F2: preferred option is dropping `LocaleCode`.
- broad/F6: count corrected from 217 in 102 files to 219 in 104 (merge recount); joined with the parties' refuted candidate as F5, "Needs decision: yes" kept.
- broad/F3, logistics/F1, context/F3 → F7 and parties/F6, context/F4 → F8: combined, wording from the clearest part; no change of severity.
