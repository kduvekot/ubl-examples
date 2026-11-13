# LLM review: 07-ExceptionNotification.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/07-ExceptionNotification.xml`, Git blob `c4c9313c99d0a0d896c6b32f955b12d7b8319fcf` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### furniture/07#F1 · High · Issue time of the compared actual data does not match the Product Activity report
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonDataCode` = `ACTUAL`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonForecastIssueDate` = `2026-04-20`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonForecastIssueTime` = `18:00:00`
- Why: The compared data are actual sales (ComparisonDataCode ACTUAL), and the line refers to the report that holds them (`/ExceptionNotification/cac:ExceptionNotificationLine/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0572`, i.e. `06-ProductActivity.xml`). That report was issued on 2026-04-20 at 16:35 (`06-ProductActivity.xml:/ProductActivity/cbc:IssueTime` = `16:35:00`), not at 18:00. No other source of actual sales exists in the flow. If the 18:00 refers to something else, the notification does not say what.
- Condition: the issue date and time of the compared data equal those of the document that holds them (2026-04-20 16:35 for `06-ProductActivity.xml`), or the forecast exception is removed (see F3).
- Options: (preferred) resolve together with F3: if the forecast exception goes, so does this time; if it stays, set the time to 16:35:00.
- Needs decision: no

### furniture/07#F2 · Medium · The line's criteria reference points to the Product Activity report
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0572`
- Why: UBL defines this reference on an exception notification line as "A reference to Exception Criteria document can be provided." The ID is the Product Activity report `06-ProductActivity.xml`, not the Exception Criteria `05-ExceptionCriteria.xml` (BS-DOC-26-0571), which is referenced only at document level (`/ExceptionNotification/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0571`). The line thus links to the data, not to the criterion it reports, and nothing tells which criteria line (1, slow sales, or 2, forecast deviation) was triggered.
- Condition: the line's document reference points to the Exception Criteria (BS-DOC-26-0571) and, where possible, identifies the triggered criterion (line 1); the Product Activity report is referenced at document level, where a generic reference fits.
- Options: (preferred) swap the two references: line → BS-DOC-26-0571, document → BS-DOC-26-0572 (or both at document level); add the criteria line in a description ("criterion line 1, slow sales").
- Needs decision: no

### furniture/07#F3 · Medium · A forecast exception in a sales-threshold exception, with sources that match no criterion
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:DataSourceCode` = `SELLER`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:IssueDate` = `2026-03-16`
- Why: UBL defines `SupplyChainActivityTypeCode` on this line as establishing "the criterion for one of the three types of exceptions: Operational, performance metric and forecast". The line carries all three: an activity code, a metric code and a `ForecastException`. What it reports (3 sets sold against a threshold of 5, "Sales below the agreed threshold") is criteria line 1 of `05-ExceptionCriteria.xml`, an operational criterion. The only forecast criterion is line 2, which compares the seller's forecast with the buyer's plan (`05-ExceptionCriteria.xml:/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cac:ForecastExceptionCriterionLine/cbc:ComparisonDataSourceCode` = `BUYER`) and is triggered by a deviation of more than 30 %, while the forecast exception here compares a seller forecast with actual sales. The forecast it names (issued 2026-03-16 10:00) is no document of the flow.
- Condition: the line reports one exception type, the one of the triggered criterion; a forecast exception, if kept, matches a forecast criterion (data source and comparison source) and refers to a forecast that the flow has.
- Options: (preferred) remove `ForecastException` and `PerformanceMetricTypeCode`, keeping the operational exception that the note, the description and the compared values describe; or, if the story wants a forecast exception too, add it as a second line that matches criteria line 2 (seller forecast against buyer plan, deviation in percent).
- Needs decision: no

### furniture/07#F4 · Low · Source and compared values look swapped
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:SourceValueMeasure` = `3`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:ComparedValueMeasure` = `5`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:VarianceQuantity` = `-2`
- Why: UBL: `SourceValueMeasure` is "The value used as the basis of comparison", `ComparedValueMeasure` "The value that was compared with the source value that resulted in the exception". The basis is the agreed threshold of 5 sets from the criteria; the value compared with it, which resulted in the exception, is the observed 3 sets. The example has them the other way round. The variance (−2) fits "observed minus basis" only with the values swapped (3 − 5 = −2); with the current assignment it is "source minus compared". The definitions are terse, so the other reading cannot be excluded.
- Condition: the threshold is the source (basis) value and the observed sales the compared value, with the variance as compared minus source; or a reason is recorded for the opposite reading.
- Options: (preferred) swap the two values (source 5, compared 3), keeping the variance −2; or keep them and record the reading.
- Needs decision: yes

## Checked and consistent
- References at document level: BS-DOC-26-0571 resolves to `05-ExceptionCriteria.xml`, BS-DOC-26-0572 to `06-ProductActivity.xml`.
- Observation period 2026-03-23 to 2026-04-20 equals the activity period of `06-ProductActivity.xml` and starts on the effective date of criteria line 1; the notification (2026-04-21 17:49) follows the report (2026-04-20 16:35).
- Arithmetic: 3 − 5 = −2 sets; the note "Three sets sold against five expected" agrees with the values.
- Codes: OPEN, HIGH, REVIEW, SALES resolve in the world's lists.

## Considered and refuted
- `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:Note`: suspected that "expected" misstates a minimum threshold — refuted because the agreed minimum is what the store expected to sell at least.
