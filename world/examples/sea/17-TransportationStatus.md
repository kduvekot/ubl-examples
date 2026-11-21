# Transportation Status: Port of Selanu to Bayforth Forwarding

*Example 17 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The port of discharge reports the container discharged and available.

[The XML file](17-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:transportation-status:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Transportation status". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **BYF-TX-26-2501**  
  The collaboration this document belongs to: the sea carriage Bayforth books with Tidewell Ocean Lines. Bayforth Forwarding started it and gave it this identifier, which every document of it repeats.
- `ID` = **POS-TS-26-8988**  
  The sender's status report number.
- `UUID` = **1713d8c6-6d60-56cc-af96-b2eb848695b4**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-17**  
  Reported when the container is discharged.
- `IssueTime` = **16:36:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Name` = **Transportation status**  
  The kind of report.
- `Description` = **Container TWLU4120872 discharged and available for customs clearance.**  
  In words.
- `Note` = **Automatic report from the sender's tracking system.**  
  How it was made.
- `ShippingOrderID` = **BYF-FI-26-1501**  
  The forwarding instructions of the shipment it reports on.
- `OtherInstruction` = **Reply only if the delivery slot must change.**  
  What the receiver should do, with the slot it is about.
- `TransportExecutionStatusCode` = **INPROGRESS** (listID `urn:ubl-examples:world:codelist:TransportExecutionStatusCode`)  
  The carriage is under way. The code is from the Trade Accord's transport execution status list: INPROGRESS = In progress.

### Consignment

Inside `Consignment`:

- `ID` = **LMW-CS-26-1001**  
  The consignment the report is about.
- `ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Velumi Trading gives it.
- `ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Velumi Trading gives it.
- `ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Velumi Trading gives it.
- `ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Velumi Trading gives it.
- `ConsigneeParty/Contact/Telephone` = **+999 3 729 5794**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Velumi Trading gives it.
- `ConsigneeParty/Contact/ElectronicMail` = **goodsin@velumi.example**  
  The contact's e-mail address; as Velumi Trading gives it.
- `ConsigneeParty/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.
- `CarrierParty/PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; as Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CarrierParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `CarrierParty/PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. As Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. As Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). As Tidewell Ocean Lines gives it.
- `CarrierParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `CarrierParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Tidewell Ocean Lines gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CarrierParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `CarrierParty/Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/Department` = **Bookings**  
  The department the desk belongs to; as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/Telephone` = **+999 2 38 2058 7929**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/ElectronicMail` = **bookings@tidewell.example**  
  The contact's e-mail address; as Tidewell Ocean Lines gives it.
- `CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Tidewell Ocean Lines gives it.
- `MainCarriageShipmentStage/ID` = **2**  
  The sea leg, stage 2 as on the bill of lading.
- `MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceDate` = **2026-05-17**  
  The container came off the ship.
- `MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceTime` = **11:20:00+00:00**  
  The local time of Lisavu, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/DischargeTransportEvent/CompletionIndicator` = **true**  
  Whether the event has taken place (true) or is still to come (false).
- `MainCarriageShipmentStage/DischargeTransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/DischargeTransportEvent/Location/Name` = **Port of Selanu**  
  At the Port of Selanu.
- `MainCarriageShipmentStage/DischargeTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Port of Selanu gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Port of Selanu**  
  The trading name; as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/Name` = **English**  
  The language's name.
- `MainCarriageShipmentStage/TerminalOperatorParty/Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/ID` = **63597165** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **32**  
  Building number of the postal address. As Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/Description` = **Port of Selanu**  
  Where the party actually operates, apart from its postal address.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/InformationURI` = **https://www.port-selanu.example**  
  A page about the place itself: the port's or the airport's own site, with its access and services.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **32** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **56.22** (unitCode `D61`)  
  The minutes of the latitude.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **2** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **9.76** (unitCode `D61`)  
  The minutes of the longitude.
- `MainCarriageShipmentStage/TerminalOperatorParty/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Port control**  
  The party's main desk, which handles this document; as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/JobTitle` = **Duty port controller**  
  The job of the person who answers at the desk; as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Department` = **Port operations**  
  The department the desk belongs to; as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Telephone` = **+999 3 727 7653**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **port@port-selanu.example**  
  The contact's e-mail address; as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Port of Selanu gives it.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41037** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Port of Selanu gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/OccurrenceDate` = **2026-05-17**  
  The ship berthed at Selanu: its pilot boarded at first light; it had been off the port, under way, since the evening.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/OccurrenceTime` = **06:30:00+00:00**  
  The local time of Lisavu, where it happens, with its offset from UTC.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/Location/Name` = **Port of Selanu**  
  At the Port of Selanu.
