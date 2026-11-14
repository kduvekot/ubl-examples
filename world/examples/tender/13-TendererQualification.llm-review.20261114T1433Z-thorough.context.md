# LLM review: 13-TendererQualification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/13-TendererQualification.xml`, Git blob `fbf9d6ddac8eb891f81b7a2f593f1db23d28b8d1` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
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

### tender/13#F1 · Medium · A sole tenderer with a subcontractor is coded as a consortium
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:TendererRoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads.`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:TendererRoleCode` = `SUBCONTRACTOR`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- XPath: `/TendererQualification/cbc:Note[2]` = `The manufacturer with Saltmere as subcontractor for the installation.`
- XPath: `15-Tender.xml:/Tender/cac:SubcontractorParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: The note says what the arrangement is: "the manufacturer with Saltmere as subcontractor for the installation", and the tender (15) names Saltmere Engineering as `SubcontractorParty`. Valdara is nevertheless coded `LEAD` ("Consortium lead") twice; the world's list has `SOLE` ("Sole tenderer") for a tenderer without partners. And Saltmere is placed in `AdditionalQualifyingParty`, which is "the qualifications of a tenderer party other than the main tenderer party when bidding as a consortium": a subcontractor is not a tenderer party and there is no consortium. "Leads." describes nothing.
- Condition: The role codes say what the note and the tender say (sole tenderer with a subcontractor), and a party is an additional qualifying party only if it is a member of a tendering consortium.
- Options: (a) Preferred: `SOLE` for Valdara, no `EconomicOperatorRole`; describe Saltmere as subcontractor in the tender (where it already is) and, if its qualifications are relied on, say so in a declaration. (b) Make Saltmere a consortium member in 13 and 15, which changes the story (joint liability, no subcontract).
- Needs decision: yes

### tender/13#F2 · Medium · A class code and the register number in the elements for evidence identifiers
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessClassificationEvidenceID` = `ISIC-3100`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `XU-R-104274`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:BusinessClassificationScheme/cac:ClassificationCategory/cbc:CodeValue` = `3100`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- Why: `BusinessClassificationEvidenceID` is "an identifier for an item of evidence to support the classification of this qualifying party" and `BusinessIdentityEvidenceID` "… to support the business identity". `ISIC-3100` is the class itself (already in `BusinessClassificationScheme`), not a document that proves it; `XU-R-104274` is the party's register number (already its `PartyIdentification`, with the register as scheme), not the identifier of a register extract or certificate. Neither identifies an item of evidence, and the document's `Evidence` list has no such item.
- Condition: Both elements carry the identifier of an evidence item (e.g. a register extract) that the document lists or references, or are absent.
- Options: (a) Preferred: an `Evidence` for the register extract (the extract 12 of the information service would do) and its ID in both elements. (b) Remove both.
- Needs decision: no

### tender/13#F3 · Medium · The qualification does not answer the requirements of the notices
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Benches for Ferrano's parks.`
- XPath: `/TendererQualification/cac:Evidence/cbc:Name` = `Ferrano reference`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Three similar supplies in five years.`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `3`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:SpecificTendererRequirement/cbc:Name` = `Certified timber`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:SpecificTendererRequirement/cac:SuggestedEvidence/cbc:Name` = `Forestry certificate`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- Why: A tenderer qualification is "a document declaring the qualifications of a tenderer", here against the requirements that 01, 02 and 03 state. They ask for three similar supplies in five years; the document declares one completed task (Ferrano's parks, one three-year contract). They ask for certified timber with a forestry certificate; nothing in the document mentions it. They ask for a yearly turnover of at least 250000 lume; the only financial figure is an unlabelled capability amount. Years in operation (41) and staff (180) are answered. On this document alone the department could not find the tenderer qualified on references and timber, yet the flow goes on to an award to this tenderer.
- Condition: The qualification shows, for each requirement of the notices, the declared fact and its evidence (three references, the timber certificate, the turnover).
- Options: (a) Preferred: three completed tasks, a turnover figure named as such, and the forestry certificate as evidence. (b) Lower the requirement in the notices to what is declared here.
- Needs decision: no

### tender/13#F4 · Medium · Capability figures without a meaning, and different from the register extract
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:Description` = `4,000 benches a year.`
- XPath: `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `4800000.00`
- XPath: `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`
- Why: `FinancialCapability` carries 9200000.00 lume with no description, type or period: turnover, equity or credit line cannot be told apart, and the notices ask for *yearly turnover*. The technical capability is "4,000 benches a year". The register extract the department receives two days later (12) gives, for the same company, a production capability of 6000 pieces and 4800000.00 lume, supported by the annual accounts. If the figures measure the same things, the documents contradict each other; if not, nothing says so.
- Condition: Each capability says what its measure is and for which period, and agrees with what 12 says about the same thing.
- Options: (a) Preferred: a described financial capability ("Turnover 2025") and the same production capacity in 12 and 13. (b) Keep the figures and name what differs.
- Needs decision: yes

### tender/13#F5 · Medium · A language code in `LocaleCode`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/13#F6 · Low · A declaration cites evidence the document does not contain
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Declaration/cac:SuppliedEvidence/cbc:ID` = `EV-DEC-1`
- XPath: `/TendererQualification/cac:Evidence/cbc:ID` = `EV-FER-PARKS`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cac:SuppliedEvidence/cbc:ID` = `EV-FER-PARKS`
- Why: The completed task cites `EV-FER-PARKS`, which the document defines under `Evidence`. The integrity declaration cites `EV-DEC-1`, which is defined nowhere in the document (and in no other example: `grep -l EV-DEC-1 world/examples/tender/*.xml` lists only this file).
- Condition: Every `SuppliedEvidence/ID` has an `Evidence` with that ID in the document.
- Options: (a) Preferred: add the evidence (the signed declaration). (b) Remove the supplied evidence; a declaration is its own statement.
- Needs decision: no

### tender/13#F7 · Low · "Party capacity" equal to the task total
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:PartyCapacityAmount` = `540000.00`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:TotalTaskAmount` = `540000.00`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:AnnualAverageAmount` = `180000.00`
- Why: `PartyCapacityAmount` is "a monetary amount corresponding to the financial capacity of the party that carried out this completed task". It repeats the total of the task (540000.00 = 3 × 180000.00, which is consistent with the period 2023–2025), so it says nothing about the party's capacity, which the same document puts at 9200000.00 lume.
- Condition: `PartyCapacityAmount` states the party's financial capacity at the time of the task, or is absent.
- Options: (a) Preferred: remove it. (b) Give the capacity (e.g. turnover of those years).
- Needs decision: no

### tender/13#F8 · Low · A second number for the self-declaration, without saying what it is
- XPath: `/TendererQualification/cac:AdditionalDocumentReference/cbc:ID` = `VI-ESPD-26`
- XPath: `/TendererQualification/cbc:ID` = `VI-DOC-26-0199`
- Why: The only document reference is `VI-ESPD-26`, with an ID alone. No example carries that ID; the flow has a qualification application response only from Brackenmere (07). If it is Valdara's answer to a qualification application request, that exchange is missing from the flow; if it is another name for this document, it is redundant.
- Condition: The reference says what it refers to and resolves, or is absent.
- Options: (a) Preferred: remove it. (b) Add Valdara's qualification application exchange to the flow and refer to its ID.
- Needs decision: yes

### tender/13#F9 · Low · The logistics provider of Valdara Industries, with contract number and key account desk, in a tenderer qualification
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: `ServiceProviderParty` is "a party providing a service to this party": Castrano Logistics, which warehouses and despatches for Valdara Industries, with the number of their arrangement and its key account desk. The qualification does not present Castrano as a party whose capacities are relied on, and the tender names only Saltmere as subcontractor. It looks copied from the party's master data into a document that does not use it.
- Condition: The party carries a service provider only in documents in which that provider acts or must be known (despatch, transport, customs).
- Options: (a) Preferred: remove the service provider here. (b) If the provider matters to the buyer, declare it where the document has a place for it (as a subcontractor or in the delivery terms).
- Needs decision: no

### tender/13#F10 · Low · Customs trader numbers of the parties in a tenderer qualification
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. Nothing in this document is declared to customs; the numbers are used only when the benches cross the border (30, 31). They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- Shares 80 % and 20 % add up to 100 and stay within the maximum subcontracting share of 30 % of the notices.
- Completed task: 540000.00 over 2023-01-01 to 2025-12-31 is 3 × the annual average of 180000.00.
- ISIC 3100 is the class the notices require; 41 years in operation and 180 staff exceed the required 3 years and 10 persons.
- Both lots are named as lots of interest, and the tender (15, issued 21 minutes later) is "for both lots" and cites this document by its ID.
- ISIN XU0001042501 (security listing of the party): check digit correct (`check_ids.py`).
- The two notes are one text in Urvanian and English, tagged `qau` and `en-XU`.

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cac:RecipientCustomerParty` (City of Ferrano, name only): suspected too thin for a reference — refuted, the customer is named and the evidence `EV-FER-PARKS` carries the proof.
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:PersonalSituation` = "No exclusion grounds apply.": suspected statement by absence — refuted, the notices require exactly this declaration ("declares this in its self-declaration").
- The security listing (ISIN, market) of the tenderer in a qualification: suspected master data — refuted for this document, a listing is part of the legal and financial standing a qualification declares.

## Outside this review
- The tenders of Brackenmere (17, 19) cite this document, Valdara's qualification, as their own tenderer qualification; that lies in 17 and 19.
