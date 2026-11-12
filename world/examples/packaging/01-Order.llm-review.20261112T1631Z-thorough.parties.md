# LLM review: 01-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/01-Order.xml`, Git blob `ddc64baa43ff662f7332461675890f01136aaac2` (committed)
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

### packaging/01#F1 · Medium · A province is given in Region
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in which this address is located". A province is a first-level subdivision of the country, which is what CountrySubentity is for ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"), and which the Bayvarran addresses of the same example do use (`/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`). Every Urvanian address in the examples has Region and none has CountrySubentity (215 Urvanian addresses counted with lxml over `world/examples/*/*.xml`; `Province of Ferrano` occurs in 104 examples), so the problem is systematic.
- Condition: no address in the example holds a province or other country subdivision in Region; the province of Ferrano is in CountrySubentity (with a CountrySubentityCode if Urvania has such a list), in both addresses.
- Options: (a) preferred: move the province to CountrySubentity, as Bayvarra does for its states, so all three countries use the same element for the same level; (b) keep Region only for a real economic region (for example the Trade Accord area), if the story has one.
- Needs decision: no

### packaging/01#F2 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL 2.5 defines Language/LocaleCode as "A code signifying the locale in which this language is used". A locale is a language in a region (English as used in Bayvarra); `en` with listID `ISO 639` is the bare language code that Language/ID already carries. The same value occurs 362 times in 213 examples (Grep over `*.xml` for `<cbc:LocaleCode listID="ISO 639">en<`), only on English-speaking parties; the Urvanian buyer and carrier of this example have none.
- Condition: LocaleCode, where present, names a locale (language and region, e.g. a BCP 47 tag such as `en-XB` with a matching listID), or is absent.
- Options: (a) preferred: a locale such as `en-XB`, which matches the `en-XU`/`en-XB` tags the examples already use in languageID; (b) remove LocaleCode where no locale matters to the document.
- Needs decision: no

### packaging/01#F3 · Low · The buyer's contact is a sales contact
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Party/Contact is "The primary contact for this party"; in BuyerCustomerParty of an Order it is the person the seller turns to about the purchase. Valdara Industries buys stretch film here; an order desk in the sales department, staffed by a customer service officer, is the contact for Valdara's own customers, not for its suppliers. The seller's contact in the same order is described identically (`/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`), which fits the seller. Across the examples, contact job titles and departments look derived from the kind of party rather than the role: `Customer service officer`/`Sales` goes with names such as `Purchasing` (52 contacts), `Buying office` (41) and `Goods inwards` (10) (lxml count of Contact Name/JobTitle/Department over `*.xml`).
- Condition: the buyer's contact in this order is a purchasing contact (name, job title and department agree and belong to buying).
- Options: (a) preferred: give Valdara a purchasing contact for documents where it buys (e.g. Name purchasing, JobTitle buyer, Department purchasing); (b) give the buyer no Contact where the order does not need one.
- Needs decision: no

