# LLM review: 01-Order.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/01-Order.xml`, Git blob `1c959f7204add325b43b103744bcf375fb8ba1db` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/01#F1 · Low · The order asks for no delivery date or period
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Rivermouth Packaging`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `River quay, Lumeport`
- Why: The order's only `Delivery` names the party that receives the goods, but carries no `RequestedDeliveryPeriod` (or `PromisedDeliveryPeriod`) and no `DeliveryLocation`; the place appears only as a free-text description under the CPT terms. Yet the transport documents of the flow work to a firm window: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-04-22`, and the waybill even states a "latest date of delivery allowed by the buyer", `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:Delivery/cbc:LatestDeliveryDate` = `2026-04-23`, which nothing from the buyer supports. Nothing may be implied by absence (IND5/IND6), so the buyer's delivery wish is not stated anywhere.
- Condition: The order states when the buyer wants the 120 t delivered (a requested delivery period), consistent with the transport window of 03/04 and the waybill's latest delivery date; or the waybill's "allowed by the buyer" date is removed (see the waybill review).
- Options: (a) preferred: add `cac:Delivery/cac:RequestedDeliveryPeriod` with an end date of 2026-04-23 (matches the waybill, after the plan's 2026-04-22), because the order is where the buyer states it; (b) leave the order as it is and drop the waybill's latest delivery date.
- Needs decision: no

## Checked and consistent
- `OrderLine` quantity × price: 120 TNE × 83200 XUF per 1 TNE = 9984000 XUF = `LineExtensionAmount` = `AnticipatedMonetaryTotal/PayableAmount`.
- Item physics: density 0.92 g/cm³ fits HS 390110 ("specific gravity of less than 0.94"); a 1 t jumbo bag of PE granulate at a bulk density of about 0.55–0.6 t/m³ (own knowledge) holds about 1.7–1.8 m³, a normal size for a jumbo bag.
- The order ID `RP-PO-26-0882` is referenced by 02, 05, 06, 08 and 10, and all resolve to this order; order line 1 is the line referenced in 06 and 08.

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID` = `CPT`: suspected a mismatch with a seller-booked barge — refuted because under CPT the seller contracts and pays the carriage to the named place, which is exactly what 03/04 (Rinova as transport user and bill-to party) and 07 (freight invoiced to Rinova) show.
