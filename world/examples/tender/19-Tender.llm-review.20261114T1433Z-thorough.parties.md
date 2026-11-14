# LLM review: 19-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: parties

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/19-Tender.xml`, Git blob `21feca31f7c744f8e198c18ed5445abb1d1142ee` (committed)
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

### tender/19#F1 · High · The tender refers to the qualification and reference documents of the competing tenderer
- XPath: `/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`
- XPath: `/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`
- Why: UBL defines `TendererQualificationDocumentReference` as "A reference to the tenderer qualification document that has been used to qualify the tenderer." The tenderer here is Brackenmere Furniture (`/Tender/cac:TendererParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`), but `VI-DOC-26-0199` is the tenderer qualification of Valdara Industries: `13-TendererQualification.xml:/TendererQualification/cbc:ID` = `VI-DOC-26-0199`, `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`, `13-TendererQualification.xml:/TendererQualification/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`. Valdara's own tender refers to the same document (`15-Tender.xml:/Tender/cac:TendererQualificationDocumentReference/cbc:ID` = `VI-DOC-26-0199`), correctly. `EvidenceDocumentReference` ("A reference to a non-structured evidentiary document supporting this tendered project") is `VI-REF-2025`, an identifier with Valdara's prefix that Valdara's tender also uses (`15-Tender.xml:/Tender/cac:TenderedProject/cac:EvidenceDocumentReference/cbc:ID` = `VI-REF-2025`); no example of the flow has that ID. Brackenmere's own qualification document in the flow is `07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`. A tender that qualifies its tenderer with a competitor's documents contradicts the referenced example.
- Condition: Every qualification and evidence document the tender refers to is a document of, or about, the tenderer that submits it; a reference that resolves to an example of the flow resolves to one whose qualifying party is Brackenmere Furniture.
- Options: Refer to Brackenmere's own documents: its qualification application response `BF-DOC-26-0193` for the qualification and a reference list of its own (a `BF-…` identifier) as evidence (preferred); or leave both references out, since the withdrawn tender this one replaces is not better documented. The same two references are in 17-Tender.xml.
- Needs decision: no

### tender/19#F2 · Medium · Language code in `LocaleCode`
- XPath: `/Tender/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is the language code again, the same value and list as `cac:Language/cbc:ID` next to it; it names no locale. The Urvanian parties of the flow (`cac:Language/cbc:ID` = `qau`) carry no `LocaleCode` at all, and where the examples do distinguish locales they write them as `en-XB` and `en-XU` (in `languageID`). 213 of the example files contain `cbc:LocaleCode` (`grep -l "cbc:LocaleCode" world/examples/*/*.xml`).
- Condition: No `LocaleCode` holds a bare language code: each one present names a locale (a language as used in a country or region), from a list of locales.
- Options: Remove `LocaleCode` where the language ID already says everything (preferred: it adds nothing here and the Urvanian parties do without it); or give the locale (for these parties `en-XB`) with a list that defines locales.
- Needs decision: no

