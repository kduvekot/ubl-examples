# LLM review: 13-TendererQualification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/13-TendererQualification.xml`, Git blob `fbf9d6ddac8eb891f81b7a2f593f1db23d28b8d1` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/13#F1 · Medium · The ISIC class itself in the element for a classification evidence identifier
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessClassificationEvidenceID` = `ISIC-3100`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:BusinessClassificationScheme/cac:ClassificationCategory/cbc:CodeValue` = `3100`
- Why: `BusinessClassificationEvidenceID` is "An identifier for an item of evidence to support the classification of this qualifying party". `ISIC-3100` is the class itself, which `BusinessClassificationScheme` next to it already gives; it identifies no item of evidence (a register extract, a certificate), and neither the document's `Evidence` list nor any other example has such an item (the string occurs only here). All four parts agree.
- Condition: The element identifies an item of evidence that the document lists or references, or is absent.
- Options: (a) an `Evidence` for the register extract (the extract 12, `BIS-DOC-26-0198`, would do) and its ID here (preferred); (b) remove it; the classification scheme gives the class.
- Needs decision: no
- From: broad (F4, part), context (F2, part), logistics (F1), parties (F1, part)

### tender/13#F2 · Medium · A sole tenderer with a subcontractor coded as a consortium lead
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads.`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:TendererRoleCode` = `SUBCONTRACTOR`
- XPath: `/TendererQualification/cbc:Note[2]` = `The manufacturer with Saltmere as subcontractor for the installation.`
- XPath: `15-Tender.xml:/Tender/cac:SubcontractorParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: The note and the tender (15, where Saltmere is `SubcontractorParty`) say Valdara tenders alone with Saltmere as subcontractor. Valdara is nevertheless coded `LEAD` twice ("Consortium lead: Leads a group of economic operators (ESPD GROUP_LEAD)"), although the world's lists have `SOLE` ("Sole tenderer: Tenders alone (ESPD SCLE)"); "Leads." describes nothing. Saltmere sits in `AdditionalQualifyingParty`, "The qualifications of a tenderer party other than the main tenderer party when bidding as a consortium". The merge checked the role list: `SUBCONTRACTOR` is "A subcontractor whose capacities are relied on (ESPD OERON)", so the world means Saltmere as an entity relied on, which ESPD lists beside consortium members; UBL's definition, however, names only consortium members, and UBL offers no other place for a relied-on subcontractor in this document (parties). The `LEAD` code is wrong in any reading; the placement of Saltmere is a judgement on the definition, hence Needs decision yes. Logistics rated it Low; broad, context and parties Medium.
- Condition: The role codes say what the note and the tender say (Valdara `SOLE`), and the placement of the relied-on subcontractor is either justified as the only place UBL offers (recorded as a difference from the definition for the TC write-up) or the two form a consortium in 13 and 15.
- Options: (a) `SOLE` for Valdara, `EconomicOperatorRole` with a description that says so or none; keep Saltmere as `SUBCONTRACTOR` in `AdditionalQualifyingParty` and record the reading (preferred: it matches 15); (b) make Saltmere a consortium member (`MEMBER`) in 13 and 15, which changes the story (joint liability, no subcontract).
- Needs decision: yes
- From: broad (F3), context (F1), logistics (F4), parties (F2)

### tender/13#F3 · Medium · A financial capability of 9.2 million lume without saying what it is
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ID` = `FC-1`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- Why: The document's purpose is "declaring the qualifications of a tenderer" against the published criteria, of which the financial one is a yearly turnover above 250000.00 lume. The capability has neither a type code ("Turnover" is one of the examples the definition of `CapabilityTypeCode` gives) nor a description, period or evidence, unlike the technical capability beside it. 9200000.00 lume could be turnover, equity or a credit line, of any year; the buyer cannot evaluate the criterion from it. Medium (money, context): information the document's purpose depends on is missing; broad rated it Low.
- Condition: The financial capability says that it is the yearly turnover (or what else), for which year(s), and names its evidence.
- Options: (a) add a type code, a description such as "Turnover 2025" (or the three years), the period and the accounts as evidence (preferred); none seen without these.
- Needs decision: no
- From: money (F2), broad (F9), context (F4, part)

