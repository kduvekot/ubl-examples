# LLM review: 02-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/02-Invoice.xml`, Git blob `24cc8e618ee2697a2fbe496ce115022415fe249c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/02#F1 · Medium · A province is given in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state", i.e. CountrySubentity, which the Bayvarran addresses of the same invoice use (`/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`). All 215 Urvanian addresses in the examples use Region and none CountrySubentity (lxml count over `*.xml`).
- Condition: the province of Ferrano is not in Region; it is in CountrySubentity.
- Options: (a) preferred: move it to CountrySubentity, as for Bayvarra; (b) keep Region only for a real economic region.
- Needs decision: no

### packaging/02#F2 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is the language itself, already in Language/ID. The same value occurs 362 times in 213 examples (Grep over `*.xml`), only on English-speaking parties.
- Condition: LocaleCode names a locale (language and region) or is absent.
- Options: (a) preferred: a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### packaging/02#F3 · Low · Valdara's address and legal form are described differently than in the order
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: the English renderings of Valdara's address carry `languageID="en-XB"` here, but `en-XU` in the order the invoice answers (`01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`, languageID `en-XU`), for the same text. The legal form is given once, without languageID, here, but in Urvanian and en-XU in the order (`01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`). Across the examples the tag of Valdara's English address follows the country of the document's issuer (en-XU in 24 examples, en-XB in 18; Velumi Trading likewise en-XL/en-XB; lxml count over `*.xml`), so the same party's address is tagged as two different varieties of English. Within this invoice the tag also differs from the document's `/Invoice/cbc:DefaultLanguageCode` = `en`, which is harmless.
- Condition: the same text of Valdara's address carries the same languageID in every example, and its legal form is rendered the same way wherever it is given (or the difference is deliberate and stated as a convention).
- Options: (a) preferred: tag a party's English names with the variety of the party's own country (en-XU for Valdara), which is what the party registers and what the order uses; (b) adopt the issuer's variety as an explicit convention and apply it to the legal form as well.
- Needs decision: yes

### packaging/02#F4 · Low · The contacts of the accounting parties are order desks in sales
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: Party/Contact is "The primary contact for this party"; under AccountingCustomerParty ("The accounting customer party") it is whom the supplier contacts about the invoice and its payment, and under AccountingSupplierParty whom the customer asks about the invoice. For Valdara, the invoiced buyer, an order desk in its sales department is neither its accounts payable nor its purchasing; for Rivermouth an order desk is a plausible but not an accounting contact. The same contacts are used in the order (`01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`), i.e. each party has one contact for every role.
- Condition: the contacts of the accounting parties belong to invoicing or payment (or are absent).
- Options: (a) preferred: give each accounting party an accounts contact (accounts payable for Valdara, accounts receivable or billing for Rivermouth); (b) omit the Contact where the invoice does not need one.
- Needs decision: no

### packaging/02#F5 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID". Rivermouth shares exactly this date with 24 other companies in three different registers (271 occurrences in 181 examples, lxml count over `*.xml`), which looks like a default (IND5).
- Condition: Rivermouth's RegistrationDate is the date of its own registration in the story, or absent.
- Options: (a) preferred: an individual date from its history; (b) remove the element; (c) confirm 1996-01-01 as a story fact.
- Needs decision: yes

### packaging/02#F6 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: ServiceProviderParty is "A party providing a service to this party"; Valdara's warehousing provider has no part in an invoice for stretch film collected by Valdara's haulier. The stock listing of the customer is not used for invoicing or payment. Both appear to be copied from master data (the Castrano block is in 75 examples, Grep for `VI-SP-2026-01` over `*.xml`).
- Condition: every customer detail in the invoice has a role in invoicing, payment or tax.
- Options: (a) preferred: leave both out; (b) if the story needs Castrano, show it in a role the invoice uses.
- Needs decision: no

## Checked and consistent
- OrderReference `VI-PO-26-0521` resolves to `01-Order.xml`; buyer and seller there are the accounting customer and supplier here, with the same register IDs, tax IDs, legal entities, endpoints and postal address values.
- BuyerCustomerParty and SellerSupplierParty repeat the accounting parties by ID and name only, which is consistent.
- The payee account `XB96BLUM38020504712805` is Rivermouth's own account (`/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`), named after Rivermouth Packaging Ltd, at the Harbour branch of the Bank of Lumeport; check digits valid (check_ids.py).
- Rivermouth's tax registration (Coastal State sales tax, `CO-1238220`) and Valdara's (Urvanian VAT, `XU007299291`) match the order.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`: the party's account repeated next to the payee account — refuted because in an invoice the supplier's account is used for payment; the repetition is consistent.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:Address/cbc:CityName` = `Lumeport`: a branch address with only a city, while the bank's head office has a full address — refuted because the branch is identified by its branch ID and name; the town is enough for the branch's location.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`: customs trader ID in an invoice — refuted because the supply is an export to Urvania and the invoice is a customs-relevant document.
