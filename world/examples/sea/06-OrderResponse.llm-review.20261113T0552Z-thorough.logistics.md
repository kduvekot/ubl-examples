# LLM review: 06-OrderResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/06-OrderResponse.xml`, Git blob `8c32d38abff802a363b6a976f771dad7ef600e7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit b532c38 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/06#F1 · Medium · Gross and net weight do not follow their definitions in the order response
- XPath: `/OrderResponse/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/OrderResponse/cbc:NetWeightMeasure` = `3762`
- Why: UBL defines the order response's `GrossWeightMeasure` as "The total gross weight for the Order Response (goods + packaging + transport equipment)" and `NetWeightMeasure` as "The total net weight for the Order Response (goods + packaging)". The values are those of the packing list, where 4,106.4 kg is goods plus packaging (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`, the sum of the goods items' gross weights 3,984 + 122.4) and 3,762 kg is the net weight "excluding packaging" (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:NetWeightMeasure` = `3762`). Under the order response's definitions, 4,106.4 kg is the net weight, and the gross weight would include the container's tare (3,750 kg, giving 7,856.4 kg, `10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`). The semantic-conformance rule requires the UBL definition even where practice reads "net" as goods only.
- Condition: each weight in the order response is the quantity its definition names, or is left out.
- Options: net 4,106.4 kg and either no gross weight or a gross weight with the transport equipment the seller already plans (one 40-foot container) (preferred: the seller confirms an FCL shipment, so the box is known in kind); or drop both weights, which the order response does not need for the confirmation (the packing list carries them).
- Needs decision: no

## Checked and consistent
- `/OrderResponse/cbc:GrossVolumeMeasure` = `41.5` ("including packaging") is consistent with the packing list's net volume of 38.9 m³ "excluding packaging": the difference of 2.6 m³ for 25 pallets is about 0.1 m³ per pallet, which for a pallet about 1.85 m long (the bench length) means a low skid of about 0.65 × 0.09 m in section (own estimate); light, but possible for film-wrapped benches on skids.
- Physics: 41.5 m³ in one 40-foot general-purpose box (inside about 12.03 × 2.35 × 2.39 m ≈ 67.7 m³, own knowledge) fills about 61 %; 7,856 kg gross is far below the 30,480 kg maximum gross of a 42G1 box.
- The order reference `VT-PO-26-0127` resolves to `05-Order.xml`; quantities 96 and 12, prices and line IDs agree with it. The contract `LD-DAG-26-0125` resolves to `03-DigitalAgreement.xml`.
- The delivery terms place is identified as `XLSEL`, the same LOCODE as in the bill of lading and the invoice.

## Considered and refuted
- `/OrderResponse/cbc:TotalPackagesQuantity` = `108`: suspected as a count of items (96 benches + 12 frames) where the shipment travels on 25 pallets — refuted because the bill of lading counts the same 108 packages (24 pallets with `TotalPackageQuantity` 4 each, the frames pallet with 12, `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TotalPackageQuantity` = `12`); film-wrapped benches are packages. Whether the 12 frames are 12 packages or one box is a question of the bill of lading (see its review).
- `/OrderResponse/cac:OriginatorDocumentReference/cbc:ID` = `PS-REQ-26-0031`: resolves to no example and the order did not carry it — refuted as a problem: the element names the kind of reference (the originator's request, Port of Selanu being the originator customer in `05-Order.xml`), and a requisition outside the flow is legitimate.

## Outside this review
- The promised delivery period ends 2026-05-18 (`/OrderResponse/cac:OrderLine[1]/cac:LineItem/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-05-18`), while the goods reach the warehouse on 2026-05-19 (bill of lading on-carriage events) and are received on 2026-05-21 (`21-ReceiptAdvice.xml`). Under CIF the seller's delivery is the loading at Lumeport on 2026-05-14, inside the period; whether the period means delivery at the warehouse is a timeline question across documents.
