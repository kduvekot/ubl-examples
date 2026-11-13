# LLM review: 16-CommonTransportationReport.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### sea/16#F1 · High · The ship's position, speed and arrival time contradict each other
- XPath: `/CommonTransportationReport/cac:ReportingLocation/cbc:Name` = `At sea, 40 nautical miles off Selanu`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ReportLocation/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:PlaceOfReportLocation/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:VesselDynamics/cbc:SpeedOverGroundMeasure` = `13.5`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceDate` = `2026-05-18`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceTime` = `06:00:00`
- Why: The report is one document issued at one moment (2026-05-16 15:38), but it gives two different places where it is reported: `ReportingLocation` ("A location to which this common transportation report applies") is 40 nm off Selanu, while the ISPS part and the health declaration, which are parts of this same report, are "reported" at 120 nm west of Selanu. Neither distance fits the rest: at the stated 13.5 knots under way (navigation status 0), 40 nm take about 3 hours and 120 nm about 9 hours, yet the requested arrival (pilot on board) is 2026-05-18 06:00, about 38 hours later; `17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `06:30:00` on 2026-05-18 confirms that arrival. Calculation: 40 nm / 13.5 kn = 3.0 h; 120 nm / 13.5 kn = 8.9 h; 2026-05-16 15:38 to 2026-05-18 06:00 = 38.4 h.
- Condition: Every place where the report says it is made names the same position, and that position, the speed over ground and the requested arrival are compatible (distance ÷ speed ≈ time to arrival, or a stated reason for the delay such as slow steaming or a waiting time).
- Options: (a) preferred: one reporting position for the whole report, with a distance and speed that fit the arrival on 2026-05-18 06:00; (b) issue the report closer to arrival (a pre-arrival report is typically sent 24 h ahead), which keeps the distances but moves the issue time; (c) keep the separate ISPS and health reporting places only if those parts are explained as having been completed earlier, which the elements do not allow to express cleanly.
- Needs decision: no

