# LLM review: 16-CommonTransportationReport.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

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

### sea/16#F1 · High · The terminal operator's location lies 3 nautical miles from the Lumeport anchorage, against the distances the report states
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `1.20`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cbc:Name` = `Lumeport anchorage`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cac:Location/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `/CommonTransportationReport/cac:ReportingLocation/cbc:Name` = `At sea, 40 nautical miles off Selanu`
- Why: The Port of Selanu (terminal operator, on the island Lisavu) has its physical location at 40°01.20′S 15°08.40′W; the Lumeport anchorage in Bayvarra, in the same report, at 40°01.20′S 15°12.60′W, which is also the Port of Lumeport's own location (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`). The two ports differ by 4.2′ of longitude on the same latitude: 4.2 × cos 40.02° ≈ 3.2 nautical miles. The same report has the ship exchange ballast "120 nautical miles west of Selanu" (between Lumeport and Selanu, since the ship sails east), report "40 nautical miles off Selanu", and justify the exchange with "more than 200 nautical miles from land". Either the coordinates or the distances are wrong; with the coordinates as they are, the voyage from Lumeport to Selanu is 3 miles. The finding rests on the coordinates being geographic (EPSG 4326, as stated).
- Condition: The Port of Selanu's coordinates, the Lumeport anchorage's coordinates and the distances stated in the report agree (distance between the ports at least the 120 nautical miles the report implies).
- Options: (a) place the ports on coordinates that reflect the distances the story uses (preferred: the text distances are what the authority reads, and the same coordinates appear in other examples of the flow, so they should be fixed once at their source); (b) change the stated distances to fit a short crossing, which would also contradict the 200-mile ballast exchange.
- Needs decision: yes (the scale of the map and the distance between the countries is a world decision)

