# LLM review: 15-DespatchAdvice.xml

Flow: rail (LMW-TX-26-0734) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/rail/15-DespatchAdvice.xml`, Git blob `c9599a8d272b4977d8534ddddea298a589883f79` (committed)
- Last commit changing the example: 771277df 2026-11-21 Rail lots per container, mast order DG identification, air timing and origin statement, sawmill buys its logs
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### rail/15#F1 · Low · One despatch time for two containers that left two hours apart
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchTime` = `15:00:00-01:00`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:PickupTransportEvent/cbc:OccurrenceTime` = `13:00:00-01:00`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:PickupTransportEvent/cbc:OccurrenceTime` = `15:00:00-01:00`
- Why: The despatch advice gives one actual despatch at 15:00 on 13 April for the whole shipment, while the waybill and `07-TransportationStatus.xml` record the carrier picking up container FRXU1044175 at 13:00 and FRXU1044180 at 15:00 from the same warehouse. 15:00 is right for the second container only; for line 1 the despatch advice states a time two hours after that container had left.
- Condition: The despatch time(s) in the despatch advice agree with the pickups in `08-Waybill.xml` for each container, or the document makes clear that the time is that of the last container.
- Options: (a) preferred: give each container its own despatch (e.g. one `Shipment/Delivery` per line via `DespatchLine/Shipment`, or the time in the line note); (b) keep one time and say in the note that the second container left at 15:00 and the first at 13:00.
- Needs decision: no

### rail/15#F2 · Low · Containers and seals only in line notes
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `Container FRXU1044175, seal XU-VI-30411: the lot of 9 April.`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cbc:Note` = `Container FRXU1044180, seal XU-VI-30412: the lot of 10 April.`
- Why: The receiving party is asked to check the goods on arrival; container numbers and seal numbers are what goods-in checks against, and the despatch advice has structured places for them (`Shipment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal`, or `DespatchLine/Shipment`). Here they are only in free text, so the receiver cannot match them mechanically with the waybill (`08-Waybill.xml`) and the transit declaration (`06-TransitCustomsDeclaration.xml`), which carry them structured. The values themselves agree with 06 and 08.
- Condition: The container and seal of each line are given in the structured transport equipment of the shipment (the notes may stay).
- Options: (a) preferred: add the two containers with their seals under the shipment and link each line to its container; (b) leave as it is, if the despatch advice is meant only for the line-level lot information.
- Needs decision: no

## Checked and consistent
- Quantities: 96 + 96 = 192 benches, as ordered (`01-Order.xml`) and invoiced (`11-Invoice.xml`); both lines refer to order line 1.
- Shipment 7400043688 and consignment 7300043586 as in 02, 03, 06, 07, 08; gross weight 10 377.6 kg as in 06 and 14; carrier Ferrano Rail Cargo as in 08.
- Container/seal pairs FRXU1044175/XU-VI-30411 and FRXU1044180/XU-VI-30412 agree with `06-TransitCustomsDeclaration.xml` and `08-Waybill.xml`; GLN passes `check_ids.py`.
- Issue time 15:20 is after the despatch at 15:00; the despatch party is Castrano Logistics, whose warehouse in Conciaro is the pickup place in 08.