- `MainCarriageShipmentStage/ActualArrivalTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `MainCarriageShipmentStage/ReportingPerson/FirstName` = **Ama**  
  The terminal's duty officer who reports.
- `MainCarriageShipmentStage/ReportingPerson/FamilyName` = **Kelune**  
  The family name.
- `MainCarriageShipmentStage/ReportingPerson/JobTitle` = **Duty officer**  
  The person's position.
- `TransportHandlingUnit/TransportEquipment/ID` = **TWLU4120872** (schemeID `ISO6346`)  
  The container.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/OccurrenceDate` = **2026-05-17**  
  The container held from 12:00 at the plant health check of its pallets: the hold is the container's, not the ship's.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/OccurrenceTime` = **12:00:00+00:00**  
  The local time of Lisavu, where it happens, with its offset from UTC.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/Description` = **Held for a check of the pallets: wooden pallets must carry the heat-treatment mark, and one mark is illegible, so customs inspects the container tomorrow, 18 May.**  
  What happened, in words.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/Location/Name` = **Port of Selanu**  
  At the Port of Selanu.
- `TransportHandlingUnit/TransportEquipment/QuarantineTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/OccurrenceDate` = **2026-05-17**  
  Stacked in the import yard.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/OccurrenceTime` = **11:40:00+00:00**  
  The local time of Lisavu, where it happens, with its offset from UTC.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/TransportEventTypeCode` = **STORAGE** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  The kind of event, as the carriers of the world code them. The code is from the Trade Accord's transport event type list: STORAGE = Stored.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/Location/Name` = **Port of Selanu**  
  At the Port of Selanu.
