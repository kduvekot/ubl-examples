# LLM review: 03-ForwardingInstructions.xml

Flow: reefer (HRW-TX-26-0730) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/03-ForwardingInstructions.xml`, Git blob `524e1c112e737d77f4a4bd97d9d879fb5da5dd9d` (committed)
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### reefer/03#F1 · Low · Ports of loading and discharge, sailing and date only in free text
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ForwarderServiceInstructions` = `Book a 40-foot reefer on Tidewell's sailing of 23 April to Selanu; …`
- Why: the instruction asks the forwarder to book a sailing from Lumeport to Selanu on 23 April, but the shipment carries no structured route: no main-carriage stage with loading and unloading port, no requested departure, no delivery location or delivery terms (the sale is CIP Port of Selanu, `01-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:ID` = `XLSEL`). The forwarder can only learn the destination port from the text and the consignee's address. The bill of lading later carries the ports as `XBLMP` and `XLSEL` (`07-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSEL`).
- Condition: the forwarding instructions state the requested route (at least the port of discharge, preferably also the port of loading and the requested sailing date) in structured elements.
- Options: (a) add a main-carriage shipment stage with LoadingPortLocation, UnloadingPortLocation and a requested departure (preferred: it is what the forwarder books); (b) add the CIP delivery terms with the place.
- Needs decision: no

## Checked and consistent
- Insurance: `/ForwardingInstructions/cac:Shipment/cbc:InsuranceValueAmount` = `31754.80` = 110 % of the agreed contract value 28,868.00 (`02-OrderResponse.xml`), as CIP requires with Institute Cargo Clauses (A) (own knowledge of Incoterms 2020); the policy amount repeats it.
- Gross weight 21,728 kg = 1,120 cartons × 19.4 kg, the figure used per goods item in `04-GoodsCertificate.xml` and `05-ExportCustomsDeclaration.xml`; 1,120 cartons × 18 kg = 20,160 kg of fruit, so 1.4 kg of tray, carton and pallet share per carton, plausible.
- 20 pallets in a 45R1 container: the count matches the 20 SSCCs in `06-DespatchAdvice.xml` and `07-BillOfLading.xml`.
- Temperatures: set point 0.5 °C inside the range 0–1 °C on goods item and equipment; 90 % humidity is usual for apples and pears (own knowledge). HS codes 080810 and 080830 fit apples and pears.
- Parties and identifiers agree with `01-Order.xml`, `05-ExportCustomsDeclaration.xml` and `07-BillOfLading.xml`.

## Considered and refuted
- `/ForwardingInstructions/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `21728`: pallets might be missing from a gross weight "including packing and packaging" — refuted: 19.4 kg per 18 kg carton leaves room for the pallet share (about 25 kg ÷ 56 cartons ≈ 0.45 kg) besides the carton.
- `/ForwardingInstructions/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:MinimumTemperature/cbc:Measure` = `0`: "minimum allowable operating temperature for this container" could mean the unit's technical range — refuted: read as the range the reefer is allowed to run in on this trip, it fits and agrees with the goods item.
- `/ForwardingInstructions/cac:Shipment/cac:GoodsItem/cac:Temperature/cbc:AttributeID` = `SETPOINT`: a set point is a setting of the equipment — refuted: TransportEquipment has no temperature element other than minimum and maximum, and the goods item's temperature is where the required carriage temperature is stated.
- `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`: UBL defines the freight forwarder as a consolidator, while the consignment is not consolidatable — refuted: the document type itself is addressed to the forwarder, and this is the role it names.
