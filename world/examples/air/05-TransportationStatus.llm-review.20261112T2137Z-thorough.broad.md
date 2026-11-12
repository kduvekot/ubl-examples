# LLM review: 05-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### air/05#F1 · High · The report refers to a waybill that is issued only later
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `KXL-WB-26-0325`
- XPath: `/TransportationStatus/cbc:IssueTime` = `10:05:00`
- XPath: `04-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-05-13`
- XPath: `04-Waybill.xml:/Waybill/cbc:IssueTime` = `10:43:00`
- Why: This status report was issued on 13 May at 10:05 and cites the air waybill `KXL-WB-26-0325`. That waybill was issued on the same day at 10:43 (both parties at UTC−1), 38 minutes later. A document cannot refer to a waybill that does not exist yet.
- Condition: the waybill's issue time is before the issue time of every document that refers to it.
- Options: (a) issue the status report after the waybill, e.g. acceptance at the terminal after 10:43 (preferred: in air cargo the waybill is completed at acceptance); (b) issue the waybill earlier. Either way, check `06-DespatchAdvice.xml` (10:07) against the same sequence.
- Needs decision: no

### air/05#F2 · High · ShippingOrderID holds the consignment ID
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- Why: ShippingOrderID is "A reference number for a shipping order". The value is the consignment's ID, while the shipping order of this shipment is `LD-SH-26-0323` according to the forwarding instructions. One kind of identifier is used as another, and it contradicts 03.
- Condition: ShippingOrderID holds the same shipping order identifier as `03-ForwardingInstructions.xml`, or is absent.
- Options: (a) `LD-SH-26-0323` (preferred); (b) remove it, since the consignment ID already identifies the cargo.
- Needs decision: no

### air/05#F3 · Medium · LocaleCode holds a language code
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code (213 example files).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### air/05#F4 · Low · Acceptance event without time or type, and a status location named after the company
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Cargo accepted and built up for the flight.`
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Lumeport airport, cargo terminal`
- Why: The one event this report exists for has only a date and a text: no time, no TransportEventTypeCode. The acceptance cannot be placed before the flight cut-off. The status location carries the operator's company name, while the event's location names the place. The terminal's PhysicalLocation (`XBLMA`, coordinates) identifies the place properly.
- Condition: the event has a time and a type code, and the status location names or identifies the place, consistent with the event location.
- Options: add OccurrenceTime and a type code for acceptance; use "Lumeport airport, cargo terminal" with `XBLMA` as StatusLocation.
- Needs decision: no

### air/05#F5 · Low · The carrier's contact does not match its name
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations`
- Why: A "Cargo sales" contact who is an operations planner in Operations. Name and title disagree (the same in 8 example files). For a status report an operations contact fits, so the name is the odd part.
- Condition: name, job title and department agree.
- Options: rename the contact (e.g. "Cargo operations").
- Needs decision: no

## Checked and consistent
- Consignment `LD-CS-26-0324` and the carrier Kelaro (`IC41311`) match `04-Waybill.xml`. The terminal operator `20412055` at `XBLMA` is the loading airport of the waybill's main carriage stage.
- Coordinates 39°59.40′ S, 15°16.20′ W, with minutes below 60 and directions set, are the same as wherever else `XBLMA` is given (only here).
- Sender (the terminal) and receiver (the carrier) fit a handling agent's report to the airline it handles for.

## Considered and refuted
- `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`: suspected to be meaningless from terminal to airline. Refuted because the terminal books the slot for delivering the built-up unit to the aircraft, and the airline can change it.
- `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Airfield Road`: tagged `en-XB` here, `en-XL` in `04-Waybill.xml`. Refuted because the tag follows the issuing party's English consistently across the examples (here a Bayvarran terminal).

## Outside this review
- Timeline: the terminal reports the cargo accepted at 10:05, while `06-DespatchAdvice.xml` (the shipper's despatch advice) is issued at 10:07 and `03-ForwardingInstructions.xml` requests despatch on 13 May. Whether the goods could be at the terminal by 10:05 is for the timeline review.
