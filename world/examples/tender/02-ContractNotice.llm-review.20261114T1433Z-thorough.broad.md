# LLM review: 02-ContractNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/02-ContractNotice.xml`, Git blob `1902067078eeb7c2dc70b632a4e813bb3c440b21` (committed)
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

### tender/02#F1 · High · Periods of the procedure lie before the document was issued
- XPath: `/ContractNotice/cbc:IssueDate` = `2026-02-11`
- XPath: `/ContractNotice/cbc:RequestedPublicationDate` = `2026-01-27`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: The contract notice is issued on 2026-02-11. Its requested publication date ("The requested publication date for this Contract Notice") is 2026-01-27, two weeks before it was issued. The documents are said to be available from 2026-01-26, the period for submitting invitations ended on 2026-02-01, and the periods for the invitation to participate and for receiving requests to participate end on 2026-02-11, the day of issue. The dates fit a publication on 2026-01-26 (the date `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-01-26` planned for the contract notice), not the issue date. The rest of the flow follows the issue date: the expression of interest 04 that answers the contract notice is of 2026-02-14, the tenders are of 2026-02-23 to 02-25.
- Condition: No period in which economic operators must act ends before or on the day the document that announces it is issued; a requested publication date is not before the issue date.
- Options: (a) move the periods (and the requested publication date) after the issue date (preferred, the rest of the flow depends on the issue dates); (b) issue contract notice and call for tenders on 2026-01-26 and shift what depends on it.
- Needs decision: yes

### tender/02#F2 · High · A latest date for security clearance although no clearance is required
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: LatestSecurityClearanceDate is "The end date until which the candidates can obtain the necessary level of security clearance." The same tendering terms say that no clearance is required, because parks are public places. The date contradicts that and has no business reason (CLAUDE.md: no fillers). The same pair occurs in 4 examples (grep for `LatestSecurityClearanceDate` over `world/examples/*/*.xml`: tender 01, 02, 03, 24).
- Condition: The tendering terms do not carry both a latest security clearance date and a statement that no clearance is required.
- Options: (a) remove LatestSecurityClearanceDate (preferred); (b) make a clearance required and say for what.
- Needs decision: no

### tender/02#F3 · High · Replaced notice and call for tenders referenced under IDs no document carries
- XPath: `/ContractNotice/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/ContractNotice/cbc:ID` = `LPWD-DOC-26-0188`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`
- Why: ReplacedNoticeDocumentReference is "A class defining a reference to the notice that is being replaced"; CallForTendersDocumentReference "A reference to a Call for Tender associated with these tendering terms." No document of the flow has the ID `PWD-2026-PARKS-PIN` or `PWD-2026-PARKS-CFT`. The prior information notice is `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187` (and the same document refers to it correctly under that ID in NoticeDocumentReference); the call for tenders is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`, issued a day after this notice. Moreover a contract notice does not replace a prior information notice: the prior information notice announced it. 25-Catalogue.xml refers to the call for tenders as `LPWD-DOC-26-0189`, so the flow uses two IDs for the same document.
- Condition: Every reference to a notice or to the call for tenders uses the ID of the document meant; a replaced notice is named only when a notice is in fact replaced.
- Options: (a) remove ReplacedNoticeDocumentReference, and give CallForTendersDocumentReference the ID of 03 (preferred); (b) keep one "procedure-level" ID for the call for tenders throughout the flow and carry it in 03.
- Needs decision: yes

