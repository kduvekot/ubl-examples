# LLM review: 03-CallForTenders.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/03-CallForTenders.xml`, Git blob `24f08018e3295692f3f3cc82e4d7e61355b48c44` (committed)
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

### tender/03#F1 · High · A latest date for obtaining security clearance, although no clearance is required
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: `LatestSecurityClearanceDate` is "the end date until which the candidates can obtain the necessary level of security clearance". The same tendering terms say, in `SecurityClearanceTerm`, that no clearance is required ("Parks are public places."). There is no "necessary level" to obtain, so the date has nothing to refer to and contradicts the term. The term itself only states what its absence would say (CLAUDE.md: nothing implied by absence).
- Condition: The tendering terms do not carry a latest clearance date while they say that no clearance is required; a security clearance term is present only if a clearance is in fact asked.
- Options: (a) Preferred: remove the date and the "not required" term, since nothing in the world asks for a clearance for park benches. (b) Give the procedure a real clearance requirement (e.g. for work in a guarded site) and keep both.
- Needs decision: no

### tender/03#F2 · High · The call for tenders refers to a call for tenders under an ID that is not its own
- XPath: `/CallForTenders/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTendersDocumentReference` is "a reference to a Call for Tender associated with these tendering terms". This document is itself the call for tenders, with the ID `LPWD-DOC-26-0189`; its own tendering terms refer to a call for tenders under another ID, `PWD-2026-PARKS-CFT`, which no example of the flow carries. Either the reference points to itself under a second name, or to a document that does not exist. The catalogue of the flow refers to this document as `LPWD-DOC-26-0189`. The same ID is used in 8 examples of the flow (01, 02, 03, 06, 15, 17, 19, 24; `grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml` lists these 8 files).
- Condition: Every reference to the call for tenders of this procedure resolves to the ID of `03-CallForTenders.xml`, and the call for tenders does not refer to itself.
- Options: (a) Preferred: remove the self-reference. (b) If `PWD-2026-PARKS-CFT` is meant as a second, file-level number of the documents, say so (e.g. `DocumentType`) and use one number consistently in the flow.
- Needs decision: no

### tender/03#F3 · High · A replaced notice is named, but a call for tenders is not a notice and replaces none
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/CallForTenders/cbc:VersionID` = `1`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`
- Why: `ReplacedNoticeDocumentReference` is "a reference to the notice that is being replaced". A call for tenders is not a notice and replaces no notice; this is its version 1. The ID named, `PWD-2026-PARKS-PIN`, is carried by no example (the prior information notice has the ID `LPWD-DOC-26-0187` and is referenced by that ID in `TenderingProcess/NoticeDocumentReference`). The same reference occurs in 4 examples (01, 02, 03, 24; `grep -l PWD-2026-PARKS-PIN world/examples/tender/*.xml`).
- Condition: `ReplacedNoticeDocumentReference` is present only in a notice that replaces an earlier notice, and then carries that notice's document ID.
- Options: (a) Preferred: remove it. (b) If the flow should show a corrected notice, add that notice and let it, and only it, carry the reference.
- Needs decision: no

### tender/03#F4 · High · Lot 2 is "works" in the prior information notice and "services" in the contract notice and the call for tenders
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementSubTypeCode` = `INSTALL`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the park benches`
- Why: The same lot of the same procedure is described with two different contract natures: `WORKS` in `01-PriorInformationNotice.xml`, `SERVICES` (sub-type `INSTALL`, CPC 87390 "Installation services of other goods n.e.c.") in `02-ContractNotice.xml` and `03-CallForTenders.xml`. The name differs as well. The nature of a lot decides which rules and thresholds apply; nothing in the later documents says that it was changed.
- Condition: Lot 2 has the same `ProcurementTypeCode` and the same name in every example that describes it.
- Options: (a) Preferred: `SERVICES` everywhere (anchoring delivered benches is an installation service, as the CPC code of 02 and 03 says). (b) `WORKS` everywhere, with a matching classification. (c) Keep the change and state it in the contract notice as a change against the prior information.
- Needs decision: no

