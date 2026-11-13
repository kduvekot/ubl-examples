# LLM review: 15-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/15-Order.xml`, Git blob `c87a13cb9349700b274d702bf91f928dddf95d64` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
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

### furniture/15#F1 · Low · Desks and installation ordered without a delivery date or an identified delivery place
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Lumeport Public Works Department, Civic Square`
- Why: The order's `Delivery` names only the receiving party, with no `DeliveryLocation`, `DeliveryAddress` or requested delivery period. The place is free text under the delivery terms, although the department's address is registered (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`, Civic Square 6) and the postal address given is that of the procurement office (room 2.14), not of the new office to be furnished. For an order that includes on-site installation by two installers, the date matters: the work was done on 2026-04-08 and 2026-04-09 (`16-WorkReport.xml:/WorkReport/cac:ReportedPeriod/cbc:StartDate` = `2026-04-08`), which nothing in the order requests.
- Condition: the order states where the desks are to be delivered and installed (address or location of the new office) and a requested delivery or installation period.
- Options: (preferred) add `Delivery/DeliveryAddress` (Civic Square 6, with the office's floor or room if different from the procurement office) and a `RequestedDeliveryPeriod` of 2026-04-08 to 2026-04-09; or add a `DeliveryLocation` with the address register ID and a note on the agreed date.
- Needs decision: no

## Checked and consistent
- Quantities and arithmetic: 6 desks × 880 = 5280.00; 14 h × 48 = 672.00; total 5952.00. 14 hours for six desks is about 2 h 20 min of installer time per desk (two installers, seven hours each, as in `16-WorkReport.xml` and `17-Invoice.xml`), plausible for assembling and placing a hardwood desk (own estimate: 1.5 to 3 h).
- Item: dimensions 1600 × 800 × 740 mm agree with the description ("1600 × 800 mm") and with a standard office desk height (720 to 750 mm, own knowledge). HS 940330 and CPC 38122 fit wooden office furniture. GTIN 9523710000029 and the seller's GLN pass the check digit.
- Units: EA for desks, HUR for hours; BaseQuantity units match the line quantities.
- Dates: order 2026-04-01 precedes the work (2026-04-08) by a week, more than the maker's lead time of 5 days stated for the garden line in `04-TradeItemLocationProfile.xml`.
