# LLM review: 06-ProductActivity.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/06-ProductActivity.xml`, Git blob `b8bd3b68d78e4195bf7df8c905e21d85b0c22321` (committed)
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

### furniture/06#F1 · Low · One four-week figure where weekly figures were requested
- XPath: `/ProductActivity/cac:ActivityPeriod/cbc:StartDate` = `2026-03-23`
- XPath: `/ProductActivity/cac:ActivityPeriod/cbc:EndDate` = `2026-04-20`
- XPath: `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityPeriod/cbc:EndDate` = `2026-04-20`
- Why: The report answers the maker's request (`/ProductActivity/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0569`, i.e. `03-ItemInformationRequest.xml`), which asked for weekly figures (`03-ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cbc:TimeFrequencyCode` = `WEEKLY`; note "Weekly figures, please"). The report gives one sales line for the whole span from Monday 2026-03-23 to Monday 2026-04-20. That span is 29 days counted inclusively (calculated), i.e. four Monday-to-Sunday weeks plus the Monday of the fifth week, which is also the issue day, so the last day is only partly covered at 16:35. The note "Rain three weeks out of four" shows the store itself counts four weeks.
- Condition: the report either gives the sales per week requested (one activity line or period per week) or the request and the report agree on a four-week figure; the period ends on the last day it fully covers.
- Options: (preferred) end the period on Sunday 2026-04-19 and keep one four-week figure, while changing the request to a four-weekly frequency, because the exception criterion and notification also work on four weeks; or split the line into four weekly lines whose quantities add up to 3 sets.
- Needs decision: no

## Checked and consistent
- Stock (calculated from the flow): 20 sets delivered before 2026-03-22 (`09-Invoice.xml`, 20 sets invoiced), 3 sold in the period → at most 17 sets on hand on 2026-04-20. This is the basis of the stock finding in `10-Order.xml` and agrees with the return of 6 sets in `12-InstructionForReturns.xml` (17 − 6 = 11, close to the target inventory of 10 in `04-TradeItemLocationProfile.xml`).
- Location: the origin GLN 9522610900026 (check digit passes) is the store's garden department, the same GLN and meaning as in `retail/22-Order.xml`; it differs, rightly, from the goods-in GLN 9522610900019 used for deliveries.
- The period and the quantity (3 sets) are those `07-ExceptionNotification.xml` reports; the report precedes the notification (2026-04-20 16:35 before 2026-04-21 17:49).
- Codes: SALES and SET resolve; item identification matches the flow.

## Considered and refuted
- `/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityFinalLocation/cbc:Name`: suspected a non-location ("Customers' gardens") in a location — refuted because for sales the location "to which the goods are moved" is the consumers' premises, which a store can only describe in general terms.
- `/ProductActivity/cbc:Note`: suspected an unexplained promotion — refuted because the note gives context for slow sales and no other value depends on it.