### tender/13#F4 · Medium · One reference supply where the notices require three, and no word on certified timber
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Benches for Ferrano's parks.`
- XPath: `/TendererQualification/cac:Evidence/cbc:Name` = `Ferrano reference`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Three similar supplies in five years.`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `3`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:SpecificTendererRequirement/cbc:Name` = `Certified timber`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:SpecificTendererRequirement/cac:SuggestedEvidence/cbc:Name` = `Forestry certificate`
- Why: The notices and the call for tenders require three similar supplies in five years (threshold 3) and certified timber with a forestry certificate. The qualification declares one completed task (benches for the parks of Ferrano, one three-year contract 2023–2025) with one piece of evidence, and nothing on the timber. Read as one supply, it does not meet the technical criterion; if the three years count as three supplies, the document does not say so. Yet the flow qualifies and awards Valdara (20, 22). Years in operation (41 ≥ 3) and staff (180 ≥ 10) are answered. Medium/no aligned with the contest merges ("one completed task vs threshold 2: Medium no"): the threshold is stated and the document's purpose depends on it. Broad said yes, logistics rated it Low.
- Condition: The qualification declares, for each requirement of the notices, the fact and its evidence (three reference supplies within five years, the timber certificate), or shows how the one task counts as three supplies.
- Options: (a) two more completed tasks and the forestry certificate as evidence (preferred); (b) describe the Ferrano task as three yearly supply contracts; (c) lower the requirement in 01 to 03 (a story change).
- Needs decision: no
- From: broad (F2), context (F3), logistics (F5)

### tender/13#F5 · Medium · A province in Region
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran addresses of the flow put their state in `CountrySubentity`. Recounted: 219 occurrences in 104 of the 250 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`, `-l` for files).
- Condition: The province of an Urvanian address is in `CountrySubentity` (with a code if Urvania has a list); `Region` is absent or holds a region in the sense of the definition.
- Options: (a) move the value to `CountrySubentity` (preferred); a code is optional.
- Needs decision: no
- From: broad (F5), parties (F3)

