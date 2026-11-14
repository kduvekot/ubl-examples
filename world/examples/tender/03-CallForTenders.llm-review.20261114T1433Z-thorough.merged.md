# LLM review: 03-CallForTenders.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/03-CallForTenders.xml`, Git blob `24f08018e3295692f3f3cc82e4d7e61355b48c44` (committed)
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

### tender/03#F1 · High · Procedure periods start, and three of them end, before the call for tenders is issued
- XPath: `/CallForTenders/cbc:IssueDate` = `2026-02-12`
- XPath: `/CallForTenders/cbc:ApprovalDate` = `2026-01-25`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `02-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-02-11`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`
- Why: The call for tenders is issued on 2026-02-12 and says its documents are available from 2026-01-26; the periods for invitations to tender, invitations to participate and requests to participate have all ended (2026-02-01, 2026-02-11, 2026-02-11) when it is issued, so it announces three periods that are already over. The dates fit a procedure launched on 2026-01-26, one day after the approval and as the prior information notice planned (`01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-01-26`); the issue dates of 02 and 03 are the values that do not fit. The flow's only request to participate, 04, lies after the reception period. Context refuted the date conflict for this document, because this instance is the copy sent to one operator on request, approved on 2026-01-25 and available since 2026-01-26; that explains the availability start, but not the three periods that have ended before the document announcing them is issued, so the finding stays.
- Condition: every period the call for tenders states has not ended when it is issued, and documents of the flow that fall under a period (04) lie inside it.
- Options: (a) preferred by logistics: issue 02 and 03 on 2026-01-26, keeping the periods (agrees with the approval date and the PIN's plan); (b) preferred by broad: keep the issue dates and move the periods after them. Decide together with 02/F1.
- Needs decision: yes
- From: broad (F1), logistics (F1); context refuted it (Considered and refuted)

### tender/03#F2 · High · A latest date for obtaining security clearance, although no clearance is required
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: `LatestSecurityClearanceDate` is "The end date until which the candidates can obtain the necessary level of security clearance." The same terms say no clearance is required; the date contradicts that (no fillers), and the "not required" term only states what absence says. Same pair in 01, 02, 03, 24.
- Condition: no latest clearance date while no clearance is required; a security clearance term only if a clearance is asked.
- Options: (a) preferred: remove the date and the "not required" term; (b) a real clearance requirement (story change).
- Needs decision: no
- From: broad (F2), context (F1), logistics (F6, Medium)

### tender/03#F3 · High · The call for tenders refers to "the call for tenders" under an ID that is not its own
- XPath: `/CallForTenders/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTendersDocumentReference` is "A reference to a Call for Tender associated with these tendering terms." This document is that call for tenders, with the ID `LPWD-DOC-26-0189`; its own terms refer to a call for tenders under another ID that no example carries. Either it refers to itself under a second ID, or to a document that does not exist. The catalogue uses the real ID, while 01, 02, 06, 15, 17, 19 and 24 use `PWD-2026-PARKS-CFT` (8 files with this one; `grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml`), so tenders and catalogue name the same document differently.
- Condition: the call for tenders has one ID, every reference to it uses that ID, and it does not refer to itself.
- Options: (a) preferred: remove the self-reference here and use `LPWD-DOC-26-0189` in the other examples; (b) give this document the ID `PWD-2026-PARKS-CFT` and change the catalogue.
- Needs decision: no
- From: broad (F3, with the replaced notice, Needs decision yes), context (F2), logistics (F2)

### tender/03#F4 · High · The prior information notice is named as "replaced notice", under an ID that is not its ID
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`
- XPath: `/CallForTenders/cbc:VersionID` = `1`
- Why: `ReplacedNoticeDocumentReference` is "A class defining a reference to the notice that is being replaced." A call for tenders is not a notice and replaces none; this is version 1. No example has the ID `PWD-2026-PARKS-PIN`; the prior information notice (`01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`) is referenced correctly by its ID in `NoticeDocumentReference`. The document names one notice under two IDs and in two roles, one of them wrong.
- Condition: a replaced notice is named only where a notice replaces an earlier one, with that notice's ID.
- Options: (a) preferred: remove `ReplacedNoticeDocumentReference`; (b) none other seen.
- Needs decision: no
- From: broad (F3, Needs decision yes), context (F3), logistics (F3)

### tender/03#F5 · High · Lot 2 is "services" here and "works" in the prior information notice
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementSubTypeCode` = `INSTALL`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the park benches`
- Why: The same lot is works in 01 and services (CPC 87390) here, in 02 and 21, with a different name; no change is stated. The deviating value is in 01 and the fix belongs there (logistics refuted the finding for 03 on that ground); it stays a finding here because this example is one side of the contradiction.
- Condition: lot 2 has the same name and procurement type in every document of the flow, or the change is stated.
- Options: (a) preferred: correct 01; this example stays as it is; (b) works everywhere.
- Needs decision: no
- From: context (F4); logistics refuted it for this example (Considered and refuted)

### tender/03#F6 · Medium · A language code in `LocaleCode`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language; it names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`, and `-rl` for files).
- Condition: `LocaleCode`, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) preferred: remove it; (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F9), context (F9), logistics (F7), parties (F1)

