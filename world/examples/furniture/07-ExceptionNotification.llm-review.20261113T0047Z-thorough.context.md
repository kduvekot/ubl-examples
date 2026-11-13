# LLM review: 07-ExceptionNotification.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/07#F1 · Medium · Line reference meant for the Exception Criteria points to the Product Activity
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0572`
- Why: In `ExceptionNotificationLine`, `DocumentReference` is defined as "A reference to Exception Criteria document can be provided." The ID `BS-DOC-26-0572` is the Product Activity report `06-ProductActivity.xml`, not the Exception Criteria `05-ExceptionCriteria.xml` (`BS-DOC-26-0571`), which only the header refers to (`/ExceptionNotification/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0571`). A reference of one kind is used for another.
- Condition: the line's `DocumentReference` refers to the Exception Criteria (`BS-DOC-26-0571`, ideally with the criterion line), and the Product Activity, if referenced, is referenced where a reference to the source data is meant (e.g. the header `DocumentReference` with a document type).
- Options: (a) line reference to `BS-DOC-26-0571`, header references to both 0571 and 0572 with document types (preferred); (b) drop the line reference and keep both in the header.
- Needs decision: no

### furniture/07#F2 · Medium · One notification line is operational, metric and forecast exception at once
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException`
- Why: `SupplyChainActivityTypeCode` "Establishes the criterion for one of the three types of exceptions: Operational, performance metric and forecast. This reports an exception notification about an operational exception." The line sets the operational type, the performance metric type and a `ForecastException` ("A forecast accuracy or comparison exception") together. The exception actually reported is the operational one: "Sales below the agreed threshold", from criterion line 1 of `05-ExceptionCriteria.xml` (fewer than 5 sets), with 3 against 5 sets.
- Condition: each notification line reports exactly one type of exception, the type of the criterion it was raised against.
- Options: (a) keep `SupplyChainActivityTypeCode` = `SALES` and remove the metric code and `ForecastException` (preferred: matches criterion line 1 and the description); (b) separate lines for each exception actually raised.
- Needs decision: no

### furniture/07#F3 · Medium · The ForecastException compares a forecast that does not exist with data from another criterion
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:IssueDate` = `2026-03-16`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:IssueTime` = `10:00:00`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:DataSourceCode` = `SELLER`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonDataCode` = `ACTUAL`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonForecastIssueDate` = `2026-04-20`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonForecastIssueTime` = `18:00:00`
- Why: Apart from F2, the content of the `ForecastException` has no counterpart in the flow. (1) It names a seller's forecast "issued" on 2026-03-16 at 10:00; no forecast is exchanged in the flow, and the ExceptionCriteria line for forecasts compares the seller's forecast with the buyer's plan (`05-ExceptionCriteria.xml:/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cac:ForecastExceptionCriterionLine/cbc:ComparisonDataSourceCode` = `BUYER`), not with actual sales. (2) `ComparisonForecastIssueDate`/`Time` are "The date/time on which this comparison forecast was issued", but the comparison data is actual sales (`ACTUAL`), not a forecast; the only actual figures, `06-ProductActivity.xml`, were issued at a different time (`06-ProductActivity.xml:/ProductActivity/cbc:IssueTime` = `16:35:00`, not 18:00). The aggregate is filled with values that the definitions and the other documents do not support.
- Condition: either the `ForecastException` is absent (see F2), or the flow contains the forecast it names, the comparison matches a forecast criterion of `05-ExceptionCriteria.xml`, and the comparison issue date and time are those of the compared document.
- Options: (a) remove the `ForecastException` (preferred, together with F2); (b) add a forecast to the story and align criterion, comparison source and times.
- Needs decision: yes

### furniture/07#F4 · Medium · LocaleCode holds a bare language code
- XPath: `/ExceptionNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/07#F5 · Low · ExceptionStatusCode, defined for shipment exceptions, used for a sales exception
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:ExceptionStatusCode` = `OPEN`
- Why: UBL 2.5 defines `ExceptionNotificationLine/ExceptionStatusCode` as "A code signifying status specific to a shipment exception". The exception here is about sales, not a shipment. The value "Not resolved" is a sensible status, and the definition looks like a copying error in UBL, but under semantic conformance the value does not meet it.
- Condition: either `ExceptionStatusCode` is absent, or the use is kept consciously and the definition problem is recorded as a finding for the UBL TC.
- Options: (a) keep it and record the definition for the TC (preferred: an open status is useful for a notification asking for review); (b) remove it.
- Needs decision: yes

### furniture/07#F6 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:SupplyItem/cbc:BrandName` = `Brackenmere`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:SupplyItem/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` = the maker's name contradicts the description unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the description.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/07#F7 · Low · Receiver's master data copied into the notification
- XPath: `/ExceptionNotification/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:AdditionalWebSite`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:SocialMediaProfile`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in an exception notification (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `ComparedValueMeasure` 5 sets (the threshold of `05-ExceptionCriteria.xml` line 1), `SourceValueMeasure` 3 sets (the sales of `06-ProductActivity.xml`), `VarianceQuantity` −2 = 3 − 5.
- `ExceptionObservationPeriod` of header and line (2026-03-23 to 2026-04-20) equals the activity period of `06-ProductActivity.xml`; issue 2026-04-21 follows the report of 2026-04-20.
- `ResolutionCode` = `REVIEW` and `CollaborationPriorityCode` = `HIGH` agree with criterion line 1 of `05-ExceptionCriteria.xml` and with the note "Please review the line with us."

## Considered and refuted
- `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:Note` = `Three sets sold against five expected.`: "expected" for a minimum threshold was suspected to misstate the criterion — refuted because in plain language the threshold is the minimum the partners expected; the description states it correctly as a threshold.
- Sender = the maker: the notification comes from Brackenmere although the criteria were set by the store — refuted because `05-ExceptionCriteria.xml` says "Both sides are told when a criterion is met", and the maker evaluating the store's figures is plausible.
