# LLM review: 02-ContractNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

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

### tender/02#F1 · High · Publication and procedure periods lie before the notice's own issue date
- XPath: `/ContractNotice/cbc:IssueDate` = `2026-02-11`
- XPath: `/ContractNotice/cbc:RequestedPublicationDate` = `2026-01-27`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:DocumentAvailabilityPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: `RequestedPublicationDate` is "the requested publication date for this Contract Notice"; it is 15 days before the date on which the notice is issued, so the department asks for a publication in the past. The same holds for the periods the notice announces: documents are said to be available from 2026-01-26 (16 days before the notice exists), the invitation submission period has ended ten days before the issue date, and the periods for invitations to participate and for requests to participate end on the issue day itself. All these dates agree with a notice published on 2026-01-26/27, which is also what the prior information notice planned (`01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-01-26`); the issue date 2026-02-11 is the value that does not fit. In addition, the flow's only request to participate, `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`, comes three days after the reception period ends, and is still answered in 05.
- Condition: the requested publication date is not before the issue date; every period the notice announces starts on or after the publication and has not ended when the notice is issued; documents of the flow that fall under a period (04) lie inside it.
- Options: (a) issue the notice on 2026-01-26 (and the call for tenders, 03, with it), keeping the periods, and move the reception period's end after 04 (preferred: one changed date makes the notice agree with the PIN's plan and with its own periods); (b) keep 2026-02-11 and move the requested publication date and all period starts and ends after it. Either way the order of the document numbers and issue dates in the flow has to be kept in view.
- Needs decision: yes

