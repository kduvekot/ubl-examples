# LLM review: 16-CommonTransportationReport.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/16-CommonTransportationReport.xml`, Git blob `fcbb7ae1a07ebdd8f8e779b15a6991056933bf53` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/16#F1 · High · The ship is reported at two different positions at the same time
- XPath: `/CommonTransportationReport/cac:ReportingLocation/cbc:Name` = `At sea, 40 nautical miles off Selanu`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ReportLocation/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:PlaceOfReportLocation/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- Why: ReportingLocation is "a location to which this common transportation report applies"; the
  ISPS part and the health declaration are parts of the same report, issued once
  (2026-05-16 15:38), and give "the location where these … are reported" as 120 nm west of Selanu.
  The ship cannot be 40 nm and 120 nm off Selanu when the one report is made. At the stated
  13.5 knots the two positions are about 6 hours apart (80 nm / 13.5 kn = 5.9 h).
- Condition: every report location in the document gives the same position, or the parts that
  were reported at another time say so (with that time).
- Options: (a, preferred) one position for the whole report, chosen to fit the arrival time and
  speed (see F2); (b) keep separate positions only if the ISPS and health parts are dated
  separately.
- Needs decision: no

### sea/16#F2 · High · Position, speed and requested arrival do not fit together
- XPath: `/CommonTransportationReport/cbc:IssueDate` = `2026-05-16`
- XPath: `/CommonTransportationReport/cbc:IssueTime` = `15:38:00`
- XPath: `/CommonTransportationReport/cac:ReportingLocation/cbc:Name` = `At sea, 40 nautical miles off Selanu`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:VesselDynamics/cbc:SpeedOverGroundMeasure` = `13.5`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceDate` = `2026-05-18`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceTime` = `06:00:00`
- Why: calculated: from 2026-05-16 15:38 to 2026-05-18 06:00 is 38.4 h. At 13.5 knots the ship
  covers 40 nm in 3.0 h and 120 nm in 8.9 h, so it would reach the fairway buoy on 2026-05-16 at
  about 18:40 (from 40 nm) or about 00:30 on 2026-05-17 (from 120 nm); to arrive at 06:00 on the
  18th it would have to average 1.0 kn (40 nm) or 3.1 kn (120 nm). The note says the ship "berths
  without anchoring" and ExpectedAnchorageIndicator is false, so it cannot wait at anchor either.
  The actual arrival in `17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `06:30:00`
  (2026-05-18) confirms the arrival time, so the position, the speed or the issue time is what
  does not fit.
- Condition: distance to Selanu ÷ speed over ground ≈ time from the issue time to the requested
  arrival (allowing for a slow approach), or the document explains the waiting time.
- Options: (a, preferred) issue the report about 3–9 hours before arrival (e.g. on 2026-05-17
  evening) with a matching position, which is also when a pre-arrival report with a 40 nm position
  is typically sent; (b) keep the date and put the ship much further away at a speed that fits;
  (c) keep everything and state a slow-steaming speed and a reason.
- Needs decision: no

