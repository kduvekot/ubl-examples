# LLM review: 11-Waybill.xml

Flow: medicines (BYF-TX-26-3169) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/11-Waybill.xml`, Git blob `659e9cecef7573a3feac25dc69f9d9b4de4ad825` (committed)
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

### medicines/11#F1 · Low · 3.5 kg of packaging for fourteen cartons and an insulated dry-ice box
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:GrossWeightMeasure` = `101.1`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem[5]/cbc:NetWeightMeasure` = `6`
- Why: the goods items 1 to 4 weigh 60 + 12 + 1.6 + 18 = 91.6 kg, the dry ice 6 kg; 101.1 − 97.6 = 3.5 kg remain for fourteen cartons and the insulated box around the dry ice. That is light for a polystyrene dry-ice shipper (some 2 to 4 kg) plus fourteen cartons (own estimate), though not impossible. The same figures are in `06-ForwardingInstructions.xml` (medicines/06#F2).
- Condition: the consignment's gross weight covers goods, dry ice and a plausible packaging weight, equal in the forwarding instructions, the despatch advice and the waybill.
- Options: as medicines/06#F2.
- Needs decision: no

## Checked and consistent
- AWB number `KXL-00698121`: the serial 0069812 with check digit 1 satisfies the air waybill mod-7 rule (69812 mod 7 = 1; own knowledge); the letter prefix cannot be mistaken for a real airline's numeric prefix.
- Times: issued 06:45 +00:00 (05:45 at Lumeport), after acceptance at 05:30 −01:00 (`10-TransportationStatus.xml`); planned departure 07:00 −01:00 (08:00 UTC), arrival 10:45 UTC, as recorded on arrival in `12-TransportationStatus.xml`.
- Dangerous goods: UN 2915 Type A, Category III-YELLOW, TI 1.5, 97 GBq on 15 June (20 GBq × 2^(150 h/65.94 h); own knowledge); UN 1845 dry ice 6 kg, class 9, PI 954, ERG 120; both stowed in the aft hold, away from each other per the handling instructions.
- Packages: ten cartons of 30 and four of 60 in the active container (= 300 + 240 units), 40 varicella doses in the dry-ice box, one radioactive package, as in `06-ForwardingInstructions.xml` and `09-DespatchAdvice.xml`.
- Parties: carrier and sender Kelaro Air Cargo, receiver and forwarder Bayforth Forwarding, consignor Quillmoor, consignee the hospital, notify party the hospital's customs broker (who lodges `13-ImportCustomsDeclaration.xml`); the two originals distributed match the note.
- Aircraft registration `QL-KXA`: ITU prefixes beginning with Q are not allocated, so it cannot be a real registration.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:Description` = `Active temperature-controlled LD3 container (RKN), set to 5 °C` on an ATR 72 freighter (`ATF`): an LD3 on a turboprop freighter looked doubtful — refuted, the ATR 72-600F with its large cargo door is offered for LD3 containers on its main deck (own knowledge), and the stowage position `MD-4` is on the main deck.
- `/Waybill/cac:Shipment/cac:GoodsItem[4]/cac:Item/cac:HazardousItem/cac:HazardousGoodsTransit/cbc:TransportAuthorizationCode` = `PCA` on a freighter: refuted, the code states that the package is permitted on passenger and cargo aircraft, which includes a freighter.

## Outside this review
- The ULD identifier `RKN20871K0` ends in the owner code `K0`; whether `K0` is a real airline's two-character code could not be checked here.
- Whether an ATR 72 can fly from Lumeport to Selanu in 2 h 45 min depends on the distance between the airports (timeline across the map).
