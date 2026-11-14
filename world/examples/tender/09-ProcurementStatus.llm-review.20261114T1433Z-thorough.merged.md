# LLM review: 09-ProcurementStatus.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/09-ProcurementStatus.xml`, Git blob `e9ed8a2b58652c74ad8a9d6547388d6e5e2746db` (committed)
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

### tender/09#F1 · Medium · The status of an open procedure reports periods for invitations and requests to participate
- XPath: `/ProcurementStatus/cbc:ProcedureCode` = `OPEN`
- XPath: `/ProcurementStatus/cac:InvitationSubmissionPeriod/cbc:StartDate` = `2026-01-26`
- XPath: `/ProcurementStatus/cac:InvitationSubmissionPeriod/cbc:EndDate` = `2026-02-01`
- XPath: `/ProcurementStatus/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: The periods are "The period during which invitations to tender must be completed and delivered" and "The period during which requests for participation must be completed and delivered". The procedure is `OPEN`: any operator tenders directly, there are no invitations to tender and no requests to participate (own knowledge of procurement practice), and Brackenmere, the receiver, tenders in 17 and 19 without invitation. The status repeats the two periods from the notice and the call for tenders, where they end before those documents' own issue dates (2026-02-11 and 2026-02-12; a finding of 02/03); here they report two steps the procedure does not have and tell the operator nothing about its question, the tender deadline. Logistics also pointed to the expression of interest the department answered on 2026-02-15 (05), after the reception period; the merge does not count that as a contradiction, since an expression of interest is not a request for participation.
- Condition: The status of an open procedure reports only periods the procedure has (here the tender submission deadline).
- Options: (a) remove the two periods here (and in 02/03), keeping the tender deadline (preferred: the procedure is open in every example of the flow); (b) make the procedure restricted or two-stage throughout the flow (a story change).
- Needs decision: no
- From: broad (F1), context (F1), logistics (F1)

### tender/09#F2 · Medium · Language code in LocaleCode
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProcurementStatus/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale. Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales.
- Options: (a) remove `LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F2), context (F2), logistics (F2), parties (F1)

### tender/09#F3 · Medium · The contracting authority, a public body, described as a company in a commercial register with a liquidation status
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status" (`ACTIVE`: "Active, not in liquidation"); `COMMERCIAL` is "Commercial register: A register of businesses". Lumeport Public Works Department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411); it is not a business and cannot be in liquidation.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies, keeping register name and number (preferred); (b) a register type for public bodies; (c) record the convention in the world's rules.
- Needs decision: no
- From: broad (F4), parties (F4)

### tender/09#F4 · Low · Issued and signed by the procurement office on a Saturday, outside the hours its contact states
- XPath: `/ProcurementStatus/cbc:IssueDate` = `2026-02-21`
- XPath: `/ProcurementStatus/cbc:IssueTime` = `11:44:00`
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: For the argument (context): 2026-02-21 is a Saturday (re-done in the merge: 2026-01-01 is a Thursday, 21 February is 51 days later, 51 = 7 × 7 + 2), and the procurement office that signs the status says it is reachable on weekdays 08:00–17:00. Against it (broad): the examples nowhere say that the world's week follows the real calendar, and a platform can send a status at any time; the contact note states when the office can be reached, not when documents may be issued. Earlier merges did treat weekday names in the world as real-calendar weekdays. The merge cannot settle whether a Saturday issue is a problem in the world, so it stays Low with both arguments.
- Condition: A document signed by the procurement office is issued on a working day, or the world records that the office or its platform issues documents on Saturdays.
- Options: (a) Monday 2026-02-23, still three days before the deadline (preferred); (b) keep it and extend the contact note, or state that the status is generated by the platform.
- Needs decision: yes
- From: context (F6); refuted by broad (carried as the counter-argument)