### tender/03#F5 · Medium · Variants are flagged as unconstrained in number, with a maximum of one
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:VariantConstraintCode` = `ALLOWED`
- Why: `VariantConstraintIndicator` is "an indicator that variants are allowed and unconstrained in number (true) or not allowed (false)". `MaximumVariantQuantity` limits the tenderer to one variant, so variants are allowed but constrained in number; the value `true` asserts the opposite of the limit next to it. The indicator has no value for "allowed with a limit"; the code `ALLOWED` and the quantity already say it.
- Condition: The indicator is not `true` while a maximum number of variants is given.
- Options: (a) Preferred: leave the indicator out and keep `VariantConstraintCode` and `MaximumVariantQuantity`. (b) Drop the maximum and keep `true`, if the buyer really accepts any number of variants.
- Needs decision: no

### tender/03#F6 · Medium · `MaximumAdvertisementAmount` of 500 lume is not the maximum advertised value of the procedure
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount` = `148896.00`
- Why: The definition is "the maximum advertised monetary value of the tendering process". The procedure is advertised with an estimate of 124080.00 and a maximum of 148896.00 lume; 500.00 is neither. The value reads like a cap on advertising costs to be reimbursed by the awardee (the Spanish practice the element comes from, from my knowledge of CODICE), which is not what the UBL definition says, and nothing else in the document explains a cost of 500 lume.
- Condition: The amount is the maximum value at which the procedure is advertised, or the element is absent.
- Options: (a) Preferred: remove it (the maximum is already in `RequestedTenderTotal/MaximumAmount`). (b) Set it to the advertised maximum. (c) If advertising costs charged to the awardee are part of the story, state them in a clause or note and record the unclear UBL definition as a finding for the TC.
- Needs decision: yes

### tender/03#F7 · Medium · The reimbursement fee of concession projects is used for the price of paper copies
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- Why: `RequiredFeeAmount` is "the amount of the reimbursement fee for concession procurement projects" and `FeeDescription` "text describing the reimbursement fee for concession procurement projects". This is a purchase of supplies under a framework, not a concession, and the text describes the price of paper copies of the documents. That price has its own element, `TenderingTerms/DocumentationFeeAmount` ("the amount to be paid to obtain the contract documents and additional documentation"), which already carries the same 50.00 lume. The two elements are repeated in both lots, so the notice states the same fee four times, three of them in the concession elements.
- Condition: `RequiredFeeAmount` and `FeeDescription` are absent from a project that is not a concession; the price of paper copies is stated once, in `DocumentationFeeAmount` (its explanation in a note of the tendering terms).
- Options: (a) Preferred: remove both elements at project and lot level and move the sentence to a `TenderingTerms/Note`. (b) None other seen: the definition leaves no room for a non-concession fee.
- Needs decision: no

### tender/03#F8 · Medium · A strategic-procurement code in the element for an additional contract nature
- XPath: `/CallForTenders/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementType` = `Environmental impact: recycled steel and certified timber are asked`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- Why: In `ProcurementAdditionalType`, `ProcurementTypeCode` is "a code signifying the type of procurement project (e.g., goods, works, services)" and `ProcurementType` the same as text. `GREEN` ("Environmental impact", from the list StrategicProcurementCode) is not a type of procurement in that sense but a policy objective. eForms uses the aggregate this way (BT-06 strategic procurement, from my knowledge of the eForms SDK); under the repository's rule of semantic conformance that practice does not change the UBL definition. The project does have a real additional nature that is not stated here: lot 2 is installation (services or works) next to the supplies of lot 1.
- Condition: `ProcurementAdditionalType/ProcurementTypeCode` carries a contract nature (supplies, services, works); the environmental objective is stated where UBL has a place for it.
- Options: (a) Preferred: put the additional nature of lot 2 here and state the environmental objective in the elements that already carry it (`ContractExecutionRequirement` with `ENVIRONMENTAL`, `SpecificTendererRequirement`), or in the project note. (b) Keep it as the eForms-compatible encoding and record it as a deliberate difference with a finding for the UBL TC.
- Needs decision: yes