### tender/02#F2 · High · Call for tenders referenced under an ID that no document has
- XPath: `/ContractNotice/cac:TenderingTerms/cac:CallForTendersDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- Why: `CallForTendersDocumentReference` is "a reference to a Call for Tender associated with these tendering terms". The call for tenders of the procedure is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`; no example has the document ID `PWD-2026-PARKS-CFT`. The catalogue refers to the call for tenders by its real ID (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`), so the flow uses two IDs for one document. The call for tenders is issued one day after this notice (`03-CallForTenders.xml:/CallForTenders/cbc:IssueDate` = `2026-02-12`); a notice announcing it is plausible, but then under the number it will carry. `PWD-2026-PARKS-CFT` occurs in 8 examples (01, 02, 03, 06, 15, 17, 19, 24; `grep -l` over `tender/*.xml`).
- Condition: every `CallForTendersDocumentReference/cbc:ID` of the flow equals the ID of example 03.
- Options: (a) use `LPWD-DOC-26-0189` in the references (preferred); (b) give the call for tenders the ID `PWD-2026-PARKS-CFT` and change the catalogue's references.
- Needs decision: no

### tender/02#F3 · High · The prior information notice is named as "replaced notice", under an ID that is not its ID
- XPath: `/ContractNotice/cac:TenderingTerms/cac:ReplacedNoticeDocumentReference/cbc:ID` = `PWD-2026-PARKS-PIN`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0187`
- Why: `ReplacedNoticeDocumentReference` is "a reference to the notice that is being replaced". A contract notice does not replace the prior information notice; it follows it, and this is version `/ContractNotice/cbc:VersionID` = `1`, so no earlier contract notice is replaced either. No example has the ID `PWD-2026-PARKS-PIN`; the prior information notice is `01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`, and this same notice refers to it correctly under that ID in `NoticeDocumentReference`. The document thus names the same notice under two IDs and in two roles, one of them wrong.
- Condition: `ReplacedNoticeDocumentReference` is present only where a notice replaces an earlier version, with that notice's ID; the PIN is referred to only by its document ID.
- Options: (a) remove `ReplacedNoticeDocumentReference` (preferred: `NoticeDocumentReference` already links the PIN); (b) add a story in which this notice replaces an earlier contract notice.
- Needs decision: no

### tender/02#F4 · Medium · OriginalContractingSystemID in a procedure that reopens nothing
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:OriginalContractingSystemID` = `PWD-FW-2024-PARKS`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ContractingSystem/cbc:ID` = `FW-1`
- Why: `OriginalContractingSystemID` is, "when reopening a tendering process, the identifier of the original framework agreement or dynamic purchasing system". This notice opens a new open procedure that sets up a framework (`FW-1`, 24 months from 2026-03-23); it does not reopen competition under an existing framework. A framework of 2024 appears nowhere in the flow except as this ID (in 02, 03 and 21), and the notice gives no hint what it is (the previous bench framework?). The definition's condition is not met.
- Condition: the element is present only in a procedure that reopens competition within an existing framework or DPS, and then identifies that system.
- Options: (a) remove it (preferred); (b) if the earlier framework is to be mentioned, say so in text (e.g. in `ProcessJustification` or a note), not in this element.
- Needs decision: no

### tender/02#F5 · Medium · Periods for invitations and requests to participate in an open procedure
- XPath: `/ContractNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationInvitationPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: the three periods are "the period during which invitations to tender must be completed and delivered", "the period during which the invitation to participate must be sent" and "the period during which requests for participation must be completed and delivered". They belong to procedures with a selection stage (restricted, negotiated). The notice announces an open procedure, in which any operator tenders by the deadline (2026-02-26 12:00) without request or invitation, and the three tenders of the flow (15, 17, 19) are submitted without an invitation. Own knowledge of procurement practice; the fictional act could differ, but the notice does not say so. The flow does contain an expression of interest (04/05), which may be what these periods were meant to carry.
- Condition: the notice carries only the periods its procedure has; if the world's open procedure has a registration step (04/05), the period that governs it is the only one present and 04 lies inside it.
- Options: (a) remove the three periods (preferred), or keep only `ParticipationRequestReceptionPeriod` as the registration period ending after 04; (b) make the procedure a restricted one, which changes the story.
- Needs decision: yes

### tender/02#F6 · Medium · Latest date to obtain a security clearance although none is required
- XPath: `/ContractNotice/cac:TenderingTerms/cbc:LatestSecurityClearanceDate` = `2026-02-21`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:SecurityClearanceTerm/cbc:Code` = `NOTREQUIRED`
- Why: `LatestSecurityClearanceDate` is "the end date until which the candidates can obtain the necessary level of security clearance". The same tendering terms say no clearance is required, so the date has no meaning (rule "no fillers").
- Condition: the date is present only if a security clearance is required.
- Options: (a) remove the date (preferred); (b) require a clearance, which would change the story.
- Needs decision: no

### tender/02#F7 · Medium · Language code in LocaleCode
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ContractNotice/cac:TenderingTerms/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred); (b) fill it with a country or locale code.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no identifiers with check digits in this example.
- `NoticeDocumentReference` `LPWD-DOC-26-0187` is the prior information notice (01), of the right kind; 04 and 21 refer to this notice by its ID `LPWD-DOC-26-0188`.
- Sequence after the issue time: additional information until 2026-02-19; documents available until 2026-02-25; tender deadline 2026-02-26 12:00; opening `OPEN-1` 2026-02-26 14:00, two hours after the deadline, `CompletionIndicator` false and status SCHEDULED, correct on 2026-02-11; guarantee to be constituted by 2026-02-26. The tenders 15 (2026-02-25), 17 (2026-02-23) and 19 (2026-02-24) are issued before the deadline.
- Framework 24 MON = planned period 2026-03-23 to 2028-03-22; `FrequencyPeriod` 4 ANN agrees with "about four years" and "2030" in the tendering terms.
- `TenderingProcess/ID` `PWD-2026-PARKS-P` is used with the same value in 03, 08, 21 and 24; `OpenTenderEvent/IdentificationID` = `TenderPreparation/OpenTenderID` = `OPEN-1`.
- Lot references: `LOT-1` and `LOT-2` are the two lots of the notice; technical documents `PWD-SPEC-LOT-1`/`PWD-SPEC-LOT-2` per lot and the same IDs in 03.
- Codes: CPC Ver.2.1 38111, 381 and 87390 ("Installation services of other goods n.e.c.", own knowledge); ISIC 8411, 8423; unit codes ANN, MON, DAY, EA, SET; OID 2.16.840.1.101.3.4.1.46 = AES-256-GCM; all world-list codes resolve in the listing.
- The request-for-tender line of lot 1 equals the one at project level and the one in 01 (same UUID, 240 EA, delivery period 2026-04-02 to 2028-03-22, lead time 10 days).

## Considered and refuted
- `/ContractNotice/cac:ProcurementProjectLot[1]/cac:LegalDocumentReference/cbc:ID`: the lot's "legal document" is the procurement act `XB-PPA-2019` — refuted because an act is a legal document and the element's definition ("a reference to a legal document") asks no more.
- `/ContractNotice/cac:TenderingTerms/cbc:FundingProgramCode`: code without `listID` — refuted, the department's own programme code (party-internal).
- `/ContractNotice/cac:TenderingProcess/cbc:ContractingSystemCode`: `FRAMEWORK` together with `ContractingSystem/ContractingSystemTypeCode` `FRAMEWORK` from another list — refuted because both elements exist in UBL with the same meaning and the values agree.
- `/ContractNotice/cac:TenderingProcess/cac:OpenTenderEvent/cbc:OccurrenceDate`: opening on the day of the deadline — refuted, 14:00 is after 12:00.
- `/ContractNotice/cac:TenderingProcess/cac:AdditionalInformationRequestPeriod/cbc:EndDate`: the status request 08 is issued on 2026-02-20, a day after this period — refuted because a status request asks for the state of the procedure, not for additional information about the procurement.
- `/ContractNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:ProcurementTypeCode`: `SERVICES` here against `WORKS` in the prior information notice — refuted for this example because 02, 03 and 21 agree; the deviating value is in 01 and reported there.

## Outside this review
- The notice announces an electronic auction before the award (`AuctionTerms`). No document of the flow between the opening (2026-02-26) and the award (22/23, 2026-03-09) mentions an auction having taken place; whether the story needs one is a question of the flow's timeline.
