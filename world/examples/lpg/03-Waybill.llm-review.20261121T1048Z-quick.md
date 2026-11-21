# LLM review: 03-Waybill.xml

Flow: lpg (9900034654) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/lpg/03-Waybill.xml`, Git blob `d672ccec3670612464073835305460574a2b9f47` (committed)
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

### lpg/03#F1 · Low · The consignee's contact is customer service, not the plant that receives the propane
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: a consignee's contact receives the goods. This waybill itself says that "the water company's operator reads the storage level before and after and signs the note" (`/Waybill/cbc:OtherInstruction`); the driver needs the plant, not the company's customer service for its water customers.
- Condition: the consignee's contact is the receiving function at the district heating plant, or there is none.
- Options: (a, preferred) the plant's operations contact (the operator named in the instruction); (b) leave out the contact.
- Needs decision: no

### lpg/03#F2 · Low · Gullhaven telephone prefix "38522" overlaps Lumeport's "38"
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Telephone` = `+999 2 38522 41906`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Telephone` = `+999 2 38522 68330`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Telephone` = `+999 2 38 9310 7518`
- Why: as in `01-Order.xml` (lpg/01#F2): two Gullhaven companies (postal zone 90540) have numbers beginning with `38522`, the Lumeport consignee one beginning with `38` and eight digits; the codes are not prefix-free.
- Condition: one prefix-free numbering plan for Gullhaven and Lumeport.
- Options: as lpg/01#F2.
- Needs decision: yes

## Checked and consistent
- Weights: vehicle loaded 37180 KGM − empty 17000 KGM = 20180 KGM = consignment gross weight = hazardous item net weight = goods item 20.18 TNE; shipment gross weight 29880 KGM = 20180 + tank tare 9700 KGM (UBL: goods plus packaging plus transport equipment); tractor ≈ 17000 − 9700 = 7300 kg, plausible for a tractor unit (own knowledge).
- Tank: 49 m³ × filling ratio 0.42 kg/l for Mixture C (ADR/P200, own knowledge) ≈ 20,580 kg, consistent with the plate's maximum load of 20,500 kg; 20,180 kg is within it.
- Dangerous goods: UN 1965, class 2.1, orange plate 23 over 1965, placard 2.1, tunnel code B/D for tank carriage, emergency card for class 2 (own knowledge of ADR).
- Emissions: 1700 KWH × 0.268 = 455.6 → 456 KGM; 1240 KWH × 0.268 = 332.3 → 332 KGM; 0.268 kg CO2e/kWh fits diesel tank-to-wheel (own knowledge); the empty run uses less energy than the loaded one.
- Times: empty weighing 05:40, loaded 06:45, issue 06:50, planned departure 07:00, planned arrival 15:40, all on 2026-06-10; the despatch advice is issued at 07:05.
- Shipment and consignment IDs match `02-DespatchAdvice.xml`; consignor, consignee and carrier match the despatch advice; the two distributed originals match the note on three originals (the carrier keeps its own).

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cac:EnvironmentalEmission[2]/cac:EmissionCalculationMethod/cbc:CalculationMethodCode` = `CALCULATED`: an emission for an empty run on the next day, stated before it happens — refuted, a calculated (not measured) value for a planned run is legitimate, and the description explains why it is counted against this consignment.
- `/Waybill/cac:ReceiverParty/cac:PhysicalLocation`: master data of the receiver in a waybill — refuted, the receiver is the consignor and its plant is the place of taking over.
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `TE`: trailer for a tank semi-trailer — refuted, the tank is carried on the trailer `BV TK 0419` of an articulated tank lorry (`3113`).
