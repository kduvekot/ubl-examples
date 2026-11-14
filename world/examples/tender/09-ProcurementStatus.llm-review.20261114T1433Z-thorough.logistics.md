# LLM review: 09-ProcurementStatus.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/09-ProcurementStatus.xml`, Git blob `e9ed8a2b58652c74ad8a9d6547388d6e5e2746db` (committed)
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

### tender/09#F1 · Medium · The status of an open procedure reports periods for invitations and requests to participate, both long over
- XPath: `/ProcurementStatus/cbc:ProcedureCode` = `OPEN`
- XPath: `/ProcurementStatus/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ProcurementStatus/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ProcurementStatus/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: the two periods are "the period during which invitations to tender must be completed and delivered" and "the period during which requests for participation must be completed and delivered". The document says the procedure is open; an open procedure has neither step (own knowledge of procurement practice), and Brackenmere, the receiver, tenders in 17 and 19 without invitation. The dates are those of the contract notice and the call for tenders, where they lie before the issue dates of those documents (2026-02-11 and 2026-02-12; reported there): the invitation period ended ten days before the procedure was announced. Repeating them in a status issued on `/ProcurementStatus/cbc:IssueDate` = `2026-02-21` tells the operator nothing it can act on, and the department itself registered a request to participate on 2026-02-15 (05), after the reception period it reports here.
- Condition: the status reports only periods the procedure has, with dates that agree with the notice and with what the department did (04/05).
- Options: (a) remove the two periods here and in 02/03, keeping the tender deadline, which is what the request asked about (preferred); (b) keep them only if the world's open procedure is given a registration step, with dates after the notice's issue date.
- Needs decision: yes

### tender/09#F2 · Medium · Language code in LocaleCode
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProcurementStatus/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/09#F3 · Low · The project is named differently from the notices and from the document's own contract name
- XPath: `/ProcurementStatus/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/ProcurementStatus/cbc:ContractName` = `Park benches for the parks renewal programme`
- Why: `ProcurementProject/Name` is "a name of this procurement project". The department's notices name the project `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme`, as does this document's `ContractName`. "Park benches for the city parks" occurs only in 08 and here.
- Condition: the project name equals the name in the contract notice.
- Options: (a) use the notice's name (preferred); (b) drop the name.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` has a correct check digit.
- `ProcedureStatusRequestDocumentReference` `BF-DOC-26-0194` resolves to 08, a procurement status request by the same operator, issued 2026-02-20 15:50; this status is issued 2026-02-21 11:44, after it.
- `TenderSubmissionDeadlinePeriod` 2026-02-26 12:00 equals the deadline in 02 and 03, lies after the issue time, and agrees with the note ("The deadline stands"), which answers the request's question.
- The four legislation references (`XB-PPA-2019`, `XB-STT-ACT`, `XB-ENV-2021`, `XB-LAB-2018`) carry the same IDs as in 01 to 03, each in the element for its kind of legislation.
- `ContractFolderID`, `ProcedureCode` OPEN and the lots `LOT-1`/`LOT-2` agree with the notice.

## Considered and refuted
- `/ProcurementStatus/cac:ParticipationRequestReceptionPeriod/cbc:EndDate`: a period that is over when the status is issued — refuted as a finding of its own because a status may report past periods; the problem is that the procedure has no such period (F1).
- `/ProcurementStatus/cbc:ID`: `LPWD-DOC-26-0195` after `LPWD-DOC-26-0192` (2026-02-13) and `-0191` (2026-02-15) — refuted, issued later than both.
- `/ProcurementStatus/cbc:Note`: the document carries no code for the state of the procedure — refuted because UBL's ProcurementStatus has no such element at document level; the note and the deadline period give the state.