### tender/13#F6 · Medium · Language code in LocaleCode
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale. Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales.
- Options: (a) remove `LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F6), context (F5), logistics (F2), parties (F4)

### tender/13#F7 · Medium · The contracting authority, a public body, described as a company in a commercial register with a liquidation status
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status" (`ACTIVE`: "Active, not in liquidation"); `COMMERCIAL` is "Commercial register: A register of businesses". Lumeport Public Works Department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411); it is not a business and cannot be in liquidation.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies, keeping register name and number (preferred); (b) a register type for public bodies; (c) record the convention in the world's rules.
- Needs decision: no
- From: broad (F14), parties (F12)

### tender/13#F8 · Low · Participation 80 % / 20 %, but the subcontractor's part is 3.5 % of the tender
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `80`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `20`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- Why: `ParticipationPercent` is "The extent to which this party is expected to participate in the tendering process, expressed as a percentage." Saltmere does the installation (note 2). In the tender issued 21 minutes later, the installation is line 2 with 4320.00 of 124080.00 lume (re-done: 4320 / 124080 = 3.48 %), and the award gives the subcontract rate as 3.5 (with the same 4320.00). No basis for 20 % is visible in the flow; the share matters because the terms limit subcontracting to 30 %. Low (broad, logistics; aligned with merger C, "Subcontractor share 20 % (13) vs 3.5 % of the tender: Low/no"): the definition does not fix the base of the percentage, so no strict contradiction; money rated it Medium.
- Condition: The participation percentages agree with the tender's split (about 96.5 and 3.5 by value), or the base of the split is stated.
- Options: (a) 96.5 and 3.5 (preferred); (b) keep 80/20 and state the base (e.g. working hours), with the award documents on the same base.
- Needs decision: no
- From: broad (F11), logistics (F6), money (F1)

### tender/13#F9 · Low · 41 years in operation, registered 63 years ago
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:OperatingYearsQuantity` = `41`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`
- XPath: `/TendererQualification/cbc:IssueDate` = `2026-02-25`
- Why: `OperatingYearsQuantity` is "The number of years that this qualifying party has been in operation." The legal entity in the same aggregate was registered on 1962-04-12, 63 full years before the issue date (re-done); 41 years would mean operation since 1985, which nothing explains. Not High: operation can start or restart later than registration (e.g. a dormant shell), so it is no strict contradiction.
- Condition: Years in operation and registration date tell one history, or the difference is explained.
- Options: (a) 63 years (preferred: the registration date is Valdara's in every example); (b) explain the 41 (e.g. years of bench production) in a description.
- Needs decision: no
- From: broad (F8), parties (F5)

### tender/13#F10 · Low · The register number in the element for a business identity evidence identifier
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `XU-R-104274`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- Why: For the argument (broad, context, parties): `BusinessIdentityEvidenceID` is "An identifier for an item of evidence to support the business identity of this qualifying party"; `XU-R-104274` is the party's register number (its `PartyIdentification`), not the identifier of a register extract or certificate. Against it (logistics): the register entry is the evidence of the business identity, and the `schemeID` says which register. Both readings are possible; aligned with the contest merges ("BusinessIdentityEvidenceID = register number: Low, yes; cannot settle"). The parts had this inside the Medium finding on the classification evidence (F1); the merge splits it off because only the classification line is beyond doubt.
- Condition: Either the element identifies an item of evidence (a register extract) that the document lists, or the world records that a register number is accepted as the identifier of the register entry as evidence.
- Options: (a) the ID of an `Evidence` for the register extract (preferred: one evidence item then serves F1 and this element); (b) keep the register number and record the reading.
- Needs decision: yes
- From: broad (F4, part), context (F2, part), parties (F1, part); refuted by logistics (carried)

### tender/13#F11 · Low · Capability figures that differ from the register extract sent to the same buyer
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:Description` = `4,000 benches a year.`
- XPath: `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`
- XPath: `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `4800000.00`
- Why: Valdara declares 4000 benches a year and a financial capability of 9200000.00 lume; the register extract 12, two days later and for the same evaluation, gives a production capability of 6000 pieces and 4800000.00 lume for "Steel frame benches…", without a period. If the quantities are both yearly bench output, 4000 and 6000 contradict each other; neither document says enough to tell. Logistics refuted it for this example (this document states its measure, "a year"; the unexplained figure is in 12); the merge keeps it as a finding of both examples because the evaluator receives both, but Low with a decision: no contradiction can be shown while 12's measure is unnamed, and which figures are Valdara's is a story fact. Same finding as 12 F15.
- Condition: Figures for the same measure agree between 12 and 13, or each says what it measures so that both can be true.
- Options: (a) one set of figures, each with its meaning and year, in both documents (preferred); (b) keep both and describe them (e.g. "6,000 pieces of street furniture, of which 4,000 benches").
- Needs decision: yes
- From: broad (F7), context (F4, part), money (F3), parties (F7); refuted by logistics for this example (carried)

### tender/13#F12 · Low · The party's capacity amount repeats the task's total
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:PartyCapacityAmount` = `540000.00`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:TotalTaskAmount` = `540000.00`
- Why: `PartyCapacityAmount` is "A monetary amount corresponding to the financial capacity of the party that carried out this completed task", `TotalTaskAmount` "The actual total monetary amount of this completed task". The party's capacity (what it could finance or turn over at the time) is not the value of the task; the same figure says nothing about the party, whose capacity this document puts at 9200000.00 lume. Broad refuted it (the party carried out the whole task itself, so its capacity for it is the total); the merge does not follow: that reading would be the party's share of the task, while the definition speaks of its financial capacity.
- Condition: `PartyCapacityAmount`, if present, states the party's financial capacity during the task, not the task's own amount.
- Options: (a) drop it; the financial capability already describes the party (preferred); (b) give the party's turnover in the years of the task.
- Needs decision: no
- From: context (F7), money (F4); refuted by broad (carried)

### tender/13#F13 · Low · Evidence and a document reference that lead nowhere
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Declaration/cac:SuppliedEvidence/cbc:ID` = `EV-DEC-1`
- XPath: `/TendererQualification/cac:Evidence/cbc:ID` = `EV-FER-PARKS`
- XPath: `/TendererQualification/cac:AdditionalDocumentReference/cbc:ID` = `VI-ESPD-26`
- XPath: `/TendererQualification/cbc:ID` = `VI-DOC-26-0199`
- Why: The completed task's evidence `EV-FER-PARKS` is defined under `Evidence` ("Ferrano reference"); the integrity declaration's `EV-DEC-1` is defined nowhere in the document or the flow (`grep -l EV-DEC-1` over the flow's XML finds only this file). The only document reference, `VI-ESPD-26`, has an ID only and resolves to no example; by its name it is a self-declaration, which is what this document itself is (`VI-DOC-26-0199`); the same pattern as `BF-ESPD-26` in 07. Context gave the reference a separate Low/yes finding (it could also be Valdara's qualification application response, an exchange missing from the flow); the merge folds it in with Needs decision no, as in 07 F6: the preferred fix (remove it, or type it) is encoding.
- Condition: Every `SuppliedEvidence/ID` has an `Evidence` with that ID (or a name where it is used), and every generic document reference states the kind of document and resolves, or is absent.
- Options: (a) add an `Evidence` for `EV-DEC-1` (the signed declaration) and remove `VI-ESPD-26` or give it a document type (preferred); (b) remove the declaration's evidence (a declaration is its own statement); (c) add Valdara's qualification application exchange to the flow and refer to its ID (a story change).
- Needs decision: no
- From: broad (F10), context (F6, F8), logistics (F3)