### sea/16#F2 · Medium · The maritime administration is described as a company in the commercial register
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC42270`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Maritime Administration of Lisavu is a public body. `PartyLegalEntity/CompanyID` is "an identifier for the party as registered within a company registration scheme", the scheme here is the "Island companies register" of type "Commercial register", and `CompanyLiquidationStatusCode` is "the party's liquidation status". A state administration is not registered as a company and cannot go into liquidation; the description gives it the attributes of a limited company. The world's CorporateRegistrationTypeCode list (COMMERCIAL, CHARITY, ASSOCIATION, FARM) has no code for public bodies. The same description is given to public bodies elsewhere: 26 `PartyLegalEntity` aggregates over `world/examples/*/*.xml` whose `RegistrationName` is a customs administration, the maritime administration or the Trade Accord Council carry `COMMERCIAL` and `ACTIVE` (counted with lxml over *.xml).
- Condition: The authority's legal entity does not claim registration in a commercial companies register and carries no liquidation status; if an identifier is kept, it is from a scheme for public bodies (or the party's identification only).
- Options: (a) drop `CompanyID`, `CorporateRegistrationScheme` and `CompanyLiquidationStatusCode` from public bodies and keep `RegistrationName` (preferred: no new list needed); (b) add a register of public bodies with its own registration type code and use it here.
- Needs decision: no

### sea/16#F3 · Medium · A language code in the reporter's LocaleCode
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value is the ISO 639 language code already given in `Language/cbc:ID`, with `listID="ISO 639"`, so it names no locale. Tidewell is a Bayvarran company, so a locale would be English in Bayvarra (the `en-XB` the flow uses in `languageID`). The same `LocaleCode` = `en` with `listID="ISO 639"` occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country), not a bare language code.
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred: nothing is lost); (b) give a locale such as `en-XB` with a list identifier that defines locales.
- Needs decision: no

### sea/16#F4 · Medium · The port company issues the ship sanitation control certificate and the medicine chest certificate
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:ShipSanitationControlCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:MedicalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- Why: `Certificate/IssuerParty` is "the authorised Organisation who issues this Certificate". The Port of Lumeport is the port company, "Port of Lumeport Ltd", a limited company in the commercial register (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Port of Lumeport Ltd`). Under the International Health Regulations (2005), Art. 39 and Annex 3 (own knowledge), a Ship Sanitation Control Certificate is issued by the competent (port health) authority at an authorised port; a medicine chest is certified by a port health authority or a pharmacist. A port company with a bunker barge is not the authorised organisation for either.
- Condition: The issuer of the ship sanitation control certificate is a health authority of the port state; the issuer of the medicine chest certificate is a party authorised to certify medicine chests.
- Options: (a) a port health authority of Bayvarra as issuer of both (preferred: one party, matches IHR practice); (b) keep the port as issuer and establish in the world that the port company is the designated competent authority, which IHR does not foresee for a company.
- Needs decision: yes (changes who the party is)

### sea/16#F5 · Low · The Lisavu parties' addresses and legal forms are written differently than in the other examples
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: The English renderings of the Port of Selanu's and the Maritime Administration's Lisavu addresses carry `languageID="en-XB"` (English as used in Bayvarra), and the port's legal form is given once, in English, without `languageID`. The same port in `17-TransportationStatus.xml` carries `en-XL` and its legal form in both languages (`17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). The same street and town are thus tagged with the issuer's locale rather than with the language the rendering is in. Over `world/examples/*/*.xml`, the English renderings of street and town names in Lisavu addresses carry `en-XL` 188 times, `en-XB` 141 times and `en-XU` 9 times; in the sea flow 66 `en-XB` and 48 `en-XL` (counted with lxml over *.xml, `StreetName`/`CityName` in aggregates with country `XL`).
- Condition: Each Lisavu party's address and legal form is described the same way in every example of the flow: the same `languageID` on the same rendering, and the legal form in the same languages.
- Options: (a) tag the English renderings of Lisavu names `en-XL` and give the legal form in Lisavan and English everywhere (preferred: the rendering belongs to the place, not to the writer of the document); (b) keep the issuer's locale, then state that convention once in the world's address rules.
- Needs decision: no

### sea/16#F6 · Low · The contacts given do not serve a ship arriving on Monday at 06:00
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Name` = `Ship registry`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Name` = `Port control`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Name` = `Bookings`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceTime` = `06:00:00`
- Why: The report announces the arrival on 2026-05-18 (a Monday) at 06:00, with port state control due. The authority's contact is its ship registry (the flag-state registration function, not arrivals or port state control) and is reachable on weekdays from 08:00; the terminal operator's contact is named "Port control" (a round-the-clock function) but is an operations planner with office hours; the reporter's contact for a regulatory report is its bookings desk. None of these can be reached when the ship arrives, and the authority's and reporter's contacts are not the functions that deal with a pre-arrival report.
- Condition: The authority's and the terminal operator's contacts are functions that handle ship arrivals and are reachable at the requested arrival time; the reporter's contact handles the ship's reporting (operations or the ship's agent), and name, job title and hours agree.
- Options: (a) role-specific contacts for the report (port control or harbour master's office, around the clock; the carrier's operations desk) (preferred); (b) keep master-data contacts and drop them where they do not serve the report.
- Needs decision: no

### sea/16#F7 · Low · The same security officer is coded with two different roles
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:RoleCode` = `SSO`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:SecurityOfficerPerson/cbc:RoleCode` = `CHIEFOFFICER`
- Why: Elsbeth Marrin is the ship security officer in both places (`SecurityOfficerPerson` of the stage and of the ISPS requirements, "the security officer responsible for these ISPS requirements"). In the stage she carries the role code "Ship security officer", in the ISPS requirements "Chief officer". In the role of security officer the code should say so in both places; her rank as chief officer is already stated in `CrewMemberPerson[2]`.
- Condition: Both `SecurityOfficerPerson` elements carry the same role code, the one for ship security officer.
- Options: (a) `SSO` in both (preferred: the element is the security role); (b) drop `RoleCode` in the ISPS requirements.
- Needs decision: no

### sea/16#F8 · Low · Tax registration and share capital of the reporter in a report to the maritime administration
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- Why: A pre-arrival report tells the maritime administration about ship, crew, health, waste, ballast and security; nothing in it is taxed and the reporter's share capital plays no part. The carrier's state sales-tax registration in Bayvarra and its capital stock look copied from its master data (the identical party appears in 10 examples of the flow). Section 4.8 of the review rules: data the document does nothing with.
- Condition: The reporter carries only the party data the report uses (identification, name, address, contact, legal registration if wanted).
- Options: (a) drop `PartyTaxScheme`, `CorporateStockAmount` and `FullyPaidSharesIndicator` from the reporter (preferred); (b) keep them, with a reason in the report that needs them.
- Needs decision: no

### sea/16#F9 · Low · Three crew members for a 9,940 GT container ship
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[1]/cbc:RoleCode` = `MASTER`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[3]/cbc:RoleCode` = `CHIEFENG`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:GrossTonnageMeasure` = `9940`
- Why: A pre-arrival report gives the authority the crew on board (the IMO FAL crew list). The report lists the master, chief officer and chief engineer only, while a feeder container ship of 9,940 GT sails with a minimum safe manning of about 12–16 (own knowledge), and the role list has a code `CREW` for ratings. Read as the crew list, it is incomplete; nothing says that only officers are listed.
- Condition: Either the crew list is complete for the ship, or the report says that only the officers are listed and why.
- Options: (a) list all crew, ratings with `CREW` (preferred if the report is meant as the crew list); (b) a note that the full crew list is submitted separately, with a document reference.
- Needs decision: no