### sea/16#F2 · High · Reason for "no control actions" given although control actions are reported, and it contradicts the exchange position
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:NoControlActionsReason` = `Exchange done at more than 200 nautical miles from land.`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:OtherControlActions` = `Sediment flushed from the forepeak tank during the exchange and recorded in the ballast water record book.`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cac:Location/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- Why: `NoControlActionsReason` is "A textual description of the reason if no control actions are being taken". This summary reports control actions: a ballast exchange of tank BT-3 (`ExchangeBallastWaterTransaction`, 95 %, sequential) and other control actions (sediment flushing). The condition of the definition is therefore not met. The text also contradicts the exchange's own location: the exchange was done 120 nm west of Selanu, not "more than 200 nautical miles from land" (the 200 nm criterion is the one of the IMO Ballast Water Management Convention, regulation B-4, own knowledge). The text reads as a justification that the exchange was compliant, not a reason for having taken no action.
- Condition: `NoControlActionsReason` is present only when no control action is reported; any statement about where the exchange was made agrees with the exchange's location.
- Options: (a) preferred: remove `NoControlActionsReason`; if the compliance of the exchange position matters, state it where it fits (e.g. in the exchange transaction's location, giving a position that is in fact more than 200 nm from land); (b) if the story wants a case with no control actions, remove the exchange and `OtherControlActions` instead, which changes the story.
- Needs decision: no

### sea/16#F3 · Medium · Lumeport declared as a WHO affected area, with a visit date that does not match the last call there
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:WHOAffectedAreaVisit/cac:WHOAffectedAreaPortLocation/cbc:Name` = `Port of Lumeport`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:WHOAffectedAreaVisit/cbc:VisitDate` = `2026-03-28`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:PortCallRecord/cac:Period/cbc:StartDate` = `2026-05-13`
- Why: `WHOAffectedAreaVisit` is "A WHO Affected Area visit related to this maritime health declaration"; in the IHR Maritime Declaration of Health it answers whether the ship called at a port in an area the WHO has declared affected (own knowledge, IHR 2005 Annex 8). Putting Lumeport there states that the WHO considers Bayvarra's main port an affected area, which is a strong statement about the world that nothing else in this report supports: no infectious disease is on board, no one is more ill than expected, and the only health incident is a sprained wrist. The date is also odd: the ship's last call at Lumeport, according to the same report, was 2026-05-13 to 2026-05-14, so a visit to an affected Lumeport on 2026-03-28 would be followed by an unreported later visit to the same affected area.
- Condition: Either the report declares no WHO affected area visit, or the world has a reason for an affected area at the named port and the visit date includes the ship's most recent call there.
- Options: (a) preferred: remove `WHOAffectedAreaVisit`, since nothing in the world makes Lumeport an affected area; (b) if the element should stay, give it a port and date for which the world has an outbreak, and let the sanitary measures refer to it.
- Needs decision: yes

### sea/16#F4 · Low · The same person carries different role codes as ship security officer
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:RoleCode` = `SSO`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:SecurityOfficerPerson/cbc:RoleCode` = `CHIEFOFFICER`
- Why: Elsbeth Marrin is the ship security officer both as `ShipmentStage/SecurityOfficerPerson` and as `ISPSRequirements/SecurityOfficerPerson` ("The security officer reponsible for these ISPC requirements"). In the first place her role code is SSO, in the second CHIEFOFFICER. `RoleCode` is "A code stating the person's role"; under a security-officer aggregate the role stated is the security role, as the first place does. The same person in the same function is coded two ways in one report.
- Condition: The person in both security-officer aggregates carries the same role code, the one of the security function.
- Options: (a) preferred: SSO in both places, since the parent names the security role; her rank as chief officer stays in `CrewMemberPerson[2]`.
- Needs decision: no

### sea/16#F5 · Low · Four tanks exchanged, but only one exchange transaction reported
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:TanksExchangedQuantity` = `4`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:TanksInBallastQuantity` = `4`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:UptakeBallastWaterTransaction/cbc:TankID` = `BT-3`
- Why: The summary says 4 tanks are in ballast and all 4 were exchanged, but the uptake, exchange and discharge transactions concern only tank BT-3 (310 m³). The ballast on board is stated as 1240 t, i.e. about four times BT-3's volume, which fits four tanks; the transaction list then covers only a quarter of what the summary reports, without saying so.
- Condition: The exchanged tank count and the exchange transactions agree, or the report makes clear that the transactions are a selection.
- Options: (a) preferred: report one exchange transaction per exchanged tank; (b) lower `TanksExchangedQuantity` to the tanks the transactions cover, with the rest under `TanksNotExchangedQuantity`.
- Needs decision: no

### sea/16#F6 · Low · An injury reported as an ill person in the health declaration
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cbc:TotalIllPersonQuantity` = `1`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:PersonnelHealthIncident/cbc:NatureOfIllnessDescription` = `Sprained wrist.`
- Why: `TotalIllPersonQuantity` "Specifies the total number of ill persons on board the vessel" and `NatureOfIllnessDescription` describes "the nature of the illness". A sprained wrist is an injury, not an illness; the Maritime Declaration of Health exists to report possible disease of public-health relevance (own knowledge, IHR 2005 Annex 8). The incident is valid data but does not fit the meaning of these elements.
- Condition: The health declaration's ill persons and incidents are illnesses, or the report explains why an injury is declared.
- Options: (a) preferred: replace the incident by an actual (mild) illness if the story wants a declared case; (b) remove the incident and set the ill-person count to 0.
- Needs decision: no

### sea/16#F7 · Low · INF ship class declared for a feeder carrying no irradiated nuclear fuel
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:INFShipClassCode` = `INF1`
- Why: `INFShipClassCode` is "A code specifying the irradiated nuclear fuel (INF) ship class". The INF class matters only for a ship that carries INF cargo under the IMO INF Code (own knowledge). Nothing in this report or the flow involves such cargo: the only cargo is one container of cotton goods for Selanu. The same vessel is described in `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:ShipConfigurationCode` = `FEEDER` without an INF class. The value has no business reason in this report (rule: no fillers).
- Condition: The INF class is present only when the ship carries, or is reported as able to carry, INF cargo for a reason the report has.
- Options: (a) preferred: remove it; (b) keep it only with a story in which the class matters to the Maritime Administration.
- Needs decision: no

### sea/16#F8 · Low · The crew list names three of fourteen crew
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[3]/cbc:RoleCode` = `CHIEFENG`
- Why: A pre-arrival report to a maritime administration usually carries the crew list (FAL Form 5, own knowledge), which names every crew member. This report has three `CrewMemberPerson` (master, chief officer, chief engineer), while `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14` for the same voyage TH-26-19E. Nothing says the three are a selection, so the report reads as a ship with three crew, which is also implausible for a ship of gross tonnage 9940.
- Condition: The crew named in the report is either complete or marked as a selection, and agrees with the crew count of the voyage.
- Options: (a) preferred: state the crew count in this report and keep the named persons as those with a function in it (master, officers named in the ISPS and health parts); (b) list all fourteen.
- Needs decision: no

### sea/16#F9 · Low · Document status "no status" says nothing
- XPath: `/CommonTransportationReport/cbc:DocumentStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of this Common Transportation Report with respect to its original state". The value "No status on document" conveys exactly what absence would convey; with `VersionID` 1 the report is plainly the original. Under the agreed rule (no fillers, nothing implied by absence) a value needs a business reason. The same value is used as `DocumentStatusCode` 26 times in the examples (counted with `grep -rh --include='*.xml' -o 'DocumentStatusCode">NoStatus<'` over `world/examples`), so this is a pattern rather than a one-off.
- Condition: `DocumentStatusCode` is present only where the status differs from an unchanged original or the document has a reason to state it.
- Options: (a) preferred: remove it here; (b) keep it if the project decides that stating "no status" is a deliberate positive statement, and record that decision.
- Needs decision: yes

## Checked and consistent
- Fuel consumption against emissions: 38 t marine gas oil × 3.206 t CO₂/t (IMO default factor for MGO, own knowledge) = 121.8 t, stated 122 t CO₂e; the flow meter's 38.2 t is consistent with the consumption.
- Ballast: total on board 1240 t is half of the capacity 2480 t, and the segregated ballast of the vessel is 2480 t; uptake (2026-05-14, Lumeport) precedes exchange (2026-05-16, at sea) precedes the planned discharge (2026-05-18, the arrival day).
- Port call: `ExpectedAnchorageIndicator` false agrees with the note "the ship berths without anchoring"; the fresh water requirement agrees with the additional purpose "Fresh water bunkering"; "Discharge one container" agrees with `15-Manifest.xml:/Manifest/cbc:Note` = `One container for Selanu.`
- Health declaration: `SanitaryMeasuresAppliedIndicator` true agrees with the disinfection on 2026-05-15; `StowawaysFoundOnBoardIndicator` false agrees with the stowaway description; dead-person count 0 agrees with `DiedIndicator` false.
- The vessel (ID, name, call sign, MMSI, tonnages, journey, direction) is described as in `15-Manifest.xml`.
- The ISPS ship-to-ship activity (bunkering 2026-05-13 05:40–08:15 at the Lumeport anchorage) lies inside the Lumeport port call record (2026-05-13 to 2026-05-14), and the bunker supplier is the Port of Lumeport, as in the fuel consumption.

## Considered and refuted
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:PassengerPerson/cbc:RoleCode`: a passenger on a feeder container ship suspected as a filler — refuted because carrying a few passengers on a cargo ship is real practice, the passenger list is part of what this report is for, and the same passenger is in `15-Manifest.xml:/Manifest/cac:PassengerPerson/cbc:FamilyName` = `Tavari`.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:AdditionalSecurityMeasure/cbc:Description`: a gangway watch suspected as an ordinary SSP measure rather than an additional one — refuted because a port-specific watch beyond what the plan requires at security level 1 is a legitimate additional measure, and the report gives it for Selanu only.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cbc:MedicalPractitionerConsultedIndicator`: "medical practitioner consulted" suspected to contradict treatment on board by the chief officer — refuted because radio medical advice from shore is the usual practice for an injury at sea and the indicator does not say where the practitioner was.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:DischargeBallastWaterTransaction/cbc:TransactionDate`: a discharge dated after the issue date suspected as a stale or impossible record — refuted because a pre-arrival ballast report declares the planned discharge at the port of arrival, and the date is the arrival day.

## Outside this review
- The coordinates of the Lumeport anchorage (`/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`, 40°1.20'S 15°12.60'W, the same as the Port of Lumeport in `13-TransportationStatus.xml`) and of the Port of Selanu (40°1.20'S 15°8.40'W) are about 3.2 nm apart (4.2' of longitude × cos 40°), which does not fit a two-day voyage of 38 t of fuel and positions 40 or 120 nm from Selanu. This is a question of the world map's scale across documents.