### sea/16#F3 · High · Ballast exchange "more than 200 nautical miles from land" took place 120 nm from Selanu
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:NoControlActionsReason` = `Exchange done at more than 200 nautical miles from land.`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cac:Location/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- Why: the only exchange recorded (tank BT-3, 2026-05-16) is located 120 nm from Selanu, i.e. from
  land on Lisavu, so "more than 200 nautical miles from land" is false by the document's own
  location (own knowledge: the BWM Convention D-1 standard asks for at least 200 nm from the
  nearest land, or at least 50 nm where that is not possible, so the distance is exactly what an
  authority checks). Besides, NoControlActionsReason is "the reason if no control actions are
  being taken", while OtherControlActions in the same summary describes a control action
  (sediment flushed), so the reason also stands next to a statement that actions were taken.
- Condition: the stated distance from land of the exchange agrees with its location; the summary
  does not give a reason for "no control actions" while it records control actions.
- Options: (a, preferred) put the exchange location where the stated distance holds (and fit it to
  F2), or state the 50 nm alternative with its reason; (b) remove the distance claim.
- Needs decision: no

### sea/16#F4 · High · The coordinates put the Lumeport anchorage 3 nm from the Port of Selanu
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cbc:Name` = `Lumeport anchorage`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `1.20`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `1.20`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`
- Why: calculated: both points lie at 40°01.20'S; the anchorage is at 15°12.60'W, Selanu at
  15°08.40'W, a difference of 4.2' of longitude, which at 40° latitude is 4.2 × cos 40° = 3.2 nm.
  The same document describes a voyage of several days between the two ports, an exchange
  "120 nautical miles west of Selanu" and a bunkering in another country's anchorage. The
  anchorage coordinates are moreover exactly those of the Lumeport container quay in
  `13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`,
  so an anchorage and a quay share one point.
- Condition: the coordinates of the anchorage and of the Port of Selanu are at a distance that
  agrees with the voyage the document describes, and the anchorage is not at the quay's position.
- Options: (a) give real-scale coordinates for the ports and the anchorage; (b, if the world's
  map deliberately uses compressed coordinates) drop the coordinates where they contradict the
  stated distances, or state distances that fit the map. Which one depends on how the world's map
  scale is meant to be read.
- Needs decision: yes (how the world's coordinates relate to its sea distances)

### sea/16#F5 · Low · The sea stage is numbered 1 here and 2 in the other documents of the shipment
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/CommonTransportationReport/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- Why: the report names shipment LD-SH-26-0132; in every other document of that shipment the
  sea voyage Lumeport–Selanu is stage 2 (pre-carriage by road is 1, on-carriage 3):
  `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:ID` = `2`,
  `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cbc:ID` = `2`. ShipmentStage/ID is
  "an identifier for this shipment stage", so the same stage of the same shipment should have the
  same identifier.
- Condition: the sea stage of LD-SH-26-0132 has the same ID in this report as in 14 and 15.
- Options: (a, preferred) ID 2; (b) if the report is meant to describe the vessel's voyage rather
  than this shipment, say so (e.g. through the journey ID only) instead of reusing the shipment's
  stage.
- Needs decision: no

### sea/16#F6 · Low · Crew list of three for a ship with a crew of fourteen
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[1]/cbc:RoleCode` = `MASTER`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[3]/cbc:RoleCode` = `CHIEFENG`
- Why: the referenced manifest states
  `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14` for the same
  voyage TH-26-19E. A pre-arrival report to the maritime administration that lists crew members
  normally lists all of them (FAL Form 5); three named crew read as the complete crew.
- Condition: either all crew are listed, or the report states the crew total (CrewQuantity) so
  the three names are not read as the whole crew.
- Options: (a, preferred) add CrewQuantity 14 to the stage; (b) list all fourteen.
- Needs decision: no

### sea/16#F7 · Low · Ship security officer coded differently in the same report
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:RoleCode` = `SSO`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:SecurityOfficerPerson/cbc:RoleCode` = `CHIEFOFFICER`
- Why: the same person (Elsbeth Marrin) is the security officer in both places; once with the role
  code "Ship security officer", once with "Chief officer". In SecurityOfficerPerson the role code
  should give the security role, as the stage-level entry does.
- Condition: both SecurityOfficerPerson entries carry the same role code, the security role.
- Options: SSO in both (preferred).
- Needs decision: no

### sea/16#F8 · Low · INF ship class declared on a voyage without INF cargo
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:INFShipClassCode` = `INF1`
- Why: the INF ship class matters to an authority only when the ship carries packaged irradiated
  nuclear fuel, plutonium or high-level radioactive waste (own knowledge of the IMO INF Code). The
  referenced manifest declares one container of park benches for Selanu, and nothing in the flow
  carries such cargo. Present without a reason in this voyage (IND5).
