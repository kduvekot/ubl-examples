# Bill of Lading: Tidewell Ocean Lines to Bayforth Forwarding

*Example 7 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Bill of Lading in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-BILL-OF-LADING-SCHEMA)*

The bill of lading of the reefer, issued to the forwarder that booked it, with the reefer's settings as the carrier is to keep them.

[The XML file](07-BillOfLading.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:bill-of-lading:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Bill of lading". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **REEFER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **TOL-BL-26-0562**  
  The bill of lading number.
- `CarrierAssignedID` = **TWL-BK-26-55194**  
  The booking the bill of lading is issued under.
- `UUID` = **6caa8b1e-206e-5ffe-a3bd-08fde43f6728**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-23**  
  Issued when the reefer is shipped on board.
- `IssueTime` = **14:30:00-01:00**  
  After the reefer was loaded on board and plugged in on the ship, in the afternoon before the evening sailing; in the issuer's local time, with its offset from UTC (D27).
- `ToOrderIndicator` = **false**  
  Made out to the named consignee, not to order: under open account the wholesaler takes delivery as consignee.
- `OtherInstruction` = **Express release: no original issued; the reefer is released at Selanu to the consignee named.**  
  Why there are no originals: the fruit is at Selanu in two days, before papers could follow it.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Harrowmead Fruit Growers (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9527430900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Harrowmead Fruit Growers (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-415873** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Harrowmead Fruit Growers (world/parties.json).
- `PartyName/Name` = **Harrowmead Fruit Growers**  
  The trading name; identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-418726** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Orchard Road**  
  Street of the postal address. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/BuildingNumber` = **3**  
  Building number of the postal address. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/CityName` = **Harrowmead**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/PostalZone` = **71640**  
  Postal code in Bayvarra's format (5 digits). identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Harrowmead Fruit Growers (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Department` = **Packhouse**  
  The department the desk belongs to; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Telephone` = **+999 2 7164 281 590**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/ElectronicMail` = **dispatch@harrowmeadfruit.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; identity of Harrowmead Fruit Growers (world/parties.json).

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Tidewell Ocean Lines (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Department` = **Bookings**  
  The department the desk belongs to; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2058 7929**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; identity of Tidewell Ocean Lines (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

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
  The party's export desk: the desk for its role in this document (it handles the transport of goods between the countries); identity of Bayforth Forwarding (world/parties.json).
- `Contact/JobTitle` = **Export coordinator**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Department` = **Export**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Telephone` = **+999 2 38 5155 2404**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
- `Contact/ElectronicMail` = **export@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **HFG-SH-26-0556**  
  The shipment carried.
- `GrossWeightMeasure` = **26528** (unitCode `KGM`)  
  The goods (21728 kg) and the tare of the transport equipment (4800 kg): a shipment's gross weight includes the equipment (worklist C15).
- `TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  The fruit, as one goods item.
- `TotalTransportHandlingUnitQuantity` = **20** (unitCode `EA`)  
  The pallets in the reefer.
- `ConsignmentQuantity` = **1** (unitCode `EA`)  
  One consignment.
- `Consignment/ID` = **HFG-CS-26-0557**  
  The cooperative's consignment.
- `Consignment/CarrierAssignedID` = **TWL-BK-26-55194**  
  The carrier's booking number.
- `Consignment/FreightForwarderAssignedID` = **BF-SH-26-0391**  
  The forwarder's own file number for the consignment.
- `Consignment/TariffDescription` = **Fresh fruit, chilled, in a reefer**  
  The carrier's commodity tariff, in words.
- `Consignment/TariffCode` = **TWL-T-0812**  
  The item of the carrier's own freight tariff for this cargo: fresh fruit, chilled. A code the carrier defines, so it has no code list.
- `Consignment/GrossWeightMeasure` = **21728** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight of the cargo.
- `Consignment/HandlingCode` = **POWER** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier stows the reefer at a power point and keeps it running. The code is from the Trade Accord's handling instruction list: POWER = Keep on power.
- `Consignment/HandlingInstructions` = **Keep plugged in; check the reefer every watch.**  
  The handling, in words.
- `Consignment/Information` = **Shipped on board in apparent good order and condition, refrigeration running at the set point.**  
  The carrier's clause.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Hafefo Fresh Produce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-043529** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Hafefo Fresh Produce**  
  The trading name; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/ID` = **40618392** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Cold store**  
  The party's cold store desk: the desk for its role in this document (it receives the goods); identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Cold store supervisor**  
  The job of the person who answers at the desk; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Cold store**  
  The department the desk belongs to; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 726 8104**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **coldstore@hafefo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Monday to Saturday 05:00–14:00**  
  When the desk can be reached; identity of Hafefo Fresh Produce (world/parties.json).
- `Consignment/OriginalDespatchParty/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OriginalDespatchParty/PartyName/Name` = **Harrowmead Fruit Growers**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/FinalDeliveryParty/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/FinalDeliveryParty/PartyName/Name` = **Hafefo Fresh Produce**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OriginalDepartureCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  From Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/FinalDestinationCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  To the island. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/DeliveryTerms/ID` = **CIP** (schemeID `INCOTERMS`)  
  Incoterms 2020: carriage and insurance paid to the port of Selanu. The code is from the world's copy of Incoterms 2020: CIP = Carriage and Insurance Paid To. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/DeliveryTerms/LossRisk` = **Risk passes when the reefer is handed to the carrier at Lumeport.**  
  In words.
- `Consignment/DeliveryTerms/DeliveryLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/DeliveryTerms/DeliveryLocation/Name` = **Port of Selanu**  
  The named place of destination.
- `Consignment/DeliveryTerms/DeliveryLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/CollectPaymentTerms/Note` = **Reefer power and monitoring at Selanu after discharge collect from the consignee.**  
  The buyer pays what follows the carriage.
- `Consignment/PrepaidPaymentTerms/Note` = **Ocean freight and bunker surcharge prepaid by the shipper.**  
  CIP: the seller pays.
- `Consignment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The basic ocean freight.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  UN/EDIFACT 7161 code FC: freight. The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReason` = **Ocean freight, 40-foot reefer**  
  In words.
- `Consignment/FreightAllowanceCharge/Amount` = **4400.00** (currencyID `XBL`)  
  The carrier's reefer rate: above the dry box's, for the power and the machinery.
- `Consignment/ExtraAllowanceCharge/ChargeIndicator` = **true**  
  A surcharge.
- `Consignment/ExtraAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The bunker surcharge is part of the freight: UN/EDIFACT 7161 has no code of its own for it, so it carries the freight code. The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/ExtraAllowanceCharge/AllowanceChargeReason` = **Bunker surcharge**  
  For the fuel price.
- `Consignment/ExtraAllowanceCharge/Amount` = **400.00** (currencyID `XBL`)  
  The surcharge of the carrier's tariff.
- `Consignment/MainCarriageShipmentStage/ID` = **2**  
  By sea from Lumeport to Selanu.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Maritime transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **TH-26-17E**  
  The voyage number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **EB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: EB = Eastbound.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **1511** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tidewell Harbour; the fleet of Tidewell Ocean Lines (world/parties.json). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 1511 = Full container ship/cellular vessel.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TradeServiceCode` = **TWL-ISL**  
  The carrier's code for its island service.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XB-S-20117** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Tidewell Harbour**  
  The vessel's name; the fleet of Tidewell Ocean Lines (world/parties.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **QBTH7**  
  The radio call sign, in Bayvarra's call sign series QB: no ITU series starts with Q, so the sign belongs to no real station (world/countries.json).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **298702117**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 298 of Bayvarra, which the ITU has not allocated to any real country, and the ship's six digits.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **9940** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **5120** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 1,000 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20117**  
  The ship's certificate of registry.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE; worklist C23).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Port of Lumeport**  
  The port of loading.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **Port of Selanu**  
  The port of discharge.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/OccurrenceDate` = **2026-04-22**  
  The terminal accepted the reefer.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/OccurrenceTime` = **17:40:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/Location/Name` = **Port of Lumeport**  
  At the container quay of the Port of Lumeport.
- `Consignment/MainCarriageShipmentStage/AcceptanceTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/PreCarriageShipmentStage/ID` = **1**  
  By reefer truck from Harrowmead to the port.
- `Consignment/PreCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/PreCarriageShipmentStage/PreCarriageIndicator` = **true**  
  Before the main carriage.
- `Consignment/PreCarriageShipmentStage/CarrierParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/CarrierParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/PreCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **37** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: container chassis truck with a clip-on generator set; the fleet of Bayforth Forwarding (world/parties.json). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 37 = Truck, container.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **BV LP 2208** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The registration plate of the truck; the fleet of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **BV CH 0436** (schemeID `urn:ubl-examples:world:XB:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the federal vehicle register of Bayvarra (BV, two letters for the series and four digits).
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/OccurrenceDate` = **2026-04-22**  
  The reefer was dropped at the container quay and plugged in, after 261 km from the packhouse on the truck's generator set.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/OccurrenceTime` = **17:40:00**  
  The local time.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/Location/Name` = **Port of Lumeport**  
  At the container quay of the Port of Lumeport.
- `Consignment/PreCarriageShipmentStage/DropoffTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/OnCarriageShipmentStage/ID` = **3**  
  By truck from the port of Selanu to the wholesaler's cold store.
- `Consignment/OnCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/OnCarriageShipmentStage/OnCarriageIndicator` = **true**  
  After the main carriage.
- `Consignment/OnCarriageShipmentStage/CarrierParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OnCarriageShipmentStage/CarrierParty/PartyName/Name` = **Nalevi Warehousing**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/OnCarriageShipmentStage/ReceiptTransportEvent/OccurrenceDate` = **2026-04-27**  
  Planned delivery at the cold store on the Monday morning, the day after discharge.
- `Consignment/OnCarriageShipmentStage/ReceiptTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/OnCarriageShipmentStage/ReceiptTransportEvent/Location/Name` = **Hafefo Fresh Produce, cold store, Selanu**  
  The wholesaler's cold store by the port.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **TWLU5316047** (schemeID `ISO6346`)  
  The container's number: the ocean carrier's owner code, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: CN = Container.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45R1** (listID `ISO 6346`)  
  ISO 6346 size and type: 40 feet, 9 ft 6 in high (high cube), a refrigerated container with its own refrigerating machinery. The code is from the world's copy of ISO 6346 container size and type code: 45R1 = 40 ft, 9 ft 6 in high, thermal, refrigerated and heated.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL** (listID `urn:ubl-examples:world:codelist:LoadTypeCode`)  
  A full container load. The code is from the Trade Accord's load type list: FCL = Full container load.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigerationOnIndicator` = **true**  
  The refrigeration runs, from the pre-cooling before loading to the unloading at the cold store: fresh fruit must not warm up.
- `Consignment/TransportHandlingUnit/TransportEquipment/AirFlowPercent` = **15**  
  The fresh-air vent's setting: open to 15 % of its full opening, about 25 m³ of outside air an hour on Tidewell's units. Apples and pears breathe; fresh air carries off the carbon dioxide and the ethylene that would ripen them.
- `Consignment/TransportHandlingUnit/TransportEquipment/HumidityPercent` = **90**  
  The relative humidity the reefer is set to hold: about 90 %, so that the fruit does not dry out and shrivel.
- `Consignment/TransportHandlingUnit/TransportEquipment/HumanFoodApprovedIndicator` = **true**  
  The reefer is approved for food: its interior is of food-grade materials and cleaned to carry food, which unpacked fruit in open trays needs.
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigeratedIndicator` = **true**  
  A refrigerated container.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **26528** (unitCode `KGM`)  
  The verified gross mass: the fruit on its pallets, 21728 kg, and the reefer's own 4,800 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **4800** (unitCode `KGM`)  
  The empty reefer's own weight, as marked on its door: heavier than a dry box by its machinery and insulation.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **TWL-S-0884517**  
  The carrier's seal, put on when the reefer was loaded.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **CARRIER** (listID `urn:ubl-examples:world:codelist:SealIssuerTypeCode`)  
  Issued by the ocean carrier. The code is from the Trade Accord's seal issuer type list: CARRIER = Carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  Put on by the shipper at the packhouse.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/Measure` = **0** (unitCode `CEL`)  
  The lowest air temperature the reefer may reach: colder, the fruit begins to freeze.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/Measure` = **1** (unitCode `CEL`)  
  The highest: warmer, it ripens on the way.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653010** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 001 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653010**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653027** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 002 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653027**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653034** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 003 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653034**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653041** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 004 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653041**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653058** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 005 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653058**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653065** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 006 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653065**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653072** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 007 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653072**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653089** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 008 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653089**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653096** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 009 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653096**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653102** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 010 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653102**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653119** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 011 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653119**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653126** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 012 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653126**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653133** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 013 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653133**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653140** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 014 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653140**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653157** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 015 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653157**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653164** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 016 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653164**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653171** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 017 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653171**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653188** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 018 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653188**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653195** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 019 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653195**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **095274300005653201** (schemeID `GS1 SSCC`)  
  The number on the pallet label: the unit's SSCC, which Harrowmead Fruit Growers gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **56** (unitCode `EA`)  
  56 cartons, eight a layer, seven layers.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **HAFEFO SELANU / 020 of 020**  
  The consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **095274300005653201**  
  The pallet's barcode, scanned at loading and at the cold store.
- `Consignment/TransportHandlingUnit/TransportEquipment/ServiceAllowanceCharge/ChargeIndicator` = **true**  
  A service to the reefer, charged.
- `Consignment/TransportHandlingUnit/TransportEquipment/ServiceAllowanceCharge/AllowanceChargeReasonCode` = **ABK** (listID `UN/EDIFACT EDED 7161`)  
  UN/EDIFACT 7161 code ABK: miscellaneous. The code is from the world's copy of UN/EDIFACT 7161 Special service description: ABK = Miscellaneous.
- `Consignment/TransportHandlingUnit/TransportEquipment/ServiceAllowanceCharge/AllowanceChargeReason` = **Reefer power and monitoring at Selanu after discharge, a day**  
  The carrier's tariff for the days the reefer stands on the port's power until the consignee collects it, collect from the consignee.
- `Consignment/TransportHandlingUnit/TransportEquipment/ServiceAllowanceCharge/Amount` = **45.00** (currencyID `XBL`)  
  A day's power and monitoring, at the carrier's tariff.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ID` = **VGM-26-0422**  
  The shipper's weight declaration.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDate` = **2026-04-22**  
  Weighed when packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingTime` = **11:30:00**  
  After the doors were closed.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingMethodCode` = **SM2** (listID `IMO SOLAS`)  
  SOLAS method 2: the cargo and packing weighed and added to the tare. The code is from UBL's default Weighing method (IMO SOLAS) list: SM2 = SOLAS verification method 2.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceID` = **HFC-SCALE-02**  
  The packhouse's pallet scale.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingDeviceType` = **Pallet scale**  
  Its kind.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/GrossMassMeasure` = **26528** (unitCode `KGM`)  
  The verified gross mass.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingParty/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/WeighingParty/PartyName/Name` = **Harrowmead Fruit Growers**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ShipperParty/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ShipperParty/PartyName/Name` = **Harrowmead Fruit Growers**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ResponsibleParty/PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/ResponsibleParty/PartyName/Name` = **Harrowmead Fruit Growers**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/DocumentReference/ID` = **VGM-26-0422**  
  The signed weight declaration sent to the carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/VerifiedGrossMass/DocumentReference/DocumentTypeCode` = **749** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, the cooperative's verified gross mass of the reefer, a document outside the examples (world/documents.json, cited; decision Q29). The code is from the world's copy of UN/EDIFACT 1001 Document name: 749 = Transport equipment gross mass verification message.
- `GoodsItem/ID` = **1**  
  The fruit in the reefer, as one item for the carrier.
- `GoodsItem/Description` = **Fresh apples and pears in cartons, on 20 pallets**  
  In words.
- `GoodsItem/GrossWeightMeasure` = **21728** (unitCode `KGM`)  
  The fruit in its cartons and the pallets.
- `GoodsItem/Temperature/AttributeID` = **SETPOINT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the temperature the reefer is set to keep in its cargo space. The code is from the Trade Accord's temperature attribute list: SETPOINT = Set point. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Temperature/Measure` = **0.5** (unitCode `CEL`)  
  The set point the reefer is to hold: 0.5 °C, the middle of the fruit's range, the figure the order's 'chilled' asks for.
- `GoodsItem/ContainedGoodsItem/ID` = **1.1**  
  The apples, Gala and Granny Smith.
- `GoodsItem/ContainedGoodsItem/Description` = **Fresh apples**  
  In words.
- `GoodsItem/ContainedGoodsItem/Item/Name` = **Fresh apples**  
  The goods.
- `GoodsItem/ContainedGoodsItem/Item/CommodityClassification/CommodityCode` = **080810** (listID `WCO HS 2022`)  
  The Harmonized System subheading of fresh apples, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080810 = Apples, fresh.
- `GoodsItem/ContainedGoodsItem/ID` = **1.2**  
  The pears.
- `GoodsItem/ContainedGoodsItem/Description` = **Fresh pears**  
  In words.
- `GoodsItem/ContainedGoodsItem/Item/Name` = **Fresh pears**  
  The goods.
- `GoodsItem/ContainedGoodsItem/Item/CommodityClassification/CommodityCode` = **080830** (listID `WCO HS 2022`)  
  The Harmonized System subheading of fresh pears. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080830 = Pears, fresh.
- `GoodsItem/MinimumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MinimumTemperature/Measure` = **0** (unitCode `CEL`)  
  The coldest the fruit may be carried at.
- `GoodsItem/MaximumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  What the temperature is of: the air in the reefer's cargo space. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MaximumTemperature/Measure` = **1** (unitCode `CEL`)  
  The warmest.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<BillOfLading xmlns="urn:oasis:names:specification:ubl:schema:xsd:BillOfLading-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:bill-of-lading:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>REEFER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TOL-BL-26-0562</cbc:ID>
  <cbc:CarrierAssignedID>TWL-BK-26-55194</cbc:CarrierAssignedID>
  <cbc:UUID>6caa8b1e-206e-5ffe-a3bd-08fde43f6728</cbc:UUID>
  <cbc:IssueDate>2026-04-23</cbc:IssueDate>
  <cbc:IssueTime>14:30:00-01:00</cbc:IssueTime>
  <cbc:ToOrderIndicator>false</cbc:ToOrderIndicator>
  <cbc:OtherInstruction>Express release: no original issued; the reefer is released at Selanu to the consignee named.</cbc:OtherInstruction>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9527430900003</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-415873</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-418726</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Orchard Road</cbc:StreetName>
      <cbc:BuildingNumber>3</cbc:BuildingNumber>
      <cbc:CityName>Harrowmead</cbc:CityName>
      <cbc:PostalZone>71640</cbc:PostalZone>
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
      <cbc:Department>Packhouse</cbc:Department>
      <cbc:Telephone>+999 2 7164 281 590</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@harrowmeadfruit.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
    </cac:Contact>
  </cac:ConsignorParty>
  <cac:CarrierParty>
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
  </cac:CarrierParty>
  <cac:FreightForwarderParty>
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
  </cac:FreightForwarderParty>
  <cac:Shipment>
    <cbc:ID>HFG-SH-26-0556</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">26528</cbc:GrossWeightMeasure>
    <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
    <cbc:TotalTransportHandlingUnitQuantity unitCode="EA">20</cbc:TotalTransportHandlingUnitQuantity>
    <cbc:ConsignmentQuantity unitCode="EA">1</cbc:ConsignmentQuantity>
    <cac:Consignment>
      <cbc:ID>HFG-CS-26-0557</cbc:ID>
      <cbc:CarrierAssignedID>TWL-BK-26-55194</cbc:CarrierAssignedID>
      <cbc:FreightForwarderAssignedID>BF-SH-26-0391</cbc:FreightForwarderAssignedID>
      <cbc:TariffDescription>Fresh fruit, chilled, in a reefer</cbc:TariffDescription>
      <cbc:TariffCode>TWL-T-0812</cbc:TariffCode>
      <cbc:GrossWeightMeasure unitCode="KGM">21728</cbc:GrossWeightMeasure>
      <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">POWER</cbc:HandlingCode>
      <cbc:HandlingInstructions>Keep plugged in; check the reefer every watch.</cbc:HandlingInstructions>
      <cbc:Information>Shipped on board in apparent good order and condition, refrigeration running at the set point.</cbc:Information>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
        </cac:PartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-043529</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Hafefo Fresh Produce</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40618392</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
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
          <cbc:Name>Cold store</cbc:Name>
          <cbc:JobTitle>Cold store supervisor</cbc:JobTitle>
          <cbc:Department>Cold store</cbc:Department>
          <cbc:Telephone>+999 3 726 8104</cbc:Telephone>
          <cbc:ElectronicMail>coldstore@hafefo.example</cbc:ElectronicMail>
          <cbc:Note>Monday to Saturday 05:00–14:00</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:OriginalDespatchParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
        </cac:PartyName>
      </cac:OriginalDespatchParty>
      <cac:FinalDeliveryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Hafefo Fresh Produce</cbc:Name>
        </cac:PartyName>
      </cac:FinalDeliveryParty>
      <cac:OriginalDepartureCountry>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:OriginalDepartureCountry>
      <cac:FinalDestinationCountry>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
      </cac:FinalDestinationCountry>
      <cac:DeliveryTerms>
        <cbc:ID schemeID="INCOTERMS">CIP</cbc:ID>
        <cbc:LossRisk>Risk passes when the reefer is handed to the carrier at Lumeport.</cbc:LossRisk>
        <cac:DeliveryLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:DeliveryLocation>
      </cac:DeliveryTerms>
      <cac:CollectPaymentTerms>
        <cbc:Note>Reefer power and monitoring at Selanu after discharge collect from the consignee.</cbc:Note>
      </cac:CollectPaymentTerms>
      <cac:PrepaidPaymentTerms>
        <cbc:Note>Ocean freight and bunker surcharge prepaid by the shipper.</cbc:Note>
      </cac:PrepaidPaymentTerms>
      <cac:FreightAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Ocean freight, 40-foot reefer</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">4400.00</cbc:Amount>
      </cac:FreightAllowanceCharge>
      <cac:ExtraAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Bunker surcharge</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">400.00</cbc:Amount>
      </cac:ExtraAllowanceCharge>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>2</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>TH-26-17E</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">EB</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">1511</cbc:TransportMeansTypeCode>
          <cbc:TradeServiceCode>TWL-ISL</cbc:TradeServiceCode>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20117</cbc:VesselID>
            <cbc:VesselName>Tidewell Harbour</cbc:VesselName>
            <cbc:RadioCallSignID>QBTH7</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>298702117</cbc:MMSIRegistrationID>
            <cbc:GrossTonnageMeasure unitCode="C62">9940</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">5120</cbc:NetTonnageMeasure>
            <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
            <cac:RegistryCertificateDocumentReference>
              <cbc:ID>REG-XB-S-20117</cbc:ID>
            </cac:RegistryCertificateDocumentReference>
            <cac:RegistryPortLocation>
              <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
              <cbc:Name>Lumeport</cbc:Name>
            </cac:RegistryPortLocation>
          </cac:MaritimeTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:UnloadingPortLocation>
        <cac:AcceptanceTransportEvent>
          <cbc:OccurrenceDate>2026-04-22</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>17:40:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:AcceptanceTransportEvent>
      </cac:MainCarriageShipmentStage>
      <cac:PreCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:PreCarriageIndicator>true</cbc:PreCarriageIndicator>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Bayforth Forwarding</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
        <cac:TransportMeans>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">37</cbc:TransportMeansTypeCode>
          <cac:RoadTransport>
            <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV LP 2208</cbc:LicensePlateID>
            <cbc:TrailerLicensePlateID schemeID="urn:ubl-examples:world:XB:vehicle-register">BV CH 0436</cbc:TrailerLicensePlateID>
          </cac:RoadTransport>
        </cac:TransportMeans>
        <cac:DropoffTransportEvent>
          <cbc:OccurrenceDate>2026-04-22</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>17:40:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:DropoffTransportEvent>
      </cac:PreCarriageShipmentStage>
      <cac:OnCarriageShipmentStage>
        <cbc:ID>3</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:OnCarriageIndicator>true</cbc:OnCarriageIndicator>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Nalevi Warehousing</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
        <cac:ReceiptTransportEvent>
          <cbc:OccurrenceDate>2026-04-27</cbc:OccurrenceDate>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:Location>
            <cbc:Name>Hafefo Fresh Produce, cold store, Selanu</cbc:Name>
          </cac:Location>
        </cac:ReceiptTransportEvent>
      </cac:OnCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">TWLU5316047</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:SizeTypeCode listID="ISO 6346">45R1</cbc:SizeTypeCode>
          <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:LoadTypeCode">FCL</cbc:FullnessIndicationCode>
          <cbc:RefrigerationOnIndicator>true</cbc:RefrigerationOnIndicator>
          <cbc:AirFlowPercent>15</cbc:AirFlowPercent>
          <cbc:HumidityPercent>90</cbc:HumidityPercent>
          <cbc:HumanFoodApprovedIndicator>true</cbc:HumanFoodApprovedIndicator>
          <cbc:RefrigeratedIndicator>true</cbc:RefrigeratedIndicator>
          <cbc:GrossWeightMeasure unitCode="KGM">26528</cbc:GrossWeightMeasure>
          <cbc:TareWeightMeasure unitCode="KGM">4800</cbc:TareWeightMeasure>
          <cac:TransportEquipmentSeal>
            <cbc:ID>TWL-S-0884517</cbc:ID>
            <cbc:SealIssuerTypeCode listID="urn:ubl-examples:world:codelist:SealIssuerTypeCode">CARRIER</cbc:SealIssuerTypeCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
          <cac:MinimumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">0</cbc:Measure>
          </cac:MinimumTemperature>
          <cac:MaximumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">1</cbc:Measure>
          </cac:MaximumTemperature>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653010</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 001 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653010</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653027</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 002 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653027</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653034</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 003 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653034</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653041</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 004 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653041</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653058</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 005 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653058</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653065</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 006 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653065</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653072</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 007 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653072</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653089</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 008 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653089</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653096</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 009 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653096</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653102</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 010 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653102</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653119</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 011 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653119</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653126</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 012 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653126</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653133</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 013 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653133</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653140</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 014 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653140</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653157</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 015 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653157</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653164</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 016 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653164</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653171</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 017 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653171</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653188</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 018 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653188</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653195</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 019 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653195</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="GS1 SSCC">095274300005653201</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:TotalPackageQuantity unitCode="EA">56</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>HAFEFO SELANU / 020 of 020</cbc:ShippingMarks>
            <cbc:TraceID>095274300005653201</cbc:TraceID>
          </cac:PackagedTransportHandlingUnit>
          <cac:ServiceAllowanceCharge>
            <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">ABK</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Reefer power and monitoring at Selanu after discharge, a day</cbc:AllowanceChargeReason>
            <cbc:Amount currencyID="XBL">45.00</cbc:Amount>
          </cac:ServiceAllowanceCharge>
          <cac:VerifiedGrossMass>
            <cbc:ID>VGM-26-0422</cbc:ID>
            <cbc:WeighingDate>2026-04-22</cbc:WeighingDate>
            <cbc:WeighingTime>11:30:00</cbc:WeighingTime>
            <cbc:WeighingMethodCode listID="IMO SOLAS">SM2</cbc:WeighingMethodCode>
            <cbc:WeighingDeviceID>HFC-SCALE-02</cbc:WeighingDeviceID>
            <cbc:WeighingDeviceType>Pallet scale</cbc:WeighingDeviceType>
            <cbc:GrossMassMeasure unitCode="KGM">26528</cbc:GrossMassMeasure>
            <cac:WeighingParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
              </cac:PartyName>
            </cac:WeighingParty>
            <cac:ShipperParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
              </cac:PartyName>
            </cac:ShipperParty>
            <cac:ResponsibleParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
              </cac:PartyName>
            </cac:ResponsibleParty>
            <cac:DocumentReference>
              <cbc:ID>VGM-26-0422</cbc:ID>
              <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">749</cbc:DocumentTypeCode>
            </cac:DocumentReference>
          </cac:VerifiedGrossMass>
        </cac:TransportEquipment>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Fresh apples and pears in cartons, on 20 pallets</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">21728</cbc:GrossWeightMeasure>
      <cac:Temperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">SETPOINT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">0.5</cbc:Measure>
      </cac:Temperature>
      <cac:ContainedGoodsItem>
        <cbc:ID>1.1</cbc:ID>
        <cbc:Description>Fresh apples</cbc:Description>
        <cac:Item>
          <cbc:Name>Fresh apples</cbc:Name>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="WCO HS 2022">080810</cbc:CommodityCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:ContainedGoodsItem>
      <cac:ContainedGoodsItem>
        <cbc:ID>1.2</cbc:ID>
        <cbc:Description>Fresh pears</cbc:Description>
        <cac:Item>
          <cbc:Name>Fresh pears</cbc:Name>
          <cac:CommodityClassification>
            <cbc:CommodityCode listID="WCO HS 2022">080830</cbc:CommodityCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:ContainedGoodsItem>
      <cac:MinimumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">0</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">1</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
  </cac:Shipment>
</BillOfLading>
```
