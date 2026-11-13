# LLM review: 05-ExceptionCriteria.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/05-ExceptionCriteria.xml`, Git blob `440e2b01e4a52b0bcacdcd69708f6bc057bfaf71` (committed)
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

### furniture/05#F1 · Low · The slow-sales threshold has no time basis
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ThresholdQuantity` = `5`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:Note` = `Slow sales.`
- Why: A sales threshold of "less than 5 sets" only means something per period of time (per week, per four weeks, per season). The line says nothing about it: an exception criteria line has no time element of its own other than its effective period (2026-03-23 to 2026-08-29, 23 weeks), and the forecast line's `TimeDeltaDaysQuantity` belongs to line 2 only. The flow applies the threshold to four weeks (`07-ExceptionNotification.xml:/ExceptionNotification/cac:ExceptionNotificationLine/cbc:Note` = `Three sets sold against five expected.`, over 2026-03-23 to 2026-04-20), while the information request asked for weekly figures (`03-ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:TimeFrequencyCode` = `WEEKLY`). Against weekly figures, "fewer than 5 sets a week" would be met almost every week with 20 sets for the season.
- Condition: the criterion states the period over which sales are compared with the threshold, and that period is the one the exception notification uses.
- Options: (preferred) state the basis in the line's note ("fewer than 5 sets in four weeks"), since UBL has no structured element for it on an operational criterion; or move the criterion to a forecast line where `TimeDeltaDaysQuantity` can carry 28 days, if the story treats it as a comparison against the plan.
- Needs decision: no

### furniture/05#F2 · Low · Line 1 sets codes of two exception types
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- Why: UBL defines `SupplyChainActivityTypeCode` here as establishing "the criterion for one of the three types of exceptions … Operational, Metric and Forecast Exceptions. This will be set if this Exception is about an Operational Exception." The line also sets a performance metric, so it is both an operational and a metric criterion. Sales in units of one item over a period is the operational quantity "sales"; the metric code adds nothing the activity code does not already say.
- Condition: each criteria line is of one exception type.
- Options: (preferred) keep `SupplyChainActivityTypeCode` = SALES only; or keep the metric only and drop the activity code, if the criterion is meant as a performance metric.
- Needs decision: no

### furniture/05#F3 · Low · Comparison and resolution codes differ from the values UBL names
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ThresholdValueComparisonCode` = `LT`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cbc:ThresholdValueComparisonCode` = `GT`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ExceptionResolutionCode` = `REVIEW`
- Why: UBL's definition of `ThresholdValueComparisonCode` says "Allowed values are: EXCEEDS_EXCEPTION_VALUE FALLS_BELOW_EXCEPTION_VALUE", and that of `ExceptionResolutionCode` lists "Possible values … DEFAULT_TO_AVERAGE_OF_COMPARED_VALUES DEFAULT_TO_BUYERS_VALUE DEFAULT_TO_HIGH_VALUE …". The world's lists use other codes (LT/GT, REVIEW), while for neighbouring elements of the same line they follow the values UBL names (`CollaborationPriorityCode` HIGH, `SupplyChainActivityTypeCode` SALES). For the comparison code the definition says "allowed", so the deviation is from the definition, not only from practice. A joint review is not one of the listed resolutions, which all default to a value.
- Condition: the comparison code uses the values the definition allows (or the list records why it departs from them), and the resolution code either uses a listed value or the list records the extension.
- Options: (preferred) give the world's ThresholdValueComparisonCode list the two values UBL names; keep REVIEW as a documented extension, since a joint review is the story's real resolution; or record both departures as a finding about UBL's definitions.
- Needs decision: yes

## Checked and consistent
- Reference: `/ExceptionCriteria/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0570` resolves to `04-TradeItemLocationProfile.xml`; validity period 2026-03-16 to 2026-08-29 equals the profile's period.
- Line 1's effective period starts 2026-03-23, after the first delivery (invoice `09-Invoice.xml` of 2026-03-22), and is the start of the observation period of `07-ExceptionNotification.xml`.
- Line 2: threshold 30 in P1 (percent) with ComparisonDataSourceCode BUYER ("the store's own plan") against DataSourceCode SELLER, over 28 days; the codes agree with the note.
- Item identification matches the rest of the flow (BF-GS-01, GTIN 9523710000012, check digit passes).
