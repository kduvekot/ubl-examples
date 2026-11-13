# LLM review: 05-ExceptionCriteria.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

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

### furniture/05#F1 · Medium · Sales threshold without a time basis
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ThresholdQuantity` = `5`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:EffectivePeriod/cbc:EndDate` = `2026-08-29`
- Why: Line 1 triggers an exception when sales are less than 5 sets, but does not say over which interval (per week, per four weeks, over the whole effective period of 2026-03-23 to 2026-08-29). Without it the criterion cannot be evaluated, which is its whole purpose. The notification `07-ExceptionNotification.xml` applies it to a four-week period (2026-03-23 to 2026-04-20), and the request `03-ItemInformationRequest.xml` asks for weekly figures, so the flow itself reads the threshold two ways. Line 2 does give a time basis (`TimeDeltaDaysQuantity` 28 days).
- Condition: Line 1 states the interval over which sales are compared with the threshold, and that interval matches the observation period in 07.
- Options: (a, preferred) state the four-week basis (e.g. in the line note, "fewer than 5 sets in four weeks"), matching 07; (b) a weekly threshold, with 07 changed to match.
- Needs decision: no

### furniture/05#F2 · Medium · Line 1 is both an operational and a metric criterion
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- Why: The definition of `SupplyChainActivityTypeCode` here says: "Establishes the criterion for one of the three types of exceptions … Operational, Metric and Forecast Exceptions. This will be set if this Exception is about an Operational Exception." Line 1 also sets `PerformanceMetricTypeCode`, which makes it a metric criterion as well; a criterion line is one of the three types.
- Condition: Each exception criteria line is of one type: operational (activity code), metric (metric code) or forecast (forecast criterion line).
- Options: (a, preferred) keep the operational `SupplyChainActivityTypeCode` SALES, which the note "Slow sales." and the product activity report match; (b) make it a metric criterion and drop the activity code.
- Needs decision: no

### furniture/05#F3 · Medium · Language code in LocaleCode
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExceptionCriteria/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/05#F4 · Low · Own-line item carries the maker's brand
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:SupplyItem/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cac:SupplyItem/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/05#F5 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExceptionCriteria/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- `/ExceptionCriteria/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0570` resolves to `04-TradeItemLocationProfile.xml`; the validity period 2026-03-16 to 2026-08-29 equals its period.
- Line 2: seller forecast (`DataSourceCode` SELLER) compared with the buyer's plan (`ComparisonDataSourceCode` BUYER), more than 30 % (`P1`), over 28 days; consistent with its note.
- Priority HIGH and resolution REVIEW of line 1 are the values 07 reports.

## Considered and refuted
- `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ExceptionStatusCode` = `ACTIVE`: the definition speaks of "status specific to a shipment exception" — refuted as a finding because in an exception criteria line the element can only mean the status of the criterion; the word "shipment" is carried over in the UBL definition.
- `/ExceptionCriteria/cac:ExceptionCriteriaLine[1]/cbc:ThresholdValueComparisonCode` = `LT`: the definition lists EXCEEDS_EXCEPTION_VALUE / FALLS_BELOW_EXCEPTION_VALUE — refuted because the code comes from the world's own list with its listID, and "Less than" has the same meaning.
