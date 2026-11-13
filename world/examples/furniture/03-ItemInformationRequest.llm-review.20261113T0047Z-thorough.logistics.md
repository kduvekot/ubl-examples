# LLM review: 03-ItemInformationRequest.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/03-ItemInformationRequest.xml`, Git blob `831fa39b706e496e223832845d95a8ebe56ea67b` (committed)
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

### furniture/03#F1 · Medium · One request line asks for activity, forecast and metric data at once
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:ForecastTypeCode` = `TOTAL`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- Why: UBL defines `ForecastTypeCode` on this line with the condition "The information request can be either about supply chain activity or about forecasts or about performance metrics, so it will be optional". The line sets all three, so it does not say which kind of information is requested. The answer in the flow is a Product Activity report of sales (`06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cbc:SupplyChainActivityTypeCode` = `SALES`), i.e. activity data; no forecast and no performance history is sent.
- Condition: each request line asks for one kind of information (activity, forecast or metric); a second kind, if wanted, is a line of its own.
- Options: (preferred) keep only `SupplyChainActivityTypeCode` = SALES, which is what `06-ProductActivity.xml` answers; or split into separate lines if the maker also wants a forecast or a sales-in-units metric, and then let the flow answer them.
- Needs decision: no

### furniture/03#F2 · Low · "For the whole season" against a request period of eight weeks
- XPath: `/ItemInformationRequest/cbc:Note` = `Weekly figures, please, for the whole season.`
- XPath: `/ItemInformationRequest/cac:Period/cbc:EndDate` = `2026-05-11`
- XPath: `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:Period/cbc:EndDate` = `2026-05-11`
- Why: The note asks for figures for the whole season, but the period runs from Monday 2026-03-16 to Monday 2026-05-11. The season of the item in this flow runs to 2026-08-29 (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:Period/cbc:EndDate` = `2026-08-29`, and the same end date in `05-ExceptionCriteria.xml:/ExceptionCriteria/cac:ValidityPeriod/cbc:EndDate`). Moreover, with weekly figures from a Monday, eight full weeks end on Sunday 2026-05-10; the end date 2026-05-11 adds one day of a ninth week (calculated: 2026-03-16 + 56 days = 2026-05-11).
- Condition: the note and the period describe the same span, and the period ends on a week boundary if weekly figures are requested.
- Options: (preferred) extend the period to the season's end (2026-08-29 or the last Sunday before it) so that it matches the note and the replenishment profile; or keep eight weeks, end them on 2026-05-10 and drop "for the whole season".
- Needs decision: no

## Checked and consistent
- Reference: `/ItemInformationRequest/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0568` resolves to `02-Quotation.xml`; item and parties agree.
- Direction: the seller (Brackenmere) is the sender and requests the information from the buyer (Brightmarket), as the definitions of `BuyerCustomerParty` and `SellerSupplierParty` in this document say.
- The request (2026-03-12) precedes the period start 2026-03-16, the day of the first order (`08-Order.xml`).
- Codes: WEEKLY, SALES, SET resolve in their lists; GS1 check digits pass.

## Considered and refuted
- `/ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cbc:Quantity`: suspected a quantity without meaning in a request — refuted because the definition is "The quantity the given information are related to", and 20 sets is the quantity of the season's order.
