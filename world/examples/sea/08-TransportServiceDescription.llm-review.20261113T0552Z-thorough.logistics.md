# LLM review: 08-TransportServiceDescription.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/08-TransportServiceDescription.xml`, Git blob `3b64d9a508af69f9f2be5711a0061f17a39e8741` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/08#F1 · High · Booking deadline lies before the offer is issued, and the booking comes after it
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:NominationDate` = `2026-05-09`
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:NominationTime` = `10:00:00`
- XPath: `/TransportServiceDescription/cbc:IssueTime` = `12:03:00`
- Why: `NominationDate` is "In a transport contract, the deadline date by which this transportation service has to be booked". The deadline (2026-05-09 10:00) has passed two hours before the description is issued (2026-05-09 12:03), so the service is offered with a booking window that is already closed. The booking itself is the forwarder's instruction to the carrier, issued the next morning (`12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:IssueDate` = `2026-05-10`, 09:15), after the deadline, and yet the carrier accepts it (booking number `TWL-BK-26-55710` on the bill of lading).
- Condition: the nomination deadline lies after the issue of the description and no earlier than the booking in `12-ForwardingInstructions.xml`, and before the sailing it is for.
- Options: a deadline between the booking (2026-05-10 09:15) and the sailing (2026-05-14), e.g. 2026-05-12 (preferred: typical cut-off two days before sailing); or drop the nomination date.
- Needs decision: no

### sea/08#F2 · High · Weekly sailing day is Friday, the sailing in the same document is on a Thursday
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:ScheduledServiceFrequency/cbc:WeekDayCode` = `5`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: `ScheduledServiceFrequency/WeekDayCode` `5` is Friday. The only event of the service is on 2026-05-14 at 18:00, which is a Thursday (calculated with Python's `datetime`), and the vessel actually leaves Lumeport on Thursday 2026-05-14 at 18:10 (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`).
- Condition: the scheduled weekday and the dated sailing(s) agree.
- Options: `WeekDayCode` `4` (Thursday) (preferred: matches the event and the actual departure); or move the sailing to a Friday, which changes the dates of the bill of lading, status and manifest.
- Needs decision: no

### sea/08#F3 · High · "Two days at sea" between ports that the flow places 3.2 nautical miles apart
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2`
- XPath: `/TransportServiceDescription/cac:TransportationService/cbc:TransportationServiceDescription` = `A weekly feeder sailing from Lumeport to Selanu, two days at sea.`
- Why: the service takes two days between Lumeport and Selanu. The flow gives both ports coordinates: Lumeport's container quay at 40°1.20′ S 15°12.60′ W (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`) and the port of Selanu at 40°1.20′ S 15°8.40′ W (`17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`, the same in `16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`). On the same latitude, 4.2′ of longitude at 40° S is 4.2 × cos 40° = 3.2 nautical miles (calculated). A feeder at 12–15 knots covers that in about 15 minutes, not two days; the common transportation report places the ship "120 nautical miles west of Selanu" during the passage, about 117 nautical miles beyond Lumeport on the line between the two ports.
- Condition: the duration of the passage, the distances stated in the flow and the coordinates of the two ports are consistent with each other.
- Options: keep two days and correct the port coordinates to positions about 600–700 nautical miles apart (preferred if the map's scale allows: the duration recurs in the manifest's estimated departure and arrival and in the report); or keep the coordinates and shorten the passage, which changes the voyage in several documents. Which one is right depends on the world's map scale.
- Needs decision: yes

### sea/08#F4 · Medium · Transport event without type or place
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:CompletionIndicator` = `false`
- Why: `TransportationService/TransportEvent` is "One or more transport events taking place in this transportation service". The event has a date, time 18:00 and a completion indicator, but no `TransportEventTypeCode`, no description and no location, so a receiver cannot tell whether 18:00 on 14 May is a departure, a cut-off, an arrival or a gate closing. The flow's later documents suggest the departure from Lumeport (actual 18:10).
- Condition: the event says what it is (type code or description) and where it takes place.
- Options: type "departure" with location `XBLMP` (preferred); or express the sailing through the service's shipment stage with an estimated departure event.
- Needs decision: no

### sea/08#F5 · Low · Shipment stage of the service without ports; route only in free text
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:ShipmentStage/cbc:TransportModeCode` = `1`
- Why: the service's single stage gives only a mode; the route Lumeport–Selanu is in `Name` and `TransportationServiceDescription` only, although both ports are identified elsewhere in the flow by LOCODE (`XBLMP`, `XLSEL` in `14-BillOfLading.xml`).
- Condition: the stage carries its loading and unloading ports.
- Options: add `LoadingPortLocation` `XBLMP` and `UnloadingPortLocation` `XLSEL` (preferred).
- Needs decision: no

### sea/08#F6 · Low · Emission of the service without its basis
- XPath: `/TransportServiceDescription/cac:TransportationService/cac:EnvironmentalEmission/cbc:ValueMeasure` = `380`
- Why: "An environmental emission resulting from this transportation service" of 380 kg CO2e, with no base (per container, per TEU, per tonne, per sailing) and no calculation method. For a whole feeder sailing of two days, 380 kg is far too little (a 1,000 TEU feeder burns roughly 15–25 t of fuel a day, about 3.2 t CO2 per tonne of fuel, own knowledge); per 40-foot box it is plausible: 7.9 t gross over two days at about 13 knots (about 1,150 km) gives 380 / (7.9 × 1,150) ≈ 42 g CO2e per tonne-km, at the high end for a feeder (own knowledge: 15–40 g). As it stands, the figure cannot be read.
- Condition: the emission states what it refers to (e.g. `ValueBaseMeasure` per container, with the method), so that it can be checked.
- Options: add base "1 container 40 ft" and the calculation method (preferred); or drop the emission.
- Needs decision: no

## Checked and consistent
- Capacity: 1,000 TEU (`TotalCapacityDimension`, unit `20` twenty-foot container) for an "Island feeder"; the vessel named on the bill of lading has gross tonnage 9,940 and net tonnage 5,120 (`14-BillOfLading.xml`), consistent with real feeders of about 1,000 TEU (about 9,900–10,000 GT, own knowledge).
- Equipment: the offered `42G1` is among the supported types and is the container type on the bill of lading and manifest; the refrigerated `45R1` is unsupported, consistent with "Freight all kinds" general cargo.
- The request reference `LD-DOC-26-0129` resolves to `07-TransportServiceDescriptionRequest.xml`; validity 2026-05-09 to 2026-08-07 covers the sailing of 2026-05-14.