- `TransportHandlingUnit/TransportEquipment/TransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-05-17**  
  The day the event took place.
- `TransportEventTypeCode` = **DISCHARGE** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  The kind of event, as the carriers of the world code them. The code is from the Trade Accord's transport event type list: DISCHARGE = Discharged.
- `Description` = **Container TWLU4120872 discharged and available for customs clearance.**  
  What happened, in words.
- `Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Location/Name` = **Port of Selanu**  
  Where it happened.

### Document Reference

Inside `DocumentReference`:

- `ID` = **TWLU000033415**  
  The transport document of the consignment.
- `DocumentTypeCode` = **BillOfLading** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: TWLU000033415 is the example sea/14, a BillOfLading; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: BillOfLading = Bill Of Lading.

### Signature

Inside `Signature`:

- `ID` = **PS-SIG-TS-17**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Port of Selanu**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Port of Selanu**  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; as Bayforth Forwarding gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-953846** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Bayforth Forwarding gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. As Bayforth Forwarding gives it.
- `PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. As Bayforth Forwarding gives it.
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Bayforth Forwarding gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bayforth Forwarding gives it.
- `PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). As Bayforth Forwarding gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bayforth Forwarding gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Export desk**  
  The party's export desk: the desk for its role in this document (it handles the transport of goods between the countries); as Bayforth Forwarding gives it.
- `Contact/JobTitle` = **Export coordinator**  
  The job of the person who answers at the desk; as Bayforth Forwarding gives it.
- `Contact/Department` = **Export**  
  The department the desk belongs to; as Bayforth Forwarding gives it.
- `Contact/Telephone` = **+999 2 38 5155 2404**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Bayforth Forwarding gives it.
- `Contact/ElectronicMail` = **export@bayforth.example**  
  The contact's e-mail address; as Bayforth Forwarding gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Bayforth Forwarding gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Status Location

Inside `StatusLocation`:

- `ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Name` = **Port of Selanu**  
  Where it happened.

### Status Period

Inside `StatusPeriod`:

- `StartDate` = **2026-05-17**  
  The status holds from the report.
- `EndDate` = **2026-05-17**  
  Until the next report.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:transportation-status:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>BYF-TX-26-2501</cbc:ProfileExecutionID>
  <cbc:ID>POS-TS-26-8988</cbc:ID>
  <cbc:UUID>1713d8c6-6d60-56cc-af96-b2eb848695b4</cbc:UUID>
  <cbc:IssueDate>2026-05-17</cbc:IssueDate>
  <cbc:IssueTime>16:36:00+00:00</cbc:IssueTime>
  <cbc:Name>Transportation status</cbc:Name>
  <cbc:Description>Container TWLU4120872 discharged and available for customs clearance.</cbc:Description>
  <cbc:Note>Automatic report from the sender's tracking system.</cbc:Note>
  <cbc:ShippingOrderID>BYF-FI-26-1501</cbc:ShippingOrderID>
  <cbc:OtherInstruction>Reply only if the delivery slot must change.</cbc:OtherInstruction>
  <cbc:TransportExecutionStatusCode listID="urn:ubl-examples:world:codelist:TransportExecutionStatusCode">INPROGRESS</cbc:TransportExecutionStatusCode>
  <cac:Consignment>
    <cbc:ID>LMW-CS-26-1001</cbc:ID>
    <cac:ConsigneeParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40351721</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Contact>
        <cbc:Name>Goods-in</cbc:Name>
        <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
        <cbc:Department>Warehouse</cbc:Department>
        <cbc:Telephone>+999 3 729 5794</cbc:Telephone>
        <cbc:ElectronicMail>goodsin@velumi.example</cbc:ElectronicMail>
        <cbc:Note>Monday to Saturday 09:00–18:00</cbc:Note>
      </cac:Contact>
    </cac:ConsigneeParty>
    <cac:CarrierParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tidewell Ocean Lines</cbc:Name>
      </cac:PartyName>
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
    </cac:CarrierParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>2</cbc:ID>
      <cac:DischargeTransportEvent>
        <cbc:OccurrenceDate>2026-05-17</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>11:20:00+00:00</cbc:OccurrenceTime>
        <cbc:CompletionIndicator>true</cbc:CompletionIndicator>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:DischargeTransportEvent>
      <cac:TerminalOperatorParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Port of Selanu</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
        </cac:Language>
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
        <cac:PhysicalLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Description>Port of Selanu</cbc:Description>
          <cbc:InformationURI>https://www.port-selanu.example</cbc:InformationURI>
          <cac:LocationCoordinate>
            <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
            <cbc:LatitudeDegreesMeasure unitCode="DD">32</cbc:LatitudeDegreesMeasure>
            <cbc:LatitudeMinutesMeasure unitCode="D61">56.22</cbc:LatitudeMinutesMeasure>
            <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
            <cbc:LongitudeDegreesMeasure unitCode="DD">2</cbc:LongitudeDegreesMeasure>
            <cbc:LongitudeMinutesMeasure unitCode="D61">9.76</cbc:LongitudeMinutesMeasure>
            <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
          </cac:LocationCoordinate>
        </cac:PhysicalLocation>
        <cac:Contact>
          <cbc:Name>Port control</cbc:Name>
          <cbc:JobTitle>Duty port controller</cbc:JobTitle>
          <cbc:Department>Port operations</cbc:Department>
          <cbc:Telephone>+999 3 727 7653</cbc:Telephone>
          <cbc:ElectronicMail>port@port-selanu.example</cbc:ElectronicMail>
          <cbc:Note>Every day, around the clock</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41037</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
      <cac:ActualArrivalTransportEvent>
        <cbc:OccurrenceDate>2026-05-17</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>06:30:00+00:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:ActualArrivalTransportEvent>
      <cac:ReportingPerson>
        <cbc:FirstName>Ama</cbc:FirstName>
        <cbc:FamilyName>Kelune</cbc:FamilyName>
        <cbc:JobTitle>Duty officer</cbc:JobTitle>
      </cac:ReportingPerson>
    </cac:MainCarriageShipmentStage>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">TWLU4120872</cbc:ID>
        <cac:QuarantineTransportEvent>
          <cbc:OccurrenceDate>2026-05-17</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>12:00:00+00:00</cbc:OccurrenceTime>
          <cbc:Description>Held for a check of the pallets: wooden pallets must carry the heat-treatment mark, and one mark is illegible, so customs inspects the container tomorrow, 18 May.</cbc:Description>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
            <cbc:Name>Port of Selanu</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:QuarantineTransportEvent>
        <cac:TransportEvent>
          <cbc:OccurrenceDate>2026-05-17</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>11:40:00+00:00</cbc:OccurrenceTime>
          <cbc:TransportEventTypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">STORAGE</cbc:TransportEventTypeCode>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
            <cbc:Name>Port of Selanu</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:TransportEvent>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-05-17</cbc:OccurrenceDate>
    <cbc:TransportEventTypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">DISCHARGE</cbc:TransportEventTypeCode>
    <cbc:Description>Container TWLU4120872 discharged and available for customs clearance.</cbc:Description>
    <cac:Location>
      <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
      <cbc:Name>Port of Selanu</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
  <cac:DocumentReference>
    <cbc:ID>TWLU000033415</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">BillOfLading</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>PS-SIG-TS-17</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Port of Selanu</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Port of Selanu</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-953846</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Dockside Way</cbc:StreetName>
      <cbc:BuildingNumber>4</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38525</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Export desk</cbc:Name>
      <cbc:JobTitle>Export coordinator</cbc:JobTitle>
      <cbc:Department>Export</cbc:Department>
      <cbc:Telephone>+999 2 38 5155 2404</cbc:Telephone>
      <cbc:ElectronicMail>export@bayforth.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:StatusLocation>
    <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
    <cbc:Name>Port of Selanu</cbc:Name>
  </cac:StatusLocation>
  <cac:StatusPeriod>
    <cbc:StartDate>2026-05-17</cbc:StartDate>
    <cbc:EndDate>2026-05-17</cbc:EndDate>
  </cac:StatusPeriod>
</TransportationStatus>
```