### tender/19#F3 · Low · Registration date 1996-01-01 looks like a default, not a fact of the party
- XPath: `/Tender/cac:TendererParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `RegistrationDate` as "The registration date of the CompanyID." Here it is `1996-01-01` for Brackenmere Furniture Ltd. The same date is the registration date of 25 different companies in three countries across the examples (271 occurrences in 181 files; counted by script over `cac:PartyLegalEntity` in `world/examples/*/*.xml`, distinct `RegistrationName`), among them four of this flow (Brackenmere Furniture Ltd, Marrowdale Sawmill Ltd, Castrano Logistics SRU, Trasvia Haulage SRU). 25 unrelated companies registered on the same New Year's Day is not plausible; the value reads as a filler, which the repository rules exclude ("No fillers": a value must have a real business reason in the world).
- Condition: Each company's `RegistrationDate` is its own date of registration, or the element is absent where the world has no such fact.
- Options: Give each of these companies a registration date of its own, consistent with its history (preferred); or leave `RegistrationDate` out for companies without one.
- Needs decision: no

### tender/19#F4 · Low · Party tax exemption reason worded as a transaction
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: UBL defines `PartyTaxScheme/ExemptionReasonCode` and `ExemptionReason` as "A reason for the party's exemption from tax". The code `PUBLIC` comes from the list of transaction exemption reasons (`…:XB:codelist:TaxExemptionReasonCode`, "Sale to a public body") and the text begins "Sale to a public body": both describe a kind of sale, not the status of the party. The second half of the text ("public bodies are exempt from the state sales tax") is the party's own status and is what the element is for.
- Condition: The party-level exemption reason states the party's status (it is a public body, exempt from the state sales tax), in code and text, and does not describe a transaction.
- Options: Reword the text to the status and use a code that names the status (preferred); or keep the code and only reword the text, if the list is meant to serve both the party and the transaction.
- Needs decision: no

### tender/19#F5 · Low · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Tender/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The parties concerned are public bodies (a municipal department, a publication service, a review board, a customs administration; `IndustryClassificationCode` 8411 or 8423). Their `PartyLegalEntity` nevertheless carries `CompanyLiquidationStatusCode` = `ACTIVE` ("A code signifying the party's liquidation status": a public body cannot be wound up like a company, so the status says nothing) and a `CorporateRegistrationScheme` typed `COMMERCIAL` (Commercial register). A general business register may well list public bodies, so the register number itself is not questioned; the type "commercial register" and the liquidation status are what do not fit the kind of party. The companies of the flow carry legal form, size and registration date here; the public bodies carry none of these, only the two values that do not apply.
- Condition: A public body carries no liquidation status, and the registration scheme it is listed in is not typed as a commercial register (or is typed as what it is for that body).
- Options: Drop `CompanyLiquidationStatusCode` for public bodies and type the register neutrally for them (preferred); or drop the `CorporateRegistrationScheme` for public bodies and keep only the register number as `CompanyID`.
- Needs decision: no

## Checked and consistent
- Brackenmere Furniture: `PartyIdentification` `20412466` (scheme `…:XB:register`) is the same in all 9 examples of the flow that carry the party; its 8 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- Lumeport Public Works Department: `PartyIdentification` `20410548` (scheme `…:XB:register`) is the same in all 36 examples of the flow that carry the party; its 36 full descriptions in the flow are identical apart from language tags and the rendering of the legal form (compared by script, ignoring `languageID` and `CompanyLegalForm`).
- For every party described in full: `PartyLegalEntity/CompanyID` equals `PartyIdentification/ID`, the `ElectronicAddressID` is the country prefix plus that number, and `PartyTaxScheme/RegistrationName` equals `PartyLegalEntity/RegistrationName` (checked by script).
- For every party described in full, `RegistrationAddress/CityName` and country agree with the `PostalAddress`, and the tax scheme fits the country (state sales tax `STT` in lume for the Bayvarran parties, with the state as jurisdiction; `VAT` in ferra for the Urvanian ones).
- Signature: the signatory (Brackenmere Furniture) is the party that issues the document according to its ID prefix and sender role.
- `TendererParty`, `Signature/SignatoryParty` and `TenderLine[1]/WarrantyParty` are all Brackenmere Furniture, the party that submits the tender and makes the bench it offers ("a bench of the furniture maker's own make"); the warranty party being the tenderer fits the note.
- Brackenmere Furniture: ISIC 3100 (Manufacture of furniture), private limited company, small enterprise, seat and postal address in Marrowdale, Upland State, tax registration with the state sales tax of Upland State: consistent with each other and with examples 06–09, 17, 18 and 23.
- Tenderer's contact "Trade sales" / "Customer service officer" / department "Sales": name, title and department agree, and a sales desk is a fitting contact for a tender.
- `ContractingParty` contact "Procurement office" / "Procurement officer" / department "Procurement" fits the contracting role; address `Department` and `MarkAttention` name the same office.
- `check_ids.py`: GLN 9523710900008 check digit correct.

## Considered and refuted
- `/Tender/cac:TendererParty/cac:PostalAddress/cbc:TimezoneOffset` (all 2 `TimezoneOffset` elements of the example have `-1`): suspected a malformed offset (ISO 8601 would write `-01:00`) — refuted because UBL defines the element as text ("as an offset from Universal Coordinated Time"), `-1` is an unambiguous offset, and every address of the flow uses the same form.
- `/Tender/cac:TendererParty/cac:Contact/cbc:Telephone` = `+999 2 7121 266 466` (and the other telephone numbers): suspected a real country code — refuted because +999 is not assigned to any country in the ITU numbering plan (my knowledge of ITU-T E.164).
- `/Tender/cac:TendererParty/cac:AdditionalPartyIdentification/cbc:ID` = `9523710900008`: suspected a real GLN — refuted because the GS1 prefix 952 is reserved for demonstrations and examples (my knowledge of the GS1 prefix list); check digit correct (`check_ids.py`).
- `/Tender/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` and `/Tender/cac:BeneficiaryParty/cac:PartyName/cbc:Name`: suspected fillers, since both repeat the contracting party with number and name only — refuted because UBL puts no "if different" condition on either role ("The party originating the Tender", "A Party for whom the associated transaction is ultimately intended"), the department that buys the benches is the body that needs and uses them, and examples 15 and 17 state the same.
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:WarrantyParty/cac:PartyName/cbc:Name`: suspected that a small furniture maker would not be the right party to give the warranty alone — refuted because it makes the bench itself and names no subcontractor.

## Outside this review
- 17-Tender.xml carries the same two references to Valdara's documents; that is a matter for the review of example 17.
