# Waybill: Kelaro Air Cargo to Bayforth Forwarding

*Example 11 of the flow "Medicines and a technetium generator for the island's hospital, by air (cold chain and radioactive material)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The air waybill for KXL207: the active container with its set temperature, the dry ice and the Type A package with its transport index.

[The XML file](11-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **BYF-TX-26-3169**  
  The collaboration this document belongs to: the air carriage Bayforth books with Kelaro Air Cargo. Bayforth Forwarding started it and gave it this identifier, which every document of it repeats.
- `ID` = **KXL-00698121**  
  The consignment note number.
- `UUID` = **ce469569-cb9b-58e9-a50d-3e0844604af3**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-06-15**  
  The air waybill, issued when the airline accepted the cargo for KXL207.
- `IssueTime` = **06:45:00+00:00**  
  At 05:45 in Lumeport, when the cargo had been accepted, before the 07:00 flight; in the issuer's local time, with its offset from UTC.
- `Name` = **Air waybill under the Montreal Convention**  
  The kind of transport document.
- `Description` = **The morning flight KXL207 of Monday 15 June on the airline's freighter.**  
  The carriage in words.
- `Note` = **Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.**  
  The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed.
- `ShippingOrderID` = **QLM-FI-26-2388**  
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
  The party's preferred identifier: its number in the Island companies register; as Kelaro Air Cargo gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; as Kelaro Air Cargo gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `PostalAddress/ID` = **58930746** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Kelaro Air Cargo gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Lupela Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Kelaro Air Cargo gives it.
- `PostalAddress/StreetName` = **Airfield Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Kelaro Air Cargo gives it.
- `PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address. As Kelaro Air Cargo gives it.
- `PostalAddress/CityName` = **Kefalasa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Kelaro Air Cargo gives it.
- `PostalAddress/CityName` = **Lintwell** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Kelaro Air Cargo gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Cargo operations**  
  The party's cargo operations desk: the desk for its role in this document (it carries or handles the goods); as Kelaro Air Cargo gives it.
- `Contact/JobTitle` = **Load controller**  
  The job of the person who answers at the desk; as Kelaro Air Cargo gives it.
- `Contact/Department` = **Operations**  
  The department the desk belongs to; as Kelaro Air Cargo gives it.
- `Contact/Telephone` = **+999 3 721 1044**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Kelaro Air Cargo gives it.
- `Contact/ElectronicMail` = **cargoops@kelaro.example**  
  The contact's e-mail address; as Kelaro Air Cargo gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Kelaro Air Cargo gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41311** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Kelaro Air Cargo gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Quillmoor Pharma Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9524910900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Quillmoor Pharma Distribution gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-413425** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Quillmoor Pharma Distribution gives it.
- `PartyName/Name` = **Quillmoor Pharma Distribution**  
  The trading name; as Quillmoor Pharma Distribution gives it.
- `PostalAddress/ID` = **LUM-ADR-718264** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Quillmoor Pharma Distribution gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Airport Road**  
  Street of the postal address. As Quillmoor Pharma Distribution gives it.
- `PostalAddress/BuildingNumber` = **40**  
  Building number of the postal address. As Quillmoor Pharma Distribution gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Quillmoor Pharma Distribution gives it.
- `PostalAddress/PostalZone` = **38528**  
  Postal code in Bayvarra's format (5 digits). As Quillmoor Pharma Distribution gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Quillmoor Pharma Distribution gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Despatch office**  
  The party's despatch office desk: the desk for its role in this document (it sends the goods off); as Quillmoor Pharma Distribution gives it.
- `Contact/JobTitle` = **Despatch coordinator**  
  The job of the person who answers at the desk; as Quillmoor Pharma Distribution gives it.
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Quillmoor Pharma Distribution gives it.
- `Contact/Telephone` = **+999 2 38 6047 1582**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Quillmoor Pharma Distribution gives it.
- `Contact/ElectronicMail` = **despatch@quillmoor.example**  
  The contact's e-mail address; as Quillmoor Pharma Distribution gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Quillmoor Pharma Distribution gives it.

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

- `ID` = **QLM-SH-26-3980**  
  The shipment as the despatching party numbered it.
- `Consignment/ID` = **QLM-CS-26-3980**  
  The consignment of the transport booking.
- `Consignment/GrossWeightMeasure` = **105.3** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The goods in their packs and shipping cartons, the dry ice and its box; the airline's container is not part of the shipment.
- `Consignment/HazardousRiskIndicator` = **true**  
  The consignment holds dangerous goods.
- `Consignment/SpecialServiceInstructions` = **Cold chain: deliver the active container to the island's cold room on arrival; radioactive package to the strong room.**  
  What the consignment needs on arrival.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **GOV-317** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Selanu General Hospital gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/PartyName/Name` = **Selanu General Hospital**  
  The trading name; as Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/PostalAddress/ID` = **52968014** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **81**  
  Building number of the postal address. As Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Pharmacy goods-in**  
  The party's pharmacy goods-in desk: the desk for its role in this document (it receives the goods); as Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Pharmacy technician**  
  The job of the person who answers at the desk; as Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/Contact/Department` = **Pharmacy**  
  The department the desk belongs to; as Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 726 8840**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **pharmacy-goodsin@selanu-hospital.example**  
  The contact's e-mail address; as Selanu General Hospital gives it.
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 07:30–17:00**  
  When the desk can be reached; as Selanu General Hospital gives it.
- `Consignment/NotifyParty/PartyIdentification/ID` = **IC41585** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Tevaro Customs Brokers gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/NotifyParty/PartyName/Name` = **Tevaro Customs Brokers**  
  The trading name; as Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/PostalAddress/ID` = **24307810** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/NotifyParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/PostalAddress/BuildingNumber` = **60**  
  Building number of the postal address. As Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Consignment/NotifyParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/NotifyParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/NotifyParty/Contact/Name` = **Declarations**  
  The party's main desk, which handles this document; as Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/Contact/JobTitle` = **Customs declarant**  
  The job of the person who answers at the desk; as Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/Contact/Department` = **Customs**  
  The department the desk belongs to; as Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/Contact/Telephone` = **+999 3 725 3563**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/Contact/ElectronicMail` = **declarations@tevaro.example**  
  The contact's e-mail address; as Tevaro Customs Brokers gives it.
- `Consignment/NotifyParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Tevaro Customs Brokers gives it.
- `Consignment/HazardousItemNotificationParty/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/HazardousItemNotificationParty/PartyName/Name` = **Quillmoor Pharma Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The flight.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Air transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 4 = Air transport.
- `Consignment/MainCarriageShipmentStage/HazardousRiskIndicator` = **true**  
  Dangerous goods on the flight: the generator and the dry ice.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **KXL207**  
  The morning flight of Monday 15 June, on the airline's freighter.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XL** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Lisavu**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **ATF** (listID `IATA SSIM Aircraft Types`)  
  The kind of means of transport: ATR 72-600F freighter of Kelaro Air Cargo; the fleet of Kelaro Air Cargo. An ATR 72-600F, the new-built freighter of the ATR 72-600 series (IATA aircraft type code ATF, ICAO type designator AT72): seven LD3 positions on the main deck (one of them for the active temperature-controlled RKN container), about 9,200 kg payload and 75 m³, a large cargo door of 2.94 × 1.80 m. A freighter, so it can carry the lithium batteries that are for cargo aircraft only. The code is from the world's copy of IATA SSIM aircraft type codes: ATF = ATR 72 Freighter.
- `Consignment/MainCarriageShipmentStage/TransportMeans/AirTransport/AircraftID` = **QL-KXA** (schemeID `urn:ubl-examples:world:XL:aircraft-register`)  
  The aircraft's registration: the nationality mark QL of Lisavu, a mark no real state uses, and three letters; the fleet of Kelaro Air Cargo. The schemeID names the scheme it is from: the civil aircraft register of Lisavu (the nationality mark QL, a hyphen and three letters).
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Lumeport airport**  
  The airport of departure.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/ID` = **XLSLA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **Selanu airport**  
  The airport of destination.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceDate` = **2026-06-15**  
  The flight's timetabled departure, in Lumeport's time, with its offset.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceTime` = **07:00:00-01:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Name` = **Lumeport airport**  
  The airport of departure.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceDate` = **2026-06-15**  
  The timetabled arrival, in island time, an hour ahead of Lumeport's: a block time of 2 h 45 eastbound.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceTime` = **10:45:00+00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/ID` = **XLSLA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Name` = **Selanu airport**  
  The airport of destination.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/TransportHandlingUnit/ID` = **RKN20871K0**  
  The airline's active temperature-controlled container, numbered as unit load devices are: its type RKN, its serial number and the airline's designator.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Keep at 2 to 8 °C; do not freeze; do not open before the island's cargo terminal.**  
  What the cold chain needs.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **RKN20871K0**  
  The container.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **UL** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code UL: unit load device. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: UL = ULD (Unit load device).
- `Consignment/TransportHandlingUnit/TransportEquipment/RefrigerationOnIndicator` = **true**  
  The container's cooling and heating are switched on: it keeps its set point by itself, on its batteries, from the wholesaler's cold room to the island.
- `Consignment/TransportHandlingUnit/TransportEquipment/Description` = **Active temperature-controlled LD3 container (RKN), set to 5 °C**  
  What kind of container: one that cools and heats, so it holds 2 to 8 °C whatever the hold's temperature.
- `Consignment/TransportHandlingUnit/TransportEquipment/TraceID` = **RKN-LOG-20871**  
  The container's data logger, which records the temperature every 15 minutes on the way.
- `Consignment/TransportHandlingUnit/TransportEquipment/StowagePositionID` = **MD-4**  
  Main deck, LD3 position 4 (the flow's air leg).
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The lowest temperature the container lets its cargo space fall to: its alarm limit. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MinimumTemperature/Measure` = **2** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/AttributeID` = **TRANSPORT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The highest: its other alarm limit. The code is from the Trade Accord's temperature attribute list: TRANSPORT = Transport temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MaximumTemperature/Measure` = **8** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The vaccines and the insulin must not fall below 2 °C: they lose their potency when they freeze. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MinimumTemperature/Measure` = **2** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  Nor rise above 8 °C. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MaximumTemperature/Measure` = **8** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-1**  
  Shipper carton 1: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-2**  
  Shipper carton 2: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-3**  
  Shipper carton 3: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-4**  
  Shipper carton 4: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-5**  
  Shipper carton 5: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-6**  
  Shipper carton 6: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-7**  
  Shipper carton 7: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-8**  
  Shipper carton 8: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-9**  
  Shipper carton 9: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-10**  
  Shipper carton 10: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **30** (unitCode `EA`)  
  Thirty packs of the influenza vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-11**  
  Shipper carton 11: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **60** (unitCode `EA`)  
  Sixty vials of insulin.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-12**  
  Shipper carton 12: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **60** (unitCode `EA`)  
  Sixty vials of insulin.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-13**  
  Shipper carton 13: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **60** (unitCode `EA`)  
  Sixty vials of insulin.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-CT-14**  
  Shipper carton 14: the wholesaler numbers its cartons for tracing, its own number, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **60** (unitCode `EA`)  
  Sixty vials of insulin.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/ID` = **QLM-BX-1**  
  The insulated box of the frozen vaccine, the wholesaler's own number.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Frozen vaccine on 6 kg of dry ice: keep the box upright and its vent clear; do not put it in the active container.**  
  How the box is handled: dry ice gives off carbon dioxide, and at -78 °C it would freeze the goods at 2 to 8 °C.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  The dry ice is dangerous goods of class 9.
- `Consignment/TransportHandlingUnit/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The live vaccine is kept frozen, at -50 °C or warmer. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MinimumTemperature/Measure` = **-50** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  And at -15 °C or colder. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/MaximumTemperature/Measure` = **-15** (unitCode `CEL`)  
  In degrees Celsius.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-BX-1**  
  The box itself.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **40** (unitCode `EA`)  
  Forty vials of the varicella vaccine.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/ID` = **QLM-RA-1**  
  The generator's Type A package, the wholesaler's own number.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box, the outer package. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/HandlingInstructions` = **Radioactive, Category III-YELLOW, transport index 1.5: stow in the aft hold, away from the crew and from the frozen vaccine's box.**  
  How the package is stowed: away from persons, by the distance its transport index asks.
- `Consignment/TransportHandlingUnit/HazardousRiskIndicator` = **true**  
  Radioactive material of class 7.
- `Consignment/TransportHandlingUnit/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `Consignment/TransportHandlingUnit/Package/ID` = **QLM-RA-1**  
  The package itself.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One generator.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **BX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BX: box. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BX = Box.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of the outer package. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **400** (unitCode `MMT`)  
  In millimetres.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **DEPTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of the outer package. The code is from the Trade Accord's dimension attribute list: DEPTH = Depth. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **300** (unitCode `MMT`)  
  In millimetres.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of the outer package. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **300** (unitCode `MMT`)  
  In millimetres.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **60** (unitCode `KGM`)  
  The goods of this item with their packaging.
- `GoodsItem/Quantity` = **300** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Influenza vaccine, inactivated, 10 prefilled syringes**  
  The goods, named.
- `GoodsItem/Temperature/AttributeID` = **SETPOINT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The set point: the temperature to carry the goods at, the middle of their range, which the active container is set to. The code is from the Trade Accord's temperature attribute list: SETPOINT = Set point. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Temperature/Measure` = **5** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: 2 to 8 °C, never frozen. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MinimumTemperature/Measure` = **2** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: 2 to 8 °C, never frozen. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MaximumTemperature/Measure` = **8** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **12** (unitCode `KGM`)  
  The goods of this item with their packaging.
- `GoodsItem/Quantity` = **240** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Insulin human, 100 IU/ml, vial of 10 ml**  
  The goods, named.
- `GoodsItem/Temperature/AttributeID` = **SETPOINT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The set point: the temperature to carry the goods at, the middle of their range, which the active container is set to. The code is from the Trade Accord's temperature attribute list: SETPOINT = Set point. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Temperature/Measure` = **5** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: 2 to 8 °C, never frozen. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MinimumTemperature/Measure` = **2** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: 2 to 8 °C, never frozen. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MaximumTemperature/Measure` = **8** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/ID` = **3**  
  The goods item number.
- `GoodsItem/Description` = **Varicella vaccine, live, frozen, single dose**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **1.6** (unitCode `KGM`)  
  The goods of this item with their packaging.
- `GoodsItem/Quantity` = **40** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Varicella vaccine, live, frozen, single dose**  
  The goods, named.
- `GoodsItem/MinimumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: frozen, -50 to -15 °C. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MinimumTemperature/Measure` = **-50** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/MaximumTemperature/AttributeID` = **PRODUCT** (schemeID `urn:ubl-examples:world:codelist:TemperatureAttributeCode`)  
  The range the maker's storage conditions give: frozen, -50 to -15 °C. The code is from the Trade Accord's temperature attribute list: PRODUCT = Product temperature. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/MaximumTemperature/Measure` = **-15** (unitCode `CEL`)  
  In degrees Celsius.
- `GoodsItem/ID` = **4**  
  The goods item number.
- `GoodsItem/Description` = **Technetium-99m generator, 20 GBq**  
  What is carried, in words.
- `GoodsItem/HazardousRiskIndicator` = **true**  
  Radioactive material.
- `GoodsItem/GrossWeightMeasure` = **18** (unitCode `KGM`)  
  The goods of this item with their packaging.
- `GoodsItem/Quantity` = **1** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Technetium-99m generator, 20 GBq**  
  The goods, named.
- `GoodsItem/Item/HazardousItem/ID` = **QLM-RAD-0020-DG**  
  The wholesaler's dangerous goods record of the generator.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the hazard label of the packages.
- `GoodsItem/Item/HazardousItem/AdditionalInformation` = **Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h**  
  What the shipper adds about handling.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **2915** (listID `UN Model Regulations Dangerous Goods List`)  
  The UN number, from the Dangerous Goods List of the UN Model Regulations. The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 2915 = Radioactive material, Type A package, non-special form, non fissile or fissile-excepted.
- `GoodsItem/Item/HazardousItem/UNPackingGroupCode` = **NA** (listID `urn:ubl-examples:world:codelist:UNPackingGroupCode`)  
  The packing group of the UN entry; NA where the entry has no packing group, as for gases, lithium batteries and radioactive material. The code is from the Trade Accord's packing group list: NA = No packing group assigned.
- `GoodsItem/Item/HazardousItem/UNPackingGroup` = **No packing group assigned**  
  The name of code NA in the Trade Accord's packing group list.
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **163** (listID `ERG 2024`)  
  The guide number of the Emergency Response Guidebook (ERG 2024) for this UN number: the world's carriers and receivers use the ERG, as the IMDG Code no longer gives medical first aid table numbers per UN number. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 163 = Radioactive Materials (Low to High Level Radiation).
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, Type A package, non-special form, non fissile or fissile-excepted**  
  The proper shipping name of the UN entry, as the Dangerous Goods List gives it for that UN number and class.
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **7** (listID `UN Model Regulations hazard class`)  
  The hazard class of the goods as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN2915**  
  The UN number marked on each package.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **7** (schemeID `UN Model Regulations hazard class`)  
  The UN hazard class of the entry. The code is from the world's copy of UN Model Regulations hazard class and division: 7 = Radioactive material. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/GrossWeightMeasure` = **18** (unitCode `KGM`)  
  The Type A package with the generator.
- `GoodsItem/Item/HazardousItem/Quantity` = **1** (unitCode `EA`)  
  One package.
- `GoodsItem/Item/HazardousItem/ContactParty/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/HazardousItem/ContactParty/PartyName/Name` = **Quillmoor Pharma Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/HazardousItem/ContactParty/Contact/Name` = **Dangerous goods emergency line**  
  Whom to call in an incident with the generator: the wholesaler's radiation protection officer.
- `GoodsItem/Item/HazardousItem/ContactParty/Contact/Telephone` = **+999 2 38 6047 1590**  
  The line answers around the clock while the goods are on the way; under the reserved +999.
- `GoodsItem/Item/HazardousItem/ContactParty/Contact/Note` = **Every day, around the clock**  
  When it answers.
- `GoodsItem/Item/HazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `GoodsItem/Item/HazardousItem/HazardousGoodsTransit/TransportAuthorizationCode` = **PCA** (listID `urn:ubl-examples:world:codelist:TransportAuthorizationCode`)  
  A Type A package with a transport index of 1.5 may fly on passenger aircraft too; it flies on the freighter because that is the island's cargo flight. The code is from the Trade Accord's transport authorization list: PCA = Passenger and cargo aircraft.
- `GoodsItem/Item/HazardousItem/PositionOnBoardStowage/LocationID` = **AFT-BULK**  
  The aft bulk hold, the furthest from the crew: a Yellow package is kept from persons by the distance its transport index asks.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/Name` = **Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)**  
  The radionuclide and the maximum activity during transport, which the transport document must state in becquerels (IAEA SSR-6 para 546): UBL has no element for the activity of contents that are not fissile, so the name carries it. The activity is the generator's at acceptance at the Lumeport cargo terminal, the highest it has on the way, as Mo-99 decays; the A2 value of Mo-99 allows up to 600 GBq in a Type A package.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.**  
  The physical and chemical form: not special form, so the A2 value applies.
- `GoodsItem/Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **1.5**  
  The transport index of the package: the highest dose rate at 1 m in mSv/h times 100, rounded up to the first decimal (IAEA SSR-6 para 523); above 1, so the package carries the Category III-YELLOW label (para 529, the higher category winning over the surface rate).
- `GoodsItem/ID` = **5**  
  The dry ice, a goods item of its own on the air waybill.
- `GoodsItem/Description` = **Dry ice, refrigerant of the frozen vaccine (goods item 3)**  
  What it is: the refrigerant in the box, not goods sold.
- `GoodsItem/HazardousRiskIndicator` = **true**  
  Dangerous goods of class 9.
- `GoodsItem/NetWeightMeasure` = **6** (unitCode `KGM`)  
  The dry ice in the box.
- `GoodsItem/Item/Name` = **Carbon dioxide, solid (dry ice)**  
  The refrigerant.
- `GoodsItem/Item/HazardousItem/ID` = **QLM-DRYICE-0615**  
  The wholesaler's entry for the dry ice in the box.
- `GoodsItem/Item/HazardousItem/PlacardNotation` = **9**  
  The class 9 label on the box.
- `GoodsItem/Item/HazardousItem/UNDGCode` = **1845** (listID `UN Model Regulations Dangerous Goods List`)  
  UN 1845, carbon dioxide, solid (dry ice). The code is from the world's copy of UN Model Regulations Dangerous Goods List (UN numbers): 1845 = Carbon dioxide, solid (dry ice).
- `GoodsItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **120** (listID `ERG 2024`)  
  The guide of the Emergency Response Guidebook (ERG 2024) for UN 1845: inert gases, including refrigerated liquids. The code is from the world's copy of Emergency Response Guidebook 2024, guide numbers: 120 = Gases - Inert (Including Refrigerated Liquids).
- `GoodsItem/Item/HazardousItem/ProperShippingName` = **Carbon dioxide, solid**  
  The proper shipping name; IATA also allows "Dry ice".
- `GoodsItem/Item/HazardousItem/HazardousCategoryCode` = **9** (listID `UN Model Regulations hazard class`)  
  The hazard class as a code of the UN Model Regulations' classes. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles.
- `GoodsItem/Item/HazardousItem/MarkingID` = **UN1845**  
  The UN number marked on the box, with the net weight of the dry ice.
- `GoodsItem/Item/HazardousItem/HazardClassID` = **9** (schemeID `UN Model Regulations hazard class`)  
  Class 9. The code is from the world's copy of UN Model Regulations hazard class and division: 9 = Miscellaneous dangerous substances and articles. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/HazardousItem/NetWeightMeasure` = **6** (unitCode `KGM`)  
  The dry ice in the box: what the air waybill must state, with the number of packages.
- `GoodsItem/Item/HazardousItem/Quantity` = **1** (unitCode `EA`)  
  One box.
- `GoodsItem/Item/HazardousItem/HazardousGoodsTransit/PackingCriteriaCode` = **PI954** (listID `urn:ubl-examples:world:codelist:PackingInstructionCode`)  
  IATA packing instruction 954: dry ice, in a package that lets the gas escape. The code is from the Trade Accord's air packing instruction list: PI954 = Packing instruction 954.
- `GoodsItem/Item/HazardousItem/HazardousGoodsTransit/HazardousRegulationCode` = **ICA** (listID `UN/EDIFACT EDED 8273`)  
  Air: the IATA Dangerous Goods Regulations. The code is from the world's copy of UN/EDIFACT 8273 Dangerous goods regulations: ICA = IATA ICAO.
- `GoodsItem/Item/HazardousItem/PositionOnBoardStowage/LocationID` = **AFT-BULK**  
  The aft bulk hold, at the other side from the generator.

### Document Reference

Inside `DocumentReference`:

- `ID` = **QLM-DGD-26-0615**  
  The shipper's declaration of the generator, which the airline keeps with the air waybill.
- `DocumentTypeCode` = **890** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to: the wholesaler's shipper's declaration for dangerous goods of the technetium generator, a declaration of its own. The code is from the world's copy of UN/EDIFACT 1001 Document name: 890 = Dangerous goods declaration.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The original for the consignor.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALHANDED** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The consignor's original, handed over when the carrier took over the goods, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALHANDED = Original, handed over.
- `Party/PartyIdentification/ID` = **20413425** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Quillmoor Pharma Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The original for the consignee.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALWITHGOODS** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  One of the three originals travels with the goods to the consignee, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALWITHGOODS = Original, with the goods.
- `DistributionType` = **Original, with the goods: the consignee's original**  
  The name of code ORIGINALWITHGOODS in the Trade Accord's distribution type list, followed by the detail of this case: the original the consignee signs on delivery.
- `Party/PartyIdentification/ID` = **GOV-317** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Selanu General Hospital**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **KXL-SIG-KXL-00698121**  
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
  <cbc:ProfileExecutionID>BYF-TX-26-3169</cbc:ProfileExecutionID>
  <cbc:ID>KXL-00698121</cbc:ID>
  <cbc:UUID>ce469569-cb9b-58e9-a50d-3e0844604af3</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-06-15</cbc:IssueDate>
  <cbc:IssueTime>06:45:00+00:00</cbc:IssueTime>
  <cbc:Name>Air waybill under the Montreal Convention</cbc:Name>
  <cbc:Description>The morning flight KXL207 of Monday 15 June on the airline's freighter.</cbc:Description>
  <cbc:Note>Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.</cbc:Note>
  <cbc:ShippingOrderID>QLM-FI-26-2388</cbc:ShippingOrderID>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9524910900003</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-413425</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-718264</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Airport Road</cbc:StreetName>
      <cbc:BuildingNumber>40</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38528</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Despatch office</cbc:Name>
      <cbc:JobTitle>Despatch coordinator</cbc:JobTitle>
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 2 38 6047 1582</cbc:Telephone>
      <cbc:ElectronicMail>despatch@quillmoor.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
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
    <cbc:ID>QLM-SH-26-3980</cbc:ID>
    <cac:Consignment>
      <cbc:ID>QLM-CS-26-3980</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">105.3</cbc:GrossWeightMeasure>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cbc:SpecialServiceInstructions>Cold chain: deliver the active container to the island's cold room on arrival; radioactive package to the strong room.</cbc:SpecialServiceInstructions>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-317</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Selanu General Hospital</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">52968014</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
          <cbc:BuildingNumber>81</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Pharmacy goods-in</cbc:Name>
          <cbc:JobTitle>Pharmacy technician</cbc:JobTitle>
          <cbc:Department>Pharmacy</cbc:Department>
          <cbc:Telephone>+999 3 726 8840</cbc:Telephone>
          <cbc:ElectronicMail>pharmacy-goodsin@selanu-hospital.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 07:30–17:00</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:NotifyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41585</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Tevaro Customs Brokers</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">24307810</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
          <cbc:BuildingNumber>60</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Declarations</cbc:Name>
          <cbc:JobTitle>Customs declarant</cbc:JobTitle>
          <cbc:Department>Customs</cbc:Department>
          <cbc:Telephone>+999 3 725 3563</cbc:Telephone>
          <cbc:ElectronicMail>declarations@tevaro.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
      </cac:NotifyParty>
      <cac:HazardousItemNotificationParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
        </cac:PartyName>
      </cac:HazardousItemNotificationParty>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:TransportMeans>
          <cbc:JourneyID>KXL207</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XL</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Lisavu</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="IATA SSIM Aircraft Types">ATF</cbc:TransportMeansTypeCode>
          <cac:AirTransport>
            <cbc:AircraftID schemeID="urn:ubl-examples:world:XL:aircraft-register">QL-KXA</cbc:AircraftID>
          </cac:AirTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMA</cbc:ID>
          <cbc:Name>Lumeport airport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSLA</cbc:ID>
          <cbc:Name>Selanu airport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:UnloadingPortLocation>
        <cac:PlannedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-06-15</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>07:00:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMA</cbc:ID>
            <cbc:Name>Lumeport airport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:PlannedDepartureTransportEvent>
        <cac:PlannedArrivalTransportEvent>
          <cbc:OccurrenceDate>2026-06-15</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:45:00+00:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XLSLA</cbc:ID>
            <cbc:Name>Selanu airport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:PlannedArrivalTransportEvent>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cbc:ID>RKN20871K0</cbc:ID>
        <cbc:HandlingInstructions>Keep at 2 to 8 °C; do not freeze; do not open before the island's cargo terminal.</cbc:HandlingInstructions>
        <cac:TransportEquipment>
          <cbc:ID>RKN20871K0</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">UL</cbc:TransportEquipmentTypeCode>
          <cbc:RefrigerationOnIndicator>true</cbc:RefrigerationOnIndicator>
          <cbc:Description>Active temperature-controlled LD3 container (RKN), set to 5 °C</cbc:Description>
          <cbc:TraceID>RKN-LOG-20871</cbc:TraceID>
          <cbc:StowagePositionID>MD-4</cbc:StowagePositionID>
          <cac:MinimumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">2</cbc:Measure>
          </cac:MinimumTemperature>
          <cac:MaximumTemperature>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">TRANSPORT</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">8</cbc:Measure>
          </cac:MaximumTemperature>
        </cac:TransportEquipment>
        <cac:MinimumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">2</cbc:Measure>
        </cac:MinimumTemperature>
        <cac:MaximumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">8</cbc:Measure>
        </cac:MaximumTemperature>
        <cac:Package>
          <cbc:ID>QLM-CT-1</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-2</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-3</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-4</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-5</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-6</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-7</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-8</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-9</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-10</cbc:ID>
          <cbc:Quantity unitCode="EA">30</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-11</cbc:ID>
          <cbc:Quantity unitCode="EA">60</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-12</cbc:ID>
          <cbc:Quantity unitCode="EA">60</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-13</cbc:ID>
          <cbc:Quantity unitCode="EA">60</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
        <cac:Package>
          <cbc:ID>QLM-CT-14</cbc:ID>
          <cbc:Quantity unitCode="EA">60</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>QLM-BX-1</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingInstructions>Frozen vaccine on 6 kg of dry ice: keep the box upright and its vent clear; do not put it in the active container.</cbc:HandlingInstructions>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:MinimumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">-50</cbc:Measure>
        </cac:MinimumTemperature>
        <cac:MaximumTemperature>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
          <cbc:Measure unitCode="CEL">-15</cbc:Measure>
        </cac:MaximumTemperature>
        <cac:Package>
          <cbc:ID>QLM-BX-1</cbc:ID>
          <cbc:Quantity unitCode="EA">40</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
        </cac:Package>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cbc:ID>QLM-RA-1</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:TransportHandlingUnitTypeCode>
        <cbc:HandlingInstructions>Radioactive, Category III-YELLOW, transport index 1.5: stow in the aft hold, away from the crew and from the frozen vaccine's box.</cbc:HandlingInstructions>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:HazardousGoodsTransit>
          <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
        </cac:HazardousGoodsTransit>
        <cac:Package>
          <cbc:ID>QLM-RA-1</cbc:ID>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BX</cbc:PackagingTypeCode>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">400</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">DEPTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">300</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">300</cbc:Measure>
          </cac:MeasurementDimension>
        </cac:Package>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">60</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">300</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Influenza vaccine, inactivated, 10 prefilled syringes</cbc:Name>
      </cac:Item>
      <cac:Temperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">SETPOINT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">5</cbc:Measure>
      </cac:Temperature>
      <cac:MinimumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">2</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">8</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">12</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">240</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Insulin human, 100 IU/ml, vial of 10 ml</cbc:Name>
      </cac:Item>
      <cac:Temperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">SETPOINT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">5</cbc:Measure>
      </cac:Temperature>
      <cac:MinimumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">2</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">8</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Description>Varicella vaccine, live, frozen, single dose</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">1.6</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">40</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Varicella vaccine, live, frozen, single dose</cbc:Name>
      </cac:Item>
      <cac:MinimumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">-50</cbc:Measure>
      </cac:MinimumTemperature>
      <cac:MaximumTemperature>
        <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:TemperatureAttributeCode">PRODUCT</cbc:AttributeID>
        <cbc:Measure unitCode="CEL">-15</cbc:Measure>
      </cac:MaximumTemperature>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>4</cbc:ID>
      <cbc:Description>Technetium-99m generator, 20 GBq</cbc:Description>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cbc:GrossWeightMeasure unitCode="KGM">18</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">1</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Technetium-99m generator, 20 GBq</cbc:Name>
        <cac:HazardousItem>
          <cbc:ID>QLM-RAD-0020-DG</cbc:ID>
          <cbc:PlacardNotation>7</cbc:PlacardNotation>
          <cbc:AdditionalInformation>Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">2915</cbc:UNDGCode>
          <cbc:UNPackingGroupCode listID="urn:ubl-examples:world:codelist:UNPackingGroupCode">NA</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>No packing group assigned</cbc:UNPackingGroup>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">163</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Radioactive material, Type A package, non-special form, non fissile or fissile-excepted</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">7</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2915</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">7</cbc:HazardClassID>
          <cbc:GrossWeightMeasure unitCode="KGM">18</cbc:GrossWeightMeasure>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cac:ContactParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
            </cac:PartyName>
            <cac:Contact>
              <cbc:Name>Dangerous goods emergency line</cbc:Name>
              <cbc:Telephone>+999 2 38 6047 1590</cbc:Telephone>
              <cbc:Note>Every day, around the clock</cbc:Note>
            </cac:Contact>
          </cac:ContactParty>
          <cac:HazardousGoodsTransit>
            <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
            <cbc:TransportAuthorizationCode listID="urn:ubl-examples:world:codelist:TransportAuthorizationCode">PCA</cbc:TransportAuthorizationCode>
          </cac:HazardousGoodsTransit>
          <cac:PositionOnBoardStowage>
            <cbc:LocationID>AFT-BULK</cbc:LocationID>
          </cac:PositionOnBoardStowage>
          <cac:RadioactiveMaterial>
            <cbc:Name>Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)</cbc:Name>
            <cbc:SpecialFormDescription>Non-special form: molybdate adsorbed on an alumina column, in its shielded housing.</cbc:SpecialFormDescription>
            <cbc:TransportIndexNumeric>1.5</cbc:TransportIndexNumeric>
          </cac:RadioactiveMaterial>
        </cac:HazardousItem>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>5</cbc:ID>
      <cbc:Description>Dry ice, refrigerant of the frozen vaccine (goods item 3)</cbc:Description>
      <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
      <cbc:NetWeightMeasure unitCode="KGM">6</cbc:NetWeightMeasure>
      <cac:Item>
        <cbc:Name>Carbon dioxide, solid (dry ice)</cbc:Name>
        <cac:HazardousItem>
          <cbc:ID>QLM-DRYICE-0615</cbc:ID>
          <cbc:PlacardNotation>9</cbc:PlacardNotation>
          <cbc:UNDGCode listID="UN Model Regulations Dangerous Goods List">1845</cbc:UNDGCode>
          <cbc:MedicalFirstAidGuideCode listID="ERG 2024">120</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Carbon dioxide, solid</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode listID="UN Model Regulations hazard class">9</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN1845</cbc:MarkingID>
          <cbc:HazardClassID schemeID="UN Model Regulations hazard class">9</cbc:HazardClassID>
          <cbc:NetWeightMeasure unitCode="KGM">6</cbc:NetWeightMeasure>
          <cbc:Quantity unitCode="EA">1</cbc:Quantity>
          <cac:HazardousGoodsTransit>
            <cbc:PackingCriteriaCode listID="urn:ubl-examples:world:codelist:PackingInstructionCode">PI954</cbc:PackingCriteriaCode>
            <cbc:HazardousRegulationCode listID="UN/EDIFACT EDED 8273">ICA</cbc:HazardousRegulationCode>
          </cac:HazardousGoodsTransit>
          <cac:PositionOnBoardStowage>
            <cbc:LocationID>AFT-BULK</cbc:LocationID>
          </cac:PositionOnBoardStowage>
        </cac:HazardousItem>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>QLM-DGD-26-0615</cbc:ID>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">890</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALHANDED</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20413425</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Quillmoor Pharma Distribution</cbc:Name>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-317</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu General Hospital</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>KXL-SIG-KXL-00698121</cbc:ID>
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
