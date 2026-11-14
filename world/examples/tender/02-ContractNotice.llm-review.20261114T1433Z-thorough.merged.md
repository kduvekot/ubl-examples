# LLM review: 02-ContractNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/02-ContractNotice.xml`, Git blob `1902067078eeb7c2dc70b632a4e813bb3c440b21` (committed)
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

### tender/02#F1 · High · Requested publication and procedure periods lie before the notice's own issue date
- XPath: `/ContractNotice/cbc:IssueDate` = `2026-02-11`
- XPath: `/ContractNotice/cbc:RequestedPublicationDate` = `2026-01-27`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-01-26`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`
- Why: `RequestedPublicationDate` is "The requested publication date for this Contract Notice"; the notice is issued on 2026-02-11 and asks to be published on 2026-01-27, fifteen days earlier. The documents are said to be available from 2026-01-26, the invitation submission period ended on 2026-02-01, ten days before the notice existed, and the periods for invitations and requests to participate end on the day of issue. These dates fit a publication on 2026-01-26/27, which is what the prior information notice planned; the issue date 2026-02-11 does not. The flow's only request to participate, 04, comes three days after the reception period ends and is still answered in 05.
- Condition: the requested publication date is not before the issue date; no period the notice announces starts before its publication or has ended when it is issued; documents of the flow that fall under a period lie inside it.
- Options: (a) preferred by context and logistics: issue the notice (and 03 with it) on about 2026-01-26, as planned in 01, keeping the periods (and move the end of the reception period after 04 if that period stays, see F5); (b) preferred by broad: keep 2026-02-11 and move the requested publication date and all periods after it, which leaves fifteen days to the tender deadline. The merge has no preference: (a) changes fewer values, (b) keeps the order of the document numbers and issue dates of the flow.
- Needs decision: yes
- From: broad (F1), context (F5), logistics (F1)

