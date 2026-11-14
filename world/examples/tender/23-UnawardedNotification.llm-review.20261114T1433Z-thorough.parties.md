# LLM review: 23-UnawardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: parties

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/23-UnawardedNotification.xml`, Git blob `39a6b648377d44e8a82177e1c91a57309cca5cc5` (committed)
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

### tender/23#F1 · Medium · Language code in `LocaleCode`
- XPath: `/UnawardedNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnawardedNotification/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is the language code again, the same value and list as `cac:Language/cbc:ID` next to it; it names no locale. The Urvanian parties of the flow (`cac:Language/cbc:ID` = `qau`) carry no `LocaleCode` at all, and where the examples do distinguish locales they write them as `en-XB` and `en-XU` (in `languageID`). 213 of the example files contain `cbc:LocaleCode` (`grep -l "cbc:LocaleCode" world/examples/*/*.xml`).
- Condition: No `LocaleCode` holds a bare language code: each one present names a locale (a language as used in a country or region), from a list of locales.
- Options: Remove `LocaleCode` where the language ID already says everything (preferred: it adds nothing here and the Urvanian parties do without it); or give the locale (for these parties `en-XB`) with a list that defines locales.
- Needs decision: no

### tender/23#F2 · Low · Party tax exemption reason worded as a transaction
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: UBL defines `PartyTaxScheme/ExemptionReasonCode` and `ExemptionReason` as "A reason for the party's exemption from tax". The code `PUBLIC` comes from the list of transaction exemption reasons (`…:XB:codelist:TaxExemptionReasonCode`, "Sale to a public body") and the text begins "Sale to a public body": both describe a kind of sale, not the status of the party. The second half of the text ("public bodies are exempt from the state sales tax") is the party's own status and is what the element is for.
- Condition: The party-level exemption reason states the party's status (it is a public body, exempt from the state sales tax), in code and text, and does not describe a transaction.
- Options: Reword the text to the status and use a code that names the status (preferred); or keep the code and only reword the text, if the list is meant to serve both the party and the transaction.
- Needs decision: no

### tender/23#F3 · Low · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The parties concerned are public bodies (a municipal department, a publication service, a review board, a customs administration; `IndustryClassificationCode` 8411 or 8423). Their `PartyLegalEntity` nevertheless carries `CompanyLiquidationStatusCode` = `ACTIVE` ("A code signifying the party's liquidation status": a public body cannot be wound up like a company, so the status says nothing) and a `CorporateRegistrationScheme` typed `COMMERCIAL` (Commercial register). A general business register may well list public bodies, so the register number itself is not questioned; the type "commercial register" and the liquidation status are what do not fit the kind of party. The companies of the flow carry legal form, size and registration date here; the public bodies carry none of these, only the two values that do not apply.
- Condition: A public body carries no liquidation status, and the registration scheme it is listed in is not typed as a commercial register (or is typed as what it is for that body).
- Options: Drop `CompanyLiquidationStatusCode` for public bodies and type the register neutrally for them (preferred); or drop the `CorporateRegistrationScheme` for public bodies and keep only the register number as `CompanyID`.
- Needs decision: no

