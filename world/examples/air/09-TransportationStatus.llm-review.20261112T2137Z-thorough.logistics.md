# LLM review: 09-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/09-TransportationStatus.xml`, Git blob `96f9c4474b3f63541414ff30ba5eab834320aedc` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### air/09#F1 · High · Arrival on 2026-05-14 contradicts the cancellation issued five minutes earlier
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cbc:IssueTime` = `17:58:00`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:IssueTime` = `17:53:00`
- Why: The fulfilment cancellation air/07 (2026-05-14 17:53) says the cargo missed its flight and
  goes on the next day's flight. The only booked flight is KXL207 on 2026-05-14 07:00 (air/04). This
  report (17:58 the same day) says the cargo arrived at Selanu on 2026-05-14. Both cannot be true
  of the same consignment LD-CS-26-0324 (see air/07#F1 for the possible readings).
- Condition: the arrival date reported here agrees with the flight the cargo actually took as stated
  in air/04 and air/07.
- Options: see air/07#F1; with its option (a) this report stays as it is.
- Needs decision: yes

### air/09#F2 · High · ShippingOrderID holds the consignment ID
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- Why: ShippingOrderID is "A reference number for a shipping order"; the shipping order of the
  forwarding instructions air/03 is LD-SH-26-0323. The value is the consignment ID, given again in
  Consignment/ID. Same value in air/04 and air/05.
- Condition: ShippingOrderID is LD-SH-26-0323 (or absent).
- Options: LD-SH-26-0323 (preferred); or drop it.
- Needs decision: no

### air/09#F3 · Medium · The arrival is a generic event instead of the stage's actual arrival
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cbc:ID` = `1`
- Why: TransportationStatus/TransportEvent is for events "not defined elsewhere in this document".
  The arrival of the main carriage has its dedicated element, ShipmentStage/ActualArrivalTransportEvent
  (UBL 2.5 model), and the report already has the main-carriage stage at Selanu. As a document-level
  event without type, the arrival and the readiness for customs are free text only.
- Condition: the arrival is the main-carriage stage's ActualArrivalTransportEvent (date, time,
  location XLSLA); readiness for customs, if kept, is an event with a type code (or AvailabilityTransportEvent).
- Options: ActualArrivalTransportEvent plus AvailabilityTransportEvent in the stage (preferred).
- Needs decision: no

### air/09#F4 · Low · The arrival has no time
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: An automatic tracking report of an arrival gives its time; the waybill's arrival is 10:00
  (air/04). Without it the report cannot be matched with a flight, which matters given air/09#F1.
- Condition: the arrival has an OccurrenceTime before the issue time 17:58.
- Options: add the time (preferred).
- Needs decision: no

### air/09#F5 · Low · Status location is the company name, without the airport's identifier
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Selanu airport, cargo terminal`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`
- Why: The status location carries the handling agent's company name; neither location has the
  UN/LOCODE XLSLA that air/04 gives for Selanu airport.
- Condition: both locations name the place and carry XLSLA (schemeID UN/LOCODE).
- Options: add the identifier and the place name (preferred).
- Needs decision: no

### air/09#F6 · Low · "Delivery slot" that no document states
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: The report goes to the forwarder; no document of the flow gives a delivery slot (time window
  for collection or delivery at Selanu), so the instruction has nothing to refer to.
- Condition: the slot the instruction refers to is stated (here or in a referenced document), or the
  instruction is not there.
- Options: state the collection slot at the cargo terminal (e.g. as an AvailabilityTransportEvent
  or in the note; preferred), or drop the instruction.
- Needs decision: no

## Checked and consistent
- `DocumentReference/ID` KXL-WB-26-0325 resolves to air/04-Waybill.xml, issued 2026-05-13, before this report.
- Consignee Velumi Trading and carrier Kelaro Air Cargo agree with air/04; Selanu Airport Cargo is
  the party that receives the consignee's original of the waybill in air/04 (distribution 1), so it is
  the destination handling agent, consistent with its role here.
- Receiver Bayforth Forwarding is the forwarder of air/03 and air/04.
- TransportExecutionStatusCode INPROGRESS fits cargo arrived but not yet cleared and delivered.