### tender/02#F2 · High · A latest date for obtaining security clearance, although no clearance is required
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Description` = `Parks are public places.`
- Why: `LatestSecurityClearanceDate` is "The end date until which the candidates can obtain the necessary level of security clearance." The same tendering terms say that no clearance is required. There is no "necessary level" to obtain, so the date contradicts the term beside it (no fillers); the "not required" term only states what its absence would say. Same pair in 01, 02, 03 and 24 (`grep -l LatestSecurityClearanceDate world/examples/*/*.xml`).
- Condition: the tendering terms do not carry a latest clearance date while they say that no clearance is required; a security clearance term is present only if a clearance is asked.
- Options: (a) preferred: remove the date and the "not required" term; (b) give the procedure a real clearance requirement (story change).
- Needs decision: no
- From: broad (F2), context (F1), logistics (F6, Medium)

### tender/02#F3 · High · Call for tenders referenced under an ID no document has
- XPath: `/ContractNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- XPath: `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTendersDocumentReference` is "A reference to a Call for Tender associated with these tendering terms." No example of the flow has the document ID `PWD-2026-PARKS-CFT`; the call for tenders is 03 (`LPWD-DOC-26-0189`, issued a day after this notice), and the catalogue refers to it by that ID, so the flow uses two IDs for one document. A notice announcing the call issued the next day is plausible, but then under the number it carries. The ID occurs in 8 files: 01, 02, 03, 06, 15, 17, 19, 24 (`grep -l PWD-2026-PARKS-CFT world/examples/tender/*.xml`).
- Condition: every `CallForTendersDocumentReference/cbc:ID` of the flow equals the ID of 03.
- Options: (a) preferred: use `LPWD-DOC-26-0189` in the references; (b) give 03 the ID `PWD-2026-PARKS-CFT` and change the catalogue.
- Needs decision: no
- From: broad (F3, with the replaced notice, Needs decision yes), context (F2), logistics (F2)

### tender/02#F4 · High · The prior information notice is named as "replaced notice", under an ID that is not its ID
- XPath: `/ContractNotice/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`
- XPath: `/ContractNotice/cbc:VersionID` = `1`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`
- Why: `ReplacedNoticeDocumentReference` is "A class defining a reference to the notice that is being replaced." A contract notice follows a prior information notice; it does not replace it, and this is version 1, so no earlier contract notice is replaced either. No example has the ID `PWD-2026-PARKS-PIN`; the same document already refers to the prior information notice correctly, by its ID, in `NoticeDocumentReference`. It thus names one notice under two IDs and in two roles, one of them wrong. The reference occurs in 01, 02, 03 and 24.
- Condition: a replaced notice is named only where a notice replaces an earlier one, with that notice's ID; the prior information notice is referred to only by its document ID.
- Options: (a) preferred: remove `ReplacedNoticeDocumentReference` (`NoticeDocumentReference` already links the PIN); (b) a story in which this notice replaces an earlier contract notice.
- Needs decision: no
- From: broad (F3, Needs decision yes), context (F3), logistics (F3)

### tender/02#F5 · High · Lot 2 is "services" here and "works" in the prior information notice
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SERVICES`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode` = `WORKS`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the park benches`
- Why: The same lot `LOT-2` is works in 01 and services (sub-type `INSTALL`, CPC 87390) here, in 03 and in 21, with a different name; nothing says the nature was changed. The value that deviates is in 01, and the fix belongs there (logistics refuted the finding for 02 on that ground); it stays a finding here because this example is one side of the contradiction (section 4).
- Condition: lot 2 has the same name and procurement type in every document of the flow, or the change is stated.
- Options: (a) preferred: correct 01 (services, "Installation of the benches"); this example stays as it is; (b) works everywhere; (c) state the change against the prior information in this notice.
- Needs decision: no
- From: broad (F4), context (F4); logistics refuted it for this example (Considered and refuted)

### tender/02#F6 · Medium · A language code in `LocaleCode`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language of `cbc:ID`; it names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `-rl` for files).
- Condition: `LocaleCode`, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) preferred: remove `LocaleCode`; (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F10), context (F10), logistics (F7), parties (F1)

### tender/02#F7 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Lumeport Public Works Department (a local authority), Bayvarra Information Service (ISIC 8411) and the Procurement Review Board of Bayvarra (ISIC 8423) are public bodies, described with a liquidation status ("A code signifying the party's liquidation status", `ACTIVE`) and a register of type `COMMERCIAL` ("A register of businesses"). A public body is not a business in a commercial register and cannot be in liquidation; the world's list has no register type for public bodies.
- Condition: a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop `CompanyLiquidationStatusCode` for public bodies and type their scheme differently (a new code), or keep only the identifier; (b) state in the world's rules that public bodies are entered in the federal business register, and drop at least the liquidation status.
- Needs decision: no
- From: broad (F21, Low), parties (F4, Low)

### tender/02#F8 · Medium · Variants flagged as unconstrained in number, with a maximum of one
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:VariantConstraintIndicator` = `true`
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:MaximumVariantQuantity` = `1`
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:VariantConstraintCode` = `ALLOWED`
- Why: `VariantConstraintIndicator` is "An indicator that variants are allowed and unconstrained in number (true) or not allowed (false)." With a maximum of one, `true` asserts the opposite of the limit next to it; `ALLOWED` and the maximum already say what is meant.
- Condition: the indicator is not `true` while a maximum number of variants is given.
- Options: (a) preferred: leave the indicator out; (b) drop the maximum.
- Needs decision: no
- From: broad (F5), context (F6)

### tender/02#F9 · Medium · Tender guarantee of 2400.00 is not 2 % of any amount the notice states
- XPath: `/ContractNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: `AmountRate` is "The rate used to calculate the amount of liability in this financial guarantee." Recalculated: 2 % of 124080.00 = 2481.60; of lot 1's 119760.00 = 2395.20; of lot 2's 4320.00 = 86.40; 2400.00 is 2 % of 120000.00, which the document does not contain. The certificate follows the amount (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`). Medium, not High (money) nor Low (broad): no base is stated, so no product can be shown to fail (2395.20 rounded is a reading), but the base the rate needs is missing.
- Condition: liability amount = rate × a stated base (with the rounding said), or no rate is given.
- Options: (a) preferred: drop `AmountRate` and describe the guarantee as a fixed 2400 lume; (b) state base and rounding; (c) the calculated amount here and in 14.
- Needs decision: no
- From: money (F2, High), broad (F14, Low)

### tender/02#F10 · Medium · Turnover criterion: "at least" in the text, "greater than" in the code, threshold not twice the estimate
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- Why: "At least" is ≥, `GT` and ">" exclude the threshold; the world's list has `GE`. 2 × 124080.00 = 248160.00, not 250000.00 (a turnover of 249000 meets the expression and fails the threshold); `ThresholdAmount` is an "Estimated monetary amount of the threshold", so rounding is possible, but not said.
- Condition: description, code, expression and threshold state the same comparison against the same limit.
- Options: (a) preferred: `GE`, "≥", and the description naming 250000 lume; (b) threshold 248160.00; (c) "more than" in the text.
- Needs decision: no
- From: money (F4), broad (F15, Low), context (F15, Low)

### tender/02#F11 · Medium · Subcontract terms: a "precise" share equal to the maximum, an amount that is 3.5 % of the estimate, and a price flagged as known
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:UnknownPriceIndicator` = `false`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`
- Why: `Rate` is "The precise percentage allowed to be subcontracted", `MaximumPercent` "The maximum percentage allowed to be subcontracted", `Amount` "The monetary amount assigned to the subcontracted task". The buyer sets a ceiling of 30 %, so a "precise" 30 % says something else at the same time. The amount is lot 2's estimate, 3.48 % of 124080.00 (30 % would be 37224.00); the award documents pair the same amount with the matching rate (`22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`), so the flow uses `Rate` once as a limit and once as the actual share. `UnknownPriceIndicator` `false` says a subcontract price is known before any tender. Broad refuted it (amount under the maximum; redundancy, not contradiction); the merge agrees that `Amount` is not defined as rate × base (hence not High), but `Rate` carries a meaning other than its definition (hence Medium).
- Condition: the buyer's terms state the limit it sets (and, if wanted, the subcontractable task with its estimate, explained), and nothing about a subcontract price that does not exist yet.
- Options: (a) preferred: keep `MaximumPercent`, `SubcontractingConditionsCode` and `Description`; remove `Rate`, `Amount` and `UnknownPriceIndicator`; (b) keep `Amount` as the installation estimate, explained, without `Rate`.
- Needs decision: no
- From: money (F1, High), context (F17, Low); broad refuted it (Considered and refuted)

### tender/02#F12 · Medium · Identifier of an "original" framework agreement in a procedure that reopens nothing
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ContractingSystem/cbc:Description` = `Framework with one supplier.`
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: `OriginalContractingSystemID` is "When reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system." This open procedure sets up a new framework (`FW-1`); it does not reopen competition under an existing one. A 2024 framework appears nowhere else, only as this ID in 02, 03 and 21 (`grep -l PWD-FW-2024-PARKS world/examples/tender/*.xml`). The definition's condition is not met, and the reader is told of an older framework the story does not have.
- Condition: the element is present only in a procedure that reopens competition under an existing framework or DPS, and then identifies it.
- Options: (a) preferred: remove it; (b) mention a predecessor framework in a note, if wanted; (c) make the procedure a call-off under a 2024 framework (story change).
- Needs decision: no
- From: broad (F7), context (F12, Needs decision yes), logistics (F4)

### tender/02#F13 · Medium · Periods for invitations and requests to participate in an open procedure
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-02-26`
- Why: The three periods are "The period during which invitations to tender must be completed and delivered", "… the invitation to participate must be sent" and "… requests for participation must be completed and delivered": steps of a procedure with a selection stage (restricted, negotiated; own knowledge of procurement practice). In an open procedure any operator tenders by the deadline without request or invitation, and the tenders of the flow (15, 17, 19) are submitted without one. Yet the flow does contain an expression of interest (04/05) and a qualification application (06/07) before the tenders, the pattern of a two-stage procedure, which may be what the periods were meant to carry; but every document calls the procedure open, so the preferred fix is encoding.
- Condition: the notice carries only the periods its procedure has; if the world's open procedure has a registration step (04/05), only the period that governs it is present and 04 lies inside it.
- Options: (a) preferred: remove the three periods (or keep only `ParticipationRequestReceptionPeriod` as the registration period, ending after 04); (b) make the procedure a restricted one, consistent with 04 to 07 (story change).
- Needs decision: no
- From: broad (F6, Needs decision yes), context (F11), logistics (F5, Needs decision yes)

### tender/02#F14 · Medium · The price of paper copies in the element for the reimbursement fee of concessions, three times
- XPath: `/ContractNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: `RequiredFeeAmount` is "The amount of the reimbursement fee for concession procurement projects" and `FeeDescription` "Text describing the reimbursement fee for concession procurement projects." Neither the project nor its lots are concessions, and the 50 lume are the price of paper copies, which `DocumentationFeeAmount` already states. The fee is stated four times, three in an element that means something else; repeated per lot it also reads as 50 lume per lot, while the tender pays it once (`15-Tender.xml:/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`).
- Condition: no concession fee in a project or lot that is not a concession; the documentation fee stated once, in `DocumentationFeeAmount`, with its explanation in a text of the tendering terms.
- Options: (a) preferred: remove the elements from the project and both lots and move the sentence to a `TenderingTerms/Note`; (b) none other seen.
- Needs decision: no
- From: broad (F8), context (F8), money (F5)

### tender/02#F15 · Medium · A strategic-procurement code in the element for an additional procurement type, also on the installation lot
- XPath: `/ContractNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/ContractNotice/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementType` = `Environmental impact: recycled steel and certified timber are asked`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementTypeCode` = `GREEN`
- Why: `ProcurementTypeCode` is "A code signifying the type of procurement project (e.g., goods, works, services)". `GREEN` ("Environmental impact", eForms env-imp) is a policy objective, not a type of procurement; eForms practice (BT-06, own knowledge) does not change the UBL meaning. On lot 2, the installation, the text "recycled steel and certified timber are asked" does not apply at all.
- Condition: `ProcurementAdditionalType` carries a type of procurement; the environmental objective is stated where UBL has a place for it (the execution requirement already states it), or the difference is recorded for the TC.
- Options: (a) preferred: state the additional nature that applies, and the environmental aim in `ContractExecutionRequirement`/`SpecificTendererRequirement`; at least remove it from lot 2; (b) keep the eForms encoding and record it as a finding for the UBL TC.
- Needs decision: yes
- From: broad (F9), context (F9)

### tender/02#F16 · Medium · Framework values: the "estimated" value leaves out the renewal, the "maximum" is below what the terms allow
- XPath: `/ContractNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount` = `148896.00`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:MaximumValueAmount` = `186120.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount` = `148896.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cac:ContractExtension/cac:Renewal/cbc:Amount` = `62040.00`
- Why: `EstimatedMaximumValueAmount` is "The estimated value which will be spent within a framework agreement over its whole duration, including options and renewals"; `MaximumValueAmount` "The maximum Value which can be spent … including options and renewals." Recalculated: estimate 124080.00 (240 benches), base maximum 148896.00 (288 benches), renewal 62040.00 (120 benches). 148896.00 is the base maximum without the renewal, so it is neither an estimate nor "including renewals" (124080 + 62040 = 186120.00); 186120.00 is the estimate plus the renewal, while the terms allow 148896 + 62040 = 210936.00. Broad refuted it: the estimate may be the expected spend with tolerance and the maximum a ceiling set by the buyer, below the arithmetic maximum. The merge accepts that a buyer may set a lower ceiling (the maximum part is therefore the weaker one), but 148896.00 still excludes the renewal the definition includes.
- Condition: `EstimatedMaximumValueAmount` includes the renewal; `MaximumValueAmount` is the ceiling the terms allow, or the document says that the renewal counts against a lower ceiling.
- Options: (a) preferred by money: estimated 186120.00, maximum 210936.00; (b) keep 186120.00 as the ceiling for everything and say so (lower the base maximum or count the renewal against it), with the estimate 186120.00 or less accordingly.
- Needs decision: yes
- From: money (F3); broad refuted it (Considered and refuted)

### tender/02#F17 · Medium · Request lines: minimum and maximum amount are unit prices, the estimated amount is a line total
- XPath: `/ContractNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- Why: "The minimum amount allowed for this deliverable", "The maximum amount allowed for this deliverable" and "The estimated total amount of the deliverable" refer to the same deliverable; the estimate is the total for 240 benches (240 × 499), minimum and maximum are prices of one bench. Read by the definitions, the line allows at most 600.00 for a deliverable estimated at 119760.00. The unit-price limits already sit in the price criterion.
- Condition: minimum, maximum and estimated amount of a line are on the same basis.
- Options: (a) preferred: line totals (84000.00 and 144000.00 for 240 benches) in the lines, unit-price limits only in the price criterion; (b) drop minimum and maximum from the lines and state the unit-price limits in a note.
- Needs decision: no
- From: money (F6)

### tender/02#F18 · Low · Urvanian declared as a language of the notice, but the notice has no Urvanian text
- XPath: `/ContractNotice/cbc:NoticeLanguageCode` = `en`
- XPath: `/ContractNotice/cac:AdditionalNoticeLanguage/cbc:ID` = `qau`
- Why: `AdditionalNoticeLanguage` is "An additional official language used in this contract notice" (as context quotes it). Every text is given once, in English; no element has a `languageID` (0 in this file). Broad refuted only why Urvanian is offered (Urvanian tenderers under the Trade Accord), which the merge accepts.
- Condition: every declared language is used in the notice, or it is not declared.
- Options: (a) preferred: Urvanian renderings of the main texts; (b) remove the additional language.
- Needs decision: no
- From: context (F22)

### tender/02#F19 · Low · Customs trader number of the contracting party in a tendering document
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The contract notice declares nothing to customs; the number is used when the benches are imported (31). Copied master data (section 4.8).
- Condition: a party carries the identifiers the document uses; no customs number in a procurement notice.
- Options: (a) preferred: leave it to the customs documents; (b) keep it only under a stated world rule.
- Needs decision: no
- From: context (F23), parties (F2)

### tender/02#F20 · Low · The department's tax exemption reason is worded as a sale
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: In `PartyTaxScheme` the exemption reason is "A reason for the party's exemption from tax". The text starts with "Sale to a public body", a transaction; the code's definition ("A body of the federation, a state or a city buys free of sales tax") fits the party. Money refuted it because the second half states the status; the merge keeps it at Low because the first half describes a sale.
- Condition: the party's exemption reason states the party's status; the transaction's reason stays on the tax categories.
- Options: (a) preferred: reword to "Public body: buys free of the state sales tax", keep the code; (b) a separate party-status code.
- Needs decision: no
- From: broad (F22), parties (F3); money refuted it (Considered and refuted)

### tender/02#F21 · Low · Eight further roles all filled with the contracting party itself
- XPath: `/ContractNotice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AdditionalInformationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:ContractResponsibleParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TenderEvaluationParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:QualificationRequestRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The contracting party, which acts `/ContractNotice/cac:ContractingParty/cac:ContractingRepresentationType/cbc:RepresentationType` = `On its own behalf`, is repeated by register number and name only in eight roles that exist for the case that another body or office does the task. They say nothing the `ContractingParty` does not say (no fillers). Context asked whether the parks department ("Head of parks" on the committee) is a body of its own that would be the real originator or beneficiary (story); the preferred option does not need that answer. Kept Low, as the contest merges did for originator and beneficiary equal to the buyer.
- Condition: a role party is present only where it differs from the contracting party or adds role-specific details.
- Options: (a) preferred: leave out the repetitions; keep `TenderRecipientParty` or `AdditionalInformationParty` only with their own contact; (b) make the parks department the originator or beneficiary (story); (c) keep all as an explicit statement.
- Needs decision: no
- From: context (F21, Needs decision yes), parties (F5)

### tender/02#F22 · Low · Maximum advertisement amount of 500 lume: advertised value or advertising cost?
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:AdvertisementAmount` = `320.00`
- Why: "The maximum advertised monetary value of the tendering process": read literally, 500.00 is neither the estimate nor the maximum of the procedure (broad, context). Money refuted that reading: the element pairs with `TenderResult/AdvertisementAmount` ("The monetary value of the advertisement for this tendering process"), 320.00 in the award notice, so both are the advertising cost (the CODICE meaning). The merge cannot settle which reading UBL means; nothing in the notice explains the 500.
- Condition: the amount fits the definition as the world reads it, with a stated reason, or the element is absent.
- Options: (a) preferred: decide the reading; if advertising cost, say in a note that the awardee bears it up to 500 lume and record the unclear definition for the TC write-up; (b) remove it; (c) the advertised maximum value.
- Needs decision: yes
- From: broad (F13), context (F7, Medium); money refuted it (Considered and refuted)

### tender/02#F23 · Low · Penalty clause without the amount its percentages apply to
- XPath: `/ContractNotice/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.`
- Why: The base of the percentages is not stated; the flow applies them to the installation price of one release (`34-DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`), one choice among several.
- Condition: the clause names its base, and it is the base the debit note uses.
- Options: (a) preferred: "0.5 % of the price of the late part of a release per day late, at most 10 % of that price"; (b) another base, with the debit note following it.
- Needs decision: no
- From: money (F10)

### tender/02#F24 · Low · The qualification request is given the role "consortium lead"
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:EconomicOperatorRole/cbc:RoleDescription` = `Leads a consortium.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:CompanyLegalForm` = `Any legal form; consortia must name a lead member.`
- Why: `EconomicOperatorRole` ("A class to describe the tenderer contracting role") makes the only qualification request apply to consortium leads only, although it is asked of every tenderer and the tenderers of the flow tender alone; the world's list also has `SOLE`.
- Condition: the role matches who must meet the request, or is absent.
- Options: (a) preferred: remove the role; (b) one request per role.
- Needs decision: no
- From: broad (F16), context (F16)

### tender/02#F25 · Low · The tender preparation is tied to lot 1 only
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TenderPreparation/cac:ProcurementProjectLot/cbc:ID` = `LOT-1`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TenderPreparation/cbc:Description` = `One encrypted envelope per tender.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric` = `2`
- Why: The only `TenderPreparation` names lot 1, while its texts speak of one envelope per tender and unit prices per lot, and a tenderer may tender for both lots; nothing says how a tender for lot 2 is prepared.
- Condition: the tender preparation covers every lot a tender can be submitted for.
- Options: (a) preferred: remove the lot from the preparation; (b) name both lots.
- Needs decision: no
- From: context (F18)

### tender/02#F26 · Low · Design-contest and negotiation indicators in an open supply procedure
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:PrizeIndicator` = `false`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:FollowupContractIndicator` = `false`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:BindingOnBuyerIndicator` = `true`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:NoFurtherNegotiationIndicator` = `true`
- Why: `PrizeIndicator` and `FollowupContractIndicator` belong to design contests and with `false` only state what absence says; `BindingOnBuyerIndicator` is the jury-decision indicator of a contest (eForms, own knowledge), while here the buyer's own committee evaluates; `NoFurtherNegotiationIndicator` says something only where negotiation is possible, not in an open procedure.
- Condition: the awarding terms of this open supply procedure carry none of these indicators, unless the document explains what each refers to.
- Options: (a) preferred: remove all four; (b) keep `NoFurtherNegotiationIndicator` only under a stated rule of the world's act.
- Needs decision: no
- From: broad (F17, the two contest indicators), context (F13, all four)

### tender/02#F27 · Low · Values that only state the default: normal urgency, no reduction of candidates, not terminated
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:UrgencyCode` = `NORMAL`
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:CandidateReductionConstraintIndicator` = `false`
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:TerminatedIndicator` = `false`
- Why: `UrgencyCode` `NORMAL` says the procedure is not urgent; `CandidateReductionConstraintIndicator` ("An indicator that the number of candidates participating in this process has been reduced (true) or not (false)") says nothing was reduced in an open procedure that has no candidates to reduce (broad grouped it with the restricted-procedure periods, F13); `TerminatedIndicator` ("An indicator that the competition launched is terminated") says that a procedure being announced is not over. Each states what its absence implies (UBL IND6).
- Condition: the tendering process carries these elements only where they say something other than the default.
- Options: (a) preferred: remove the three; (b) none other seen.
- Needs decision: no
- From: context (F24), broad (F17 for TerminatedIndicator, F6 for CandidateReductionConstraintIndicator)

### tender/02#F28 · Low · Quality criterion: a range of 5 to 10 years without explanation, and one sub-criterion of half its weight
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:WeightNumeric` = `40`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MinimumQuantity` = `5`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:MaximumQuantity` = `10`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric` = `20`
- Why: "Quality" has a range in years but no description or expression (presumably the warranty offered, the required warranty being 5 years); its only sub-criterion "Durability of the coating" weighs 20 of 40. Money refuted the weight part (the rest is the warranty scored by the parent); plausible, but not stated.
- Condition: the criterion says what its range measures, and its sub-criteria or description account for its weight.
- Options: (a) preferred: two sub-criteria (coating 20, warranty years 20 with the range) and a description; (b) a description only; (c) remove the range.
- Needs decision: no
- From: broad (F18), context (F19); money refuted the weight part (Considered and refuted)

### tender/02#F29 · Low · Technical committee of three officers, one named
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:TechnicalCommitteeDescription` = `Three officers of the department.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:TechnicalCommitteePerson/cbc:FamilyName` = `Delling`
- Why: The description says three officers; one `TechnicalCommitteePerson` ("A member of a committee of experts …") is listed.
- Condition: the persons listed and the description agree.
- Options: (a) preferred: say that Mara Delling chairs and the others are appointed later; (b) list all three.
- Needs decision: no
- From: parties (F6)

### tender/02#F30 · Low · Contact of the review board's registry described as a procurement officer
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: `AppealReceiverParty` is "The Party who receives the appeal." Its contact is the registry of the review board, but job title and department are those of the buyer's contact; a registry of a review body does not buy. Name, job title and department do not agree.
- Condition: name, job title and department describe one function that fits receiving appeals.
- Options: (a) preferred: e.g. "Registrar" in "Registry"; (b) drop job title and department.
- Needs decision: no
- From: broad (F20), parties (F7)

### tender/02#F31 · Low · The place of an electronic opening named after the department and a square
- XPath: `/ContractNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:OccurrenceLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:Description` = `Electronic opening; tenderers may follow it online.`
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:SubmissionMethodCode` = `ELECTRONIC`
- Why: `OccurrenceLocation` is "The location of this event". The opening is electronic and followed online, but the location names the organisation and its square (the name is the place, not the company), without the address identifier the same building has in this document (`/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`) and without the address of the online session. It is not clear whether anyone can attend on site.
- Condition: the location of the opening is where it can be attended (the online session, or a named room with its address), or it is absent for a purely electronic opening.
- Options: (a) preferred by context: remove the location and give the platform address in the description; (b) preferred by parties: name the room and give the address of Civic Square 6 with its register ID, saying that attendance on site is possible. The merge prefers (a): the description says the opening is electronic.
- Needs decision: no
- From: context (F27), parties (F8)

### tender/02#F32 · Low · Lot 2 (installation) is described with the data of the bench supply
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:EstimatedOverallContractQuantity` = `240`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cbc:OptionsDescription` = `One extension of a year with 120 more benches.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- Why: A lot's `ProcurementProject` describes that lot. Lot 2 is an installation service (CPC 87390), but its description and option text are those of the whole project, the same as lot 1's (which covers delivery and anchoring together); its quantity is 240 "each" without saying of what, and it has no request-for-tender line of its own, while lot 1's line contains the sub-line "Ground anchor set" and an estimate (240 × 499 = 119760.00) that leaves out lot 2's 4320.00. It is not clear in which lot the anchors are. (Lot 2's additional classification "Furniture" is in F33.)
- Condition: each lot describes what that lot buys, with its own quantity and option text; it is clear in which lot the ground anchors are.
- Options: (a) preferred: each lot its own description (e.g. "Anchoring of 240 benches in the parks of Lumeport over two years") and a request line for the installation; (b) only name, type, classification and amounts on the lots.
- Needs decision: no
- From: broad (F11), context (F26)

### tender/02#F33 · Low · The additional classification is the parent group of the main one; the installation is not classified at project level, and lot 2 is classified as furniture
- XPath: `/ContractNotice/cac:ProcurementProject/cac:MainCommodityClassification/cbc:ItemClassificationCode` = `38111`
- XPath: `/ContractNotice/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:MainCommodityClassification/cbc:ItemClassificationCode` = `87390`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- Why: `AdditionalCommodityClassification` is "An association to additional classification categories for the deliverable requested." CPC 381 "Furniture" contains the main class 38111 and adds nothing; the installation is not classified at project level although lot 2 carries 87390; and lot 2 lists "Furniture" as an additional category of an installation service.
- Condition: additional classifications name categories the main one does not already imply; the project shows both deliverables.
- Options: (a) preferred: 87390 as the project's additional classification, no "Furniture" on lot 2; (b) remove the additional classifications.
- Needs decision: no
- From: context (F20), broad (F11, lot 2's 381)

### tender/02#F34 · Low · Works quality control stated for a supply project and both lots
- XPath: `/ContractNotice/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:QualityControlCode` = `INSPECTION`
- Why: `QualityControlCode` is "The indication of whether or not the control quality is included in the works project." The project is supplies and lot 2 services; "Inspection on delivery" is an acceptance rule for goods.
- Condition: `QualityControlCode` only for a works project or lot; the inspection of deliveries stated as an acceptance term.
- Options: (a) preferred: remove it and state the inspection in the contract conditions or a note; (b) none other, as no lot of this notice is works.
- Needs decision: no
- From: context (F14)

### tender/02#F35 · Low · Lot-level tendering terms and process that only say "As for the procedure."
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:TenderingProcess/cbc:Description` = `As for the procedure.`
- Why: Four aggregates for what is specific to a lot each hold one sentence saying that nothing differs, which is what their absence means (no fillers). See also F36: some terms in fact do not fit lot 2.
- Condition: a lot carries tendering terms or a process only where something is specific to it.
- Options: (a) preferred: remove the four aggregates; (b) put real lot-specific terms there (F36).
- Needs decision: no
- From: broad (F12), context (F25)

### tender/02#F36 · Low · Money terms set for the whole procedure do not fit a tender for lot 2 alone
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:PartPresentationCode` = `ONEORMORE`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`
- Why: Tenders may be made for one lot, and lot 2 takes its terms from the procedure. Lot 2 is estimated at 4320.00 (18 lume per bench). For it, the price limits of 350 to 600 lume cannot be met by any unit price; the auction "on the unit prices of both lots" has a step only for "the bench's unit price" (2 lume would be 11 % of the installation price); the guarantee of 2400.00 is 56 % of the lot's estimate, and the turnover threshold 58 times it (all recalculated). The terms were written for lot 1 or for both lots together.
- Condition: every money term that applies to lot 2 can be met by a tender for lot 2 alone, or the document says that lot 2 can only be tendered together with lot 1.
- Options: (a) preferred: price limits, bid step, guarantee and turnover threshold per lot in each lot's tendering terms; (b) require tenders for both lots (group G-1 exists) and say so.
- Needs decision: yes
- From: money (F7)

### tender/02#F37 · Low · An electronic auction is announced, but the flow shows no trace of it
- XPath: `/ContractNotice/cac:TenderingProcess/cac:AuctionTerms/cbc:AuctionConstraintIndicator` = `true`
- XPath: `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:LowerTenderAmount` = `119040.00`
- Why: `AuctionConstraintIndicator` "Indicates whether an electronic auction will be used before the awarding of a contract". The award is made at exactly the winner's original tender (`15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`), and the lowest tender reported is the other tenderer's original amount. No document between the opening (2026-02-26) and the award mentions an auction held or not held. It may have brought no bids; the flow does not say so.
- Condition: the flow shows what became of the announced auction, or the procedure has no auction.
- Options: (a) preferred: say in the award documents that the auction of a given date brought no lower bids; (b) let the auction lower a price and carry it through award, contract, catalogue, order and invoice; (c) remove the auction.
- Needs decision: yes
- From: money (F9), logistics (Outside this review)

### tender/02#F38 · Low · The whole two-year amount on one budget account of 2026
- XPath: `/ContractNotice/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:BudgetAccountLine/cac:BudgetAccount/cbc:BudgetYearNumeric` = `2026`
- Why: The releases run 2026-03-23 to 2028-03-22, paid 30 days after each, so spending falls in 2026 to 2028; the single line charges the full estimate to a 2026 account without saying it is a multi-year commitment.
- Condition: the budget line(s) show the budget years of the spending, or say that the line is a two-year commitment of the 2026 budget.
- Options: (a) one budget account per year; (b) preferred, smallest: a note that it is a two-year commitment of the 2026 budget.
- Needs decision: yes
- From: money (F11)

### tender/02#F39 · Low · The buyer's estimates equal the winning tender to the cent
- XPath: `/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `119760.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- Why: Valdara's tender of 2026-02-25 offers exactly the estimates of this notice, in both lots, while the other tenderer offers 119040.00. An estimate met to the cent reads as the outcome copied back; all derived figures (minimum, maximum, renewal, average release, budget line, framework values) inherit it.
- Condition: the buyer's estimate differs from the tendered prices, or the story explains the equality.
- Options: (a) preferred: a rounded estimate (e.g. 500 and 20 lume per bench: 124800.00) with derived amounts following it; (b) say in the tender that it offers the published estimate.
- Needs decision: yes
- From: money (F8)

## Checked and consistent
- TenderingTerms equal those of 01 leaf for leaf, plus `AppealReceiverParty` and `MediationParty`; the project's `ProcurementProject` equals that of 01 (broad, by script).
- Amounts (redone): lot 1 119760.00 = 240 × 499; lot 2 4320.00 = 240 × 18; sum 124080.00; minimums 59880 + 2160 = 62040, maximums 143712 + 5184 = 148896, renewals 59880 + 2160 = 62040, average releases 19960 + 720 = 20680 = 124080 / 6; lot 2's renewal 2160.00 = 120 × 18.
- Award weights 60 + 40 = 100 match the description; WSUM, BESTVALUE and INVERSE fit; price limits 350–600 contain 499, 470 and 480 (tenders 15, 17, 19); the auction terms agree with the bid step of the price criterion.
- Dates after the issue time: additional information until 2026-02-19; documents until 2026-02-25; tender deadline 2026-02-26 12:00; opening `OPEN-1` 2026-02-26 14:00, scheduled and not completed; guarantee constituted by 2026-02-26; tenders 15, 17, 19 before the deadline; framework 24 months = planned period; `FrequencyPeriod` 4 years agrees with "about four years" and 2030.
- `NoticeDocumentReference` `LPWD-DOC-26-0187` is 01; 04 and 21 refer to this notice by `LPWD-DOC-26-0188`; `TenderingProcess/ID` is the same in 03, 08, 21, 24; lot references and per-lot technical documents agree with 03.
- Tax category E / STT on project and lots agrees with the department's tax scheme; PERRELEASE agrees with "30 days after each accepted release"; expense code INVESTMENT fits.
- Codes: CPC 38111, 381, 87390; ISIC 8411, 8423; unit codes ANN, MON, DAY, EA, SET; OID = AES-256-GCM; all world-list codes resolve; XBL and XUF are not ISO 4217 codes; telephone code +999 unassigned.
- `check_ids.py`: no identifier with a check digit.
- Parties identical to their descriptions in the other examples of the flow (parties, by script), apart from the findings.

## Considered and refuted
- `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode`: `SERVICES` against `WORKS` in 01 — refuted by logistics for this example because 02, 03 and 21 agree and the deviating value is in 01 — the merge keeps it as F5, with the fix in 01 (from logistics).
- `/ContractNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount`: does not include the renewal — refuted by broad (expected spend vs ceiling, both readings possible) — the merge keeps money's finding as F16, Needs decision yes (from broad).
- `/ContractNotice/cac:TenderingProcess/cbc:GovernmentAgreementConstraintIndicator`: `true` without naming the agreement, or asserting the WTO GPA — refuted because the Lumeport Trade Accord can be "a government procurement agreement" and Urvanian tenderers take part (from broad, context).
- `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:MediationParty`: the review board both receives appeals and mediates — refuted, a review body may offer mediation; it is identified consistently in the three appeal roles (from broad, context, parties).
- `/ContractNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate`: rate and maximum both 30 with an amount of 4320 — refuted by broad (redundant, not contradictory) — the merge disagrees in part and keeps F11 (from broad).
- `/ContractNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:Contact`: a name only — refuted, the procurement office is fully described as the contracting party's contact (from broad).
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` not ISO 8601 — refuted, text without prescribed format, unambiguous (from broad, parties).
- `/ContractNotice/cac:AdditionalNoticeLanguage/cbc:ID`: Urvanian as additional language — refuted, Urvanian tenderers take part under the Trade Accord; the missing Urvanian text is F18 (from broad).
- `/ContractNotice/cac:TenderingTerms/cbc:FundingProgramCode`: no listID — refuted, the department's own programme number (party-internal codes are exempt) (from context, logistics; broad's finding under "Refuted in the merge").
- `/ContractNotice/cac:TenderingTerms/cac:LotDistribution/cbc:MaximumLotsSubmittedNumeric`: says nothing — refuted, explicit statement that both lots may be tendered for and won (from context).
- `/ContractNotice/cac:ProcurementProject/cbc:RequestedDeliveryDate`: one date for two years — refuted, the first release (from context).
- `/ContractNotice/cac:ProcurementProject/cbc:ProcurementSubTypeCode`: PURCHASE — refuted, a sub-type of supplies (from context).
- `/ContractNotice/cac:ProcurementProject/cbc:SMESuitableIndicator`: against the turnover and staff thresholds — refuted, such a firm is still small (from context).
- `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cbc:OperatingYearsQuantity` and `cbc:EmployeeQuantity`: the model prints the legal-form definition — refuted, an error of the UBL model (from context; a note for the TC write-up).
- `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealInformationParty`: wrong party — refuted, the review board is the natural source (from context).
- `/ContractNotice/cac:TenderingTerms/cac:ContractResponsibleParty`: could mean the contractor — refuted, a buyer-side role here; the repetition is F21 (from context, parties).
- `/ContractNotice/cac:TenderingProcess/cac:ProcessJustification`: filler or missing threshold — refuted, a real reason, and the threshold is a matter of the referenced act (from context, money).
- `/ContractNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:ExpectedOperatorQuantity` and `cbc:MaximumOperatorQuantity`: redundant — refuted, they agree with "Framework with one supplier." and the single award (from context).
- `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid`: consistent with the auction conditions (from context).
- `/ContractNotice/cac:FrequencyPeriod`: consistent with the recurrence (from context).
- `/ContractNotice/cac:ProcurementProjectLot[1]/cac:LegalDocumentReference/cbc:ID`: an act as "legal document" — refuted, an act is a legal document (from logistics).
- `/ContractNotice/cac:TenderingProcess/cbc:ContractingSystemCode`: FRAMEWORK in two elements from two lists — refuted, both exist in UBL and agree (from logistics).
- `/ContractNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate`: opening on the deadline day — refuted, 14:00 is after 12:00 (from logistics).
- `/ContractNotice/cac:TenderingProcess/cac:AdditionalInformationRequestPeriod/cbc:EndDate`: the status request 08 comes a day after it — refuted, a status request is not a request for additional information (from logistics).
- `/ContractNotice/cac:TenderingTerms/cbc:MaximumAdvertisementAmount`: 500.00 against the advertised value — refuted by money (pairs with `AdvertisementAmount` 320.00) — the merge cannot settle it: F22, Low, Needs decision yes (from money).
- `/ContractNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount`: 119760.00 not adding up to 124080.00 — refuted, the difference is lot 2 without a goods line (from money).
- `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cac:Renewal/cbc:Amount`: renewal "with 120 more benches" in the installation lot — refuted, 2160.00 = 120 × 18 is their installation (from money).
- `/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: says nothing about the later invoice's taxes — refuted, those depend on the supplier, unknown here (from money).
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason`: transaction wording — refuted by money (second half states the status) — the merge keeps F20 (from money).
- `/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric`: 20 of 40 — refuted by money (the warranty scored by the parent) — kept in F28 (from money).
- `/ContractNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate`: 2 rather than 0.02 — refuted, the flow's convention, not fixed by UBL (from money).
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: belongs in `Room` — refuted, fits the definition (from parties).
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: functional name; two department wordings — refuted (from parties).
- `/ContractNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: `STATE` for a local authority — refuted, the level of the tax (from parties).
- `/ContractNotice/cac:ReceiverParty`: an information service as receiver — refuted, the publication service (from parties).

## Refuted in the merge
### broad/F19 · Low · Funding programme code without a list
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26`
- Why (broad): every code has a listID except party-internal codes; `PARKS-26` has none.
- Condition (broad): the code names its list, or the programme is given as text only.
- Refuted because: `PARKS-26` is the department's own programme number, a party-internal code that the rule exempts, explained by `FundingProgram`; context and logistics refuted it on the same ground.

## Changed in the merge
- broad/F1, context/F5, logistics/F1 → F1: combined; both preferred options kept, without a preference of the merge (the parts disagree, and each changes the story differently).
- broad/F2, context/F1, logistics/F6 (Medium) → F2: High, as in 01.
- broad/F3 → split into F3 (call for tenders) and F4 (replaced notice), as context and logistics have them; Needs decision no (broad said yes), because the preferred options are encoding.
- broad/F4, context/F4 → F5: kept High although logistics refuted it for 02; the fix is placed in 01.
- broad/F21, parties/F4 → F7: Low raised to Medium (main table of `analysis/review-merge-decisions.md`, mergers B, C, D).
- money/F2 (High), broad/F14 (Low) → F9: Medium (no base stated); as in 01 and merger D.
- money/F4, broad/F15, context/F15 → F10: Medium.
- money/F1 (High), context/F17 (Low) → F11: Medium; broad's refutation in Why.
- broad/F7, context/F12 (yes), logistics/F4 → F12: Needs decision no; context's call-off option kept as (c).
- broad/F6 (yes), context/F11 (no), logistics/F5 (yes) → F13: Needs decision no, aligned with merger B (09): the procedure is OPEN in every document, so removing the periods is encoding; the restricted procedure stays as story option (b); `CandidateReductionConstraintIndicator` moved to F27.
- broad/F13 (Low), context/F7 (Medium) → F22: Low, Needs decision yes, money's refutation carried.
- context/F21 (yes), parties/F5 (no) → F21: Needs decision no; context's story question as option (b).
- broad/F17, context/F13, context/F24 → F26 (contest and negotiation indicators) and F27 (default values, with `TerminatedIndicator` and `CandidateReductionConstraintIndicator`): regrouped by kind.
- broad/F11, context/F26 → F32; lot 2's additional classification 381 from broad/F11 moved to F33 (with context/F20).
- context/F27, parties/F8 → F31: combined; the merge prefers context's option.
- money/F9 with logistics' Outside entry → F37.
- broad/F5, context/F6 → F8; broad/F8, context/F8, money/F5 → F14; broad/F9, context/F9 → F15; broad/F10, context/F10, logistics/F7, parties/F1 → F6; context/F23, parties/F2 → F19; broad/F22, parties/F3 → F20; broad/F16, context/F16 → F24; broad/F18, context/F19 → F28; broad/F20, parties/F7 → F30; broad/F12, context/F25 → F35: combined, severity unchanged.

## Outside this review
- Whether the contract notice should be issued only one day before the call for tenders and 15 days before the tender deadline is a timeline question of the flow (from broad).
- The expression of interest (04, 2026-02-14) and the qualification application (06, 2026-02-13) follow the end of the reception of requests to participate (2026-02-11); whether those documents belong in an open procedure is a question for their reviews and the story (from context; see F1 and F13).
- The invoice of the first release applies the supplier's standard terms rather than "30 days after each accepted release"; that lies in 32 (from money).