### packaging/01#F4 · Low · Two unrelated companies registered on the same date, 1 January 1996
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Rivermouth Packaging (Federal business register of Bayvarra) and Trasvia Haulage (Commercial register of Urvania) are in different registers of different countries but share the same date, and 25 different companies across all three countries carry exactly `1996-01-01` (271 occurrences in 181 examples; lxml count over `*.xml`), while the few other companies have individual dates (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`). This looks like a default rather than a fact of the world (IND5: no fillers). If the story has a reason (for example a re-registration of all companies on one date under the Trade Accord), it is not visible in the documents.
- Condition: each company's RegistrationDate is the date of its own registration in the story, or the element is absent where the story has none.
- Options: (a) preferred: give each company its own registration date from its history; (b) remove RegistrationDate for companies without one; (c) if 1996-01-01 is a story fact (a common re-registration date), confirm it so later reviews can accept it.
- Needs decision: yes

### packaging/01#F5 · Low · Party master data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Party/ServiceProviderParty is "A party providing a service to this party"; Valdara's warehousing and despatch provider plays no part in this order: the film is collected FCA at Rivermouth by Valdara's carrier Trasvia (`/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`), and Castrano is named nowhere else in the order. Party/FinancialAccount is "The financial account associated with this party"; the order has no payment means or terms, so the seller's bank account has no use in it. SecurityListing ("One or more securities issued by this Party Legal Entity that are listed on regulated markets") is not something a purchase order for stretch film relies on. The same Castrano service provider block occurs in 75 examples (Grep for `VI-SP-2026-01` over `*.xml`). These look copied from master data.
- Condition: every party detail in the order has a role in the order (or the example's intent says why it is there).
- Options: (a) preferred: leave out ServiceProviderParty, the seller's FinancialAccount and the SecurityListing in this order; (b) if Castrano is meant to receive or despatch the goods, show it in its role (delivery party or despatch party) instead.
- Needs decision: no

## Checked and consistent
- Party identifiers: Valdara `XU-R-104274` is the same in PartyIdentification, PartyLegalEntity/CompanyID and the endpoint `XU:XU-R-104274`; Rivermouth `20412740` likewise (`XB:20412740`); Trasvia `XU-R-104822` likewise. The despatch party is Rivermouth with the same register ID.
- The same three parties carry the same identifiers, tax IDs, legal forms and addresses in `02-Invoice.xml` (Valdara, Rivermouth) and in the flow index.
- check_ids.py: ISIN `XU0001042501` and the IBAN-like account `XB96BLUM38020504712805` have valid check digits.
- Fictional codes against real registers: MIC `XFER` is not in the ISO 10383 list (`world/codelists/sources/iso10383/ISO10383_MIC.csv`); bank owner code `BLUM` is not in `world/codelists/sources/bic/owner-codes.txt`; telephone prefix `+999` is reserved by ITU (own knowledge); the `.example` domains are reserved.
- Legal entity: Valdara as a listed public limited company (SUA), large, with share capital and a stock listing; Rivermouth and Trasvia as small private limited companies; all active. The legal form text agrees with the code in each case.
- Tax schemes: Valdara national VAT of Urvania in XUF; Rivermouth state sales tax of the Coastal State in XBL with the jurisdiction address naming the Coastal State.
- Contacts of the seller (order desk, sales) and of the carrier (planning desk, operations) fit their roles.
- Carrier: Trasvia, an Urvanian road haulier with an international road haulage permit valid until 2030-06-30, collecting under FCA, is the buyer-nominated carrier FCA implies.

## Considered and refuted
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: an Italian-looking text tagged `en-XU` — refuted because it is a proper name in the form used in Urvanian English (the same pattern as `Ferrano` and the legal form names), and the world gives Urvania Italianate exonyms consistently; the tag says which variety of English uses the name, not that the words are English.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`: customs trader IDs in an order — refuted because the sale is cross-border (Bayvarra to Urvania, tax category G "Export outside Bayvarra"), so both parties' customs identities are relevant to the transaction.
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`: carrier licence in an order — refuted because the carrier crosses the Bayvarra–Urvania border and the seller hands the goods to it under FCA; its haulage permit is a reasonable thing for the buyer to state.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: ISO 6523 ICD 0990 — refuted as a clash with a real register, because ICD 0990 is not assigned (own knowledge: assigned ICDs end in the 0200s).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: UBL defines it as "The number of shares in the capital stock of a corporation", but the element is an Amount with currencyID; the value is a capital amount, the only reading the data type allows — refuted for this example (an inconsistency in the UBL definition, a possible point for the TC write-up).
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Rivermouth Packaging, dispatch, Lumeport`: a delivery location without address or ID — refuted because the seller's full address is in the order and the description names the point within it, which is enough for an FCA named place.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:EndOfLifeTreatment/cac:TreatmentLocation/cbc:Name` = `Rinova Recovery's plant, Ferrano`: a company name in a location name — refuted because it names the plant (the place) of that company, not the company as a party.