### tender/09#F5 · Low · Four legislation references in an answer about a deadline
- XPath: `/ProcurementStatus/cac:ProcurementLegislationDocumentReference/cbc:ID` = `XB-PPA-2019`
- XPath: `/ProcurementStatus/cac:FiscalLegislationDocumentReference/cbc:ID` = `XB-STT-ACT`
- XPath: `/ProcurementStatus/cac:EnvironmentalLegislationDocumentReference/cbc:ID` = `XB-ENV-2021`
- XPath: `/ProcurementStatus/cac:EmploymentLegislationDocumentReference/cbc:ID` = `XB-LAB-2018`
- XPath: `/ProcurementStatus/cbc:Note` = `The deadline stands; the answers did not change the documents.`
- Why: For the argument (context): the operator asked whether the deadline stands (08), and the note answers exactly that; the status also lists the procurement, tax, environmental and labour legislation of the procedure, none of which changed or bears on the question, each with an ID only. Against it (broad): the document is "A document sent by a Contracting Party to an Economic Operator describing the status of a procurement procedure, Project, or Lot", i.e. of the procedure as a whole, its model provides exactly these references, and the IDs agree with the notices. Whether a status answering one question should restate the procedure's legislation cannot be settled from the definition; Low with both arguments.
- Condition: Either the status carries only what answers the request and what has changed, or the world records that a procedure status always restates the applicable legislation.
- Options: (a) remove the four references (preferred: nothing in the answer depends on them); (b) keep the procurement legislation only, with the article, if the rule on deadlines after clarifications is to be cited.
- Needs decision: yes
- From: context (F3); refuted by broad (carried as the counter-argument)

### tender/09#F6 · Low · The department's customs trader number in a procedure status
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Copied master data (section 4.8): a customs trader number identifies the department towards customs; nothing in this document is declared to customs (the numbers are used in the customs declarations 30 and 31).
- Condition: Each party carries only the identifiers the document uses or the receiver needs to identify it.
- Options: (a) leave the customs trader number to the customs and transport documents (preferred); (b) keep it if the world's rule is that every document carries all identifiers of a party, and state that rule.
- Needs decision: no
- From: context (F7), parties (F2)

### tender/09#F7 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `ExemptionReason` in `PartyTaxScheme` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" names a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is a buyer status and fits; the wording does not.
- Condition: The party's exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F5), parties (F3)

### tender/09#F8 · Low · Registration date 1 January 1996, shared by 25 unrelated companies
- XPath: `/ProcurementStatus/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Brackenmere Furniture shares the New Year's Day with 24 other parties, 271 times in 181 of the 250 examples (recounted: `grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, `-l` for files): a default, not a fact of each company.
- Condition: Each company has its own registration date (or none where the world has none).
- Options: (a) a date per company from its history (preferred); (b) drop the date where unused; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F5)

### tender/09#F9 · Low · Document provider and tender recipient only repeat the contracting party
- XPath: `/ProcurementStatus/cac:DocumentProviderParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ProcurementStatus/cac:TenderRecipientParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `DocumentProviderParty` is "The Party that provides the procurement documents to the Economic Operator", `TenderRecipientParty` "The Party to which tenders will be submitted". Both are the contracting party that issues the status, with register number and name only: no contact, address or channel that differs per role, so they say nothing the document does not already say (no fillers). Broad refuted the tender recipient because the role's definition is met; the merge keeps the finding, as merger A of this flow and the contest merges did for such repeated roles: meeting the definition does not give the repetition a business reason.
- Condition: Each role is present only where it names a party, office or contact that differs from the contracting party, or adds details specific to the role (e.g. the electronic address tenders go to).
- Options: (a) remove them (preferred); (b) give `TenderRecipientParty` the electronic address or contact that receives tenders.
- Needs decision: no
- From: context (F4), parties (F6)

### tender/09#F10 · Low · The project is named "… for the city parks" here and "… for the parks renewal programme" in the notices and in this document's own contract name
- XPath: `/ProcurementStatus/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/ProcurementStatus/cbc:ContractName` = `Park benches for the parks renewal programme`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme`
- Why: `ProcurementProject/Name` is "A name of this procurement project". The notices name the project "Park benches for the parks renewal programme", as does this document's `ContractName`; "Park benches for the city parks" occurs only in 08, 09 and 24 (recounted: `grep -rc --include='*.xml' 'Park benches for the city parks' world/examples`). The process is identified by `ContractFolderID`, so this is an inconsistency of the name only.
- Condition: The project has the same name as in the contract notice.
- Options: (a) use the notice's name (preferred); (b) drop the name.
- Needs decision: no
- From: broad (F3), context (F5), logistics (F3)