### tender/03#F7 · Medium · A province in `Region`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use. `Province of Ferrano` in `Region` occurs 219 times in 104 files (22 of them in tender) (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano'`, lines and files).
- Condition: the province is in `CountrySubentity` (with a code if Urvania has a list); `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the value to `CountrySubentity`; (b) none other seen.
- Needs decision: no
- From: broad (F10), parties (F2)

### tender/03#F8 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Lumeport Public Works Department (a local authority) and the Procurement Review Board of Bayvarra (ISIC 8423) are described with a liquidation status and a register of type `COMMERCIAL` ("A register of businesses"). A public body is not a business in a commercial register and cannot be in liquidation; the world's list has no register type for public bodies.
- Condition: a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop `CompanyLiquidationStatusCode` for public bodies and type their scheme differently (a new code), or keep only the identifier; (b) a stated world rule that public bodies are in the federal business register, without the liquidation status.
- Needs decision: no
- From: broad (F23, Low), parties (F5, Low)

### tender/03#F9 · Medium · Variants flagged as unconstrained in number, with a maximum of one
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- Why: `VariantConstraintIndicator` is "An indicator that variants are allowed and unconstrained in number (true) or not allowed (false)"; with a maximum of one, `true` asserts the opposite of the limit; `VariantConstraintCode` `ALLOWED` and the maximum already say what is meant.
- Condition: the indicator is not `true` while a maximum is given.
- Options: (a) preferred: leave the indicator out; (b) drop the maximum.
- Needs decision: no
- From: broad (F4), context (F5)

### tender/03#F10 · Medium · Tender guarantee of 2400.00 is not 2 % of any amount the document states
- XPath: `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: `AmountRate` is "The rate used to calculate the amount of liability in this financial guarantee." Recalculated: 2 % of 124080.00 = 2481.60, of 119760.00 = 2395.20, of 4320.00 = 86.40; 2400.00 is 2 % of 120000.00, not in the document. The certificate follows the amount (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`). Medium: no base is stated, so no product can be shown to fail, but the base the rate needs is missing.
- Condition: liability amount = rate × a stated base (with the rounding said), or no rate.
- Options: (a) preferred: drop `AmountRate`, fixed 2400 lume in the description; (b) state base and rounding; (c) the calculated amount here and in 14.
- Needs decision: no
- From: money (F2, High), broad (F14, Low)

### tender/03#F11 · Medium · Turnover criterion: "at least" in the text, "greater than" in the code, threshold not twice the estimate
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- Why: "At least" is ≥; `GT` and ">" exclude the threshold; the world's list has `GE`. 2 × 124080.00 = 248160.00, not 250000.00; rounding is possible ("Estimated monetary amount of the threshold") but not said.
- Condition: description, code, expression and threshold state the same comparison and limit.
- Options: (a) preferred: `GE`, "≥", the description naming 250000 lume; (b) threshold 248160.00; (c) "more than".
- Needs decision: no
- From: money (F4), broad (F15, Low), context (F14, Low)

### tender/03#F12 · Medium · Subcontract terms: a "precise" share equal to the maximum, an amount that is 3.5 % of the estimate, and a price flagged as known
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:UnknownPriceIndicator` = `false`
- Why: `Rate` is "The precise percentage allowed to be subcontracted", `MaximumPercent` "The maximum percentage allowed to be subcontracted", `Amount` "The monetary amount assigned to the subcontracted task". A "precise" 30 % next to a maximum of 30 % says two things; the amount, lot 2's estimate, is 3.48 % of 124080.00; the award documents pair it with `Rate` 3.5 (`22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`); `UnknownPriceIndicator` `false` claims a known subcontract price before any tender. Broad refuted it (redundant, not contradictory); not High because `Amount` is not defined as rate × base, Medium because `Rate` carries a meaning other than its definition.
- Condition: the buyer's terms state the limit it sets, and nothing about a subcontract price that does not exist yet.
- Options: (a) preferred: keep `MaximumPercent`, `SubcontractingConditionsCode` and `Description`; remove `Rate`, `Amount`, `UnknownPriceIndicator`; (b) keep `Amount` as the installation estimate, explained, without `Rate`.
- Needs decision: no
- From: money (F1, High), context (F16, Low); broad refuted it (Considered and refuted)

### tender/03#F13 · Medium · Identifier of an "original" framework agreement in a procedure that reopens nothing
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: `OriginalContractingSystemID` is "When reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system." This open procedure sets up a new framework; it reopens nothing. `PWD-FW-2024-PARKS` appears only as this ID in 02, 03 and 21.
- Condition: the element only in a procedure that reopens competition under an existing framework or DPS.
- Options: (a) preferred: remove it; (b) a note on a predecessor framework, if wanted; (c) a call-off under a 2024 framework (story change).
- Needs decision: no
- From: broad (F6), context (F11, Needs decision yes), logistics (F4)

### tender/03#F14 · Medium · Periods for invitations and requests to participate in an open procedure
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-02-26`
- Why: The three periods ("… invitations to tender must be completed and delivered", "… the invitation to participate must be sent", "… requests for participation must be completed and delivered") are steps of a procedure with a selection stage (own knowledge of procurement practice); in an open procedure any operator tenders by the deadline without request or invitation, as tenders 15, 17 and 19 do. The flow nevertheless has an expression of interest (04/05) and a qualification application (06/07) before the tenders, the pattern of a two-stage procedure; which kind of procedure the flow has could be a story question, but every document calls it open, so the preferred fix is encoding.
- Condition: the call carries only the periods its procedure has; if the world's open procedure has a registration step (04/05), only the period that governs it, with 04 inside it.
- Options: (a) preferred: remove the three periods (or keep only `ParticipationRequestReceptionPeriod` as the registration period, ending after 04); (b) a restricted procedure, consistent with 04 to 07 (story change).
- Needs decision: no
- From: broad (F5, Needs decision yes), context (F10), logistics (F5, Needs decision yes)

### tender/03#F15 · Medium · The price of paper copies in the element for the reimbursement fee of concessions, three times
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: `RequiredFeeAmount`/`FeeDescription` are "the reimbursement fee for concession procurement projects"; nothing here is a concession, and the 50 lume are the price of paper copies, which `DocumentationFeeAmount` already states. Stated four times, three in the wrong element; per lot it reads as 50 lume per lot, while the tender pays it once (`15-Tender.xml:/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`).
- Condition: no concession fee where there is no concession; the documentation fee stated once, its explanation in a text of the tendering terms.
- Options: (a) preferred: remove the elements from project and lots, sentence to a `TenderingTerms/Note`; (b) none other seen.
- Needs decision: no
- From: broad (F7), context (F7), money (F5)

### tender/03#F16 · Medium · A strategic-procurement code in the element for an additional procurement type, also on the installation lot
- XPath: `/CallForTenders/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- Why: `ProcurementTypeCode` is "A code signifying the type of procurement project (e.g., goods, works, services)"; `GREEN` is a policy objective (eForms BT-06 practice, own knowledge, which does not change the UBL meaning). On lot 2 the text "recycled steel and certified timber are asked" does not apply.
- Condition: `ProcurementAdditionalType` carries a type of procurement; the environmental objective where UBL has a place for it, or the difference recorded for the TC.
- Options: (a) preferred: the additional nature that applies; the aim in `ContractExecutionRequirement`/`SpecificTendererRequirement`; at least not on lot 2; (b) keep the eForms encoding and record it for the TC.
- Needs decision: yes
- From: broad (F8), context (F8)

### tender/03#F17 · Medium · Framework values: the "estimated" value leaves out the renewal, the "maximum" is below what the terms allow
- XPath: `/CallForTenders/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount` = `148896.00`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:FrameworkAgreement/cbc:MaximumValueAmount` = `186120.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:ContractExtension/cac:Renewal/cbc:Amount` = `62040.00`
- Why: Both elements are defined "over its whole duration, including options and renewals" (estimated, and maximum). Recalculated: 148896.00 is the base maximum (288 benches) without the renewal; 124080 + 62040 = 186120.00 is the estimate with the renewal; 148896 + 62040 = 210936.00 is the most the terms allow. Broad refuted it (expected spend vs ceiling); the merge accepts that a buyer may set a ceiling below the arithmetic maximum, but the estimate still excludes the renewal the definition includes.
- Condition: the estimated value includes the renewal; the maximum is the ceiling the terms allow, or the document says the renewal counts against a lower ceiling.
- Options: (a) preferred by money: estimated 186120.00, maximum 210936.00; (b) 186120.00 as the stated ceiling for everything, with the estimate following.
- Needs decision: yes
- From: money (F3); broad refuted it (Considered and refuted)

### tender/03#F18 · Medium · Request lines: minimum and maximum amount are unit prices, the estimated amount is a line total
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- Why: "The minimum/maximum amount allowed for this deliverable" and "The estimated total amount of the deliverable" refer to one deliverable; the estimate is for 240 benches (240 × 499), minimum and maximum are bench prices. Read by the definitions, the line allows at most 600.00 for a deliverable estimated at 119760.00.
- Condition: minimum, maximum and estimate of a line on the same basis.
- Options: (a) preferred: line totals (84000.00 and 144000.00) in the lines, unit-price limits only in the price criterion; (b) drop them from the lines and state the unit limits in a note.
- Needs decision: no
- From: money (F6)

### tender/03#F19 · Low · Copied master data of both parties that the call for tenders does nothing with
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: A call for tenders tells an operator what is bought and how to tender. Nothing in it is declared to customs (the customs trader numbers of both parties matter in 30 and 31), concerns warehousing or despatch (`ServiceProviderParty`, "A party providing a service to this party": Castrano Logistics acts in 29), the receiver's VAT registration, its share capital or its stock listing. The buyer cannot know, and does not use, who despatches the goods of an operator that has not yet tendered. This is master data copied into a document that does not use it (section 4.8). `CorporateStockAmount` holds share capital where UBL defines "The number of shares in the capital stock" (a note for the TC write-up; broad and parties refuted it as the model's oddity, since the element is an amount type).
- Condition: the receiver of the call for tenders is identified (ID, name, address, electronic address); no service providers, tax, capital or customs data the document does not use.
- Options: (a) preferred: reduce the receiver to its identification, name, address and electronic address, and drop the department's customs number; (b) keep them only where the document says what they are for.
- Needs decision: no
- From: broad (F21), context (F21, F26), parties (F3)

### tender/03#F20 · Low · The department's tax exemption reason is worded as a sale
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: In `PartyTaxScheme` the exemption reason is "A reason for the party's exemption from tax". The text starts with a transaction ("Sale to a public body"); the code's definition ("A body of the federation, a state or a city buys free of sales tax") fits the party. Money refuted it (the second half states the status); kept at Low because the first half describes a sale.
- Condition: the party's exemption reason states the party's status.
- Options: (a) preferred: "Public body: buys free of the state sales tax", code unchanged; (b) a separate party-status code.
- Needs decision: no
- From: broad (F24), parties (F4); money refuted it (Considered and refuted)

### tender/03#F21 · Low · Eight further roles all filled with the contracting party itself
- XPath: `/CallForTenders/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AdditionalInformationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ContractResponsibleParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderEvaluationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:QualificationRequestRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The contracting party, acting `/CallForTenders/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationType` = `On its own behalf`, is repeated by register number and name in eight roles meant for another body or office; they say nothing the `ContractingParty` does not (no fillers). The model even defines `OriginatorCustomerParty` here as "the party who originated Order" (context). Context's story question (is the parks department a body of its own?) is option (b).
- Condition: a role party only where it differs from the contracting party or adds role-specific details.
- Options: (a) preferred: drop the repetitions; keep `TenderRecipientParty` or `AdditionalInformationParty` only with their own contact; (b) the parks department as originator or beneficiary (story); (c) keep all as an explicit statement.
- Needs decision: no
- From: context (F20, Needs decision yes), parties (F6)

### tender/03#F22 · Low · Maximum advertisement amount of 500 lume: advertised value or advertising cost?
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:AdvertisementAmount` = `320.00`
- Why: "The maximum advertised monetary value of the tendering process": literally, 500.00 is neither the estimate nor the maximum (broad, context). Money: the element pairs with `TenderResult/AdvertisementAmount` (320.00 in 21), so both are advertising costs (the CODICE meaning). The merge cannot settle which reading UBL means; the document does not explain the 500.
- Condition: the amount fits the definition as the world reads it, with a stated reason, or is absent.
- Options: (a) preferred: decide the reading; if advertising cost, say who bears it and record the unclear definition for the TC; (b) remove it; (c) the advertised maximum value.
- Needs decision: yes
- From: broad (F13), context (F6, Medium); money refuted it (Considered and refuted)

### tender/03#F23 · Low · Penalty clause without the amount its percentages apply to
- XPath: `/CallForTenders/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.`
- Why: The base is not stated; the debit note applies it to the installation price of one release (`34-DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`), one choice among several.
- Condition: the clause names its base, the one the debit note uses.
- Options: (a) preferred: "0.5 % of the price of the late part of a release per day late, at most 10 % of that price"; (b) another base, with the debit note following.
- Needs decision: no
- From: money (F10)

### tender/03#F24 · Low · The qualification request is given the role "consortium lead"
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Any legal form; consortia must name a lead member.`
- Why: `EconomicOperatorRole` ("A class to describe the tenderer contracting role") limits the only qualification request to consortium leads, while every tenderer must meet it and the tenderers of the flow tender alone; the list also has `SOLE`.
- Condition: the role matches who must meet the request, or is absent.
- Options: (a) preferred: remove the role; (b) one request per role.
- Needs decision: no
- From: broad (F16), context (F15)

### tender/03#F25 · Low · The tender preparation is tied to lot 1 only
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderPreparation/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TenderPreparation/cbc:Description` = `One encrypted envelope per tender.`
- Why: The only `TenderPreparation` names lot 1, while a tenderer may tender for both lots; nothing says how a tender for lot 2 is prepared.
- Condition: the preparation covers every lot a tender can be submitted for.
- Options: (a) preferred: no lot in the preparation; (b) both lots.
- Needs decision: no
- From: context (F17)

### tender/03#F26 · Low · Design-contest and negotiation indicators in an open supply procedure
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:NoFurtherNegotiationIndicator` = `true`
- Why: Prize and follow-up contract belong to design contests (and `false` only states absence); `BindingOnBuyerIndicator` is a contest jury's indicator (eForms, own knowledge); no negotiation is possible in an open procedure.
- Condition: none of these indicators, unless the document explains what each refers to.
- Options: (a) preferred: remove all four; (b) keep `NoFurtherNegotiationIndicator` only under a stated rule of the world's act.
- Needs decision: no
- From: broad (F17, the two contest indicators), context (F12, all four)

### tender/03#F27 · Low · Values that only state the default: normal urgency, no reduction of candidates, not terminated
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:UrgencyCode` = `NORMAL`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `false`
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:TerminatedIndicator` = `false`
- Why: Each states what its absence implies (UBL IND6): not urgent; no candidates reduced in an open procedure without candidates; a procedure just launched is not terminated.
- Condition: these elements only where they say something other than the default.
- Options: (a) preferred: remove the three; (b) none other seen.
- Needs decision: no
- From: context (F22), broad (F17 for `TerminatedIndicator`, F5 for `CandidateReductionConstraintIndicator`)

### tender/03#F28 · Low · Quality criterion: a range of 5 to 10 years without explanation, and one sub-criterion of half its weight
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MaximumQuantity` = `10`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric` = `20`
- Why: "Quality" (40) has a range in years without description or expression (presumably the warranty offered), and one sub-criterion of 20. Money refuted the weight part (the warranty scored by the parent); plausible, not stated.
- Condition: the criterion says what its range measures, and its sub-criteria or description account for its weight.
- Options: (a) preferred: two sub-criteria (coating 20, warranty years 20 with the range) and a description; (b) a description only; (c) remove the range.
- Needs decision: no
- From: broad (F18), context (F18); money refuted the weight part (Considered and refuted)

### tender/03#F29 · Low · Technical committee of three officers, one named
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:TechnicalCommitteeDescription` = `Three officers of the department.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:FamilyName` = `Delling`
- Why: Three officers described, one listed.
- Condition: the persons listed and the description agree.
- Options: (a) preferred: Mara Delling chairs, the others are appointed later; (b) list all three.
- Needs decision: no
- From: parties (F9)

### tender/03#F30 · Low · Contact of the review board's registry described as a procurement officer
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: The registry that receives appeals ("The Party who receives the appeal.") has the buyer's job title and department; name, job title and department do not agree.
- Condition: one function, fitting the receipt of appeals.
- Options: (a) preferred: "Registrar" in "Registry"; (b) drop job title and department.
- Needs decision: no
- From: broad (F20), parties (F10)

### tender/03#F31 · Low · The call for tenders is addressed to the order desk
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `order@valdara.example`
- Why: Valdara Industries receives the call as a prospective tenderer; its contact is the desk that takes purchase orders (right in 26–28), not one that prepares tenders. The same contact is used for Valdara in every role of the flow.
- Condition: the contact of the receiver of a call for tenders handles tenders, or is left out.
- Options: (a) preferred: a tender or bid desk contact in the tendering documents; (b) no contact here.
- Needs decision: no
- From: broad (F22), parties (F8)

### tender/03#F32 · Low · The place of an electronic opening named after the department and a square
- XPath: `/CallForTenders/cac:TenderingProcess/cac:OpenTenderEvent/cac:OccurrenceLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:OpenTenderEvent/cbc:Description` = `Electronic opening; tenderers may follow it online.`
- Why: The location of an electronic opening names the organisation and its square (not a place), without the address ID the building has in this document (`/CallForTenders/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`) and without the online session.
- Condition: the location is where the opening can be attended, or absent for a purely electronic opening.
- Options: (a) preferred (context): remove the location, give the platform address in the description; (b) (parties) a room with the address of Civic Square 6.
- Needs decision: no
- From: context (F25), parties (F11)

### tender/03#F33 · Low · Lot 2 (installation) is described with the data of the bench supply
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:EstimatedOverallContractQuantity` = `240`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cbc:OptionsDescription` = `One extension of a year with 120 more benches.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- Why: Lot 2's description and option are those of the whole project, the same as lot 1's; its quantity is 240 "each" without saying of what; it has no request line, while lot 1's line holds the ground anchor sets with an estimate that leaves out lot 2's 4320.00, so it is not clear in which lot the anchors are. (Lot 2's "Furniture" classification is in F34.)
- Condition: each lot describes what it buys; it is clear in which lot the anchors are.
- Options: (a) preferred: own descriptions per lot and a request line for the installation; (b) only name, type, classification and amounts on the lots.
- Needs decision: no
- From: broad (F11), context (F24)

### tender/03#F34 · Low · The additional classification is the parent group of the main one; the installation is not classified at project level, and lot 2 is classified as furniture
- XPath: `/CallForTenders/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:MainCommodityClassification/cbc:ItemClassificationCode` = `87390`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- Why: CPC 381 "Furniture" contains the main class 38111 and adds nothing ("additional classification categories for the deliverable requested"); the installation (87390) is not classified at project level; lot 2 lists "Furniture" as an additional category of an installation service.
- Condition: additional classifications name categories the main one does not imply.
- Options: (a) preferred: 87390 as the project's additional classification, no "Furniture" on lot 2; (b) remove the additional classifications.
- Needs decision: no
- From: context (F19), broad (F11, lot 2's 381)

### tender/03#F35 · Low · Works quality control stated for a supply project and both lots
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- Why: `QualityControlCode` is "The indication of whether or not the control quality is included in the works project"; the project is supplies and lot 2 services; "Inspection on delivery" is an acceptance rule for goods.
- Condition: only for a works project or lot; inspection of deliveries as an acceptance term.
- Options: (a) preferred: remove it, state the inspection in the contract conditions or a note; (b) none other, as no lot is works.
- Needs decision: no
- From: context (F13)

### tender/03#F36 · Low · Lot-level tendering terms and process that only say "As for the procedure."
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- Why: Four aggregates that only say nothing differs, which is what their absence means (no fillers). See F37: some terms do not fit lot 2.
- Condition: lot-level terms or process only where something is specific to the lot.
- Options: (a) preferred: remove the four; (b) real lot-specific terms (F37).
- Needs decision: no
- From: broad (F12), context (F23)

### tender/03#F37 · Low · Money terms set for the whole procedure do not fit a tender for lot 2 alone
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:PartPresentationCode` = `ONEORMORE`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumAmount` = `350.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`
- Why: Tenders may be made for one lot, and lot 2 (estimated 4320.00, 18 lume per bench) takes the procedure's terms: no unit price can meet 350–600 lume; the auction "on the unit prices of both lots" has a step only for the bench price (2 lume = 11 % of the installation price); the guarantee is 56 % and the turnover threshold 58 times the lot's estimate (recalculated).
- Condition: every money term for lot 2 can be met by a tender for lot 2 alone, or lot 2 can only be tendered with lot 1, as stated.
- Options: (a) preferred: price limits, bid step, guarantee and turnover threshold per lot; (b) require tenders for both lots (group G-1) and say so.
- Needs decision: yes
- From: money (F7)

### tender/03#F38 · Low · An electronic auction is announced, but the flow shows no trace of it
- XPath: `/CallForTenders/cac:TenderingProcess/cac:AuctionTerms/cbc:AuctionConstraintIndicator` = `true`
- XPath: `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:LowerTenderAmount` = `119040.00`
- Why: The award is made at exactly the winner's tendered amount and the lowest tender reported is the other tenderer's original amount; no document mentions an auction held or not held.
- Condition: the flow shows what became of the auction, or the procedure has none.
- Options: (a) preferred: say in the award documents that the auction of a given date brought no lower bids; (b) let it lower a price and carry it through; (c) no auction.
- Needs decision: yes
- From: money (F9), logistics (Outside this review)

### tender/03#F39 · Low · The whole two-year amount on one budget account of 2026
- XPath: `/CallForTenders/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:BudgetAccountLine/cac:BudgetAccount/cbc:BudgetYearNumeric` = `2026`
- Why: Spending falls in 2026 to 2028; the single line charges it all to a 2026 account without saying it is a multi-year commitment.
- Condition: the budget lines show the years, or say it is a two-year commitment of the 2026 budget.
- Options: (a) one account per year; (b) preferred, smallest: a note.
- Needs decision: yes
- From: money (F11)

### tender/03#F40 · Low · The buyer's estimates equal the winning tender to the cent
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: Valdara's tender offers exactly the estimates in both lots (119760.00 and 4320.00), the other tenderer 119040.00; it reads as the outcome copied back into the estimate, and all derived figures inherit it.
- Condition: the estimate differs from the tendered prices, or the story explains the equality.
- Options: (a) preferred: a rounded estimate (e.g. 124800.00) with derived amounts following; (b) say in the tender that it offers the published estimate.
- Needs decision: yes
- From: money (F8)

### tender/03#F41 · Low · Valdara Industries is "large" with 180 employees
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- Why: The world's list defines `LARGE` as "250 persons or more, or a turnover above the limits of a medium-sized enterprise"; Valdara states 180 employees and a financial capability of 9200000.00 XBL in its qualification, far below the turnover limit. Because the definition reads "or" and no turnover is stated as such, there is no strict contradiction; nothing in the flow supports `LARGE` either. Aligned with mergers B and C.
- Condition: Valdara's size class agrees with its employees and financial figures in the flow.
- Options: (a) 250 or more employees in the qualification, if Valdara is meant to be a large listed company (preferred by parties); (b) `MEDIUM` in every example that describes it.
- Needs decision: yes
- From: parties (F7)

### tender/03#F42 · Low · Valdara's Urvanian address tagged `en-XB` here, `en-XU` elsewhere
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: The English rendering of Valdara's street is tagged `en-XB` in 13 files of the flow and `en-XU` in 9 (`grep -l` over `tender/*.xml`), depending on the issuer; the Italianate names are tagged as English at all. Broad and parties refuted it: these are the world's English names of Urvanian places, and the tag follows the issuer's locale consistently. Earlier merges of every flow could not settle this either and recorded it as Low, Needs decision yes (`analysis/review-merge-decisions.md`); the merge aligns with them rather than refute it.
- Condition: one documented rule for the language tag of a party's address renderings (the party's variety or the issuer's), applied in every example.
- Options: (a) the party's own variety (`en-XU`) everywhere; (b) the issuer's variety, stated as a world convention.
- Needs decision: yes
- From: merge (broad and parties considered and refuted it)

### tender/03#F43 · Low · Valdara's legal form in one untagged rendering
- XPath: `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Where the address is given in Urvanian (`qau`) and English, the legal form appears once, without `languageID`, in the English form; in the documents Valdara issues it has a `qau` and an `en-XU` rendering (e.g. 13, 15). Parties noted the difference and refuted it together with the tags; earlier merges kept the untagged single legal form as a separate Low finding (`analysis/review-merge-decisions.md`, wood, plastics, rail, D).
- Condition: the legal form is rendered like the address (both languages, each tagged), as in Valdara's own documents.
- Options: (a) preferred: both renderings, tagged; (b) none other seen.
- Needs decision: no
- From: merge (parties considered and refuted it)

### tender/03#F44 · Low · The call for tenders links the prior information notice but not its contract notice
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`
- XPath: `02-ContractNotice.xml:/ContractNotice/cbc:ID` = `LPWD-DOC-26-0188`
- Why: `NoticeDocumentReference` is "A reference to a notice pertaining to this tendering process". The contract notice that launched the procedure, issued the day before, is not referenced; the block is copied from 02, where the reference to the PIN alone is right.
- Condition: the call for tenders refers to its contract notice.
- Options: (a) preferred: a second `NoticeDocumentReference` with `LPWD-DOC-26-0188`; (b) leave the link to `ContractFolderID`.
- Needs decision: no
- From: logistics (F8)

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` has a correct check digit.
- TenderingProcess, ProcurementProject and both lots equal those of 02 leaf for leaf; TenderingTerms equal 02's without `MediationParty` (broad, by script).
- Amounts and dates as in 02 (recalculated there): lots 119760.00 + 4320.00 = 124080.00; minimums, maximums, renewals and average releases add up; deadline 2026-02-26 12:00 before the opening at 14:00; approval 2026-01-25 before issue 2026-02-12 13:26; the receiver's tender (15) of 2026-02-25 and guarantee (14) of 2026-02-24 lie before the deadline.
- Award weights, price limits, auction step, tax category E/STT, PERRELEASE, framework duration and `TenderingProcess/ID` agree as in 02.
- Document references at the top (`PWD-LEGAL-26`, `PWD-SPEC-BENCH-26`, `PWD-PRICE-TPL`, `PWD-SITE-PLAN`, `PWD-QA-26`) are each of the kind their element names; `PWD-PRICE-TPL` is the template in `TenderPreparation`; lots carry `PWD-SPEC-LOT-1`/`-2` as in 02.
- Valdara Industries is described as in 12, 14, 16 and the later examples, apart from the language tags (F42, F43); ISIC 3100 is the class the qualification request requires; registration date 1962-04-12 is its own (not the 1996-01-01 default).
- Codes: CPC 38111, 381, 87390; ISIC 3100, 8411, 8423; unit codes; channel code AL in EDED 3155; all world-list codes resolve; `qau` is in the ISO 639 local-use range; +999 is unassigned.

## Considered and refuted
- `/CallForTenders/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate`: availability from 2026-01-26 before issue 2026-02-12 — refuted by context because this instance is the copy sent to one operator, approved on 2026-01-25 and available since 2026-01-26 — the merge accepts this for the availability start, but not for the periods that have ended; F1 stays (from context).
- `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode`: `SERVICES` against `WORKS` in 01 — refuted by logistics for this example (the deviating value is in 01) — the merge keeps F5 with the fix in 01 (from logistics).
- `/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: Italianate names tagged `en-XB`, and tags that differ by issuer — refuted by broad and parties (the world's English names; the tag follows the issuer consistently) — the merge aligns with earlier merges and keeps F42 and F43 (from broad, parties).
- `/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: an amount where UBL says "number of shares" — refuted, the element is an amount type; the definition is the model's oddity (a note for the TC write-up); the value itself is in the copied-data finding F19 (from broad, parties).
- `/CallForTenders/cac:LegalDocumentReference/cbc:ID`: `PWD-LEGAL-26` at the top, `XB-PPA-2019` in the lots — refuted, two different legal documents, each "a legal document" (from broad, logistics; context's finding is under "Refuted in the merge").
- `/CallForTenders/cac:ProvidedDocumentReference`: references with an ID only — refuted, the element names say what each is, and `AccessToolsURI` where they are (from broad).
- `/CallForTenders/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount`: excludes the renewal — refuted by broad (expected spend vs ceiling) — the merge keeps money's F17 (from broad).
- `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate`: redundant with the maximum — refuted by broad — the merge keeps F12 (from broad).
- `/CallForTenders/cac:ReceiverParty`: one operator as receiver of an open call — refuted, this instance is the copy sent to one operator (from broad, parties).
- `/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode`: no listID — refuted, a party-internal programme number (from context, logistics; broad's finding under "Refuted in the merge").
- `/CallForTenders/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric`, `/CallForTenders/cac:ProcurementProject/cbc:RequestedDeliveryDate`, `/CallForTenders/cac:ProcurementProject/cbc:ProcurementSubTypeCode`, `/CallForTenders/cac:ProcurementProject/cbc:SMESuitableIndicator`, `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:OperatingYearsQuantity` (model definition error), `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealInformationParty`, `/CallForTenders/cac:TenderingTerms/cac:ContractResponsibleParty`, `/CallForTenders/cac:TenderingProcess/cbc:GovernmentAgreementConstraintIndicator`, `/CallForTenders/cac:TenderingProcess/cac:ProcessJustification`, `/CallForTenders/cac:TenderingProcess/cac:FrameworkAgreement/cbc:ExpectedOperatorQuantity`, `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` — refuted for the same reasons as in 02 (from context; the contract-responsible party also from parties).
- `/CallForTenders/cac:OriginatorCustomerParty`: the model defines it as "the party who originated Order" — the wording is the model's; the role is in F21 (from context).
- `/CallForTenders/cac:TenderingProcess/cbc:ContractingSystemCode`, `/CallForTenders/cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate`, `/CallForTenders/cac:TenderingProcess/cac:AdditionalInformationRequestPeriod/cbc:EndDate`, `/CallForTenders/cac:ProcurementProjectLot[1]/cac:LegalDocumentReference/cbc:ID` — refuted as in 02 (from logistics).
- `/CallForTenders/cac:TenderingTerms/cbc:MaximumAdvertisementAmount`: refuted by money (pairs with `AdvertisementAmount` 320.00) — the merge keeps F22, Low, Needs decision yes (from money).
- `/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount`, `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cac:Renewal/cbc:Amount` (2160.00 = 120 × 18), `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`, `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` (2 vs 0.02), `/CallForTenders/cac:TenderingProcess/cac:ProcessJustification/cbc:ProcessReason` — refuted as in 02 (from money).
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason`: refuted by money — the merge keeps F20 (from money).
- `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric`: refuted by money — kept in F28 (from money).
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`, `/CallForTenders/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`, `/CallForTenders/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`, `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` — refuted as in 01 (from parties).
- `/CallForTenders/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` an assigned ISO 6523 code — refuted as far as own knowledge goes (assigned ICDs are far below 0990); the ICD register was not checked (from parties).
- `/CallForTenders/cac:ReceiverParty/cac:Language/cbc:ID`: `qau` a real ISO 639 code — refuted, qaa–qtz is reserved for local use (from parties).

## Refuted in the merge
### broad/F19 · Low · Funding programme code without a list
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26`
- Why (broad): every code has a listID except party-internal codes; `PARKS-26` has none.
- Condition (broad): the code names its list, or the programme is given as text only.
- Refuted because: a party-internal programme number, exempt from the rule and explained by `FundingProgram`; context and logistics refuted it likewise.

### context/F27 · Low · "Legal document" is a department document at the top and the Procurement Act in the lots
- XPath: `/CallForTenders/cac:LegalDocumentReference/cbc:ID` = `PWD-LEGAL-26`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:LegalDocumentReference/cbc:ID` = `XB-PPA-2019`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:LegalDocumentReference/cbc:ID` = `XB-PPA-2019`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ProcurementLegislationDocumentReference/cbc:ID` = `XB-PPA-2019`
- Why (context): in a call for tenders the legal document is the document with the administrative conditions; the lots name the act, which is legislation and already referenced as such, so the element points to two kinds of thing and the lots do not say which conditions apply.
- Condition (context): the lot's legal document reference points to the conditions document that applies to the lot, or is absent.
- Refuted because: the definition is only "A reference to a legal document", which an act is; the top-level and lot-level references name two different legal documents and contradict nothing (broad and logistics refuted it on the same ground). That the lots repeat the act already named in `ProcurementLegislationDocumentReference` is at most a duplication; it is not a misuse of the element.

## Changed in the merge
- broad/F1, logistics/F1 → F1: context's refutation carried and answered; both preferred options kept, to be decided with 02/F1.
- broad/F2, context/F1, logistics/F6 (Medium) → F2: High.
- broad/F3 → split into F3 and F4, as context and logistics; Needs decision no (broad said yes).
- context/F4 → F5: kept High although logistics refuted it for 03; fix placed in 01 (broad had no lot finding in 03).
- broad/F23, parties/F5 → F8: Low raised to Medium (main table, mergers B, C, D).
- money/F2 (High), broad/F14 (Low) → F10: Medium; money/F4, broad/F15, context/F14 → F11: Medium; money/F1 (High), context/F16 (Low) → F12: Medium — as in 01 and 02.
- broad/F6, context/F11 (yes), logistics/F4 → F13: Needs decision no.
- broad/F5 (yes), context/F10 (no), logistics/F5 (yes) → F14: Needs decision no, aligned with merger B (09) and 02/F13: the procedure is OPEN everywhere, so removal is encoding; restricted procedure as story option (b); `CandidateReductionConstraintIndicator` moved to F27.
- broad/F21, context/F21, context/F26, parties/F3 → F19: grouped as one copied-master-data finding (customs numbers, service provider, receiver's tax registration, share capital, listing).
- broad/F13 (Low), context/F6 (Medium) → F22: Low, Needs decision yes.
- context/F20 (yes), parties/F6 (no) → F21: Needs decision no.
- broad/F17, context/F12, context/F22 → F26 and F27, regrouped by kind.
- broad/F11, context/F24 → F33; lot 2's 381 moved to F34 (with context/F19).
- context/F25, parties/F11 → F32: the merge prefers context's option.
- money/F9 with logistics' Outside entry → F38.
- F42 and F43 added by the merge, against the refutations of broad and parties, to align with the decisions of earlier merges on language tags and untagged legal forms.
- broad/F4, context/F5 → F9; broad/F7, context/F7, money/F5 → F15; broad/F8, context/F8 → F16; broad/F9, context/F9, logistics/F7, parties/F1 → F6; broad/F10, parties/F2 → F7; broad/F24, parties/F4 → F20; broad/F16, context/F15 → F24; broad/F18, context/F18 → F28; broad/F20, parties/F10 → F30; broad/F22, parties/F8 → F31; broad/F12, context/F23 → F36: combined, severity unchanged.

## Outside this review
- The call for tenders is issued one day after the contract notice and 14 days before the tender deadline; whether an operator in Urvania could receive it on 2026-02-12 and tender by 2026-02-25 with a guarantee of 2026-02-24 is a timeline question (from broad, context).
- `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:CallForTendersLineReference/cbc:LineID` refers to a line 2 of this call for tenders, which has only the lines `1` and `1.1`; the problem lies in the catalogue (from context).
- The invoice of the first release applies the supplier's standard terms rather than "30 days after each accepted release"; that lies in 32 (from money).
