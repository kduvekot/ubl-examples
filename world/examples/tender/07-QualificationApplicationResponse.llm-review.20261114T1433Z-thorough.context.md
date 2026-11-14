# LLM review: 07-QualificationApplicationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/07-QualificationApplicationResponse.xml`, Git blob `b7881bd86aa8b49492a0144e2fe61673b25b13f4` (committed)
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

### tender/07#F1 · High · "All criteria answered", but one property of six is answered
- XPath: `/QualificationApplicationResponse/cbc:Note` = `All criteria answered.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-TURNOVER`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:Note` = `Answer every criterion.`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:ID` = `CR-DEBT`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:ID` = `CR-TAXES`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:ID` = `P-6`
- Why: The request 06 has three criteria (turnover, debt ratio, payment of taxes) with six properties (P-1 to P-6) and says "Answer every criterion." This response lists one criterion (`CR-TURNOVER`) and has one criterion response, for P-1. The debt ratio and, above all, the exclusion ground on unpaid taxes (P-6, a question) are not answered, nor are years in business, registration and consortium share (P-2 to P-4). The note says the opposite.
- Condition: The response has a criterion response for every property of 06 that the operator must answer, and the note agrees with what is answered.
- Options: (a) Preferred: add the missing responses (the values for years in business and registration are already in this document, in the wrong place; see the next finding). (b) Change the note and the story to a partial answer, which the buyer would have to reject or query.
- Needs decision: no

### tender/07#F2 · Medium · One response value carries twelve answers of different types, most of them not answers to the property
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Response` = `As in the accounts.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseBinaryObject` = `QW5udWFsIGFjY291bnRzIDIwMjUsIGV4dHJhY3Qu`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseCode` = `MET`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseDate` = `2025-12-31`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseID` = `BF-ACC-2025`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseIndicator` = `true`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseMeasure` = `12`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseNumeric` = `26`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseQuantity` = `26`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseTime` = `12:00:00`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseURI` = `https://www.brackenmere.example/accounts-2025.pdf`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:ValueDataTypeCode` = `AMOUNT`
- Why: Each `Response…` element is "a … used as a reply to the criterion requirement". The response replies to property P-1, whose data type in 06 is `AMOUNT`: the reply is `ResponseAmount` 410000.00. The same response value also holds a number 26 and a quantity of 26 years (the answer to P-2, years in business, which has its own property), an indicator `true` (the type of P-3), a measure of 12 months, a time 12:00:00, a date, a code `MET` (a verdict that is the evaluator's, not the responder's), an identifier that is the document number of the accounts (already given as evidence), a URI of the accounts, a text and a "binary object" that is a 30-character plain-text sentence ("Annual accounts 2025, extract.", not "a binary graphic, picture, sound or video object"). A turnover has no time of day and no duration of 12 months. The value is filled with one element of every type (CLAUDE.md: no fillers; every value needs a business reason).
- Condition: A response value carries the reply in the element that matches the data type of the property it answers; answers to other properties are in their own criterion responses; supporting documents are given as evidence.
- Options: (a) Preferred: keep `ResponseAmount` here; move 26 years to a response for P-2 and the indicator to a response for P-3; drop time, measure, code, binary object and the duplicate ID/URI. (b) If each type must be shown, give the request properties that really ask for a date, a URI, a code and so on.
- Needs decision: no

### tender/07#F3 · Medium · The response does not identify the request it answers
- XPath: `/QualificationApplicationResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-ESPD-26`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:ID` = `LPWD-DOC-26-0192`
- XPath: `/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`
- Why: The response names criteria and properties by the IDs the request defined (`CR-TURNOVER`, `P-1`), but it has no reference to the request itself (`LPWD-DOC-26-0192`). Its only document reference is `BF-ESPD-26`, an ID that no example carries and that has no document type; if it is the operator's own number for this self-declaration, it is a second number for the document whose ID is `BF-DOC-26-0193`. The criterion and property IDs are only meaningful within the request; without it the response cannot be matched.
- Condition: The response refers to the qualification application request by its document ID, and every other reference says what it refers to.
- Options: (a) Preferred: an `AdditionalDocumentReference` to `LPWD-DOC-26-0192` with a document type; drop `BF-ESPD-26` or explain it. (b) None other seen.
- Needs decision: no