## Checked and consistent
- `ProcedureStatusRequestDocumentReference` `BF-DOC-26-0194` resolves to 08, a procurement status request by the same operator, issued 2026-02-20 15:50; this status follows on 2026-02-21 11:44; parties, folder, contract name and lots are those of 08, and the note answers 08's question.
- `TenderSubmissionDeadlinePeriod` 2026-02-26 12:00 equals the deadline in 02 and 03, lies after the issue time and agrees with the note ("The deadline stands").
- The four legislation references carry the IDs of 01 to 03, each in the element for its kind of legislation; procedure code OPEN and lots `LOT-1`/`LOT-2` agree with the notice.
- `check_ids.py`: GLN `9523710900008` has a correct check digit. Parties described as in the other examples of the flow (parties compared by script); ISIC 3100 and 8411 fit; +999 telephone numbers and `.example` addresses.

## Considered and refuted
- `/ProcurementStatus/cac:TenderSubmissionDeadlinePeriod`: suspected stale — refuted, it lies five days after the issue date and is the subject of the answer (from context).
- `/ProcurementStatus/cac:ParticipationRequestReceptionPeriod/cbc:EndDate`: a period that is over when the status is issued, as a finding of its own — refuted, a status may report past periods; the problem is that the procedure has no such period (F1) (from logistics).
- `/ProcurementStatus/cbc:ID`: `LPWD-DOC-26-0195` after `LPWD-DOC-26-0192` (2026-02-13) and `-0191` (2026-02-15) — refuted, issued later than both (from logistics).
- `/ProcurementStatus/cbc:Note`: no code for the state of the procedure — refuted, UBL's ProcurementStatus has no such element at document level; the note and the deadline give the state (from logistics).
- `/ProcurementStatus/cac:ProcurementLegislationDocumentReference`: four legislation references in an answer about the deadline — refuted by broad (the document describes the status of the procedure as a whole); the merge disagrees in part and keeps context's finding as F5, Low/yes, with this argument.
- `/ProcurementStatus/cbc:IssueDate`: a Saturday in the real calendar — refuted by broad (the world's calendar is not stated; a platform can send at any time); kept as F4, Low/yes, with this argument.
- `/ProcurementStatus/cac:TenderRecipientParty`: repeats the contracting party — refuted by broad (the role's definition is met); the merge keeps it as F9 (above).
- `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` = `-1` — refuted, no format prescribed, reads as UTC−1 (from parties).
- `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` — refuted, fits "The specific identifable location within a building where mail is delivered" (from parties).
- `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office` — refuted, a functional contact name; "Procurement office" and "Procurement" name the same unit (from parties).
- `/ProcurementStatus/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` = `STATE` — refuted, the level of the tax, not of the party (from parties).
- `/ProcurementStatus/cac:EconomicOperatorParty/cac:Party/cac:Contact`: a sales contact ("Trade sales") for a procurement procedure — refuted, for a small manufacturer the sales office handles tenders (from parties).

## Changed in the merge
- broad/F1, logistics/F1 (Needs decision yes), context/F1 (no) → F1 no: the procedure is open in every example; removing periods it does not have is encoding. Option (b) stays as the story alternative.
- broad/F4, parties/F4 (Low) → F3 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies).
- context/F6 (Low/no) → F4 Low/yes: broad refuted it; the merge cannot settle it.
- context/F3 (Low/no) → F5 Low/yes: broad refuted it; the merge cannot settle it.
- parties/F5 (Needs decision no) → F8 yes: aligned with analysis/review-merge-decisions.md (RegistrationDate 1996-01-01).
- context/F4 and parties/F6 combined → F9.

## Outside this review
- The invitation and participation periods of the notice and the call for tenders end before those documents were issued (2026-02-01 and 2026-02-11 against 2026-02-11 and 2026-02-12); that lies in 02 and 03 (from logistics).
