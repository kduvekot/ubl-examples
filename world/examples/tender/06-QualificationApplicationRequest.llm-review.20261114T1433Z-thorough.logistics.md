# LLM review: 06-QualificationApplicationRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/06-QualificationApplicationRequest.xml`, Git blob `0aa9ad5b8c13d2a778a247ffd72698f140609eec` (committed)
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

### tender/06#F1 · High · Call for tenders referenced under an ID that no document has
- XPath: `/QualificationApplicationRequest/cac:AdditionalDocumentReference/cbc:ID` = `PWD-2026-PARKS-CFT`
- Why: the reference is "a reference to an additional document associated with this document"; by its ID it means the call for tenders. The call for tenders of the procedure, issued the day before this request, is `03-CallForTenders.xml:/CallForTenders/cbc:ID` = `LPWD-DOC-26-0189`; no example has the document ID `PWD-2026-PARKS-CFT`, and the catalogue refers to the call for tenders by its real ID (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:CallForTendersDocumentReference/cbc:ID` = `LPWD-DOC-26-0189`). The reference carries only the ID, no document type, so nothing else tells the operator which document is meant. The ID occurs in 8 examples (01, 02, 03, 06, 15, 17, 19, 24; `grep -l` over `tender/*.xml`).
- Condition: the reference carries the ID of example 03 (or of another existing document), and says what kind of document it is.
- Options: (a) `LPWD-DOC-26-0189` with a document type "Call for tenders" (preferred); (b) give the call for tenders the ID `PWD-2026-PARKS-CFT` throughout the flow.
- Needs decision: no

### tender/06#F2 · Medium · A yes/no property that also expects an identifier, a code and a URI
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ValueDataTypeCode` = `INDICATOR`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedIndicator` = `true`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedID` = `REG`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedCode` = `REGISTERED`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[3]/cbc:ExpectedURI` = `https://register.bayvarra.example`
- Why: property `P-3` ("Registered in a business register") declares its answer to be an indicator and expects `true`. It also carries `ExpectedID`, "the expected identifier that the responder has to provide in the criterion response", `ExpectedCode`, "the expected code that the responder has to provide", and `ExpectedURI`, "the expected URL that the responder has to provide". A responder cannot provide the identifier `REG`: it is not an identifier of anything (a register number would differ per operator and cannot be expected in advance), and the URI is the register's address, not something the responder provides. For an indicator-type property only `ExpectedIndicator` has a meaning; the other three have no business reason here (rule "no fillers") and contradict the declared data type.
- Condition: a property expects a value only in the element that matches its `ValueDataTypeCode`; an expected identifier, where present, is an identifier the responder can actually give.
- Options: (a) keep `ExpectedIndicator` and `ExpectedDescription`, remove `ExpectedID`, `ExpectedCode` and `ExpectedURI` (preferred); (b) split into separate properties (a code-type and a URI-type question), each with one expected value.
- Needs decision: no

### tender/06#F3 · Medium · Language code in LocaleCode
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/QualificationApplicationRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/06#F4 · Low · Document number ahead of its date in the department's own series
- XPath: `/QualificationApplicationRequest/cbc:ID` = `LPWD-DOC-26-0192`
- XPath: `/QualificationApplicationRequest/cbc:IssueDate` = `2026-02-13`
- Why: the ID is "assigned by the sender". The department's document numbers run in one series (`LPWD-DOC-26-0187`, `-0188`, `-0189`, `-0191`, `-0192`, `-0195`, …). This document, number 0192, is issued on 2026-02-13, two days before the department's number 0191 (`05-ExpressionOfInterestResponse.xml:/ExpressionOfInterestResponse/cbc:IssueDate` = `2026-02-15`). A running number assigned at issue cannot be issued before a lower one. Across the flow the numbers 0187 to 0225 form one sequence over all senders in the order of the examples (the gaps in the department's series are the numbers of the other parties' documents), which shows the numbers follow the order of the examples, not the issue dates; the same occurs in 18 and, outside this part, in 19 and 21 to 23.
- Condition: within one sender's series, a higher number is not issued before a lower one (or the ID does not suggest a running number).
- Options: (a) issue this request after 05, e.g. on 2026-02-16 (still three days before the response 07) (preferred, smallest change); (b) number the documents per sender in the order of their issue times.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` (Brackenmere) has a correct check digit; the GS1 prefix 952 is reserved for demonstrations and examples (own knowledge), so it cannot be mistaken for a real company's.
- Issued 2026-02-13 08:25, the morning after the call for tenders (2026-02-12 13:26); the response 07 follows on 2026-02-19, a week before the tender deadline.
- `ContractFolderID`, `ProcurementProject/ID` `PWD-2026-PARKS`, `ProcedureCode` OPEN and `LOT-1` agree with 02/03.
- The turnover threshold 250000.00 XBL and "greater than twice the estimate" agree with the financial criterion of 01 to 03 (2 × 124080 = 248160, rounded up); "three years in business" agrees with `OperatingYearsQuantity` 3 there.
- `ApplicablePeriod` 2023-01-01 to 2025-12-31 is "the last three years" before the issue date; 2025-01-01 to 2025-12-31 is the last financial year for the debt ratio.
- `Legislation/ID` `XB-PPA-2019` is the procurement act referenced in the notices; criteria and property IDs (CR-…, PG-…, P-1 to P-6) are unique in the document.
- Codes: CPC 38111; ISIC 3100, 8411; unit codes ANN and P1 (percent); `ValueUnitCode` ANN with the Rec. 20 list name; XBL; world-list codes resolve.

## Considered and refuted
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[2]/cbc:MinimumQuantity`: the minimum of three years is stated three times (`ExpectedValueNumeric`, `MinimumValueNumeric`, `MinimumQuantity` 3 ANN) — refuted as a finding of this lens because the three values agree; whether all three are needed is a question of presence, not of consistency.
- `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumQuantity`: 80 with unit P1 beside `MaximumValueNumeric` 80 — refuted, same value, P1 is the Rec. 20 code for percent.
- `/QualificationApplicationRequest/cbc:IssueDate`: a qualification request sent after the call for tenders although the criteria are part of the procurement documents — refuted because the request is addressed to one operator (Brackenmere) and may follow the documents.
