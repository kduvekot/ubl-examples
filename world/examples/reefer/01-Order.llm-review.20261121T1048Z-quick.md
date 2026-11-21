# LLM review: 01-Order.xml

Flow: reefer (26-0214) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/01-Order.xml`, Git blob `8d635db83f22781844f7cf54142a4094f745406b` (committed)
- Last commit changing the example: 2a048333 2026-11-20 Read-throughs of 2026-11-20: mechanical fixes in tender, contest, medicines, lpg, ore, rail, energy, utilities, reefer, waste, plastics, mast, air, packaging; owner decisions on the tender lead time, the plastics customs value, the air transit and O269
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

## Checked and consistent
- Line arithmetic: 672 × 26 = 17,472.00; 224 × 24.5 = 5,488.00; 224 × 27 = 6,048.00; sum 29,008.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `29008.00` = taxable amount; tax 0.00 at category G with the export exemption.
- Quantities are whole pallets of 56 cartons (12 + 4 + 4 = 20 pallets), the pallet size used in `06-DespatchAdvice.xml` and `07-BillOfLading.xml`; 20 pallets fit a 40-foot reefer.
- GS1 keys (GLN, three GTINs) pass their check digits; the 952 prefix is GS1's range for demonstrations.
- The note's "sailing of 23 April" matches the estimated departure in `05-ExportCustomsDeclaration.xml` (2026-04-23, a Thursday).

## Considered and refuted
- `/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-04-26`: a Sunday, while the buyer's contact note says `Monday to Saturday 05:00–14:00` — refuted because the delivery terms are CIP with the place `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:ID` = `XLSEL` (the port of Selanu), and the reefer does arrive at the port on 26 April (`10-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-26`); the cold store receives it on Monday 27 April.
- `/Order/cac:DeliveryTerms/cbc:ID` = `CIP`: CIF would be the sea term — refuted: for containerised goods handed over before loading, Incoterms 2020 recommends CIP/CPT rather than CIF (own knowledge).
