# LLM review: 07-TransportationStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/07-TransportationStatus.xml`, Git blob `104dc14ba8f489635d6473fbc6d93903f6bf457e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### rail/07#F1 · Medium · The consignment ID is given as shipping order and as a document reference
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `VI-CS-26-0327`
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `VI-CS-26-0327`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `VI-CS-26-0327`
- Why: ShippingOrderID is "a reference number for a shipping order", DocumentReference "a reference to another document associated with this document". VI-CS-26-0327 is the consignment identifier ("an identifier assigned to a collection of goods", as in rail/02, rail/03, rail/08); no document of the flow has this ID (flow_index: `-> ?`). The report thus uses a consignment ID as an order number and as a document number — an identifier of one kind used as another. The shipping order of this transport is the transport execution plan request rail/02 (VI-TR-26-0326), or the plan rail/03, which is already referenced in TransportExecutionPlanDocumentReference. The same consignment ID is in the waybill's ShippingOrderID (rail/08).
- Condition: ShippingOrderID, if present, holds the ID of the shipping order (or forwarding instruction) of this transport, and DocumentReference points to an existing document of a stated kind or is absent; the consignment ID appears only as the consignment's ID.
- Options: (a) preferred: ShippingOrderID = VI-TR-26-0326 (the transport user's request, the closest thing to a shipping order in the flow) and remove the DocumentReference; (b) remove both, since the consignment and the plan are already identified.
- Needs decision: no

### rail/07#F2 · Medium · Road pickup at the warehouse recorded in the rail main carriage
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: The pickup on 2026-04-13 at 15:00 is the collection of the containers at the Castrano warehouse by the carrier's tractor (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`), a road leg to the hub. The main carriage of this consignment is the container train from the hub (rail/03, rail/08). An event belongs to the stage it happens in; the road pickup is pre-carriage.
- Condition: The pickup at the warehouse is in a pre-carriage stage (with its mode), or the main carriage's first event is the takeover/loading at the hub.
- Options: (a) preferred: a `cac:PreCarriageShipmentStage` (TransportModeCode 3) carrying the actual pickup, with the warehouse as location; (b) drop the pickup from the report, since it reports the loading on the train.
- Needs decision: no

### rail/07#F3 · Medium · The loading is reported as free text, and the stage's 05:40 event says nothing
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Two containers loaded on the container train.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportEvent/cbc:OccurrenceTime` = `05:40:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportEvent/cbc:CompletionIndicator` = `true`
- Why: The report's purpose (its description: "Two containers loaded on the container train.") is the loading. ShipmentStage has a dedicated LoadingTransportEvent ("the loading of goods in this shipment stage"), but the loading is given as a document-level TransportEvent ("any additional events … not defined elsewhere in this document") with text, a date and no time. In the main carriage stage, a generic TransportEvent at 05:40 is completed, with no type code, description or location; only the waybill reveals that 05:40 is the loading time (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingTransportEvent/cbc:OccurrenceTime` = `05:40:00`). The structured event that would carry the report's message is missing, and the one that is present is meaningless on its own.
- Condition: The loading is in `cac:MainCarriageShipmentStage/cac:LoadingTransportEvent` with date, time 05:40, completion and location (the hub); no event without a type, description or dedicated element remains.
- Options: (a) preferred: replace the stage's generic TransportEvent with LoadingTransportEvent (05:40, location Ferrano Intermodal Hub) and drop the document-level TransportEvent or keep it only as the report's event of record with a TransportEventTypeCode; (b) give the generic events a TransportEventTypeCode from a list and a location.
- Needs decision: no

### rail/07#F4 · Low · An optional takeover with no place and no purpose in the story
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent/cbc:OccurrenceTime` = `17:00:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent/cbc:CompletionIndicator` = `false`
- Why: OptionalTakeoverTransportEvent is "the optional takeover of the goods in this shipment stage". On 2026-04-14 at 17:00 the train is on its way to Marrowdale, where it is due on 2026-04-15 (planned delivery 11:00 in the same stage); the report does not say where a takeover could happen, by whom, or why it is optional. No other example of the flow mentions a takeover. The value has no visible business reason (IND5/IND6).
- Condition: Either the optional takeover is removed, or it has a location and party and fits the train's schedule (e.g. the handover to a Bayvarran rail undertaking at the border station, which then appears in the plan and waybill too).
- Options: (a) preferred: remove it; (b) make it the handover at the border station (location, TransportEventTypeCode), with matching statements in rail/03 and rail/08.
- Needs decision: yes

### rail/07#F5 · Low · Two containers reported loaded, but not identified
- XPath: `/TransportationStatus/cbc:Description` = `Two containers loaded on the container train.`
- XPath: `/TransportationStatus/cac:Consignment`
- Why: The report says two containers were loaded but names neither the containers (FRXU1044175, FRXU1044180 in rail/06 and rail/08) nor the train or wagon; the receiving carrier has to infer them from the consignment ID. A status report on equipment loading usually identifies the equipment.
- Condition: The containers the report is about are identified in it (e.g. `cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID`), or the report is evidently about the consignment only.
- Options: add the two containers with their IDs and, optionally, the train FRC 4417 in the stage's TransportMeans (preferred).
- Needs decision: no

## Checked and consistent
- TransportExecutionPlanDocumentReference FRC-TEP-26-0328 resolves to the plan rail/03 for the same consignment.
- Times against the issue time (2026-04-14 13:11): the loading at 05:40 and the pickup on 2026-04-13 are in the past and completed; the delivery 2026-04-15 11:00 is not completed (CompletionIndicator false) and equals the plan's planned delivery; status period 2026-04-14.
- Terminal operator Ferrano Intermodal Hub is the party where the loading takes place (rail/08 loading location Ferrano, XUFER); sender (hub) to receiver (carrier) fits a terminal's loading report.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DeliveryTransportEvent/cbc:CompletionIndicator` = `false`: a future delivery in a status report — refuted: the completion indicator marks it as not yet happened, which is a correct way to report the expected delivery.
- `/TransportationStatus/cbc:TransportExecutionStatusCode` = `INPROGRESS`: fits a train under way after loading; consistent with rail/05 and rail/08.
