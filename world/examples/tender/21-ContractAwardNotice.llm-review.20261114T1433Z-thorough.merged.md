# LLM review: 21-ContractAwardNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/21-ContractAwardNotice.xml`, Git blob `59a77855a9c7e78ea4690806b5a919a52b58df71` (committed)
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

### tender/21#F1 · High · The opening of tenders is still "scheduled" and not completed in the notice of the award
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate` = `2026-02-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:CompletionIndicator` = `false`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:CurrentStatus/cbc:ConditionCode` = `SCHEDULED`
- XPath: `/ContractAwardNotice/cbc:IssueDate` = `2026-03-13`
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:AwardDate` = `2026-03-09`
- Why: `CompletionIndicator` is "An indicator that this event has been completed (true) or not (false)". The notice, issued 2026-03-13, reports an award of 2026-03-09 on two received tenders (`/ContractAwardNotice/cac:TenderResult/cbc:ReceivedTenderQuantity` = `2`); the opening of 2026-02-26 14:00 necessarily took place, yet the notice says it is not completed and scheduled. The values are those of the contract notice and the call (02, 03), where they were true. (Broad's mention of "an auction held on 6 March" is not supported by the XML: no date of the flow belongs to an auction, see F13.)
- Condition: In the award notice the opening event is absent or marked completed, with a status that says it took place.
- Options: (a) `CompletionIndicator` true and a status for a completed event (preferred); (b) leave the opening event out of the award notice.
- Needs decision: no
- From: broad, logistics, context

### tender/21#F2 · High · Document availability and the invitation and participation periods start or end before the procedure was announced
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0188`
- XPath: `02-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-02-11`
- XPath: `03-CallForTenders.xml:/CallForTenders/cbc:IssueDate` = `2026-02-12`
- Why: The notice refers to the contract notice 02, issued 2026-02-11, and the call followed on 2026-02-12. By the periods here the documents were available from 2026-01-26, 16 days before they were issued, invitations had to be delivered by 2026-02-01 and participation requests by 2026-02-11, the day the procedure was announced. The expression of interest (04, 2026-02-14) and Brackenmere's qualification application (07, 2026-02-19) came after all of them ended. The start date fits the contract notice's requested publication date (27 January), not its issue date (logistics), so either the notices or the periods are misdated; which one moves is the procedure's calendar.
- Condition: Every period of the tendering process lies after the publication of the contract notice that announces it.
- Options: (a) start the document availability at the call for tenders (2026-02-12) and drop the periods an open procedure does not have (F3) (preferred); (b) move the contract notice and the call to late January, so the periods become true.
- Needs decision: yes
- From: broad, logistics (both High, needs decision yes); context listed the dates under "Outside this review"

### tender/21#F3 · Medium · Invitation and participation-request periods in an open procedure
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: `InvitationSubmissionPeriod` is "The period during which invitations to tender must be completed and delivered", `ParticipationInvitationPeriod` "The period during which the invitation to participate must be sent", `ParticipationRequestReceptionPeriod` "The period during which requests for participation must be completed and delivered": steps of a restricted or negotiated procedure. The procedure is open ("Open procedure with two lots."); nobody requests participation or is invited, and no document of the flow is such a request or invitation.
- Condition: A tendering process with `ProcedureCode` `OPEN` carries no periods for participation requests or invitations.
- Options: (a) remove the three periods (preferred); (b) describe a registration step of the world's open procedure and date it after the contract notice; (c) make the procedure a restricted one, which changes the story.
- Needs decision: no
- From: context, broad and logistics (both within their High finding, F2)

