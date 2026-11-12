# LLM review: 05-TransportProgressStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/05-TransportProgressStatus.xml`, Git blob `973a4b0e2c9db9dec81b3d925185e8a004dcb691` (committed)
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

### rail/05#F1 · High · Actual departure after the time of the report
- XPath: `/TransportProgressStatus/cbc:IssueTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cbc:ReferenceTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`
- Why: ActualDepartureTransportEvent is "the actual departure from a location". A report issued at 06:45, with the status referring to 06:45, cannot report an actual departure at 06:52. The note "Left on time." also says the train has already left when the report is made.
- Condition: every actual event in the report lies at or before its reference and issue time.
- Options: (a) preferred: issue the report after 06:52 (and refer the status to that time); (b) report 06:52 as an estimate.
- Needs decision: no

### rail/05#F2 · Medium · Arrival events of another place under the hub's status location
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `05:30:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:PlannedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- Why: StatusLocation of a TransportSchedule is "the location for which status is reported", and the schedule's events are "arrival at a specified location". The actual arrival at 05:30 on 14 April is the train's arrival at the hub, but the estimated and planned arrivals (15 April 10:40 and 10:30) are the arrival in Marrowdale (see `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedArrivalTransportEvent/cbc:OccurrenceTime` = `10:30:00`). One schedule entry thus mixes two locations without saying so.
- Condition: each TransportSchedule entry has events of its own status location only (a second entry, sequence 2, for Marrowdale where its times are reported).
- Options: (a) preferred: a second TransportSchedule for Marrowdale with the planned and estimated arrival; (b) drop the Marrowdale arrivals.
- Needs decision: no

### rail/05#F3 · Medium · Province in Region
- XPath: `/TransportProgressStatus/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportProgressStatus/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: A province is an administrative division (CountrySubentity), not a Region.
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/05#F4 · Low · "On time" for a departure seven minutes late
- XPath: `/TransportProgressStatus/cbc:Note[2]` = `Left on time.`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cbc:Remarks` = `On time.`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`
- Why: The planned departure is 06:45 and the actual one 06:52. Whether seven minutes count as "on time" depends on a punctuality margin the document does not state; without one, the text and the times disagree.
- Condition: the remarks agree with the times (state the margin, or say "seven minutes late, within the slot").
- Options: (a) preferred: remarks that agree with the times; (b) move the actual departure to within the stated margin.
- Needs decision: no

### rail/05#F5 · Low · Sender is a terminal operator, the document comes from a network manager
- XPath: `/TransportProgressStatus/cac:SourceIssuerParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- Why: UBL defines the document as "sent from a Transportation Network Manager to a Transport Service Provider". The hub is a terminal operator; it can report departures from its yard, but it is not the network manager of the train's route (the estimated arrival in Marrowdale is outside its knowledge as a terminal).
- Condition: the issuer is the network manager, or the story says the hub reports for the network.
- Options: (a) preferred: state the hub's reporting role in the world; (b) a network manager as issuer.
- Needs decision: yes

## Checked and consistent
- The report answers the request: `/TransportProgressStatus/cac:TransportProgressStatusRequestDocumentReference/cbc:ID` = `FRC-DOC-26-0329` is rail/04; JourneyID CT 4471 matches.
- Planned departure 06:45, estimated 06:50 and planned arrival 10:30, estimated 10:40 agree with the plan rail/03.

## Considered and refuted
- `/TransportProgressStatus/cac:TransportSchedule/cbc:ReliabilityPercent` = `95`: suspected meaningless for a report of actual events — refuted because the schedule also carries estimates (arrival in Marrowdale), to which a reliability applies.