### tender/03#F9 · Medium · A language code in `LocaleCode`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply, e.g. Bayvarra for English as used there). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: `LocaleCode`, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/03#F10 · Medium · An open procedure with periods for invitations and requests to participate
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-02-26`
- Why: `InvitationSubmissionPeriod` is "the period during which invitations to tender must be completed and delivered", `ParticipationInvitationPeriod` "the period during which the invitation to participate must be sent" and `ParticipationRequestReceptionPeriod` "the period during which requests for participation must be completed and delivered". These are the steps of a procedure in two stages (restricted, negotiated). The procedure is `OPEN`: any operator tenders directly until 2026-02-26, nobody requests to participate and nobody is invited; the tenders of the flow (15, 17, 19) are submitted without an invitation. The three periods describe steps the procedure does not have, and all three have ended before this call for tenders is issued (2026-02-12).
- Condition: A procedure with `ProcedureCode` `OPEN` carries no periods for invitations or requests to participate.
- Options: (a) Preferred: remove the three periods. (b) Make the procedure a restricted one, which changes the story of the flow (requests to participate, a selection, invitations).
- Needs decision: no

### tender/03#F11 · Medium · An "original contracting system" in a procedure that reopens nothing
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:ContractingSystemCode` = `FRAMEWORK`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ContractingSystem/cbc:Description` = `Framework with one supplier.`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: `OriginalContractingSystemID` is, "when reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system". This procedure does not reopen competition under an existing framework: it is an open procedure that establishes a new framework with one supplier (`ContractingSystem` `FW-1`, `FrameworkAgreement`). A framework of 2024 (`PWD-FW-2024-PARKS`) appears nowhere else in the flow (the value occurs only in 02, 03 and 21, in this element; `grep -l PWD-FW-2024-PARKS world/examples/tender/*.xml`). The condition of the definition is not met, and the reader is told that a second, older framework is involved.
- Condition: `OriginalContractingSystemID` is present only in a procedure that reopens competition under an existing framework agreement or dynamic purchasing system, and then identifies that system.
- Options: (a) Preferred: remove it. (b) If the benches of 2026 are meant to be a call-off under a 2024 framework, the whole procedure (open, new framework, notices) would have to change.
- Needs decision: yes

### tender/03#F12 · Low · Design-contest indicators in a supply procedure
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:NoFurtherNegotiationIndicator` = `true`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: `PrizeIndicator` ("whether a prize will be awarded") and `FollowupContractIndicator` ("if any service contract following the contest will be awarded to the winner or one of the winners of the contest") belong to design contests; with `false` they only state what their absence says (nothing implied by absence). `BindingOnBuyerIndicator` ("if the decision is binding on the buyer") is the jury-decision indicator of a contest; here there is no jury decision, the buyer's own committee evaluates. `NoFurtherNegotiationIndicator` ("if no further negotiation is allowed") says something only in a procedure that could have negotiation; in an open procedure it is never allowed.
- Condition: The awarding terms of an open supply procedure carry none of the four indicators, unless the document explains what each refers to.
- Options: (a) Preferred: remove all four. (b) Keep `NoFurtherNegotiationIndicator` if the world's procurement law lets an open procedure be followed by negotiation, and say so.
- Needs decision: no

### tender/03#F13 · Low · Works quality control stated for a supply project
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- Why: `QualityControlCode` is "the indication of whether or not the control quality is included in the works project". The project is `SUPPLIES`; "Inspection on delivery" is an acceptance rule for delivered goods, not quality control included in a works project.
- Condition: `QualityControlCode` is present only for (the part of) a project that is works, with a value that says whether quality control is part of it; the inspection of delivered benches is stated as a delivery or acceptance term.
- Options: (a) Preferred: remove it and state the inspection on delivery in the contract conditions or a note. (b) Keep it only on the installation lot if that lot is works (see the finding on lot 2).
- Needs decision: no

### tender/03#F14 · Low · "At least" in the text, "greater than" in the code
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- Why: The description sets a minimum that is included ("at least twice the estimate"); `ExpressionCode` `GT` and the expression "Turnover > 2 × estimate" exclude the threshold itself. A tenderer with a turnover of exactly the threshold passes by the text and fails by the code. (Twice the estimate of 124080.00 is 248160.00; the threshold is the rounded 250000.00, which the text does not say either.)
- Condition: Description, code and expression state the same comparison against the same amount.
- Options: (a) Preferred: a "greater than or equal" code and "≥", with the description naming 250000 lume. (b) Change the text to "more than".
- Needs decision: no

### tender/03#F15 · Low · The qualification request is given the role "consortium lead"
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads a consortium.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Any legal form; consortia must name a lead member.`
- Why: `EconomicOperatorRole` here is "a class to describe the tenderer contracting role", i.e. the role to which this set of qualifications applies. With `LEAD` the only qualification request of the procedure applies to consortium leads only, although its content (legal form, turnover, references, certified timber) is asked of every tenderer, and the tenders of the flow come from single tenderers. "Leads a consortium." describes a party, not a requirement.
- Condition: The qualification request applies to the tenderers it is meant for: no role when it applies to every tenderer, or one request per role with the requirements of that role.
- Options: (a) Preferred: remove the role. (b) Add what is specific to a lead (e.g. joint liability) in a second request with that role.
- Needs decision: no

### tender/03#F16 · Low · Subcontract terms: a "precise" share equal to the maximum, an amount that is not that share, and a price flagged as known
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:UnknownPriceIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Description` = `Installation may be subcontracted.`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted", `MaximumPercent` "the maximum percentage allowed to be subcontracted": the buyer sets a ceiling, so only the maximum has a reason; a precise share is what a tenderer states. `Amount` ("the monetary amount assigned to the subcontracted task") is 4320.00, the estimate of the installation lot, which is 3.5 % of the estimate of 124080.00 (4320 / 124080), not 30 %; the terms do not say which of the two limits holds. `UnknownPriceIndicator` `false` says the subcontract price is known, which a buyer cannot say before tenders exist; it states what absence would imply.
- Condition: The buyer's subcontract terms state one limit (a maximum share, or the task that may be subcontracted with its estimated amount), and no statement about a subcontract price that does not exist yet.
- Options: (a) Preferred: keep `MaximumPercent`, `SubcontractingConditionsCode` and `Description`; remove `Rate`, `Amount` and `UnknownPriceIndicator`. (b) Keep `Amount` as the estimate of the installation and explain it in the description.
- Needs decision: no

### tender/03#F17 · Low · The tender envelope is tied to lot 1 only
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderPreparation/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderPreparation/cbc:Description` = `One encrypted envelope per tender.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderPreparation/cac:DocumentTenderRequirement/cbc:Description` = `Unit prices per lot.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric` = `2`
- Why: The only `TenderPreparation` names lot 1 as the lot it applies to, while its texts speak of "one encrypted envelope per tender" and "unit prices per lot" and a tenderer may tender for both lots. Nothing says how a tender for lot 2 is prepared.
- Condition: The tender preparation covers every lot a tender can be submitted for (no lot named, both lots named, or one preparation per lot).
- Options: (a) Preferred: remove the lot from the preparation, since the envelope rule is the same for both. (b) Name both lots.
- Needs decision: no

### tender/03#F18 · Low · Quality criterion: a range in years without explanation, and one sub-criterion of half the weight
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:WeightNumeric` = `40`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MaximumQuantity` = `10`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:Name` = `Durability of the coating`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric` = `20`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:WarrantyValidityPeriod/cbc:DurationMeasure` = `5`
- Why: `MinimumQuantity` and `MaximumQuantity` are "the minimum/maximum quantity for an awarding criterion". The criterion "Quality" has no description and does not say what is counted in years from 5 to 10; presumably the warranty offered (the required warranty is 5 years), but then the range belongs to a warranty criterion, not to "Quality" as a whole. Its only sub-criterion, "Durability of the coating", weighs 20 of the 40 points; the other 20 are not assigned.
- Condition: The quality criterion says what its quantity range measures, and its sub-criteria add up to its weight.
- Options: (a) Preferred: two sub-criteria (coating durability 20, warranty years 20, the latter with the 5–10 year range) and a description. (b) Remove the range and the single sub-criterion.
- Needs decision: no

### tender/03#F19 · Low · The additional classification is the parent group of the main one, and the installation is not classified at project level
- XPath: `/CallForTenders/cac:ProcurementProject/cac:MainCommodityClassification/cbc:ItemClassificationCode` = `38111`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:MainCommodityClassification/cbc:ItemClassificationCode` = `87390`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- Why: `AdditionalCommodityClassification` is "an association to additional classification categories for the deliverable requested". CPC 381 "Furniture" is the group that contains the main class 38111 "Seats, primarily with metal frames"; it adds no further category. The second deliverable of the project, the installation (lot 2), is not classified at project level although lot 2 itself carries CPC 87390; lot 2 in turn lists "Furniture" as an additional category of an installation service.
- Condition: Additional classifications name categories the main one does not already imply; a project with a supply lot and an installation lot shows both.
- Options: (a) Preferred: 87390 as the additional classification of the project; no "Furniture" on lot 2. (b) Remove the additional classification.
- Needs decision: no

### tender/03#F20 · Low · Eight further roles all filled with the contracting party itself
- XPath: `/CallForTenders/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AdditionalInformationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ContractResponsibleParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderEvaluationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:QualificationRequestRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The contracting party is repeated as originator ("a party who originated Order"), beneficiary, and in six roles of the tendering terms (additional information, document provider, tender recipient, contract responsible, evaluation, qualification request recipient). These roles exist for the case that another body does the task (a central purchasing body, another department as beneficiary, a platform operator). Where the contracting party does everything itself, the repetitions say nothing the `ContractingParty` does not say, and they suggest eight distinct roles in a procedure that has one actor. The parks department that the benches are for ("Head of parks" sits on the committee) would be a real originator or beneficiary, if it is a body of its own.
- Condition: A role party is present where a party other than the contracting party fills the role, or where the receiver needs the role's own contact data (e.g. where tenders are received).
- Options: (a) Preferred: keep `TenderRecipientParty` and `AdditionalInformationParty` if they get their own contact (platform, helpdesk); remove the rest. (b) Keep all as an explicit statement and accept the repetition.
- Needs decision: yes

### tender/03#F21 · Low · Customs trader number of the contracting party in a tendering document
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- Why: The call for tenders identifies the department also by its customs trader number, and the receiving operator by its own. Nothing in this document is declared to customs; the number is used only when the benches are imported (31). It looks copied from the party's master data into a document that does not use it.
- Condition: A party carries the identifiers the document uses or that the receiver needs to identify it; no customs number in a procurement notice or call.
- Options: (a) Preferred: leave the customs trader number to the customs and transport documents. (b) Keep it if the world's rule is that every document carries all identifiers of a party; then the rule should be stated.
- Needs decision: no

### tender/03#F22 · Low · Values that only state the default: normal urgency, no reduction of candidates, not terminated
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:UrgencyCode` = `NORMAL`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:TerminatedIndicator` = `false`
- Why: `UrgencyCode` `NORMAL` says the procedure is not urgent; `CandidateReductionConstraintIndicator` `false` ("the number of candidates participating in this process has been reduced (true) or not") says nothing was reduced, in an open procedure that has no candidates to reduce; `TerminatedIndicator` `false` ("the competition launched is terminated") says a procedure that is just being announced is not over. Each states what its absence implies (UBL IND6, CLAUDE.md "nothing implied by absence").
- Condition: The tendering process carries these elements only where they say something that differs from the default.
- Options: (a) Preferred: remove the three. (b) None other seen.
- Needs decision: no

### tender/03#F23 · Low · Lot-level tendering terms and process that only say "As for the procedure."
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- Why: `ProcurementProjectLot/TenderingTerms` and `ProcurementProjectLot/TenderingProcess` are the "tendering terms/process for this procurement project lot", for what differs per lot. Four aggregates each hold one sentence saying that nothing differs. They have no business content (no fillers).
- Condition: A lot carries tendering terms or a tendering process only where something is specific to the lot.
- Options: (a) Preferred: remove the four aggregates. (b) Put real lot-specific terms there (e.g. the guarantee per lot, or that the auction covers the unit prices of each lot separately).
- Needs decision: no

### tender/03#F24 · Low · Lot 2 (installation) is described with the data of the bench supply
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:EstimatedOverallContractQuantity` = `240`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cbc:OptionsDescription` = `One extension of a year with 120 more benches.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`
- Why: The lot "Installation of the benches" has the description of the whole project ("240 steel park benches with hardwood slats …, delivered and anchored"), a quantity of 240 "each" without saying of what, and the option "120 more benches". For an installation service the reader expects what is installed where: 240 installations (anchoring) and, in the extension, 120 more. Lot 2 has no request-for-tender line of its own; lot 1's line includes the ground anchor sets.
- Condition: The description, quantity and option of lot 2 describe the installation service, not the supply of lot 1.
- Options: (a) Preferred: a description such as "Anchoring of 240 benches in the parks of Lumeport over two years" and a request-for-tender line for the installation. (b) Leave only name, type, classification and amounts on the lot.
- Needs decision: no

### tender/03#F25 · Low · A street address as the place of an electronic opening
- XPath: `/CallForTenders/cac:TenderingProcess/cac:OpenTenderEvent/cbc:Description` = `Electronic opening; tenderers may follow it online.`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:OpenTenderEvent/cac:OccurrenceLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:SubmissionMethodCode` = `ELECTRONIC`
- Why: The opening is electronic and followed online; tenders are submitted electronically. The event nevertheless has a physical location, named by the party and its square ("the name is the place, not the company"), and no address of the online session. It is not clear whether anyone can attend at Civic Square.
- Condition: The location of the opening is where it can be attended: the URI of the online session, or a room if it is public on site, and the name names that place.
- Options: (a) Preferred: remove the location and give the platform address in the description. (b) Name the room and say that attendance on site is possible.
- Needs decision: no

### tender/03#F26 · Low · The receiving operator comes with its logistics provider and tax data
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: `ReceiverParty` is the party receiving the call for tenders, here one interested operator. Its description includes `ServiceProviderParty` ("a party providing a service to this party"): its warehouse and despatch contractor Castrano Logistics with a contract number and a "key account desk". The contracting party cannot know, and the call for tenders does not use, who will despatch the goods of an operator that has not yet tendered; the same holds for the receiver's tax scheme and customs number. This is the operator's master data in a document written by the buyer.
- Condition: The receiver of the call for tenders is identified (ID, name, address or electronic address); no service providers or tax data of the receiver.
- Options: (a) Preferred: reduce the receiver to identification, name and electronic address. (b) None other seen.
- Needs decision: no

### tender/03#F27 · Low · "Legal document" is a department document at the top and the Procurement Act in the lots
- XPath: `/CallForTenders/cac:LegalDocumentReference/cbc:ID` = `PWD-LEGAL-26`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:LegalDocumentReference/cbc:ID` = `XB-PPA-2019`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:LegalDocumentReference/cbc:ID` = `XB-PPA-2019`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ProcurementLegislationDocumentReference/cbc:ID` = `XB-PPA-2019`
- XPath: `/CallForTenders/cac:TechnicalDocumentReference/cbc:ID` = `PWD-SPEC-BENCH-26`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:TechnicalDocumentReference/cbc:ID` = `PWD-SPEC-LOT-1`
- Why: In a call for tenders the legal document is the document with the legal (administrative) conditions of the procedure, next to the technical one; at the top it is `PWD-LEGAL-26`. Both lots name the Public Procurement Act itself as their legal document, which is legislation and is already referenced as such in `ProcurementLegislationDocumentReference`. The same element thus points to two different kinds of thing, and the lots do not say which conditions document applies to them. (The technical references are consistent: one specification for the benches, one per lot.)
- Condition: The legal document reference of a lot points to the conditions document that applies to the lot, or is absent when the top-level one applies.
- Options: (a) Preferred: remove the lot-level legal references. (b) Point them to `PWD-LEGAL-26`.
- Needs decision: no

## Checked and consistent
- Lots and amounts: the project estimate 124080.00 is the sum of the lot estimates of 02/03 (119760.00 + 4320.00); the request-for-tender line (240 × 499 = 119760.00) and the unit price bounds 350–600 agree with the price criterion's `MinimumAmount`/`MaximumAmount`.
- `WeightingAlgorithmCode` WSUM, description "Price 60 %, quality 40 %" and the criterion weights 60 and 40 agree; `AwardingMethodTypeCode` BESTVALUE fits two weighted criteria.
- `PaymentFrequencyCode` PERRELEASE agrees with the payment terms ("30 days after each accepted release") and with the framework of 02/03 ("Releases every few months").
- `RecurringProcurementIndicator` true, "about four years" and `EstimatedTimingFurtherPublication` 2030 agree with the planned period (to 2028-03-22) plus one extension of a year.
- `PostAwardProcess`: catalogue, order, invoice and payment are indeed electronic in the flow (25, 26, 32, 36).
- `RequiredItemLocationQuantity/LeadTimeMeasure` of 10 days fits the first delivery (order 26 issued 2026-03-23, `RequestedDeliveryDate` 2026-04-02).
- `OtherConditionsIndicator` true has its `AdditionalConditions`; `RequiredCurriculaIndicator` true has its `RequiredCurriculaCode`.
- `ContractExtension`: one renewal of 12 months with 120 benches, renewal amount = half of the estimate; `MaximumNumberNumeric` 1 and `RenewalsIndicator` true agree.

## Considered and refuted
- `/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode`: a code without `listID` was suspected — refuted for this lens because `PARKS-26` is the department's own programme number (party-internal codes are exempt from the listID rule, CLAUDE.md), and it matches `FundingProgram`.
- `/CallForTenders/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric` and `cbc:MaximumLotsAwardedNumeric` (both 2 of 2 lots): suspected to say nothing — refuted because they are the explicit statement that a tenderer may tender for and win both lots, which `GroupingLots` ("Lots 1 and 2 may be awarded together.") builds on.
- `/CallForTenders/cac:ProcurementProject/cbc:RequestedDeliveryDate` = 2026-04-02 in a two-year project: suspected not to be "the" delivery date — refuted because it is the first release and equals the start of the delivery period of the request-for-tender line.
- `/CallForTenders/cac:ProcurementProject/cbc:ProcurementSubTypeCode` = PURCHASE: the definition speaks of "the subcategory of the type of work"; suspected misuse — refuted because purchase (as against lease or rental) is a sub-type of a supply contract and the definition's examples are only examples.
- `/CallForTenders/cac:ProcurementProject/cbc:SMESuitableIndicator` = true against a required turnover of 250000 lume and 10 employees: suspected contradiction — refuted, a firm of that size is still a small enterprise.
- `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:OperatingYearsQuantity` and `cbc:EmployeeQuantity`: the model prints the definition of another element ("Textual description of the legal form …") for both, as for `PriceEvaluationCode`; suspected misuse — refuted, the element names say what they are and the values (3 years, 10 persons) fit; the definitions are an error of the UBL model, not of the example.
- `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealInformationParty`: suspected wrong party (the review board "presents the information for the appeal") — refuted, the board that hears appeals is the natural source of information on them.
- `/CallForTenders/cac:TenderingTerms/cac:ContractResponsibleParty`: "the Party who executes the Contract" could mean the contractor — refuted as a wrong party, since in the procurement documents it is the body that concludes and manages the contract; it is kept only in the finding on repeated roles.
- `/CallForTenders/cac:TenderingProcess/cbc:GovernmentAgreementConstraintIndicator` = true: suspected to assert the real WTO Government Procurement Agreement for fictional countries — refuted, the definition says "a government procurement agreement", which the Lumeport Trade Accord can be.
- `/CallForTenders/cac:TenderingProcess/cac:ProcessJustification` (STANDARD, "Value above the threshold for open procedures."): suspected filler, since justifications are usually given for exceptional procedures — refuted, the definition is "a justification for the selection of this tendering process" and the text gives a real reason.
- `/CallForTenders/cac:TenderingProcess/cac:FrameworkAgreement/cbc:ExpectedOperatorQuantity` and `cbc:MaximumOperatorQuantity` (both 1): suspected redundant — refuted, they agree with "Framework with one supplier." and with the single award of the flow.
- `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid`: checked against the auction — consistent with `AuctionTerms/ConditionsDescription` ("by at least the minimum step of the price criterion").
- `/CallForTenders/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = 2026-01-26 before the issue date 2026-02-12: suspected date conflict as in 02 — refuted for this document, because this instance is the copy sent to one operator (`ReceiverParty` Valdara Industries) on its request, approved on 2026-01-25 and available since 2026-01-26.
- `/CallForTenders/cac:OriginatorCustomerParty`: the model defines it here as "the party who originated Order", which does not fit a call for tenders — the wording is the model's; the role is covered by the finding on repeated roles.

## Outside this review
- `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersLineReference/cbc:LineID` refers to line 2 of this call for tenders; its request-for-tender lines are `1` and the sub-line `1.1` (project and lot 1). The problem lies in the catalogue.
- Whether an operator in Urvania could receive the documents on 2026-02-12 and tender by 2026-02-25 with a bank guarantee of 2026-02-24 is a timeline question across documents.
