# LLM review: 01-Order.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/01-Order.xml`, Git blob `888e6ba193f9e99d9a10149a112547e954b6d115` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### road/01#F1 · High · Emission factor × base does not give the emission value
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". A factor of 0.82 per 1 EA (one bench) gives 0.82 kg CO2e per bench, not the 96 kg stated in ValueMeasure. No other reading fits either: 96 / 0.82 = 117.1, which is neither the bench count, nor the materials of the bench (34 kg steel + 22.5 kg hardwood = 56.5 kg in the CircularityProfile), nor the bench weight implied by the transport documents (about 38 kg). The same three values occur in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`, all with ValueMeasure 96 KGM), 9 of them in this flow.
- Condition: ValueFactorNumeric × (activity quantity / ValueBaseMeasure) equals ValueMeasure, with the activity quantity and the factor's unit evident from the element values; or the factor and base are absent.
- Options: (a) preferred: give the factor and base the activity they really relate to (e.g. a factor per kg of steel with the base in KGM, the value then the product), so the calculation can be redone; (b) drop ValueFactorNumeric and ValueBaseMeasure and keep only the total, if no factor has a real basis.
- Needs decision: no

### road/01#F2 · Low · Maximum delivery unit smaller than the single delivery ordered
- XPath: `/Order/cac:Delivery/cbc:Quantity` = `108`
- XPath: `/Order/cac:Delivery/cbc:MinimumQuantity` = `108`
- XPath: `/Order/cac:Delivery/cbc:MaximumQuantity` = `108`
- XPath: `/Order/cac:Delivery/cac:MaximumDeliveryUnit/cbc:BatchQuantity` = `100`
- XPath: `/Order/cac:Delivery/cac:MinimumDeliveryUnit/cbc:BatchQuantity` = `4`
- Why: The order asks for exactly 108 items in this one delivery (minimum = maximum = quantity), yet sets the maximum delivery unit ("the quantity of ordered Items that constitutes a batch for delivery purposes") at 100. Nothing in the flow gives 100 a meaning: the goods travel as one full truck of 25 pallets (24 × 4 benches and one pallet of 12 side frames, `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:TotalTransportHandlingUnitQuantity` = `25`). The minimum of 4 matches the 4 benches per pallet; 100 matches nothing and can be read as forbidding the 108-item delivery that is ordered.
- Condition: the maximum delivery unit is either absent or a batch size that the ordered delivery of 108 items respects and that has a reason in the flow.
- Options: (a) preferred: remove MaximumDeliveryUnit (no real case); (b) set it to a batch the story uses (e.g. a full pallet load, if one is defined).
- Needs decision: no

## Checked and consistent
- Delivery quantity 108 = order lines 96 + 12; both lines are multiples of the minimum batch of 4 (96/4 = 24 pallets, 12/4 = 3).
- RequestedDespatchDate/Time 2026-03-23 14:00 lies within RequestedDespatchPeriod 13:00–17:00 and matches the requested pickup in `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceTime` = `14:00:00`.
- Despatch instruction "Have the export declaration ready when the truck arrives" fits FCA (seller clears export); the export declaration `05-ExportCustomsDeclaration.xml` is issued 2026-03-23 13:25, before the pickup.
- The carrier named in Despatch/CarrierParty (Trasvia Haulage, XU-R-104822) is the one the buyer books in `03-TransportExecutionPlanRequest.xml` and who issues the waybill; DespatchParty Castrano Logistics is the 3PL who despatches in `04-DespatchAdvice.xml`.
- Item dimensions 1800 × 620 × 780 mm and resource consumption (34 kg steel, 22.5 kg hardwood) are the same as in the despatch advice and customs documents.
- Check digits: GLN 9520610900008 passes (check_ids.py).

## Considered and refuted
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description`: FCA named place given only as text, without a LOCODE or address, while the pickup place is identified elsewhere (XUFER) — refuted because the text names the place unambiguously and the full despatch address is in the same Delivery (`/Order/cac:Delivery/cac:Despatch/cac:DespatchAddress`); an identifier would add nothing the order needs.
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty`: an order naming the buyer's carrier one day before the transport request is sent (`03-TransportExecutionPlanRequest.xml`, issued 2026-03-17) — refuted because under FCA the buyer chooses the carrier and the request is sent under an existing framework contract (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `LD-TH-FW-2026`).
