# Forwarding Instructions: Lumeport Textile Mill to Bayforth Forwarding

*Example 9 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Forwarding Instructions in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORWARDING-INSTRUCTIONS-SCHEMA)*

Under FOB the buyer books the main carriage: the mill instructs its forwarder.

[The XML file](09-ForwardingInstructions.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:forwarding-instructions:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Forwarding instructions"; the community specification "Lumeport port community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900013298**  
  The collaboration this document belongs to: the forwarding the textile mill gives Bayforth Forwarding. Lumeport Textile Mill started it and gave it this identifier, which every document of it repeats.
- `ID` = **2700007979**  
  The mill's instruction number.
- `UUID` = **1e4f0578-b6cd-5679-84ad-93eb9ac890fd**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-24**  
  The day after the order: under FOB the buyer instructs the forwarder for the main carriage.
- `IssueTime` = **11:39:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Name` = **Forwarding instructions**  
  What they are.
- `Description` = **Instructions for the bales to Bayvarra.**  
  In words.
- `Note` = **Please confirm the booking.**  
  What the sender expects.
- `ToOrderIndicator` = **false**  
  A straight bill: the consignee is named.
- `OtherInstruction` = **Send the bill of lading to the forwarder.**  
  Where the documents go.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Cotton Ginnery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-042681** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Selanu Cotton Ginnery gives it.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; as Selanu Cotton Ginnery gives it.
- `PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Cotton Ginnery gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Cotton Ginnery gives it.
- `PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Cotton Ginnery gives it.
- `PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. As Selanu Cotton Ginnery gives it.
- `PostalAddress/CityName` = **Pakesa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Cotton Ginnery gives it.
- `PostalAddress/CityName` = **Bollworth** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Cotton Ginnery gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Contact/Name` = **Despatch office**  
  The party's despatch office desk: the desk for its role in this document (it sends the goods off); as Selanu Cotton Ginnery gives it.
- `Contact/JobTitle` = **Despatch coordinator**  
  The job of the person who answers at the desk; as Selanu Cotton Ginnery gives it.
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Selanu Cotton Ginnery gives it.
- `Contact/Telephone` = **+999 3 721 0486**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Cotton Ginnery gives it.
- `Contact/ElectronicMail` = **despatch@selanuginnery.example**  
  The contact's e-mail address; as Selanu Cotton Ginnery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Selanu Cotton Ginnery gives it.

### Freight Forwarder Party

Inside `FreightForwarderParty`:

- `PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Bayforth Forwarding**  
  The trading name; as Bayforth Forwarding gives it.
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
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Bayforth Forwarding gives it.
- `Contact/ElectronicMail` = **export@bayforth.example**  
  The contact's e-mail address; as Bayforth Forwarding gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Bayforth Forwarding gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **SCG-SH-26-0218**  
  The shipment to be booked.
- `Consignment/ID` = **7300013298**  
  The consignment.
- `Consignment/GrossWeightMeasure` = **6190.29** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight of the bales.
- `Consignment/ForwarderServiceInstructions` = **Book a 40-foot container on the Tidewell Reef's sailing from Selanu of 7 May and have the empty container released to the ginnery for packing; clear the bales for import at Lumeport and truck the container to our goods-in.**  
  What the forwarder is to do: under free on board the buyer books the main carriage and takes the goods from the port of discharge.
- `Consignment/TotalPackagesQuantity` = **27** (unitCode `EA`)  
  The bales the forwarder is to book, in one container.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeport Textile Mill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **9524010900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-412603** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `Consignment/ConsigneeParty/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Consignment/ConsigneeParty/PostalAddress/ID` = **LUM-ADR-933254** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address. As Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address. As Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/PostalAddress/CitySubdivisionName` = **Mill Quarter**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits). As Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeport Textile Mill gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 2 38 2837 6029**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **goodsin@lumeporttextile.example**  
  The contact's e-mail address; as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeport Textile Mill gives it.
- `Consignment/ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XB:20412603** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeport Textile Mill gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  By sea from Selanu to Lumeport.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Maritime transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **TR-26-19W**  
  The voyage to book: the Tidewell Reef's from Selanu to Lumeport in week 19.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **WB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: WB = Westbound.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **1511** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tidewell Reef; the fleet of Tidewell Ocean Lines. The line's second feeder, bought second-hand in December 2025 and moved to Bayvarra's flag on 15 January 2026. Until the flag state verifies its security system, it sails with an interim International Ship Security Certificate (ISPS Code A/19.4). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 1511 = Full container ship/cellular vessel.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XB-S-20231** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Tidewell Reef**  
  The vessel's name; the fleet of Tidewell Ocean Lines.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **QBTR4**  
  The radio call sign, in Bayvarra's call sign series QB: no ITU series starts with Q, so the sign belongs to no real station.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **298702231**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 298 of Bayvarra, which the ITU has not allocated to any real country, and the ship's six digits.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **7480** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **3910** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 700 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20231**  
  The ship's certificate of registry.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Port of Selanu**  
  The port of loading, where free on board delivers.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **Port of Lumeport**  
  The port of discharge.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/RequestedDepartureTransportEvent/OccurrenceDate` = **2026-05-07**  
  The sailing the bales are wanted on: the order's free on board date, Thursday 7 May, in island time.
- `Consignment/MainCarriageShipmentStage/RequestedDepartureTransportEvent/OccurrenceTime` = **14:00:00+00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/RequestedDepartureTransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/RequestedDepartureTransportEvent/Location/Name` = **Port of Selanu**  
  The port of loading.
- `Consignment/MainCarriageShipmentStage/RequestedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Cotton lint, compressed bale**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **6190.29** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **6129** (unitCode `KGM`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Cotton lint, compressed bale**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **520100** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 520100 = Cotton, not carded or combed.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The goods travel in 27 of them, the consignment's package count. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: CN = Container.
- `TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **42G1** (listID `ISO 6346`)  
  The equipment to book: a 40-foot dry container, as an ISO 6346 size and type; the carrier assigns the container itself when it releases one. The code is from the world's copy of ISO 6346 container size and type code: 42G1 = 40 ft, 8 ft 6 in high, general purpose.

### Document Reference

Inside `DocumentReference`:

- `ID` = **4500013293**  
  The order the goods are for.
- `DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 4500013293 is the example cotton/08, a Order; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Order.

### Signature

Inside `Signature`:

- `ID` = **LTM-SIG-FI-09**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForwardingInstructions xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForwardingInstructions-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:forwarding-instructions:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900013298</cbc:ProfileExecutionID>
  <cbc:ID>2700007979</cbc:ID>
  <cbc:UUID>1e4f0578-b6cd-5679-84ad-93eb9ac890fd</cbc:UUID>
  <cbc:IssueDate>2026-04-24</cbc:IssueDate>
  <cbc:IssueTime>11:39:00-01:00</cbc:IssueTime>
  <cbc:Name>Forwarding instructions</cbc:Name>
  <cbc:Description>Instructions for the bales to Bayvarra.</cbc:Description>
  <cbc:Note>Please confirm the booking.</cbc:Note>
  <cbc:ToOrderIndicator>false</cbc:ToOrderIndicator>
  <cbc:OtherInstruction>Send the bill of lading to the forwarder.</cbc:OtherInstruction>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-042681</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">23618907</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Gin Yard Road</cbc:StreetName>
      <cbc:BuildingNumber>42</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Pakesa</cbc:CityName>
      <cbc:CityName languageID="en-XL">Bollworth</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Despatch office</cbc:Name>
      <cbc:JobTitle>Despatch coordinator</cbc:JobTitle>
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 3 721 0486</cbc:Telephone>
      <cbc:ElectronicMail>despatch@selanuginnery.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
  </cac:ConsignorParty>
  <cac:FreightForwarderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Bayforth Forwarding</cbc:Name>
    </cac:PartyName>
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
    <cbc:ID>SCG-SH-26-0218</cbc:ID>
    <cac:Consignment>
      <cbc:ID>7300013298</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">6190.29</cbc:GrossWeightMeasure>
      <cbc:ForwarderServiceInstructions>Book a 40-foot container on the Tidewell Reef's sailing from Selanu of 7 May and have the empty container released to the ginnery for packing; clear the bales for import at Lumeport and truck the container to our goods-in.</cbc:ForwarderServiceInstructions>
      <cbc:TotalPackagesQuantity unitCode="EA">27</cbc:TotalPackagesQuantity>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
        </cac:PartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="GS1 GLN">9524010900002</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412603</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Textile Mill</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID schemeID="ISO 639">en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-933254</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
          <cbc:StreetName>Mill Street</cbc:StreetName>
          <cbc:BuildingNumber>21</cbc:BuildingNumber>
          <cbc:CitySubdivisionName>Mill Quarter</cbc:CitySubdivisionName>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38504</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
          <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            <cbc:Name>Bayvarra</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Goods-in</cbc:Name>
          <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
          <cbc:Department>Warehouse</cbc:Department>
          <cbc:Telephone>+999 2 38 2837 6029</cbc:Telephone>
          <cbc:ElectronicMail>goodsin@lumeporttextile.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412603</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:ConsigneeParty>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>TR-26-19W</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">WB</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">1511</cbc:TransportMeansTypeCode>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20231</cbc:VesselID>
            <cbc:VesselName>Tidewell Reef</cbc:VesselName>
            <cbc:RadioCallSignID>QBTR4</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>298702231</cbc:MMSIRegistrationID>
            <cbc:GrossTonnageMeasure unitCode="C62">7480</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">3910</cbc:NetTonnageMeasure>
            <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
            <cac:RegistryCertificateDocumentReference>
              <cbc:ID>REG-XB-S-20231</cbc:ID>
            </cac:RegistryCertificateDocumentReference>
            <cac:RegistryPortLocation>
              <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
              <cbc:Name>Lumeport</cbc:Name>
            </cac:RegistryPortLocation>
          </cac:MaritimeTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:UnloadingPortLocation>
        <cac:RequestedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-05-07</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>14:00:00+00:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
            <cbc:Name>Port of Selanu</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:RequestedDepartureTransportEvent>
      </cac:MainCarriageShipmentStage>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Cotton lint, compressed bale</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">6190.29</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="KGM">6129</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Cotton lint, compressed bale</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">520100</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
      <cac:ContainingPackage>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
      </cac:ContainingPackage>
    </cac:GoodsItem>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
        <cbc:SizeTypeCode listID="ISO 6346">42G1</cbc:SizeTypeCode>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>4500013293</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>LTM-SIG-FI-09</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Textile Mill</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ForwardingInstructions>
```
