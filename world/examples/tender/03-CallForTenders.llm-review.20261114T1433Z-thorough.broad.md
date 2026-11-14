# LLM review: 03-CallForTenders.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

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

### tender/03#F1 · High · Periods of the procedure lie before the document was issued
- XPath: `/CallForTenders/cbc:IssueDate` = `2026-02-12`
- XPath: `/CallForTenders/cbc:ApprovalDate` = `2026-01-25`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: The call for tenders is issued on 2026-02-12. The documents are said to be available from 2026-01-26, the period for submitting invitations ended on 2026-02-01, and the periods for the invitation to participate and for receiving requests to participate end on 2026-02-11, the day before issue. The dates fit a publication on 2026-01-26 (the date `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-01-26` planned for the contract notice), not the issue date. The rest of the flow follows the issue date: the expression of interest 04 that answers the contract notice is of 2026-02-14, the tenders are of 2026-02-23 to 02-25.
- Condition: No period in which economic operators must act ends before or on the day the document that announces it is issued; a requested publication date is not before the issue date.
- Options: (a) move the periods (and the requested publication date) after the issue date (preferred, the rest of the flow depends on the issue dates); (b) issue contract notice and call for tenders on 2026-01-26 and shift what depends on it.
- Needs decision: yes

### tender/03#F2 · High · A latest date for security clearance although no clearance is required
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: LatestSecurityClearanceDate is "The end date until which the candidates can obtain the necessary level of security clearance." The same tendering terms say that no clearance is required, because parks are public places. The date contradicts that and has no business reason (CLAUDE.md: no fillers). The same pair occurs in 4 examples (grep for `LatestSecurityClearanceDate` over `world/examples/*/*.xml`: tender 01, 02, 03, 24).
- Condition: The tendering terms do not carry both a latest security clearance date and a statement that no clearance is required.
- Options: (a) remove LatestSecurityClearanceDate (preferred); (b) make a clearance required and say for what.
- Needs decision: no

### tender/03#F3 · High · Replaced notice and call for tenders referenced under IDs no document carries
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`
- Why: ReplacedNoticeDocumentReference is "A class defining a reference to the notice that is being replaced"; CallForTendersDocumentReference "A reference to a Call for Tender associated with these tendering terms." No document of the flow has the ID `PWD-2026-PARKS-PIN` or `PWD-2026-PARKS-CFT`. The prior information notice is `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187` (and the same document refers to it correctly under that ID in NoticeDocumentReference); this call for tenders itself has the ID `LPWD-DOC-26-0189`, so it refers to itself under another ID. Moreover a call for tenders does not replace a prior information notice: the prior information notice announced it. 25-Catalogue.xml refers to the call for tenders as `LPWD-DOC-26-0189`, so the flow uses two IDs for the same document.
- Condition: Every reference to a notice or to the call for tenders uses the ID of the document meant; a replaced notice is named only when a notice is in fact replaced.
- Options: (a) remove ReplacedNoticeDocumentReference, and give CallForTendersDocumentReference the ID of 03 or drop it from the call for tenders itself (preferred); (b) keep one "procedure-level" ID for the call for tenders throughout the flow and carry it in 03.
- Needs decision: yes

### tender/03#F4 · Medium · Variants limited to one, but the indicator says their number is unconstrained
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- Why: VariantConstraintIndicator is "An indicator that variants are allowed and unconstrained in number (true) or not allowed (false)." MaximumVariantQuantity limits them to one. By the definition `true` says the number is unconstrained.
- Condition: The indicator and the maximum do not contradict each other.
- Options: (a) drop the indicator and keep VariantConstraintCode `ALLOWED` with the maximum (preferred); (b) drop the maximum.
- Needs decision: no

### tender/03#F5 · Medium · Periods of a restricted procedure in an open procedure
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `false`
- Why: InvitationSubmissionPeriod is "The period during which invitations to tender must be completed and delivered", ParticipationInvitationPeriod "The period during which the invitation to participate must be sent", ParticipationRequestReceptionPeriod "The period during which requests for participation must be completed and delivered". In an open procedure any operator may tender directly; there are no requests to participate and no invitations (own knowledge of procurement practice). Either these periods have no business reason, or the procedure is not open: the flow does contain an expression of interest (04, 05) and a qualification application (06, 07) before the tenders, which is the pattern of a restricted procedure.
- Condition: The periods stated fit the procedure type: an open procedure has no invitation and participation-request periods, a two-stage procedure is not called open.
- Options: (a) remove the three periods and CandidateReductionConstraintIndicator (preferred if the procedure is open); (b) make it a restricted procedure, consistent with 04 to 07.
- Needs decision: yes

### tender/03#F6 · Medium · Identifier of an "original" framework agreement although nothing is reopened
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`
- Why: OriginalContractingSystemID is "When reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system." This procedure sets up a new framework agreement (`FW-1`); it does not reopen competition under an existing one, and no framework `PWD-FW-2024-PARKS` occurs anywhere else (grep over `world/examples/*/*.xml`: only tender 02, 03, 21).
- Condition: OriginalContractingSystemID is present only in a reopening of competition under an existing framework or system.
- Options: (a) remove it (preferred); (b) if a 2024 framework is the predecessor, say so in a note instead.
- Needs decision: no

