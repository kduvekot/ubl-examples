# LLM review: 17-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/17-TransportationStatus.xml`, Git blob `ca6268e2b075e6b8011b2c7aa08d386ab1c51391` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### sea/17#F1 · High · A consignment ID is given as the shipping order number
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- Why: ShippingOrderID is "a reference number for a shipping order"; LD-CS-26-0133 is the
  consignment's identifier (`/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`). The bill of lading this status
  refers to gives the shipping order as
  `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137` (the forwarding
  instructions 12-ForwardingInstructions.xml). Across the flow the element carries three different
  values for the same shipment: LD-SH-26-0132 in 09 and 12, LD-CS-26-0133 in 13 and 17,
  BF-FI-26-0137 in 14 (grep of `<cbc:ShippingOrderID>` over `sea/*.xml`).
- Condition: ShippingOrderID, if present, is the identifier of the shipping order (the same as in
  14-BillOfLading.xml), not the consignment ID.
- Options: (a, preferred) BF-FI-26-0137, matching the bill of lading; (b) remove it, since the
  consignment and the bill of lading already identify the shipment.
- Needs decision: no

### sea/17#F2 · Medium · DetentionTransportEvent used for holding the cargo for a pallet check
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:OccurrenceTime` = `12:00:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:Description` = `Wooden pallets must carry the heat-treatment mark.`
- Why: DetentionTransportEvent is "the detention of a transport means during loading and unloading
  operations", i.e. the vessel held at the berth. At 12:00 the container had already been
  discharged (11:20); what is held for the heat-treatment check of the wooden pallets is the
  container and its cargo, which the document records separately as the container's quarantine
  (`/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:QuarantineTransportEvent/cbc:OccurrenceTime` = `15:00:00`).
  The description states a rule, not what happened.
- Condition: no detention of the transport means is reported unless the vessel was held; the hold
  of the container for the pallet check is recorded on the container (start and end), with a
  description of what happened.
- Options: (a, preferred) move the 12:00 hold to the container (e.g. as the start of the
  quarantine, with 15:00 as its completion) and describe it as an event ("held for the
  heat-treatment mark check of the wooden pallets"); (b) remove the detention event.
- Needs decision: no

### sea/17#F3 · Low · A container event that says nothing
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-18`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEvent/cbc:OccurrenceTime` = `11:40:00`
- Why: "an additional transport event not specified elsewhere" with only a date and time: no type
  code, description or location, so the reader cannot tell what happened at 11:40 (between the
  discharge at 11:20 and the hold at 12:00). Without a type it has no business content (IND5).
- Condition: the event says what happened (type code or description) and where, or is absent.
- Options: (a) give it a type and description (e.g. container moved to the inspection area);
  (b) remove it.
- Needs decision: no

## Checked and consistent
- References: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `TOL-BL-26-0139` is
  14-BillOfLading.xml; consignment LD-CS-26-0133, consignee Velumi Trading, carrier Tidewell
  Ocean Lines and container TWLU4120872 (ISO 6346 check digit 2 correct) agree with it; stage ID 2
  agrees with the main carriage stage of 14 and 15.
- Times against the issue time 2026-05-18 16:36: arrival 06:30, discharge 11:20 (completed),
  11:40, 12:00, quarantine completed 15:00, all before the issue time and in a plausible order
  (one container discharged about five hours after arrival); the status period is that day.
- Port of Selanu (XLSEL, coordinates 40°01.20'S 15°08.40'W) is described as in
  16-CommonTransportationReport.xml.

## Outside this review
- 14-BillOfLading.xml expects the container to be available on 2026-05-18 at 14:00; here it is
  released after the quarantine at 15:00 (timeline across documents).
