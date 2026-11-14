# LLM review: 22-AwardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: parties

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/22-AwardedNotification.xml`, Git blob `06273957bdbccc6b43bc0afefe91af957c32f85c` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/22#F1 · Medium · Language code in `LocaleCode`
- XPath: `/AwardedNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is the language code again, the same value and list as `cac:Language/cbc:ID` next to it; it names no locale. The Urvanian parties of the flow (`cac:Language/cbc:ID` = `qau`) carry no `LocaleCode` at all, and where the examples do distinguish locales they write them as `en-XB` and `en-XU` (in `languageID`). 213 of the example files contain `cbc:LocaleCode` (`grep -l "cbc:LocaleCode" world/examples/*/*.xml`).
- Condition: No `LocaleCode` holds a bare language code: each one present names a locale (a language as used in a country or region), from a list of locales.
- Options: Remove `LocaleCode` where the language ID already says everything (preferred: it adds nothing here and the Urvanian parties do without it); or give the locale (for these parties `en-XB`) with a list that defines locales.
- Needs decision: no

### tender/22#F2 · Medium · Province in `Region`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located." `Province of Ferrano` is an administrative division of Urvania, which is what `CountrySubentity` is for ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same examples put their state in `CountrySubentity` (`Coastal State`, `Upland State`). 111 of the example files contain `cbc:Region` (`grep -l "<cbc:Region>" world/examples/*/*.xml`).
- Condition: A province of Urvania is given in `CountrySubentity` (with `CountrySubentityCode` if the country has codes for its provinces); `Region` is absent or holds a region in the sense of the definition.
- Options: Move the value to `CountrySubentity` (preferred: it is the element UBL defines for provinces and the one the Bayvarran addresses use); or, if Urvania's address format really has no administrative level and "Province of Ferrano" is a postal region only, say so and keep it, which needs the world's address rules.
- Needs decision: no

### tender/22#F3 · Low · Party tax exemption reason worded as a transaction
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: UBL defines `PartyTaxScheme/ExemptionReasonCode` and `ExemptionReason` as "A reason for the party's exemption from tax". The code `PUBLIC` comes from the list of transaction exemption reasons (`…:XB:codelist:TaxExemptionReasonCode`, "Sale to a public body") and the text begins "Sale to a public body": both describe a kind of sale, not the status of the party. The second half of the text ("public bodies are exempt from the state sales tax") is the party's own status and is what the element is for.
- Condition: The party-level exemption reason states the party's status (it is a public body, exempt from the state sales tax), in code and text, and does not describe a transaction.
- Options: Reword the text to the status and use a code that names the status (preferred); or keep the code and only reword the text, if the list is meant to serve both the party and the transaction.
- Needs decision: no

### tender/22#F4 · Low · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/AwardedNotification/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The parties concerned are public bodies (a municipal department, a publication service, a review board, a customs administration; `IndustryClassificationCode` 8411 or 8423). Their `PartyLegalEntity` nevertheless carries `CompanyLiquidationStatusCode` = `ACTIVE` ("A code signifying the party's liquidation status": a public body cannot be wound up like a company, so the status says nothing) and a `CorporateRegistrationScheme` typed `COMMERCIAL` (Commercial register). A general business register may well list public bodies, so the register number itself is not questioned; the type "commercial register" and the liquidation status are what do not fit the kind of party. The companies of the flow carry legal form, size and registration date here; the public bodies carry none of these, only the two values that do not apply.
- Condition: A public body carries no liquidation status, and the registration scheme it is listed in is not typed as a commercial register (or is typed as what it is for that body).
- Options: Drop `CompanyLiquidationStatusCode` for public bodies and type the register neutrally for them (preferred); or drop the `CorporateRegistrationScheme` for public bodies and keep only the register number as `CompanyID`.
- Needs decision: no

### tender/22#F5 · Low · Same Urvanian party described with different language tags and legal-form renderings across the flow
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: The checklist asks that the same party is described the same way in every example and that each repeated rendering is in the language its `languageID` names. In this example the second rendering of the Urvanian street and city names is tagged `languageID="en-XB"` and `CompanyLegalForm` occurs once, without `languageID` and without the Urvanian text. In the examples issued from Urvania the same texts are tagged `en-XU` and the legal form is given twice, in Urvanian (`qau`) and in English (`en-XU`): `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine` (languageID `en-XU`), `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)` (languageID `qau`). The text is identical in both variants ("Via delle Officine", "Ferrano", "Piazza della Banca"), so one of the two tags cannot be a statement about the text; it follows the country of the document's issuer. The tag `en-XB` occurs in 13 examples of the flow and `en-XU` in 9 (`grep -c 'languageID="en-XB"' world/examples/tender/*.xml`, likewise `en-XU`). I could not settle whether this is intended (a rendering "as an English-language reader in the issuer's country writes it") or an inconsistency.
- Condition: The second rendering of a given address or legal form carries the same `languageID` in every example of the flow, or the rule by which it differs is one a reader can state from the XML; `CompanyLegalForm` is rendered in the same languages wherever the party is described in full.
- Options: Tag the English rendering of an Urvanian name by what it is (`en-XU`, the form used in Urvania) in every example (preferred: the tag then describes the text, not the document); or keep the issuer-dependent tag and apply it uniformly, including a tagged `CompanyLegalForm` in the Bayvarran-issued examples.
- Needs decision: yes

