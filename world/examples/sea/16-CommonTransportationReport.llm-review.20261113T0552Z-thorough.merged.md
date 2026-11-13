# LLM review: 16-CommonTransportationReport.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/16-CommonTransportationReport.xml`, Git blob `fcbb7ae1a07ebdd8f8e779b15a6991056933bf53` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/16#F1 · High · Two reporting positions at one moment, and neither fits the speed and the requested arrival
- XPath: `/CommonTransportationReport/cbc:IssueDate` = `2026-05-16`
- XPath: `/CommonTransportationReport/cbc:IssueTime` = `15:38:00`
- XPath: `/CommonTransportationReport/cac:ReportingLocation/cbc:Name` = `At sea, 40 nautical miles off Selanu`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ReportLocation/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:PlaceOfReportLocation/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:VesselDynamics/cbc:SpeedOverGroundMeasure` = `13.5`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:VesselDynamics/cbc:NavigationStatusCode` = `0`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceDate` = `2026-05-18`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceTime` = `06:00:00`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cbc:ExpectedAnchorageIndicator` = `false`
- Why: The report is one document issued at one moment, 2026-05-16 15:38. `ReportingLocation` ("a location to which this common transportation report applies") puts the ship 40 nm off Selanu, while the ISPS part and the health declaration of the same report are "reported" 120 nm west of Selanu; the ship cannot be at both. Neither position fits the rest. Merge recalculation: from 2026-05-16 15:38 to 2026-05-18 06:00 is 38 h 22 min = 38.4 h. At 13.5 kn under way (navigational status 0), 40 nm take 40 / 13.5 = 2.96 h and 120 nm take 8.89 h, so the ship would be at the fairway buoy about 18:36 on 05-16 (from 40 nm) or about 00:31 on 05-17 (from 120 nm). To arrive at 06:00 on the 18th it would have to average 40 / 38.4 = 1.0 kn or 120 / 38.4 = 3.1 kn, and it cannot wait at anchor: `ExpectedAnchorageIndicator` is false and the note says "the ship berths without anchoring". The actual arrival in `17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `06:30:00` (on 2026-05-18) confirms the arrival time, so it is the position, the speed or the issue time that does not fit. The 80 nm between the two positions take 5.9 h at the stated speed.
- Condition: Every place where the report says it is made names the same position (or the parts made at another time say so, with their time), and that position, the speed over ground and the requested arrival agree (distance ÷ speed ≈ time from issue to arrival, or a stated reason for the waiting time).
- Options: (a) preferred: one reporting position for the whole report, with the report issued a few hours before arrival (e.g. on the evening of 2026-05-17 about 40 nm off), which is when a pre-arrival report with such a position is sent; (b) keep the issue time and put the ship much further away at a speed that fits, with one position for all parts; (c) keep everything and state slow steaming with a reason. Separate ISPS/health reporting places only if those parts are dated separately, which the elements barely allow.
- Needs decision: no
- From: broad (F1), context (F1), logistics (F1, F2)

