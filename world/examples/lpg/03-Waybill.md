# Waybill: Gullhaven Tank Haulage to Kelpstone Gas

*Example 3 of the flow "Propane by road tanker to Lumeport's district heating (dangerous goods, domestic, Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The haulier's consignment note under Bayvarra's road carriage law, with the dangerous goods as loaded in the tank: the orange plates 23 over 1965, the placard and the tunnel restriction.

[The XML file](03-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **LPG-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **GTH-WB-26-0899**  
  The consignment note number.
- `CarrierAssignedID` = **GTH-NATROAD-26-0895**  
  The carrier's own number for the carriage.
- `UUID` = **1bcd7f24-a71e-5869-ae2d-2b2aab46d19b**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-06-10**  
  Issued at the plant when the haulier took over the loaded tank.
- `IssueTime` = **06:50:00-01:00**  
  After the tanker was weighed full; in the issuer's local time, with its offset from UTC (D27).
- `Name` = **Consignment note under the national road carriage law**  
  The kind of transport document.
- `Description` = **The tanker carries the propane from the gas plant to the water company's peak boilers in Lumeport.**  
  The carriage in words.
- `Note` = **Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.**  
  The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed (worklist C33).
- `WaybillTypeCode` = **NATROAD** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: NATROAD = Domestic road consignment note.
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `OtherInstruction` = **Pump into the propane storage at the boiler house; the water company's operator reads the storage level before and after and signs the note.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `Name` = **Kelpstone Gas plant, Gullhaven, LPG loading bay**  
  Where the carrier took over the goods and issued the note.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20413151** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Gullhaven Tank Haulage (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Gullhaven Tank Haulage**  
  The trading name; identity of Gullhaven Tank Haulage (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **NT-ADR-604219** (schemeID `urn:ubl-examples:world:XB:NT:address-register`)  
  The address's number in the address register of Northern Territory (NT-ADR- and six digits); identity of Gullhaven Tank Haulage (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Gullhaven Tank Haulage (world/parties.json).
- `PostalAddress/BuildingNumber` = **14**  
  Building number of the postal address. identity of Gullhaven Tank Haulage (world/parties.json).
- `PostalAddress/CityName` = **Gullhaven**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Gullhaven Tank Haulage (world/parties.json).
- `PostalAddress/PostalZone` = **90540**  
  Postal code in Bayvarra's format (5 digits). identity of Gullhaven Tank Haulage (world/parties.json).
- `PostalAddress/CountrySubentity` = **Northern Territory**  
  The name of code XB-NT in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-NT** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Gullhaven Tank Haulage (world/parties.json). The code is from Bayvarra's national state or territory list: XB-NT = Northern Territory.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Tanker planning**  
  The party's main desk, which handles this document; identity of Gullhaven Tank Haulage (world/parties.json).
- `Contact/JobTitle` = **Tanker planner**  
  The job of the person who answers at the desk; identity of Gullhaven Tank Haulage (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Gullhaven Tank Haulage (world/parties.json).
- `Contact/Telephone` = **+999 2 38522 41906**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Gullhaven Tank Haulage (world/parties.json).
- `Contact/ElectronicMail` = **planning@gullhaventank.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Gullhaven Tank Haulage (world/parties.json).
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Gullhaven Tank Haulage (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20413151** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Gullhaven Tank Haulage (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Kelpstone Gas (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:19676** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Kelpstone Gas (world/parties.json).
- `PartyName/Name` = **Kelpstone Gas**  
  The trading name; identity of Kelpstone Gas (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **NT-ADR-587853** (schemeID `urn:ubl-examples:world:XB:NT:address-register`)  
  The address's number in the address register of Northern Territory (NT-ADR- and six digits); identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Shoreline Road**  
  Street of the postal address. identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/BuildingNumber` = **2**  
  Building number of the postal address. identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/CityName` = **Gullhaven**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/PostalZone` = **90540**  
  Postal code in Bayvarra's format (5 digits). identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/CountrySubentity` = **Northern Territory**  
  The name of code XB-NT in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-NT** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Kelpstone Gas (world/parties.json). The code is from Bayvarra's national state or territory list: XB-NT = Northern Territory.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PhysicalLocation/Description` = **Gas treatment plant on the north coast; the platform of the offshore field lies about 80 kilometres out.**  
  Where the party actually operates, apart from its postal address. The distance is the length of the map's route gas-field, rounded to 10 km.
- `PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **28** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **15.95** (unitCode `D61`)  
  The minutes of the latitude.
- `PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **33.76** (unitCode `D61`)  
  The minutes of the longitude.
- `PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Contact/Name` = **Pipeline control**  
  The party's pipeline control desk: the desk for its role in this document (it carries or handles the goods); identity of Kelpstone Gas (world/parties.json).
- `Contact/JobTitle` = **Pipeline controller**  
  The job of the person who answers at the desk; identity of Kelpstone Gas (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Kelpstone Gas (world/parties.json).
- `Contact/Telephone` = **+999 2 38522 68330**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Kelpstone Gas (world/parties.json).
- `Contact/ElectronicMail` = **pipeline@kelpstone.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Kelpstone Gas (world/parties.json).
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Kelpstone Gas (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412877** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Kelpstone Gas (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Kelpstone Gas**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **20413151** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Gullhaven Tank Haulage**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **KG-SH-26-0897**  
  The shipment as the despatching party numbered it.
- `GrossWeightMeasure` = **29880** (unitCode `KGM`)  
  The goods (20180 kg) and the tare of the transport equipment (9700 kg): a shipment's gross weight includes the equipment (worklist C15).
- `Consignment/ID` = **KG-CS-26-0898**  
  The consignment of the transport booking.
- `Consignment/GrossWeightMeasure` = **20180** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The propane, net, from the plant's weighbridge.
- `Consignment/HazardousRiskIndicator` = **true**  
  The consignment is dangerous goods.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Coastal State Water Company**  
  The trading name; identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/ID` = **LUM-ADR-782593** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address. identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address. identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits). identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Coastal State Water Company (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Customer service**  
  The party's main desk, which handles this document; identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Customer service**  
  The department the desk belongs to; identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 2 38 9310 7518**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **customer@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Coastal State Water Company (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Coastal State Water Company (world/parties.json).
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The one road leg, from the plant to Lumeport.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/MainCarriageShipmentStage/HazardousRiskIndicator` = **true**  
  Dangerous goods on the road.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **3113** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tractor unit with an LPG tank semi-trailer; the fleet of Gullhaven Tank Haulage (world/parties.json). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 3113 = Lorry, articulated with tank.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **BV GT 2604** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The registration plate of the truck; the fleet of Gullhaven Tank Haulage (world/parties.json). The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/MainCarriageShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **BV TK 0419** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The tanker weighed full on the plant's weighbridge. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/Measure` = **37180** (unitCode `KGM`)  
  Within the Accord's 40,000 kg for a combination.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/Description` = **Loaded, at 06:45**  
  When it was weighed.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **TAREWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The same tanker weighed empty before loading. The code is from the Trade Accord's dimension attribute list: TAREWEIGHT = Tare weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/Measure` = **17000** (unitCode `KGM`)  
  The tractor about 7,300 kg and the tank semi-trailer about 9,700 kg (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/Description` = **Empty, at 05:40**  
  When it was weighed.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceDate` = **2026-06-10**  
  The tanker leaves the plant once loaded and weighed.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceTime` = **07:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Name` = **Kelpstone Gas plant, Gullhaven, LPG loading bay**  
  The plant's loading bay.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceDate` = **2026-06-10**  
  About 515 km at about 65 km/h, with the driver's break of 45 minutes.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceTime` = **15:40:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Name` = **Coastal State Water Company, district heating plant, Reservoir Road, Lumeport**  
  The boiler house's storage.
- `Consignment/MainCarriageShipmentStage/DriverPerson/FirstName` = **Rowan**  
  The driver, trained for dangerous goods in tanks.
- `Consignment/MainCarriageShipmentStage/DriverPerson/FamilyName` = **Tallis**  
  The family name.
- `Consignment/TransportHandlingUnit/ID` = **GT-TK-0419**  
  The propane travels in bulk, without packages: the tank is the unit it is handled in, by the tank's number.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **GT-TK-0419**  
  The haulier's number of its tank semi-trailer, painted on the tank.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **TE** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code TE: trailer, here the tank semi-trailer. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: TE = Trailer.
- `Consignment/TransportHandlingUnit/TransportEquipment/DangerousGoodsApprovedIndicator` = **true**  
  Approved for the propane it carries.
- `Consignment/TransportHandlingUnit/TransportEquipment/Description` = **A pressure tank for liquefied flammable gases, approved for UN 1965; its plate gives 49 m³ and a maximum load of 20,500 kg.**  
  The tank, as its approval plate gives it.
- `Consignment/TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **9700** (unitCode `KGM`)  
  The tank semi-trailer empty, from the haulier's fleet data (world/parties.json).
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ID` = **KG-LPG-DG**  
  Kelpstone's dangerous goods record of its propane.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PlacardNotation` = **2.1**  
  The class 2.1 placard on both sides and at the back of the tank.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UNDGCode` = **1965** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 1965 = Hydrocarbon gas mixture, liquefied, n.o.s..
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/TunnelRestrictionCode` = **B/D** (listID `UNECE ADR tunnel restriction code`)  
  The tunnel restriction code the transport document gives: in a tank, no passage through tunnels of categories B to E. The road from Gullhaven to Lumeport passes through no tunnel. The code is from the world's copy of ADR tunnel restriction code: B/D.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/TechnicalName` = **Mixture C**  
  The mixture the n.o.s. entry is described by (special provision 274): mixture C, of which the trade name is propane; in a tank, "propane" may be used only beside the mixture's name (ADR 2.2.2.3).
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ProperShippingName` = **Hydrocarbon gas mixture, liquefied, n.o.s.**  
  The proper shipping name of the UN entry, as the transport document must give it.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UpperOrangeHazardPlacardID` = **23**  
  The hazard identification number on the upper half of the orange plates at the front and back of the tanker: 2, gas, and 3, flammable.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/LowerOrangeHazardPlacardID` = **1965**  
  The UN number on the lower half of the orange plates.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardClassID` = **2.1** (schemeID `UN Model Regulations hazard class`)  
  Division 2.1, flammable gases. The code is from the world's copy of UN Model Regulations hazard class and division: 2.1 = Flammable gases. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetWeightMeasure` = **20180** (unitCode `KGM`)  
  The propane in the tank, from the weighbridge.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyName/Name` = **Kelpstone Gas**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Name` = **Plant control room**  
  Whom to call in an incident with the propane.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Telephone` = **+999 2 38522 68399**  
  The control room answers around the clock, while the tanker is on the road; under the reserved +999.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Note` = **Every day, around the clock**  
  When it answers.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC2** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The Trade Accord's emergency card for class 2, the instructions in writing the crew carries in the cab for this transit. The code is from the Trade Accord's transport emergency card list: TEC2 = Emergency card for class 2.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **ADR** (listID `UN/EDIFACT EDED 8273`)  
  Road: the ADR, which the Trade Accord's road rules apply to the carriage of dangerous goods, also within one country. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ADR = European agreement on the international carriage of dangerous goods on road (ADR).
- `Consignment/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  Greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Consignment/EnvironmentalEmission/ValueMeasure` = **456** (unitCode `KGM`)  
  1,700 kWh times 0.268 kg CO2e per kWh.
- `Consignment/EnvironmentalEmission/ValueFactorNumeric` = **0.268**  
  Tank to wheel, kg CO2e per kWh of diesel: about 2.67 kg per litre of about 10 kWh, the order of the default factor for diesel in EN 16258 (D41).
- `Consignment/EnvironmentalEmission/ValueBaseMeasure` = **1700** (unitCode `KWH`)  
  The diesel the run used, 170 litres of about 10 kWh, from the haulier's fuel records: about 33 litres per 100 km for the 515 km of the combination loaded.
- `Consignment/EnvironmentalEmission/Description` = **The loaded run, Gullhaven to Lumeport.**  
  What the figure covers.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  From the fuel used and an emission factor. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **5** (listID `UN/EDIFACT EDED 8169`)  
  UN/EDIFACT 8169 code 5: full. The tank goes loaded to Lumeport, filled to its maximum load. The code is from the world's copy of UN/EDIFACT 8169 Full or empty indicator: 5 = Full.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementFromLocation/Name` = **Kelpstone Gas plant, Gullhaven, LPG loading bay**  
  Where the run starts.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementToLocation/Name` = **Coastal State Water Company, district heating plant, Reservoir Road, Lumeport**  
  Where it ends.
- `Consignment/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  Greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Consignment/EnvironmentalEmission/ValueMeasure` = **332** (unitCode `KGM`)  
  1,240 kWh times 0.268 kg CO2e per kWh.
- `Consignment/EnvironmentalEmission/ValueFactorNumeric` = **0.268**  
  Tank to wheel, kg CO2e per kWh of diesel: about 2.67 kg per litre of about 10 kWh, the order of the default factor for diesel in EN 16258 (D41).
- `Consignment/EnvironmentalEmission/ValueBaseMeasure` = **1240** (unitCode `KWH`)  
  The diesel the run used, 124 litres of about 10 kWh, from the haulier's fuel records: about 24 litres per 100 km for the 515 km of the tanker empty.
- `Consignment/EnvironmentalEmission/Description` = **The tanker's empty run back to Gullhaven the next day, counted against this consignment: the Coastal State Water Company's greenhouse-gas report asks its suppliers' carriers for the whole round trip.**  
  What the figure covers.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  From the fuel used and an emission factor. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **4** (listID `UN/EDIFACT EDED 8169`)  
  UN/EDIFACT 8169 code 4: empty. A tanker of propane comes back empty: there is no load for it on the way north, so its empty run counts against the consignment. The code is from the world's copy of UN/EDIFACT 8169 Full or empty indicator: 4 = Empty.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementFromLocation/Name` = **Coastal State Water Company, district heating plant, Reservoir Road, Lumeport**  
  Where the run starts.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementToLocation/Name` = **Kelpstone Gas plant, Gullhaven, LPG loading bay**  
  Where it ends.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Propane, commercial**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **20180** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **20.18** (unitCode `TNE`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Propane, commercial**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **271112** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 271112 = Petroleum gases and other gaseous hydrocarbons; liquefied, propane.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **2**  
  The original for the consignee.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALWITHGOODS** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  One of the three originals travels with the goods to the consignee, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALWITHGOODS = Original, with the goods.
- `DistributionType` = **Original, with the goods: the consignee's original**  
  The name of code ORIGINALWITHGOODS in the Trade Accord's distribution type list, followed by the detail of this case: the original the consignee signs on delivery.
- `Party/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Coastal State Water Company**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **GTH-SIG-GTH-WB-26-0899**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **20413151** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Gullhaven Tank Haulage**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:waybill:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>LPG-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>GTH-WB-26-0899</cbc:ID>
  <cbc:CarrierAssignedID>GTH-NATROAD-26-0895</cbc:CarrierAssignedID>
  <cbc:UUID>1bcd7f24-a71e-5869-ae2d-2b2aab46d19b</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-06-10</cbc:IssueDate>
  <cbc:IssueTime>06:50:00-01:00</cbc:IssueTime>
  <cbc:Name>Consignment note under the national road carriage law</cbc:Name>
  <cbc:Description>The tanker carries the propane from the gas plant to the water company's peak boilers in Lumeport.</cbc:Description>
  <cbc:Note>Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.</cbc:Note>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">NATROAD</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:OtherInstruction>Pump into the propane storage at the boiler house; the water company's operator reads the storage level before and after and signs the note.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:Name>Kelpstone Gas plant, Gullhaven, LPG loading bay</cbc:Name>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413151</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Gullhaven Tank Haulage</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:NT:address-register">NT-ADR-604219</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>14</cbc:BuildingNumber>
      <cbc:CityName>Gullhaven</cbc:CityName>
      <cbc:PostalZone>90540</cbc:PostalZone>
      <cbc:CountrySubentity>Northern Territory</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-NT</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Tanker planning</cbc:Name>
      <cbc:JobTitle>Tanker planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 38522 41906</cbc:Telephone>
      <cbc:ElectronicMail>planning@gullhaventank.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20413151</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:19676</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelpstone Gas</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:NT:address-register">NT-ADR-587853</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Shoreline Road</cbc:StreetName>
      <cbc:BuildingNumber>2</cbc:BuildingNumber>
      <cbc:CityName>Gullhaven</cbc:CityName>
      <cbc:PostalZone>90540</cbc:PostalZone>
      <cbc:CountrySubentity>Northern Territory</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-NT</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PhysicalLocation>
      <cbc:Description>Gas treatment plant on the north coast; the platform of the offshore field lies about 80 kilometres out.</cbc:Description>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure unitCode="DD">28</cbc:LatitudeDegreesMeasure>
        <cbc:LatitudeMinutesMeasure unitCode="D61">15.95</cbc:LatitudeMinutesMeasure>
        <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
        <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
        <cbc:LongitudeMinutesMeasure unitCode="D61">33.76</cbc:LongitudeMinutesMeasure>
        <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
      </cac:LocationCoordinate>
    </cac:PhysicalLocation>
    <cac:Contact>
      <cbc:Name>Pipeline control</cbc:Name>
      <cbc:JobTitle>Pipeline controller</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 2 38522 68330</cbc:Telephone>
      <cbc:ElectronicMail>pipeline@kelpstone.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412877</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelpstone Gas</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413151</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Gullhaven Tank Haulage</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:Shipment>
    <cbc:ID>KG-SH-26-0897</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">29880</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>KG-CS-26-0898</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">20180</cbc:GrossWeightMeasure>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Coastal State Water Company</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-782593</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
          <cbc:StreetName>Reservoir Road</cbc:StreetName>
          <cbc:BuildingNumber>51</cbc:BuildingNumber>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38500</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Customer service</cbc:Name>
          <cbc:JobTitle>Customer service officer</cbc:JobTitle>
          <cbc:Department>Customer service</cbc:Department>
          <cbc:Telephone>+999 2 38 9310 7518</cbc:Telephone>
          <cbc:ElectronicMail>customer@coastalwater.example</cbc:ElectronicMail>
          <cbc:Note>Every day, around the clock</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportMeans>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">3113</cbc:TransportMeansTypeCode>
          <cac:RoadTransport>
            <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV GT 2604</cbc:LicensePlateID>
            <cbc:TrailerLicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV TK 0419</cbc:TrailerLicensePlateID>
          </cac:RoadTransport>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="KGM">37180</cbc:Measure>
            <cbc:Description>Loaded, at 06:45</cbc:Description>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">TAREWEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="KGM">17000</cbc:Measure>
            <cbc:Description>Empty, at 05:40</cbc:Description>
          </cac:MeasurementDimension>
        </cac:TransportMeans>
        <cac:PlannedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-06-10</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>07:00:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:Name>Kelpstone Gas plant, Gullhaven, LPG loading bay</cbc:Name>
          </cac:Location>
        </cac:PlannedDepartureTransportEvent>
        <cac:PlannedArrivalTransportEvent>
          <cbc:OccurrenceDate>2026-06-10</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>15:40:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:Name>Coastal State Water Company, district heating plant, Reservoir Road, Lumeport</cbc:Name>
          </cac:Location>
        </cac:PlannedArrivalTransportEvent>
        <cac:DriverPerson>
          <cbc:FirstName>Rowan</cbc:FirstName>
          <cbc:FamilyName>Tallis</cbc:FamilyName>
        </cac:DriverPerson>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cbc:ID>GT-TK-0419</cbc:ID>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportEquipment>
          <cbc:ID>GT-TK-0419</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">TE</cbc:TransportEquipmentTypeCode>
          <cbc:DangerousGoodsApprovedIndicator>true</cbc:DangerousGoodsApprovedIndicator>
          <cbc:Description>A pressure tank for liquefied flammable gases, approved for UN 1965; its plate gives 49 m³ and a maximum load of 20,500 kg.</cbc:Description>
          <cbc:TareWeightMeasure unitCode="KGM">9700</cbc:TareWeightMeasure>
          <cac:LoadedHazardousItem>
            <cbc:ID>KG-LPG-DG</cbc:ID>
            <cbc:PlacardNotation>2.1</cbc:PlacardNotation>
            <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">1965</cbc:UNDGCode>
            <cbc:TunnelRestrictionCode listID="UNECE ADR tunnel restriction code">B/D</cbc:TunnelRestrictionCode>
            <cbc:TechnicalName>Mixture C</cbc:TechnicalName>
            <cbc:ProperShippingName>Hydrocarbon gas mixture, liquefied, n.o.s.</cbc:ProperShippingName>
            <cbc:UpperOrangeHazardPlacardID>23</cbc:UpperOrangeHazardPlacardID>
            <cbc:LowerOrangeHazardPlacardID>1965</cbc:LowerOrangeHazardPlacardID>
            <cbc:HazardClassID schemeID="UN Model Regulations hazard class">2.1</cbc:HazardClassID>
            <cbc:NetWeightMeasure unitCode="KGM">20180</cbc:NetWeightMeasure>
            <cac:ContactParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Kelpstone Gas</cbc:Name>
              </cac:PartyName>
              <cac:Contact>
                <cbc:Name>Plant control room</cbc:Name>
                <cbc:Telephone>+999 2 38522 68399</cbc:Telephone>
                <cbc:Note>Every day, around the clock</cbc:Note>
              </cac:Contact>
            </cac:ContactParty>
            <cac:HazardousGoodsTransit>
              <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC2</cbc:TransportEmergencyCardCode>
              <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ADR</cbc:HazardousRegulationCode>
            </cac:HazardousGoodsTransit>
          </cac:LoadedHazardousItem>
        </cac:TransportEquipment>
      </cac:TransportHandlingUnit>
      <cac:EnvironmentalEmission>
        <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
        <cbc:ValueMeasure unitCode="KGM">456</cbc:ValueMeasure>
        <cbc:ValueFactorNumeric>0.268</cbc:ValueFactorNumeric>
        <cbc:ValueBaseMeasure unitCode="KWH">1700</cbc:ValueBaseMeasure>
        <cbc:Description>The loaded run, Gullhaven to Lumeport.</cbc:Description>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
          <cbc:FullnessIndicationCode listID="UN/EDIFACT EDED 8169">5</cbc:FullnessIndicationCode>
          <cac:MeasurementFromLocation>
            <cbc:Name>Kelpstone Gas plant, Gullhaven, LPG loading bay</cbc:Name>
          </cac:MeasurementFromLocation>
          <cac:MeasurementToLocation>
            <cbc:Name>Coastal State Water Company, district heating plant, Reservoir Road, Lumeport</cbc:Name>
          </cac:MeasurementToLocation>
        </cac:EmissionCalculationMethod>
      </cac:EnvironmentalEmission>
      <cac:EnvironmentalEmission>
        <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
        <cbc:ValueMeasure unitCode="KGM">332</cbc:ValueMeasure>
        <cbc:ValueFactorNumeric>0.268</cbc:ValueFactorNumeric>
        <cbc:ValueBaseMeasure unitCode="KWH">1240</cbc:ValueBaseMeasure>
        <cbc:Description>The tanker's empty run back to Gullhaven the next day, counted against this consignment: the Coastal State Water Company's greenhouse-gas report asks its suppliers' carriers for the whole round trip.</cbc:Description>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
          <cbc:FullnessIndicationCode listID="UN/EDIFACT EDED 8169">4</cbc:FullnessIndicationCode>
          <cac:MeasurementFromLocation>
            <cbc:Name>Coastal State Water Company, district heating plant, Reservoir Road, Lumeport</cbc:Name>
          </cac:MeasurementFromLocation>
          <cac:MeasurementToLocation>
            <cbc:Name>Kelpstone Gas plant, Gullhaven, LPG loading bay</cbc:Name>
          </cac:MeasurementToLocation>
        </cac:EmissionCalculationMethod>
      </cac:EnvironmentalEmission>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Propane, commercial</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">20180</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="TNE">20.18</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Propane, commercial</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">271112</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALWITHGOODS</cbc:DistributionTypeCode>
    <cbc:DistributionType>Original, with the goods: the consignee's original</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Coastal State Water Company</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>GTH-SIG-GTH-WB-26-0899</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413151</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Gullhaven Tank Haulage</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