### tender/02#F4 · High · Lot 2 is a service here and works in the prior information notice
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the park benches`
- Why: The same lot `LOT-2` of the same procedure is classified as works in the prior information notice and as services (sub-type INSTALL, CPC 87390 installation services) here, in 03 and in 21, and its name differs. The nature of a lot (works or services) decides thresholds and rules and does not change between the advance notice and the notice.
- Condition: Lot 2 has the same name and the same procurement type in every document of the flow.
- Options: (a) services and "Installation of the benches" in 01 as well (preferred: three documents say so); (b) works everywhere.
- Needs decision: no

### tender/02#F5 · Medium · Variants limited to one, but the indicator says their number is unconstrained
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- Why: VariantConstraintIndicator is "An indicator that variants are allowed and unconstrained in number (true) or not allowed (false)." MaximumVariantQuantity limits them to one. By the definition `true` says the number is unconstrained.
- Condition: The indicator and the maximum do not contradict each other.
- Options: (a) drop the indicator and keep VariantConstraintCode `ALLOWED` with the maximum (preferred); (b) drop the maximum.
- Needs decision: no

### tender/02#F6 · Medium · Periods of a restricted procedure in an open procedure
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `false`
- Why: InvitationSubmissionPeriod is "The period during which invitations to tender must be completed and delivered", ParticipationInvitationPeriod "The period during which the invitation to participate must be sent", ParticipationRequestReceptionPeriod "The period during which requests for participation must be completed and delivered". In an open procedure any operator may tender directly; there are no requests to participate and no invitations (own knowledge of procurement practice). Either these periods have no business reason, or the procedure is not open: the flow does contain an expression of interest (04, 05) and a qualification application (06, 07) before the tenders, which is the pattern of a restricted procedure.
- Condition: The periods stated fit the procedure type: an open procedure has no invitation and participation-request periods, a two-stage procedure is not called open.
- Options: (a) remove the three periods and CandidateReductionConstraintIndicator (preferred if the procedure is open); (b) make it a restricted procedure, consistent with 04 to 07.
- Needs decision: yes

### tender/02#F7 · Medium · Identifier of an "original" framework agreement although nothing is reopened
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`
- Why: OriginalContractingSystemID is "When reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system." This procedure sets up a new framework agreement (`FW-1`); it does not reopen competition under an existing one, and no framework `PWD-FW-2024-PARKS` occurs anywhere else (grep over `world/examples/*/*.xml`: only tender 02, 03, 21).
- Condition: OriginalContractingSystemID is present only in a reopening of competition under an existing framework or system.
- Options: (a) remove it (preferred); (b) if a 2024 framework is the predecessor, say so in a note instead.
- Needs decision: no

### tender/02#F8 · Medium · Fee for paper copies in the element for the reimbursement fee of concessions
- XPath: `/ContractNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: RequiredFeeAmount is "The amount of the reimbursement fee for concession procurement projects" and FeeDescription "Text describing the reimbursement fee for concession procurement projects." This is a supply contract, not a concession; the 50 lume are the price of paper copies, which DocumentationFeeAmount ("The amount to be paid to obtain the contract documents and additional documentation") already states. Repeated on the project and on both lots, it reads as three fees.
- Condition: No concession fee is stated for a procurement that is not a concession; the documentation fee is stated once, in DocumentationFeeAmount.
- Options: (a) remove RequiredFeeAmount and FeeDescription from the project and the lots (preferred); (b) none other seen.
- Needs decision: no

### tender/02#F9 · Medium · A strategic-procurement code in ProcurementTypeCode
- XPath: `/ContractNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- Why: ProcurementTypeCode is "A code signifying the type of procurement project (e.g., goods, works, services)". `GREEN` (list StrategicProcurementCode, "Environmental impact") is a policy goal, not a type of procurement. eForms uses the element this way (own knowledge); by the repository's rule on semantic conformance that practice does not change the UBL meaning. On lot 2, the installation, the text "recycled steel and certified timber are asked" does not apply at all.
- Condition: ProcurementAdditionalType carries a type of procurement (goods, works, services), or the environmental aim is carried elsewhere (the contract execution requirement already states it).
- Options: (a) remove it, or state the additional type that applies (preferred); (b) keep it and record it as a finding on eForms practice.
- Needs decision: yes