### tender/07#F4 · Medium · A language code in `LocaleCode`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/07#F5 · Low · Turnover is asked for three years and answered for one
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:Description` = `Yearly turnover of 410,000 lume.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description` = `Turnover 2025.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:StartDate` = `2025-01-01`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:EndDate` = `2025-12-31`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Description` = `Turnover of the last three years.`
- XPath: `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:StartDate` = `2023-01-01`
- Why: The criterion is "Turnover of the last three years" and property P-1 applies to 2023-01-01 to 2025-12-31. The response gives one figure, for 2025, with an applicable period of 2025 only. The years 2023 and 2024 are not answered, so the buyer cannot tell whether the minimum was reached in each year or on average.
- Condition: The response covers the period the property asks for (one value per year, or the average with that period).
- Options: (a) Preferred: three response values, one per year. (b) Ask only for the last year in 06.
- Needs decision: no

### tender/07#F6 · Low · A single operator names itself as the "economic operator group"
- XPath: `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere Furniture`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: `EconomicOperatorGroupName` is the "Economic Operator Group Name associated with this Qualification", the name of a group of operators (consortium) that applies together. Brackenmere Furniture applies alone (its tenders 17 and 19 name no partner); its own name is not a group name and repeats the party name.
- Condition: The group name is present only when a group of operators applies, and is then the name of the group.
- Options: (a) Preferred: remove it. (b) None other seen.
- Needs decision: no

### tender/07#F7 · Low · "No weighting" repeated from the request
- XPath: `/QualificationApplicationResponse/cbc:WeightingTypeCode` = `NONE`
- XPath: `/QualificationApplicationResponse/cbc:WeightScoringMethodologyNote` = `Pass or fail.`
- Why: Weighting and scoring method are the buyer's rules; the operator's response repeats them, and what it repeats is that there is no weighting (see the same finding in 06). The response has nothing to weight.
- Condition: The response does not restate that there is no weighting.
- Options: (a) Preferred: remove both. (b) None other seen.
- Needs decision: no

## Checked and consistent
- Turnover 410000.00 lume is above the minimum of 250000.00 lume of P-1 in 06 and of the notices.
- Criterion ID `CR-TURNOVER` and property ID `P-1` exist in 06; lot `LOT-1`, classification 38111, procedure code and folder agree with 06.
- `SuppliedEvidence` `EV-ACC-BF` is defined in `Evidence` (annual accounts 2025, document `BF-ACC-2025`), and the confidentiality level is the same in both places.
- GLN 9523710900008: check digit correct (`check_ids.py`).

## Considered and refuted
- `/QualificationApplicationResponse/cac:Evidence/cac:EvidenceIssuingParty` = the operator itself: suspected wrong issuer for "audited" accounts — refuted, the annual accounts are issued by the company; the auditor issues the opinion.
- `/QualificationApplicationResponse/cac:Evidence/cbc:CandidateStatement` = "True and complete.": the definition speaks of a statement "that the contracting authority accepts as a sufficient response"; suspected to be the buyer's element — refuted, it is the text of the candidate's own statement, which is what the buyer accepts.
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ConfidentialityLevelCode` = CONFIDENTIAL: suspected to conflict with public evaluation — refuted, turnover figures are commonly confidential.
- `/QualificationApplicationResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-ESPD-26`: "ESPD" is a term of EU procurement in a fictional world — refuted as a clash, the UBL definition of the request itself speaks of a "Single Procurement Document"; the open point is only what the ID refers to (finding above).

## Outside this review
- The tenders of this operator (17, 19) cite as qualification the document `VI-DOC-26-0199`, which is the qualification of Valdara Industries (13), not this response; that lies in 17 and 19.
