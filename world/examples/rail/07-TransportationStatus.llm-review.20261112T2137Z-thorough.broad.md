# LLM review: 07-TransportationStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/07-TransportationStatus.xml`, Git blob `104dc14ba8f489635d6473fbc6d93903f6bf457e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 02a09a9 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### rail/07#F1 · Medium · Consignment ID used as shipping order and as document reference
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `VI-CS-26-0327`
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `VI-CS-26-0327`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `VI-CS-26-0327`
- Why: ShippingOrderID is "A reference number for a shipping order", DocumentReference/ID "An identifier for the referenced document". VI-CS-26-0327 is the consignment's identifier ("An identifier assigned to a collection of goods"), given as such in the same document and in 02, 03, 06 and 08; no shipping order or document with that number exists in the flow (flow_index: `-> ?`). The booking documents are the request VI-TR-26-0326 (02) and the plan FRC-TEP-26-0328 (03, already referenced).
- Condition: ShippingOrderID and DocumentReference hold identifiers of a shipping order or document that exists (or are absent); the consignment is identified only as a consignment.
- Options: (a) preferred: drop both; the consignment and the plan are already identified; (b) ShippingOrderID = VI-TR-26-0326 if the world treats the transport request as the shipping order.
- Needs decision: no

### rail/07#F2 · Medium · Loading reported in generic events instead of the loading event
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Two containers loaded on the container train.`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportEvent/cbc:OccurrenceTime` = `05:40:00`
- Why: The shipment stage has a dedicated LoadingTransportEvent ("The loading of goods in this shipment stage"). The report states the loading twice in generic events: at document level ("Any additional events ... not defined elsewhere in this document") with a date and place but no time, and in the stage as an anonymous TransportEvent ("A additional significant occurrence ... not defined elsewhere") at 05:40 with no type, description or location, which on its own says nothing. The waybill records the loading of the container at the same time (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingTransportEvent/cbc:OccurrenceTime` = `05:40:00`).
- Condition: The loading is reported once, in MainCarriageShipmentStage/LoadingTransportEvent, with date, time and location; no event without type or location remains.
- Options: (a) preferred: one LoadingTransportEvent (14 April 05:40, Ferrano Intermodal Hub) and drop both generic events; (b) keep the document-level event only for something that has no dedicated element.
- Needs decision: no

### rail/07#F3 · Medium · Pickup at the warehouse put in the main carriage stage
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: The pickup on 13 April at 15:00 is the carrier's tractor collecting the boxes at Castrano's warehouse (03 plans it, 08 records it as the equipment pickup at "Castrano Logistics warehouse, Ferrano"). That is the carrier haulage before the rail stage, i.e. pre-carriage; the main carriage begins at the hub on 14 April.
- Condition: The pickup is in a PreCarriageShipmentStage (or at consignment level), and the main carriage stage holds only rail events.
- Options: (a) preferred: a PreCarriageShipmentStage (road, mode 3) with the pickup and the arrival at the hub; (b) report the pickup at consignment level if stages are not wanted.
- Needs decision: no

### rail/07#F4 · Medium · Province given in Region
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division (CountrySubentity). 219 occurrences over the examples.
- Condition: The province is in CountrySubentity, or the world defines it as non-administrative.
- Options: (a) preferred: CountrySubentity; (b) keep Region if provinces are not administrative.
- Needs decision: yes (a fact of the world)

### rail/07#F5 · Low · Optional takeover with no reason in the flow
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent/cbc:OccurrenceTime` = `17:00:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent/cbc:CompletionIndicator` = `false`
- Why: OptionalTakeoverTransportEvent is "The optional takeover of the goods in this shipment stage". On 14 April at 17:00 the containers are on the train between Ferrano and Marrowdale (they left at 06:52); no document of the flow describes any party that could take the goods over then, or an option to do so. The event has no location either.
- Condition: The event is absent, or the flow describes the takeover option (who, where) it refers to.
- Options: (a) preferred: drop it; (b) give it a location and a party if the world has a takeover (e.g. a handover at the border to a Bayvarran rail operator).
- Needs decision: no

### rail/07#F6 · Low · Terminal control reachable only in office hours
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Name` = `Terminal control`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The terminal operator's control loads the train at 05:40 and dispatches it at 06:52; weekdays 08:00–17:00 does not fit a contact that is used in these hours.
- Condition: The stated availability covers the terminal's operating hours.
- Options: (a) preferred: the hub's real hours; (b) drop the Note.
- Needs decision: no

## Checked and consistent
- Reference: `FRC-TEP-26-0328` resolves to 03 (TransportExecutionPlan); the planned delivery 15 April 11:00 equals the delivery event here (not yet completed, correct at 13:11 on 14 April).
- Sender Ferrano Intermodal Hub (also terminal operator and signatory) and receiver Ferrano Rail Cargo fit a terminal reporting to the carrier; parties are described as in the other rail examples.
- StatusPeriod 14 April and status location the hub agree with the events; TransportExecutionStatusCode INPROGRESS fits a train under way.
- Loading at 05:40 lies between the train's arrival at the hub at 05:30 and its departure at 06:52 (05).

## Considered and refuted
- `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`: suspected an instruction to the wrong party — refuted because the carrier, which receives the report, is the party that would have to change the delivery slot with the consignee.
- `/TransportationStatus/cbc:IssueTime` = `13:11:00`: suspected a stale report (loading at 05:40, departure at 06:52 not reported) — refuted because a status report need not report every event and the document says it reports the loading; the delay between event and report is a timeline question.