### tender/21#F4 · Medium · OriginalContractingSystemID in a process that reopens nothing
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`
- Why: The definition is conditional: "When reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system". This open procedure sets up a new framework with one supplier, whose releases are ordered without a new competition; a framework of 2024 occurs only in this element (01, 02, 03, 21; logistics, by grep).
- Condition: The element is present only in a mini-competition under an earlier framework or system that the documents describe.
- Options: (a) remove it (preferred); (b) mention a predecessor framework in text (the element still does not fit).
- Needs decision: no
- From: broad, logistics, context

### tender/21#F5 · Medium · PublishAwardIndicator true for a supply contract
- XPath: `/ContractAwardNotice/cbc:PublishAwardIndicator` = `true`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`
- Why: "An indicator specifying if the notice is published for service contracts within certain service categories (true) or not (false)." True says this is an award of a service contract of such a category; the procurement is a supply of benches (lot 2, the installation, is an accessory service of 4320.00 out of 124080.00), and the world names no such categories. The value seems meant as "the award may be published", which the element does not say. (In the contest flow the indicator was Low/yes, on a services procurement; here it is a supply.)
- Condition: The indicator is absent or false for a notice that is not about a service contract of the categories the definition means.
- Options: (a) remove it (preferred); (b) false; (c) define service categories and use it for lot 2 only.
- Needs decision: no
- From: broad, context

