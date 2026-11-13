# LLM review: 08-ContractNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/08-ContractNotice.xml`, Git blob `b31ec7709d9a9be65b496829edeb2df120890205` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
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

### contest/08#F1 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- Why: The example describes Lumeport Public Works Department, Bayvarra Information Service, Procurement Review Board of Bayvarra with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register: A register of businesses", world list CorporateRegistrationTypeCode) in the "Federal business register of Bayvarra", and with `CompanyLiquidationStatusCode` `ACTIVE` ("A code signifying the party's liquidation status"; code: "Active, not in liquidation"). These are public bodies (a city department, a federal information service, a review board): they are not businesses, are not entered in a register of businesses and are not wound up by liquidation (section 5, "a public body or a department is not a company in a commercial register and has no liquidation status"). A department of a city is moreover not a legal person; the legal entity behind the Public Works Department is the City of Lumeport. The same example calls the department "a department of the city of Lumeport" in its contracting party type, so the legal-entity data contradicts the party type next to it. The world list has no register type for public bodies (its codes are COMMERCIAL, CHARITY, ASSOCIATION, FARM). The same description is carried by every occurrence of these parties in the world (Lumeport Public Works Department 55, Bayvarra Information Service 12, Procurement Review Board of Bayvarra 7 party aggregates, counted by party name over `world/examples/*/*.xml`).
- Condition: No public body in the example carries a `CompanyLiquidationStatusCode` or a corporate registration scheme of the type "Commercial register"; the legal entity given for the Public Works Department is either the body with legal personality (the City of Lumeport) or explicitly a department of it.
- Options: (preferred) leave out `CompanyLiquidationStatusCode` and `CorporateRegistrationScheme` for public bodies and keep only the registration name and identifier, because the story needs no register type for them; or add a register type for public bodies to the world list, if the federal register really lists them; or give the City of Lumeport as the department's legal entity.
- Needs decision: yes

### contest/08#F2 · Medium · Language code in LocaleCode
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". A locale is a language together with the region or country it is used in (e.g. English as used in Bayvarra); the value `en` with `listID` `ISO 639` is the ISO 639 language code itself and repeats `Language/cbc:ID` of the same aggregate, so the element carries the language instead of a locale (section 6 names "a language code in `LocaleCode`" as Medium). The same value occurs 362 times in 213 examples (`grep -o '<cbc:LocaleCode listID="ISO 639">en'` over `world/examples/*/*.xml`).
- Condition: Every `Language/LocaleCode` in the example is either absent or holds a locale (language and country or region) from a list of locales, with that list as `listID`.
- Options: (preferred) leave out `LocaleCode`, because nothing in the example depends on a locale and `cbc:ID` already gives the language; or give a real locale (for instance the `en-XB` form the examples use for `languageID`) from a stated list.
- Needs decision: no

### contest/08#F3 · Low · Party tax exemption of the contracting authority stated as a sale
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReasonCode` and `ExemptionReason` are "A reason for the party's exemption from tax", i.e. the party's own status. The code `PUBLIC` comes from the Bayvarran list of exemption reasons for supplies (its other codes are export, drinking water, resale, levy, basic food, medicine) and is named "Sale to a public body", and the text begins "Sale to a public body": both describe a transaction, not the department's status. The second half of the text ("public bodies are exempt from the state sales tax") is the status the element asks for. Nothing in this document is sold, so the transaction wording has nothing to refer to here.
- Condition: The party's exemption reason in the example states the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) word the text as the status only ("Public body: exempt from the state sales tax") and keep the code, whose list definition ("A body of the federation, a state or a city buys free of sales tax") does describe the status; or add a status code for public bodies to the list.
- Needs decision: no

### contest/08#F4 · Low · Party master data the document does nothing with
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Section 4.8: data copied from a party's master data into a document that does not use it. The Public Works Department's customs trader identifier (scheme `urn:ubl-examples:world:XB:customs-trader`) is relevant to customs declarations, not to a design contest; no part of this procurement document involves customs. The same customs identifier is in all 55 aggregates of the department (counted by party name over `world/examples/*/*.xml`).
- Condition: The parties in the example carry only identifiers and legal data that this document or its procedure uses.
- Options: (preferred) leave these elements out of the procurement documents; keep them where the documents use them (customs, goods flows).
- Needs decision: no

### contest/08#F5 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: Section 5: the contact must fit the role the party has in this document. In this example the review board's registry, which receives appeals, is staffed by a "Procurement officer" of a "Procurement" department; a review board does not procure, and the person it names as the receiver of appeals should be a registry or appeals clerk. The contacts are the parties' general contacts from the goods flows, the same in every example of the world that carries these parties.
- Condition: Each contact in the example is one that handles the party's part in the contest (tendering or bids for participants, the registry or appeals for the review board), with job title and department that agree with it.
- Options: (preferred) give these parties a tendering or registry contact for the procurement documents; or leave the contact out where the document does not need one.
- Needs decision: no

## Checked and consistent
- Every party is described identically in every example of the flow that carries it (all leaf values compared per party name across the 16 examples; the pre-selected party in 15/16 is a subset of Brackenmere's data).
- For every party, `PartyIdentification/ID`, `PartyLegalEntity/CompanyID` and the suffix of `ElectronicAddressID` agree, and the tax scheme's jurisdiction (state or country) matches the state or country of the postal address.
- Fictional values: telephone numbers use +999 (not assigned to a country by ITU, own knowledge); e-mail and web domains use `.example` (reserved, RFC 2606).

## Considered and refuted
- `/ContractNotice/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 "General public administration activities" for a public works department was suspected to be too general — refuted: the department is part of the city's general administration, and no ISIC class fits a municipal works department better.
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: the address department "Procurement office" against the contact department "Procurement" — refuted: the same unit, once as the addressee on mail and once as the contact's department.
- `/ContractNotice/cac:ReceiverParty/cac:PostalAddress/cbc:PostalZone`: two postal zones (38517, 38520) for buildings on the same square (Civic Square) — refuted: postal codes for individual large addressees on one square are usual, and both are in the same city subdivision and state.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties (tender, utilities, furniture, mast and the goods flows); they belong to those examples' reviews.