### tender/02#F10 · Medium · Language code in LocaleCode
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/02#F11 · Low · Lot 2, the installation, carries the description, quantity, classification and options of the benches
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:EstimatedOverallContractQuantity` = `240`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cbc:OptionsDescription` = `One extension of a year with 120 more benches.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- Why: A lot's ProcurementProject is "A description of the procurement project to be divided", i.e. of that lot. Lot 2 is an installation service (CPC 87390), but its description, its additional classification (381 Furniture) and its option text are those of the whole project; both lots have the same description, which covers delivery (lot 1) and anchoring (lot 2) together. Lot 1 in turn contains the sub-line "Ground anchor set", while its estimate (119 760.00 = 240 × 499) leaves out the 4 320.00 that is the estimate of lot 2, so it is not clear whether the anchors belong to lot 1 or lot 2.
- Condition: Each lot describes what that lot buys (benches; installation), with its own quantity unit, classification and option text; it is clear in which lot the ground anchors are.
- Options: (a) give each lot its own description and drop from lot 2 what belongs to the benches (preferred); (b) describe the lots only by name and amount and leave the rest on the project.
- Needs decision: no

### tender/02#F12 · Low · Lot-level terms and process that only say "As for the procedure."
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- Why: The two aggregates per lot exist only to say that nothing differs from the procedure, which is what their absence means. That is a filler (CLAUDE.md: no fillers, nothing implied by absence).
- Condition: A lot carries tendering terms or a tendering process only where they differ from the procedure's.
- Options: (a) remove them (preferred); (b) give the lots a real difference (e.g. the references required only for lot 2).
- Needs decision: no

### tender/02#F13 · Low · Maximum advertised value of 500 lume against an estimate of 124 080
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- Why: MaximumAdvertisementAmount is "The maximum advertised monetary value of the tendering process." Read by that definition, 500 lume contradicts the estimate. The value looks like the maximum cost of publishing the notices to be borne by the successful tenderer (the meaning in the Spanish CODICE model the element comes from; own knowledge), which the UBL definition does not say, and nothing in the document explains it.
- Condition: The amount fits the definition, or the element is absent.
- Options: (a) remove it (preferred); (b) keep it as advertising cost with a note and record the unclear UBL definition as a finding.
- Needs decision: yes

### tender/02#F14 · Low · Guarantee of 2 400 is not 2 % of any stated amount
- XPath: `/ContractNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: AmountRate is "The rate used to calculate the amount of liability in this financial guarantee." 2 % of 124 080.00 is 2 481.60; of the bench line 119 760.00 it is 2 395.20; 2 400.00 is 2 % of 120 000, which the document does not state. Probably rounded, but neither base nor rounding is said. The guarantee issued (14-GuaranteeCertificate.xml) is for the same 2 400.00.
- Condition: Rate × base = liability amount for a stated base, or the description says what the amount is rounded from.
- Options: (a) say in the description what the 2 % is taken of and that it is rounded (preferred); (b) set the amount to the calculated value.
- Needs decision: no

### tender/02#F15 · Low · "At least twice" coded as "greater than"
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- Why: "At least" is ≥; `GT` ("Greater than") and "Turnover > 2 × estimate" exclude a turnover of exactly the threshold. Also 2 × 124 080.00 = 248 160.00, not 250 000.00 (rounded up, not said).
- Condition: Description, expression code and expression state the same comparison.
- Options: (a) a "greater than or equal" code and expression if the list has one (preferred); (b) change the description to "more than".
- Needs decision: no

### tender/02#F16 · Low · The tenderer is required to lead a consortium
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Any legal form; consortia must name a lead member.`
- Why: Within a TendererQualificationRequest ("Required set of qualifications for a tenderer") the EconomicOperatorRole states the role the set applies to. As written, the requirements apply to consortium leads only, while any legal form may tender and the tenderers of the flow (Valdara Industries, Brackenmere Furniture) tender alone.
- Condition: The role of the qualification request matches who must meet it, or is absent.
- Options: (a) remove the role (preferred); (b) a role that covers sole tenderers and lead members.
- Needs decision: no

### tender/02#F17 · Low · Contest and other "false" indicators without a case
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:TerminatedIndicator` = `false`
- Why: FollowupContractIndicator "Indicates if any service contract following the contest will be awarded to the winner…", PrizeIndicator whether a prize will be awarded: both belong to design contests, and this is a supply procedure. TerminatedIndicator is "An indicator that the competition launched is terminated"; in the document that launches the competition `false` says nothing. These are fillers (CLAUDE.md: no fillers, nothing implied by absence).
- Condition: Indicators that cannot apply to this procedure, or that only state the obvious negative, are absent.
- Options: (a) remove them (preferred); (b) none other seen.
- Needs decision: no

### tender/02#F18 · Low · Quality criterion with a range of 5 to 10 years and no explanation
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MaximumQuantity` = `10`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric` = `20`
- Why: The criterion "Quality" (weight 40) has a minimum and maximum quantity in years but no description or expression; its only sub-criterion, "Durability of the coating", has weight 20, the other 20 are not described. A tenderer cannot tell what the years measure (probably the warranty offered; the required warranty is 5 years).
- Condition: The criterion says what is scored between 5 and 10 years, and its sub-criteria account for its weight.
- Options: (a) add a description and the missing sub-criterion (preferred); (b) remove the quantities.
- Needs decision: no

