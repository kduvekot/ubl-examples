# LLM review: 13-TendererQualification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/13-TendererQualification.xml`, Git blob `fbf9d6ddac8eb891f81b7a2f593f1db23d28b8d1` (committed)
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

## Findings

### tender/13#F1 · High · Valdara Industries is a large enterprise, but declares 180 employees
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- Why: EntitySizeCode `LARGE` means "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (50,000,000.00 XBL) in the world's list (`world/codelists/lists.json`, EntitySizeCode). In its tenderer qualification (13) Valdara declares 180 employees ("The number of people employed by this qualifying party") and a financial capability of 9 200 000.00 lume; 12 gives a production value of 4 800 000.00 lume. No figure in the flow supports a turnover above 50 million lume, so by the figures it gives the company is medium-sized.
- Condition: Size class, number of employees and the financial figures of Valdara Industries agree.
- Options: (a) at least 250 employees in 13 (preferred: a listed company with a share capital of 250 million ferra and its own foundry is plausibly large); (b) size `MEDIUM` wherever the party is described.
- Needs decision: no

### tender/13#F2 · Medium · One reference supply where the notice requires three
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Benches for Ferrano's parks.`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Three similar supplies in five years.`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `3`
- Why: The document is "A document declaring the qualifications of a tenderer". The notice and the call for tenders require three similar supplies in five years (threshold quantity 3), with references as evidence. The qualification declares one completed task (benches for the parks of Ferrano, 2023 to 2025) with one piece of evidence. Nor does it address the environmental requirement (certified timber, forestry certificate). On what it declares, the tenderer does not meet the technical criterion it is later admitted on.
- Condition: The qualification declares what the notice requires (three reference supplies within five years, the timber certificate), or the notice requires what is declared.
- Options: (a) two more completed tasks and the forestry certificate as evidence (preferred); (b) lower the requirement in 01 to 03.
- Needs decision: yes

### tender/13#F3 · Medium · A consortium lead without a consortium, and a subcontractor as additional qualifying party
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads.`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:TendererRoleCode` = `SUBCONTRACTOR`
- XPath: `/TendererQualification/cbc:Note[2]` = `The manufacturer with Saltmere as subcontractor for the installation.`
- Why: AdditionalQualifyingParty is "The qualifications of a tenderer party other than the main tenderer party when bidding as a consortium." Valdara tenders alone with a subcontractor (its note, and SubcontractorParty in 15); a subcontractor is not a member of a consortium, and a tenderer with a subcontractor is not a "Consortium lead" (the meaning of `LEAD` in both lists). The role description "Leads." explains nothing. The roles as coded describe a consortium of two, the note and the tender a sole tenderer.
- Condition: The roles describe the arrangement the note and the tender state: a sole tenderer (or main contractor) and its subcontractor.
- Options: (a) a role for a sole tenderer or main contractor instead of `LEAD`, and the subcontractor only where the model provides for subcontractors (preferred); (b) make it a consortium in 13 and 15.
- Needs decision: yes

### tender/13#F4 · Medium · The classification and the register number in elements for evidence identifiers
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessClassificationEvidenceID` = `ISIC-3100`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `XU-R-104274`
- Why: BusinessClassificationEvidenceID is "An identifier for an item of evidence to support the classification of this qualifying party", BusinessIdentityEvidenceID "An identifier for an item of evidence to support the business identity". `ISIC-3100` is the classification itself (also given in BusinessClassificationScheme), and `XU-R-104274` is the party's register number (its PartyIdentification), not identifiers of evidence documents such as a register extract. The document's Evidence list has no item with these IDs.
- Condition: Each of the two elements identifies an item of evidence (and that evidence is listed or referenced), or is absent.
- Options: (a) refer to evidence items, e.g. the register extract of the commercial register, listed under `cac:Evidence` (preferred); (b) remove both.
- Needs decision: no

### tender/13#F5 · Medium · A province in Region
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division of the country, for which CountrySubentity exists ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the flow do use CountrySubentity for their state. The same value is in 22 of the 36 examples of the flow (grep for `Province of Ferrano` over the `*.xml` of the flow, files counted).
- Condition: The province is in CountrySubentity (with its code where the country has one); Region is used only for a region that is not an administrative division.
- Options: (a) move the province to CountrySubentity (preferred); (b) none other seen.
- Needs decision: no

### tender/13#F6 · Medium · Language code in LocaleCode
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/13#F7 · Low · 4 000 benches a year here, a capability of 6 000 in the register extract
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:Description` = `4,000 benches a year.`
- XPath: `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`
- Why: Valdara declares a technical capability of 4 000 benches a year; the register extract 12, issued two days later for the evaluation of this tender, states a production capability of 6 000 (steel frame benches, valid to 2026-12-31). The extract does not say "per year", so the two may measure different things, but an evaluator comparing them sees two figures for the same plant.
- Condition: The two documents give the same production capability, or say what each figure measures.
- Options: (a) the same figure in both (preferred); (b) describe the 6 000 in 12 (e.g. installed capacity) so that it differs on purpose.
- Needs decision: no

