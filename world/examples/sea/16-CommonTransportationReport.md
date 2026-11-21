# Common Transportation Report: Tidewell Ocean Lines to Maritime Administration of Lisavu

*Example 16 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Common Transportation Report in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-COMMON-TRANSPORTATION-REPORT-SCHEMA)*

Before entering Selanu the carrier reports to the island's maritime administration, the port state authority there. The ship flies Bayvarra's flag, so its security certificate was issued by Bayvarra's maritime administration, the flag state.

[The XML file](16-CommonTransportationReport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:common-transportation-report:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Common transportation report". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900668583**  
  The collaboration this document belongs to: Tidewell's report of the feeder's arrival at Selanu to the maritime administration. Tidewell Ocean Lines started it and gave it this identifier, which every document of it repeats.
- `ID` = **8600033430**  
  The carrier's report number.
- `UUID` = **cd4e897c-62e6-5fb8-90e8-b04d34a9df22**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-16**  
  Sent before the ship enters the port of Selanu.
- `IssueTime` = **15:40:00-01:00**  
  Sent a few hours before the ship comes off the port; in the issuer's local time, with its offset from UTC.
- `ReportTypeCode` = **PREARRIVAL** (listID `urn:ubl-examples:world:codelist:TransportReportTypeCode`)  
  The report before entering the port. The code is from the Trade Accord's transport report type list: PREARRIVAL = Pre-arrival report.
- `ReportType` = **Pre-arrival report**  
  The name of code PREARRIVAL in the Trade Accord's transport report type list.
- `Description` = **The ship's report before arrival at Selanu.**  
  What it is.
- `Note` = **Pilot requested at the Selanu fairway buoy at first light; the ship waits off the port under way overnight and berths without anchoring.**  
  The master's note on the arrival.
- `VersionID` = **1**  
  The first version.

### Reporter Party

Inside `ReporterParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; as Tidewell Ocean Lines gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Tidewell Ocean Lines gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. As Tidewell Ocean Lines gives it.
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. As Tidewell Ocean Lines gives it.
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Tidewell Ocean Lines gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Tidewell Ocean Lines gives it.
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). As Tidewell Ocean Lines gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Tidewell Ocean Lines gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; as Tidewell Ocean Lines gives it.
- `Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; as Tidewell Ocean Lines gives it.
- `Contact/Department` = **Bookings**  
  The department the desk belongs to; as Tidewell Ocean Lines gives it.
- `Contact/Telephone` = **+999 2 38 2058 7929**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Tidewell Ocean Lines gives it.
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  The contact's e-mail address; as Tidewell Ocean Lines gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Tidewell Ocean Lines gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Authority Party

Inside `AuthorityParty`:

- `PartyIdentification/ID` = **GOV-131** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Maritime Administration of Lisavu gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Maritime Administration of Lisavu**  
  The trading name; as Maritime Administration of Lisavu gives it.
- `PostalAddress/ID` = **44886737** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Maritime Administration of Lisavu gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Maritime Administration of Lisavu gives it.
- `PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Maritime Administration of Lisavu gives it.
- `PostalAddress/BuildingNumber` = **37**  
  Building number of the postal address. As Maritime Administration of Lisavu gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Maritime Administration of Lisavu gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Maritime Administration of Lisavu gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Ship registry**  
  The party's main desk, which handles this document; as Maritime Administration of Lisavu gives it.
- `Contact/JobTitle` = **Registrar of ships**  
  The job of the person who answers at the desk; as Maritime Administration of Lisavu gives it.
- `Contact/Department` = **Ship registry**  
  The department the desk belongs to; as Maritime Administration of Lisavu gives it.
- `Contact/Telephone` = **+999 3 720 7988**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Maritime Administration of Lisavu gives it.
- `Contact/ElectronicMail` = **ship@maritime-xl.example**  
  The contact's e-mail address; as Maritime Administration of Lisavu gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Maritime Administration of Lisavu gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:GOV-131** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Government list of public bodies of Lisavu; as Maritime Administration of Lisavu gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **GOV-131** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Maritime Administration of Lisavu**  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.

### Reporting Location

Inside `ReportingLocation`:

- `Name` = **At sea, 30 nautical miles off Selanu**  
  Where the report was made: the ship's distance to go at the time of the report.

### Shipment

Inside `Shipment`:

- `ID` = **TH-26-19E**  
  The ship's voyage the report is about: a report on the ship and all it carries, so its shipment is the voyage, not one shipper's consignment.
- `ShipmentStage/ID` = **2**  
  The sea leg to Selanu, stage 2 as on the bill of lading and the manifest.
- `ShipmentStage/CrewQuantity` = **14** (unitCode `IE`)  
  The crew on board: 14 persons; those with a function in this report are named below.
- `ShipmentStage/PassengerQuantity` = **1** (unitCode `IE`)  
  The one passenger, the supercargo travelling with the cargo.
- `ShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Port of Selanu gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `ShipmentStage/TerminalOperatorParty/PartyName/Name` = **Port of Selanu**  
  The trading name; as Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/ID` = **63597165** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **32**  
  Building number of the postal address. As Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `ShipmentStage/TerminalOperatorParty/Contact/Name` = **Port control**  
  The party's main desk, which handles this document; as Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Duty port controller**  
  The job of the person who answers at the desk; as Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/Contact/Department` = **Port operations**  
  The department the desk belongs to; as Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 3 727 7653**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **port@port-selanu.example**  
  The contact's e-mail address; as Port of Selanu gives it.
- `ShipmentStage/TerminalOperatorParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Port of Selanu gives it.
- `ShipmentStage/PassengerPerson/FirstName` = **Ines**  
  The one passenger, a supercargo.
- `ShipmentStage/PassengerPerson/FamilyName` = **Tavari**  
  The family name.
- `ShipmentStage/PassengerPerson/GenderCode` = **2** (listID `ISO 5218`)  
  As on the crew and passenger lists. The code is from the world's copy of ISO/IEC 5218 Representation of human sexes: 2 = Female.
- `ShipmentStage/PassengerPerson/RoleCode` = **PASSENGER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: PASSENGER = Passenger.
- `ShipmentStage/ReportingPerson/FirstName` = **Corin**  
  The master reports.
- `ShipmentStage/ReportingPerson/FamilyName` = **Halvard**  
  The family name.
- `ShipmentStage/ReportingPerson/RoleCode` = **MASTER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: MASTER = Master.
- `ShipmentStage/CrewMemberPerson/FirstName` = **Corin**  
  The master.
- `ShipmentStage/CrewMemberPerson/FamilyName` = **Halvard**  
  The family name.
- `ShipmentStage/CrewMemberPerson/GenderCode` = **1** (listID `ISO 5218`)  
  As on the crew and passenger lists. The code is from the world's copy of ISO/IEC 5218 Representation of human sexes: 1 = Male.
- `ShipmentStage/CrewMemberPerson/RoleCode` = **MASTER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: MASTER = Master.
- `ShipmentStage/CrewMemberPerson/FirstName` = **Elsbeth**  
  The chief officer, also the ship's medical officer.
- `ShipmentStage/CrewMemberPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/CrewMemberPerson/GenderCode` = **2** (listID `ISO 5218`)  
  As on the crew and passenger lists. The code is from the world's copy of ISO/IEC 5218 Representation of human sexes: 2 = Female.
- `ShipmentStage/CrewMemberPerson/RoleCode` = **CHIEFOFFICER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFOFFICER = Chief officer.
- `ShipmentStage/CrewMemberPerson/FirstName` = **Rafe**  
  The chief engineer.
- `ShipmentStage/CrewMemberPerson/FamilyName` = **Dunmore**  
  The family name.
- `ShipmentStage/CrewMemberPerson/GenderCode` = **1** (listID `ISO 5218`)  
  As on the crew and passenger lists. The code is from the world's copy of ISO/IEC 5218 Representation of human sexes: 1 = Male.
- `ShipmentStage/CrewMemberPerson/RoleCode` = **CHIEFENG** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFENG = Chief engineer.
- `ShipmentStage/SecurityOfficerPerson/FirstName` = **Elsbeth**  
  The ship security officer.
- `ShipmentStage/SecurityOfficerPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/SecurityOfficerPerson/RoleCode` = **SSO** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: SSO = Ship security officer.
- `ShipmentStage/ShipsSurgeonPerson/FirstName` = **Elsbeth**  
  No surgeon on a feeder: the chief officer is the medical officer.
- `ShipmentStage/ShipsSurgeonPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/ShipsSurgeonPerson/RoleCode` = **MEDICAL** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: MEDICAL = Medical officer.
- `ShipmentStage/DestinationPortCall/ID` = **XLSEL-26-0517**  
  The port call at Selanu.
- `ShipmentStage/DestinationPortCall/PlannedOperationsDescription` = **Discharge one container, load six.**  
  What the ship will do.
- `ShipmentStage/DestinationPortCall/PlannedWorksDescription` = **Overhaul of the No. 2 auxiliary engine alongside, about 8 hours; the main engine stays ready to sail.**  
  The works the ship plans in port: the port needs to know when a machine is out of service.
- `ShipmentStage/DestinationPortCall/PlannedInspectionsDescription` = **Port state control is due.**  
  An inspection is expected.
- `ShipmentStage/DestinationPortCall/ExpectedAnchorageIndicator` = **false**  
  Straight to the berth.
- `ShipmentStage/DestinationPortCall/PositionInPortID` = **BERTH-2**  
  The container berth.
- `ShipmentStage/DestinationPortCall/CargoAndBallastTankConditionDescription` = **Tanks clean; ballast exchanged at sea.**  
  Their condition.
- `ShipmentStage/DestinationPortCall/ShipRequirement/ID` = **SR-1**  
  A need of the ship.
- `ShipmentStage/DestinationPortCall/ShipRequirement/Description` = **Fresh water, 40 tonnes.**  
  What it needs.
- `ShipmentStage/DestinationPortCall/PrimaryPortCallPurpose/PurposeTypeCode` = **CARGO** (listID `urn:ubl-examples:world:codelist:PortCallPurposeCode`)  
  Cargo operations. The code is from the Trade Accord's port call purpose list: CARGO = Cargo operations.
- `ShipmentStage/DestinationPortCall/PrimaryPortCallPurpose/PurposeType` = **Cargo operations**  
  The name of code CARGO in the Trade Accord's port call purpose list.
- `ShipmentStage/DestinationPortCall/PrimaryPortCallPurpose/Description` = **Discharge and load containers.**  
  The purpose.
- `ShipmentStage/DestinationPortCall/AdditionalPortCallPurpose/PurposeTypeCode` = **WATER** (listID `urn:ubl-examples:world:codelist:PortCallPurposeCode`)  
  Taking on water. The code is from the Trade Accord's port call purpose list: WATER = Fresh water bunkering.
- `ShipmentStage/DestinationPortCall/AdditionalPortCallPurpose/PurposeType` = **Fresh water bunkering**  
  The name of code WATER in the Trade Accord's port call purpose list.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/IdentificationID` = **ARR-XLSEL-0517**  
  The requested arrival.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/OccurrenceDate` = **2026-05-17**  
  The morning after the ship comes off the port: Selanu's pilots take ships in by daylight only.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/OccurrenceTime` = **06:00:00+00:00**  
  At first light, in island time, with its offset from UTC.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/TypeCode` = **ARRIVAL** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  An arrival. The code is from the Trade Accord's transport event type list: ARRIVAL = Arrival.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/Description` = **Pilot on board at the fairway buoy.**  
  What is asked.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/CompletionIndicator` = **false**  
  Not yet.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/CurrentStatus/ConditionCode` = **ONTIME** (listID `urn:ubl-examples:world:codelist:StatusConditionCode`)  
  Expected on time. The code is from the Trade Accord's status condition list: ONTIME = On time.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/Contact/Name` = **Bridge**  
  Whom to call.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/Contact/Telephone` = **+999 2 7900 702 117**  
  The ship's phone, a Bayvarran mobile number, as the ship flies Bayvarra's flag.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/OccurrenceLocation/Name` = **Selanu fairway buoy**  
  Where the pilot boards.
- `ShipmentStage/DestinationPortCall/RequestedArrivalEvent/OccurrenceLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The buoy lies in Lisavu's waters, off the port of Selanu. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ShipmentStage/ShipStoreArticle/ID` = **ST-1**  
  Spirits in the bonded store.
- `ShipmentStage/ShipStoreArticle/Name` = **Spirits**  
  What.
- `ShipmentStage/ShipStoreArticle/Quantity` = **24** (unitCode `LTR`)  
  Litres.
- `ShipmentStage/ShipStoreArticle/OfficialUse` = **Sealed by customs at Lumeport.**  
  Under seal.
- `ShipmentStage/ShipStoreArticle/Stowage/LocationID` = **BOND-1**  
  The bonded locker.
- `ShipmentStage/ShipStoreArticle/Stowage/Location` = **Bonded locker, accommodation deck**  
  Where.
- `ShipmentStage/ShipStoreArticle/ID` = **ST-2**  
  Cigarettes.
- `ShipmentStage/ShipStoreArticle/Name` = **Cigarettes**  
  What.
- `ShipmentStage/ShipStoreArticle/Quantity` = **2000** (unitCode `EA`)  
  Pieces, counted each (EA).
- `ShipmentStage/CrewPersonEffect/EffectDescription` = **One camera, one laptop.**  
  What the crew member declares.
- `ShipmentStage/CrewPersonEffect/CrewPerson/FirstName` = **Rafe**  
  The chief engineer.
- `ShipmentStage/CrewPersonEffect/CrewPerson/FamilyName` = **Dunmore**  
  The family name.
- `ShipmentStage/CrewPersonEffect/CrewPerson/RoleCode` = **CHIEFENG** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFENG = Chief engineer.
- `ShipmentStage/MaritimeWaste/ID` = **W-1**  
  Oily waste.
- `ShipmentStage/MaritimeWaste/Description` = **Sludge from the fuel separators.**  
  What.
- `ShipmentStage/MaritimeWaste/WasteTypeCode` = **OIL** (listID `urn:ubl-examples:world:codelist:ShipWasteTypeCode`)  
  MARPOL Annex I waste. The code is from the Trade Accord's ship waste type list: OIL = Oily waste.
- `ShipmentStage/MaritimeWaste/ToBeDeliveredMeasure` = **2.4** (unitCode `MTQ`)  
  To be delivered at Selanu.
- `ShipmentStage/MaritimeWaste/RetainedOnBoardMeasure` = **0.6** (unitCode `MTQ`)  
  Kept on board.
- `ShipmentStage/MaritimeWaste/MaxDedicatedStorageCapacityMeasure` = **8** (unitCode `MTQ`)  
  The tank's capacity.
- `ShipmentStage/MaritimeWaste/EstimatedGeneratedUntilNextPortMeasure` = **0.8** (unitCode `MTQ`)  
  Until Lumeport again.
- `ShipmentStage/MaritimeWaste/RemainingWasteDeliveryPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/MaritimeWaste/RemainingWasteDeliveryPortLocation/Name` = **Port of Lumeport**  
  The rest goes ashore at Lumeport.
- `ShipmentStage/MaritimeWaste/RemainingWasteDeliveryPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/MaritimeWaste/ID` = **W-2**  
  Garbage.
- `ShipmentStage/MaritimeWaste/Description` = **Food and packaging waste.**  
  What.
- `ShipmentStage/MaritimeWaste/WasteTypeCode` = **GARBAGE** (listID `urn:ubl-examples:world:codelist:ShipWasteTypeCode`)  
  MARPOL Annex V waste. The code is from the Trade Accord's ship waste type list: GARBAGE = Garbage.
- `ShipmentStage/MaritimeWaste/ToBeDeliveredMeasure` = **1.5** (unitCode `MTQ`)  
  To be delivered.
- `ShipmentStage/BallastWaterSummary/ID` = **BW-26-0517**  
  The ballast water report.
- `ShipmentStage/BallastWaterSummary/ManagementPlanOnBoardIndicator` = **true**  
  The plan is on board.
- `ShipmentStage/BallastWaterSummary/ManagementPlanImplementedIndicator` = **true**  
  And followed.
- `ShipmentStage/BallastWaterSummary/IMOGuidelinesOnBoardIndicator` = **true**  
  The IMO guidelines are on board.
- `ShipmentStage/BallastWaterSummary/TotalBallastTanksOnBoardQuantity` = **8** (unitCode `EA`)  
  Ballast tanks.
- `ShipmentStage/BallastWaterSummary/TanksInBallastQuantity` = **4** (unitCode `EA`)  
  Tanks with ballast now.
- `ShipmentStage/BallastWaterSummary/TanksExchangedQuantity` = **4** (unitCode `EA`)  
  Exchanged at sea.
- `ShipmentStage/BallastWaterSummary/TanksNotExchangedQuantity` = **0** (unitCode `EA`)  
  None left unexchanged.
- `ShipmentStage/BallastWaterSummary/TotalBallastWaterOnBoardMeasure` = **1240** (unitCode `TNE`)  
  Ballast on board.
- `ShipmentStage/BallastWaterSummary/TotalBallastWaterCapacityMeasure` = **2480** (unitCode `TNE`)  
  The capacity.
- `ShipmentStage/BallastWaterSummary/OtherControlActions` = **Sediment flushed from the forepeak tank during the exchange and recorded in the ballast water record book.**  
  A control action besides the exchange: sediment management under the ballast water management plan.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankID` = **BT-1**  
  The tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankTypeCode` = **PEAK** (listID `urn:ubl-examples:world:codelist:BallastTankTypeCode`)  
  The fore peak tank, whose sediment was flushed during the exchange. The code is from the Trade Accord's ballast tank type list: PEAK = Peak tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Taken up at Lumeport: 310 cubic metres, a quarter of the 1,240 tonnes on board (a tonne of water is about a cubic metre).
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SeaHeightMeasure` = **2** (unitCode `MTR`)  
  The depth of the intake.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SalinityMeasure` = **30** (unitCode `GL`)  
  Salinity.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TransactionDate` = **2026-05-14**  
  At Lumeport.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Name` = **Port of Lumeport**  
  The port.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/AttributeID` = **WATER** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The water. The code is from the Trade Accord's temperature attribute list: WATER = Water temperature. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/Measure` = **16** (unitCode `CEL`)  
  Its temperature.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankID` = **BT-2**  
  The tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankTypeCode` = **DOUBLEBOTTOM** (listID `urn:ubl-examples:world:codelist:BallastTankTypeCode`)  
  A double bottom tank. The code is from the Trade Accord's ballast tank type list: DOUBLEBOTTOM = Double bottom tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Taken up at Lumeport: 310 cubic metres, a quarter of the 1,240 tonnes on board (a tonne of water is about a cubic metre).
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SeaHeightMeasure` = **2** (unitCode `MTR`)  
  The depth of the intake.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SalinityMeasure` = **30** (unitCode `GL`)  
  Salinity.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TransactionDate` = **2026-05-14**  
  At Lumeport.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Name` = **Port of Lumeport**  
  The port.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/AttributeID` = **WATER** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The water. The code is from the Trade Accord's temperature attribute list: WATER = Water temperature. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/Measure` = **16** (unitCode `CEL`)  
  Its temperature.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankID` = **BT-3**  
  The tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankTypeCode` = **WING** (listID `urn:ubl-examples:world:codelist:BallastTankTypeCode`)  
  A wing tank, port side. The code is from the Trade Accord's ballast tank type list: WING = Wing tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Taken up at Lumeport: 310 cubic metres, a quarter of the 1,240 tonnes on board (a tonne of water is about a cubic metre).
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SeaHeightMeasure` = **2** (unitCode `MTR`)  
  The depth of the intake.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SalinityMeasure` = **30** (unitCode `GL`)  
  Salinity.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TransactionDate` = **2026-05-14**  
  At Lumeport.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Name` = **Port of Lumeport**  
  The port.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/AttributeID` = **WATER** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The water. The code is from the Trade Accord's temperature attribute list: WATER = Water temperature. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/Measure` = **16** (unitCode `CEL`)  
  Its temperature.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankID` = **BT-4**  
  The tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TankTypeCode` = **WING** (listID `urn:ubl-examples:world:codelist:BallastTankTypeCode`)  
  A wing tank, starboard side. The code is from the Trade Accord's ballast tank type list: WING = Wing tank.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Taken up at Lumeport: 310 cubic metres, a quarter of the 1,240 tonnes on board (a tonne of water is about a cubic metre).
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SeaHeightMeasure` = **2** (unitCode `MTR`)  
  The depth of the intake.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/SalinityMeasure` = **30** (unitCode `GL`)  
  Salinity.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/TransactionDate` = **2026-05-14**  
  At Lumeport.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Name` = **Port of Lumeport**  
  The port.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/AttributeID` = **WATER** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The water. The code is from the Trade Accord's temperature attribute list: WATER = Water temperature. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/BallastWaterSummary/UptakeBallastWaterTransaction/BallastWaterTemperature/Measure` = **16** (unitCode `CEL`)  
  Its temperature.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TankID` = **BT-1**  
  The tank.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangeMethodCode` = **SEQ** (listID `urn:ubl-examples:world:codelist:BallastExchangeMethodCode`)  
  Emptied and refilled. The code is from the Trade Accord's ballast water exchange method list: SEQ = Sequential.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangedPercent` = **95**  
  Of the volume.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Exchanged: the same 310 cubic metres.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TransactionDate` = **2026-05-15**  
  At sea, half way across.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/Location/Name` = **At sea, about 320 nautical miles from Selanu, in mid-ocean**  
  Where: half way, far from any land.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TankID` = **BT-2**  
  The tank.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangeMethodCode` = **SEQ** (listID `urn:ubl-examples:world:codelist:BallastExchangeMethodCode`)  
  Emptied and refilled. The code is from the Trade Accord's ballast water exchange method list: SEQ = Sequential.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangedPercent` = **95**  
  Of the volume.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Exchanged: the same 310 cubic metres.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TransactionDate` = **2026-05-15**  
  At sea, half way across.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/Location/Name` = **At sea, about 320 nautical miles from Selanu, in mid-ocean**  
  Where: half way, far from any land.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TankID` = **BT-3**  
  The tank.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangeMethodCode` = **SEQ** (listID `urn:ubl-examples:world:codelist:BallastExchangeMethodCode`)  
  Emptied and refilled. The code is from the Trade Accord's ballast water exchange method list: SEQ = Sequential.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangedPercent` = **95**  
  Of the volume.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Exchanged: the same 310 cubic metres.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TransactionDate` = **2026-05-15**  
  At sea, half way across.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/Location/Name` = **At sea, about 320 nautical miles from Selanu, in mid-ocean**  
  Where: half way, far from any land.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TankID` = **BT-4**  
  The tank.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangeMethodCode` = **SEQ** (listID `urn:ubl-examples:world:codelist:BallastExchangeMethodCode`)  
  Emptied and refilled. The code is from the Trade Accord's ballast water exchange method list: SEQ = Sequential.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/ExchangedPercent` = **95**  
  Of the volume.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/VolumeMeasure` = **310** (unitCode `MTQ`)  
  Exchanged: the same 310 cubic metres.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/TransactionDate` = **2026-05-15**  
  At sea, half way across.
- `ShipmentStage/BallastWaterSummary/ExchangeBallastWaterTransaction/Location/Name` = **At sea, about 320 nautical miles from Selanu, in mid-ocean**  
  Where: half way, far from any land.
- `ShipmentStage/BallastWaterSummary/DischargeBallastWaterTransaction/TankID` = **BT-3**  
  The tank.
- `ShipmentStage/BallastWaterSummary/DischargeBallastWaterTransaction/VolumeMeasure` = **120** (unitCode `MTQ`)  
  To be discharged at Selanu: 120 cubic metres (a volume; a tonne of water is about a cubic metre, so the number stays).
- `ShipmentStage/BallastWaterSummary/DischargeBallastWaterTransaction/TransactionDate` = **2026-05-17**  
  In port.
- `ShipmentStage/BallastWaterSummary/ResponsibleOfficerPerson/FirstName` = **Elsbeth**  
  The chief officer, also the ship's medical officer.
- `ShipmentStage/BallastWaterSummary/ResponsibleOfficerPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/BallastWaterSummary/ResponsibleOfficerPerson/RoleCode` = **CHIEFOFFICER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFOFFICER = Chief officer.
- `ShipmentStage/ISPSRequirements/ID` = **ISSC-XB-2023-0117**  
  The number of the ship's International Ship Security Certificate, issued by its flag state, Bayvarra.
- `ShipmentStage/ISPSRequirements/ValidISSCIndicator` = **true**  
  The ship holds a valid security certificate.
- `ShipmentStage/ISPSRequirements/ISSCExpiryDate` = **2028-09-30**  
  The certificate is valid for five years from its issue.
- `ShipmentStage/ISPSRequirements/SSPOnBoardIndicator` = **true**  
  The security plan is on board.
- `ShipmentStage/ISPSRequirements/SSPSecurityMeasuresAppliedIndicator` = **true**  
  Its measures were applied.
- `ShipmentStage/ISPSRequirements/CurrentOperatingSecurityLevelCode` = **1** (listID `IMO ISPS security level`)  
  Security level 1, the normal level. The code is from the world's copy of IMO ISPS Code security level: 1 = Security level 1.
- `ShipmentStage/ISPSRequirements/AdditionalSecurityMeasure/ID` = **SM-1**  
  An extra measure.
- `ShipmentStage/ISPSRequirements/AdditionalSecurityMeasure/Description` = **Gangway watch at Selanu.**  
  What the ship adds.
- `ShipmentStage/ISPSRequirements/PortCallRecord/ID` = **PCR-1**  
  The last port call.
- `ShipmentStage/ISPSRequirements/PortCallRecord/SecurityLevelCode` = **1** (listID `IMO ISPS security level`)  
  Security level 1 at Lumeport. The code is from the world's copy of IMO ISPS Code security level: 1 = Security level 1.
- `ShipmentStage/ISPSRequirements/PortCallRecord/SecurityMeasure/Description` = **Normal access control.**  
  The measures.
- `ShipmentStage/ISPSRequirements/PortCallRecord/PortFacilityLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/ISPSRequirements/PortCallRecord/PortFacilityLocation/Name` = **Port of Lumeport**  
  The port facility.
- `ShipmentStage/ISPSRequirements/PortCallRecord/PortFacilityLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/ISPSRequirements/PortCallRecord/Period/StartDate` = **2026-05-13**  
  Arrived.
- `ShipmentStage/ISPSRequirements/PortCallRecord/Period/EndDate` = **2026-05-14**  
  Sailed.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/ID` = **STS-1**  
  The ship's one ship-to-ship activity in its last ten calls at port facilities, which the security information before arrival lists (SOLAS XI-2, regulation 9).
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Description` = **Bunkering: 120 tonnes of marine gas oil from the Port of Lumeport's bunker barge, alongside at the Lumeport anchorage, before the ship berthed.**  
  What the activity was.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/AppliedSecurityMeasure/ID` = **SM-STS-1**  
  The ship's measure for the transfer, from its security plan.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/AppliedSecurityMeasure/Description` = **The barge's crew list checked against the bunker order; access limited to the bunker station, with a deck watch for the whole transfer.**  
  What the ship did.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Period/StartDate` = **2026-05-13**  
  The day of the bunkering.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Period/StartTime` = **05:40:00-01:00**  
  The barge made fast; in the issuer's local time, with its offset from UTC.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Period/EndDate` = **2026-05-13**  
  The same morning.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Period/EndTime` = **08:15:00-01:00**  
  The barge cast off; in the issuer's local time, with its offset from UTC.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/Name` = **Lumeport anchorage**  
  Where the barge came alongside.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/LocationCoordinate/LatitudeDegreesMeasure` = **31** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/LocationCoordinate/LatitudeMinutesMeasure` = **6.22** (unitCode `D61`)  
  The minutes of the latitude.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/LocationCoordinate/LongitudeDegreesMeasure` = **13** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/LocationCoordinate/LongitudeMinutesMeasure` = **23.07** (unitCode `D61`)  
  The minutes of the longitude.
- `ShipmentStage/ISPSRequirements/ShipToShipActivityRecord/Location/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `ShipmentStage/ISPSRequirements/ReportLocation/Name` = **At sea, 30 nautical miles off Selanu**  
  Where the report is made, as the report's own reporting location.
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyIdentification/ID` = **5389612047** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Bayvarra's flag state administration: keeps the register of Bayvarran ships and issues their international ship security certificates under the ISPS Code. Referenced only, as the issuer of the certificate of Tidewell Ocean Lines' ship. Its identifier and name are enough (referenced).
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyName/Name` = **Maritime Administration of Bayvarra**  
  Bayvarra's flag state administration: keeps the register of Bayvarran ships and issues their international ship security certificates under the ISPS Code. Referenced only, as the issuer of the certificate of Tidewell Ocean Lines' ship. Its identifier and name are enough (referenced).
- `ShipmentStage/ISPSRequirements/SecurityOfficerPerson/FirstName` = **Elsbeth**  
  The chief officer, also the ship's medical officer.
- `ShipmentStage/ISPSRequirements/SecurityOfficerPerson/FamilyName` = **Marrin**  
  The family name.
- `ShipmentStage/ISPSRequirements/SecurityOfficerPerson/RoleCode` = **SSO** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The same person as the stage's ship security officer, in the same role. The code is from the Trade Accord's role on board list: SSO = Ship security officer.
- `ShipmentStage/MaritimeHealthDeclaration/ID` = **MDH-26-0517**  
  The maritime declaration of health.
- `ShipmentStage/MaritimeHealthDeclaration/InfectiousDiseaseCaseOnBoardIndicator` = **false**  
  No infectious disease.
- `ShipmentStage/MaritimeHealthDeclaration/MoreIllThanExpectedIndicator` = **false**  
  No more ill than usual.
- `ShipmentStage/MaritimeHealthDeclaration/MedicalPractitionerConsultedIndicator` = **true**  
  A doctor was consulted by radio.
- `ShipmentStage/MaritimeHealthDeclaration/StowawaysFoundOnBoardIndicator` = **false**  
  No stowaways.
- `ShipmentStage/MaritimeHealthDeclaration/SickAnimalOnBoardIndicator` = **false**  
  No sick animals.
- `ShipmentStage/MaritimeHealthDeclaration/FumigatedCargoTransportIndicator` = **false**  
  No fumigated cargo.
- `ShipmentStage/MaritimeHealthDeclaration/SanitaryMeasuresAppliedIndicator` = **true**  
  The galley was disinfected.
- `ShipmentStage/MaritimeHealthDeclaration/ValidSanitationCertificateOnBoardIndicator` = **true**  
  The certificate is valid.
- `ShipmentStage/MaritimeHealthDeclaration/ReinspectionRequiredIndicator` = **false**  
  No reinspection needed.
- `ShipmentStage/MaritimeHealthDeclaration/TotalDeadPersonQuantity` = **0** (unitCode `IE`)  
  No persons.
- `ShipmentStage/MaritimeHealthDeclaration/TotalIllPersonQuantity` = **1** (unitCode `IE`)  
  One person: a crew member who was seasick.
- `ShipmentStage/MaritimeHealthDeclaration/StowawayDescription` = **None found in the search before departure.**  
  The search.
- `ShipmentStage/MaritimeHealthDeclaration/LastDrinkingWaterAnalysisDate` = **2026-04-02**  
  The last water test.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/ID` = **HI-1**  
  The one incident.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/JoinedShipDate` = **2025-11-01**  
  When the person joined.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/NatureOfIllnessDescription` = **Seasickness in the swell of the open ocean.**  
  What the illness was: a mild one, not infectious.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/OnsetDate` = **2026-05-15**  
  On the first full day at sea.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/ReportedToMedicalOfficerIndicator` = **true**  
  Reported.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/GivenTreatmentDescription` = **Tablets against seasickness and rest.**  
  Treatment.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/StillIllIndicator` = **true**  
  Still recovering.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/DiedIndicator` = **false**  
  No.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/StillOnBoardIndicator` = **true**  
  On board.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/EvacuatedIndicator` = **false**  
  Not evacuated.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/BuriedAtSeaIndicator` = **false**  
  No.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/Note` = **Fit for light duty.**  
  The status.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/Person/FirstName` = **Rafe**  
  The chief engineer.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/Person/FamilyName` = **Dunmore**  
  The family name.
- `ShipmentStage/MaritimeHealthDeclaration/PersonnelHealthIncident/Person/RoleCode` = **CHIEFENG** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: CHIEFENG = Chief engineer.
- `ShipmentStage/MaritimeHealthDeclaration/SanitaryMeasure/SanitaryMeasureTypeCode` = **DISINFECT** (listID `urn:ubl-examples:world:codelist:SanitaryMeasureCode`)  
  The galley was disinfected. The code is from the Trade Accord's sanitary measure list: DISINFECT = Disinfection.
- `ShipmentStage/MaritimeHealthDeclaration/SanitaryMeasure/ApplicationDate` = **2026-05-15**  
  When.
- `ShipmentStage/MaritimeHealthDeclaration/PlaceOfReportLocation/Name` = **At sea, 30 nautical miles off Selanu**  
  Where the report is made, as the report's own reporting location.
- `ShipmentStage/MaritimeHealthDeclaration/MedicalCertificate/ID` = **MC-TH-2026**  
  The ship's medicine chest certificate, unique only with its issuer, the port health office of its home port.
- `ShipmentStage/MaritimeHealthDeclaration/MedicalCertificate/CertificateType` = **Medicine chest**  
  Its kind.
- `ShipmentStage/MaritimeHealthDeclaration/MedicalCertificate/IssuerParty/PartyIdentification/ID` = **7140583926** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Bayvarra's port health authority at Lumeport, an office of the federal health administration, as the Maritime Administration is federal: under the International Health Regulations (2005) it inspects ships in the port and issues their ship sanitation control and exemption certificates (Annex 3) and the medicine chest certificates of Bayvarran ships. Referenced only, as the issuer of the certificates of Tidewell Ocean Lines' ships. Its identifier and name are enough (referenced).
- `ShipmentStage/MaritimeHealthDeclaration/MedicalCertificate/IssuerParty/PartyName/Name` = **Port Health Office of Bayvarra, Lumeport**  
  Bayvarra's port health authority at Lumeport, an office of the federal health administration, as the Maritime Administration is federal: under the International Health Regulations (2005) it inspects ships in the port and issues their ship sanitation control and exemption certificates (Annex 3) and the medicine chest certificates of Bayvarran ships. Referenced only, as the issuer of the certificates of Tidewell Ocean Lines' ships. Its identifier and name are enough (referenced).
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlCertificate/ID` = **SSCC-XB-2026-0318**  
  The ship sanitation control certificate (International Health Regulations, Annex 3), issued at Lumeport on 18 March 2026: the inspection found traces of cockroaches in the galley stores, which were treated. It replaced the exemption certificate the ship had carried until then. Unique only with its issuer.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlCertificate/CertificateType` = **Ship sanitation control**  
  Its kind.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlCertificate/IssuerParty/PartyIdentification/ID` = **7140583926** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Bayvarra's port health authority at Lumeport, an office of the federal health administration, as the Maritime Administration is federal: under the International Health Regulations (2005) it inspects ships in the port and issues their ship sanitation control and exemption certificates (Annex 3) and the medicine chest certificates of Bayvarran ships. Referenced only, as the issuer of the certificates of Tidewell Ocean Lines' ships. Its identifier and name are enough (referenced).
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlCertificate/IssuerParty/PartyName/Name` = **Port Health Office of Bayvarra, Lumeport**  
  Bayvarra's port health authority at Lumeport, an office of the federal health administration, as the Maritime Administration is federal: under the International Health Regulations (2005) it inspects ships in the port and issues their ship sanitation control and exemption certificates (Annex 3) and the medicine chest certificates of Bayvarran ships. Referenced only, as the issuer of the certificates of Tidewell Ocean Lines' ships. Its identifier and name are enough (referenced).
- `ShipmentStage/FuelConsumption/ID` = **FC-26-19E**  
  The fuel of the voyage.
- `ShipmentStage/FuelConsumption/FuelTypeCode` = **MGO** (listID `urn:ubl-examples:world:codelist:FuelTypeCode`)  
  Marine gas oil. The code is from the Trade Accord's fuel type list: MGO = Marine gas oil.
- `ShipmentStage/FuelConsumption/FuelType` = **Marine gas oil, 0.1 % sulphur**  
  In words.
- `ShipmentStage/FuelConsumption/FuelConsumptionMeasure` = **38** (unitCode `TNE`)  
  Used from Lumeport.
- `ShipmentStage/FuelConsumption/AdditionalFuelProperty/TypeID` = **Sulphur**  
  The sulphur content.
- `ShipmentStage/FuelConsumption/AdditionalFuelProperty/Value` = **0.1 %**  
  Its value.
- `ShipmentStage/FuelConsumption/FuelMetering/TypeID` = **FlowMeter**  
  Measured by the flow meter.
- `ShipmentStage/FuelConsumption/FuelMetering/Value` = **38.2 t**  
  The reading.
- `ShipmentStage/FuelConsumption/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  Carbon dioxide. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `ShipmentStage/FuelConsumption/EnvironmentalEmission/ValueMeasure` = **122** (unitCode `TNE`)  
  From 38 t of gas oil.
- `ShipmentStage/FuelConsumption/FuelProviderParty/PartyIdentification/ID` = **20411781** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ShipmentStage/FuelConsumption/FuelProviderParty/PartyName/Name` = **Port of Lumeport**  
  A party referred to from another party's details: its identifier and name are enough.

### Transport Means

Inside `TransportMeans`:

- `JourneyID` = **TH-26-19E**  
  The voyage.
- `RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `DirectionCode` = **EB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: EB = Eastbound.
- `TransportMeansTypeCode` = **1511** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tidewell Harbour; the fleet of Tidewell Ocean Lines. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 1511 = Full container ship/cellular vessel.
- `MaritimeTransport/VesselID` = **XB-S-20117** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships.
- `MaritimeTransport/VesselName` = **Tidewell Harbour**  
  The vessel's name; the fleet of Tidewell Ocean Lines.
- `MaritimeTransport/RadioCallSignID` = **QBTH7**  
  The radio call sign, in Bayvarra's call sign series QB: no ITU series starts with Q, so the sign belongs to no real station.
- `MaritimeTransport/MMSIRegistrationID` = **298702117**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 298 of Bayvarra, which the ITU has not allocated to any real country, and the ship's six digits.
- `MaritimeTransport/ShipsRequirements` = **Shore power at the container quay.**  
  What the ship needs in port.
- `MaritimeTransport/GrossTonnageMeasure` = **9940** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `MaritimeTransport/NetTonnageMeasure` = **5120** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `MaritimeTransport/SegregatedBallastMeasure` = **2480** (unitCode `TNE`)  
  The capacity of the tanks for ballast water only.
- `MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 1,000 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `MaritimeTransport/AntennaLocus` = **Mast, 28 m above the waterline**  
  Where the AIS antenna is.
- `MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20117**  
  The ship's certificate of registry.
- `MaritimeTransport/RegistryPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.
- `MaritimeTransport/VesselDynamics/NavigationStatusCode` = **0** (listID `ITU-R M.1371 Navigational status`)  
  The AIS navigational status: under way. The code is from the world's copy of ITU-R M.1371 AIS navigational status: 0 = Under way.
- `MaritimeTransport/VesselDynamics/AtAnchorageIndicator` = **false**  
  Not at anchor.
- `MaritimeTransport/VesselDynamics/CourseOverGroundDirection` = **088**  
  Course over ground, in degrees.
- `MaritimeTransport/VesselDynamics/SpeedOverGroundMeasure` = **13.5** (unitCode `KNT`)  
  Speed over ground.
- `MaritimeTransport/VesselDynamics/RateOfTurnMeasure` = **0** (unitCode `E96`)  
  Not turning: 0 degrees per second.

### Document Reference

Inside `DocumentReference`:

- `ID` = **8500033423**  
  The cargo manifest.
- `DocumentTypeCode` = **Manifest** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 8500033423 is the example sea/15, a Manifest; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Manifest.

### Signature

Inside `Signature`:

- `ID` = **TWL-SIG-CTR**  
  The master's signature.
- `SignatoryParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Tidewell Ocean Lines**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CommonTransportationReport xmlns="urn:oasis:names:specification:ubl:schema:xsd:CommonTransportationReport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:common-transportation-report:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900668583</cbc:ProfileExecutionID>
  <cbc:ID>8600033430</cbc:ID>
  <cbc:UUID>cd4e897c-62e6-5fb8-90e8-b04d34a9df22</cbc:UUID>
  <cbc:IssueDate>2026-05-16</cbc:IssueDate>
  <cbc:IssueTime>15:40:00-01:00</cbc:IssueTime>
  <cbc:ReportTypeCode listID="urn:ubl-examples:world:codelist:TransportReportTypeCode">PREARRIVAL</cbc:ReportTypeCode>
  <cbc:ReportType>Pre-arrival report</cbc:ReportType>
  <cbc:Description>The ship's report before arrival at Selanu.</cbc:Description>
  <cbc:Note>Pilot requested at the Selanu fairway buoy at first light; the ship waits off the port under way overnight and berths without anchoring.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ReporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-547539</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>18</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38527</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Bookings</cbc:Name>
      <cbc:JobTitle>Booking agent</cbc:JobTitle>
      <cbc:Department>Bookings</cbc:Department>
      <cbc:Telephone>+999 2 38 2058 7929</cbc:Telephone>
      <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReporterParty>
  <cac:AuthorityParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-131</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Maritime Administration of Lisavu</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">44886737</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>37</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Ship registry</cbc:Name>
      <cbc:JobTitle>Registrar of ships</cbc:JobTitle>
      <cbc:Department>Ship registry</cbc:Department>
      <cbc:Telephone>+999 3 720 7988</cbc:Telephone>
      <cbc:ElectronicMail>ship@maritime-xl.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:GOV-131</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:AuthorityParty>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-131</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Maritime Administration of Lisavu</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:ReportingLocation>
    <cbc:Name>At sea, 30 nautical miles off Selanu</cbc:Name>
  </cac:ReportingLocation>
  <cac:Shipment>
    <cbc:ID>TH-26-19E</cbc:ID>
    <cac:ShipmentStage>
      <cbc:ID>2</cbc:ID>
      <cbc:CrewQuantity unitCode="IE">14</cbc:CrewQuantity>
      <cbc:PassengerQuantity unitCode="IE">1</cbc:PassengerQuantity>
      <cac:TerminalOperatorParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Port of Selanu</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">63597165</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
          <cbc:BuildingNumber>32</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Port control</cbc:Name>
          <cbc:JobTitle>Duty port controller</cbc:JobTitle>
          <cbc:Department>Port operations</cbc:Department>
          <cbc:Telephone>+999 3 727 7653</cbc:Telephone>
          <cbc:ElectronicMail>port@port-selanu.example</cbc:ElectronicMail>
          <cbc:Note>Every day, around the clock</cbc:Note>
        </cac:Contact>
      </cac:TerminalOperatorParty>
      <cac:PassengerPerson>
        <cbc:FirstName>Ines</cbc:FirstName>
        <cbc:FamilyName>Tavari</cbc:FamilyName>
        <cbc:GenderCode listID="ISO 5218">2</cbc:GenderCode>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">PASSENGER</cbc:RoleCode>
      </cac:PassengerPerson>
      <cac:ReportingPerson>
        <cbc:FirstName>Corin</cbc:FirstName>
        <cbc:FamilyName>Halvard</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">MASTER</cbc:RoleCode>
      </cac:ReportingPerson>
      <cac:CrewMemberPerson>
        <cbc:FirstName>Corin</cbc:FirstName>
        <cbc:FamilyName>Halvard</cbc:FamilyName>
        <cbc:GenderCode listID="ISO 5218">1</cbc:GenderCode>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">MASTER</cbc:RoleCode>
      </cac:CrewMemberPerson>
      <cac:CrewMemberPerson>
        <cbc:FirstName>Elsbeth</cbc:FirstName>
        <cbc:FamilyName>Marrin</cbc:FamilyName>
        <cbc:GenderCode listID="ISO 5218">2</cbc:GenderCode>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFOFFICER</cbc:RoleCode>
      </cac:CrewMemberPerson>
      <cac:CrewMemberPerson>
        <cbc:FirstName>Rafe</cbc:FirstName>
        <cbc:FamilyName>Dunmore</cbc:FamilyName>
        <cbc:GenderCode listID="ISO 5218">1</cbc:GenderCode>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFENG</cbc:RoleCode>
      </cac:CrewMemberPerson>
      <cac:SecurityOfficerPerson>
        <cbc:FirstName>Elsbeth</cbc:FirstName>
        <cbc:FamilyName>Marrin</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">SSO</cbc:RoleCode>
      </cac:SecurityOfficerPerson>
      <cac:ShipsSurgeonPerson>
        <cbc:FirstName>Elsbeth</cbc:FirstName>
        <cbc:FamilyName>Marrin</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">MEDICAL</cbc:RoleCode>
      </cac:ShipsSurgeonPerson>
      <cac:DestinationPortCall>
        <cbc:ID>XLSEL-26-0517</cbc:ID>
        <cbc:PlannedOperationsDescription>Discharge one container, load six.</cbc:PlannedOperationsDescription>
        <cbc:PlannedWorksDescription>Overhaul of the No. 2 auxiliary engine alongside, about 8 hours; the main engine stays ready to sail.</cbc:PlannedWorksDescription>
        <cbc:PlannedInspectionsDescription>Port state control is due.</cbc:PlannedInspectionsDescription>
        <cbc:ExpectedAnchorageIndicator>false</cbc:ExpectedAnchorageIndicator>
        <cbc:PositionInPortID>BERTH-2</cbc:PositionInPortID>
        <cbc:CargoAndBallastTankConditionDescription>Tanks clean; ballast exchanged at sea.</cbc:CargoAndBallastTankConditionDescription>
        <cac:ShipRequirement>
          <cbc:ID>SR-1</cbc:ID>
          <cbc:Description>Fresh water, 40 tonnes.</cbc:Description>
        </cac:ShipRequirement>
        <cac:PrimaryPortCallPurpose>
          <cbc:PurposeTypeCode listID="urn:ubl-examples:world:codelist:PortCallPurposeCode">CARGO</cbc:PurposeTypeCode>
          <cbc:PurposeType>Cargo operations</cbc:PurposeType>
          <cbc:Description>Discharge and load containers.</cbc:Description>
        </cac:PrimaryPortCallPurpose>
        <cac:AdditionalPortCallPurpose>
          <cbc:PurposeTypeCode listID="urn:ubl-examples:world:codelist:PortCallPurposeCode">WATER</cbc:PurposeTypeCode>
          <cbc:PurposeType>Fresh water bunkering</cbc:PurposeType>
        </cac:AdditionalPortCallPurpose>
        <cac:RequestedArrivalEvent>
          <cbc:IdentificationID>ARR-XLSEL-0517</cbc:IdentificationID>
          <cbc:OccurrenceDate>2026-05-17</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:00:00+00:00</cbc:OccurrenceTime>
          <cbc:TypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">ARRIVAL</cbc:TypeCode>
          <cbc:Description>Pilot on board at the fairway buoy.</cbc:Description>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:CurrentStatus>
            <cbc:ConditionCode listID="urn:ubl-examples:world:codelist:StatusConditionCode">ONTIME</cbc:ConditionCode>
          </cac:CurrentStatus>
          <cac:Contact>
            <cbc:Name>Bridge</cbc:Name>
            <cbc:Telephone>+999 2 7900 702 117</cbc:Telephone>
          </cac:Contact>
          <cac:OccurrenceLocation>
            <cbc:Name>Selanu fairway buoy</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:OccurrenceLocation>
        </cac:RequestedArrivalEvent>
      </cac:DestinationPortCall>
      <cac:ShipStoreArticle>
        <cbc:ID>ST-1</cbc:ID>
        <cbc:Name>Spirits</cbc:Name>
        <cbc:Quantity unitCode="LTR">24</cbc:Quantity>
        <cbc:OfficialUse>Sealed by customs at Lumeport.</cbc:OfficialUse>
        <cac:Stowage>
          <cbc:LocationID>BOND-1</cbc:LocationID>
          <cbc:Location>Bonded locker, accommodation deck</cbc:Location>
        </cac:Stowage>
      </cac:ShipStoreArticle>
      <cac:ShipStoreArticle>
        <cbc:ID>ST-2</cbc:ID>
        <cbc:Name>Cigarettes</cbc:Name>
        <cbc:Quantity unitCode="EA">2000</cbc:Quantity>
      </cac:ShipStoreArticle>
      <cac:CrewPersonEffect>
        <cbc:EffectDescription>One camera, one laptop.</cbc:EffectDescription>
        <cac:CrewPerson>
          <cbc:FirstName>Rafe</cbc:FirstName>
          <cbc:FamilyName>Dunmore</cbc:FamilyName>
          <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFENG</cbc:RoleCode>
        </cac:CrewPerson>
      </cac:CrewPersonEffect>
      <cac:MaritimeWaste>
        <cbc:ID>W-1</cbc:ID>
        <cbc:Description>Sludge from the fuel separators.</cbc:Description>
        <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:ShipWasteTypeCode">OIL</cbc:WasteTypeCode>
        <cbc:ToBeDeliveredMeasure unitCode="MTQ">2.4</cbc:ToBeDeliveredMeasure>
        <cbc:RetainedOnBoardMeasure unitCode="MTQ">0.6</cbc:RetainedOnBoardMeasure>
        <cbc:MaxDedicatedStorageCapacityMeasure unitCode="MTQ">8</cbc:MaxDedicatedStorageCapacityMeasure>
        <cbc:EstimatedGeneratedUntilNextPortMeasure unitCode="MTQ">0.8</cbc:EstimatedGeneratedUntilNextPortMeasure>
        <cac:RemainingWasteDeliveryPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:RemainingWasteDeliveryPortLocation>
      </cac:MaritimeWaste>
      <cac:MaritimeWaste>
        <cbc:ID>W-2</cbc:ID>
        <cbc:Description>Food and packaging waste.</cbc:Description>
        <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:ShipWasteTypeCode">GARBAGE</cbc:WasteTypeCode>
        <cbc:ToBeDeliveredMeasure unitCode="MTQ">1.5</cbc:ToBeDeliveredMeasure>
      </cac:MaritimeWaste>
      <cac:BallastWaterSummary>
        <cbc:ID>BW-26-0517</cbc:ID>
        <cbc:ManagementPlanOnBoardIndicator>true</cbc:ManagementPlanOnBoardIndicator>
        <cbc:ManagementPlanImplementedIndicator>true</cbc:ManagementPlanImplementedIndicator>
        <cbc:IMOGuidelinesOnBoardIndicator>true</cbc:IMOGuidelinesOnBoardIndicator>
        <cbc:TotalBallastTanksOnBoardQuantity unitCode="EA">8</cbc:TotalBallastTanksOnBoardQuantity>
        <cbc:TanksInBallastQuantity unitCode="EA">4</cbc:TanksInBallastQuantity>
        <cbc:TanksExchangedQuantity unitCode="EA">4</cbc:TanksExchangedQuantity>
        <cbc:TanksNotExchangedQuantity unitCode="EA">0</cbc:TanksNotExchangedQuantity>
        <cbc:TotalBallastWaterOnBoardMeasure unitCode="TNE">1240</cbc:TotalBallastWaterOnBoardMeasure>
        <cbc:TotalBallastWaterCapacityMeasure unitCode="TNE">2480</cbc:TotalBallastWaterCapacityMeasure>
        <cbc:OtherControlActions>Sediment flushed from the forepeak tank during the exchange and recorded in the ballast water record book.</cbc:OtherControlActions>
        <cac:UptakeBallastWaterTransaction>
          <cbc:TankID>BT-1</cbc:TankID>
          <cbc:TankTypeCode listID="urn:ubl-examples:world:codelist:BallastTankTypeCode">PEAK</cbc:TankTypeCode>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:SeaHeightMeasure unitCode="MTR">2</cbc:SeaHeightMeasure>
          <cbc:SalinityMeasure unitCode="GL">30</cbc:SalinityMeasure>
          <cbc:TransactionDate>2026-05-14</cbc:TransactionDate>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
          <cac:BallastWaterTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">WATER</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">16</cbc:Measure>
          </cac:BallastWaterTemperature>
        </cac:UptakeBallastWaterTransaction>
        <cac:UptakeBallastWaterTransaction>
          <cbc:TankID>BT-2</cbc:TankID>
          <cbc:TankTypeCode listID="urn:ubl-examples:world:codelist:BallastTankTypeCode">DOUBLEBOTTOM</cbc:TankTypeCode>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:SeaHeightMeasure unitCode="MTR">2</cbc:SeaHeightMeasure>
          <cbc:SalinityMeasure unitCode="GL">30</cbc:SalinityMeasure>
          <cbc:TransactionDate>2026-05-14</cbc:TransactionDate>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
          <cac:BallastWaterTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">WATER</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">16</cbc:Measure>
          </cac:BallastWaterTemperature>
        </cac:UptakeBallastWaterTransaction>
        <cac:UptakeBallastWaterTransaction>
          <cbc:TankID>BT-3</cbc:TankID>
          <cbc:TankTypeCode listID="urn:ubl-examples:world:codelist:BallastTankTypeCode">WING</cbc:TankTypeCode>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:SeaHeightMeasure unitCode="MTR">2</cbc:SeaHeightMeasure>
          <cbc:SalinityMeasure unitCode="GL">30</cbc:SalinityMeasure>
          <cbc:TransactionDate>2026-05-14</cbc:TransactionDate>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
          <cac:BallastWaterTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">WATER</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">16</cbc:Measure>
          </cac:BallastWaterTemperature>
        </cac:UptakeBallastWaterTransaction>
        <cac:UptakeBallastWaterTransaction>
          <cbc:TankID>BT-4</cbc:TankID>
          <cbc:TankTypeCode listID="urn:ubl-examples:world:codelist:BallastTankTypeCode">WING</cbc:TankTypeCode>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:SeaHeightMeasure unitCode="MTR">2</cbc:SeaHeightMeasure>
          <cbc:SalinityMeasure unitCode="GL">30</cbc:SalinityMeasure>
          <cbc:TransactionDate>2026-05-14</cbc:TransactionDate>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
          <cac:BallastWaterTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">WATER</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">16</cbc:Measure>
          </cac:BallastWaterTemperature>
        </cac:UptakeBallastWaterTransaction>
        <cac:ExchangeBallastWaterTransaction>
          <cbc:TankID>BT-1</cbc:TankID>
          <cbc:ExchangeMethodCode listID="urn:ubl-examples:world:codelist:BallastExchangeMethodCode">SEQ</cbc:ExchangeMethodCode>
          <cbc:ExchangedPercent>95</cbc:ExchangedPercent>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:TransactionDate>2026-05-15</cbc:TransactionDate>
          <cac:Location>
            <cbc:Name>At sea, about 320 nautical miles from Selanu, in mid-ocean</cbc:Name>
          </cac:Location>
        </cac:ExchangeBallastWaterTransaction>
        <cac:ExchangeBallastWaterTransaction>
          <cbc:TankID>BT-2</cbc:TankID>
          <cbc:ExchangeMethodCode listID="urn:ubl-examples:world:codelist:BallastExchangeMethodCode">SEQ</cbc:ExchangeMethodCode>
          <cbc:ExchangedPercent>95</cbc:ExchangedPercent>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:TransactionDate>2026-05-15</cbc:TransactionDate>
          <cac:Location>
            <cbc:Name>At sea, about 320 nautical miles from Selanu, in mid-ocean</cbc:Name>
          </cac:Location>
        </cac:ExchangeBallastWaterTransaction>
        <cac:ExchangeBallastWaterTransaction>
          <cbc:TankID>BT-3</cbc:TankID>
          <cbc:ExchangeMethodCode listID="urn:ubl-examples:world:codelist:BallastExchangeMethodCode">SEQ</cbc:ExchangeMethodCode>
          <cbc:ExchangedPercent>95</cbc:ExchangedPercent>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:TransactionDate>2026-05-15</cbc:TransactionDate>
          <cac:Location>
            <cbc:Name>At sea, about 320 nautical miles from Selanu, in mid-ocean</cbc:Name>
          </cac:Location>
        </cac:ExchangeBallastWaterTransaction>
        <cac:ExchangeBallastWaterTransaction>
          <cbc:TankID>BT-4</cbc:TankID>
          <cbc:ExchangeMethodCode listID="urn:ubl-examples:world:codelist:BallastExchangeMethodCode">SEQ</cbc:ExchangeMethodCode>
          <cbc:ExchangedPercent>95</cbc:ExchangedPercent>
          <cbc:VolumeMeasure unitCode="MTQ">310</cbc:VolumeMeasure>
          <cbc:TransactionDate>2026-05-15</cbc:TransactionDate>
          <cac:Location>
            <cbc:Name>At sea, about 320 nautical miles from Selanu, in mid-ocean</cbc:Name>
          </cac:Location>
        </cac:ExchangeBallastWaterTransaction>
        <cac:DischargeBallastWaterTransaction>
          <cbc:TankID>BT-3</cbc:TankID>
          <cbc:VolumeMeasure unitCode="MTQ">120</cbc:VolumeMeasure>
          <cbc:TransactionDate>2026-05-17</cbc:TransactionDate>
        </cac:DischargeBallastWaterTransaction>
        <cac:ResponsibleOfficerPerson>
          <cbc:FirstName>Elsbeth</cbc:FirstName>
          <cbc:FamilyName>Marrin</cbc:FamilyName>
          <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFOFFICER</cbc:RoleCode>
        </cac:ResponsibleOfficerPerson>
      </cac:BallastWaterSummary>
      <cac:ISPSRequirements>
        <cbc:ID>ISSC-XB-2023-0117</cbc:ID>
        <cbc:ValidISSCIndicator>true</cbc:ValidISSCIndicator>
        <cbc:ISSCExpiryDate>2028-09-30</cbc:ISSCExpiryDate>
        <cbc:SSPOnBoardIndicator>true</cbc:SSPOnBoardIndicator>
        <cbc:SSPSecurityMeasuresAppliedIndicator>true</cbc:SSPSecurityMeasuresAppliedIndicator>
        <cbc:CurrentOperatingSecurityLevelCode listID="IMO ISPS security level">1</cbc:CurrentOperatingSecurityLevelCode>
        <cac:AdditionalSecurityMeasure>
          <cbc:ID>SM-1</cbc:ID>
          <cbc:Description>Gangway watch at Selanu.</cbc:Description>
        </cac:AdditionalSecurityMeasure>
        <cac:PortCallRecord>
          <cbc:ID>PCR-1</cbc:ID>
          <cbc:SecurityLevelCode listID="IMO ISPS security level">1</cbc:SecurityLevelCode>
          <cac:SecurityMeasure>
            <cbc:Description>Normal access control.</cbc:Description>
          </cac:SecurityMeasure>
          <cac:PortFacilityLocation>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:PortFacilityLocation>
          <cac:Period>
            <cbc:StartDate>2026-05-13</cbc:StartDate>
            <cbc:EndDate>2026-05-14</cbc:EndDate>
          </cac:Period>
        </cac:PortCallRecord>
        <cac:ShipToShipActivityRecord>
          <cbc:ID>STS-1</cbc:ID>
          <cbc:Description>Bunkering: 120 tonnes of marine gas oil from the Port of Lumeport's bunker barge, alongside at the Lumeport anchorage, before the ship berthed.</cbc:Description>
          <cac:AppliedSecurityMeasure>
            <cbc:ID>SM-STS-1</cbc:ID>
            <cbc:Description>The barge's crew list checked against the bunker order; access limited to the bunker station, with a deck watch for the whole transfer.</cbc:Description>
          </cac:AppliedSecurityMeasure>
          <cac:Period>
            <cbc:StartDate>2026-05-13</cbc:StartDate>
            <cbc:StartTime>05:40:00-01:00</cbc:StartTime>
            <cbc:EndDate>2026-05-13</cbc:EndDate>
            <cbc:EndTime>08:15:00-01:00</cbc:EndTime>
          </cac:Period>
          <cac:Location>
            <cbc:Name>Lumeport anchorage</cbc:Name>
            <cac:LocationCoordinate>
              <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
              <cbc:LatitudeDegreesMeasure unitCode="DD">31</cbc:LatitudeDegreesMeasure>
              <cbc:LatitudeMinutesMeasure unitCode="D61">6.22</cbc:LatitudeMinutesMeasure>
              <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
              <cbc:LongitudeDegreesMeasure unitCode="DD">13</cbc:LongitudeDegreesMeasure>
              <cbc:LongitudeMinutesMeasure unitCode="D61">23.07</cbc:LongitudeMinutesMeasure>
              <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
            </cac:LocationCoordinate>
          </cac:Location>
        </cac:ShipToShipActivityRecord>
        <cac:ReportLocation>
          <cbc:Name>At sea, 30 nautical miles off Selanu</cbc:Name>
        </cac:ReportLocation>
        <cac:ISSCIssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">5389612047</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Maritime Administration of Bayvarra</cbc:Name>
          </cac:PartyName>
        </cac:ISSCIssuerParty>
        <cac:SecurityOfficerPerson>
          <cbc:FirstName>Elsbeth</cbc:FirstName>
          <cbc:FamilyName>Marrin</cbc:FamilyName>
          <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">SSO</cbc:RoleCode>
        </cac:SecurityOfficerPerson>
      </cac:ISPSRequirements>
      <cac:MaritimeHealthDeclaration>
        <cbc:ID>MDH-26-0517</cbc:ID>
        <cbc:InfectiousDiseaseCaseOnBoardIndicator>false</cbc:InfectiousDiseaseCaseOnBoardIndicator>
        <cbc:MoreIllThanExpectedIndicator>false</cbc:MoreIllThanExpectedIndicator>
        <cbc:MedicalPractitionerConsultedIndicator>true</cbc:MedicalPractitionerConsultedIndicator>
        <cbc:StowawaysFoundOnBoardIndicator>false</cbc:StowawaysFoundOnBoardIndicator>
        <cbc:SickAnimalOnBoardIndicator>false</cbc:SickAnimalOnBoardIndicator>
        <cbc:FumigatedCargoTransportIndicator>false</cbc:FumigatedCargoTransportIndicator>
        <cbc:SanitaryMeasuresAppliedIndicator>true</cbc:SanitaryMeasuresAppliedIndicator>
        <cbc:ValidSanitationCertificateOnBoardIndicator>true</cbc:ValidSanitationCertificateOnBoardIndicator>
        <cbc:ReinspectionRequiredIndicator>false</cbc:ReinspectionRequiredIndicator>
        <cbc:TotalDeadPersonQuantity unitCode="IE">0</cbc:TotalDeadPersonQuantity>
        <cbc:TotalIllPersonQuantity unitCode="IE">1</cbc:TotalIllPersonQuantity>
        <cbc:StowawayDescription>None found in the search before departure.</cbc:StowawayDescription>
        <cbc:LastDrinkingWaterAnalysisDate>2026-04-02</cbc:LastDrinkingWaterAnalysisDate>
        <cac:PersonnelHealthIncident>
          <cbc:ID>HI-1</cbc:ID>
          <cbc:JoinedShipDate>2025-11-01</cbc:JoinedShipDate>
          <cbc:NatureOfIllnessDescription>Seasickness in the swell of the open ocean.</cbc:NatureOfIllnessDescription>
          <cbc:OnsetDate>2026-05-15</cbc:OnsetDate>
          <cbc:ReportedToMedicalOfficerIndicator>true</cbc:ReportedToMedicalOfficerIndicator>
          <cbc:GivenTreatmentDescription>Tablets against seasickness and rest.</cbc:GivenTreatmentDescription>
          <cbc:StillIllIndicator>true</cbc:StillIllIndicator>
          <cbc:DiedIndicator>false</cbc:DiedIndicator>
          <cbc:StillOnBoardIndicator>true</cbc:StillOnBoardIndicator>
          <cbc:EvacuatedIndicator>false</cbc:EvacuatedIndicator>
          <cbc:BuriedAtSeaIndicator>false</cbc:BuriedAtSeaIndicator>
          <cbc:Note>Fit for light duty.</cbc:Note>
          <cac:Person>
            <cbc:FirstName>Rafe</cbc:FirstName>
            <cbc:FamilyName>Dunmore</cbc:FamilyName>
            <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">CHIEFENG</cbc:RoleCode>
          </cac:Person>
        </cac:PersonnelHealthIncident>
        <cac:SanitaryMeasure>
          <cbc:SanitaryMeasureTypeCode listID="urn:ubl-examples:world:codelist:SanitaryMeasureCode">DISINFECT</cbc:SanitaryMeasureTypeCode>
          <cbc:ApplicationDate>2026-05-15</cbc:ApplicationDate>
        </cac:SanitaryMeasure>
        <cac:PlaceOfReportLocation>
          <cbc:Name>At sea, 30 nautical miles off Selanu</cbc:Name>
        </cac:PlaceOfReportLocation>
        <cac:MedicalCertificate>
          <cbc:ID>MC-TH-2026</cbc:ID>
          <cbc:CertificateType>Medicine chest</cbc:CertificateType>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">7140583926</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Port Health Office of Bayvarra, Lumeport</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:MedicalCertificate>
        <cac:ShipSanitationControlCertificate>
          <cbc:ID>SSCC-XB-2026-0318</cbc:ID>
          <cbc:CertificateType>Ship sanitation control</cbc:CertificateType>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">7140583926</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Port Health Office of Bayvarra, Lumeport</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:ShipSanitationControlCertificate>
      </cac:MaritimeHealthDeclaration>
      <cac:FuelConsumption>
        <cbc:ID>FC-26-19E</cbc:ID>
        <cbc:FuelTypeCode listID="urn:ubl-examples:world:codelist:FuelTypeCode">MGO</cbc:FuelTypeCode>
        <cbc:FuelType>Marine gas oil, 0.1 % sulphur</cbc:FuelType>
        <cbc:FuelConsumptionMeasure unitCode="TNE">38</cbc:FuelConsumptionMeasure>
        <cac:AdditionalFuelProperty>
          <cbc:TypeID>Sulphur</cbc:TypeID>
          <cbc:Value>0.1 %</cbc:Value>
        </cac:AdditionalFuelProperty>
        <cac:FuelMetering>
          <cbc:TypeID>FlowMeter</cbc:TypeID>
          <cbc:Value>38.2 t</cbc:Value>
        </cac:FuelMetering>
        <cac:EnvironmentalEmission>
          <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
          <cbc:ValueMeasure unitCode="TNE">122</cbc:ValueMeasure>
        </cac:EnvironmentalEmission>
        <cac:FuelProviderParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411781</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Port of Lumeport</cbc:Name>
          </cac:PartyName>
        </cac:FuelProviderParty>
      </cac:FuelConsumption>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:TransportMeans>
    <cbc:JourneyID>TH-26-19E</cbc:JourneyID>
    <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
    <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
    <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">EB</cbc:DirectionCode>
    <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">1511</cbc:TransportMeansTypeCode>
    <cac:MaritimeTransport>
      <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20117</cbc:VesselID>
      <cbc:VesselName>Tidewell Harbour</cbc:VesselName>
      <cbc:RadioCallSignID>QBTH7</cbc:RadioCallSignID>
      <cbc:MMSIRegistrationID>298702117</cbc:MMSIRegistrationID>
      <cbc:ShipsRequirements>Shore power at the container quay.</cbc:ShipsRequirements>
      <cbc:GrossTonnageMeasure unitCode="C62">9940</cbc:GrossTonnageMeasure>
      <cbc:NetTonnageMeasure unitCode="C62">5120</cbc:NetTonnageMeasure>
      <cbc:SegregatedBallastMeasure unitCode="TNE">2480</cbc:SegregatedBallastMeasure>
      <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
      <cbc:AntennaLocus>Mast, 28 m above the waterline</cbc:AntennaLocus>
      <cac:RegistryCertificateDocumentReference>
        <cbc:ID>REG-XB-S-20117</cbc:ID>
      </cac:RegistryCertificateDocumentReference>
      <cac:RegistryPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
        <cbc:Name>Lumeport</cbc:Name>
      </cac:RegistryPortLocation>
      <cac:VesselDynamics>
        <cbc:NavigationStatusCode listID="ITU-R M.1371 Navigational status">0</cbc:NavigationStatusCode>
        <cbc:AtAnchorageIndicator>false</cbc:AtAnchorageIndicator>
        <cbc:CourseOverGroundDirection>088</cbc:CourseOverGroundDirection>
        <cbc:SpeedOverGroundMeasure unitCode="KNT">13.5</cbc:SpeedOverGroundMeasure>
        <cbc:RateOfTurnMeasure unitCode="E96">0</cbc:RateOfTurnMeasure>
      </cac:VesselDynamics>
    </cac:MaritimeTransport>
  </cac:TransportMeans>
  <cac:DocumentReference>
    <cbc:ID>8500033423</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Manifest</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>TWL-SIG-CTR</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</CommonTransportationReport>
```
