# LLM review: 03-ContractNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/03-ContractNotice.xml`, Git blob `7954b4a6494a5104f6b223a28caf36da90fc85ff` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 374ad95 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### contest/03#F1 · Medium · NoticeTypeCode `CN` is the standard-procedure type, not a design-contest notice
- XPath: `/ContractNotice/cbc:NoticeTypeCode` = `CN`
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:ProcedureCode` = `DESIGNCONTEST`
- Why: `ContractNotice. Notice Type Code` is "The type of notice (PIN, Qualification, Reduce time...)". The world's NoticeTypeCode list (verified in `world/codelists/gc/NoticeTypeCode.gc`) describes `CN` as "Calls for competition (eForms cn-standard)" and has no type for a design contest; the eForms list it cites has a separate design-contest notice (cn-desg, own knowledge of eForms), and UBL itself names the distinction for the award notice ("The type of notice (CAN general, CAN social, Design)"). The procedure is a design contest, so the code exists but its stated meaning is not this notice's.
- Condition: The notice type code of this notice identifies a design-contest notice, or the list's description of the code used covers design contests.
- Options: (preferred) add design-contest notice types to the world list (as eForms cn-desg / can-desg) and use them here and in the award notices; or widen the description of `CN`/`CAN` in the list.
- Needs decision: no
- From: context F2

### contest/03#F2 · Medium · Language code in LocaleCode
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language. Locale Code` as "A code signifying the locale in which this language is used". A locale is a language as used in a country or region (for example English as used in Bayvarra); `en` with `listID="ISO 639"` is the ISO 639 language code itself, the same value as the sibling `cbc:ID`, so the element repeats the language and says nothing about a locale (section 6 names a language code in `LocaleCode` as Medium). Verified in the XML at every place listed. The same value occurs 362 times in 213 examples (recounted in the merge with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l` and `grep -rl` for the file count; a line count of `LocaleCode listID="ISO 639">en<` gives 364 because it also matches other `…LocaleCode` elements).
- Condition: No `cbc:LocaleCode` in the example holds a bare ISO 639 language code; where a `LocaleCode` is present it identifies a locale (language and country or region) with a `listID` naming a locale list.
- Options: (preferred) leave `LocaleCode` out, since nothing in the document needs a locale beyond the language that `Language/cbc:ID` already gives; or give a real locale (e.g. a BCP 47 tag such as `en-XB`) with a matching listID. Same as every earlier flow.
- Needs decision: no
- From: broad F1, parties F2, context F1

### contest/03#F3 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- Why: The public bodies of this example (Lumeport Public Works Department, Bayvarra Information Service, Procurement Review Board of Bayvarra) are entered in the "Federal business register of Bayvarra" with `CorporateRegistrationTypeCode` `COMMERCIAL` (world list: "Commercial register: A register of businesses") and carry `CompanyLiquidationStatusCode` `ACTIVE` ("A code signifying the party's liquidation status"; code: "Active, not in liquidation"). A city department (and, where present, a federal information service or a review board) is not a business in a register of businesses and is not wound up by liquidation; the contracting party describes itself as "a department of the city of Lumeport" (`ContractingPartyType/PartyType`), and its ISIC class is 8411 (public administration). The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no type for a register of public bodies, so the value is forced. Verified in the XML. The values carry a meaning that does not fit the party (Medium, as the customs authority described as a company in the earlier flows). Parties added that a city department is not a legal person at all; the legal entity behind it is the City of Lumeport.
- Condition: No public body in the example carries a `CompanyLiquidationStatusCode` or a corporate registration scheme of the type "Commercial register"; a registration scheme given for a public body says what kind of register it is.
- Options: (preferred) leave the liquidation status and the registration type out for public bodies and keep only the register name and identifier, because the story needs no register type for them; or add a register type for public bodies to the world list; or give the City of Lumeport as the department's legal entity (this last option changes who the party is and would need a decision).
- Needs decision: no
- From: broad F2, parties F1, context F4

### contest/03#F4 · Low · Customs master data the procurement document does nothing with
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "One or more additional identifiers for this Party". The customs trader number (scheme `urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works Department towards customs and is used in its customs declarations (e.g. `tender/31-ImportCustomsDeclaration.xml`); this ContractNotice is a procurement document of a design contest for a service: nothing is imported, declared or transported, and nobody in the document uses the number. It is copied from the party's master data (section 4.8; the value is in 55 examples, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`, recounted in the merge).
- Condition: The contracting authority carries no customs trader identifier in this procurement document.
- Options: (preferred) leave these values out of the procurement documents and keep them where documents use them (customs declarations, invoices); or keep one only where the story gives this document a reason, and say so.
- Needs decision: no
- From: broad F3 (part), parties F4, logistics F1, context F3 (part)

### contest/03#F5 · Low · Tax scheme of the contracting authority in a document that may not use it
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". The contracting authority brings its state sales tax registration and exemption into a procurement document. This document states amounts (prizes, participation payments, an estimated contract value, a production limit of 900 lume a bench) but no tax on them. Broad and context (and money from 05 on) read it as master data copied into a document that does not use it (section 4.8). Money (01-04, 08) refuted that: the buyer's exemption tells candidates that the amounts of the contest and of the follow-up contract are net of the state sales tax. Both readings are possible; the merge could not settle which the world intends.
- Condition: Either the authority's `PartyTaxScheme` is absent from this document, or the world states that procurement documents carry it to show that amounts are net of sales tax (and it is then carried consistently).
- Options: (preferred) leave it out of documents without amounts and decide for the notices whether the exemption is meant as information to candidates (then keep it and say so where amounts are given); or keep it everywhere as the buyer's tax status.
- Needs decision: yes
- From: broad F3 (part), context F3 (part); refuted by money

### contest/03#F6 · Low · Exemption reason of the contracting authority worded as a sale
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReason` is "A reason for the party's exemption from tax", i.e. the party's own status. The text begins "Sale to a public body", the name of the code in the Bayvarran exemption list (whose other codes are reasons for exempt supplies), and so describes a transaction; this document records no sale. The second half of the text ("public bodies are exempt from the state sales tax") is the status the element asks for. Money refuted the code itself, rightly: the list describes `PUBLIC` as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer (verified in `world/codelists/gc/XB-TaxExemptionReasonCode.gc`). What remains is the wording of the text. The same text is in 55 examples (`grep -rl --include='*.xml' 'Sale to a public body: public bodies' world/examples | wc -l`).
- Condition: Where the authority's exemption reason is stated, the text states the party's status (a public body exempt from the state sales tax), not a sale.
- Options: (preferred) word the text as the status ("Public body: exempt from the state sales tax") and keep the code; or add a status code for public bodies to the list.
- Needs decision: no
- From: broad F3 (part), parties F3, context F3 (part)

### contest/03#F7 · Low · Requested legal form applies to the follow-up contract, not to the contest participants
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalFormCode` = `LTD`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Limited company (private): a group of participants forms one before the follow-u…`
- Why: `TendererQualificationRequest. Company Legal Form Code` is "The legal status requested for potential tenderers". The code `LTD` requests a private limited company, while the text says that for the contest itself a group only names a lead member and forms the company before the follow-up contract is awarded (context). Counter-argument (broad, which refuted it): the text explains the code, and a legal form to be taken by a group before award is exactly the kind of requested legal status the element carries. Both readings are possible; the merge cannot settle it.
- Condition: What the code requests and what the text says apply to the same tenderers at the same step.
- Options: (preferred) keep the code and word the text as the requirement on groups ("a group forms a limited company before the follow-up contract is awarded"); or state the requirement for the follow-up contract in text only.
- Needs decision: yes
- From: context F5; refuted by broad

### contest/03#F8 · Low · DurationPeriod of the reference criterion is the look-back window, not the criterion's validity
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:Description` = `Two completed designs of furniture or fittings for public spaces in the last five years.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cac:DurationPeriod/cbc:DurationMeasure` = `5`
- Why: `EvaluationCriterion. Duration_ Period` "Describes the period for which the evaluation criterion is valid" (verified in the model). The 5 years are the window in which the two reference designs must have been completed ("in the last five years"), not a period during which the criterion applies: a legitimate value in an element whose definition means something else (context).
- Condition: The five-year window is stated where it means a reference window (the Description already does), and `DurationPeriod`, if kept, gives the period for which the criterion is valid.
- Options: (preferred) keep the window in the Description and drop `DurationPeriod`; or keep it and record the reading as a finding on the UBL definition.
- Needs decision: no
- From: context F6

### contest/03#F9 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: A contact is "The primary contact for this party" and should handle the party's part in this document (section 5). The Procurement Review Board's "Registry", which receives appeals, is staffed by a `Procurement officer` of a `Procurement` department: the function of a buyer, not of the body that reviews buyers. The contacts are the parties' general contacts from the goods flows, the same in every example that carries these parties. Verified in the XML.
- Condition: Each contact in the example handles the party's part in the contest (requests to participate, designs and questions of the jury for a participant; appeals for the review board), with job title and department that agree with it.
- Options: (preferred) give these parties a contact for their role (a bids or design office for the participants, a registry clerk or registrar for the review board); or leave the contact out where the electronic address is the channel.
- Needs decision: no
- From: broad F4, parties F5, context F7

### contest/03#F10 · Low · CandidateReductionConstraintIndicator says the candidates have already been reduced
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `true`
- Why: UBL: "An indicator that the number of candidates participating in this process has been reduced (true) or not (false)". This document is issued before the requests to participate are due, so no candidate has been selected or dropped; what it announces is that the number will be limited, which the `EconomicOperatorShortList` already states (context). Counter-argument (broad, which refuted it): read for the procedure, the process does reduce the candidates to three to five. eForms maps its BT-52 "successive reduction" to this element (own knowledge), but under the semantic-conformance rule the definition decides; practice is context only.
- Condition: The indicator is absent from documents issued before any reduction, or its reading as "will be reduced" is recorded as a finding on the UBL definition.
- Options: (preferred) leave it out of the notice and the call (the short list carries the limitation); or keep it and record the reading for the TC write-up.
- Needs decision: no
- From: context F8; refuted by broad

### contest/03#F11 · Low · What the estimated contract amount of 54,000 lume covers is not stated
- XPath: `/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cbc:Description` = `A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.`
- Why: `RequestedTenderTotal` holds "Budget monetary amounts for the project as whole" and `EstimatedOverallContractAmount` is "The estimated overall monetary amount of a contract". The procurement is a design contest for services (`ProcurementTypeCode` `SERVICES`, UN CPC 83912): prizes, payments of 1,000 lume to each of at most five participants and a follow-up service contract. Nothing says what the 54,000 lume cover. The figure is exactly 60 × the production limit of 900 lume a bench in the project description (recalculated), which suggests the production cost of the benches, a contract this procurement does not award. Read instead as prizes, payments and follow-up contract (the usual way of valuing a design contest, money's own knowledge of Directive 2014/24/EU Art. 78), it should have changed when the first prize rose from 6,000 to 8,000 lume between the two versions of the prior information notice (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`, `02-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`), while the estimate stayed at 54,000 in every notice. Counter-argument (broad, which refuted it): without a breakdown no arithmetic contradiction can be shown (prizes 14,000 or 16,000 and payments up to 5,000 leave room for a follow-up contract of about 35,000). The merge cannot settle what the figure is meant to be, hence Low with a decision. In this document the first prize is already 8,000 lume.
- Condition: The estimated overall contract amount is the estimated value of what this procurement buys (prizes, payments and/or the follow-up service contract), agrees with the prize amounts of the same version, and what it covers can be read from the notice.
- Options: (a, preferred) keep an estimate of prizes, payments and follow-up contract, say what it covers and adjust it with the prize change; (b) if 54,000 is the production budget, remove it from `RequestedTenderTotal` and keep the per-bench limit in the description.
- Needs decision: yes
- From: money F1; refuted by broad

## Checked and consistent
- Merge: every finding above was re-checked against the XML (values, positions, counts) and against the referenced examples; the definitions quoted were looked up in UBL-Entities-2.5.gc and the code meanings in `world/codelists/gc/`. The counts were redone over `*.xml` only.
- `NoticeDocumentReference` `LPWD-DOC-26-0633` resolves to the prior information notice (`01-PriorInformationNotice.xml`, `02-PriorInformationNotice.xml`); its version 2 announced this notice for this date. (from broad)
- Prizes 8,000 + 4,000 + 2,000 lume and the text "Three prizes; the first is 8,000 lume" agree; the participation payment (1,000 lume) and the jury (five members) are the same in all notices and calls. (from broad)
- Dates: issue date before the end of the request period (2026-04-18) before the tender deadline 2026-06-12 12:00; the award (`15-ContractAwardNotice.xml`, award date 2026-06-28) comes after it. (from broad)
- Short list: expected 5, maximum 5, minimum 3, agreeing with the process description "three to five selected participants"; threshold of two references in five years agrees with the qualification request (`ThresholdQuantity` 2 EA, `DurationMeasure` 5 ANN). (from broad)
- The relaunch justification (`PreviousCancellationReasonCode` `UNSUITABLE`, "both designs received were unacceptable") fits the code's meaning "No suitable tender". (from broad)
- The contracting authority, Bayvarra Information Service, the review board and Brackenmere Furniture are described with the same identifiers, names, addresses, legal entities and contacts in every example of the flow where they occur (compared element by element over all 16 XML files). (from broad)
- Prizes: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`, second 4,000, third 2,000 lume; `PrizeDescription` ("Three prizes; the first is 8,000 lume.") agrees with the three `Prize` aggregates and their ranks. (from money)
- Currency: every amount is in `XBL` (Lume), the currency of the contracting authority's tax scheme (`TaxScheme/CurrencyCode` `XBL`). (from money)
- Payments to participants: 1,000 lume to each selected participant that submits a conforming design; with at most five participants (`EconomicOperatorShortList/MaximumQuantity` 5) the outlay is at most 5,000 lume, and prizes plus payments total at most 19,000 lume (calculated). (from money)
- The prize amounts equal those of every other version of the notices from 02 onwards (02, 03, 04, 08, 09 and the award notice 16), compared over `*.xml`. (from money)
- Every party is described identically in every example of the flow that carries it (all leaf values compared per party name across the 16 examples; the pre-selected party in 15/16 is a subset of Brackenmere's data). (from parties)
- For every party, `PartyIdentification/ID`, `PartyLegalEntity/CompanyID` and the suffix of `ElectronicAddressID` agree, and the tax scheme's jurisdiction (state or country) matches the state or country of the postal address. (from parties)
- Fictional values: telephone numbers use +999 (not assigned to a country by ITU, own knowledge); e-mail and web domains use `.example` (reserved, RFC 2606). (from parties)
- Reference: `/ContractNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633` resolves to the prior information notice (01, 02), a notice of the same process (same ContractFolderID), which is what NoticeDocumentReference means. (from logistics)
- Dates against the issue time: `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-04-18` and `/ContractNotice/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-06-12` lie after the issue date and in that order; the requests to participate (06, 11: 2026-04-01 and 2026-04-13) arrive before the participation deadline, the award (`15-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:AwardDate` = `2026-06-28`) after the submission deadline. (from logistics)
- Quantities: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `2` with DurationMeasure 5 ANN matches its Description (two designs in the last five years); short list Minimum 3 / Expected 5 / Maximum 5 matches "three to five selected participants" in TenderingProcess/Description. (from logistics)
- Codes: NoticeTypeCode CN, ProcedureCode DESIGNCONTEST, SubmissionMethodCode ELECTRONIC, PreviousCancellationReasonCode UNSUITABLE (fits the cancelled 2025 contest with unacceptable designs), EvaluationCriterionTypeCode REFERENCES, EconomicOperatorRoleCode LEAD, CompanyLegalFormCode LTD, ISIC 8423 for the review board. (from logistics)
- Appeal receiver: the Procurement Review Board (register 20410822, address LUM-ADR-075593) is described identically in 03, 04, 08 and 09. (from logistics)
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against. (from logistics)
- Prize amounts: Prize[1] = `8000.00`, Prize[2] = 4000.00, Prize[3] = 2000.00 lume, matching the PrizeDescription ("the first is 8,000 lume") and version 2 of the PIN. (from context)
- The short list (minimum 3, expected and maximum 5) agrees with the process description ("three to five selected participants") and with `02-PriorInformationNotice.xml`. (from context)
- Dates: requests to participate due before designs (participation `2026-04-18`, designs 2026-06-12 12:00), both after the issue date. (from context)
- ProcessJustification: PreviousCancellationReasonCode `UNSUITABLE` ("No suitable tender") agrees with its text (both designs of the cancelled contest were unacceptable). (from context)
- The appeal terms name a receiver of appeals (the review board) and a time limit; the AppealTerms aggregate fits. (from context)

## Considered and refuted
- `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cbc:IndustryClassificationCode` = `8423`: suspected that "Public order and safety activities" does not fit a procurement review board — refuted because ISIC 8423 includes the administration of courts and the judicial system, and a review board deciding appeals is a quasi-judicial body (own knowledge of ISIC Rev.4). (from broad)
- `/ContractNotice/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `true`: suspected that the indicator ("the number of candidates … has been reduced") cannot be true before the selection — refuted because the notice describes the procedure, which reduces the candidates to three to five by selection; read for the process, the value is correct. (from broad) Not followed in the merge: kept as F10, with this argument recorded there as counter-argument.
- `/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`: suspected that the estimate should have risen with the first prize (6,000 to 8,000 lume between the two versions of the prior information notice) — refuted because the flow does not say what the 54,000 lume consist of (prizes 14,000 + participation payments up to 5,000 leave about 35,000 for the follow-up contract); without a breakdown no arithmetic contradiction can be shown. (from broad) Not followed in the merge: kept as F11, with this argument recorded there as counter-argument.
- `/ContractNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633`: suspected that the reference is ambiguous between the two versions of the prior information notice — refuted because a notice reference by ID refers to the notice, whose current version is version 2; nothing in this notice depends on version 1. (from broad)
- `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalFormCode` = `LTD`: suspected that requiring a limited company excludes the groups the notice invites — refuted because `CompanyLegalForm` explains that a group forms a limited company only before the follow-up contract and names a lead member for the contest. (from broad) Not followed in the merge: kept as F7, with this argument recorded there as counter-argument.
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: suspected that the reason describes a transaction ("Sale to a public body") rather than the party's own status — refuted because the list defines the code as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer, and `ExemptionReason` says so ("public bodies are exempt from the state sales tax"). (from money) Accepted in the merge for the code; the wording of the text remains finding F6.
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme`: suspected as master data copied into a notice without tax content — refuted because the notice sets a production limit of 900 lume a bench and announces a follow-up service contract; the buyer's exemption tells candidates that these amounts are net of the state sales tax. (from money) Not followed in the merge: kept as F5, with this argument recorded there as counter-argument.
- `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[3]/cbc:Description`: suspected that a third prize awarded only "if the jury finds it of prize standard" contradicts "Three prizes" and `PrizeIndicator` true — refuted because a conditional third prize is an ordinary contest term and the first two prizes are unconditional. (from money)
- `XBL` as currency: checked that it is not a code assigned in ISO 4217 (own knowledge: the assigned X-codes near it are XBA–XBD, bond-market units); it is the world's fictional Lume. (from money)
- `/ContractNotice/cac:ContractingParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 8411 "General public administration activities" for a public works department was suspected to be too general — refuted: the department is part of the city's general administration, and no ISIC class fits a municipal works department better. (from parties)
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:Department`: the address department "Procurement office" against the contact department "Procurement" — refuted: the same unit, once as the addressee on mail and once as the contact's department. (from parties)
- `/ContractNotice/cac:ReceiverParty/cac:PostalAddress/cbc:PostalZone`: two postal zones (38517, 38520) for buildings on the same square (Civic Square) — refuted: postal codes for individual large addressees on one square are usual, and both are in the same city subdivision and state. (from parties)
- `/ContractNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633`: suspected that a reference by ID alone is ambiguous because two versions of the referenced document exist (01 and 02) — refuted because the versions share one document ID by design (VersionID/PreviousVersionID), a reference by document ID addresses the document, and the issue dates make the intended version unambiguous (the notice refers to the PIN published before it; version 2 of 2026-02-23 is the current one). (from logistics)
- `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-04-18`: suspected that a deadline without EndTime is incomplete — refuted: a date-only deadline is a legitimate reading (end of that day); the submission deadline, where the hour matters for the anonymous judging, does carry `12:00:00`. (from logistics)
- `/ContractNotice/cbc:ID` = `LPWD-DOC-26-0634`: suspected that document numbers running consecutively across three senders (LPWD-DOC-26-0633 … BF-DOC-26-0637, BF-DOC-26-0638, BIS-DOC-26-0639, LPWD-DOC-26-0640) imply one shared counter — refuted: each number carries its sender's prefix, is unique over `*.xml` (`grep -rl --include='*.xml'` finds each only in this flow) and nothing in UBL requires gaps; the same numbering style runs through the whole world (e.g. `tender/*.xml`). (from logistics)
- `/ContractNotice/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationTypeCode` = `OWN`: suspected that an aggregate defined as "The type of represention empowering the party to act on behalf of a third party" does not belong to a party acting for itself — refuted because the world's list offers `OWN` and `BEHALF` as the two answers, and stating `OWN` explicitly avoids implying it by absence (IND6). (from context)
- `/ContractNotice/cac:TenderingProcess/cac:ProcessJustification/cbc:Description` = `Relaunch of the design contest PWD-2025-PROM-DC…`: suspected that a justification "for the selection of this tendering process" should explain the choice of a design contest rather than the relaunch — refuted: the aggregate also carries the reason a previous process was cancelled (PreviousCancellationReasonCode), and the text explains why the same procedure is run again. (from context)
- `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `true` and `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`: checked whether the indicators agree with their text — they do: the first prize says its author "is invited to negotiate the follow-up service contract", and nothing in the text makes the jury's ranking advisory. (from context)
- `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`: whether a role belongs in a qualification request — refuted: the notice asks a group to name a lead member, which is what the role states. (from context)
- `/ContractNotice/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayvarra Information Service`: suspected a wrong receiver for a notice of a city department — refuted because a notice goes to the publication office, and the Information Service is that office (its contact is "Publications and register"). (from context)

## Changed in the merge
- context F2 (NoticeTypeCode) kept Medium; Needs decision yes → no: the fix is a code or a list description, not the story (aligned with merger B for the award notices).
- broad F2 + parties F1 + context F4 → one finding, Medium, Needs decision no (see the reasons in 01: aligned with the earlier flows and merger B).
- broad F3 and context F3 split into three findings (customs identifier; authority tax scheme, now Low/yes because money refuted it; wording of the exemption reason).
- context F5 (requested legal form) Needs decision no → yes, because broad refuted it with a reading the merge cannot dismiss.
- context F7 (review board registry) merged into the contacts finding of broad F4 / parties F5 (same contact, same condition).
- context F8 (CandidateReductionConstraintIndicator) kept Low/no; broad's refutation recorded in the finding as counter-argument (aligned with merger B).
- Every finding merged from several parts keeps the clearest wording and all evidence; findings are numbered by severity and then by position in the document.

## Outside this review
- The same party descriptions (public bodies in the commercial register, `LocaleCode` `en`, the general contacts, the registration date 1996-01-01, the province in `Region`) recur in the other flows that carry these parties (tender, utilities, furniture, mast and the goods flows); they belong to those examples' reviews. (from parties)