### tender/03#F7 · Medium · Fee for paper copies in the element for the reimbursement fee of concessions
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: RequiredFeeAmount is "The amount of the reimbursement fee for concession procurement projects" and FeeDescription "Text describing the reimbursement fee for concession procurement projects." This is a supply contract, not a concession; the 50 lume are the price of paper copies, which DocumentationFeeAmount ("The amount to be paid to obtain the contract documents and additional documentation") already states. Repeated on the project and on both lots, it reads as three fees.
- Condition: No concession fee is stated for a procurement that is not a concession; the documentation fee is stated once, in DocumentationFeeAmount.
- Options: (a) remove RequiredFeeAmount and FeeDescription from the project and the lots (preferred); (b) none other seen.
- Needs decision: no

### tender/03#F8 · Medium · A strategic-procurement code in ProcurementTypeCode
- XPath: `/CallForTenders/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- Why: ProcurementTypeCode is "A code signifying the type of procurement project (e.g., goods, works, services)". `GREEN` (list StrategicProcurementCode, "Environmental impact") is a policy goal, not a type of procurement. eForms uses the element this way (own knowledge); by the repository's rule on semantic conformance that practice does not change the UBL meaning. On lot 2, the installation, the text "recycled steel and certified timber are asked" does not apply at all.
- Condition: ProcurementAdditionalType carries a type of procurement (goods, works, services), or the environmental aim is carried elsewhere (the contract execution requirement already states it).
- Options: (a) remove it, or state the additional type that applies (preferred); (b) keep it and record it as a finding on eForms practice.
- Needs decision: yes

### tender/03#F9 · Medium · Language code in LocaleCode
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/03#F10 · Medium · A province in Region
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division of the country, for which CountrySubentity exists ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the flow do use CountrySubentity for their state. The same value is in 22 of the 36 examples of the flow (grep for `Province of Ferrano` over the `*.xml` of the flow, files counted).
- Condition: The province is in CountrySubentity (with its code where the country has one); Region is used only for a region that is not an administrative division.
- Options: (a) move the province to CountrySubentity (preferred); (b) none other seen.
- Needs decision: no

### tender/03#F11 · Low · Lot 2, the installation, carries the description, quantity, classification and options of the benches
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:EstimatedOverallContractQuantity` = `240`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cbc:OptionsDescription` = `One extension of a year with 120 more benches.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- Why: A lot's ProcurementProject is "A description of the procurement project to be divided", i.e. of that lot. Lot 2 is an installation service (CPC 87390), but its description, its additional classification (381 Furniture) and its option text are those of the whole project; both lots have the same description, which covers delivery (lot 1) and anchoring (lot 2) together. Lot 1 in turn contains the sub-line "Ground anchor set", while its estimate (119 760.00 = 240 × 499) leaves out the 4 320.00 that is the estimate of lot 2, so it is not clear whether the anchors belong to lot 1 or lot 2.
- Condition: Each lot describes what that lot buys (benches; installation), with its own quantity unit, classification and option text; it is clear in which lot the ground anchors are.
- Options: (a) give each lot its own description and drop from lot 2 what belongs to the benches (preferred); (b) describe the lots only by name and amount and leave the rest on the project.
- Needs decision: no

