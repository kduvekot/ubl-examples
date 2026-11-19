# Waybill: Kelaro Air Cargo to Bayforth Forwarding

*Example 3 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The air waybill for cargo aircraft only, with the dangerous goods on it.

[The XML file](03-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **MAST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **KXL-WB-26-0717**  
  The consignment note number.
- `CarrierAssignedID` = **KXL-AWB-26-0713**  
  The carrier's own number for the carriage.
- `UUID` = **bf007d9d-013c-5ef5-8c7c-b450b24811d3**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-06-04**  
  The air waybill, cargo aircraft only.
- `IssueTime` = **17:15:00+00:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `Name` = **Air waybill under the Montreal Convention**  
  The kind of transport document.
- `Description` = **A cargo-aircraft-only flight to the island.**  
  The carriage in words.
- `Note` = **Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.**  
  The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed (worklist C33).
- `ShippingOrderID` = **SE-FI-26-0714**  
  The forwarding instructions the carriage is booked under.
- `WaybillTypeCode` = **AWB** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: AWB = Air waybill.
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Name` = **Lumeport airport, cargo terminal**  
  Where the carrier took over the goods and issued the note.
- `Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; identity of Kelaro Air Cargo (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English (O19). The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `PostalAddress/ID` = **58930746** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/StreetName` = **Airfield Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address. identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/CityName` = **Kefalasa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it (world/map.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/CityName` = **Lintwell** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelaro Air Cargo (world/parties.json).
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Cargo operations**  
  The party's cargo operations desk: the desk for its role in this document (it carries or handles the goods); identity of Kelaro Air Cargo (world/parties.json).
- `Contact/JobTitle` = **Load controller**  
  The job of the person who answers at the desk; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Telephone` = **+999 3 721 1044**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Kelaro Air Cargo (world/parties.json).
- `Contact/ElectronicMail` = **cargoops@kelaro.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Kelaro Air Cargo (world/parties.json).
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; identity of Kelaro Air Cargo (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41311** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-953846** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). identity of Bayforth Forwarding (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Export desk**  
  The party's main desk, which handles this document; identity of Bayforth Forwarding (world/parties.json).
- `Contact/JobTitle` = **Export coordinator**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Department` = **Export**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Telephone` = **+999 2 38 5155 2404**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-587295** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). identity of Saltmere Engineering (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Saltmere Engineering (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Saltmere Engineering (world/parties.json).
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Saltmere Engineering (world/parties.json).
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Saltmere Engineering (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 930 729**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Saltmere Engineering (world/parties.json).
- `Contact/ElectronicMail` = **dispatch@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Bayforth Forwarding**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **SE-SH-26-0715**  
  The shipment as the despatching party numbered it.
- `Consignment/ID` = **SE-CS-26-0716**  
  The consignment of the transport booking.
- `Consignment/GrossWeightMeasure` = **334.25** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight.
- `Consignment/HazardousRiskIndicator` = **true**  
  The consignment holds dangerous goods.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/ID` = **34928611** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Network stores**  
  The party's network stores desk: the desk for its role in this document (it receives the goods); identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Stores supervisor**  
  The job of the person who answers at the desk; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Network operations**  
  The department the desk belongs to; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 727 3193**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **stores@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Selanu Telecom (world/parties.json).
- `Consignment/HazardousItemNotificationParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/HazardousItemNotificationParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The flight.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Air transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 4 = Air transport.
- `Consignment/MainCarriageShipmentStage/HazardousRiskIndicator` = **true**  
  Dangerous goods on the flight.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **KXL209**  
  The cargo flight of the day.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XL** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Lisavu**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **ATF** (listID `IATA SSIM Aircraft Types`)  
  The kind of means of transport: ATR 72-600F freighter of Kelaro Air Cargo; the fleet of Kelaro Air Cargo (world/parties.json). An ATR 72-600F, the new-built freighter of the ATR 72-600 series (IATA aircraft type code ATF, ICAO type designator AT72): seven LD3 positions on the main deck (one of them for the active temperature-controlled RKN container), about 9,200 kg payload and 75 m³, a large cargo door of 2.94 × 1.80 m. A freighter, so it can carry the lithium batteries that are for cargo aircraft only. The code is from the world's copy of IATA SSIM aircraft type codes: ATF = ATR 72 Freighter.
- `Consignment/MainCarriageShipmentStage/TransportMeans/AirTransport/AircraftID` = **QL-KXA** (schemeID `urn:ubl-examples:world:XL:aircraft-register`)  
  The aircraft's registration: the nationality mark QL of Lisavu, a mark no real state uses, and three letters; the fleet of Kelaro Air Cargo (world/parties.json). The schemeID names the scheme it is from: the civil aircraft register of Lisavu (the nationality mark QL, a hyphen and three letters).
- `Consignment/TransportHandlingUnit/ID` = **RKN41207K0**  
  The container as a handling unit.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods inside.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **RKN41207K0**  
  The temperature-controlled air container, numbered as unit load devices are: its type RKN, its serial number 41207 and the designator of its owner, the airline Kelaro Air Cargo (world/parties.json).
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **AM** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code AM: refrigerated container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: AM = Refrigerated container.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigerationOnIndicator` = **true**  
  The unit is switched on.
- `Consignment/TransportHandlingUnit/TransportEquipment/AirFlowPercent` = **40**  
  The fan's air flow.
- `Consignment/TransportHandlingUnit/TransportEquipment/HumidityPercent` = **50**  
  Humidity kept below 50 %.
- `Consignment/TransportHandlingUnit/TransportEquipment/AnimalFoodApprovedIndicator` = **false**  
  Not for feed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HumanFoodApprovedIndicator` = **false**  
  Not for food.
- `Consignment/TransportHandlingUnit/TransportEquipment/DangerousGoodsApprovedIndicator` = **true**  
  Approved for dangerous goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigeratedIndicator` = **true**  
  A temperature-controlled unit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PowerIndicator` = **true**  
  Battery-powered cooling and heating.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.**  
  The conditions.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ID` = **SE-BAT-4850-DG**  
  The battery modules in the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UNDGCode` = **3480** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number of the battery modules. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 3480 = Lithium ion batteries (including lithium ion polymer batteries).
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/CategoryName` = **Miscellaneous dangerous goods**  
  Class 9 in words.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ProperShippingName` = **Lithium ion batteries**  
  As on the declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardClassID` = **9** (schemeID `UN Model Regulations hazard class`)  
  Class 9. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousTypeCode` = **ARTICLE** (listID `urn:ubl-examples:world:codelist:HazardousGoodsTypeCode`)  
  Batteries are articles, not substances. The code is from the Trade Accord's dangerous goods type list: ARTICLE = Article.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/GrossWeightMeasure` = **324** (unitCode `KGM`)  
  Twelve modules in their crates, 27 kg each: within the 35 kg a package of packing instruction 965 section IA may weigh on a cargo aircraft, so no approval is needed (D36).
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetWeightMeasure` = **288** (unitCode `KGM`)  
  The modules alone.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/NetVolumeMeasure` = **0.24** (unitCode `MTQ`)  
  Their volume: the same cells as the six larger packs first planned.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Quantity` = **12** (unitCode `EA`)  
  Twelve modules.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Name` = **Dangerous goods emergency line**  
  Whom to call in an incident with the batteries.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Telephone` = **+999 2 7121 930 486**  
  The line answers around the clock, while the goods are on the way; under the reserved +999.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Note` = **Every day, around the clock**  
  When it answers.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.**  
  The conditions.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/AdditionalTemperature/AttributeID` = **STORAGE** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Recommended storage. The code is from the Trade Accord's temperature attribute list: STORAGE = Storage temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/AdditionalTemperature/Measure` = **20** (unitCode `CEL`)  
  Around 20 °C.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PositionOnBoardStowage/LocationID` = **MD-2**  
  Main deck, LD3 position 2 from the front (world/parties.json, the aircraft's positions).
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PositionOnBoardStowage/Location` = **Main deck, accessible**  
  Where it flies: cargo aircraft only packages must be accessible to the crew.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module to a crate; the twelve crates are counted above and listed with their own numbers in the handling unit (mast/02#F1).
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportEmergencyCardCode` = **TEC9** (listID `urn:ubl-examples:world:codelist:TransportEmergencyCardCode`)  
  The emergency card on board. The code is from the Trade Accord's transport emergency card list: TEC9 = Emergency card for class 9.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/PackingCriteriaCode` = **PI965IA** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 965, section IA. The code is from the Trade Accord's air packing instruction list: PI965IA = Packing instruction 965, section IA.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/InhalationToxicityZoneCode` = **NOTTOXIC** (listID `urn:ubl-examples:world:codelist:InhalationToxicityZoneCode`)  
  Not toxic by inhalation. The code is from the Trade Accord's inhalation toxicity zone list: NOTTOXIC = Not toxic by inhalation.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransportAuthorizationCode` = **CAO** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Cargo aircraft only. The code is from the Trade Accord's transport authorization list: CAO = Cargo aircraft only.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/TransitDescription` = **Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.**  
  The conditions.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MinimumTemperature/Measure` = **5** (unitCode `CEL`)  
  The lowest allowed.
- `Consignment/TransportHandlingUnit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Lithium-ion packs must not freeze nor overheat. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MaximumTemperature/Measure` = **35** (unitCode `CEL`)  
  The highest allowed.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-1**  
  Crate 1 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0001**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-2**  
  Crate 2 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0002**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-3**  
  Crate 3 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0003**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-4**  
  Crate 4 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0004**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-5**  
  Crate 5 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0005**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-6**  
  Crate 6 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0006**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-7**  
  Crate 7 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0007**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-8**  
  Crate 8 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0008**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-9**  
  Crate 9 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0009**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-10**  
  Crate 10 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0010**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-11**  
  Crate 11 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0011**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-CR-12**  
  Crate 12 of twelve: the engineering company numbers each crate of dangerous goods it packs, so that each can be traced; its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One battery module in the crate.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CR** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CR: crate. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CR = Crate.
- `Consignment/TransportHandlingUnit/Package/TraceID` = **SE-DL-26-0012**  
  The serial number of the data logger fixed to the crate, which records its temperature and shocks on the way, for tracing a battery that is damaged.
- `Consignment/TransportHandlingUnit/ID` = **AKE20514K0**  
  The second air container, numbered as unit load devices are: its type AKE (an LD3 container), its serial number 20514 and the designator of its owner, the airline.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Dangerous goods inside.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **AKE20514K0**  
  The container.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **UL** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code UL: unit load device. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: UL = ULD (Unit load device).
- `Consignment/TransportHandlingUnit/TransportEquipment/DangerousGoodsApprovedIndicator` = **true**  
  Loaded with dangerous goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ID` = **SE-SMK-10-DG**  
  The ionisation smoke detector set in the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UNDGCode` = **2911** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2911 = Radioactive material, excepted package – instruments or articles.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  As on the declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  Class 7. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/GrossWeightMeasure` = **3** (unitCode `KGM`)  
  Packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Quantity` = **1** (unitCode `SET`)  
  As ordered.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Name` = **Dangerous goods emergency line**  
  Whom to call in an incident with these goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Telephone` = **+999 2 7121 930 486**  
  The line answers around the clock, while the goods are on the way; under the reserved +999.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Note` = **Every day, around the clock**  
  When it answers.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PositionOnBoardStowage/LocationID` = **MD-6**  
  Main deck, LD3 position 6. The smoke detectors are an excepted package of class 7, which needs no segregation from other classes (IATA DGR Table 9.3.A, note 1), so they share the container with the stripper.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ID` = **SE-CS-01-DG**  
  The coating stripper for electronics in the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/UNDGCode` = **2920** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2920 = Corrosive liquid, flammable, n.o.s..
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  As on the declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardClassID` = **8** (schemeID `UN Model Regulations hazard class`)  
  Class 8. The code is from the world's copy of UN Model Regulations hazard class and division: 8 = Corrosive substances. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PackagingDangerLevelCode` = **2** (listID `UN/EDIFACT EDED 8339`)  
  The packaging danger level of UN/EDIFACT 8339 that matches the packing group II. The code is from the world's copy of UN/EDIFACT 8339 Packaging danger level: 2 = Medium danger.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/GrossWeightMeasure` = **7.25** (unitCode `KGM`)  
  Packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/Quantity` = **5** (unitCode `LTR`)  
  As ordered.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/PartyName/Name` = **Saltmere Engineering**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Name` = **Dangerous goods emergency line**  
  Whom to call in an incident with these goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Telephone` = **+999 2 7121 930 486**  
  The line answers around the clock, while the goods are on the way; under the reserved +999.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/ContactParty/Contact/Note` = **Every day, around the clock**  
  When it answers.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/PackingCriteriaCode` = **PI851** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 851: one 1-litre tin to a box, within the quantity a passenger aircraft may carry (D36). The code is from the Trade Accord's air packing instruction list: PI851 = Packing instruction 851.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/HazardousGoodsTransit/TransportAuthorizationCode` = **PCA** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  Passenger and cargo aircraft: no crew access needed. The code is from the Trade Accord's transport authorization list: PCA = Passenger and cargo aircraft.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadedHazardousItem/PositionOnBoardStowage/LocationID` = **MD-6**  
  Main deck, LD3 position 6, four positions aft of the batteries: the stripper bears a class 3 label for its subsidiary hazard, and lithium-ion batteries of packing instruction 965 section IA must not be stowed next to, or where a fire could reach, packages with a class 3 label (IATA DGR 9.3.2.1.3).
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-BX-1**  
  The box of smoke detectors, the engineering company's own number.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One box: the set of ten.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-BX-2**  
  Box 1 of five of coating stripper.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One 1-litre tin in the box.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-BX-3**  
  Box 2 of five of coating stripper.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One 1-litre tin in the box.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-BX-4**  
  Box 3 of five of coating stripper.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One 1-litre tin in the box.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-BX-5**  
  Box 4 of five of coating stripper.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One 1-litre tin in the box.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/Package/ID` = **SE-BX-6**  
  Box 5 of five of coating stripper.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One 1-litre tin in the box.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Lithium-ion battery module 48 V 50 Ah**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **324** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **12** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Lithium-ion battery module 48 V 50 Ah**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **850760** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 850760 = Lithium-ion accumulators.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Ionisation smoke detector set**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **3** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **1** (unitCode `SET`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Ionisation smoke detector set**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **853110** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 853110 = Burglar or fire alarms and similar apparatus.
- `GoodsItem/ID` = **3**  
  The goods item number.
- `GoodsItem/Description` = **Coating stripper for electronics**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **7.25** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **5** (unitCode `LTR`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Coating stripper for electronics**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **381400** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 381400 = Organic composite solvents and thinners, n.e.s.; prepared paint or varnish removers.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The original for the consignor.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALHANDED** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The consignor's original, handed over when the carrier took over the goods, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALHANDED = Original, handed over.
- `Party/PartyIdentification/ID` = **20412055** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeport Airport Cargo Terminal**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The original for the consignee.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALWITHGOODS** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  One of the three originals travels with the goods to the consignee, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALWITHGOODS = Original, with the goods.
- `DistributionType` = **Original, with the goods: the consignee's original**  
  The name of code ORIGINALWITHGOODS in the Trade Accord's distribution type list, followed by the detail of this case: the original the consignee signs on delivery.
- `Party/PartyIdentification/ID` = **IC41174** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Selanu Airport Cargo**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **KXL-SIG-KXL-WB-26-0717**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Kelaro Air Cargo**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:waybill:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>KXL-WB-26-0717</cbc:ID>
  <cbc:CarrierAssignedID>KXL-AWB-26-0713</cbc:CarrierAssignedID>
  <cbc:UUID>bf007d9d-013c-5ef5-8c7c-b450b24811d3</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-06-04</cbc:IssueDate>
  <cbc:IssueTime>17:15:00+00:00</cbc:IssueTime>
  <cbc:Name>Air waybill under the Montreal Convention</cbc:Name>
  <cbc:Description>A cargo-aircraft-only flight to the island.</cbc:Description>
  <cbc:Note>Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.</cbc:Note>
  <cbc:ShippingOrderID>SE-FI-26-0714</cbc:ShippingOrderID>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">AWB</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:ID schemeID="UN/LOCODE">XBLMA</cbc:ID>
    <cbc:Name>Lumeport airport, cargo terminal</cbc:Name>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelaro Air Cargo</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">58930746</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Lupela Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Airfield Road</cbc:StreetName>
      <cbc:BuildingNumber>46</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Kefalasa</cbc:CityName>
      <cbc:CityName languageID="en-XL">Lintwell</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Cargo operations</cbc:Name>
      <cbc:JobTitle>Load controller</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 3 721 1044</cbc:Telephone>
      <cbc:ElectronicMail>cargoops@kelaro.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41311</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
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
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Saltmere Engineering</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-587295</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Foundry Road</cbc:StreetName>
      <cbc:BuildingNumber>13</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71218</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Dispatch office</cbc:Name>
      <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 2 7121 930 729</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@saltmere.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelaro Air Cargo</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>SE-SH-26-0715</cbc:ID>
    <cac:Consignment>
      <cbc:ID>SE-CS-26-0716</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">334.25</cbc:GrossWeightMeasure>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu Telecom</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">34928611</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Kitata Vekase Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Mast Hill Road</cbc:StreetName>
          <cbc:BuildingNumber>58</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Network stores</cbc:Name>
          <cbc:JobTitle>Stores supervisor</cbc:JobTitle>
          <cbc:Department>Network operations</cbc:Department>
          <cbc:Telephone>+999 3 727 3193</cbc:Telephone>
          <cbc:ElectronicMail>stores@selanutelecom.example</cbc:ElectronicMail>
          <cbc:Note>Every day, around the clock</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:HazardousItemNotificationParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Saltmere Engineering</cbc:Name>
        </cac:PartyName>
      </cac:HazardousItemNotificationParty>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportMeans>
          <cbc:JourneyID>KXL209</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XL</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Lisavu</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="IATA SSIM Aircraft Types">ATF</cbc:TransportMeansTypeCode>
          <cac:AirTransport>
            <cbc:AircraftID schemeID="urn:ubl-examples:world:XL:aircraft-register">QL-KXA</cbc:AircraftID>
          </cac:AirTransport>
        </cac:TransportMeans>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cbc:ID>RKN41207K0</cbc:ID>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportEquipment>
          <cbc:ID>RKN41207K0</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">AM</cbc:TransportEquipmentTypeCode>
          <cbc:RefrigerationOnIndicator>true</cbc:RefrigerationOnIndicator>
          <cbc:AirFlowPercent>40</cbc:AirFlowPercent>
          <cbc:HumidityPercent>50</cbc:HumidityPercent>
          <cbc:AnimalFoodApprovedIndicator>false</cbc:AnimalFoodApprovedIndicator>
          <cbc:HumanFoodApprovedIndicator>false</cbc:HumanFoodApprovedIndicator>
          <cbc:DangerousGoodsApprovedIndicator>true</cbc:DangerousGoodsApprovedIndicator>
          <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
          <cbc:PowerIndicator>true</cbc:PowerIndicator>
          <cac:MinimumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">5</cbc:Measure>
          </cac:MinimumTemperature>
          <cac:MaximumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">35</cbc:Measure>
          </cac:MaximumTemperature>
          <cac:HazardousGoodsTransit>
            <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
            <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
            <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
            <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
            <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
            <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.</cbc:TransitDescription>
            <cac:MaximumTemperature>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">35</cbc:Measure>
            </cac:MaximumTemperature>
            <cac:MinimumTemperature>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">5</cbc:Measure>
            </cac:MinimumTemperature>
          </cac:HazardousGoodsTransit>
          <cac:LoadedHazardousItem>
            <cbc:ID>SE-BAT-4850-DG</cbc:ID>
            <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">3480</cbc:UNDGCode>
            <cbc:CategoryName>Miscellaneous dangerous goods</cbc:CategoryName>
            <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
            <cbc:HazardClassID schemeID="UN Model Regulations hazard class">9</cbc:HazardClassID>
            <cbc:HazardousTypeCode listID="urn:ubl-examples:world:codelist:HazardousGoodsTypeCode">ARTICLE</cbc:HazardousTypeCode>
            <cbc:GrossWeightMeasure unitCode="KGM">324</cbc:GrossWeightMeasure>
            <cbc:NetWeightMeasure unitCode="KGM">288</cbc:NetWeightMeasure>
            <cbc:NetVolumeMeasure unitCode="MTQ">0.24</cbc:NetVolumeMeasure>
            <cbc:Quantity unitCode="EA">12</cbc:Quantity>
            <cac:ContactParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Saltmere Engineering</cbc:Name>
              </cac:PartyName>
              <cac:Contact>
                <cbc:Name>Dangerous goods emergency line</cbc:Name>
                <cbc:Telephone>+999 2 7121 930 486</cbc:Telephone>
                <cbc:Note>Every day, around the clock</cbc:Note>
              </cac:Contact>
            </cac:ContactParty>
            <cac:HazardousGoodsTransit>
              <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
              <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
              <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
              <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
              <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
              <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.</cbc:TransitDescription>
              <cac:MaximumTemperature>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
                <cbc:Measure unitCode="CEL">35</cbc:Measure>
              </cac:MaximumTemperature>
              <cac:MinimumTemperature>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
                <cbc:Measure unitCode="CEL">5</cbc:Measure>
              </cac:MinimumTemperature>
            </cac:HazardousGoodsTransit>
            <cac:AdditionalTemperature>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">STORAGE</cbc:AttributeID>
              <cbc:Measure unitCode="CEL">20</cbc:Measure>
            </cac:AdditionalTemperature>
            <cac:PositionOnBoardStowage>
              <cbc:LocationID>MD-2</cbc:LocationID>
              <cbc:Location>Main deck, accessible</cbc:Location>
            </cac:PositionOnBoardStowage>
            <cac:Package>
              <cbc:Quantity unitCode="EA">1</cbc:Quantity>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
            </cac:Package>
          </cac:LoadedHazardousItem>
        </cac:TransportEquipment>
        <cac:HazardousGoodsTransit>
          <cbc:TransportEmergencyCardCode listID="urn:ubl-examples:world:codelist:TransportEmergencyCardCode">TEC9</cbc:TransportEmergencyCardCode>
          <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI965IA</cbc:PackingCriteriaCode>
          <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
          <cbc:InhalationToxicityZoneCode listID="urn:ubl-examples:world:codelist:InhalationToxicityZoneCode">NOTTOXIC</cbc:InhalationToxicityZoneCode>
          <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">CAO</cbc:TransportAuthorizationCode>
          <cbc:TransitDescription>Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.</cbc:TransitDescription>
          <cac:MaximumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">35</cbc:Measure>
          </cac:MaximumTemperature>
          <cac:MinimumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">5</cbc:Measure>
          </cac:MinimumTemperature>
        </cac:HazardousGoodsTransit>
        <cac:MinimumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">5</cbc:Measure>
        </cac:MinimumTemperature>
        <cac:MaximumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">35</cbc:Measure>
        </cac:MaximumTemperature>
        <cac:Package>
          <cbc:ID>SE-CR-1</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0001</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-2</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0002</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-3</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0003</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-4</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0004</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-5</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0005</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-6</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0006</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-7</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0007</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-8</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0008</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-9</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0009</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-10</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0010</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-11</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0011</cbc:TraceID>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-CR-12</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CR</cbc:PackagingTypeCode>
          <cbc:TraceID>SE-DL-26-0012</cbc:TraceID>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>AKE20514K0</cbc:ID>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportEquipment>
          <cbc:ID>AKE20514K0</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">UL</cbc:TransportEquipmentTypeCode>
          <cbc:DangerousGoodsApprovedIndicator>true</cbc:DangerousGoodsApprovedIndicator>
          <cac:LoadedHazardousItem>
            <cbc:ID>SE-SMK-10-DG</cbc:ID>
            <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2911</cbc:UNDGCode>
            <cbc:ProperShippingName>Radioactive material, excepted package - instruments or articles</cbc:ProperShippingName>
            <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
            <cbc:GrossWeightMeasure unitCode="KGM">3</cbc:GrossWeightMeasure>
            <cbc:Quantity unitCode="SET">1</cbc:Quantity>
            <cac:ContactParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Saltmere Engineering</cbc:Name>
              </cac:PartyName>
              <cac:Contact>
                <cbc:Name>Dangerous goods emergency line</cbc:Name>
                <cbc:Telephone>+999 2 7121 930 486</cbc:Telephone>
                <cbc:Note>Every day, around the clock</cbc:Note>
              </cac:Contact>
            </cac:ContactParty>
            <cac:PositionOnBoardStowage>
              <cbc:LocationID>MD-6</cbc:LocationID>
            </cac:PositionOnBoardStowage>
          </cac:LoadedHazardousItem>
          <cac:LoadedHazardousItem>
            <cbc:ID>SE-CS-01-DG</cbc:ID>
            <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2920</cbc:UNDGCode>
            <cbc:ProperShippingName>Corrosive liquid, flammable, n.o.s.</cbc:ProperShippingName>
            <cbc:HazardClassID schemeID="UN Model Regulations hazard class">8</cbc:HazardClassID>
            <cbc:PackagingDangerLevelCode listID="UN/EDIFACT EDED 8339">2</cbc:PackagingDangerLevelCode>
            <cbc:GrossWeightMeasure unitCode="KGM">7.25</cbc:GrossWeightMeasure>
            <cbc:Quantity unitCode="LTR">5</cbc:Quantity>
            <cac:ContactParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Saltmere Engineering</cbc:Name>
              </cac:PartyName>
              <cac:Contact>
                <cbc:Name>Dangerous goods emergency line</cbc:Name>
                <cbc:Telephone>+999 2 7121 930 486</cbc:Telephone>
                <cbc:Note>Every day, around the clock</cbc:Note>
              </cac:Contact>
            </cac:ContactParty>
            <cac:HazardousGoodsTransit>
              <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI851</cbc:PackingCriteriaCode>
              <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
              <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">PCA</cbc:TransportAuthorizationCode>
            </cac:HazardousGoodsTransit>
            <cac:PositionOnBoardStowage>
              <cbc:LocationID>MD-6</cbc:LocationID>
            </cac:PositionOnBoardStowage>
          </cac:LoadedHazardousItem>
        </cac:TransportEquipment>
        <cac:Package>
          <cbc:ID>SE-BX-1</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-BX-2</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-BX-3</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-BX-4</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-BX-5</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>SE-BX-6</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Lithium-ion battery module 48 V 50 Ah</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">324</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Lithium-ion battery module 48 V 50 Ah</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">850760</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Ionisation smoke detector set</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">3</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="SET">1</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Ionisation smoke detector set</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">853110</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Description>Coating stripper for electronics</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">7.25</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="LTR">5</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Coating stripper for electronics</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">381400</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALHANDED</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412055</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALWITHGOODS</cbc:DistributionTypeCode>
    <cbc:DistributionType>Original, with the goods: the consignee's original</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41174</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Airport Cargo</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>KXL-SIG-KXL-WB-26-0717</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Kelaro Air Cargo</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
