# LLM review: 09-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

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
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:IssueTime` = `17:53:00`
- Why: Five minutes before this report (14 May 17:53), the seller's cancellation says the cargo missed its flight and goes on the next day's flight, i.e. 15 May. This report says the same consignment `LD-CS-26-0324` arrived at Selanu on 14 May. Both cannot be true.
- Condition: the arrival date reported here agrees with the flight the cargo actually took according to `07-FulfilmentCancellation.xml` and `04-Waybill.xml`.
- Options: as 07#F2 (preferred there: the missed flight was on 13 May, the cargo flew on 14 May, and this report stands).
- Needs decision: yes

### air/09#F2 · High · ShippingOrderID holds the consignment ID
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- Why: ShippingOrderID is "A reference number for a shipping order". The value is the consignment's ID. The shipping order of this shipment is `LD-SH-26-0323` according to the forwarding instructions.
- Condition: ShippingOrderID holds the same shipping order identifier as `03-ForwardingInstructions.xml`, or is absent.
- Options: (a) `LD-SH-26-0323`; (b) remove it (preferred: the forwarder knows the consignment ID).
- Needs decision: no

### air/09#F3 · Medium · The arrival is a generic event without time, while the stage has a dedicated arrival event
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Selanu airport, cargo terminal`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cbc:ID` = `1`
- Why: TransportationStatus/TransportEvent is for "additional events … that are not defined elsewhere in this document". An arrival has its own place: the main carriage stage's ActualArrivalTransportEvent, and the stage is already in the document. The event has only a date, no time and no type code, so the arrival cannot be placed against the 10:00 arrival of `04-Waybill.xml` or the cancellation at 17:53.
- Condition: the arrival is stated in the stage's actual arrival event with date, time and location; the readiness for customs may stay as an additional event or in the description.
- Options: MainCarriageShipmentStage/ActualArrivalTransportEvent with OccurrenceDate, OccurrenceTime and the Selanu airport location (`XLSLA`) (preferred).
- Needs decision: no

### air/09#F4 · Medium · LocaleCode holds a language code
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code (213 example files).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### air/09#F5 · Low · Status location named after the company
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Selanu Airport Cargo`
- Why: The location's name is the handling company's name (the TerminalOperatorParty). The place is "Selanu airport, cargo terminal", as the event location says, and `04-Waybill.xml` identifies it as `XLSLA`.
- Condition: the status location names or identifies the place, consistent with the event location.
- Options: "Selanu airport, cargo terminal" with `XLSLA`.
- Needs decision: no

### air/09#F6 · Low · Contacts do not fit their roles
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- Why: The consignee's contact, the one who should collect the arrived cargo, is "Purchasing", a customer service officer in Sales. The carrier's "Cargo sales" contact is an operations planner. Name and title disagree (52 and 8 example files).
- Condition: the contacts' names, titles and departments agree with each other and with the roles.
- Options: align names or titles.
- Needs decision: no

## Checked and consistent
- `KXL-WB-26-0325` resolves to `04-Waybill.xml`. Consignment `LD-CS-26-0324`, carrier Kelaro and consignee Velumi agree with it. Selanu Airport Cargo (`IC41174`) is the party the waybill sends the consignee's original to.
- The arrival date 14 May agrees with the waybill's flight on 14 May 07:00–10:00, and the report (17:58) is after it.
- Sending the arrival report to the forwarder Bayforth fits: it arranged the transport and is the waybill's receiver.

## Considered and refuted
- `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`: refuted, because the destination terminal books the delivery slot to the consignee and the forwarder may need to change it.
- `/TransportationStatus/cbc:TransportExecutionStatusCode` = `INPROGRESS`: on arrival. Refuted because delivery to the consignee and customs clearance are still open.

## Outside this review
- Customs: "ready for customs clearance" in Lisavu, but the air flow has no import declaration. Whether one belongs in the flow is a question about the flow's documents, not this report.