### tender/23#F4 · Low · Registration date 1996-01-01 looks like a default, not a fact of the party
- XPath: `/UnawardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `RegistrationDate` as "The registration date of the CompanyID." Here it is `1996-01-01` for Brackenmere Furniture Ltd. The same date is the registration date of 25 different companies in three countries across the examples (271 occurrences in 181 files; counted by script over `cac:PartyLegalEntity` in `world/examples/*/*.xml`, distinct `RegistrationName`), among them four of this flow (Brackenmere Furniture Ltd, Marrowdale Sawmill Ltd, Castrano Logistics SRU, Trasvia Haulage SRU). 25 unrelated companies registered on the same New Year's Day is not plausible; the value reads as a filler, which the repository rules exclude ("No fillers": a value must have a real business reason in the world).
- Condition: Each company's `RegistrationDate` is its own date of registration, or the element is absent where the world has no such fact.
- Options: Give each of these companies a registration date of its own, consistent with its history (preferred); or leave `RegistrationDate` out for companies without one.
- Needs decision: no

### tender/23#F5 · Low · Appeal receiver without address or any means of contact
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealInformationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- Why: The appeal terms give the addressee of this decision ten days to appeal (`/UnawardedNotification/cac:AppealTerms/cbc:Description` = `An appeal against the decision goes to the review board within ten days.`). The party to appeal to is identified by register number and name only. The notices of the flow describe the same board in full, so the data exists: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PostalAddress/cbc:StreetName` = `Justice Row`, `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:ElectronicMail` = `registry@review-xb.example`. A recipient who has only this document cannot lodge the appeal from it. Rated Low because the board can be looked up by its register number.
- Condition: The party that receives the appeal can be reached from this document: it carries at least a postal or electronic address, as in the notices.
- Options: Describe `AppealReceiverParty` in full here as in the contract notice and the award notice (preferred); or give it at least its `ElectronicAddress` and contact.
- Needs decision: no

### tender/23#F6 · Low · The body that receives and decides the appeal is also named as its mediator
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:MediationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- Why: UBL defines `MediationParty` as "The Party who mediates any appeal" and `AppealReceiverParty` as "The Party who receives the appeal". Both are the Procurement Review Board of Bayvarra, and the terms say the appeal "goes to the review board" (`/UnawardedNotification/cac:AppealTerms/cbc:Description` = `An appeal against the decision goes to the review board within ten days.`). Mediation is by its nature done by someone other than the body that rules on the dispute; a board that both mediates and decides is possible in a fictional legal order, but nothing in the flow says that the board offers mediation, and the element looks filled because the role exists. The same three-fold use of the board is in 02-ContractNotice.xml (`AppealInformationParty`, `AppealReceiverParty`, `MediationParty`).
- Condition: A mediation party is named only if the procedure has mediation, and it is the body that actually mediates.
- Options: Remove `MediationParty` (preferred, unless the world's procurement law gives the board a mediation stage); or name the mediating body and say in the appeal terms that mediation precedes the appeal.
- Needs decision: yes

## Checked and consistent
- Lumeport Public Works Department: `PartyIdentification` `20410548` (scheme `…:XB:register`) is the same in all 36 examples of the flow that carry the party; its 36 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Brackenmere Furniture: `PartyIdentification` `20412466` (scheme `…:XB:register`) is the same in all 9 examples of the flow that carry the party; its 8 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Valdara Industries: `PartyIdentification` `XU-R-104274` (scheme `…:XU:register`) is the same in all 23 examples of the flow that carry the party; its 22 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Procurement Review Board of Bayvarra: `PartyIdentification` `20410822` (scheme `…:XB:register`) is the same in all 7 examples of the flow that carry the party; its 3 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- For every party described in full: `PartyLegalEntity/CompanyID` equals `PartyIdentification/ID`, the `ElectronicAddressID` is the country prefix plus that number, and `PartyTaxScheme/RegistrationName` equals `PartyLegalEntity/RegistrationName` (checked by script).
- For every party described in full, `RegistrationAddress/CityName` and country agree with the `PostalAddress`, and the tax scheme fits the country (state sales tax `STT` in lume for the Bayvarran parties, with the state as jurisdiction; `VAT` in ferra for the Urvanian ones).
- Signature: the signatory (Lumeport Public Works Department) is the party that issues the document according to its ID prefix and sender role.
- `ReceiverParty` is Brackenmere Furniture, the tenderer whose tender (19) ranked second; `WinningParty` is Valdara Industries by number and name, the same party as in the awarded notification (22) and the award notice (21).
- `check_ids.py`: GLN 9523710900008 check digit correct.

## Considered and refuted
- `/UnawardedNotification/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset` (all 2 `TimezoneOffset` elements of the example have `-1`): suspected a malformed offset (ISO 8601 would write `-01:00`) — refuted because UBL defines the element as text ("as an offset from Universal Coordinated Time"), `-1` is an unambiguous offset, and every address of the flow uses the same form.
- `/UnawardedNotification/cac:SenderParty/cac:Contact/cbc:Telephone` = `+999 2 38 2648 0548` (and the other telephone numbers): suspected a real country code — refuted because +999 is not assigned to any country in the ITU numbering plan (my knowledge of ITU-T E.164).
- `/UnawardedNotification/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `9523710900008`: suspected a real GLN — refuted because the GS1 prefix 952 is reserved for demonstrations and examples (my knowledge of the GS1 prefix list); check digit correct (`check_ids.py`).
- `/UnawardedNotification/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyName/cbc:Name`: suspected that naming the winner to the loser is a disclosure the document should not make — refuted because an unawarded notification exists to tell the tenderer who won and why, and the award notice (21) publishes the same.