### tender/13#F14 · Low · Master data the qualification does nothing with: customs trader numbers and Valdara's warehouse contractor
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: Copied master data (section 4.8). The customs trader numbers identify the parties towards customs; nothing here is declared to customs (they are used in 30 and 31). `ServiceProviderParty` ("A party providing a service to this party") names Castrano Logistics, Valdara's warehouse and despatch contractor, with the arrangement number and key account desk; the qualification relies on Saltmere only and does nothing with a warehouse operator (Castrano acts in 29). Unlike the register extract 12 (F13 there), a tenderer's own qualification has no reason to describe the business as such.
- Condition: Each party carries only the identifiers and related parties the document's purpose uses.
- Options: (a) leave them out of the tendering documents (preferred); (b) if Valdara relies on Castrano for delivery, declare it as such.
- Needs decision: no
- From: broad (F13), context (F9, F10), parties (F8)

### tender/13#F15 · Low · Italian street name and legal form tagged as English
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: The renderings tagged `en-XU` are Italian ("Via delle Officine"; "Società urvaniana per azioni", with an English gloss in brackets). Broad and parties refuted it: these are the world's English-language names of Urvanian places and legal forms (accepted as given), the texts are the same in every example, and here the tag is Valdara's own variety. analysis/review-merge-decisions.md keeps "Italian(ate) street names tagged English" as Low with Needs decision yes in every flow, because no convention is recorded; the merge aligns and carries the refutation. The legal form is the stronger case (not a proper name). The tag difference against Bayvarran-issued documents (`en-XB`) is a finding of those (12 F10).
- Condition: The world records that Italianate names and legal forms are the English renderings of Urvanian ones, or the English renderings are in English.
- Options: (a) record the convention in the world's story (preferred); (b) English renderings, at least of the legal form.
- Needs decision: yes
- From: merge (broad's and parties' refuted candidates, aligned with the main decisions table)

