# LLM review: 05-TransportProgressStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/05-TransportProgressStatus.xml`, Git blob `973a4b0e2c9db9dec81b3d925185e8a004dcb691` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 0cafa9c 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### rail/05#F1 · High · Actual departure after the time of the report, and "on time" seven minutes late
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`
- XPath: `/TransportProgressStatus/cbc:IssueTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cbc:ReferenceTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cbc:Note[2]` = `Left on time.`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cbc:Remarks` = `On time.`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`
- Why: ActualDepartureTransportEvent is "The actual departure from a location". The report, issued and referenced at 06:45 on 14 April, states an actual departure at 06:52 the same day, seven minutes in the future. It also says the train "Left on time", whereas the planned departure is 06:45, so 06:52 is seven minutes late (and two minutes after the estimate of 06:50). The waybill records the same actual departure at 06:52 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`).
- Condition: Every actual event lies at or before the issue and reference time, and the remarks agree with planned and actual times.
- Options: (a) preferred: issue the report after the departure (e.g. 06:55), with remarks such as "Left 7 minutes late" or a tolerance that makes 06:52 "on time" stated; (b) at 06:45, report only the estimate and no actual departure.
- Needs decision: no

### rail/05#F2 · Medium · Arrival events of two different places under one status location
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:PlannedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- Why: StatusLocation is "The location for which status is reported", and the events carry no location of their own, so all of them read as events at the hub. The actual arrival (14 April 05:30) is the train's arrival at the hub, but the planned and estimated arrivals (15 April 10:30 and 10:40) are those at Marrowdale, as in the plan (03). Read as written, the train is planned to arrive at the hub a day after it actually did.
- Condition: Each event is attributable to its place: either the schedule reports only events at its status location, or events at other places carry their own Location (or are in a second TransportSchedule for Marrowdale).
- Options: (a) preferred: a second TransportSchedule with StatusLocation Marrowdale for the planned and estimated arrival; (b) give the arrival events at Marrowdale a Location.
- Needs decision: no

### rail/05#F3 · Medium · Province given in Region
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division (CountrySubentity). 219 occurrences over the examples.
- Condition: The province is in CountrySubentity, or the world defines it as a non-administrative region.
- Options: (a) preferred: CountrySubentity; (b) keep Region if provinces are not administrative.
- Needs decision: yes (a fact of the world)

### rail/05#F4 · Low · Terminal control reachable only in office hours
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:Contact/cbc:Name` = `Terminal control`
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The hub's terminal control reports on a train that arrived at 05:30 and left before 07:00; availability on weekdays from 08:00 to 17:00 does not fit a terminal control that works these hours.
- Condition: The stated availability covers the hours in which the terminal control acts in the flow.
- Options: (a) preferred: the hub's real operating hours; (b) drop the Note.
- Needs decision: no

## Checked and consistent
- Reference: `FRC-DOC-26-0329` resolves to 04 (TransportProgressStatusRequest from Ferrano Rail Cargo to the hub); this answer goes from the hub back to the carrier, about the same journey CT 4471 and the same status location.
- Planned departure 06:45, planned arrival 15 April 10:30, estimated departure 06:50 and estimated arrival 10:40 equal the plan (03) and the waybill (08).
- Sequence at the hub: arrival 05:30, loading of the two containers at 05:40 (07, 08), departure 06:52: in order.
- SourceIssuerParty = SenderParty (the hub issues the status it sends) is consistent; StatusAvailableIndicator true agrees with the schedule reported.

## Considered and refuted
- `/TransportProgressStatus/cac:TransportSchedule/cbc:ReliabilityPercent` = `95`: suspected meaningless next to actual events — refuted because the reliability applies to the estimates in the same schedule (arrival at Marrowdale), which are still uncertain.
- `/TransportProgressStatus/cac:SourceIssuerParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`: suspected a redundant repetition of the sender — refuted because the element states who originates the status information, which need not be the sender; stating it when they coincide is harmless.
