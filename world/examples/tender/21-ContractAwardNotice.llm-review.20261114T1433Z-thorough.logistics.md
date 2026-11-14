# LLM review: 21-ContractAwardNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/21-ContractAwardNotice.xml`, Git blob `59a77855a9c7e78ea4690806b5a919a52b58df71` (committed)
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

### tender/21#F1 · High · The opening of the tenders is still "scheduled" and not completed in the award notice
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:CompletionIndicator` = `false`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cac:CurrentStatus/cbc:ConditionCode` = `SCHEDULED`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate` = `2026-02-26`
- Why: CompletionIndicator is "an indicator that this event has been completed (true) or not (false)". The notice is issued on `/ContractAwardNotice/cbc:IssueDate` = `2026-03-13` and reports the award of `/ContractAwardNotice/cac:TenderResult/cbc:AwardDate` = `2026-03-09`, which is only possible after the tenders were opened on 26 February. The event is copied unchanged from the contract notice, where it lay in the future.
- Condition: In the award notice the opening event is completed (indicator true, a status that says so), or the event is not carried.
- Options: (a) preferred: CompletionIndicator true and a status code for a completed event; (b) leave the event out of the award notice.
- Needs decision: no

### tender/21#F2 · High · Procedure periods that end before the contract notice was issued, and belong to a restricted procedure
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: The notice refers to the contract notice (`/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0188`), issued on `02-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-02-11`; the tender documents were issued on `03-CallForTenders.xml:/CallForTenders/cbc:IssueDate` = `2026-02-12`. According to the periods carried here, invitations were sent until 1 February, requests to participate were received until 11 February (the day the procedure was announced) and the documents were available from 26 January, 17 days before they were issued. Besides, invitation and participation-request periods are steps of a restricted procedure; in an open procedure (ProcedureCode OPEN, "Open procedure with two lots") any operator tenders directly, and no document of the flow is a request to participate or an invitation to tender (the expression of interest 04/05 is of 14–15 February, after all three periods). The periods start on 26 January, which fits the contract notice's requested publication date (27 January) but not its issue date; the same values are in 02 and 03.
- Condition: Every period of the tendering process lies between the publication of the contract notice and the award, and only periods that the open procedure has are carried.
- Options: (a) preferred: remove the invitation and participation periods and let the document availability start at the issue of the call for tenders; (b) move the contract notice and the call for tenders to late January so the periods become true, and still drop the periods that an open procedure does not have.
- Needs decision: yes

### tender/21#F3 · Medium · "Original contracting system" identifier without a reopening
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- Why: "When reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system." This process is not a reopening under an existing framework: it is an open procedure that itself establishes the framework (`/ContractAwardNotice/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`, "Framework with one supplier", contract `PWD-2026-PARKS` from 23 March 2026). A framework of 2024 is mentioned nowhere else in the flow (grep for `PWD-FW-2024-PARKS` over `world/examples/**/*.xml`: tender 01, 02, 03, 21, always this element).
- Condition: The element is present only if the process reopens competition under an earlier framework that the story knows, and then identifies that framework.
- Options: (a) preferred: remove it; (b) give the 2024 framework a place in the story (the note or description).
- Needs decision: no

### tender/21#F4 · Low · The award notice is issued inside the appeal period and before the contract exists
- XPath: `/ContractAwardNotice/cbc:IssueDate` = `2026-03-13`
- XPath: `/ContractAwardNotice/cbc:RequestedPublicationDate` = `2026-03-14`
- XPath: `/ContractAwardNotice/cbc:Note` = `Award of the framework contract for park benches.`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- Why: The notice announces the awarded contract with its identifier and start date, but on 13–14 March the appeal period of the unsuccessful tenderer is still running (`23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`) and the contract is only signed on `24-TenderContract.xml:/TenderContract/cbc:IssueDate` = `2026-03-19`. From my knowledge of procurement practice (e.g. the EU directives), a contract award notice follows the conclusion of the contract. The department's running number also places the notice (…0207) before the two notifications of 9 March (…0208, …0209), which were issued four days earlier.
- Condition: The notice is issued after the contract is concluded (or says that the award is not yet final), and its number fits its place in the department's sequence.
- Options: (a) preferred: issue it after 19 March, with a number after the contract's (`LPWD-DOC-26-0210`); (b) keep the date and say in the note that the award is subject to the standstill.
- Needs decision: yes

### tender/21#F5 · Low · Auction announced as part of the procedure, but the result shows none
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:AuctionTerms/cbc:AuctionConstraintIndicator` = `true`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:LowerTenderAmount` = `119040.00`
- Why: The auction terms say that after the evaluation every tenderer with an admissible tender is invited to an electronic auction on the unit prices. The awarded amount and the lowest and highest tender amounts are exactly the amounts of the tenders as submitted (`15-Tender.xml`: 124080.00; `19-Tender.xml`: 119040.00), the award description does not mention an auction, and no document or date of the flow belongs to one (qualification 3 March, award 9 March). An award notice that carries the auction terms unchanged leaves open whether the auction was held without bids or not held.
- Condition: The notice either reports the auction (held, with its outcome, or not held and why) or does not carry terms of a step that did not take place.
- Options: (a) say in the award description that no tenderer lowered its price in the auction; (b) drop the auction from the procedure; no preference, this is a story decision.
- Needs decision: yes

### tender/21#F6 · Low · Additional document references with only an ID
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:AdditionalDocumentReference/cbc:ID` = `PWD-SPEC-BENCH-26`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:AdditionalDocumentReference/cbc:ID` = `PWD-QA-26`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:AdditionalDocumentReference/cbc:ID` = `PWD-QA-26`
- Why: The "additional" references do not say what kind of document they point to, and the documents are not examples of the flow. `PWD-SPEC-BENCH-26` is the technical specification according to `03-CallForTenders.xml:/CallForTenders/cac:TechnicalDocumentReference/cbc:ID` = `PWD-SPEC-BENCH-26`; what `PWD-QA-26` is (questions and answers? quality assurance?) cannot be told.
- Condition: Each reference states the kind of document.
- Options: add `cbc:DocumentType` (preferred).
- Needs decision: no