### tender/13#F16 · Low · Large enterprise with 180 employees
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- Why: The world's list defines `LARGE` as "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (above 50,000,000.00 XBL; `world/codelists/gc/EntitySizeCode.gc`). Valdara states 180 employees and a financial capability of 9200000.00 lume, and nothing in the flow states a turnover above the limit; by the figures given it is medium-sized. Broad rated it High; the merge follows parties (Low, decision yes) and merger C: the definition's "or a turnover above …" leaves room, and 9200000.00 is not stated to be the turnover (F3), so no strict contradiction can be shown. Unlike Marrowdale's `SMALL` with 85 persons (10 F1), where both conditions of the definition must hold.
- Condition: The size class of Valdara agrees with the employees and financial figures stated for it in the flow.
- Options: (a) state a turnover above 50 million lume (or 250+ employees), if Valdara is meant to be large (preferred: listed, 250 million ferra of capital, its own foundry); (b) `MEDIUM` in every example that describes it.
- Needs decision: yes
- From: broad (F1), parties (F6)

### tender/13#F17 · Low · Contacts that do not fit the role: Valdara's order desk, the subcontractor's "bids office" in procurement
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `order@valdara.example`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- Why: Valdara is the tenderer declaring its qualification, yet its contact is the order desk (a customer service officer, `order@…`), the function that takes purchase orders (right in the order documents 26–28). Saltmere's contact is named "Bids office", a selling function, but its job title and department are those of buying ("Procurement officer", "Procurement"); name, job title and department disagree. One finding per example, as the main decisions table groups contacts.
- Condition: Each contact's name, job title and department agree and fit the party's role in this document (preparing and answering a tender).
- Options: (a) a bid or tender contact for Valdara in the tendering documents, and a bid manager in sales or bids for Saltmere (preferred); (b) drop job title and department, or the contact, where the document needs none.
- Needs decision: no
- From: parties (F9, F10), broad (F12)