## Checked and consistent
- Reporter, sender and signatory are the same party (Tidewell Ocean Lines, `20411918` in the Bayvarra register); authority and receiver are the same party (Maritime Administration of Lisavu, `IC42270`), with the same identifier in `PartyIdentification`, `PartyLegalEntity/CompanyID` and `ElectronicAddressID`.
- Tidewell's full description (address, tax scheme, legal entity, contact, electronic address) is identical in all 10 examples of the flow that describe it in full (07, 08, 12, 13, 14, 15, 16, 17, 18, 20); compared element by element with a script.
- Industry classifications fit the parties: ISIC 5012 for a sea freight carrier, 5222 for a port operator, 8413 for a transport regulator.
- The Port of Selanu as terminal operator matches the port of call (`XLSEL`, berth 2) and its description matches 17 apart from F5.
- The ISSC issuer is the flag state's administration (Maritime Administration of Bayvarra; the ship is registered in Bayvarra), which fits ISPS practice.
- The fuel provider (Port of Lumeport) matches the ship-to-ship record of bunkering from the Port of Lumeport's bunker barge.

## Considered and refuted
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:PassengerPerson/cbc:RoleCode`: a passenger on a container feeder without any reason looked like a filler — refuted because cargo ships may carry up to 12 passengers and a pre-arrival report carries the passenger list; nothing contradicts her presence.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ShipsSurgeonPerson/cbc:RoleCode`: the chief officer as the person responsible for health — refuted because ships without a doctor designate an officer in charge of medical care (STCW medical care training), and the role code `MEDICAL` fits that.
- `/CommonTransportationReport/cac:ReporterParty`: the carrier rather than the master or the ship's agent as reporter — refuted because the operating carrier may submit the ship's reports, and the master is named as `ReportingPerson`.
- `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: an amount in an element UBL defines as "the number of shares" — refuted as a finding of this example because the element's type is Amount in UBL itself; the definition text is UBL's inconsistency, not the example's.
- `/CommonTransportationReport/cac:AuthorityParty/cac:Language/cbc:ID`: Lisavan as the authority's language in an English report — refuted because it states the party's language, not the document's.

## Outside this review
- The same commercial-register description of public bodies (F2) and the bare `en` LocaleCode (F3) are in many other examples; each belongs to that example's review.