### tender/03#F12 · Low · Lot-level terms and process that only say "As for the procedure."
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- Why: The two aggregates per lot exist only to say that nothing differs from the procedure, which is what their absence means. That is a filler (CLAUDE.md: no fillers, nothing implied by absence).
- Condition: A lot carries tendering terms or a tendering process only where they differ from the procedure's.
- Options: (a) remove them (preferred); (b) give the lots a real difference (e.g. the references required only for lot 2).
- Needs decision: no

### tender/03#F13 · Low · Maximum advertised value of 500 lume against an estimate of 124 080
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- Why: MaximumAdvertisementAmount is "The maximum advertised monetary value of the tendering process." Read by that definition, 500 lume contradicts the estimate. The value looks like the maximum cost of publishing the notices to be borne by the successful tenderer (the meaning in the Spanish CODICE model the element comes from; own knowledge), which the UBL definition does not say, and nothing in the document explains it.
- Condition: The amount fits the definition, or the element is absent.
- Options: (a) remove it (preferred); (b) keep it as advertising cost with a note and record the unclear UBL definition as a finding.
- Needs decision: yes

### tender/03#F14 · Low · Guarantee of 2 400 is not 2 % of any stated amount
- XPath: `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: AmountRate is "The rate used to calculate the amount of liability in this financial guarantee." 2 % of 124 080.00 is 2 481.60; of the bench line 119 760.00 it is 2 395.20; 2 400.00 is 2 % of 120 000, which the document does not state. Probably rounded, but neither base nor rounding is said. The guarantee issued (14-GuaranteeCertificate.xml) is for the same 2 400.00.
- Condition: Rate × base = liability amount for a stated base, or the description says what the amount is rounded from.
- Options: (a) say in the description what the 2 % is taken of and that it is rounded (preferred); (b) set the amount to the calculated value.
- Needs decision: no

### tender/03#F15 · Low · "At least twice" coded as "greater than"
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- Why: "At least" is ≥; `GT` ("Greater than") and "Turnover > 2 × estimate" exclude a turnover of exactly the threshold. Also 2 × 124 080.00 = 248 160.00, not 250 000.00 (rounded up, not said).
- Condition: Description, expression code and expression state the same comparison.
- Options: (a) a "greater than or equal" code and expression if the list has one (preferred); (b) change the description to "more than".
- Needs decision: no

### tender/03#F16 · Low · The tenderer is required to lead a consortium
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Any legal form; consortia must name a lead member.`
- Why: Within a TendererQualificationRequest ("Required set of qualifications for a tenderer") the EconomicOperatorRole states the role the set applies to. As written, the requirements apply to consortium leads only, while any legal form may tender and the tenderers of the flow (Valdara Industries, Brackenmere Furniture) tender alone.
- Condition: The role of the qualification request matches who must meet it, or is absent.
- Options: (a) remove the role (preferred); (b) a role that covers sole tenderers and lead members.
- Needs decision: no

### tender/03#F17 · Low · Contest and other "false" indicators without a case
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:TerminatedIndicator` = `false`
- Why: FollowupContractIndicator "Indicates if any service contract following the contest will be awarded to the winner…", PrizeIndicator whether a prize will be awarded: both belong to design contests, and this is a supply procedure. TerminatedIndicator is "An indicator that the competition launched is terminated"; in the document that launches the competition `false` says nothing. These are fillers (CLAUDE.md: no fillers, nothing implied by absence).
- Condition: Indicators that cannot apply to this procedure, or that only state the obvious negative, are absent.
- Options: (a) remove them (preferred); (b) none other seen.
- Needs decision: no

### tender/03#F18 · Low · Quality criterion with a range of 5 to 10 years and no explanation
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MaximumQuantity` = `10`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric` = `20`
- Why: The criterion "Quality" (weight 40) has a minimum and maximum quantity in years but no description or expression; its only sub-criterion, "Durability of the coating", has weight 20, the other 20 are not described. A tenderer cannot tell what the years measure (probably the warranty offered; the required warranty is 5 years).
- Condition: The criterion says what is scored between 5 and 10 years, and its sub-criteria account for its weight.
- Options: (a) add a description and the missing sub-criterion (preferred); (b) remove the quantities.
- Needs decision: no

### tender/03#F19 · Low · Funding programme code without a list
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26`
- Why: The agreed rule is that every code has a listID (except party-internal codes). `PARKS-26` has none.
- Condition: The code names its list, or the programme is given as text only.
- Options: (a) add the city's list of programmes as listID (preferred); (b) keep only `cbc:FundingProgram`.
- Needs decision: no

