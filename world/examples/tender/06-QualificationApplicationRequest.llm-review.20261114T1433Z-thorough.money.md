# LLM review: 06-QualificationApplicationRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

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

### tender/06#F1 · Medium · Turnover requirement: the "expected amount" is the threshold, not an amount the responder has to give
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:ExpectedAmount` = `250000.00`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:MinimumAmount` = `250000.00`
- Why: `ExpectedAmount` is "The expected amount that the responder has to provide in the criterion response"; `MinimumAmount` "The minimum amount the response must have." The responder gives its own turnover (`07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`), and any amount of at least 250000.00 passes. There is no amount the answer is expected to equal; the threshold is already in `MinimumAmount`. As it stands the property says both "answer 250000.00" and "answer at least 250000.00".
- Condition: the threshold of the turnover requirement is carried once, as the minimum; no expected amount is given for a value that every responder answers differently.
- Options: (a, preferred) drop `ExpectedAmount`; (b) none seen that keeps it.
- Needs decision: no

### tender/06#F2 · Low · What has to reach 250000: each year, the average, or one year; "at least" here, "greater than" in the notice
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Name` = `General yearly turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:Description` = `Turnover of the last three years.`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:SubTenderingCriterion/cbc:Name` = `Average turnover`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:StartDate` = `2023-01-01`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cac:ApplicablePeriod/cbc:EndDate` = `2025-12-31`
- Why: the property asks for a "Yearly turnover" of at least 250000.00 over a period of three years, under a criterion that speaks of the turnover "of the last three years" and has a sub-criterion "Average turnover". The request does not say whether each of the three years, their average or their sum must reach the minimum. The responder answers with one year (`07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ApplicablePeriod/cbc:StartDate` = `2025-01-01`). The published terms are different again: one "Yearly turnover", compared with "greater than" (`02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`), whereas a minimum includes the threshold itself.
- Condition: the request states which turnover figure is compared with the minimum (per year, or the three-year average), with a period that fits, and the comparison is the same as in the notice.
- Options: (a, preferred) "average yearly turnover 2023–2025 of at least 250,000 lume", in the request and in the notices; (b) the last year only, with the period 2025.
- Needs decision: no

### tender/06#F3 · Low · A debt-ratio criterion that the published terms do not contain
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:Name` = `Debt ratio`
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumValueNumeric` = `80`
- Why: the criterion is pass or fail (`/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:EvaluationMethodTypeCode` = `PASSFAIL`): a tenderer whose liabilities exceed 80 % of its assets fails. The contract notice and the call for tenders, which set the conditions of the procedure, name one financial criterion only, the turnover (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:EvaluationCriterionTypeCode` = `TURNOVER`). A selection criterion applied to a tenderer but not published is a difference between the documents; and the response in example 07 does not answer it.
- Condition: every financial criterion of the request is among the criteria of the notice and the call for tenders (or the other way round, the request asks only what was published).
- Options: (a, preferred) add the debt ratio as a second financial evaluation criterion to the notices; (b) drop it from the request.
- Needs decision: yes

## Checked and consistent
- The turnover minimum of 250000.00 equals the threshold amount of the notices (examples 01–03); the currency of the value (`ValueCurrencyCode` XBL) matches the currency of the amounts.
- Debt ratio: `MaximumValueNumeric` 80 and `MaximumQuantity` 80 with unit P1 (percent) state the same limit; the period 2025 fits "the last annual accounts".
- Unpaid taxes: the limit of 1000.00 lume gives a figure to the "minor amounts" of the criterion's description and of the legislation entry.

## Considered and refuted
- `/QualificationApplicationRequest/cac:TenderingCriterion[1]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty[1]/cbc:MinimumAmount`: suspected a conflict with "twice the estimate" (248160) — refuted for this example because the request does not mention the estimate; it repeats the notices' threshold amount. The difference lies in the notices and is raised there.
- `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:MaximumQuantity`: suspected a duplicate of `MaximumValueNumeric` — refuted because the two elements are alternative carriers of the same limit (a number, and a quantity with the unit percent) and agree.