### tender/21#F6 · Medium · The two framework values are composed differently, and neither includes both the quantity option and the renewal
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount` = `148896.00`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:MaximumValueAmount` = `186120.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount` = `148896.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:ContractExtension/cac:Renewal/cbc:Amount` = `62040.00`
- Why: `EstimatedMaximumValueAmount` is "the estimated value which will be spent within a framework agreement over its whole duration, including options and renewals", `MaximumValueAmount` "the maximum value which can be spent … including options and renewals". Recalculated: the quantity option (at most 288 benches) gives 288 × 499 + 288 × 18 = 148 896.00, the renewal (120 more benches) 120 × 517 = 62 040.00. The estimate contains the option but not the renewal; the maximum (124 080.00 + 62 040.00 = 186 120.00) the renewal but not the option. What can be spent under the stated terms is 148 896.00 + 62 040.00 = 210 936.00, above the stated maximum. Not High, because a reading where the 288 benches already include part of the renewal is conceivable (money's option b), though 240 + 120 = 360 > 288 makes it unlikely. The same values are in 02 and 03.
- Condition: `MaximumValueAmount` is not lower than the highest base amount plus all renewals stated, and `EstimatedMaximumValueAmount` covers the same scope without exceeding it; both recomputable from the notice.
- Options: (a) maximum 210 936.00 and an estimate with renewal (e.g. 186 120.00) (preferred); (b) state in `OptionsDescription` that the 288 benches include the renewal's and adjust the renewal and the values.
- Needs decision: no
- From: money

### tender/21#F7 · Medium · The paper-copy fee as "reimbursement fee for concession procurement projects", three times, in a notice after the award
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: `RequiredFeeAmount` is "The amount of the reimbursement fee for concession procurement projects", `FeeDescription` its text. The project is a supply framework (`ProcurementSubTypeCode` PURCHASE), not a concession, and 50 lume is the price of a paper copy, for which UBL has `TenderingTerms/DocumentationFeeAmount` (used in 01–03). Stated per project and per lot it reads as 150 lume for both lots, which the text contradicts; in an award notice the documents can no longer be bought.
- Condition: No `RequiredFeeAmount`/`FeeDescription` in a project that is not a concession; the documentation fee is not repeated in the award notice.
- Options: (a) remove fee and description from project and lots (preferred); (b) once in `TenderingTerms/DocumentationFeeAmount`, if it must stay visible.
- Needs decision: no
- From: money, context

### tender/21#F8 · Medium · Unit prices as minimum and maximum amount of a deliverable whose estimate is a total
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- Why: The three are "The minimum amount allowed for this deliverable", "The maximum amount allowed for this deliverable" and "The estimated total amount of the deliverable"; the deliverable of the line is 240 benches. 350.00 and 600.00 are prices of one bench, 119 760.00 is 240 × 499.00, so as defined the line allows at most 600.00 for a deliverable estimated at 119 760.00. Counter-argument (broad, refuted): the call's price criterion defines the same range per bench, so the reading is fixed within the flow. The merge keeps it as Medium (context; money Low): the elements carry a per-unit meaning their definitions do not have, and nothing in the line says so.
- Condition: Minimum, maximum and estimate of a request-for-tender line are on the same basis, or the basis is stated in the line.
- Options: (a) line totals (240 × 350 = 84 000.00, 240 × 600 = 144 000.00), or drop the limits from the award notice (preferred); (b) state the per-bench basis in the line's note.
- Needs decision: no
- From: money (Low), context (Medium); broad refuted it

### tender/21#F9 · Medium · Language code in LocaleCode
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (`listID="ISO 639"`) repeats the language of `cbc:ID`. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code.
- Options: (a) remove `cbc:LocaleCode` (preferred by parties and context); (b) a locale such as `en-XB` from a locale list (preferred by broad).
- Needs decision: no
- From: broad, parties, context

### tender/21#F10 · Medium · Province in Region
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the administrative division `CountrySubentity` holds, as the Bayvarran addresses do. 219 occurrences in 104 examples (`grep -r --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: The province is in `CountrySubentity`; `Region` is absent or holds a region in its sense.
- Options: (a) move it to `CountrySubentity` (preferred).
- Needs decision: no
- From: broad, parties, context

### tender/21#F11 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The department, the Bayvarra Information Service and the Procurement Review Board are public bodies (ISIC 8411, 8411, 8423). A liquidation status has no meaning for them and a scheme of type `COMMERCIAL` ("A register of businesses") does not fit; the register numbers themselves are not questioned.
- Condition: Public bodies carry no liquidation status, and their registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and the `COMMERCIAL` type (preferred); (b) reduce their legal entity to registration name and identifier.
- Needs decision: no
- From: broad, parties, context

### tender/21#F12 · Low · The award notice is issued inside the appeal period, before the contract, and numbered before the notifications it follows
- XPath: `/ContractAwardNotice/cbc:ID` = `LPWD-DOC-26-0207`
- XPath: `/ContractAwardNotice/cbc:IssueDate` = `2026-03-13`
- XPath: `/ContractAwardNotice/cbc:RequestedPublicationDate` = `2026-03-14`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- XPath: `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `24-TenderContract.xml:/TenderContract/cbc:IssueDate` = `2026-03-19`
- XPath: `22-AwardedNotification.xml:/AwardedNotification/cbc:ID` = `LPWD-DOC-26-0208`
- Why: The notice announces the awarded contract while the unsuccessful tenderer's appeal period runs until 2026-03-19 and the contract is signed only on 2026-03-19 (24). In procurement practice (own knowledge, e.g. the EU directives) an award notice follows the conclusion of the contract, or at least the standstill. The department's running number places this notice (…0207) before the two notifications of 2026-03-09 (…0208 and …0209), issued four days earlier.
- Condition: The notice is issued after the contract is concluded (or says the award is not yet final), and its number fits its place in the department's sequence.
- Options: (a) issue it after 2026-03-19 with a number after the contract's (preferred); (b) keep the date and say the award is subject to the standstill.
- Needs decision: yes
- From: logistics

### tender/21#F13 · Low · An electronic auction is announced, and the award shows no trace of one
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:AuctionTerms/cbc:AuctionConstraintIndicator` = `true`
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:LowerTenderAmount` = `119040.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:HigherTenderAmount` = `124080.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `19-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`
- Why: `AuctionConstraintIndicator` "Indicates whether an electronic auction will be used before the awarding of a contract", and the terms invite every admissible tenderer to an auction on the unit prices after the evaluation. The awarded amount and the lowest and highest tender are exactly the totals as submitted, the award description does not mention an auction, and no document or date of the flow belongs to one. An award notice, whose purpose is to report the outcome, leaves open whether the auction was held without bids or not held.
- Condition: The notice reports the auction (held, with or without bids) or does not announce one.
- Options: (a) state in the tender result that the auction was held and no tenderer lowered its price (preferred by context); (b) drop the auction from the procedure in all its documents.
- Needs decision: yes
- From: logistics, context

### tender/21#F14 · Low · The estimate made before the procedure equals the winning tender to the cent
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:HigherTenderAmount` = `124080.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`
- XPath: `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- Why: The estimate, published from 01 on (12 January), is 240 × 499.00 + 240 × 18.00, exactly the unit prices Valdara later tendered. An estimate that matches a later tender on two separate prices is not plausible, and makes the notice's estimate indistinguishable from the result. Same as 15#F15.
- Condition: The estimate differs from the awarded amounts, or the notice explains why they coincide; the amounts derived from it follow.
- Options: (a) round estimates of its own (e.g. 500 and 20 lume a piece) in the notices of the flow (preferred); (b) keep the figures and say the estimate is the previous framework's price, which the tenderer matched.
- Needs decision: yes
- From: broad (needs decision no), money; context listed it under "Outside this review"

### tender/21#F15 · Low · The "precise percentage" subcontracted is rounded and does not give the amount
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted", `Amount` "the monetary amount assigned to the subcontracted task". Recalculated: 4320.00 / 124080.00 = 3.4816 %; 3.5 % of 124080.00 is 4342.80. The amount is right (240 × 18, line 2 of 15); the rate is a rounding. Counter-arguments: ordinary rounding to one decimal (broad); "allowed" read as the share the awarded tender subcontracts is legitimate in a result (context). The merge keeps it as Low: a "precise" percentage that does not reproduce the amount next to it.
- Condition: `Rate` × awarded amount / 100 equals `Amount` to the cent, or the rate is absent.
- Options: (a) drop `Rate` (preferred); (b) more decimals (3.4816 still gives 4319.97).
- Needs decision: no
- From: money (broad and context refuted it)

### tender/21#F16 · Low · The award notice repeats the instructions given to tenderers
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-02-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:AdditionalInformationRequestPeriod/cbc:EndDate` = `2026-02-19`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:SubmissionMethodCode` = `ELECTRONIC`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:RequiredDocumentReference/cbc:ID` = `PWD-PRICE-TPL`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProvidedDocumentReference/cbc:ID` = `PWD-SITE-PLAN`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:RequiredDocumentReference/cbc:ID` = `PWD-PRICE-TPL`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProvidedDocumentReference/cbc:ID` = `PWD-SITE-PLAN`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- Why: A contract award notice is "A document published by a Contracting Party to announce the awarding of a procurement project". Deadlines for documents, questions and tenders, the submission method, the price template, the site plan and lot terms "as for the procedure" (of which the notice carries only the appeal body) were instructions to tenderers; all lie in the past and the announcement uses none of them. The block reads as copied from the contract notice (also the source of F1–F3, F7, F8). Counter-argument (logistics, refuted for the deadline): a past deadline is a correct historical fact of the procedure. What identifies the procedure and its object stays.
- Condition: The award notice carries of the tendering process and the lots what identifies them and what the award refers to.
- Options: (a) remove the past instructions (preferred); (b) keep them if the world's notice form prescribes a full repetition, and record that rule.
- Needs decision: no
- From: context (needs decision yes)

### tender/21#F17 · Low · The installation lot is described with the supply lot's texts
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Name` = `Installation of the benches`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:Description` = `240 steel park benches with hardwood slats over two years, delivered and anchored.`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:AdditionalCommodityClassification/cbc:ItemClassificationCode` = `381`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ProcurementAdditionalType/cbc:ProcurementType` = `Environmental impact: recycled steel and certified timber are asked`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cbc:OptionsDescription` = `One extension of a year with 120 more benches.`
- Why: Lot 2 is a service (`SERVICES`, CPC 87390). Its description is the project's (supply of benches), its additional classification CPC 381 (furniture), its green requirement concerns steel and timber, which an installation does not supply, and its extension speaks of more benches. The lot-specific values (name, type codes, main classification, amounts 4320.00 / 2160.00) are right.
- Condition: Description, classifications, strategic requirement and option text of lot 2 describe the installation.
- Options: (a) own description and option text, service classification only, and no green type unless the installation has a requirement (preferred).
- Needs decision: no
- From: broad, context

### tender/21#F18 · Low · Urvanian declared as additional language of a notice that has no Urvanian text
- XPath: `/ContractAwardNotice/cac:AdditionalNoticeLanguage/cbc:ID` = `qau`
- XPath: `/ContractAwardNotice/cbc:NoticeLanguageCode` = `en`
- Why: `AdditionalNoticeLanguage` is "An additional official language used in this contract award notice". No text of the notice is in Urvanian: the only `qau` values are the winner's street and town names (3 elements, grep), parts of an address. Counter-argument (parties, refuted): the procedure is open to Urvanian tenderers and the winner is Urvanian, so a second official language is plausible. That supports declaring the language only if the texts are given in it; whether the Trade Accord requires that is a story question.
- Condition: Every language declared for the notice is one in which its texts are given, or it is not declared.
- Options: (a) remove the additional language (preferred); (b) give the notice's texts in Urvanian (words from the lexicon), if the Trade Accord requires it.
- Needs decision: yes
- From: broad (needs decision no), context (parties refuted it)

### tender/21#F19 · Low · Opening event: an electronic opening located at the department's name and square, with a contact that cannot be reached
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:Description` = `Electronic opening; tenderers may follow it online.`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:OccurrenceLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:Contact/cbc:Name` = `Procurement office`
- Why: `OccurrenceLocation` is "The location of this event"; its name is the organisation plus a square, not a place to attend, while the description says the opening is online, so a reader cannot tell whether one may attend. The building is identified in the same notice by its address-register ID (`/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`) but not here; the event contact has a name only. The same values are in 02 and 03.
- Condition: The location is either the online place or an identified room that can be attended, agreeing with the description; a contact for the event can be reached or is absent.
- Options: (a) drop location and contact from the award notice (preferred: the description and access URI suffice, and the event is past); (b) the room with its address or register ID, and a reachable contact.
- Needs decision: no
- From: broad, parties

### tender/21#F20 · Low · The review board's registry has the job title and department of a buyer
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Name` = `Registry`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:Department` = `Procurement`
- Why: The appeal receiver's contact is named "Registry", which fits a review board (ISIC 8423), but its job title and department are those of the contracting department's buying office; a review board does not procure. Name, title and department contradict each other and the role.
- Condition: The registry's job title and department belong to a registry of a review body.
- Options: (a) "Registrar" or "Clerk of the board", department "Registry" (preferred); (b) drop job title and department.
- Needs decision: no
- From: broad, parties

### tender/21#F21 · Low · Master data of the winner, and customs trader numbers, in a published notice
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: An award notice names the winner. Who stores and despatches its goods (Castrano, a key account desk without any means of contact), its share capital and listing, the mobile number of its order desk and the customs trader numbers have no function in a published notice (section 4.8); the installer who matters for the award (Saltmere) appears only in free text. Counter-argument (parties, refuted): share capital and listing describe the party as a legal entity. The merge keeps them, as in 16 and 20.
- Condition: The winning party carries what a published award needs (identity, name, address, size); data about its own suppliers, sales desk, shares and customs registration is absent.
- Options: (a) reduce the winner's party data (preferred); (b) keep it if full party data in every document is the world's rule, and record that.
- Needs decision: no
- From: broad, parties (service provider only), context; customs trader numbers added by the merge

### tender/21#F22 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax": the party's status; the text begins with a transaction. Counter-argument (broad, refuted): the text states the status. Kept as in 15–20; the code fits (list description: a public body "buys free of sales tax"), parties would prefer a status code. (The budget's own tax category E/PUBLIC is consistent and correct where it is, money.)
- Condition: The party's exemption reason states its status only.
- Options: (a) reword the text, keeping the code (preferred); (b) a party-status code.
- Needs decision: no
- From: parties (broad refuted it)

### tender/21#F23 · Low · Originator and beneficiary repeat the contracting party
- XPath: `/ContractAwardNotice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ContractAwardNotice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: Both roles hold the contracting party, adding nothing (no fillers). Counter-argument (parties, refuted): no "if different" condition, and the department needs and uses the benches. Kept as in the tenders and as merger A's decision for the notices (roles filled with the contracting party: Low/no).
- Condition: Both are present only when they are another party, or absent.
- Options: (a) remove both (preferred); (b) name the body that uses the benches, if the world has one.
- Needs decision: no
- From: context (parties refuted it)

### tender/21#F24 · Low · Italian text tagged English, and en-XB here against en-XU in Valdara's own documents
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The same text is tagged `en-XB` here and `en-XU` in Valdara's documents (13); the tag follows the issuer's country, not the text, and the text is Italian. No convention is stated (parties could not settle it); aligned with the earlier flows (Low, decision).
- Condition: One recorded rule for these renderings and their tags, applied in every example.
- Options: (a) tag by what the text is (`en-XU`) everywhere (preferred by parties); (b) keep the issuer-dependent tag and record the rule.
- Needs decision: yes
- From: parties

### tender/21#F25 · Low · Valdara's legal form in one untagged rendering
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`
- Why: The legal form occurs once without `languageID`, while the address is given in both languages, tagged, and Valdara's documents give the legal form twice (13). Split from parties/F7.
- Condition: The legal form is rendered like the address (both renderings, tagged).
- Options: (a) both renderings, tagged (preferred); (b) at least tag the single rendering.
- Needs decision: no
- From: parties

### tender/21#F26 · Low · Additional document references with only an ID
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:AdditionalDocumentReference/cbc:ID` = `PWD-SPEC-BENCH-26`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:AdditionalDocumentReference/cbc:ID` = `PWD-QA-26`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:AdditionalDocumentReference/cbc:ID` = `PWD-QA-26`
- Why: The references do not say what they point to, and the documents are not examples of the flow; `PWD-SPEC-BENCH-26` is the technical specification by 03 (`03-CallForTenders.xml:/CallForTenders/cac:TechnicalDocumentReference/cbc:ID` = `PWD-SPEC-BENCH-26`), but what `PWD-QA-26` is (questions and answers? quality assurance?) cannot be told.
- Condition: Each reference states the kind of document.
- Options: (a) add `cbc:DocumentType` (preferred).
- Needs decision: no
- From: logistics

## Checked and consistent
- `PreviousDocumentReference` `LPWD-DOC-26-0188` is the contract notice (02), `NoticeDocumentReference` `LPWD-DOC-26-0187` the prior information notice (01); the minutes `PWD-MIN-AWARD-26` are also cited by 22 and 23.
- Tender result, recalculated: two tenders counted (15 and 19; 17 was withdrawn), both electronic, one foreign (Valdara); lowest 119 040.00 (19), highest 124 080.00 (15); awarded 124 080.00 = 119 760.00 + 4 320.00 = 15 and 22; subcontract amount 240 × 18.00 = 4 320.00; advertisement 320.00 within the 500.00 of 01–03; description "ten years of warranty on the coating" = Valdara's criterion response.
- Derived amounts: minimum 62 040.00 (120 benches), maximum 148 896.00 (288), renewal 62 040.00 = 59 880.00 + 2 160.00, average release 20 680.00 = 124 080.00 / 6 (= the first invoiced release, 32); the same per lot.
- Dates: award 2026-03-09 09:30 before the notifications (22, 23) and this notice; requested publication 2026-03-14 after issue; formalization 2026-03-19 to 2026-03-22 contains the contract's issue date (24); contract start 2026-03-23 = planned period start; 24 months to 2028-03-22; delivery period within it.
- Budget tax category E, 0 %, reason PUBLIC, scheme STT, `TaxIncludedIndicator` false: consistent with each other and with 01–03.
- Codes: CAN, procedure, urgency, contracting system, submission method, event type, CPC 38111/87390 and the tax codes are in their lists; `TenderResultCode` AWARDED, contract and system type FRAMEWORK, one operator: consistent.
- Parties: register numbers the same throughout the flow (department, information service 20410959, review board 20410822, Valdara, Castrano); the receiver is the publication service that also receives 01 and 02; the winner is the party of 15, 22, 23, 24; the information service's contact fits its role (parties). ISIN `XU0001042501` check digit correct.

## Considered and refuted
- `/ContractAwardNotice/cac:TenderingProcess/cbc:GovernmentAgreementConstraintIndicator`: might claim the WTO GPA — refuted, "a government procurement agreement" in general, which the Trade Accord is (from broad, context).
- `/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Rate`: 3.5 rounded from 3.48 — refuted as ordinary rounding (from broad; and as a legitimate reading of "allowed" in a result, from context; the merge keeps money's finding F15).
- `/ContractAwardNotice/cac:TenderResult/cbc:ReceivedTenderQuantity`: three tenders exist — refuted, 17 was withdrawn (from broad, logistics, context).
- `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount`: unit prices next to a line total — refuted, the call's criterion fixes the reading per bench (from broad; the merge keeps context's and money's finding F8).
- `/ContractAwardNotice/cac:TenderResult/cac:Contract/cbc:ID`: `PWD-2026-PARKS` also folder and project ID — refuted here; the contract may be numbered after the file (from broad; context listed it under "Outside this review").
- `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:UUID`: same UUID as the project-level line — refuted, the same line repeated under its lot (from broad).
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: transaction-like — refuted, the text states the status (from broad; the merge keeps F22).
- `/ContractAwardNotice/cac:TenderingProcess/cbc:TerminatedIndicator`: false although the competition is over — refuted, "terminated" means stopped without result (from broad, logistics, context).
- `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:TotalAmount`: "including taxes" with `TaxIncludedIndicator` false — refuted, exempt at 0 % (from money).
- `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: Bayvarran exemption although the winner invoices Urvanian VAT — refuted, the budget's taxes are the authority's side (from money).
- `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MinimumAmount`: equal to the renewal — refuted, both are 120 benches with installation (from money).
- `/ContractAwardNotice/cac:TenderResult/cbc:AdvertisementAmount`: no counterpart elsewhere — refuted, the authority's publication cost, within the maximum (from money).
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` malformed — refuted (from parties).
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:Contact/cbc:Telephone`: +999 real — refuted, unassigned (from parties).
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: master data not used — refuted for the parties lens (from parties; the merge keeps it in F21).
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD 0990 real — refuted from knowledge of the ICD list (from parties).
- `/ContractAwardNotice/cac:AdditionalNoticeLanguage/cbc:ID`: unrelated language — refuted, Urvanian tenderers take part (from parties; the merge keeps F18).
- `/ContractAwardNotice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` and `/ContractAwardNotice/cac:BeneficiaryParty/cac:PartyName/cbc:Name`: fillers — refuted, no "if different" condition (from parties; the merge keeps F23).
- `/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Description`: subcontractor should be a structured party — refuted for the parties lens, consistent with 15 (from parties).
- `/ContractAwardNotice/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate`: a past deadline — refuted, a correct historical fact (from logistics; the merge keeps its presence question in F16).
- `/ContractAwardNotice/cac:ProcurementProject/cbc:RequestedDeliveryDate`: one date for a two-year framework, `2026-04-02` — refuted, the start of the delivery period of the first release (from logistics, context).
- `/ContractAwardNotice/cac:ProcurementProject/cbc:QualityControlCode`: "works project" in the definition — refuted, inspection on delivery fits a supply (from context).
- `/ContractAwardNotice/cac:TenderingProcess/cac:ContractingSystem`: "Only when the procedure is repetitive" — refuted, the releases are the repetition (from context).
- `/ContractAwardNotice/cbc:RegulatoryDomain`: names a domain rather than a law — refuted, a legitimate reading (from context).
- `/ContractAwardNotice/cac:ReceiverParty`: a receiver of a published notice — refuted, the publication service (from context).

## Changed in the merge
- broad/F2, logistics/F2 (High/yes) and context/F2 (Medium/no) split into F2 (dates before the contract notice: High/yes) and F3 (restricted-procedure periods in an open procedure: Medium/no, as merger B for 09): two problems with different severities.
- broad/F11, parties/F4, context/F14 → F11: raised to Medium; the registry contact (broad/F11, parties/F5) split off as F20.
- money/F3 (Low), context/F6 (Medium) → F8: Medium, broad's refutation carried.
- money/F5 (Low/yes), broad/F8 (Low/no) → F14: Low/yes, as 15#F15.
- context/F10 (Low/yes) → F16: needs decision no, as merger D's decision on tender-phase data in the contract (encoding, not story).
- broad/F7 (Low/no), context/F12 (Low/yes) → F18: Low/yes, because parties refuted it and the answer depends on the Trade Accord.
- broad/F9, parties/F6 → F19; broad/F12, parties/F8, context/F15 → F21 (customs trader numbers added by the merge).
- parties/F7 split into F24 (tags, Low/yes) and F25 (untagged legal form, Low/no), as the earlier flows.
- broad/F1: its statement of an auction "held on 6 March" dropped (no such date in the XML).

## Outside this review
- 02 requests publication on 27 January but is issued on 11 February; the source of F2 lies there and in 03 (from logistics, context).
- The same periods, `OriginalContractingSystemID`, fee and estimate are in 02 and 03 (from broad).
- The same identifier `PWD-2026-PARKS` serves as contract folder, project and contract; looked at with 24 and 26 (from broad, context).
