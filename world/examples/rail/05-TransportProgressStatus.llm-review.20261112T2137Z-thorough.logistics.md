# LLM review: 05-TransportProgressStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

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

### rail/05#F1 · High · "Actual" departure after the time of the report, reported as on time although 7 minutes late
- XPath: `/TransportProgressStatus/cbc:IssueTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cbc:ReferenceTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:PlannedDepartureTransportEvent/cbc:OccurrenceTime` = `06:45:00`
- XPath: `/TransportProgressStatus/cbc:Note[2]` = `Left on time.`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cbc:Remarks` = `On time.`
- Why: ActualDepartureTransportEvent is "the actual departure from a location". The report is issued at 06:45 with a reference time of 06:45 and reports an actual departure at 06:52 on the same day, seven minutes in the future. The note says the train left on time, but the departure it reports is seven minutes after the planned 06:45 (and two minutes after the estimate 06:50). The waybill confirms the departure at 06:52 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`).
- Condition: Every actual event lies at or before the issue time (and the reference time) of the report, and the note and remarks agree with the reported times.
- Options: (a) preferred: issue the report after the departure (e.g. 06:55, and the request rail/04 at or after the planned departure), with remarks saying the train left 7 minutes late or within the punctuality tolerance; (b) keep 06:45 and report no actual departure yet (status "ready, departure expected 06:50").
- Needs decision: no

### rail/05#F2 · High · One status location with an actual arrival today and planned/estimated arrivals tomorrow
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `05:30:00`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- XPath: `/TransportProgressStatus/cac:TransportSchedule/cac:PlannedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-04-15`
- Why: TransportSchedule "describes the status and schedule of the transport means … as well as the current location", and its StatusLocation is "the location for which status is reported"; its events are, by their definitions, "the actual arrival at a location", "an estimated arrival at a specified location", "the planned arrival at a specified location". For the one status location, the Ferrano hub, the schedule thus reports that the train arrived at 05:30 on 2026-04-14 and is planned and estimated to arrive on 2026-04-15 at 10:30 / 10:40. The 2026-04-15 times are the arrival in Marrowdale (rail/03), a different location, which this schedule does not name.
- Condition: All events of a TransportSchedule refer to its StatusLocation; arrival times at Marrowdale are in a schedule whose status location is Marrowdale (or the Lumeway siding).
- Options: (a) preferred: a second `cac:TransportSchedule` (SequenceNumeric 2) with StatusLocation Marrowdale for the planned and estimated arrival, keeping the hub schedule for the actual arrival and departure; (b) drop the 2026-04-15 arrival events from the hub schedule.
- Needs decision: no

## Checked and consistent
- The report references the request rail/04 (FRC-DOC-26-0329), answers 15 minutes after it, for the same journey CT 4471 and status location.
- Planned departure 06:45, estimated departure 06:50, planned arrival 2026-04-15 10:30 and estimated arrival 10:40 equal the plan (rail/03) and the waybill (rail/08).
- Actual arrival of the train at the hub at 05:30 is before the loading of the containers at 05:40 recorded in the waybill (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingTransportEvent/cbc:OccurrenceTime` = `05:40:00`) and before the departure: consistent order of events.

## Considered and refuted
- `/TransportProgressStatus/cac:TransportSchedule/cbc:ReliabilityPercent` = `95`: a reliability of 95 % for a status that includes an actual (past) event seemed odd — refuted: the reliability can apply to the estimates the schedule carries.
- `/TransportProgressStatus/cac:TransportMeans/cbc:JourneyID` = `CT 4471`: the train run is identified only by its timetable service — refuted here, the response mirrors the request; raised for the request in rail/04.
