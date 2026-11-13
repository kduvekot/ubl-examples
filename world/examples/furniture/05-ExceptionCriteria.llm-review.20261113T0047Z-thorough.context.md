# LLM review: 05-ExceptionCriteria.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/05#F1 · Medium · One criterion line is both an operational and a metric criterion
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- Why: In `ExceptionCriteriaLine`, `SupplyChainActivityTypeCode` "Establishes the criterion for one of the three types of exceptions. There can be three types of exception criteria: Operational, Metric and Forecast Exceptions. This will be set if this Exception is about an Operational Exception." `PerformanceMetricTypeCode` sets a metric criterion, and line 2 shows the third type (`ForecastExceptionCriterionLine`). Line 1 sets two of the three types at once, so it is not clear whether "Slow sales" is an operational criterion on sales activity or a performance-metric criterion on sales in units. The notification `07-ExceptionNotification.xml` then carries both as well.
- Condition: each criterion line establishes exactly one of the three types of exception.
- Options: (a) keep `SupplyChainActivityTypeCode` = `SALES` only (preferred: the threshold is a sales quantity in sets, i.e. an operational criterion); (b) keep the metric only, if the story means a performance metric.
- Needs decision: no

### furniture/05#F2 · Medium · LocaleCode holds a bare language code
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExceptionCriteria/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/05#F3 · Low · Sales threshold without a time basis
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ThresholdQuantity` = `5`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:EffectivePeriod/cbc:EndDate` = `2026-08-29`
- Why: "Sales less than 5 sets" is only a criterion when it says per what time interval. Line 1 gives no interval; its only period is the `EffectivePeriod` ("The period during which this exception criteria line is in effect", 2026-03-23 to 2026-08-29), which would mean fewer than 5 sets in the whole season and could not be judged before its end. The notification `07-ExceptionNotification.xml` nevertheless fires on four weeks (2026-03-23 to 2026-04-20, `07-ExceptionNotification.xml:/ExceptionNotification/cac:ExceptionNotificationLine/cbc:Note` = `Three sets sold against five expected.`). Line 2 has the time basis it needs (`/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cac:ForecastExceptionCriterionLine/cbc:TimeDeltaDaysQuantity` = `28`); line 1 has none.
- Condition: the criterion on line 1 states the interval its threshold applies to (e.g. four weeks), in a structured element or at least in the line note, and the notification's observation period matches it.
- Options: (a) state the four-week basis in the line note (preferred: there is no structured interval element for operational criteria); (b) express the criterion differently.
- Needs decision: no

### furniture/05#F4 · Low · ExceptionStatusCode, defined for shipment exceptions, used for the status of a criterion
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ExceptionStatusCode` = `ACTIVE`
- Why: UBL 2.5 defines `ExceptionCriteriaLine/ExceptionStatusCode` as "A code signifying status specific to a shipment exception". The value "Criterion in force" is the status of a sales criterion; there is no shipment exception. The definition reads like a copying error in UBL, but under the rule of semantic conformance the value does not meet it. Only line 1 carries it, so line 2 is not "in force" by the same reasoning.
- Condition: either `ExceptionStatusCode` is absent here, or the finding is recorded for the UBL TC and the use is consciously kept (then also on line 2).
- Options: (a) remove it (preferred: `ValidityPeriod` and `EffectivePeriod` already say the criterion is in force); (b) keep it and record the definition problem as a finding for the TC.
- Needs decision: yes

### furniture/05#F5 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:SupplyItem/cbc:BrandName` = `Brackenmere`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:SupplyItem/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` = the maker's name contradicts the description unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the description.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/05#F6 · Low · Sender's master data copied into the criteria
- XPath: `/ExceptionCriteria/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:AdditionalWebSite`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:SocialMediaProfile`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in exception criteria (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- Line 2: `ForecastExceptionCriterionLine` with data source `SELLER` and comparison source `BUYER`, threshold `GT` 30 percent, matches its note "Forecast far from the store's own plan."
- `ValidityPeriod` 2026-03-16 to 2026-08-29 equals the period of the profile `04-TradeItemLocationProfile.xml`, which `DocumentReference` refers to.
- `ExceptionResolutionCode` = `REVIEW` (joint review) agrees with the notification's `ResolutionCode` in `07-ExceptionNotification.xml`.

## Considered and refuted
- `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:EffectivePeriod/cbc:StartDate` = `2026-03-23`: a line starting a week after the document's validity was suspected to be inconsistent — refuted because a line may come into effect later; the first week after delivery is a plausible run-in.
- `/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cbc:ThresholdQuantity` = `30` in percent: a percentage as a "quantity" was suspected — refuted because `ThresholdQuantity` with unit percent is a quantity in UBL terms and fits a forecast variance.