### tender/13#F18 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `ExemptionReason` in `PartyTaxScheme` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" names a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is a buyer status and fits; the wording does not.
- Condition: The party's exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F15), parties (F11)

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` has a correct check digit.
- Completed task: 540000.00 over 2023-01-01 to 2025-12-31 = 3 × the annual average 180000.00 (re-done), within five years before the issue date; its evidence `EV-FER-PARKS` is in the Evidence list; the customer, the City of Ferrano, is the city of Valdara's seat.
- Participation 80 % + 20 % = 100 %; 20 % is within the 30 % the notice allows for subcontracting (but see F8).
- 180 employees and 41 years exceed the required 10 persons and 3 years; ISIC 3100 is the required class; 9200000.00, if it is a yearly turnover, is far above 250000.00; 4000 benches a year cover the 240 of the contract and the 120 of the renewal.
- Issued 2026-02-25 08:52, 21 minutes before the tender 15 (09:13), which refers to it by its ID `VI-DOC-26-0199`; `VI-DOC-26-0199` precedes `VI-DOC-26-0201` in number and time. Interested lots `LOT-1` and `LOT-2` are the two lots of the procedure.
- The two notes are one text in Urvanian and English (`qau`, `en-XU`). Saltmere Engineering (register 20410685, ISIC 4290) is described as in 15 and is the subcontractor named there.
- Amounts are in lume, the currency of the criteria; Valdara's capital 250000000 XUF is 2.5 million lume at the invoice's 100 : 1 rate (money). Unit codes ANN, IE, EA; world-list codes resolve. +999 telephone numbers and `.example` addresses.

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: tagged `en-XU` here and `en-XB` in 03, 12, 14 and 16 — refuted, the tag follows the author of the document and the text is the same (from broad, parties); the Italian-text question is kept as F15 in line with the main decisions table.
- `/TendererQualification/cbc:Note[1]`: whether the Urvanian note says the same as the English one cannot be checked — refuted as a finding; nothing indicates a difference (from broad).
- `/TendererQualification/cbc:Note[2]`: `languageID` "en-XU" on an English note — refuted, a regional subtag is a valid language tag and Valdara is Urvanian (from logistics).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:PartyCapacityAmount`: equal to the total task amount — refuted by broad (the party did the whole task); the merge keeps the finding of context and money as F12, with this argument.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:AnnualAverageAmount`: the definition speaks of "The average monetary amount of a task such as this completed task" — refuted, the name says annual average and the value is the total over the three years (from money).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cac:RecipientCustomerParty` (City of Ferrano, name only): too thin for a reference — refuted, the customer is named and the evidence carries the proof (from context).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:PersonalSituation` = "No exclusion grounds apply.": a statement by absence — refuted, the notices require exactly this declaration (from context).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`: listing and share capital in a qualification — refuted, they bear on the legal and financial standing the qualification declares (from broad, context).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID`: the register number as an evidence identifier — refuted by logistics (the register entry is the evidence); the merge keeps it as F10, Low/yes, with this argument.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity`: 4000 against 6000 in 12 — refuted by logistics for this example (this document states its measure); kept as F11, Low/yes, with this argument.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount`: an amount where the definition says "The number of shares in the capital stock of a corporation" — refuted, the element is of an amount type; a point for the TC write-up (from parties).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` assigned in ISO 6523 — refuted as far as own knowledge goes; the ICD register was not available to check (from parties; the merge could not check it either).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:Language/cbc:ID`: `qau` a real ISO 639 code — refuted, qaa–qtz is reserved for local use (from parties).
- `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyLegalEntity`: incomplete (no legal form, size or registration date) — refuted, all optional and nothing depends on them (from parties).
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` = `-1` — refuted, no format prescribed, reads as UTC−1 (from parties).
- `/TendererQualification/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` — refuted, fits "The specific identifable location within a building where mail is delivered" (from parties).
- `/TendererQualification/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office` — refuted, a functional contact name; "Procurement office" and "Procurement" name the same unit (from parties).
- `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` = `STATE` — refuted, the level of the tax, not of the party (from parties).

## Changed in the merge
- broad/F4, context/F2, parties/F1 (Medium, both evidence IDs) → F1 Medium (classification, with logistics/F1) and F10 Low/yes (identity): logistics refuted the identity line, and the contest merges rated the same use Low/yes.
- logistics/F4 (Low/no) → F2 Medium/yes, with broad/F3, context/F1, parties/F2; the world's `SUBCONTRACTOR` definition (ESPD OERON) added to "Why" and the options.
- broad/F9 (Low) → F3 Medium, with money/F2 and context/F4 (part).
- broad/F2 (yes), logistics/F5 (Low) → F4 Medium/no: aligned with the contest merges (completed tasks below the threshold: Medium/no).
- broad/F14, parties/F12 (Low) → F7 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies).
- money/F1 (Medium) → F8 Low, with broad/F11 and logistics/F6: aligned with merger C; the base of the percentage is not fixed.
- context/F4 (Medium/yes) split: the undescribed financial capability into F3, the difference from 12 into F11 (Low/yes, with broad/F7, money/F3, parties/F7).
- context/F8 (Low/yes) folded into F13 with Needs decision no, as 07 F6.
- broad/F13, context/F9, context/F10, parties/F8 combined into F14 (one copied-master-data finding per example).
- F15 added from broad's and parties' refuted candidates, aligned with the main decisions table.
- broad/F1 (High/no) → F16 Low/yes, with parties/F6: no strict contradiction under the `LARGE` definition; aligned with merger C.
- parties/F9, parties/F10, broad/F12 combined into F17 (contacts grouped per example).

## Outside this review
- Brackenmere's tenders (17, 19) cite this document, Valdara's qualification, as their own tenderer qualification; that lies in 17 and 19 (from context).
