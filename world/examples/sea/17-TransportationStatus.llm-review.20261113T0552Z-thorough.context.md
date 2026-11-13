# LLM review: 17-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### sea/17#F1 · Medium · A consignment ID given as the shipping order number
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`
- Why: `ShippingOrderID` is "A reference number for a shipping order". The value is the consignment's own identifier, which the same document gives as `Consignment/ID` ("An identifier assigned to a collection of goods for both import and export"). A shipping order is a document by which the shipper or forwarder books carriage; in this flow that role is played by the forwarder's forwarding instructions to the carrier, `12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `BF-FI-26-0137`, which the bill of lading also cites. An identifier of one kind (a consignment) is used as another (an order).
- Condition: `ShippingOrderID` holds the number of a shipping order (booking or instruction) that exists in the flow, or is absent.
- Options: (a) preferred: remove it, since the consignment is already identified and the port has no reason to quote the shipper's order; (b) put the number of the instruction that booked the carriage (`BF-FI-26-0137`) if the port knows it.
- Needs decision: no

### sea/17#F2 · Medium · Vessel detention used for a pallet marking requirement on the container
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:Description` = `Wooden pallets must carry the heat-treatment mark.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:OccurrenceTime` = `12:00:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:QuarantineTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: `DetentionTransportEvent` under a shipment stage is "The detention of a transport means during loading and unloading operations", i.e. the ship being held. The event is dated 12:00, after the container was already discharged (11:20), and its text is a phytosanitary rule about the wooden pallets in the container (ISPM 15 heat-treatment mark, own knowledge), which concerns the goods' packaging, not the vessel. The container's own `QuarantineTransportEvent` (15:00, completed) is where the pallet inspection belongs. The detention event therefore says that the ship was detained, which nothing else supports, and its text is a requirement, not an event.
- Condition: No detention of the transport means is reported unless the ship was held; the pallet inspection is expressed on the equipment or goods it concerns, with text that describes what happened.
- Options: (a) preferred: remove the detention event and describe the inspection (pallets checked for the mark, result) on the container's quarantine event; (b) if the story wants the ship held, give the detention a reason concerning the ship and a time while it was alongside before discharge ended.
- Needs decision: no

### sea/17#F3 · Low · An equipment event with neither type nor description
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEvent/cbc:OccurrenceTime` = `11:40:00`
- Why: `TransportEvent` under the equipment is "An additional transport event not specified elsewhere in this Transport Equipment". It carries only a date and a time: no type code, description or location says what happened at 11:40, so the receiver cannot use it.
- Condition: Every transport event says what it is (type code or description) and, where it matters, where it happened.
- Options: (a) preferred: give it a type and description (e.g. container moved to the inspection area, gated in to the container yard); (b) remove it.
- Needs decision: no

### sea/17#F4 · Low · The discharge is reported twice, once as an "additional" event
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Container TWLU4120872 discharged and available for customs clearance.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:OccurrenceTime` = `11:20:00`
- Why: The document-level `TransportEvent` is for "Any additional events associated with this Transportation Status report that are not defined elsewhere in this document". The discharge is already defined in the dedicated `DischargeTransportEvent`; the extra event repeats it word for word from the document `Description`, with a date but no time. Only the part "available for customs clearance" is new, and that is a status, which the report would better carry once.
- Condition: The discharge is reported once, in its dedicated element; any additional event adds something not expressed elsewhere.
- Options: (a) preferred: keep the additional event only for the release for customs clearance, with its time (after the quarantine inspection at 15:00); (b) remove it.
- Needs decision: no

### sea/17#F5 · Low · "Automatic report" while a named duty officer reports and asks for replies on a delivery slot
- XPath: `/TransportationStatus/cbc:Note[2]` = `Automatic report from the sender's tracking system.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ReportingPerson/cbc:JobTitle` = `Duty officer`
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: The note says the report is generated automatically, but the main-carriage stage names a duty officer of the port as the `ReportingPerson` ("a person being responsible for providing the required administrative reporting relating to a transport"; at a sea stage this is normally the ship's master or agent, not the terminal's duty officer). The `OtherInstruction` refers to a "delivery slot", but the document contains no delivery or slot: it reports discharge, quarantine and availability for clearance. The free texts do not agree with the structured content.
- Condition: The notes and instructions describe what this report is and refer only to things the report contains; the reporting person is the one responsible for the stage's reporting.
- Options: (a) preferred: drop the "automatic" note or the reporting person, and make the instruction refer to something in the report (e.g. the collection after clearance); (b) add the delivery slot the instruction refers to, if the port books one.
- Needs decision: no

## Checked and consistent
- Event order on 2026-05-18: actual arrival 06:30, discharge 11:20 (completed), equipment event 11:40, quarantine 15:00 (completed), issue 16:36; all completed events lie before the issue time.
- The arrival agrees with the requested arrival in `16-CommonTransportationReport.xml` (2026-05-18 06:00 at the fairway buoy, 06:30 here).
- The container `TWLU4120872` (ISO 6346 check digit OK) is the one in `15-Manifest.xml` and `14-BillOfLading.xml`; the referenced bill of lading `TOL-BL-26-0139` exists (`14-BillOfLading.xml`).
- The terminal operator's location (UN/LOCODE XLSEL, coordinates) is described as in `16-CommonTransportationReport.xml`.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:Amount`: a terminal handling charge in a status report suspected as data the document does nothing with — refuted because the definition provides for a service charge per equipment and telling the forwarder what the terminal will bill for the discharge is a real reason for it.
- `/TransportationStatus/cbc:TransportExecutionStatusCode`: "in progress" suspected to contradict the completed discharge — refuted because the transport to the consignee is not finished; the container still awaits clearance and collection.