### tender/13#F8 · Low · 41 years in operation, registered 63 years ago
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:OperatingYearsQuantity` = `41`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`
- Why: OperatingYearsQuantity is "The number of years that this qualifying party has been in operation." The company was registered on 1962-04-12, almost 64 years before this document; 41 years would mean operation since 1985, which nothing explains.
- Condition: Years in operation and registration date agree, or the difference is explained.
- Options: (a) 63 years (preferred); (b) a description saying since when benches are made, in the capability instead.
- Needs decision: no

### tender/13#F9 · Low · A financial capability of 9.2 million without saying what it measures
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ID` = `FC-1`
- Why: The capability has an amount but neither a type code nor a description; it may be the yearly turnover the notice asks for (at least 250 000), equity, or a credit line. The reader cannot check it against the criterion. (12 gives 4 800 000.00 as the value of the production capability.)
- Condition: The financial capability says what the amount is (type code or description) and for which period.
- Options: (a) add CapabilityTypeCode or Description "yearly turnover 2025" (preferred); (b) none other seen.
- Needs decision: no

### tender/13#F10 · Low · Evidence and document references that lead nowhere
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Declaration/cac:SuppliedEvidence/cbc:ID` = `EV-DEC-1`
- XPath: `/TendererQualification/cac:AdditionalDocumentReference/cbc:ID` = `VI-ESPD-26`
- XPath: `/TendererQualification/cac:Evidence/cbc:ID` = `EV-FER-PARKS`
- Why: The declaration "No conflict of interest" names the evidence `EV-DEC-1`, but the document's Evidence list contains only `EV-FER-PARKS`. The additional document `VI-ESPD-26` has an ID only; nothing says what it is (the same pattern as `BF-ESPD-26` in 07), and no such document exists in the flow.
- Condition: Every evidence ID used is in the Evidence list (or is a referenced document), and the additional document says what it is.
- Options: (a) add `EV-DEC-1` to the Evidence list and give `VI-ESPD-26` a document type, or drop it (preferred); (b) none other seen.
- Needs decision: no

### tender/13#F11 · Low · A 20 % share for the subcontractor whose work is 3.5 % of the tender
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `20`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `80`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: ParticipationPercent is "The extent to which this party is expected to participate in the tendering process, expressed as a percentage." Saltmere is the subcontractor "for the installation" (the note). In the tender 15, issued 21 minutes later, the installation is line 2 with 4 320.00 of 124 080.00 lume, i.e. 3.5 %, not 20 %.
- Condition: The shares declared in the qualification agree with the split of the tender.
- Options: (a) about 3.5 % and 96.5 % (preferred); (b) say what else Saltmere does for 20 %.
- Needs decision: no

### tender/13#F12 · Low · Bids office of the subcontractor staffed by a procurement officer
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- Why: A bids office prepares offers to customers; "Procurement officer" in a department "Procurement" is someone who buys. Name, job title and department of the contact do not agree, and for a subcontractor taking part in a tender the selling side is the one that fits.
- Condition: Name, job title and department of the contact agree and fit the role.
- Options: (a) e.g. "Bid manager", department "Sales" or "Bids" (preferred); (b) drop job title and department.
- Needs decision: no

### tender/13#F13 · Low · The logistics service provider of the tenderer in its qualification
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: The qualifying party carries its logistics service provider (Castrano Logistics, warehousing and despatch, with a key account desk). The qualification declares capacity, references and declarations; it names Saltmere as the party it relies on, and does nothing with a warehouse operator. The data looks copied from master data.
- Condition: The party carries a service provider only where the document relies on it.
- Options: (a) remove the service provider here (preferred); (b) if Valdara relies on Castrano for the delivery, declare it as such in the qualification.
- Needs decision: no

### tender/13#F14 · Low · A public body described as a company in a commercial register
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/13#F15 · Low · The department's tax exemption reason describes a sale
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: ISIN `XU0001042501` has a correct check digit.
- Completed task: 180 000.00 a year × 3 years (2023-01-01 to 2025-12-31) = 540 000.00 = TotalTaskAmount; its evidence `EV-FER-PARKS` is in the Evidence list; the customer, the City of Ferrano, is the city of Valdara's seat.
- Participation 80 % + 20 % = 100 %; 20 % is within the 30 % the notice allows for subcontracting.
- 180 employees and 41 years are above the notice's minimum of 10 employees and 3 years; ISIC 3100 is the class required; both lots of interest exist.
- The qualification (2026-02-25 08:52) precedes Valdara's tender 15 (09:13 the same day), which refers to it by its ID `VI-DOC-26-0199`.
- Saltmere Engineering is described identically in 13 and 15 (hash of leaf values); ISIC 4290 fits a firm that anchors street furniture.

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: the English rendering is tagged `en-XU` here and `en-XB` in 03, 12, 14 and 16 — refuted because the tag follows the author of the document (Valdara writes Urvanian English, the Bayvarran parties Bayvarran English); the text is the same.
- `/TendererQualification/cbc:Note[1]`: whether the Urvanian note says the same as the English one cannot be checked, the language being invented — refuted as a finding; nothing indicates a difference.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:PartyCapacityAmount`: equal to the total task amount — refuted because the party carried out the whole task itself, so its capacity for it is the total.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`: listing and share capital in a qualification — refuted because they bear on the financial standing the qualification declares.
