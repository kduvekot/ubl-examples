# LLM review: 30-ExportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: parties

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/30-ExportCustomsDeclaration.xml`, Git blob `badd401509d1f287a27ff308ccae49e844329ef6` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 1ae0e51 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

This part is the focused run **parties**: it looks only at the parties and their roles, identifiers,
legal entities, tax schemes, contacts, addresses and locations. Everything else is outside its lens.

## Findings

### tender/30#F1 · Medium · Province in `Region`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located." `Province of Ferrano` is an administrative division of Urvania, which is what `CountrySubentity` is for ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same examples put their state in `CountrySubentity` (`Coastal State`, `Upland State`). 111 of the example files contain `cbc:Region` (`grep -l "<cbc:Region>" world/examples/*/*.xml`).
- Condition: A province of Urvania is given in `CountrySubentity` (with `CountrySubentityCode` if the country has codes for its provinces); `Region` is absent or holds a region in the sense of the definition.
- Options: Move the value to `CountrySubentity` (preferred: it is the element UBL defines for provinces and the one the Bayvarran addresses use); or, if Urvania's address format really has no administrative level and "Province of Ferrano" is a postal region only, say so and keep it, which needs the world's address rules.
- Needs decision: no

### tender/30#F2 · Medium · Language code in `LocaleCode`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is the language code again, the same value and list as `cac:Language/cbc:ID` next to it; it names no locale. The Urvanian parties of the flow (`cac:Language/cbc:ID` = `qau`) carry no `LocaleCode` at all, and where the examples do distinguish locales they write them as `en-XB` and `en-XU` (in `languageID`). 213 of the example files contain `cbc:LocaleCode` (`grep -l "cbc:LocaleCode" world/examples/*/*.xml`).
- Condition: No `LocaleCode` holds a bare language code: each one present names a locale (a language as used in a country or region), from a list of locales.
- Options: Remove `LocaleCode` where the language ID already says everything (preferred: it adds nothing here and the Urvanian parties do without it); or give the locale (for these parties `en-XB`) with a list that defines locales.
- Needs decision: no

### tender/30#F3 · Low · Same Urvanian party described with different language tags and legal-form renderings across the flow
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: The checklist asks that the same party is described the same way in every example and that each repeated rendering is in the language its `languageID` names. In this example the second rendering of the Urvanian street and city names is tagged `languageID="en-XU"` and the legal form is given in Urvanian (`qau`) and in English (`en-XU`). In the examples issued from Bayvarra the same texts are tagged `en-XB` and the legal form is given once, without `languageID` and without the Urvanian text: `03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine` (languageID `en-XB`), `03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)` (no languageID). The text is identical in both variants ("Via delle Officine", "Ferrano", "Piazza della Banca"), so one of the two tags cannot be a statement about the text; it follows the country of the document's issuer. The tag `en-XB` occurs in 13 examples of the flow and `en-XU` in 9 (`grep -c 'languageID="en-XB"' world/examples/tender/*.xml`, likewise `en-XU`). I could not settle whether this is intended (a rendering "as an English-language reader in the issuer's country writes it") or an inconsistency.
- Condition: The second rendering of a given address or legal form carries the same `languageID` in every example of the flow, or the rule by which it differs is one a reader can state from the XML; `CompanyLegalForm` is rendered in the same languages wherever the party is described in full.
- Options: Tag the English rendering of an Urvanian name by what it is (`en-XU`, the form used in Urvania) in every example (preferred: the tag then describes the text, not the document); or keep the issuer-dependent tag and apply it uniformly, including a tagged `CompanyLegalForm` in the Bayvarran-issued examples.
- Needs decision: yes

### tender/30#F4 · Low · Exporter's contact is the sales order desk
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's contact fits its role. The exporter ("The Party who exports the goods or has similar right of disposal over them at the time of export") declares the goods to customs and signs the declaration; the contact customs would turn to is the order desk of the sales department, a customer service officer, the same contact Valdara carries in the tender, the catalogue and the invoice. The goods are physically despatched by its warehouse company, which has a contact of its own in the despatch advice (`29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`).
- Condition: The exporter's contact in a customs declaration is one that deals with export formalities (or the contact is absent).
- Options: Give the exporter an export or shipping contact (preferred); or leave `Contact` out of the declaration.
- Needs decision: no

### tender/30#F5 · Low · Registration date 1996-01-01 looks like a default, not a fact of the party
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `RegistrationDate` as "The registration date of the CompanyID." Here it is `1996-01-01` for Trasvia Haulage SRU. The same date is the registration date of 25 different companies in three countries across the examples (271 occurrences in 181 files; counted by script over `cac:PartyLegalEntity` in `world/examples/*/*.xml`, distinct `RegistrationName`), among them four of this flow (Brackenmere Furniture Ltd, Marrowdale Sawmill Ltd, Castrano Logistics SRU, Trasvia Haulage SRU). 25 unrelated companies registered on the same New Year's Day is not plausible; the value reads as a filler, which the repository rules exclude ("No fillers": a value must have a real business reason in the world).
- Condition: Each company's `RegistrationDate` is its own date of registration, or the element is absent where the world has no such fact.
- Options: Give each of these companies a registration date of its own, consistent with its history (preferred); or leave `RegistrationDate` out for companies without one.
- Needs decision: no

### tender/30#F6 · Low · Party tax exemption reason worded as a transaction
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: UBL defines `PartyTaxScheme/ExemptionReasonCode` and `ExemptionReason` as "A reason for the party's exemption from tax". The code `PUBLIC` comes from the list of transaction exemption reasons (`…:XB:codelist:TaxExemptionReasonCode`, "Sale to a public body") and the text begins "Sale to a public body": both describe a kind of sale, not the status of the party. The second half of the text ("public bodies are exempt from the state sales tax") is the party's own status and is what the element is for.
- Condition: The party-level exemption reason states the party's status (it is a public body, exempt from the state sales tax), in code and text, and does not describe a transaction.
- Options: Reword the text to the status and use a code that names the status (preferred); or keep the code and only reword the text, if the list is meant to serve both the party and the transaction.
- Needs decision: no

### tender/30#F7 · Low · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The parties concerned are public bodies (a municipal department, a publication service, a review board, a customs administration; `IndustryClassificationCode` 8411 or 8423). Their `PartyLegalEntity` nevertheless carries `CompanyLiquidationStatusCode` = `ACTIVE` ("A code signifying the party's liquidation status": a public body cannot be wound up like a company, so the status says nothing) and a `CorporateRegistrationScheme` typed `COMMERCIAL` (Commercial register). A general business register may well list public bodies, so the register number itself is not questioned; the type "commercial register" and the liquidation status are what do not fit the kind of party. The companies of the flow carry legal form, size and registration date here; the public bodies carry none of these, only the two values that do not apply.
- Condition: A public body carries no liquidation status, and the registration scheme it is listed in is not typed as a commercial register (or is typed as what it is for that body).
- Options: Drop `CompanyLiquidationStatusCode` for public bodies and type the register neutrally for them (preferred); or drop the `CorporateRegistrationScheme` for public bodies and keep only the register number as `CompanyID`.
- Needs decision: no

## Checked and consistent
- Valdara Industries: `PartyIdentification` `XU-R-104274` (scheme `…:XU:register`) is the same in all 23 examples of the flow that carry the party; its 22 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Castrano Logistics: `PartyIdentification` `XU-R-104411` (scheme `…:XU:register`) is the same in all 22 examples of the flow that carry the party.
- Trasvia Haulage: `PartyIdentification` `XU-R-104822` (scheme `…:XU:register`) is the same in all 2 examples of the flow that carry the party; its 2 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Codana Identification Agency: `PartyIdentification` `XU-R-105644` (scheme `…:XU:register`) is the same in all 7 examples of the flow that carry the party.
- Lumeport Public Works Department: `PartyIdentification` `20410548` (scheme `…:XB:register`) is the same in all 36 examples of the flow that carry the party; its 36 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Customs Administration of Urvania: `PartyIdentification` `XU-R-105507` (scheme `…:XU:register`) is the same in all 1 examples of the flow that carry the party.
- For every party described in full: `PartyLegalEntity/CompanyID` equals `PartyIdentification/ID`, the `ElectronicAddressID` is the country prefix plus that number, and `PartyTaxScheme/RegistrationName` equals `PartyLegalEntity/RegistrationName` (checked by script).
- For every party described in full, `RegistrationAddress/CityName` and country agree with the `PostalAddress`, and the tax scheme fits the country (state sales tax `STT` in lume for the Bayvarran parties, with the state as jurisdiction; `VAT` in ferra for the Urvanian ones).
- Signature: the signatory (Valdara Industries) is the party that issues the document according to its ID prefix and sender role.
- `ExporterParty` and `CustomsDeclaration/ConsignorParty` are Valdara Industries (which signs; ID prefix VI), `ConsigneeParty` the department, `CarrierParty` Trasvia Haulage as in the despatch advice (29), `CustomsParty` the customs administration of the country of export: each is the right party for its role. The exporter carries its customs trader number `XU-TR-104274` and the consignee `XB-TR-410548`.
- Customs Administration of Urvania: postal address of type `POSTAL` with a post box and the street of the border crossing ("Valico di Confine"), contact "Border office" / "Public service officer" / "Public services" with telephone and fax: consistent with each other and with a border customs office; `ApplicableTerritoryAddress` XU is the territory of the declaring administration.
- `OriginCountry` XU agrees with the exporter's seat. `check_ids.py`: ISIN XU0001042501 check digit correct.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:TimezoneOffset` (all 4 `TimezoneOffset` elements of the example have `-1`): suspected a malformed offset (ISO 8601 would write `-01:00`) — refuted because UBL defines the element as text ("as an offset from Universal Coordinated Time"), `-1` is an unambiguous offset, and every address of the flow uses the same form.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274` (and the other telephone numbers): suspected a real country code — refuted because +999 is not assigned to any country in the ITU numbering plan (my knowledge of ITU-T E.164).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`, with `CorporateStockAmount` and `FullyPaidSharesIndicator`: suspected master data the document does not use — refuted for this lens because they are part of the description of the party as a legal entity (a listed public limited company), not a separate service or certificate; the ISIN check digit is correct (`check_ids.py`) and the prefix `XU` is no ISO 3166 country and no ISIN prefix I know, so it cannot be a real security.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: suspected a real ISO 6523 ICD — refuted because 0990 is not an ICD I know to be allocated (my knowledge of the ICD list; the register was not consulted online), and the identifier is the same wherever the party occurs.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`: suspected master data copied into the document (it is in almost every description of Valdara Industries in the flow) — refuted here because this document is about the despatch and movement of the goods, which is the service Castrano Logistics provides to the seller.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`: suspected too vague, a description instead of a named and coded customs office — refuted because the examples of the world name customs offices this way throughout (six examples use this very name; `grep -h -A3 "OfficeLocation>" world/examples/*/*.xml`), the XML shows no office code scheme, and the name does say which office it is.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`: suspected out of place for a customs authority — refuted because a public body can be registered for VAT, and the number is in the Urvanian tax scheme.