### sea/16#F2 · High · The coordinates put the Lumeport anchorage 3.2 nautical miles from the Port of Selanu, against the distances the report states
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `1.20`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cbc:Name` = `Lumeport anchorage`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `1.20`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cac:Location/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `/CommonTransportationReport/cac:ReportingLocation/cbc:Name` = `At sea, 40 nautical miles off Selanu`
- Why: Both points lie at 40°01.20′S; the Port of Selanu (terminal operator, on Lisavu) at 15°08.40′W, the Lumeport anchorage in Bayvarra at 15°12.60′W. Merge recalculation: 4.2′ of longitude × cos 40.02° = 3.2 nm. The same report has the ship exchange ballast 120 nm west of Selanu (which by these coordinates is also about 117 nm west of Lumeport, i.e. not between the ports), report 40 nm off Selanu, burn 38 t of fuel and take from 2026-05-14 18:10 (departure, `13-TransportationStatus.xml`) to 2026-05-18 for the crossing. The anchorage's coordinates are, moreover, exactly those of the Port of Lumeport's quay (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`). Within this one document, the coordinates (stated as geographic, EPSG 4326) and the stated distances cannot both be right. Broad and context put the cross-document map-scale question under "Outside this review"; the contradiction inside this report is a finding of it. The resolution depends on how the world's map coordinates are meant to relate to its sea distances, which is a world decision.
- Condition: The coordinates of the Port of Selanu and the Lumeport anchorage and the distances stated in the report agree (distance between the ports at least what the report's positions imply), and the anchorage is not at the quay's point.
- Options: (a) preferred: give the ports and the anchorage coordinates that reflect the distances the story uses, fixed once where the coordinates come from (the same coordinates occur in other examples); (b) if the map deliberately uses compressed coordinates, drop the coordinates where they contradict the stated distances, or state distances that fit the map (which then also clashes with F3's 200 nm claim).
- Needs decision: yes (map scale and the distance between the countries is a world decision)
- From: logistics (F4), parties (F1); broad and context under "Outside this review"

### sea/16#F3 · High · Ballast exchange "more than 200 nautical miles from land" took place 120 nm from Selanu
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:NoControlActionsReason` = `Exchange done at more than 200 nautical miles from land.`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cac:Location/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- Why: The only exchange recorded (tank BT-3, 2026-05-16) is located 120 nm from Selanu, i.e. from land on Lisavu, so "more than 200 nautical miles from land" is false by the document's own location. The 200 nm distance is the D-1 criterion of the IMO Ballast Water Management Convention, regulation B-4 (at least 200 nm from the nearest land, or at least 50 nm where that is not possible; own knowledge), exactly the distance a port state checks. By this report's coordinates (F2) the route Lumeport–Selanu has no stretch 200 nm from land at all.
- Condition: The stated distance from land of the exchange agrees with its location.
- Options: (a) preferred: state the actual distance (and, if relevant, that the 50 nm alternative or a designated exchange area applied, with its reason), in a place where it fits (see F6); (b) move the exchange location to where the 200 nm statement holds, which must also fit F1 and F2.
- Needs decision: no
- From: broad (F2), logistics (F3), context (F2, part)

### sea/16#F4 · Medium · A language code in the reporter's LocaleCode
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value is the ISO 639 language code already given in `Language/cbc:ID`, with `listID="ISO 639"`, so it names no locale. The same value occurs 362 times in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`, the count used by all earlier merges).
- Condition: `LocaleCode` is absent or holds a locale (language and country) from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode` where it only repeats the language (nothing is lost, no new list needed); (b) a locale such as `en-XB` with a listID that defines locales.
- Needs decision: no
- From: parties (F3)

### sea/16#F5 · Medium · The Maritime Administration of Lisavu described as a company in the commercial register
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC42270`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The authority is a public body. `CompanyID` is "an identifier for the party as registered within a company registration scheme", the scheme is the "Island companies register" of type "Commercial register", and `CompanyLiquidationStatusCode` is "the party's liquidation status". A state administration is not registered as a company and cannot go into liquidation. The world's registration type list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no code for public bodies. The parties part counted 26 `PartyLegalEntity` aggregates of customs administrations, maritime administrations or the Trade Accord Council with `COMMERCIAL` and `ACTIVE` (lxml over `*.xml`).
- Condition: The authority's legal entity claims no registration in a commercial companies register and carries no liquidation status; an identifier, if kept, is from a scheme for public bodies.
- Options: (a) preferred: drop `CompanyID`, `CorporateRegistrationScheme` and `CompanyLiquidationStatusCode` from public bodies, keeping `RegistrationName`; (b) a register of public bodies with its own registration type code.
- Needs decision: no
- From: parties (F2), broad (F8, part)

### sea/16#F6 · Medium · NoControlActionsReason used although control actions were taken
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:NoControlActionsReason` = `Exchange done at more than 200 nautical miles from land.`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:OtherControlActions` = `Sediment flushed from the forepeak tank during the exchange and recorded in the ballast water record book.`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:TanksExchangedQuantity` = `4`
- Why: UBL defines `NoControlActionsReason` as "A textual description of the reason if no control actions are being taken." This summary reports control actions: an exchange (`ExchangeBallastWaterTransaction`, 95 %, sequential; four tanks exchanged) and sediment flushing in `OtherControlActions`. The definition's condition is not met; the text is a compliance statement about the exchange, not a reason for having taken no action. (The distance in the text is wrong as well: F3.)
- Condition: `NoControlActionsReason` is present only in a summary where no control action is reported.
- Options: (a) preferred: drop it; the exchange is described by its transactions; (b) move a (corrected) distance statement into `OtherControlActions` or the exchange's location; (c) if the story wants a case without control actions, remove the exchange instead (changes the story).
- Needs decision: no
- From: broad (F3), context (F2, part), logistics (F3, part)

### sea/16#F7 · Medium · Lumeport declared a WHO affected area, visited on a date that is not the last call there
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:WHOAffectedAreaVisit/cbc:VisitDate` = `2026-03-28`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:WHOAffectedAreaVisit/cac:WHOAffectedAreaPortLocation/cbc:ID` = `XBLMP`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:WHOAffectedAreaVisit/cac:WHOAffectedAreaPortLocation/cbc:Name` = `Port of Lumeport`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:PortCallRecord/cac:Period/cbc:StartDate` = `2026-05-13`
- Why: `WHOAffectedAreaVisit` is "A WHO Affected Area visit related to this maritime health declaration"; in the IHR Model of Maritime Declaration of Health it answers whether the ship called at a port in an area the WHO has declared affected (IHR 2005 Annex 8, own knowledge). It thus states that Bayvarra's main port, the ship's home port, is an affected area, which nothing else in the report supports (no suspected infectious case, the only incident is a sprained wrist). The date is also inconsistent: the same report records the last Lumeport call on 2026-05-13 to 05-14, so a visit to an affected Lumeport on 2026-03-28 is followed by an undeclared later visit to the same area; 2026-03-28 is also outside the 30-day window the declaration asks about.
- Condition: Either no WHO affected area visit is declared, or the world has a reason for an affected area at the named port and the visit date is the ship's most recent call there.
- Options: (a) preferred: remove `WHOAffectedAreaVisit`; (b) keep it with a port and date for which the world has an outbreak, and let the sanitary measures refer to it.
- Needs decision: yes
- From: broad (F5), context (F3)

### sea/16#F8 · Medium · The port company issues the ship sanitation control certificate and the medicine chest certificate
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:ShipSanitationControlCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:MedicalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- Why: `Certificate/IssuerParty` is "the authorised Organisation who issues this Certificate". The Port of Lumeport is the port company, a private limited company (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Limited company (private)`). Under the IHR 2005 (Art. 39, Annex 3; own knowledge) a Ship Sanitation Control Certificate is issued by the competent (port health) authority at an authorised port, and a medicine chest is certified by a port health authority or a pharmacist. The definition's "authorised" is not met by a terminal operator.
- Condition: The issuer of the ship sanitation control certificate is a health authority of the port state; the issuer of the medicine chest certificate is a party authorised to certify medicine chests, or the story makes the port company the delegated competent authority.
- Options: (a) preferred: a port health authority of Bayvarra as issuer of both (one party, matches IHR practice); (b) keep the port as issuer and state the delegation in the world.
- Needs decision: yes (changes who the party is)
- From: parties (F4), broad (F11)