- Condition: INFShipClassCode is present only if the voyage carries INF cargo.
- Options: (a, preferred) remove it; (b) keep it only with INF cargo in the world.
- Needs decision: no

### sea/16#F9 · Low · Planned ballast discharge without a place
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:DischargeBallastWaterTransaction/cbc:VolumeMeasure` = `120`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:DischargeBallastWaterTransaction/cbc:TransactionDate` = `2026-05-18`
- Why: the uptake and the exchange carry a location, the discharge does not. For the port state the
  place of discharge (in the port of Selanu, at the berth) is the point of reporting it.
- Condition: the discharge transaction has a location.
- Options: add the Selanu location (XLSEL).
- Needs decision: no

## Checked and consistent
- Reference `/CommonTransportationReport/cac:DocumentReference/cbc:ID` = `TOL-MF-26-0140` resolves to
  15-Manifest.xml (same voyage TH-26-19E, vessel XB-S-20117, one container for Selanu, matching
  "Discharge one container").
- Vessel data equal to 14 and 15: vessel ID, name, call sign, MMSI, GT 9940, NT 5120 (ratio 0.52,
  plausible), segregated ballast 2480 t = TotalBallastWaterCapacityMeasure 2480 t; type 1511 and
  configuration FEEDER agree; course 088 fits the eastbound direction code.
- Ballast: 8 tanks, 4 in ballast, 4 exchanged, 0 not exchanged (4 + 0 = 4); 1240 t on board =
  4 × 310 (tank BT-3 holds 310 m³ ≈ 318 t of sea water at 1.025 t/m³; close enough for a summary);
  uptake at Lumeport on 2026-05-14 lies within the Lumeport port call record 2026-05-13 to
  2026-05-14; exchange 95 % fits the sequential method; discharge 120 m³ ≤ 310 m³.
- Fuel: 38 t MGO × 3.206 t CO2/t (IMO emission factor for MGO, own knowledge) = 121.8 t ≈ 122 t
  CO2e; flow meter 38.2 t agrees with 38 t; 38 t ≤ the 120 t bunkered; for a ~10 000 GT feeder at
  13.5 kn about 15–20 t/day, 38 t corresponds to roughly two days at sea, plausible.
- Waste: retained 0.6 m³ + expected 0.8 m³ until next port = 1.4 m³ ≤ 8 m³ dedicated storage.
- ISPS: ISSC issued 2023, expiry 2028-09-30 (five-year term); bunkering period 05:40–08:15 on
  2026-05-13 lies within the Lumeport port call.
- Requested arrival 2026-05-18 06:00 agrees with the actual arrival 06:30 in 17-TransportationStatus.xml.

## Considered and refuted
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cbc:ID` = `XLSEL-26-0517`: the "0517" looked like 17 May while the
  arrival is on the 18th — refuted because the ID is an opaque number assigned by the port; nothing
  says it encodes a date.
- `/CommonTransportationReport/cac:Shipment/cbc:ID` = `LD-SH-26-0132`: a ship-level report hung on one
  cargo shipment looked like the wrong kind of identifier — refuted as a finding of its own because
  UBL 2.5 places crew, ballast, waste and port call under Shipment/ShipmentStage, and the shipment is
  the one the referenced manifest declares; only the stage number is inconsistent (F5).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:DischargeBallastWaterTransaction/cbc:TransactionDate` = `2026-05-18`:
  a date after the issue date — refuted because a pre-arrival ballast report declares the planned
  discharge.
- `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:MMSIRegistrationID` = `298702117`:
  could not be checked against the ITU MID table (no source in the repository); not raised.

## Outside this review
- The referenced manifest gives
  `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceTime` = `22:00:00`
  on 2026-05-17 and an estimated departure on 2026-05-15 06:00, while 13-TransportationStatus.xml
  reports the actual departure on 2026-05-14 18:10 and this report requests arrival on 2026-05-18
  06:00 with status "On time": a timeline question across documents.
