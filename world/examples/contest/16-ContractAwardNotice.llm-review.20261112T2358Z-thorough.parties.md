# LLM review: 16-ContractAwardNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/16-ContractAwardNotice.xml`, Git blob `22f99199125c95d2a66f61bed50f597234a75af6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 219a684 2026-11-12 Reviews of the road flow, run 20261112T2311Z-thorough: merge complete
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

### contest/16#F1 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- Why: The example describes Lumeport Public Works Department, Bayvarra Information Service with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register: A register of businesses", world list CorporateRegistrationTypeCode) in the "Federal business register of Bayvarra", and with `CompanyLiquidationStatusCode` `ACTIVE` ("A code signifying the party's liquidation status"; code: "Active, not in liquidation"). These are public bodies (a city department, a federal information service): they are not businesses, are not entered in a register of businesses and are not wound up by liquidation (section 5, "a public body or a department is not a company in a commercial register and has no liquidation status"). A department of a city is moreover not a legal person; the legal entity behind the Public Works Department is the City of Lumeport. The same example calls the department "a department of the city of Lumeport" in its contracting party type, so the legal-entity data contradicts the party type next to it. The world list has no register type for public bodies (its codes are COMMERCIAL, CHARITY, ASSOCIATION, FARM). The same description is carried by every occurrence of these parties in the world (Lumeport Public Works Department 55, Bayvarra Information Service 12, Procurement Review Board of Bayvarra 7 party aggregates, counted by party name over `world/examples/*/*.xml`).
- Condition: No public body in the example carries a `CompanyLiquidationStatusCode` or a corporate registration scheme of the type "Commercial register"; the legal entity given for the Public Works Department is either the body with legal personality (the City of Lumeport) or explicitly a department of it.
- Options: (preferred) leave out `CompanyLiquidationStatusCode` and `CorporateRegistrationScheme` for public bodies and keep only the registration name and identifier, because the story needs no register type for them; or add a register type for public bodies to the world list, if the federal register really lists them; or give the City of Lumeport as the department's legal entity.
- Needs decision: yes

### contest/16#F2 · Medium · Language code in LocaleCode
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". A locale is a language together with the region or country it is used in (e.g. English as used in Bayvarra); the value `en` with `listID` `ISO 639` is the ISO 639 language code itself and repeats `Language/cbc:ID` of the same aggregate, so the element carries the language instead of a locale (section 6 names "a language code in `LocaleCode`" as Medium). In this example the Language of Valdara Industries has no `LocaleCode` at all, which shows that the code adds nothing to `cbc:ID`. The same value occurs 362 times in 213 examples (`grep -o '<cbc:LocaleCode listID="ISO 639">en'` over `world/examples/*/*.xml`).
- Condition: Every `Language/LocaleCode` in the example is either absent or holds a locale (language and country or region) from a list of locales, with that list as `listID`.
- Options: (preferred) leave out `LocaleCode`, because nothing in the example depends on a locale and `cbc:ID` already gives the language; or give a real locale (for instance the `en-XB` form the examples use for `languageID`) from a stated list.
- Needs decision: no

