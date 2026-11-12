# LLM review: 05-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/05-TransportationStatus.xml`, Git blob `9e63ff7c8a83c2b085bcdc225a1065a3d43ba26b` (committed)
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

### air/05#F1 · High · The report refers to a waybill that is issued 38 minutes later
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `KXL-WB-26-0325`
- XPath: `/TransportationStatus/cbc:IssueTime` = `10:05:00`
- XPath: `04-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-05-13`
- XPath: `04-Waybill.xml:/Waybill/cbc:IssueTime` = `10:43:00`
- Why: The status report is issued on 2026-05-13 at 10:05 and refers to waybill KXL-WB-26-0325,
  which the carrier issues on the same day at 10:43 (both parties at TimezoneOffset −1). A document
  cannot cite a document that does not yet exist. Accepting cargo before the air waybill is issued is
  normal (the carrier issues the AWB on acceptance), so the report may precede the waybill, but then
  it cannot carry its number.
- Condition: the report is issued after the waybill it refers to, or it refers only to identifiers
  that exist at its issue time (e.g. the consignment LD-CS-26-0324 or the booking).
- Options: issue the report after 10:43 (preferred, the event date stays 2026-05-13); or drop the
  reference and identify the cargo by consignment and shipping order.
- Needs decision: no

### air/05#F2 · High · ShippingOrderID holds the consignment ID
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- Why: ShippingOrderID is "A reference number for a shipping order". The forwarding instructions
  air/03 give the shipping order LD-SH-26-0323; the value here is the consignment ID, which the
  report already gives in Consignment/ID. The same value is in air/04 and air/09.
- Condition: ShippingOrderID is LD-SH-26-0323 (or absent).
- Options: LD-SH-26-0323 (preferred); or drop it, as the consignment ID identifies the cargo.
- Needs decision: no

### air/05#F3 · Medium · Acceptance and build-up reported as a generic event instead of the stage's acceptance event
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Cargo accepted and built up for the flight.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cbc:ID` = `1`
- Why: TransportationStatus/TransportEvent is for "Any additional events … that are not defined
  elsewhere in this document". ShipmentStage has AcceptanceTransportEvent for exactly this (UBL 2.5
  model), and the report already has the main-carriage stage at Lumeport, so the dedicated element
  exists. As a document-level event without TransportEventTypeCode it is tied to no stage and
  carries its meaning only as free text; two events (acceptance and build-up) are folded into one.
- Condition: the acceptance is in the main-carriage stage's AcceptanceTransportEvent (with date,
  time and location); any build-up event that remains has a type code.
- Options: AcceptanceTransportEvent in the stage (preferred); or keep the document-level event with
  a TransportEventTypeCode.
- Needs decision: no

### air/05#F4 · Low · The event has no time, although the report is issued the same morning
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13`
- Why: An automatic tracking report gives the time of acceptance; without it the reader cannot tell
  whether the acceptance was before the cut-off (air/03 has an untyped event at 2026-05-13 19:00) or
  relate it to the despatch advice air/06 issued at 10:07.
- Condition: the acceptance event has an OccurrenceTime before the report's issue time.
- Options: add the time (preferred).
- Needs decision: no

### air/05#F5 · Low · Status location is the company name, not the place
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Lumeport airport, cargo terminal`
- Why: Location/Name is "The name of this location"; the status location carries the operator's
  company name, and neither location has the UN/LOCODE XBLMA that the terminal's physical location in
  the same report has.
- Condition: both locations name the place and carry XBLMA (schemeID UN/LOCODE).
- Options: add the identifier and use the place name (preferred).
- Needs decision: no

### air/05#F6 · Low · An instruction about a delivery slot sent by the origin terminal to the carrier
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- Why: The report is from the origin cargo terminal to the airline about acceptance; no document of
  the flow gives a delivery slot (a time window at the destination), and neither party of this
  report delivers to the consignee. The instruction has nothing to refer to.
- Condition: the instruction refers to something the report or a referenced document states, or it is
  not there.
- Options: drop it (preferred); or state the slot it refers to.
- Needs decision: no

## Checked and consistent
- `DocumentReference/ID` KXL-WB-26-0325 resolves to air/04-Waybill.xml (an air waybill of the same
  consignment LD-CS-26-0324 and carrier Kelaro Air Cargo); see F1 for its timing.
- Terminal operator location XBLMA agrees with the waybill's loading airport.
- TransportExecutionStatusCode INPROGRESS fits cargo accepted for a flight not yet flown.
- StatusPeriod 2026-05-13 agrees with the event date.

## Outside this review
- The despatch advice air/06 is issued at 10:07, two minutes after the cargo is reported accepted at
  the airport; whether the goods were despatched from Marrowdale in time is a timeline question.