### tender/02#F19 · Low · Funding programme code without a list
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26`
- Why: The agreed rule is that every code has a listID (except party-internal codes). `PARKS-26` has none.
- Condition: The code names its list, or the programme is given as text only.
- Options: (a) add the city's list of programmes as listID (preferred); (b) keep only `cbc:FundingProgram`.
- Needs decision: no

### tender/02#F20 · Low · Contact of the review board described as a procurement officer
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: AppealReceiverParty is "The Party who receives the appeal.". Its contact is the registry of the Procurement Review Board, which receives appeals; a registry clerk of a review body is not a "Procurement officer" in a department "Procurement" (that is the contact of a buyer). Name, job title and department do not agree.
- Condition: Job title and department of the contact fit a registry that receives appeals.
- Options: (a) e.g. job title "Registrar", department "Registry" (preferred); (b) drop job title and department.
- Needs decision: no

### tender/02#F21 · Low · A public body described as a company in a commercial register
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department, Bayvarra Information Service, Procurement Review Board of Bayvarra. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/02#F22 · Low · The department's tax exemption reason describes a sale
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: nothing reported as wrong.
- TenderingTerms equal those of 01 leaf for leaf, plus AppealReceiverParty and MediationParty; ProcurementProject equals that of 01 (compared with a script over the leaf values).
- Amounts: lot 1 119 760.00 (= 240 × 499) + lot 2 4 320.00 (= 240 × 18) = 124 080.00, the project estimate; lot minimum = half, lot maximum = 1.2 ×; average subsequent contract 19 960 + 720 = 20 680 = 124 080 / 6; renewal 59 880 + 2 160 = 62 040.
- Framework: EstimatedMaximumValueAmount 148 896.00 = 1.2 × 124 080 = the project's MaximumAmount; MaximumValueAmount 186 120.00 = 124 080 + 62 040 (one renewal); duration 24 months = planned period 2026-03-23 to 2028-03-22; one operator expected and at most, matching "Framework with one supplier."
- Tender deadline 2026-02-26 12:00, guarantee to be constituted by 2026-02-26, opening event `OPEN-1` on 2026-02-26 14:00 (after the deadline, scheduled, not completed) and referenced by TenderPreparation/OpenTenderID; questions until 2026-02-19, documents until 2026-02-25.
- NoticeDocumentReference `LPWD-DOC-26-0187` is the ID of 01-PriorInformationNotice.xml. FrequencyPeriod 4 years agrees with "A next procedure in about four years." and `2030`.
- The auction terms agree with MinimumImprovementBid of the price criterion (minimum step 2 lume) and with the award criteria (only the price score changes).
- CPC 87390 "Installation services of other goods n.e.c." fits lot 2; ISIC 8423 fits a review board.

## Considered and refuted
- `/ContractNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount`: "including options and renewals" should include the renewal of 62 040, but 148 896 does not — refuted because the estimate may be the expected spend (base contract with its 20 % tolerance) and the maximum (186 120) the ceiling with the renewal; both readings are possible.
- `/ContractNotice/cac:TenderingProcess/cbc:GovernmentAgreementConstraintIndicator`: `true` without saying which agreement — refuted because the Lumeport Trade Accord covers procurement between the three countries and tenderers from Urvania take part.
- `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:MediationParty`: the review board is both the body that receives appeals and the mediator — refuted because a review body may offer mediation; nothing in the document contradicts it.
- `/ContractNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate`: `Rate` and `MaximumPercent` both 30 with an amount of 4 320 — refuted because the amount (the installation estimate) lies under the maximum; redundant, not contradictory.
- `/ContractNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:Contact`: contact with a name only — refuted because the department's procurement office is fully described as the contracting party's contact.
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` is not an ISO 8601 offset — refuted because the element is text and the world's time zone is fictional.
- `/ContractNotice/cac:AdditionalNoticeLanguage/cbc:ID`: Urvanian as additional language — refuted because Urvanian tenderers take part under the Trade Accord.

## Outside this review
- Whether the notice should be issued only one day before the call for tenders and 15 days before the tender deadline is a timeline question of the flow.
