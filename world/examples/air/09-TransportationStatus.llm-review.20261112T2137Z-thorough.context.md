# LLM review: 09-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### air/09#F1 · High · Arrival on 14 May contradicts the cancellation's "next day's flight"
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- Why: Five minutes before this report (14 May 17:53), the seller cancels its despatch advice because the cargo missed its flight (booked for 14 May 07:00 in 04-Waybill.xml) and goes on the next day's flight, i.e. 15 May. This report says the cargo arrived at Selanu on 14 May. The two statements about the same consignment LD-CS-26-0324 contradict each other.
- Condition: the arrival date and the reason for the cancellation agree.
- Options: (preferred) settle the story once (a later flight on 14 May, and the cancellation worded so), keeping this report; or move the arrival to 15 May.
- Needs decision: yes (when the cargo flew)

### air/09#F2 · High · Shipping order ID holds the consignment ID and contradicts the forwarding instructions
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- Why: ShippingOrderID is "A reference number for a shipping order". The value is the consignment ID (also in Consignment/ID); the forwarding instructions give LD-SH-26-0323 as the shipping order. An identifier of one kind used as another.
- Condition: ShippingOrderID equals the shipping order (or forwarding instruction) ID used in 03-ForwardingInstructions.xml and 04-Waybill.xml, or is absent.
- Options: (preferred) the value the waybill uses once fixed (LD-FI-26-0322); or drop it.
- Needs decision: no

### air/09#F3 · Medium · Arrival reported as a generic event without time, where a dedicated event exists
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- Why: TransportationStatus/TransportEvent is for events "not defined elsewhere in this document". The arrival is defined: the report has a main-carriage stage, and ShipmentStage has ActualArrivalTransportEvent (and AvailabilityTransportEvent for "ready"). The generic event has neither time nor TransportEventTypeCode, so the status the report exists to give (when the cargo arrived and became available) is only in free text and to the day.
- Condition: the arrival is in the dedicated event of the main-carriage stage, with date, time and location (and availability for clearance where meant).
- Options: (preferred) `MainCarriageShipmentStage/ActualArrivalTransportEvent` with date, time and Selanu airport (XLSLA); or keep the generic event with a type code and time.
- Needs decision: no

### air/09#F4 · Medium · LocaleCode holds a language code
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language and repeats Language/ID. 362 such elements over `world/examples/*/*.xml` (grep).
- Condition: LocaleCode holds a locale, or is absent.
- Options: (preferred) drop it; or a real locale code with a locale list.
- Needs decision: no

### air/09#F5 · Low · Status location named after the company
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Selanu Airport Cargo`
- Why: StatusLocation is one of the "Locations associated with this Transportation Status report"; the name is the party name of the sender and terminal operator, while the event location is `Selanu airport, cargo terminal` and the waybill identifies the airport as XLSLA. The place is named after a company.
- Condition: the status location is named as a place and, where possible, identified (XLSLA), consistently with the event location.
- Options: (preferred) one location `Selanu airport, cargo terminal` with ID XLSLA; or drop StatusLocation.
- Needs decision: no

### air/09#F6 · Low · Signature aggregate without a signature
- XPath: `/TransportationStatus/cac:Signature/cbc:ID` = `SAC-SIG-TS-09`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with no method, attachment or extension, in an automatic tracking report (Note[2]). 131 of 133 Signature aggregates over `world/examples/*/*.xml` are like this (lxml count).
- Condition: either a verifiable signature or no Signature aggregate.
- Options: (preferred) drop it.
- Needs decision: yes (a convention across many examples)

## Checked and consistent
- DocumentReference KXL-WB-26-0325 resolves to 04-Waybill.xml, issued before this report; consignment, consignee and carrier agree with it.
- The sender Selanu Airport Cargo is the party to which the waybill's consignee original travels with the goods (`04-Waybill.xml:/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`); reporting to the forwarder fits.
- TransportExecutionStatusCode `INPROGRESS` fits cargo arrived but not yet delivered; the OtherInstruction about the delivery slot fits a destination handler arranging delivery.