## Checked and consistent
- No identifiers with check digits outside the parties (`check_ids.py` reports no failures).
- `cac:PreviousDocumentReference` LPWD-DOC-26-0188 is the contract notice of this procedure; `cac:TenderingProcess/cac:NoticeDocumentReference` LPWD-DOC-26-0187 is the prior information notice; both exist and are of the kind the elements mean.
- Requested publication date (14 March) is after the issue time (13 March 13:55); award date 9 March 09:30 is before it.
- `cac:TenderResult` agrees with 22, 23 and 24: award ID, award date and time, contract PWD-2026-PARKS from 2026-03-23 for 24 MON (ends 2028-03-22 = planned period end), lots, 124080.00, formalisation 19–22 March, winner Valdara Industries.
- Tender statistics: lowest 119040.00 = `19-Tender.xml`, highest 124080.00 = `15-Tender.xml`; 1 foreign tender (Valdara, Urvania); advertisement 320.00 is within the maximum of 500.00.
- Framework duration 24 MON agrees with the contract validity; delivery period 2026-04-02 to 2028-03-22 lies within the planned period.
- Codes: NoticeTypeCode CAN, ProcedureCode, UrgencyCode, ContractingSystemCode, SubmissionMethodCode, TenderEventTypeCode, CPC 38111/381/87390, tax category E and scheme STT are in their lists and fit their elements.

## Considered and refuted
- `/ContractAwardNotice/cac:TenderResult/cbc:ReceivedTenderQuantity`: `2`, although the flow has three tender documents (15, 17, 19) — refuted: 17 was withdrawn and replaced by 19, so two tenders stood at the opening; lowest and highest amount fit that reading.
- `/ContractAwardNotice/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate`: a past deadline in an award notice — refuted: a correct historical fact of the procedure, unlike the opening's status (F1).
- `/ContractAwardNotice/cac:ProcurementProject/cbc:RequestedDeliveryDate`: `2026-04-02` — refuted here: it is the requested date of the procedure and lies after the contract start; whether the first release met it is checked in the order and the despatch advice.
- `/ContractAwardNotice/cac:TenderingProcess/cbc:TerminatedIndicator`: `false` after the award — refuted: "the competition launched is terminated" means cancelled, which it was not.

## Outside this review
- `02-ContractNotice.xml` requests publication on 27 January but is issued on 11 February; the source of F2 lies there and in `03-CallForTenders.xml`.
