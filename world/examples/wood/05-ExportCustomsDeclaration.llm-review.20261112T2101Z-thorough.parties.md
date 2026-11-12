# LLM review: 05-ExportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/05-ExportCustomsDeclaration.xml`, Git blob `485e09ca0ec698fc71593b783ad60898b71c45fd` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### wood/05#F1 · Medium · Province of Ferrano in Region instead of CountrySubentity
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "the recognized geographic or economic region or group of countries in which this address is located", and `Address/CountrySubentity` as "the political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, an administrative division, so it belongs in `CountrySubentity`. The Bayvarran addresses in the same flow do exactly that (e.g. `01-RequestForQuotation.xml:/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`, with `CountrySubentityCode`). Affected here: the addresses of Trasvia Haulage, Valdara Industries. The same element and value occur 219 times in 104 examples (`grep -o '<cbc:Region>Province of Ferrano</cbc:Region>'` over `*.xml`), so this is a generator-wide pattern for Urvanian addresses.
- Condition: No address in this example carries the Urvanian province in `cbc:Region`; the province is given in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` where Urvania's subdivision list has a code).
- Options: (Preferred) move the province of every Urvanian address to `CountrySubentity`, generator-wide, adding the subdivision code if the world defines one; this matches the Bayvarran addresses. Alternative: if the world really means an economic region rather than the province, rename it accordingly and still give the administrative division in `CountrySubentity`.
- Needs decision: no

### wood/05#F2 · Medium · Language code 'en' in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "a code signifying the locale in which this language is used". A locale is a language as used in a region or country; the example itself distinguishes locales of English in its `languageID` attributes (`en-XB`, `en-XU`). The value `en` with `listID="ISO 639"` is a language code only and repeats `Language/cbc:ID`, so the element carries a meaning other than its definition. The Urvanian parties in the flow carry no `LocaleCode` at all, so the parties are also described unevenly. The same value occurs 362 times in 213 examples (`grep '<cbc:LocaleCode listID="ISO 639">en<'` over `*.xml`).
- Condition: Every `cbc:LocaleCode` in this example either holds a locale (language and country, e.g. `en-XB`) with a list identifier for locales, or is absent.
- Options: (Preferred) a locale value such as `en-XB` with a locale list (e.g. BCP 47), consistent with the `languageID` values the world already uses; or remove `LocaleCode` where the locale adds nothing to `Language/cbc:ID`.
- Needs decision: no

### wood/05#F3 · Low · Contact does not fit the party's role in this export customs declaration
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist question for a party in a role is whether its `Contact` fits the role. In this export customs declaration: Marrowdale Sawmill as exporter (Sales office / Customer service officer / Sales), whose contact should be the one who handles the export declaration: shipping or customs; Valdara Industries as consignee (Order desk / Customer service officer / Sales), whose contact should be the one who receives the goods: goods-in or the warehouse. A sales department and a customer service officer are the functions of a seller towards its customers; they do not fit a party acting as consignee or exporter. The parties carry the same contact in every example of the flow, whatever role they have there (Valdara Industries' `Order desk` in Sales also as consignee, importer and accounting customer). Across all examples the job title `Customer service officer` occurs 395 times in 229 examples (`grep -o` over `*.xml`), with departments always `Sales`, including contacts named `Purchasing`, `Buying office` and `Goods inwards`, so the job title and department look like a default rather than a description of the contact.
- Condition: Each contact listed above has a name, job title and department that fit the role the party has in this export customs declaration, and name, job title and department agree with each other.
- Options: (Preferred) give each party role-specific contacts in the world (purchasing, goods-in, despatch, customs, accounts) and pick the one for the role the party has in each document; alternatively drop `JobTitle` and `Department` where only a functional mailbox is known.
- Needs decision: no

### wood/05#F4 · Low · Master data of Valdara Industries the document does not use
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Valdara Industries is described in this export customs declaration with data from its master record that the document does nothing with: a `ServiceProviderParty` (Castrano Logistics, "Warehousing and despatch", a logistics service provider of the buyer) and, in its legal entity, its share capital (`CorporateStockAmount`) and its stock-exchange listing (`SecurityListing`). Nothing else in the document involves Castrano Logistics, and nothing in a export customs declaration depends on Valdara's share capital or listing. Data copied from a party's master data into a document that does not use it is a Low finding (section 4.8). The same block appears in every full description of Valdara in the flow (01–09).
- Condition: Valdara Industries' description in this export customs declaration carries a service provider, share capital and security listing only if the document does something with them (e.g. the service provider receives the goods or acts for Valdara here).
- Options: (Preferred) leave the service provider, share capital and security listing out of this document and keep them for documents whose purpose involves them (e.g. a party master data or registration context). Fixing this in the generator's party rendering per document type would cover all examples of the flow.
- Needs decision: no

### wood/05#F5 · Low · Legal form of an Urvanian party in one rendering without language, unlike its address
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Ban Kumek`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`
- Why: In this example the Urvanian parties (Trasvia Haulage, Valdara Industries) give their address in two renderings, Urvanian (`qau`) and English, but their legal form only once, without `languageID`. In the examples issued in Urvania, Valdara Industries gives both renderings of its legal form with their language, e.g. `01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)` (`qau`) and `cbc:CompanyLegalForm[2]` with `en-XU`. So Valdara Industries is described differently from example to example, and within this example its address and its legal form follow different language rules.
- Condition: Within this example, each Urvanian party's legal form follows the same language rule as its address: either both renderings, each with its `languageID`, or one rendering with its `languageID`.
- Options: (Preferred) render the legal form like the address (Urvanian and English, each tagged), as the Urvanian-issued examples do; or, if a Bayvarran issuer writes only English, tag the single rendering with `languageID` and say why the address keeps the Urvanian rendering (it is needed for delivery).
- Needs decision: no

### wood/05#F6 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "the registration date of the CompanyID". Here Marrowdale Sawmill Ltd and Trasvia Haulage SRU are each registered on 1996-01-01. Across all examples this date is given 271 times in 181 examples (`grep` over `*.xml`) for 25 different companies in all three countries' registers (Bayvarra's federal business register, the Urvanian commercial register and Lisavu's register), from a sawmill and a haulier to ports, an airport cargo terminal, a telecom company and an insurer (counted with lxml over every `PartyLegalEntity` in `*.xml`). A first of January shared by companies of every kind in three registers is not plausible as their actual registration dates and looks like a filler, which the rules exclude, unless the world has an event (e.g. a re-registration of all companies under the Trade Accord) that explains it.
- Condition: The registration date of each company in this example is either its own plausible date in the world, or the world documents an event that put these companies on the register on 1996-01-01; otherwise it is absent.
- Options: (Preferred) give each company its own registration date from its history in the world; or, if a 1996 re-registration is part of the story, record it there so the date has a reason; or leave the date out where the world has none.
- Needs decision: yes

### wood/05#F7 · Low · Customs authority described as a company in a commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The customs authority Customs and Border Service of Bayvarra is described as a company: its legal entity is registered in the Federal business register of Bayvarra with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register") and carries `CompanyLiquidationStatusCode` `ACTIVE` ("Active, not in liquidation"). A customs administration is a public body established by law; it is not entered in a commercial register and cannot be in liquidation, so these values describe a kind of party it is not (checklist: "a public body or a department is not a company in a commercial register and has no liquidation status"). Nothing in the declaration uses them.
- Condition: The customs authority's legal entity, if present, describes it as a public body (no commercial-register type, no liquidation status).
- Options: (Preferred) leave `PartyLegalEntity` out for the authority, or describe its legal basis with a registration type for public bodies if the world's list has one; drop the liquidation status.
- Needs decision: no

## Checked and consistent
- Every full description of the same party in the flow was compared field by field (script over `*.xml`): Valdara Industries is described identically in its nine full descriptions (01–09) apart from the language renderings noted above; Marrowdale Sawmill identically in all eleven examples; Trasvia Haulage identically in 04, 05 and 06; Brackenmere Furniture identically in 10 and 11.
- Every short party reference (identifier and name only, e.g. signatories, `SellerSupplierParty`/`BuyerCustomerParty` next to the accounting parties, consignor, transport user, bill-to) carries the same register identifier as the full description of that party.
- Identifiers per party are consistent: register number in `PartyIdentification` = `PartyLegalEntity/CompanyID`; customs trader number, tax number and endpoint (`XB:20412329`, `XU:XU-R-104274` …) follow the party's country; tax schemes fit the country (Bayvarra: state sales tax STT, level STATE, Upland State; Urvania: VAT, level NATIONAL).
- `check_ids.py`: all check digits in this example pass.
- The carrier Trasvia Haulage (ISIC 4923, road freight, international haulage permit valid to 2030-06-30) fits its role; it is the same party in 04, 05 and 06.
- The customs authority is that of the country of the declaration (Bayvarra for the export, Urvania for the import), and the exporter/importer is the seller/buyer of `03-Order.xml`.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: the English rendering of Valdara's street is Italian text, so the `languageID` would not match the language — refuted because a street's proper name is commonly kept untranslated in English text, and the world consistently uses Italianate names for Urvanian streets and towns in its English renderings (`Via delle Officine` alone 80 times over `*.xml`); this is a world convention, not a mismatch of the rendering.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: the ISO 6523 identifier could use a real ICD — refuted because ICD `0990` is not in the real ICD list in `world/codelists/sources/peppol/ICD.xml`, so it cannot be mistaken for a real one.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER`: the market code might be a real ISO 10383 MIC — refuted because `XFER` is not in `world/codelists/sources/iso10383/ISO10383_MIC.csv`.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: wrong ISIN check digit — refuted because `check_ids.py` reports the ISIN as correct.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: UBL defines `CorporateStockAmount` as "the number of shares in the capital stock", while the value is an amount in Ferra — refuted because the element is of type Amount, so the amount of the capital stock is the only reading the type allows; the wording is UBL's own (it is reported here only as a remark on the definition). Whether the element belongs in this document is a separate finding.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`: the same Urvanian town is tagged `en-XB` here but `en-XU` in the Urvanian-issued examples (e.g. `01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`) — refuted because `languageID` names the language variant of the rendering, which follows the issuer's English; the text is the same.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`: a customs authority under "General public administration activities" — refuted because ISIC Rev.4 class 8411 includes the administration of fiscal affairs and the collection of duties on goods (own knowledge of ISIC).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Bayvarran side`: exit office without an identifier — refuted because no example of the world identifies a customs office by code (the same name occurs, without identifier, in 7 examples, `grep -l` over `*.xml`), so there is no identifier to use; the name names the place.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`: an authority contact should be reachable when the goods cross — refuted because the declaration is issued and valid from Thursday 2026-02-26 during those hours.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`: carrier detail in an export declaration — refuted because the carrier and its international haulage permit are relevant to the export of goods by road.
