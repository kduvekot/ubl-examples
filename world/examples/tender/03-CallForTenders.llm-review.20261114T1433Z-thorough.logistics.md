# LLM review: 03-CallForTenders.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

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

### tender/03#F1 · High · Procedure periods start, and three of them end, before the call for tenders is issued
- XPath: `/CallForTenders/cbc:IssueDate` = `2026-02-12`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: the call for tenders is the set of procurement documents. It says these documents are available from 2026-01-26, 17 days before it is issued (and 18 days after its approval, `/CallForTenders/cbc:ApprovalDate` = `2026-01-25`). The periods for invitations to tender, invitations to participate and requests to participate have all ended (2026-02-01, 2026-02-11, 2026-02-11) when the document is issued on 2026-02-12, so it announces three periods that are already over. The dates fit a procedure launched on 2026-01-26, as the prior information notice planned (`01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-01-26`) and one day after the approval; the issue date (and that of the contract notice, `02-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-02-11`) is the value that does not fit. The flow's only request to participate, `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`, lies after the reception period.
- Condition: every period the call for tenders states starts on or after the day the documents exist and has not ended when it is issued; documents of the flow that fall under a period (04) lie inside it.
- Options: (a) issue the contract notice and the call for tenders on 2026-01-26, keeping the periods (preferred: agrees with the approval date and the PIN's plan); (b) keep the issue dates and move the periods after them.
- Needs decision: yes

### tender/03#F2 · High · The call for tenders refers to "the call for tenders" under an ID that is not its own
- XPath: `/CallForTenders/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- XPath: `/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`
- Why: `CallForTendersDocumentReference` is "a reference to a Call for Tender associated with these tendering terms". This document is that call for tenders, and its ID is `LPWD-DOC-26-0189`; no example has the document ID `PWD-2026-PARKS-CFT`. Either the reference points to the document itself under a second ID, or to a document that does not exist. The catalogue uses the real ID (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`), while 01, 02, 06, 15, 17, 19 and 24 use `PWD-2026-PARKS-CFT` (8 examples including this one; `grep -l` over `tender/*.xml`), so tenders and the catalogue name the same document differently.
- Condition: the call for tenders has one ID, and every reference to it in the flow uses that ID; the call for tenders does not refer to itself.
- Options: (a) remove the self-reference here and use `LPWD-DOC-26-0189` in the other examples (preferred); (b) give this document the ID `PWD-2026-PARKS-CFT` and change the catalogue.
- Needs decision: no

### tender/03#F3 · High · The prior information notice is named as "replaced notice", under an ID that is not its ID
- XPath: `/CallForTenders/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`
- Why: `ReplacedNoticeDocumentReference` is "a reference to the notice that is being replaced". A call for tenders is not a notice and replaces none, and this is version `/CallForTenders/cbc:VersionID` = `1`. No example has the ID `PWD-2026-PARKS-PIN`; the prior information notice is `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`, and this same document refers to it correctly under that ID in `NoticeDocumentReference`. The document thus names the same notice under two IDs and in two roles, one of them wrong.
- Condition: `ReplacedNoticeDocumentReference` is present only where a notice replaces an earlier version, with that notice's ID; the PIN is referred to only by its document ID.
- Options: (a) remove `ReplacedNoticeDocumentReference` (preferred: `NoticeDocumentReference` already links the PIN); (b) none seen.
- Needs decision: no

### tender/03#F4 · Medium · OriginalContractingSystemID in a procedure that reopens nothing
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`
- Why: `OriginalContractingSystemID` is, "when reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system". This document belongs to a new open procedure that sets up a framework (`FW-1`, 24 months from 2026-03-23); it does not reopen competition under an existing framework. A framework of 2024 appears nowhere in the flow except as this ID (in 02, 03 and 21), and the document gives no hint what it is (the previous bench framework?). The definition's condition is not met.
- Condition: the element is present only in a procedure that reopens competition within an existing framework or DPS, and then identifies that system.
- Options: (a) remove it (preferred); (b) if the earlier framework is to be mentioned, say so in text (e.g. in `ProcessJustification` or a note), not in this element.
- Needs decision: no

### tender/03#F5 · Medium · Periods for invitations and requests to participate in an open procedure
- XPath: `/CallForTenders/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: the three periods are "the period during which invitations to tender must be completed and delivered", "the period during which the invitation to participate must be sent" and "the period during which requests for participation must be completed and delivered". They belong to procedures with a selection stage (restricted, negotiated). The document describes an open procedure, in which any operator tenders by the deadline (2026-02-26 12:00) without request or invitation, and the three tenders of the flow (15, 17, 19) are submitted without an invitation. Own knowledge of procurement practice; the fictional act could differ, but the document does not say so. The flow does contain an expression of interest (04/05), which may be what these periods were meant to carry.
- Condition: the call for tenders carries only the periods its procedure has; if the world's open procedure has a registration step (04/05), the period that governs it is the only one present and 04 lies inside it.
- Options: (a) remove the three periods (preferred), or keep only `ParticipationRequestReceptionPeriod` as the registration period ending after 04; (b) make the procedure a restricted one, which changes the story.
- Needs decision: yes

