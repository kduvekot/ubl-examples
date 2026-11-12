# LLM review: 01-Order.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/01-Order.xml`, Git blob `b65397fa0c7cc5caf77d2e114d9eb2db2610109c` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/01#F1 · High · Emission factor × base quantity does not give the stated emission
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines ValueFactorNumeric as "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure as "the base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a base of 1 EA (one bench) the factor gives 0.82 × 1 = 0.82 kg CO2e per bench, while ValueMeasure states 96 kg. No other quantity in the element is one the factor could apply to (96 / 0.82 ≈ 117, which matches nothing in the item: steel 34 kg + hardwood 22.5 kg = 56.5 kg consumed). The same triple 96 / 0.82 / 1 EA is in 39 examples (counted with `grep -rc --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'` and the neighbouring ValueMeasure/ValueBaseMeasure lines), in this flow also in `06-TransitCustomsDeclaration.xml` and `11-Invoice.xml`.
- Condition: ValueFactorNumeric × ValueBaseMeasure equals ValueMeasure (in the units given), or ValueFactorNumeric and ValueBaseMeasure are absent.
- Options: (a) preferred: remove ValueFactorNumeric and ValueBaseMeasure, since 96 kg per bench is already a per-unit value and the factor adds nothing; (b) state the factor per kilogram of material with a base in KGM, so that factor × mass = 96; (c) if 0.82 is meant as something else (an allocation share), it does not belong in ValueFactorNumeric.
- Needs decision: no

### rail/01#F2 · Low · Delivery place described only in text, and no requested delivery date
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Rail siding of Lumeway Distribution, Marrowdale`
- XPath: `/Order/cac:Delivery`
- Why: The same siding is identified by a GLN in the waybill (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9520610900015`) and by the UN/LOCODE of Marrowdale (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:UnloadingLocation/cbc:ID` = `XBMRW`). The order's Delivery carries only the delivery party, no requested period or location, although the seller's transport request asks for delivery on a specific day (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-16`), which must come from the buyer's order. The checklist asks for identifiers where the same place is identified elsewhere.
- Condition: The delivery location of the order carries the GLN (and/or LOCODE) used for the same siding in the waybill, and the order says when delivery is requested, or the absence of a date is explained by the story.
- Options: (a) preferred: add `cbc:ID` with schemeID GS1 GLN to the delivery location and a `cac:RequestedDeliveryPeriod` in `cac:Delivery`; (b) move the location into `cac:Delivery/cac:DeliveryLocation` and keep DeliveryTerms for the Incoterms rule only.
- Needs decision: no

## Checked and consistent
- Check digits: GLN 9520610900008 (check_ids.py OK); ISIN in the seller's legal entity OK. The GLN prefix 952 is GS1's prefix for demonstration numbers, so it cannot be mistaken for a real GLN.
- Quantities and references: 192 EA here = 192 EA in `11-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `192` and in `06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `192`, and "192 park benches" in the consignment summaries of 02, 03 and 08. The invoice's OrderReference resolves to this order (LD-PO-26-0325).
- Delivery terms DAP at the Lumeway siding in Marrowdale agree with the waybill's delivery location name and the invoice note "Delivered at place: the price includes the carriage to the siding."
- Physics, per bench: materials consumed 34 kg steel + 22.5 kg hardwood = 56.5 kg; consignment gross 7968 kg / 192 = 41.5 kg per bench including packaging (02, 03, 06). Material consumed exceeding the product mass by about 15 kg (27 %) is plausible for casting and sawing losses, so the figures do not contradict each other. Load capacity 450 kg over three seats (150 kg per seat) is plausible for a park bench.
- Dimensions 1800 × 620 × 780 mm, seat height 450 mm within 440–460 mm: internally consistent.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`: does not resolve to an example (flow_index `-> ?`) — refuted as a broken reference because it is the seller's data sheet, a document the flow does not model and the reference names it unambiguously; the same applies to `VI-LCA-2025` and `VI-RM-B180`.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteMeasure` = `0.4`: stretch film and pallet straps of 0.4 kg per bench suggested palletised benches, which might contradict the container fill in the waybill — refuted here, because the order says nothing about packaging for transport; the container-fill question is raised in the waybill review (rail/08).