### tender/22#F6 · Low · Logistics service provider of the supplier carried in a document that does nothing with it
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/AwardedNotification/cac:ReceiverParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: Valdara Industries is described with a `ServiceProviderParty` ("A party providing a service to this party"): Castrano Logistics, warehousing and despatch, with a `SellerContact` ("The contact for the Service Provider") that has a name and no means of contact. This document is not about storing or despatching goods and refers to the service nowhere else; the block is in all 22 full descriptions of Valdara Industries in the flow, whatever the document (counted by script over `world/examples/tender/*.xml`). Section 4.8 of the review rules names "a service provider … the document does nothing with" as data copied from master data; the repository rule is that a value needs a business reason in the document that carries it.
- Condition: The supplier's logistics service provider appears only in documents whose purpose involves it (the despatch and the documents that follow the goods); where it appears, its contact can be reached.
- Options: Leave the `ServiceProviderParty` out of this document (preferred); or, if the world wants it wherever the supplier is described in full, give the contact a telephone or mail address so that it is usable.
- Needs decision: no

## Checked and consistent
- Lumeport Public Works Department: `PartyIdentification` `20410548` (scheme `…:XB:register`) is the same in all 36 examples of the flow that carry the party; its 36 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Valdara Industries: `PartyIdentification` `XU-R-104274` (scheme `…:XU:register`) is the same in all 23 examples of the flow that carry the party; its 22 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Castrano Logistics: `PartyIdentification` `XU-R-104411` (scheme `…:XU:register`) is the same in all 22 examples of the flow that carry the party.
- For every party described in full: `PartyLegalEntity/CompanyID` equals `PartyIdentification/ID`, the `ElectronicAddressID` is the country prefix plus that number, and `PartyTaxScheme/RegistrationName` equals `PartyLegalEntity/RegistrationName` (checked by script).
- For every party described in full, `RegistrationAddress/CityName` and country agree with the `PostalAddress`, and the tax scheme fits the country (state sales tax `STT` in lume for the Bayvarran parties, with the state as jurisdiction; `VAT` in ferra for the Urvanian ones).
- Signature: the signatory (Lumeport Public Works Department) is the party that issues the document according to its ID prefix and sender role.
- `SenderParty` (the awarding department, which signs) and `ReceiverParty` (Valdara Industries) fit an awarded notification; `TenderResult/WinningParty` is the receiver itself, by number and name, consistent with the note "Your tender has won both lots".
- `check_ids.py`: ISIN XU0001042501 check digit correct.

## Considered and refuted
- `/AwardedNotification/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset` (all 2 `TimezoneOffset` elements of the example have `-1`): suspected a malformed offset (ISO 8601 would write `-01:00`) — refuted because UBL defines the element as text ("as an offset from Universal Coordinated Time"), `-1` is an unambiguous offset, and every address of the flow uses the same form.
- `/AwardedNotification/cac:SenderParty/cac:Contact/cbc:Telephone` = `+999 2 38 2648 0548` (and the other telephone numbers): suspected a real country code — refuted because +999 is not assigned to any country in the ITU numbering plan (my knowledge of ITU-T E.164).
- `/AwardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`, with `CorporateStockAmount` and `FullyPaidSharesIndicator`: suspected master data the document does not use — refuted for this lens because they are part of the description of the party as a legal entity (a listed public limited company), not a separate service or certificate; the ISIN check digit is correct (`check_ids.py`) and the prefix `XU` is no ISO 3166 country and no ISIN prefix I know, so it cannot be a real security.
- `/AwardedNotification/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: suspected a real ISO 6523 ICD — refuted because 0990 is not an ICD I know to be allocated (my knowledge of the ICD list; the register was not consulted online), and the identifier is the same wherever the party occurs.
- `/AwardedNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`: suspected an unsuitable contact for an award — refuted because it is the contact Valdara gave as tenderer (examples 13 and 15).
