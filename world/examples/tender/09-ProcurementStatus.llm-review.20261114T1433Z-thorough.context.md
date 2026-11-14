# LLM review: 09-ProcurementStatus.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/09#F1 · Medium · An open procedure reported with periods for invitations and requests to participate
- XPath: `/ProcurementStatus/cbc:ProcedureCode` = `OPEN`
- XPath: `/ProcurementStatus/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ProcurementStatus/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ProcurementStatus/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `/ProcurementStatus/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-02-26`
- XPath: `/ProcurementStatus/cbc:IssueDate` = `2026-02-21`
- Why: The status repeats from the notices a period for invitations to tender and one for requests to participate. The procedure is `OPEN`: nobody requests to participate and nobody is invited (see the same finding in 02 and 03; the definitions there are "the period during which invitations to tender must be completed and delivered" and "… requests for participation must be completed and delivered"). Both periods ended weeks before this status is issued, and the operator asked only whether the tender deadline stands. The status thus reports two steps the procedure does not have.
- Condition: The status of an open procedure reports the periods that exist in it (here the tender submission deadline).
- Options: (a) Preferred: remove both periods. (b) Make the procedure a two-stage one in the whole flow.
- Needs decision: no

### tender/09#F2 · Medium · A language code in `LocaleCode`
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProcurementStatus/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/09#F3 · Low · Four legislation references in an answer about a deadline
- XPath: `/ProcurementStatus/cac:ProcurementLegislationDocumentReference/cbc:ID` = `XB-PPA-2019`
- XPath: `/ProcurementStatus/cac:FiscalLegislationDocumentReference/cbc:ID` = `XB-STT-ACT`
- XPath: `/ProcurementStatus/cac:EnvironmentalLegislationDocumentReference/cbc:ID` = `XB-ENV-2021`
- XPath: `/ProcurementStatus/cac:EmploymentLegislationDocumentReference/cbc:ID` = `XB-LAB-2018`
- XPath: `/ProcurementStatus/cbc:Note` = `The deadline stands; the answers did not change the documents.`
- Why: The operator asked whether the deadline stands (08), and the note answers exactly that. The status also lists the procurement, tax, environmental and labour legislation of the procedure, as the notices do. None of it changed and none of it bears on the question; the references have only an ID and say nothing new to an operator that has the documents.
- Condition: The status carries what answers the request and what has changed; legislation is referenced only if the answer depends on it.
- Options: (a) Preferred: remove the four references. (b) Keep the procurement legislation only, if the rule on deadlines after clarifications is to be cited, with the article.
- Needs decision: no

### tender/09#F4 · Low · Document provider and tender recipient repeat the contracting party
- XPath: `/ProcurementStatus/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ProcurementStatus/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `DocumentProviderParty` is "the Party that provides the procurement documents to the Economic Operator" and `TenderRecipientParty` "the Party to which tenders will be submitted". Both are the contracting party that issues the status, with ID and name only, so they tell the operator nothing (no address or channel for submission).
- Condition: The two parties are present where another party fills the role or where they give the operator the contact or address to use.
- Options: (a) Preferred: remove them. (b) Give `TenderRecipientParty` the electronic address tenders are submitted to.
- Needs decision: no

### tender/09#F5 · Low · The project is named "… for the city parks" here and "… for the parks renewal programme" everywhere else
- XPath: `/ProcurementStatus/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/ProcurementStatus/cbc:ContractName` = `Park benches for the parks renewal programme`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme`
- Why: `ProcurementProject/Name` is "a name of this procurement project". The notices name the project "Park benches for the parks renewal programme", and this document uses that name itself as `ContractName`. Its `ProcurementProject` has another name, which occurs only in 08, 09 and 24 (`grep -c "Park benches for the city parks" world/examples/tender/*.xml`). A reader matching the status exchange to a procedure by name finds two names for one project in one document.
- Condition: The project has the same name in `ProcurementProject/Name` as in the notices (or the name of the lot, where the document is about one lot).
- Options: (a) Preferred: use the name of the notices. (b) None other seen.
- Needs decision: no

### tender/09#F6 · Low · Issued by the department on a Saturday, outside the hours its contact states
- XPath: `/ProcurementStatus/cbc:IssueDate` = `2026-02-21`
- XPath: `/ProcurementStatus/cbc:IssueTime` = `11:44:00`
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: 2026-02-21 is a Saturday (1 January 2026 is a Thursday; my own calculation, assuming the common calendar). The procurement office that signs this status states that it is reachable on weekdays from 08:00 to 17:00.
- Condition: The issue date of a document signed by the procurement office is a working day, or the document says it is generated automatically.
- Options: (a) Preferred: Monday 2026-02-23 (still three days before the deadline). (b) Keep it and extend the contact note.
- Needs decision: no

### tender/09#F7 · Low · Customs trader numbers of the parties in a procedure status
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. Nothing in this document is declared to customs; the numbers are used only when the benches cross the border (30, 31). They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- `ProcedureStatusRequestDocumentReference` `BF-DOC-26-0194` is 08, issued the day before by the operator this status is addressed to; the note answers the question of 08.
- Tender deadline 2026-02-26 12:00 and procedure code OPEN agree with 02 and 03; the four legislation IDs are those of the notices.
- GLN 9523710900008: check digit correct (`check_ids.py`).

## Considered and refuted
- `/ProcurementStatus/cac:TenderSubmissionDeadlinePeriod`: suspected stale — refuted, it lies five days after the issue date and is the subject of the answer.