### tender/03#F20 · Low · Contact of the review board described as a procurement officer
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: AppealReceiverParty is "The Party who receives the appeal.". Its contact is the registry of the Procurement Review Board, which receives appeals; a registry clerk of a review body is not a "Procurement officer" in a department "Procurement" (that is the contact of a buyer). Name, job title and department do not agree.
- Condition: Job title and department of the contact fit a registry that receives appeals.
- Options: (a) e.g. job title "Registrar", department "Registry" (preferred); (b) drop job title and department.
- Needs decision: no

### tender/03#F21 · Low · Master data of Valdara Industries that this document does nothing with
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- Why: The receiver of the call for tenders is described with its logistics service provider (Castrano Logistics, warehousing and despatch, with a key account desk), its share capital and its stock exchange listing. A call for tenders tells an economic operator what is to be bought and how to tender. Nothing in it concerns warehousing, despatch or listed shares; the data looks copied from the party's master data (section 4.8 of the review rules: data copied into a document that does not use it).
- Condition: The party carries only what this document uses or what identifies it.
- Options: (a) remove the service provider, the security listing and the stock amount here (preferred); (b) keep them only in the documents where they matter (despatch, business information).
- Needs decision: no

### tender/03#F22 · Low · The call for tenders is addressed to the order desk
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The receiver's contact is the person or desk that handles the document. An order desk with a customer service officer takes orders from customers; a call for tenders of a public buyer goes to whoever prepares tenders (a bid or tender desk). The same contact is used for Valdara Industries in every role of the flow.
- Condition: The contact of the receiver of a call for tenders is one that prepares tenders.
- Options: (a) a tender desk contact in the tendering documents (preferred); (b) drop job title and name and keep a general sales contact.
- Needs decision: no

### tender/03#F23 · Low · A public body described as a company in a commercial register
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department, Procurement Review Board of Bayvarra. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/03#F24 · Low · The department's tax exemption reason describes a sale
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: ISIN `XU0001042501` has a correct check digit.
- TenderingProcess, ProcurementProject and both lots equal those of 02 leaf for leaf; TenderingTerms equal those of 02 without MediationParty (compared with a script over the leaf values).
- Amounts and dates as in 02: lots 119 760.00 + 4 320.00 = 124 080.00; framework maximum 186 120.00 = 124 080 + 62 040; deadline 2026-02-26 12:00 before the opening at 14:00; approval 2026-01-25 before issue.
- The top-level TechnicalDocumentReference `PWD-SPEC-BENCH-26` is the specification the request-for-tender line refers to; RequiredDocumentReference `PWD-PRICE-TPL` is the template of the price schedule in TenderPreparation.
- The receiver, Valdara Industries, is described as in 12, 14, 16 and the later examples (same hash of leaf values); its ISIC 3100 (manufacture of furniture) is the class the qualification request requires.

## Considered and refuted
- `/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: "Via delle Officine" and "Ferrano" are tagged `en-XB` although they do not look English — refuted because in this world the English names of Urvanian places and companies are of this form throughout (Ferrano, Società urvaniana per azioni), and the Urvanian rendering is tagged `qau`.
- `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: an amount in ferra where the definition says "The number of shares in the capital stock" — refuted because the element is an amount type and the UBL definition is the oddity; the value is a plausible share capital.
- `/CallForTenders/cac:LegalDocumentReference/cbc:ID`: `PWD-LEGAL-26` here, `XB-PPA-2019` as legal document of the lots — refuted because the procedure's legal conditions and the act are different documents.
- `/CallForTenders/cac:ProvidedDocumentReference`: the five document references have an ID only — refuted because the element names say what kind of document each is, and AccessToolsURI says where the documents are.
- `/CallForTenders/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount`: does not include the renewal — refuted as in 02 (expected spend against ceiling).
- `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate`: `Rate` and `MaximumPercent` both 30 — refuted, redundant but not contradictory.
- `/CallForTenders/cac:ReceiverParty`: only one economic operator receives the call for tenders of an open procedure — refuted because the example is one instance of the document, sent to one operator.

## Outside this review
- The call for tenders is issued one day after the contract notice and 14 days before the tender deadline; whether that is enough is a timeline question of the flow.
