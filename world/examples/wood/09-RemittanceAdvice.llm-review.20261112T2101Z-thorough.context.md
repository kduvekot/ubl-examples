# LLM review: 09-RemittanceAdvice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/09-RemittanceAdvice.xml`, Git blob `41a5df331d4ec5f08a936109c93263e9b39bd319` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### wood/09#F1 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, i.e. an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the same examples do (`Upland State`, `Coastal State`). The same value is in `Region` in 104 examples (`grep -rl --include='*.xml' 'Region>Province of Ferrano' world/examples | wc -l`).
- Condition: Every Urvanian address that names its province carries it in `cbc:CountrySubentity` (with a national code in `CountrySubentityCode` if the world has one), and `cbc:Region` is either absent or holds a region in the UBL sense.
- Options: Preferred: move the value to `CountrySubentity` everywhere (one change at the source of the Urvanian address format). Alternative: if in the world the Urvanian "provinces" are not administrative divisions but economic regions, rename them so that the name does not say "Province", and record that in the world story.
- Needs decision: yes (whether Urvanian provinces are administrative divisions is a decision about the world)

### wood/09#F2 · Medium · A language code in `Language/LocaleCode`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). `en` from ISO 639 is the language itself and repeats `Language/ID`; it says nothing about the locale, so the element carries a meaning other than its definition (the severity guide names "a language code in `LocaleCode`" as Medium). The same pair occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`). The documents themselves already use locale-like tags such as `en-XU` and `en-XB` in `languageID`.
- Condition: Wherever `cbc:LocaleCode` is present it holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: Preferred: drop `LocaleCode` where no locale matters (the document gains nothing from it). Alternative: carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`.
- Needs decision: no

### wood/09#F3 · Low · The invoice is referenced twice on the line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `MS-INV-26-0635`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `MS-INV-26-0635`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:DocumentTypeCode` = `Invoice`
- Why: The line already refers to the invoice it pays through the dedicated `BillingReference/InvoiceDocumentReference`. `DocumentReference` ("A reference to a document associated with this remittance advice line") then refers to the same invoice again, with the same date and a type code saying it is an invoice. The second reference adds nothing and makes it look as if a further document were associated with the payment.
- Condition: The invoice is referenced once, in the dedicated element; a `DocumentReference` on the line, if any, refers to another document.
- Options: Preferred: drop the line's `DocumentReference`.
- Needs decision: no

### wood/09#F4 · Low · The line repeats the header's parties
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: The line's parties are "The Accounting Supplier (Customer) Party related to the remittance information reported on this Remittance Advice Line"; they are needed where a line concerns other parties than the document (e.g. a payment covering several suppliers or group companies). Here they are the same two parties as the header, on the only line, and say nothing new.
- Condition: Line-level parties are present only where they differ from the header's.
- Options: Preferred: drop them from the line.
- Needs decision: no

### wood/09#F5 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role the party has in this document. Here the paying party's contact answers questions about the payment (accounts payable); the payee's contact is the one reconciling the payment (accounts receivable). A customer-service officer in the Sales department answers customers; it is not the function this role needs. The same Sales contact is used for every role of these parties in every example of the flow.
- Condition: Each contact in this document belongs to the function the party's role here needs (purchasing, goods receipt, shipping, customs, accounts receivable or payable), or the contact is left out.
- Options: Preferred: give each party role-specific contacts in the world data and pick the one that fits the role of the document. Alternative: leave the contact out where the document does not need one.
- Needs decision: no

### wood/09#F6 · Low · Party master data this document does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Under the rule "no fillers" every optional element needs a reason in this document. A remittance advice tells the payee which invoices a payment settles; it needs the parties' identities and the payment details. Valdara's logistics service provider ("Warehousing and despatch" — a despatching service for a party that, in this flow, only receives goods) and its stock-exchange listing are master data of the party that look copied into the document; nothing in the document uses them. Castrano Logistics appears in 9 of the 11 wood examples, never in a role of its own (`grep -c Castrano world/examples/wood/*.xml`).
- Condition: Every party detail present in the document has a stated use in this document.
- Options: Preferred: carry the full description of a party only in the documents whose purpose needs it (e.g. the securities listing nowhere in this flow, the service provider only where it acts) and identify the party by ID and name elsewhere.
- Needs decision: no

## Checked and consistent
- The invoice referenced is `08-Invoice.xml` (ID and issue date agree); amount 34 800.00 = the invoice's payable amount; balance 0.00.
- Payee account `XB78BLUM38712004398618` and RF reference `RF83MSINV260635` are those the invoice requested; `check_ids.py` confirms both check digits and the payer's account.
- Issued 2026-03-26, before the due date 2026-03-28.

## Considered and refuted
- `/RemittanceAdvice/cbc:PayerReference` = `VI-0625` and `PaymentOrderReference` = `VI-PAY-26-0625` share the running number of the request for quotation (`VI-DOC-26-0625`): suspected confusion — refuted because they belong to different number series of the buyer (prefixes PAY and DOC).
- `/RemittanceAdvice/cbc:InvoicingPartyReference` = `RF83MSINV260635`: suspected that a creditor reference is not "an internal reference to the order for payment by the invoicing party" — refuted because the definition continues "This may have been requested of the payer by the payee to accompany the payer's remittance", which the RF reference is.
