# LLM review: 06-ForwardingInstructions.xml

Flow: medicines (QLM-TX-26-3980) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/06-ForwardingInstructions.xml`, Git blob `8b40a60b37a0d339848eedadace2f9a7a335e0b3` (committed)
- Last commit changing the example: d34fe695 2026-11-21 O277 (3): UBL's spelling "despatch" for UBL concepts, and a published-text rule for it
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### medicines/06#F1 · Medium · The dry ice is not declared as dangerous goods in the forwarding instructions
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cbc:HandlingInstructions` = `Frozen vaccine on 6 kg of dry ice: keep the box upright and its vent clear; do not put it in the active container.`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cbc:HazardousRiskIndicator` = `true`
- Why: 6 kg of dry ice is UN 1845, class 9, packing instruction 954, which must be declared for carriage by air (own knowledge of the ICAO Technical Instructions / IATA DGR). The forwarding instructions mark the box as hazardous but declare only the generator as a hazardous goods item; the forwarder has to book the dry ice with the airline, and the air waybill does declare it as a goods item of its own (`11-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem[5]/cac:Item/cac:HazardousItem/cbc:UNDGCode` = `1845`). The instructions the forwarder works from are therefore incomplete against the waybill it produces.
- Condition: the forwarding instructions declare the dry ice (UN 1845, net quantity 6 kg) as they declare the generator, consistent with the waybill.
- Options: (a, preferred) a fifth goods item for the dry ice with its hazardous item, as in the waybill; (b) a hazardous item on the dry-ice box's handling unit.
- Needs decision: no

### medicines/06#F2 · Low · 3.5 kg of packaging for fourteen cartons and an insulated dry-ice box
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:GrossWeightMeasure` = `101.1`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cbc:GrossWeightMeasure` = `60`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cbc:GrossWeightMeasure` = `12`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[3]/cbc:GrossWeightMeasure` = `1.6`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[4]/cbc:GrossWeightMeasure` = `18`
- Why: the goods items weigh 60 + 12 + 1.6 + 18 = 91.6 kg; with 6 kg of dry ice that leaves 101.1 − 97.6 = 3.5 kg for fourteen shipping cartons and the insulated box holding the dry ice. A polystyrene shipper for 6 kg of dry ice alone weighs some 2 to 4 kg, and fourteen cartons several hundred grams each (own estimate), so the total is low, though not impossible.
- Condition: the consignment's gross weight covers the goods, the dry ice and a plausible weight of cartons and insulated packaging.
- Options: (a, preferred) a consignment gross weight a few kilograms higher, kept equal in the waybill and the despatch advice; (b) confirm light packaging.
- Needs decision: no

### medicines/06#F3 · Low · The unit for the active container is typed as a carton
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:TransportHandlingUnitTypeCode` = `CT`
- Why: the first handling unit holds the fourteen cartons (`Package[1]` to `Package[14]`, each typed carton) that go into "the airline's active container at 5 °C" (`/ForwardingInstructions/cbc:Note`); in the waybill that unit is the active container `RKN20871K0` (`11-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`). A carton holding fourteen cartons is not what the consignor hands over.
- Condition: the handling unit's type is what the consignor actually hands over (fourteen loose cartons, or the container it asks to be collected).
- Options: (a, preferred) leave out the type code of the unit (the airline's container is assigned by the carrier) or give each carton as its own handling unit; (b) a type for a temperature-controlled container.
- Needs decision: no

## Checked and consistent
- Packages: ten cartons of 30 and four of 60 = 300 influenza packs + 240 insulin vials, as in goods items 1 and 2 and in `04-Order.xml`; one dry-ice box of 40 varicella doses; one radioactive package.
- Radioactive material: Mo-99, half-life 65.9 h (own knowledge); 20 GBq at 21 June 12:00 UTC gives 20 × 2^(150 h / 65.9 h) ≈ 97 GBq at about 06:00 UTC on 15 June, matching the stated maximum; far below the Type A limit A2 = 0.6 TBq for Mo-99; transport index 1.5 (> 1) and surface dose rate 0.30 mSv/h fit Category III-YELLOW; UN 2915, ERG 163, class 7 (own knowledge of the IAEA SSR-6 and ICAO rules).
- Package 400 × 300 × 300 mm and 18 kg fit a shielded Mo-99/Tc-99m generator.
- References: `DocumentReference[1]` resolves to `04-Order.xml`; the dangerous goods declaration `QLM-DGD-26-0615` is an external document, typed 890, also cited in `11-Waybill.xml`.
- The shipment and consignment IDs are those of `09-DespatchAdvice.xml` and `11-Waybill.xml`; flight KXL207 of Monday 15 June matches the waybill.
