# LLM review: 07-QualificationApplicationResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

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

### tender/07#F1 · High · "All criteria answered", but only the turnover is answered
- XPath: `/QualificationApplicationResponse/cbc:Note` = `All criteria answered.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-1`
- Why: the request this responds to has three criteria and tells the operator to "Answer every criterion." (`06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cbc:Note` = `Answer every criterion.`): the turnover (properties P-1 to P-4), the debt ratio (`06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:ID` = `P-5`) and unpaid taxes and contributions (`06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:ID` = `P-6`). The response has a single criterion response, for P-1, and names only the criterion CR-TURNOVER. The two other financial questions (liabilities as a share of assets, at most 80 %; unpaid taxes, at most 1000.00 lume) have no answer, so the note is not true and the pass-or-fail evaluation cannot be made.
- Condition: there is a criterion response for every property of the request that requires one, or the note says what is answered.
- Options: (a, preferred) add responses for P-5 (a percentage) and P-6 (an amount), and for P-2 to P-4 as far as they apply; (b) reduce the request to what is answered.
- Needs decision: no

### tender/07#F2 · Medium · The answer covers 2025 only; the requirement is for 2023 to 2025
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:StartDate` = `2025-01-01`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:EndDate` = `2025-12-31`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Description` = `Turnover 2025.`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`
- Why: property P-1 applies to the period `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:StartDate` = `2023-01-01` to 2025-12-31, under a criterion described as `06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Description` = `Turnover of the last three years.` The response gives one amount for 2025 and one evidence, the annual accounts of 2025. The turnover of 2023 and 2024 (or the average) is not given, yet the response code says the criterion is met.
- Condition: the response gives the turnover for the whole period the property asks for (one value per year, each with its period, or the average with the period 2023–2025), with evidence for those years.
- Options: (a, preferred) three response values, one per year, with the accounts of the three years as evidence; (b) if the request is changed to ask for the last year only, the response stays as it is.
- Needs decision: no

### tender/07#F3 · Medium · The response to an amount carries values of every other kind as well
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseNumeric` = `26`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseQuantity` = `26`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseMeasure` = `12`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseTime` = `12:00:00`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseDate` = `2025-12-31`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseIndicator` = `true`
- Why: the validated property P-1 has the value type amount (`06-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:ValueDataTypeCode` = `AMOUNT`), so its reply is `ResponseAmount`. The same response value also holds a number and a quantity of 26 years (which look like the answer to P-2, years in business), a measure of 12 months, a time of day, a date and an indicator. Each is defined as a value "used as a reply to the criterion requirement"; a turnover requirement has one reply. A reader cannot tell which of them is the answer, and the time of 12:00:00 answers nothing. This runs against the rule that every value needs a business reason.
- Condition: a response value holds the reply in the element that matches the property's value type, and answers to other properties are separate criterion responses that name their own property.
- Options: (a, preferred) keep amount, description and the reference to the accounts in the response to P-1; move the 26 years to a response to P-2 and the indicator to a response to P-3; drop measure and time; (b) none seen that keeps all values in one response.
- Needs decision: no

## Checked and consistent
- 410000.00 lume is above the minimum of 250000.00 of the request, so the code MET fits the amount given; `Description` "Yearly turnover of 410,000 lume." agrees with `ResponseAmount`; the currency is the one the request asks for (XBL).
- The evidence EV-ACC-BF (annual accounts 2025, document BF-ACC-2025) is the one the response value names in `ResponseID`.

## Considered and refuted
- `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount`: suspected that a yearly turnover of 410000.00 is too small for a tender of 119040.00 over two years (example 19) — refuted: the tender is about 59500 lume a year, some 15 % of the turnover, and the buyer's own threshold is 250000.00.
