# LLM review: 10-PackingList.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/10-PackingList.xml`, Git blob `aef1ab21426bbd03022aba54b057f406aeb46b61` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/10#F1 · High · Emission factor times base does not give the emission value
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: as in the catalogue: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" on the base `ValueBaseMeasure`; 0.82 × 1 EA = 0.82, not 96 kg CO2e. Same triple in 39 XML examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>' world/examples`).
- Condition: factor × base = value, or factor and base are absent.
- Options: drop factor and base (preferred); or a factor on a base whose product is 96.
- Needs decision: no

### sea/10#F2 · Medium · The packing list does not say how the goods are packed
- XPath: `/PackingList/cbc:Note` = `25 pallets.`
- XPath: `/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `25`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4120872`
- Why: a Packing List is "A document describing how goods are packed". This one has a single transport handling unit, the container, and no pallet, package or handling-unit structure: the 25 pallets exist only as a note and a count, and nothing says which goods are on which pallet, how many benches per pallet, or the pallets' marks, SSCCs, weights or dimensions. The bill of lading, issued two days later by the carrier, has exactly this information (24 bench pallets with 4 each and SSCCs `095206101230000018` … `095206101230000247`, one frames pallet `095206101230000254`, shipping marks `VELUMI SELANU / 001 of 025` …), which a carrier would take from the shipper's packing list. The count of 25 handling units also does not match the one `TransportHandlingUnit` the shipment contains.
- Condition: the packing list describes the 25 pallets (or the handling units it counts) with their contents, and the count agrees with the units it lists.
- Options: list the 25 pallets as packaged handling units of the container, with SSCC, marks, goods item and package count, as on the bill of lading (preferred: the packing list is the source of that data); or at least give per goods item the number and kind of packages.
- Needs decision: no

### sea/10#F3 · Medium · Shipment gross weight excludes the transport equipment its definition includes
- XPath: `/PackingList/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The document itself states the container's gross weight of 7,856.4 kg (= 4,106.4 + tare 3,750), so the shipment's gross weight under its definition is 7,856.4 kg; 4,106.4 kg is goods plus packaging (the goods items' gross weights 3,984 + 122.4). The same value is in five other examples of the flow.
- Condition: the shipment's gross weight includes the transport equipment, or the goods-and-packaging weight is carried only where its definition fits (goods items).
- Options: 7,856.4 kg as the shipment's gross weight (preferred: the box is known in this document); or drop it and rely on the goods items' gross weights and the container's gross weight.
- Needs decision: no

### sea/10#F4 · Low · Document reference to the order without saying it is the order
- XPath: `/PackingList/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: a plain `DocumentReference` with only an ID; the carrier and forwarder receiving the packing list cannot tell that it is the buyer's purchase order (`05-Order.xml`).
- Condition: the reference states its document type.
- Options: add `DocumentTypeCode` `220` (Order) (preferred).
- Needs decision: no

## Checked and consistent
- Weights (calculated): goods items 3,984 + 122.4 = 4,106.4 kg; plus tare 3,750 kg = 7,856.4 kg, the container's gross weight here and the verified gross mass on the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:VerifiedGrossMass/cbc:GrossMassMeasure` = `7856.4`). Gross minus net = 344.4 kg of packaging for 25 pallets (about 14 kg each, a light skid plus film).
- Per unit: 3,984 kg / 96 benches = 41.5 kg gross per bench (166 kg per pallet of 4); 122.4 kg / 12 = 10.2 kg per side frame. Net 3,762 kg leaves about 38 kg per bench if a frame weighs about 9.5 kg net, plausible for a cast-steel bench with hardwood slats (own estimate).
- Tare 3,750 kg is typical for a 40-foot general-purpose box (about 3,700–3,900 kg, own knowledge); `check_ids.py`: ISO 6346 check digit of `TWLU4120872` valid.
- Volume: 38.9 m³ net (41.5 m³ with packaging in the order response) against about 67.7 m³ inside a 40-foot box: fits by volume.
- Shipment `LD-SH-26-0132` and consignment `LD-CS-26-0133` match the forwarding instructions, export declaration and bill of lading; the declared values 49,920 and 768 XBL match the order lines.

## Considered and refuted
- Floor space of 25 pallets in a 40-foot box: with pallets as long as a bench (about 1.85 m) a single tier fits only 18 (3 across × 6 along in 12.03 × 2.35 m), so 25 pallets need two tiers. Gross volume per pallet is 41.5 / 25 ≈ 1.66 m³; with a footprint of about 1.85 × 0.77 m the pallet is about 1.17 m high, and two tiers (2.34 m) fit under the inside height of about 2.39 m. Refuted: the load fits, though tightly, if benches are nested on narrow pallets; the documents give no pallet dimensions that would prove otherwise.
- Net weight per bench (about 38 kg) against the catalogue's material input of 56.5 kg (34 kg steel, 22.5 kg hardwood): refuted, the input is "consumed" material including casting and sawing losses (see the catalogue's review).