### contest/16#F3 · Medium · Winning team reduced to Brackenmere: Saltmere Engineering is not a winning party
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:Description` = `First prize to the Brackenmere and Saltmere design team, second to Valdara Industries. The jury withheld the third prize: no other design reached prize standard.`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:EconomicOperatorShortList/cac:PreSelectedParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `12-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: `WinningParty` is "A party that is identified as the awarded by a tender result". The tender result says the first prize goes to "the Brackenmere and Saltmere design team", and the tenderer qualification names Saltmere Engineering as member of that team (30 % in version 2, `12-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `30`). The structured result, however, names only Brackenmere Furniture as first-ranked winner and as the party invited to negotiate the follow-up contract, so a reader of the structured data does not learn that the prize and the negotiation concern a group with a second member. Who won is what a contract award notice is for.
- Condition: The award notice identifies every member of the winning group (in rank 1), or states in structured form that Brackenmere acts as lead for a group that includes Saltmere Engineering.
- Options: (preferred) add Saltmere Engineering as a further `WinningParty` with rank 1, because UBL has no group aggregate in `TenderResult` and eForms likewise lists every member of a winning group; optionally also as pre-selected party.
- Needs decision: no

### contest/16#F4 · Medium · Province in Region
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "the political or administrative division of a country in which this address is located, such as the name of its county, province, or state", i.e. `CountrySubentity`. The Bayvarran addresses of the same example put their state in `CountrySubentity` (with `CountrySubentityCode`), so the Urvanian province is in the wrong element (section 6 names "a province in `Region`" as Medium). The value occurs 219 times in 111 examples (`grep -o '<cbc:Region>Province of Ferrano'` over `world/examples/*/*.xml`).
- Condition: The province of Valdara's address is in `CountrySubentity` (with a code if the Urvanian list has one), and `Region` is absent or holds a region in the sense of the definition.
- Options: (preferred) move the province to `CountrySubentity`, as the Bayvarran addresses do.
- Needs decision: no

### contest/16#F5 · Low · Party tax exemption of the contracting authority stated as a sale
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReasonCode` and `ExemptionReason` are "A reason for the party's exemption from tax", i.e. the party's own status. The code `PUBLIC` comes from the Bayvarran list of exemption reasons for supplies (its other codes are export, drinking water, resale, levy, basic food, medicine) and is named "Sale to a public body", and the text begins "Sale to a public body": both describe a transaction, not the department's status. The second half of the text ("public bodies are exempt from the state sales tax") is the status the element asks for. Nothing in this document is sold, so the transaction wording has nothing to refer to here.
- Condition: The party's exemption reason in the example states the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) word the text as the status only ("Public body: exempt from the state sales tax") and keep the code, whose list definition ("A body of the federation, a state or a city buys free of sales tax") does describe the status; or add a status code for public bodies to the list.
- Needs decision: no

### contest/16#F6 · Low · Party master data the document does nothing with
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: Section 4.8: data copied from a party's master data into a document that does not use it. The Public Works Department's customs trader identifier (scheme `urn:ubl-examples:world:XB:customs-trader`) is relevant to customs declarations, not to a design contest; no part of this procurement document involves customs. For Valdara Industries, the second-prize winner, the notice also carries its customs trader number, its share capital, its stock-exchange listing and its logistics service provider Castrano Logistics ("Warehousing and despatch"): a design-contest award notice publishes who won which prize and does nothing with the winner's customs status, shares or warehouse. They are the master data Valdara carries as a seller in the goods flows (the same values in all 75 Valdara party aggregates, counted by party name over `world/examples/*/*.xml`). The same customs identifier is in all 55 aggregates of the department (counted by party name over `world/examples/*/*.xml`).
- Condition: The parties in the example carry only identifiers and legal data that this document or its procedure uses.
- Options: (preferred) leave these elements out of the procurement documents; keep them where the documents use them (customs, goods flows).
- Needs decision: no

### contest/16#F7 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: Section 5: the contact must fit the role the party has in this document. In this example Brackenmere Furniture, here in the role of a contest participant, gives its "Trade sales" desk and a "Customer service officer", the contact for its trade customers' orders, not someone who handles a design contest or a tender; Valdara Industries, a prize winner, gives its "Order desk" and a "Customer service officer", the contact for purchase orders. The contacts are the parties' general contacts from the goods flows, the same in every example of the world that carries these parties.
- Condition: Each contact in the example is one that handles the party's part in the contest (tendering or bids for participants, the registry or appeals for the review board), with job title and department that agree with it.
- Options: (preferred) give these parties a tendering or registry contact for the procurement documents; or leave the contact out where the document does not need one.
- Needs decision: no

### contest/16#F8 · Low · Registration date 1996-01-01 looks like a default, not the party's date
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday on which no register enters companies, and the same date is the registration date of 25 different companies in all three countries (Bayvarra, Urvania and Lisavu; 271 occurrences, counted over `world/examples/*/*.xml` by `RegistrationDate` and the `RegistrationName` beside it), among them Brackenmere, Castrano Logistics, Port of Lumeport and Selanu Telecom. That points to a filler rather than a date with a reason in the world (IND5). If the world has a reason (e.g. all registers were re-founded under the Trade Accord on that day), the date is right but the story should say so; this review could not settle that from the examples.
- Condition: The registration date of Brackenmere Furniture is a date with a reason in the world, or the element is absent.
- Options: (preferred) give each company its own registration date from its history; or leave the element out where nothing uses it; or, if 1996-01-01 is a real event in the world (one re-registration day), keep it.
- Needs decision: yes

## Checked and consistent
- Every party is described identically in every example of the flow that carries it (all leaf values compared per party name across the 16 examples; the pre-selected party in 15/16 is a subset of Brackenmere's data).
- For every party, `PartyIdentification/ID`, `PartyLegalEntity/CompanyID` and the suffix of `ElectronicAddressID` agree, and the tax scheme's jurisdiction (state or country) matches the state or country of the postal address.
- Fictional values: telephone numbers use +999 (not assigned to a country by ITU, own knowledge); e-mail and web domains use `.example` (reserved, RFC 2606).
- Brackenmere's GLN 9523710900008 has a valid check digit (check_ids.py) and uses GS1 prefix 952, which GS1 reserves for demonstrations (own knowledge).
- Valdara Industries is the one foreign participant (address in Urvania, `ReceivedForeignTenderQuantity` 1); its register identifier, legal-entity CompanyID and endpoint agree (XU-R-104274); ISIN XU0001042501 has a valid check digit (check_ids.py); market code XFER is not in the ISO 10383 MIC source in `world/codelists/sources/iso10383/`.

## Considered and refuted
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 "General public administration activities" for a public works department was suspected to be too general — refuted: the department is part of the city's general administration, and no ISIC class fits a municipal works department better.
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: the address department "Procurement office" against the contact department "Procurement" — refuted: the same unit, once as the addressee on mail and once as the contact's department.
- `/ContractAwardNotice/cac:ReceiverParty/cac:PostalAddress/cbc:PostalZone`: two postal zones (38517, 38520) for buildings on the same square (Civic Square) — refuted: postal codes for individual large addressees on one square are usual, and both are in the same city subdivision and state.
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: "Via delle Officine" tagged `en-XB` was suspected to be an Italian, not an English rendering — refuted because the examples consistently give Urvanian places their Italianate exonyms in the English renderings (the city as "Ferrano" beside `qau` "Ruldraz"), as English texts keep foreign street names; the tag names the variant used in Bayvarra, and both renderings name the same street.
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount`: an amount where the definition says "The number of shares in the capital stock" — refuted as a finding of this example: the element's data type is Amount, so the UBL definition itself is inconsistent; reading it as the share capital is the only reading the type allows (the element's presence here is part of the master-data finding).
- `/ContractAwardNotice/cac:TenderingProcess/cac:EconomicOperatorShortList/cac:PreSelectedParty/cac:PartyName/cbc:Name`: `PreSelectedParty` is defined for a negotiated procedure — refuted: the follow-up service contract is negotiated with the first-prize winner without a new call, which is a negotiated procedure, and the short list here names the party invited to it.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties (tender, utilities, furniture, mast and the goods flows); they belong to those examples' reviews.
