# LLM review: 07-TransportationStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

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

### rail/07#F1 · Medium · Consignment ID used as shipping order number and as document reference
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `VI-CS-26-0327`
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `VI-CS-26-0327`
- Why: ShippingOrderID is "a reference number for a shipping order"; DocumentReference/ID is "an identifier for the referenced document". VI-CS-26-0327 is the consignment's ID (`/TransportationStatus/cac:Consignment/cbc:ID` = `VI-CS-26-0327`, also in rail/02, 03, 06, 08, 09). No shipping order and no document with this ID exists in the flow (`flow_index.py rail`: `-> ?`), and the consignment is already identified in the report.
- Condition: ShippingOrderID and DocumentReference/ID are absent or hold identifiers of a shipping order / document that exists in the flow.
- Options: (a) preferred: drop both (the consignment is identified in Consignment/ID); (b) reference the transport execution plan or request as the shipping order, if the world treats it so.
- Needs decision: no

### rail/07#F2 · Medium · The road collection reported as an event of the rail main carriage
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: The pickup on 13 April 15:00 is the collection of the containers at the Castrano warehouse by the carrier's tractor (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`). That is road pre-carriage to the hub, not part of the main carriage by train, which begins with loading at the hub on 14 April.
- Condition: the road collection is in a pre-carriage stage (or at consignment level), the main-carriage stage holds rail events only.
- Options: (a) preferred: a PreCarriageShipmentStage with the pickup; (b) the pickup as the consignment's actual pickup.
- Needs decision: no

### rail/07#F3 · Medium · A transport event that says nothing about what happened
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportEvent/cbc:OccurrenceTime` = `05:40:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportEvent/cbc:CompletionIndicator` = `true`
- Why: The stage's TransportEvent is "an additional significant occurrence … that is not defined elsewhere in this Shipment Stage". It has only a date, a time and a completion flag: no type code, description or location, so the receiver cannot tell what occurred. From the waybill it can be guessed as the loading of the containers onto the wagon at 05:40 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingTransportEvent/cbc:OccurrenceTime` = `05:40:00`), which the document-level event "Two containers loaded on the container train" describes without a time.
- Condition: every transport event says what it is (type or description) and, where it matters, where.
- Options: (a) preferred: merge the two: one loading event with time, description and location; (b) add a type code and location to the stage event.
- Needs decision: no

### rail/07#F4 · Medium · Province in Region
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: A province is an administrative division (CountrySubentity), not a Region.
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/07#F5 · Low · Optional takeover without a reason or place
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent/cbc:OccurrenceTime` = `17:00:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent/cbc:CompletionIndicator` = `false`
- Why: OptionalTakeoverTransportEvent is "the optional takeover of the goods in this shipment stage". Nothing in the flow describes a takeover option (by whom, where); at 17:00 on 14 April the train is under way to Marrowdale. Without a party, place or reason the event is a filler.
- Condition: the event is absent, or describes a takeover the story contains (place and party).
- Options: (a) preferred: drop it; (b) give it a location and context (e.g. handover to a Bayvarran rail operator at the border station), which would change the story.
- Needs decision: no

## Checked and consistent
- Sender (the hub) is the terminal operator of the stage; the report refers to the plan (`/TransportationStatus/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0328`, rail/03).
- The planned delivery 15 April 11:00, not completed, agrees with the plan.
- TransportExecutionStatusCode INPROGRESS fits a report between departure and delivery.

## Considered and refuted
- `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`: suspected an instruction without a reason — refuted because it tells the receiver when an answer is expected, which is what the element is for.

## Outside this review
- Timeline: the report "Two containers loaded on the container train" is issued at 13:11 on 14 April, six hours after the train left the hub at 06:52 (rail/05, rail/08).
