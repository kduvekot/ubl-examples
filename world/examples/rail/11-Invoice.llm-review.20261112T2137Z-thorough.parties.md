# LLM review: 11-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/11-Invoice.xml`, Git blob `ee9c00c2aed8b2e82ac3390db74cfce890bdf1a1` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/11#F1 · Medium · Province in Region of the supplier's and the bank's address
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"). The customer's Bayvarran address in the same document does so (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no Urvanian address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it.
- Needs decision: no

### rail/11#F2 · Medium · Language code in LocaleCode of the customer
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language. Locale Code is "A code signifying the locale in which this language is used." `en` (listID ISO 639) is a language code and repeats `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`. The value occurs 362 times in 213 example files (`grep -o 'LocaleCode listID="ISO 639">en<'` over `*.xml`).
- Condition: the customer's Language has no LocaleCode, or one that names a locale from a list of locales.
- Options: (a) drop it (preferred); (b) a locale such as `en-XB` with a locale list (e.g. BCP 47).
- Needs decision: no

### rail/11#F3 · Medium · Gate in AdditionalStreetName of the customer's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: Address. Additional Street Name is "An additional street name used to further clarify the address". "Gate 3" is an entrance of the site, not a street name; on the invoice the address identifies the customer, and a vehicle gate has no place in it.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) remove it from the postal address (preferred); (b) state a gate, where a transport document needs it, at a delivery location.
- Needs decision: no

### rail/11#F4 · Low · "English" renderings of the addresses and legal form are Italian
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/11#F5 · Low · Customer's contact on the invoice is its sales customer service
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting customer's contact handles the invoice and its payment (accounts payable) or, as buyer, purchasing. Lumeway's sales customer service serves Lumeway's own customers. The same contact is used for Lumeway as buyer in `01-Order.xml` and as consignee in the transport documents.
- Condition: the accounting customer's contact is Lumeway's accounts-payable or purchasing function.
- Options: (a) an accounts-payable contact (preferred); (b) role-specific contacts in Lumeway's master data.
- Needs decision: no

### rail/11#F6 · Low · Master data the goods invoice does nothing with
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Section 4.8: the invoice does nothing with the supplier's stock-exchange listing or its warehousing provider Castrano Logistics, nor with the customer's share capital.
- Condition: every legal-entity and service-provider element present has a purpose in the invoice.
- Options: (a) drop them here (preferred); (b) keep the supplier's own share capital if the world's invoicing rules require it (see "Considered and refuted").
- Needs decision: no

## Checked and consistent
- Accounting supplier and seller Valdara (`XU-R-104274`), accounting customer and buyer Lumeway (`20410274`): the seller and buyer of the order referenced (`01-Order.xml`), with identical full descriptions apart from the differences noted in the order's review (the order tags Valdara's address `en-XB`; here it is `en-XU`, as in the other examples).
- Payee account name `Valdara Industries SUA` equals the supplier's registration name; the IBAN-like account and the RF reference have correct check digits; GLN `9520610900008` and ISIN `XU0001042501` correct.
- Customer's tax scheme (state sales tax, Upland State) and supplier's (national VAT) fit their countries and the export treatment.
- Codana Identification Agency (`XU-R-105644`) as issuer of the property identifier is the same as in `01-Order.xml`.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: the supplier's contact on an invoice should be billing — refuted: the seller's sales order desk is a legitimate contact for the buyer about a goods invoice that follows its order.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: share capital copied into the invoice — refuted: several real jurisdictions require a company's share capital on its business documents and invoices (own knowledge, e.g. Italy), a legitimate reason for the supplier's own value.
