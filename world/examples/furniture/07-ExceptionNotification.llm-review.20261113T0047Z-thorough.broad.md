# LLM review: 07-ExceptionNotification.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

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

### furniture/07#F1 · Medium · Line reference meant for the exception criteria points to the activity report
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0572`
- XPath: `/ExceptionNotification/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0571`
- Why: In an exception notification line, `DocumentReference` is defined as "A reference to Exception Criteria document can be provided." `BS-DOC-26-0572` is the Product Activity `06-ProductActivity.xml`; the exception criteria are `BS-DOC-26-0571` (`05-ExceptionCriteria.xml`), referenced only at document level. The line therefore cites a document of another kind in an element meant for the criteria.
- Condition: The line-level `DocumentReference` references the exception criteria (`BS-DOC-26-0571`), or is absent; the product activity is referenced at document level.
- Options: (a, preferred) line reference to `BS-DOC-26-0571`, and the product activity `BS-DOC-26-0572` as a second document-level reference; (b) drop the line reference.
- Needs decision: no

### furniture/07#F2 · Medium · Sales exception carries a forecast exception and a metric code
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ForecastPurposeCode` = `SALES`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:IssueDate` = `2026-03-16`
- Why: `SupplyChainActivityTypeCode` "Establishes the criterion for one of the three types of exceptions: Operational, performance metric and forecast. This reports an exception notification about an operational exception." The line reports criterion line 1 of `05-ExceptionCriteria.xml` (sales below 5 sets: description "Sales below the agreed threshold", compared 5 and source 3 SET), an operational exception. It also sets a metric code and a `ForecastException` ("A forecast accuracy or comparison exception") about a seller sales forecast issued on 2026-03-16, compared with actual sales. That forecast exception matches neither criterion: line 2 of 05 compares the seller's forecast with the buyer's plan (`ComparisonDataSourceCode` BUYER, threshold 30 %), and no forecast figures appear anywhere in the line.
- Condition: The notification line is of one exception type, matching the criterion line it reports; a forecast exception appears only when a forecast criterion was met and its figures are given.
- Options: (a, preferred) remove `ForecastException` and `PerformanceMetricTypeCode`, keeping the operational sales exception; (b) report a forecast exception in a separate line against criterion line 2, with its forecast and comparison values.
- Needs decision: no

### furniture/07#F3 · Medium · ComparisonDataCode holds a kind of data, not a partner
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonDataCode` = `ACTUAL`
- Why: `ComparisonDataCode` is defined as "A code signifying the partner providing the information in this forecast exception". `ACTUAL` ("Actual sales") says what kind of data was compared, not which partner provided it (the partner list used elsewhere is `DataSourceCode`, with BUYER/SELLER).
- Condition: `ComparisonDataCode`, where present, names the partner providing the comparison information (e.g. BUYER), from a list of partners.
- Options: (a, preferred) disappears with the forecast exception (previous finding); (b) if kept, `BUYER` from the data-source list, since the actual sales came from the store.
- Needs decision: no

### furniture/07#F4 · Medium · Language code in LocaleCode
- XPath: `/ExceptionNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/07#F5 · Low · Comparison issue time does not match the activity report
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonForecastIssueDate` = `2026-04-20`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonForecastIssueTime` = `18:00:00`
- XPath: `06-ProductActivity.xml:/ProductActivity/cbc:IssueTime` = `16:35:00`
- Why: The comparison data are the actual sales (`ComparisonDataCode` ACTUAL) of 2026-04-20, i.e. the product activity report `06-ProductActivity.xml`, issued 2026-04-20 at 16:35. The forecast exception gives 18:00 as the issue time of the comparison. If the forecast exception stays, the times disagree.
- Condition: If a comparison issue date and time are given, they are those of the document the comparison data come from.
- Options: (a, preferred) resolved by removing the forecast exception; (b) 16:35:00.
- Needs decision: no

### furniture/07#F6 · Low · Compared and source values may be swapped
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:ComparedValueMeasure` = `5`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:SourceValueMeasure` = `3`
- Why: `SourceValueMeasure` is "The value used as the basis of comparison" and `ComparedValueMeasure` "The value that was compared with the source value that resulted in the exception". The basis of comparison is the threshold (5 sets); the value compared with it and resulting in the exception is the observed sales (3 sets). The example has them the other way round. The UBL definitions are terse enough that the opposite reading (source = observed data) is possible, so this needs a decision.
- Condition: `SourceValueMeasure` holds the basis of comparison and `ComparedValueMeasure` the value compared with it, under one documented reading, with `VarianceQuantity` consistent with it.
- Options: (a, preferred) source 5 SET (threshold), compared 3 SET (observed), variance −2; (b) keep as is, recording the reading that source means the observed data.
- Needs decision: yes

### furniture/07#F7 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:VarianceQuantity` = `-2`: 3 − 5 = −2 SET.
- Observation periods (document and line) 2026-03-23 to 2026-04-20 equal the activity period of `06-ProductActivity.xml`; issued the day after it.
- Priority HIGH and resolution REVIEW match line 1 of `05-ExceptionCriteria.xml`; 3 sets is less than the threshold 5, so the criterion is met.
- `/ExceptionNotification/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0571` resolves to the criteria; `11-OrderCancellation.xml` and `12-InstructionForReturns.xml` reference this notification.
