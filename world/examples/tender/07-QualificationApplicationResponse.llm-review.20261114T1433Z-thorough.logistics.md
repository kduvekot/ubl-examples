# LLM review: 07-QualificationApplicationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

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

### tender/07#F1 · High · "All criteria answered", but one of six properties is answered
- XPath: `/QualificationApplicationResponse/cbc:Note` = `All criteria answered.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-TURNOVER`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- Why: the request this document answers (`06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:Note` = `Answer every criterion.`) defines three criteria (`CR-TURNOVER`, `CR-DEBT`, `CR-TAXES`) with six properties `P-1` to `P-6`. The response contains one `TenderingCriterion` (`CR-TURNOVER`) and one `TenderingCriterionResponse`, for `P-1`. The debt ratio (`P-5`), the unpaid taxes (`P-6`, an exclusion ground), the business registration (`P-3`), the years in business (`P-2`) and the consortium share (`P-4`) have no response of their own. The note contradicts the content, and a qualification response that leaves the exclusion ground unanswered does not serve its purpose.
- Condition: there is a `TenderingCriterionResponse` for every property of the request that applies to the operator, each with its `ValidatedCriterionPropertyID`; the note agrees with what is answered.
- Options: (a) add responses for P-2, P-3, P-5 and P-6 (P-4 does not apply to a single operator) (preferred); (b) reword the note to say that only the turnover is answered here, if the rest is in the referenced self-declaration.
- Needs decision: no

### tender/07#F2 · Medium · One response value for the amount property carries values of every other kind
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseQuantity` = `26`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseNumeric` = `26`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseMeasure` = `12`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseTime` = `12:00:00`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseDate` = `2025-12-31`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseIndicator` = `true`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseCode` = `MET`
- Why: the response is tied to property `P-1`, which the request declares as an amount (`06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:ValueDataTypeCode` = `AMOUNT`). Only `ResponseAmount` (410000.00 XBL, above the minimum of 250000.00) answers it. The same `ResponseValue` also holds a quantity and a number of 26 (years; this is the answer to `P-2`, "years in business", filed under the wrong property), a measure of 12 months, a time of 12:00:00, an indicator and a code. Each is "… used as a reply to the criterion requirement", but the requirement asks for none of them; the time of day in particular answers nothing about a yearly turnover (rule "no fillers"). The date 2025-12-31 is at least the balance-sheet date of the accounts.
- Condition: a `ResponseValue` carries the value type its property asks for; answers to other properties are in responses that name those properties.
- Options: (a) keep amount, description, the evidence ID/URI, and move 26 ANN to a response for P-2 and the indicator to one for P-3 (preferred, it also resolves F1 in part); (b) remove the values that answer nothing.
- Needs decision: no

### tender/07#F3 · Medium · Turnover asked for three years, answered for one
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:StartDate` = `2025-01-01`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:EndDate` = `2025-12-31`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description` = `Turnover 2025.`
- Why: the request asks for the "turnover of the last three years" and gives property `P-1` the period `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:StartDate` = `2023-01-01` to 2025-12-31, with a sub-criterion "Average turnover". The response covers 2025 only; the turnover of 2023 and 2024, and the average, are missing, so the property is not answered for the period it applies to.
- Condition: the response covers the period of the property (one value per year, or the three-year average with that period).
- Options: (a) three `ResponseValue`s for 2023, 2024 and 2025 (preferred); (b) one value stated as the three-year average with the period 2023-01-01 to 2025-12-31.
- Needs decision: no

### tender/07#F4 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/07#F5 · Low · The response does not name the request it answers, and its one document reference does not say what it is
- XPath: `/QualificationApplicationResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-ESPD-26`
- Why: the document answers `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:ID` = `LPWD-DOC-26-0192`, but that ID appears nowhere in it; the link exists only through `ContractFolderID` and the criterion and property IDs. The only `AdditionalDocumentReference` carries the ID `BF-ESPD-26` and nothing else. No document of the flow has this ID; by its name it is a self-declaration of the operator, which is what this response itself is (its own ID is `/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0193`). A reader cannot tell whether it is another document or this one under a second number.
- Condition: the response refers to its request by ID, and every other reference states the kind of document.
- Options: (a) add an `AdditionalDocumentReference` to `LPWD-DOC-26-0192` with a document type, and give `BF-ESPD-26` a document type or remove it (preferred); (b) leave the request implicit and only type the existing reference.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` has a correct check digit.
- Issued 2026-02-19 10:47, six days after the request (2026-02-13) and before the tender deadline (2026-02-26 12:00) and Brackenmere's tenders (17: 2026-02-23, 19: 2026-02-24).
- `ContractFolderID`, `ProcedureCode` OPEN, `QualificationApplicationTypeCode` REGULATED, `WeightingTypeCode` NONE, `LOT-1` and CPC 38111 equal the request; `CR-TURNOVER` and `P-1` exist in the request.
- `ResponseAmount` 410000.00 XBL exceeds the required 250000.00 XBL; `ResponseCode` MET agrees.
- `SuppliedEvidence/ID` `EV-ACC-BF` is the `Evidence/ID` defined in the document; its `DocumentReference` `BF-ACC-2025` equals `ResponseID`, and the URI names the accounts of 2025; `ResponseBinaryObject` decodes (Base64) to "Annual accounts 2025, extract.", matching `text/plain`.
- Unit codes MON, ANN; XBL; world-list codes resolve.

## Considered and refuted
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseID`: an identifier as a reply to an amount property — refuted as a separate finding because it is the ID of the evidence document (`BF-ACC-2025`), which the same response supplies.
- `/QualificationApplicationResponse/cac:Evidence/cac:DocumentReference/cbc:ID`: `BF-ACC-2025` resolves to no example — refuted because annual accounts are not a UBL document of the flow; the evidence block says what it is (annual accounts 2025, audited, issued by Brackenmere).
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseDate`: accounts of 2025 audited by 2026-02-19 — refuted, seven weeks after year end is fast but possible for a small company, and it is a timeline matter.
