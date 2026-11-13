# LLM review: 16-CommonTransportationReport.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

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

### sea/16#F1 · High · Ship's position, speed and requested arrival do not agree
- XPath: `/CommonTransportationReport/cbc:IssueTime` = `15:38:00`
- XPath: `/CommonTransportationReport/cac:ReportingLocation/cbc:Name` = `At sea, 40 nautical miles off Selanu`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:VesselDynamics/cbc:SpeedOverGroundMeasure` = `13.5`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceDate` = `2026-05-18`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceTime` = `06:00:00`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cbc:ExpectedAnchorageIndicator` = `false`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ReportLocation/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:PlaceOfReportLocation/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- Why: The report is issued on 2026-05-16 at 15:38 with the ship "40 nautical miles off Selanu", making 13.5 knots under way (navigational status 0). At that speed 40 nm take about 3 hours (40 / 13.5 = 2.96 h), so the ship would be at the fairway buoy around 18:40 on 05-16; yet the requested arrival (pilot on board) is 2026-05-18 06:00, 38 h 22 min after the report, and the ship is said not to anchor (`ExpectedAnchorageIndicator` false, note "the ship berths without anchoring"). In the same report, the ISPS part and the health declaration are said to be reported "120 nautical miles west of Selanu", a position 80 nm further out. One report carries two reporting positions and a position/speed that cannot be squared with its own arrival time.
- Condition: The reporting position(s), the speed over ground, and the requested arrival time are consistent (distance ÷ speed roughly matches the time to arrival, or the ship's waiting is explained), and the parts of the report name the same reporting place or the difference is explained.
- Options: (a) preferred: move the report to the time the ship is about 40 nm off (i.e. 05-18 early morning) and use one reporting place for the ISPS and health parts; (b) keep the issue time and set the ship further away / at slower speed, with the 120 nm position as the single reporting location.
- Needs decision: no

### sea/16#F2 · High · Ballast exchange "more than 200 nautical miles from land" took place 120 nm from Selanu
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:NoControlActionsReason` = `Exchange done at more than 200 nautical miles from land.`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cac:Location/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- Why: The exchange of tank BT-3 is located 120 nm from Selanu, which is land (the island Lisavu), while the summary states the exchange was done more than 200 nm from land (the D-1 distance of the IMO BWM Convention, own knowledge). The two statements in the same summary contradict each other. In addition, by the coordinates in this example the Lumeport anchorage (15°12.60'W) lies only 4.2' of longitude (about 3 nm at 40°S) west of the Port of Selanu (15°8.40'W), so an eastbound voyage between them has no stretch 200 nm from land.
- Condition: The stated distance from land and the location of the exchange agree.
- Options: (a) state the actual distance (and that the exchange met or did not meet the D-1 distance, e.g. in a designated exchange area); (b) move the exchange location. Preferred (a), since the world's geography leaves no open sea 200 nm from land on this route.
- Needs decision: no

### sea/16#F3 · Medium · NoControlActionsReason used although control actions were taken
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:NoControlActionsReason` = `Exchange done at more than 200 nautical miles from land.`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:OtherControlActions` = `Sediment flushed from the forepeak tank during the exchange and recorded in the ballast water record book.`
- Why: UBL defines NoControlActionsReason as "A textual description of the reason if no control actions are being taken." Here an exchange (`ExchangeBallastWaterTransaction`, `TanksExchangedQuantity` 4) and other control actions (`OtherControlActions`) were taken, so there is no "no control actions" case; the text describes the exchange rather than a reason for not acting.
- Condition: `NoControlActionsReason` is absent, or present only in a summary where no control action is taken.
- Options: (a) preferred: drop it; the exchange is already described by the transactions; (b) move the distance statement into `OtherControlActions`.
- Needs decision: no

### sea/16#F4 · Medium · Crew list to the authority holds 3 persons; the manifest of the same voyage counts 14 crew
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[1]/cbc:RoleCode` = `MASTER`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[3]/cbc:RoleCode` = `CHIEFENG`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14`
- Why: A pre-arrival report to the maritime administration carries the crew list for the authority (the FAL crew list function). The manifest for the same journey `TH-26-19E` (`15-Manifest.xml`) gives 14 crew, but this report names only three. For a 9 940 GT feeder, three persons is also not a plausible complement (own knowledge). The report thus understates who is on board, which its purpose depends on.
- Condition: The crew named or counted in this report agrees with the crew quantity of `15-Manifest.xml`, or the report states it lists only the officers and gives the total.
- Options: (a) add `CrewQuantity` = 14 to the stage and keep the officers as named examples; (b) list all 14. Preferred (a): it keeps the example readable.
- Needs decision: no

### sea/16#F5 · Medium · Lumeport declared a WHO affected area, visited on a date that is not the last call
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:WHOAffectedAreaVisit/cbc:VisitDate` = `2026-03-28`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:WHOAffectedAreaVisit/cac:WHOAffectedAreaPortLocation/cbc:ID` = `XBLMP`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:PortCallRecord/cac:Period/cbc:StartDate` = `2026-05-13`
- Why: `WHOAffectedAreaVisit` is "A WHO Affected Area visit related to this maritime health declaration": it states that Lumeport, the ship's home port, is an area identified by WHO as affected (IHR Model of Maritime Declaration of Health, question on affected areas; own knowledge). Nothing else in the report treats Lumeport as affected (no infectious case, no measures linked to it), and if it were, the relevant visit would be the call of 2026-05-13/14 recorded in the same report, not one on 2026-03-28, which also lies outside the 30-day window the declaration asks about.
- Condition: Either Lumeport is not declared a WHO affected area, or it is, the story supports it and the visit date is the latest call.
- Options: (a) preferred: remove the visit (no affected area visited); (b) keep it and make the world story and the date consistent.
- Needs decision: yes

### sea/16#F6 · Low · Four tanks exchanged, one exchange transaction
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:TanksExchangedQuantity` = `4`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cbc:TankID` = `BT-3`
- Why: The summary says four tanks were exchanged, but only tank BT-3 has an exchange transaction (and only BT-3 has an uptake). The ballast reporting form lists every tank exchanged.
- Condition: The number of exchange transactions equals `TanksExchangedQuantity`, or the summary says why only one is shown.
- Options: add the other three tanks' transactions (each about 310 m³: 1 240 t / 4); or lower the count. Preferred: add them.
- Needs decision: no

### sea/16#F7 · Low · Reporter's contact is the bookings desk
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Name` = `Bookings`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: For a ship's pre-arrival report to the maritime administration, the contact the authority needs is the ship or the line's operations/marine desk reachable at arrival (05-18 06:00), not "Bookings" with weekday office hours. The bridge contact is only given on the arrival event.
- Condition: The reporter's contact is one that handles the ship's reporting and is reachable around the arrival time.
- Options: a marine operations / duty contact of Tidewell, or the master's contact.
- Needs decision: no

### sea/16#F8 · Low · Maritime administration described as a company, with a ship-registry contact on office hours
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Name` = `Ship registry`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: A public authority is not registered in the island's commercial companies register and has no liquidation status. Its contact is the ship registry with weekday office hours, while the report concerns an arrival at 06:00 and the authority's role here is receiving the pre-arrival report (port state / vessel traffic), not ship registration.
- Condition: The authority's legal entity carries no commercial-register or liquidation data, and its contact is the unit that receives arrival reports and is reachable when ships arrive.
- Options: drop the commercial-register/liquidation elements (keep the registration name); use a port state / vessel reporting contact with round-the-clock note.
- Needs decision: no

### sea/16#F9 · Low · Ship security officer carries different role codes in the same report
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:RoleCode` = `SSO`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:SecurityOfficerPerson/cbc:RoleCode` = `CHIEFOFFICER`
- Why: Elsbeth Marrin is the ship security officer in both places; the stage gives her role as `SSO`, the ISPS part, where she appears precisely as security officer, as `CHIEFOFFICER`. In a security-officer element the role code should be the security role.
- Condition: Both security-officer elements give the same role code for the same function.
- Options: use `SSO` in the ISPS part too (preferred: the element is the security-officer role).
- Needs decision: no

### sea/16#F10 · Low · INF ship class on a feeder carrying no irradiated nuclear fuel
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:INFShipClassCode` = `INF1`
- Why: The INF Code class is relevant only to ships certified for and carrying packaged irradiated nuclear fuel, plutonium or high-level waste (own knowledge). Nothing in this flow involves such cargo, and the same vessel in `15-Manifest.xml` and `14-BillOfLading.xml` carries no INF class. Without a business reason the value is a filler (IND5).
- Condition: `INFShipClassCode` is absent, or the voyage carries INF cargo.
- Options: drop it (preferred); keep it only with an INF cargo in the story.
- Needs decision: no

### sea/16#F11 · Low · Port company issues the ship sanitation and medicine chest certificates
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:ShipSanitationControlCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:MedicalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- Why: Under the IHR a Ship Sanitation Control Certificate is issued by the competent (port health) authority at an authorised port (own knowledge). Port of Lumeport is a private limited company (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Limited company (private)`), i.e. the terminal operator, not a health authority.
- Condition: The certificate issuer is a party that can issue it (a port health authority), or the story makes the port company the delegated competent authority.
- Options: introduce a port health authority of Bayvarra as issuer (preferred); or state the delegation.
- Needs decision: yes

### sea/16#F12 · Low · Requested arrival differs from the manifest's estimated arrival
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceTime` = `06:00:00`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-05-17`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceTime` = `22:00:00`
- Why: The manifest of 05-15 estimates arrival at Selanu 2026-05-17 22:00; this report of 05-16 requests arrival 2026-05-18 06:00, and `17-TransportationStatus.xml` has the actual arrival at 06:30. The CTR's status is `ONTIME`, so nothing explains the 8-hour shift relative to the manifest. A requested time can differ from an ETA, but here no delay is stated.
- Condition: The manifest's ETA and this report's requested arrival agree, or the report says why they differ.
- Options: align the ETA in the manifest (it is the later document's predecessor) or mention a revised ETA here.
- Needs decision: no

### sea/16#F13 · Low · English renderings of Lisavan addresses tagged as Bayvarran English
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`
- XPath: `17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: The English renderings of the Lisavu addresses of the Maritime Administration and the Port of Selanu carry `languageID="en-XB"` (6 times in this file, including the registration addresses), while the same address of the Port of Selanu in `17-TransportationStatus.xml` carries `en-XL`. Over all examples, "Port Wrenfield" is tagged `en-XL` 125 times, `en-XB` 94 times and `en-XU` 6 times (grep over `*.xml`). The same address is described with different language tags depending on the document.
- Condition: The same rendering of the same address carries the same `languageID` in every example, following one documented rule.
- Options: (a) tag English renderings of Lisavu addresses always `en-XL` (preferred: the address is in Lisavu); (b) keep the sender-dependent tag, if that is the agreed rule, and record it.
- Needs decision: yes

### sea/16#F14 · Low · Registry port named without the identifier used elsewhere; manifest reference without type
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport`
- XPath: `/CommonTransportationReport/cac:DocumentReference/cbc:ID` = `TOL-MF-26-0140`
- Why: Lumeport is identified as `XBLMP` (UN/LOCODE) elsewhere in this report, but the registry port gives only a name. The only document reference gives the ID of `15-Manifest.xml` without saying what it is (no `DocumentTypeCode` / `DocumentType`), so the authority cannot tell it is the cargo manifest.
- Condition: The registry port carries `XBLMP`; the document reference states its type.
- Options: add the UN/LOCODE and a document type code (Manifest).
- Needs decision: no

### sea/16#F15 · Low · Ship-level report hung on one shipper's shipment
- XPath: `/CommonTransportationReport/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cbc:PlannedOperationsDescription` = `Discharge one container, load six.`
- Why: Everything in the stage (crew, stores, waste, ballast, ISPS, health, fuel) concerns the vessel and its voyage, but the shipment carrying it is Lumeway Distribution's shipment `LD-SH-26-0132`, while the ship also loads six other containers at Selanu. The shipment ID identifies one shipper's goods, not the ship's voyage.
- Condition: The shipment identifier is one that identifies the voyage/port call (e.g. the journey or the carrier's voyage reference), or the shipment is left without an ID.
- Options: use the carrier's voyage identifier (e.g. based on `TH-26-19E`) as the shipment ID (preferred); or omit it.
- Needs decision: no

## Checked and consistent
- References: `TOL-MF-26-0140` resolves to `15-Manifest.xml` (a manifest of the same vessel and journey `TH-26-19E`); registry certificate `REG-XB-S-20117`, vessel ID, call sign `QBTH7`, MMSI `298702117`, GT 9940, NT 5120 and segregated ballast 2480 t agree with `15-Manifest.xml`.
- Departure: the port-call record at Lumeport (2026-05-13 to 05-14) and the ballast uptake there on 05-14 agree with the actual departure 2026-05-14 18:10 in `13-TransportationStatus.xml`; the bunkering at the anchorage 05-13 05:40–08:15 "before the ship berthed" precedes that.
- Arrival: requested arrival 05-18 06:00 (pilot) fits the actual arrival 06:30 in `17-TransportationStatus.xml`; berth not anchoring agrees with `ExpectedAnchorageIndicator` false; "discharge one container" agrees with the one container `TWLU4120872` for Selanu in the manifest.
- Emissions: 38 t MGO × 3.206 t CO2/t (IMO emission factor for MGO, own knowledge) = 121.8 t ≈ the stated 122 t CO2e; flow meter 38.2 t against 38 t consumption is rounding.
- Ballast: 1 240 t on board in 4 of 8 tanks = 310 t per tank, consistent with BT-3's 310 m³ (about 318 t seawater); capacity 2 480 t equals `SegregatedBallastMeasure`; exchange at 95 % meets the D-2/D-1 volumetric rule; discharge of 120 m³ ≤ 310 m³.
- Waste W-1: 2.4 m³ delivered + 0.6 m³ retained + 0.8 m³ generated until next port well within 8 m³ capacity.
- Health: one ill person (sprained wrist, chief engineer, still on board, fit for light duty) agrees with `TotalIllPersonQuantity` 1 and `TotalDeadPersonQuantity` 0; sanitary measure applied (disinfection 05-15) agrees with `SanitaryMeasuresAppliedIndicator` true; SSCC on board agrees with its indicator.
- ISPS: valid ISSC with expiry 2028-09-30, issued by the flag state's maritime administration (Bayvarra, the registration nationality); security level 1 at the ship and at the Lumeport call.
- Passenger Ines Tavari and master Corin Halvard agree with `15-Manifest.xml`.
- `check_ids.py`: no identifier with a check digit in this example.

## Considered and refuted
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cbc:ID` = `XLSEL-26-0517`: the "0517" in the port-call, ballast and health IDs looked like a date that is not the arrival date (05-18) — refuted because the IDs are opaque references and match the manifest's original ETA of 05-17; nothing reads them as dates.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`: the anchorage has exactly the coordinates of the Port of Lumeport (`cotton/14-CommonTransportationReport.xml`) — refuted as a finding because the world's map gives one coordinate per port tile; the anchorage belongs to the port.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cbc:StowawayDescription` = `None found in the search before departure.`: suspected filler with `StowawaysFoundOnBoardIndicator` false — refuted because it records that a search was made, which the declaration may report.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ShipsSurgeonPerson/cbc:FirstName` = `Elsbeth`: the chief officer as SSO and medical officer at once — refuted: on a small cargo ship the chief officer usually holds both duties.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:PassengerPerson/cbc:FamilyName` = `Tavari`: a passenger on a container feeder — refuted: the manifest carries the same passenger, and supernumeraries on feeders are normal.

## Outside this review
- The voyage Lumeport → Selanu takes from 05-14 18:10 to 05-18 06:30 although the two ports lie about 3 nm apart on the world's coordinates; a question of the world's map scale and timelines across flows.
- `15-Manifest.xml` (issued 2026-05-15 16:08) still gives an estimated departure of 2026-05-15 06:00, after the actual departure 2026-05-14 18:10 in `13-TransportationStatus.xml`; lies in the manifest.