### tender/03#F6 · Medium · Latest date to obtain a security clearance although none is required
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- Why: `LatestSecurityClearanceDate` is "the end date until which the candidates can obtain the necessary level of security clearance". The same tendering terms say no clearance is required, so the date has no meaning (rule "no fillers").
- Condition: the date is present only if a security clearance is required.
- Options: (a) remove the date (preferred); (b) require a clearance, which would change the story.
- Needs decision: no

### tender/03#F7 · Medium · Language code in LocaleCode
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred); (b) fill it with a country or locale code.
- Needs decision: no

### tender/03#F8 · Low · The call for tenders links the prior information notice but not the contract notice it belongs to
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`
- Why: `NoticeDocumentReference` is "a reference to a notice pertaining to this tendering process". The only notice named is the prior information notice. The notice that launched the procedure, and under which an operator finds these documents, is the contract notice `02-ContractNotice.xml:/ContractNotice/cbc:ID` = `LPWD-DOC-26-0188`, issued the day before; it is not referenced anywhere in this document (the block is copied unchanged from 02, where a reference to the PIN alone is right).
- Condition: the call for tenders refers to the contract notice of its procedure.
- Options: (a) add a second `NoticeDocumentReference` with `LPWD-DOC-26-0188` (preferred); (b) leave as is, accepting that the link exists only through `ContractFolderID`.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` (receiver's legal entity data) has a correct check digit.
- `ApprovalDate` 2026-01-25 is before the issue date 2026-02-12 13:26; the document follows the contract notice (2026-02-11 08:32) by a day.
- `NoticeDocumentReference` `LPWD-DOC-26-0187` is the prior information notice (01), of the right kind.
- Sequence after the issue time: additional information until 2026-02-19; documents available until 2026-02-25; tender deadline 2026-02-26 12:00; opening `OPEN-1` 2026-02-26 14:00, `CompletionIndicator` false and status SCHEDULED, correct on 2026-02-12; guarantee to be constituted by 2026-02-26. The receiver's tender (15) is issued on 2026-02-25, its guarantee (14) on 2026-02-24.
- Document references at the top (`PWD-LEGAL-26`, `PWD-SPEC-BENCH-26`, `PWD-PRICE-TPL`, `PWD-SITE-PLAN`, `PWD-QA-26`) are each of the kind their element names, and `PWD-PRICE-TPL` is also the template in `TenderPreparation`; lots carry `PWD-SPEC-LOT-1`/`PWD-SPEC-LOT-2` as in 02.
- Framework 24 MON = planned period 2026-03-23 to 2028-03-22. `TenderingProcess/ID` `PWD-2026-PARKS-P` as in 02, 08, 21, 24; `OpenTenderEvent/IdentificationID` = `TenderPreparation/OpenTenderID` = `OPEN-1`.
- Codes: CPC Ver.2.1 38111, 381, 87390; ISIC 3100, 8411, 8423; unit codes ANN, MON, DAY, EA, SET; channel code AL (cellular phone) in EDED 3155; all world-list codes resolve in the listing.
- The request-for-tender line equals the one in 01 and 02 (same UUID, 240 EA, delivery period 2026-04-02 to 2028-03-22, lead time 10 days).

## Considered and refuted
- `/CallForTenders/cac:ProcurementProjectLot[1]/cac:LegalDocumentReference/cbc:ID`: the lot's "legal document" is the procurement act `XB-PPA-2019` — refuted because an act is a legal document and the element's definition ("a reference to a legal document") asks no more.
- `/CallForTenders/cac:LegalDocumentReference/cbc:ID`: the document-level legal document is `PWD-LEGAL-26` while the lots name the act `XB-PPA-2019` — refuted because these are two legal documents (the department's legal conditions and the act), each a legitimate reading of "a reference to a legal document".
- `/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode`: code without `listID` — refuted, the department's own programme code (party-internal).
- `/CallForTenders/cac:TenderingProcess/cbc:ContractingSystemCode`: `FRAMEWORK` together with `ContractingSystem/ContractingSystemTypeCode` `FRAMEWORK` from another list — refuted because both elements exist in UBL with the same meaning and the values agree.
- `/CallForTenders/cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate`: opening on the day of the deadline — refuted, 14:00 is after 12:00.
- `/CallForTenders/cac:TenderingProcess/cac:AdditionalInformationRequestPeriod/cbc:EndDate`: the status request 08 is issued on 2026-02-20, a day after this period — refuted because a status request asks for the state of the procedure, not for additional information about the procurement.
- `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode`: `SERVICES` here against `WORKS` in the prior information notice — refuted for this example because 02, 03 and 21 agree; the deviating value is in 01 and reported there.

## Outside this review
- The call for tenders announces an electronic auction before the award (`AuctionTerms`). No document of the flow between the opening (2026-02-26) and the award (22/23, 2026-03-09) mentions an auction having taken place; whether the story needs one is a question of the flow's timeline.