### sea/16#F9 · Low · Document status "no status"
- XPath: `/CommonTransportationReport/cbc:DocumentStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of this Common Transportation Report with respect to its original state". "No status" conveys what absence conveys; with `VersionID` 1 the report is plainly the original. Under the rule "no fillers, nothing implied by absence" the value has no reason. The context part counted 26 `DocumentStatusCode` = `NoStatus` in the examples (`grep -rh --include='*.xml' -o 'DocumentStatusCode">NoStatus<' world/examples`).
- Condition: `DocumentStatusCode` is absent, or carries a status the report has a reason to state.
- Options: (a) preferred: drop it; (b) keep it only if the project records "no status" as a deliberate positive statement.
- Needs decision: no
- From: context (F9)

### sea/16#F10 · Low · Reporter's sales-tax registration and share capital in a pre-arrival report
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- Why: The report (`ReportTypeCode` PREARRIVAL) tells the maritime administration about ship, crew, health, waste, ballast and security; nothing in it is taxed, invoiced or paid, and the carrier's share capital plays no part. The data look copied from Tidewell's master data (section 4.8); the same party block occurs in 10 examples of the flow (07, 08, 12–18, 20; the parties and money parts compared them with a script).
- Condition: The reporter carries only the party data the report uses (identification, name, address, contact, legal registration if wanted).
- Options: (a) preferred: drop `PartyTaxScheme`, `CorporateStockAmount` and `FullyPaidSharesIndicator` from the reporter; (b) give the report a reason to carry them (e.g. port dues invoiced against it), which changes the story.
- Needs decision: no
- From: parties (F8), money (F1)

### sea/16#F11 · Low · The contacts given do not serve the report or a ship arriving on Monday at 06:00
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Name` = `Bookings`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Name` = `Ship registry`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Name` = `Port control`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The report announces an arrival on 2026-05-18 (a Monday) at 06:00. The reporter's contact for a regulatory report is its bookings desk with office hours; the authority's contact is its ship registry (flag-state registration, not arrivals or port state control), reachable on weekdays from 08:00; the terminal operator's "Port control" (a round-the-clock function) is an operations planner with office hours. None is reachable when the ship arrives, and the reporter's and authority's contacts are not the functions that deal with a pre-arrival report. The bridge contact is given only on the arrival event.
- Condition: The reporter's contact handles the ship's reporting; the authority's and terminal operator's contacts handle ship arrivals and are reachable at the requested arrival time; name, job title and hours agree.
- Options: (a) preferred: role-specific contacts (carrier's marine operations or duty desk; harbour master / vessel reporting office and port control around the clock); (b) drop contacts that do not serve the report.
- Needs decision: no
- From: broad (F7, F8 part), parties (F6)

### sea/16#F12 · Low · English renderings of Lisavu addresses tagged as Bayvarran English; port's legal form in one language
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: The six English renderings of the Lisavu addresses of the Maritime Administration and the Port of Selanu carry `languageID="en-XB"` (English as used in Bayvarra), while the same address of the Port of Selanu in `17-TransportationStatus.xml` carries `en-XL`, and the port's legal form there is given in Lisavan and English, here once in English without a tag. The tag follows the issuer, not the place. Counts made by the parts (over `*.xml`): "Port Wrenfield" tagged `en-XL` 125 times, `en-XB` 94, `en-XU` 6 (broad, grep); English street/town renderings in Lisavu addresses `en-XL` 188, `en-XB` 141, `en-XU` 9 (parties, lxml). Earlier flows (air, wood, plastics) left the rule open.
- Condition: The same rendering of the same address carries the same `languageID` in every example, following one documented rule, and each Lisavu party's legal form is given in the same languages everywhere.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu names and the legal form in Lisavan and English everywhere (the rendering belongs to the place); (b) keep the issuer-dependent tag and record the convention in the world's address rules.
- Needs decision: yes (one rule for the whole world; parties said no, aligned with broad and the earlier flows' yes)
- From: broad (F13), parties (F5)

### sea/16#F13 · Low · Ship-level report hung on one shipper's shipment
- XPath: `/CommonTransportationReport/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cbc:PlannedOperationsDescription` = `Discharge one container, load six.`
- Why: Everything in the stage (crew, stores, waste, ballast, ISPS, health, fuel) concerns the vessel and its voyage, but the shipment that carries it is Lumeway Distribution's shipment `LD-SH-26-0132`, while the ship also loads six other containers at Selanu. The shipment ID identifies one shipper's goods, not the ship's voyage. The logistics part refuted this (UBL 2.5 puts crew, ballast, waste and port call under `Shipment/ShipmentStage`, and it is the shipment the referenced manifest declares); the merge keeps it as Low: the structure forces a Shipment, but not that its ID be one shipper's shipment.
- Condition: The shipment identifier identifies the voyage or port call (e.g. based on the journey `TH-26-19E`), or the shipment carries no ID; if the shipper's shipment is kept, its stage numbering follows F14.
- Options: (a) preferred: the carrier's voyage identifier as shipment ID; (b) omit the ID.
- Needs decision: no
- From: broad (F15); logistics refuted it (argument above)

### sea/16#F14 · Low · The sea stage is numbered 1 here and 2 in the other documents of the shipment
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:ID` = `2`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cbc:ID` = `2`
- Why: The report names shipment LD-SH-26-0132; in the bill of lading and the manifest of that shipment the sea voyage Lumeport–Selanu is stage 2 (pre-carriage 1, on-carriage 3, verified in `14-BillOfLading.xml`). `ShipmentStage/ID` is "an identifier for this shipment stage", so the same stage of the same shipment should have the same identifier.
- Condition: The sea stage of LD-SH-26-0132 has the same ID here as in 14 and 15, or the report identifies the voyage rather than this shipment (F13).
- Options: (a) preferred: ID 2; (b) resolve through F13 option (a).
- Needs decision: no
- From: logistics (F5)

### sea/16#F15 · Low · Crew list of three for a ship with a crew of fourteen
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[1]/cbc:RoleCode` = `MASTER`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[3]/cbc:RoleCode` = `CHIEFENG`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:GrossTonnageMeasure` = `9940`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14`
- Why: A pre-arrival report that lists crew members carries the crew list for the authority (IMO FAL Form 5, own knowledge), which names every crew member. This report has three, while the referenced manifest gives 14 for the same journey TH-26-19E; three persons is also not a plausible complement for a 9 940 GT feeder (minimum safe manning about 12–16, own knowledge). Nothing says the three are a selection, and the stage has no `CrewQuantity`.
- Condition: The crew named in the report is complete, or the report states the crew total (14) so the named persons are not read as the whole crew.
- Options: (a) preferred: add `CrewQuantity` 14 and keep the persons with a function in the report; (b) list all fourteen, ratings with `CREW`.
- Needs decision: no
- From: broad (F4, Medium), context (F8), logistics (F6), parties (F9)

### sea/16#F16 · Low · The same ship security officer carries two different role codes
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:RoleCode` = `SSO`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:SecurityOfficerPerson/cbc:RoleCode` = `CHIEFOFFICER`
- Why: Elsbeth Marrin is the ship security officer in both places (`ISPSRequirements/SecurityOfficerPerson`: "the security officer responsible for these ISPS requirements"). Once her role code is "Ship security officer", once "Chief officer". Under a security-officer aggregate the role stated is the security role; her rank is already in `CrewMemberPerson[2]`.
- Condition: Both `SecurityOfficerPerson` elements carry the same role code, the security role.
- Options: (a) preferred: `SSO` in both; (b) drop `RoleCode` in the ISPS requirements.
- Needs decision: no
- From: broad (F9), context (F4), logistics (F7), parties (F7)

### sea/16#F17 · Low · Requested arrival differs from the referenced manifest's estimated arrival, without explanation
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceTime` = `06:00:00`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cac:CurrentStatus/cbc:ConditionCode` = `ONTIME`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-05-17`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceTime` = `22:00:00`
- Why: The referenced manifest (issued 2026-05-15) estimates arrival at Selanu 2026-05-17 22:00; this report (05-16) requests arrival 2026-05-18 06:00 with status "on time". A requested pilot time can differ from an ETA, so this is no hard contradiction, but nothing explains the 8-hour shift. The logistics part put it under "Outside this review" as a timeline question; since this report refers to the manifest, the merge keeps broad's finding.
- Condition: The manifest's ETA and this report's requested arrival agree, or the report says why they differ (and the status reflects it).
- Options: align the manifest's ETA (preferred: the manifest is the earlier document, and 17 confirms 05-18 06:30), or state a revised ETA here.
- Needs decision: no
- From: broad (F12); logistics under "Outside this review"

### sea/16#F18 · Low · Four tanks exchanged, one exchange transaction
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:TanksInBallastQuantity` = `4`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cbc:TanksExchangedQuantity` = `4`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cbc:TankID` = `BT-3`
- Why: Four tanks are in ballast and all four were exchanged, but the uptake, exchange and discharge transactions concern only tank BT-3 (310 m³). The 1 240 t on board is about four times BT-3's volume, which fits four tanks; the transaction list covers a quarter of what the summary reports without saying so. The ballast reporting form lists every tank.
- Condition: The number of exchange transactions equals `TanksExchangedQuantity`, or the report makes clear the transactions are a selection.
- Options: (a) preferred: one exchange (and uptake) transaction per tank; (b) lower the count, the rest under `TanksNotExchangedQuantity`.
- Needs decision: no
- From: broad (F6), context (F5)

### sea/16#F19 · Low · Planned ballast discharge without a place
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:DischargeBallastWaterTransaction/cbc:VolumeMeasure` = `120`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:DischargeBallastWaterTransaction/cbc:TransactionDate` = `2026-05-18`
- Why: The uptake and the exchange carry a location, the discharge does not; for the port state the place of discharge (in the port of Selanu) is the point of reporting it.
- Condition: The discharge transaction has a location.
- Options: add the Selanu location (`XLSEL`).
- Needs decision: no
- From: logistics (F9)

### sea/16#F20 · Low · An injury reported as an ill person in the health declaration
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cbc:TotalIllPersonQuantity` = `1`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:PersonnelHealthIncident/cbc:NatureOfIllnessDescription` = `Sprained wrist.`
- Why: `TotalIllPersonQuantity` "Specifies the total number of ill persons on board the vessel" and `NatureOfIllnessDescription` describes "the nature of the illness". A sprained wrist is an injury; the Maritime Declaration of Health asks about disease of possible public-health relevance (IHR 2005 Annex 8, own knowledge). Refutation attempt: ships' attachment lists sometimes include injuries; but the element names illness, so Low remains.
- Condition: The declared ill persons and incidents are illnesses, or the report explains why an injury is declared.
- Options: (a) preferred: a (mild) illness if the story wants a declared case; (b) remove the incident and set the count to 0.
- Needs decision: no
- From: context (F6)

### sea/16#F21 · Low · INF ship class on a feeder carrying no irradiated nuclear fuel
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:INFShipClassCode` = `INF1`
- Why: `INFShipClassCode` is "A code specifying the irradiated nuclear fuel (INF) ship class". The class matters only for ships certified for and carrying packaged irradiated nuclear fuel, plutonium or high-level waste under the IMO INF Code (own knowledge). Nothing in the flow carries such cargo; the referenced manifest declares one container of park benches for Selanu, and describes the same vessel without an INF class. No business reason (IND5).
- Condition: `INFShipClassCode` is absent, or the voyage carries INF cargo.
- Options: (a) preferred: drop it; (b) keep it only with INF cargo in the story.
- Needs decision: no
- From: broad (F10), context (F7), logistics (F8)

### sea/16#F22 · Low · Registry port named without the identifier used elsewhere in the report
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:UptakeBallastWaterTransaction/cac:Location/cbc:ID` = `XBLMP`
- Why: Lumeport is identified by its UN/LOCODE `XBLMP` elsewhere in this report, but the registry port gives only a name.
- Condition: The registry port carries `XBLMP`.
- Options: add the UN/LOCODE.
- Needs decision: no
- From: broad (F14, part)

### sea/16#F23 · Low · Manifest reference with ID only
- XPath: `/CommonTransportationReport/cac:DocumentReference/cbc:ID` = `TOL-MF-26-0140`
- Why: The only document reference gives the ID of `15-Manifest.xml` without `DocumentTypeCode` or `DocumentType`, so the authority cannot tell from the reference that it is the cargo manifest.
- Condition: The reference states what it refers to.
- Options: add a document type code (manifest) or `DocumentType`.
- Needs decision: no
- From: broad (F14, part)

## Checked and consistent
- Reference: `TOL-MF-26-0140` resolves to `15-Manifest.xml` (same vessel, journey `TH-26-19E`, one container `TWLU4120872` for Selanu, matching "Discharge one container"). Registry certificate `REG-XB-S-20117`, vessel ID, name, call sign `QBTH7`, GT 9940, NT 5120 (ratio 0.52), segregated ballast 2480 t = `TotalBallastWaterCapacityMeasure` 2480 t agree with 14 and 15; type 1511 and FEEDER agree; course 088 fits the eastbound direction (broad, logistics, context).
- MMSI `298702117`: MID 298 is not allocated by the ITU (`world/codelists/sources/PROVENANCE-second-round.md` line 206: the ITU MID table re-read 2026-11-11 lists none of 280–299), so it cannot be mistaken for a real station (merge).
- Departure side: the Lumeport port-call record (2026-05-13 to 05-14), the ballast uptake there on 05-14 and the bunkering 05-13 05:40–08:15 "before the ship berthed" precede the actual departure 2026-05-14 18:10 in `13-TransportationStatus.xml` (broad, logistics, context).
- Emissions: 38 t MGO × 3.206 t CO2/t (IMO factor, own knowledge) = 121.8 t ≈ 122 t CO2e; flow meter 38.2 t; 38 t ≤ 120 t bunkered; about two days at 15–20 t/day (broad, logistics, money, context; recalculated by the merge).
- Ballast: 8 tanks, 4 in ballast, 4 exchanged, 0 not (4 + 0 = 4); 1240 t = 4 × 310 (310 m³ × 1.025 t/m³ = 318 t, close enough); 95 % meets the volumetric rule of the sequential method; discharge 120 m³ ≤ 310 m³; uptake 05-14 precedes exchange 05-16 precedes the planned discharge 05-18 (broad, logistics, context).
- Waste W-1: 0.6 m³ retained + 0.8 m³ until the next port = 1.4 m³ ≤ 8 m³ capacity (broad, logistics).
- Health: one ill person, no dead (`DiedIndicator` false), sanitary measure (disinfection 05-15) with `SanitaryMeasuresAppliedIndicator` true; SSCC on board with its indicator; no stowaways with its description (broad, context).
- ISPS: ISSC issued by the flag state's administration (Maritime Administration of Bayvarra; the ship is registered in Bayvarra), 2023 to 2028-09-30; security level 1 (broad, logistics, parties).
- Parties: reporter = sender = Tidewell Ocean Lines; authority = receiver = Maritime Administration of Lisavu, with the same identifier in party identification, legal entity and electronic address; Tidewell's description is identical in all 10 examples of the flow that describe it in full (parties, by script); ISIC 5012 / 5222 / 8413 fit carrier, port operator, transport regulator (parties). Passenger Ines Tavari and master Corin Halvard agree with `15-Manifest.xml`.
- `check_ids.py`: no identifier with a check digit in this example.

## Considered and refuted
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cbc:ID` = `XLSEL-26-0517`: the "0517" looked like a date that is not the arrival date (05-18) — refuted because the IDs are opaque references assigned by the port and match the manifest's original ETA of 05-17 (from broad, logistics).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`: the anchorage has exactly the Port of Lumeport's coordinates — refuted as a finding on its own by broad (one coordinate per port tile; the anchorage belongs to the port); the merge folds the point into F2, where the distance to Selanu, not the shared point, is the contradiction (from broad).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cbc:StowawayDescription` = `None found in the search before departure.`: suspected filler next to `StowawaysFoundOnBoardIndicator` false — refuted because it records that a search was made (from broad).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ShipsSurgeonPerson/cbc:FirstName` = `Elsbeth`: the chief officer as SSO and medical officer at once — refuted: on a small cargo ship without a doctor an officer is designated for medical care (STCW), and `MEDICAL` fits (from broad, parties).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:PassengerPerson/cbc:FamilyName` = `Tavari`: a passenger on a container feeder as filler — refuted: up to 12 passengers on cargo ships is real practice, the passenger list is part of the report, and the manifest carries the same passenger (from broad, context, parties).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:AdditionalSecurityMeasure/cbc:Description`: a gangway watch as an ordinary SSP measure — refuted: a port-specific watch beyond level-1 requirements is a legitimate additional measure (from context).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cbc:MedicalPractitionerConsultedIndicator`: contradicting treatment on board — refuted: radio medical advice is usual (from context).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:DischargeBallastWaterTransaction/cbc:TransactionDate` = `2026-05-18`: a discharge dated after the issue date — refuted because a pre-arrival ballast report declares the planned discharge (from context, logistics).
- `/CommonTransportationReport/cac:Shipment/cbc:ID` = `LD-SH-26-0132`: refuted by logistics (UBL places ship data under Shipment/ShipmentStage) — not followed by the merge; kept as F13 with logistics' argument (from logistics).
- `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:MMSIRegistrationID` = `298702117`: logistics could not check the MID; the merge checked it: MID 298 is unallocated (PROVENANCE-second-round.md line 206), no finding (from logistics).
- `/CommonTransportationReport/cac:ReporterParty`: the carrier rather than the master or agent as reporter — refuted: the operating carrier may submit the ship's reports, the master is `ReportingPerson` (from parties).
- `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: an Amount in an element defined as "the number of shares" — refuted as a finding of this example: the type is Amount in UBL itself; the definition text is UBL's inconsistency (TC write-up) (from parties).
- `/CommonTransportationReport/cac:AuthorityParty/cac:Language/cbc:ID`: Lisavan as the authority's language in an English report — refuted: it states the party's language, not the document's (from parties).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ShipStoreArticle[1]/cbc:Quantity` = `24`: bonded stores without a value for duty — refuted: stores under seal are declared by quantity; duty arises only if landed (from money).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:FuelConsumption/cac:FuelProviderParty/cac:PartyName/cbc:Name` = `Port of Lumeport`: a bunker purchase that should be billed in the flow — refuted: the report only states who supplied the fuel (from money).

## Changed in the merge
- broad/F1, context/F1, logistics/F1 and logistics/F2 → F1: combined (two positions at one time, and position/speed/arrival); one fix covers both.
- logistics/F4 and parties/F1 → F2: combined; kept High/yes. Broad and context had the map distance under "Outside this review"; the merge treats the contradiction inside this report as a finding.
- context/F2 split: the distance contradiction joins broad/F2 and logistics/F3 in F3 (High); the misuse of `NoControlActionsReason` joins broad/F3 in F6 (Medium, as broad), because the two conditions are independent.
- broad/F8 split: the company attributes join parties/F2 in F5 (Medium, as parties and all earlier flows' public-body findings); the ship-registry contact joins F11.
- broad/F11 (Low) → F8 (Medium, as parties/F4): the issuer does not meet the definition's "authorised Organisation".
- broad/F4 (Medium) → F15 (Low, as context, logistics, parties): nothing in the report claims a complete crew; the gap is completeness, the pre-arrival purpose is still served.
- context/F9 (NoStatus) Needs decision yes → no, aligned with all earlier flows (drop).
- parties/F5 Needs decision no → yes (F12), aligned with broad/F13 and the earlier flows' row on en-XB vs en-XL.
- broad/F14 split into F22 (registry port) and F23 (reference with ID only), two different conditions.
- broad/F7, parties/F6 → F11: all contacts grouped in one finding (as earlier flows).
- parties/F8, money/F1 → F10: combined.

## Outside this review
- The voyage Lumeport → Selanu takes from 2026-05-14 18:10 to 2026-05-18 06:30 across documents; with the map's coordinates the ports lie about 3 nm apart: a question of the world map's scale and timelines across flows (beyond F2, which covers the contradiction inside this report) (from broad, context).
- `15-Manifest.xml` (issued 2026-05-15 16:08) gives an estimated departure 2026-05-15 06:00, after the actual departure 2026-05-14 18:10 in `13-TransportationStatus.xml`; lies in the manifest (from broad, logistics).
- The same commercial-register description of public bodies and the bare `en` LocaleCode occur in many other examples; each belongs to that example's review (from parties).
