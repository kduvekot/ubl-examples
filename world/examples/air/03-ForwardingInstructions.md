# Forwarding Instructions: Lumeway Distribution to Bayforth Forwarding

*Example 3 of the flow "Urgent spare frames by air (Urvania → Bayvarra → island Lisavu)" · [Forwarding Instructions in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-FORWARDING-INSTRUCTIONS-SCHEMA)*

The distributor asks its forwarder to book the frames on the afternoon flight of 13 May.

[The XML file](03-ForwardingInstructions.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:forwarding-instructions:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Forwarding instructions". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **LMW-TX-26-1010**  
  The collaboration this document belongs to: the forwarding by air Lumeway gives Bayforth Forwarding. Lumeway Distribution started it and gave it this identifier, which every document of it repeats.
- `ID` = **LMW-FI-26-0606**  
  The instruction number.
- `UUID` = **8a0ceec7-aa03-5c38-8c5d-9f93d07709aa**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-12**  
  The distributor asks its forwarder to book air freight.
- `IssueTime` = **13:44:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Name` = **Forwarding instructions**  
  What they are.
- `Description` = **Instructions for the shipment to the island.**  
  In words.
- `Note` = **Please confirm the booking.**  
  What the sender expects.
- `ToOrderIndicator` = **false**  
  A straight bill: the consignee is named.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Lumeway Distribution gives it.
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Despatch office**  
  The party's despatch office desk: the desk for its role in this document (it sends the goods off); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Despatch coordinator**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **despatch@lumeway.example**  
  The contact's e-mail address; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

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
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Bayforth Forwarding gives it.
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

- `ID` = **LMW-SH-26-1010**  
  The shipment to be booked.
- `Consignment/ID` = **LMW-CS-26-1010**  
  The distributor's consignment number.
- `Consignment/GrossWeightMeasure` = **104.6** (unitCode `KGM`)  
  The eight frame cartons and the skid of 7.0 kg they are strapped to.
- `Consignment/NetNetWeightMeasure` = **88.8** (unitCode `KGM`)  
  The castings alone.
- `Consignment/NetVolumeMeasure` = **0.3** (unitCode `MTQ`)  
  The frames' own volume, without their cartons: the envelope of each frame.
- `Consignment/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods.
- `Consignment/DeclaredForCarriageValueAmount` = **512.00** (currencyID `XBL`)  
  Declared to the airline so its liability covers the value of the frames.
- `Consignment/SplitConsignmentIndicator` = **false**  
  All eight cartons on one flight.
- `Consignment/ConsignmentQuantity` = **1** (unitCode `EA`)  
  One consignment.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 3 729 5794**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **goodsin@velumi.example**  
  The contact's e-mail address; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.
- `Consignment/FreightForwarderParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/FreightForwarderParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportEvent/OccurrenceDate` = **2026-05-13**  
  Latest acceptance at the cargo terminal for the afternoon flight KXL209 of 13 May.
- `Consignment/TransportEvent/OccurrenceTime` = **12:00:00-01:00**  
  The local time.
- `Consignment/TransportEvent/TransportEventTypeCode` = **ACCEPTANCE** (listID `urn:ubl-examples:world:codelist:TransportEventTypeCode`)  
  The kind of event, as the carriers of the world code them. The code is from the Trade Accord's transport event type list: ACCEPTANCE = Accepted.
- `Consignment/TransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/TransportEvent/Location/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportEvent/Location/Name` = **Lumeport airport**  
  The cargo terminal at Lumeport airport.
- `Consignment/TransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/TransportHandlingUnit/ID` = **095206100003729347** (schemeID `GS1 SSCC`)  
  The skid the cartons are strapped to: the unit's SSCC, which Lumeway Distribution gives every logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check digit.
- `Consignment/TransportHandlingUnit/TransportHandlingUnitTypeCode` = **SI** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code SI: skid. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: SI = Skid.
- `Consignment/TransportHandlingUnit/ReferencedShipment/ID` = **LMW-SH-26-1010**  
  The distributor's shipment on the skid.
- `Consignment/TransportHandlingUnit/Package/ID` = **LMW-AIR-BOX**  
  The eight frame cartons as one package entry with their number: inner packages on the skid have a local identifier, without a scheme.
- `Consignment/TransportHandlingUnit/Package/Quantity` = **8** (unitCode `EA`)  
  Eight side frames, one to a carton.
- `Consignment/TransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/Package/GoodsItem/ID` = **1**  
  The side frames.
- `Consignment/TransportHandlingUnit/Package/GoodsItem/Description` = **Bench side frame castings**  
  In words.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of one carton. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  In millimetres.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of one carton. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  In millimetres.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Of one carton. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  In millimetres.
- `Consignment/TransportHandlingUnit/Package/DeliveryUnit/BatchQuantity` = **8** (unitCode `EA`)  
  All eight delivered together.
- `Consignment/TransportHandlingUnit/Package/Delivery/RequestedDeliveryPeriod/StartDate` = **2026-05-13**  
  At Selanu airport on the evening of 13 May, by KXL209.
- `Consignment/TransportHandlingUnit/Package/Delivery/RequestedDeliveryPeriod/EndDate` = **2026-05-14**  
  At the latest the next day, before the ship arrives.
- `Consignment/TransportHandlingUnit/Package/Pickup/ID` = **BYF-PU-26-0611**  
  The forwarder's pick-up order.
- `Consignment/TransportHandlingUnit/Package/Pickup/EarliestPickupDate` = **2026-05-13**  
  Valdara casts the frames on 12 May and packs them on 13 May; Trasvia brings them to the distributor's despatch area that morning.
- `Consignment/TransportHandlingUnit/Package/Pickup/PickupParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/Package/Pickup/PickupParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/Package/Despatch/RequestedDespatchDate` = **2026-05-13**  
  For the afternoon flight KXL209 of 13 May.
- `Consignment/TransportHandlingUnit/Package/Status/ConditionCode` = **SCHEDULED** (listID `urn:ubl-examples:world:codelist:StatusConditionCode`)  
  Not packed yet: the frames are cast today. The code is from the Trade Accord's status condition list: SCHEDULED = Scheduled.
- `Consignment/TransportHandlingUnit/Package/Status/Description` = **Cast at Valdara on 12 May, galvanised and packed on 13 May, then trucked to the despatch area under transit.**  
  Where they are and what follows.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Bench side frame casting**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **97.6** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels.
- `GoodsItem/Quantity` = **8** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Bench side frame casting**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940199** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940199 = Parts of seats, other.

### Document Reference

Inside `DocumentReference`:

- `ID` = **26-0065**  
  The order the goods are for.
- `DocumentTypeCode` = **OrderChange** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 26-0065 is the example air/01, a OrderChange; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: OrderChange = Order Change.

### Signature

Inside `Signature`:

- `ID` = **LD-SIG-FI-03**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ForwardingInstructions xmlns="urn:oasis:names:specification:ubl:schema:xsd:ForwardingInstructions-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:forwarding-instructions:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>LMW-TX-26-1010</cbc:ProfileExecutionID>
  <cbc:ID>LMW-FI-26-0606</cbc:ID>
  <cbc:UUID>8a0ceec7-aa03-5c38-8c5d-9f93d07709aa</cbc:UUID>
  <cbc:IssueDate>2026-05-12</cbc:IssueDate>
  <cbc:IssueTime>13:44:00-01:00</cbc:IssueTime>
  <cbc:Name>Forwarding instructions</cbc:Name>
  <cbc:Description>Instructions for the shipment to the island.</cbc:Description>
  <cbc:Note>Please confirm the booking.</cbc:Note>
  <cbc:ToOrderIndicator>false</cbc:ToOrderIndicator>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
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
      <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>despatch@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
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
    <cbc:ID>LMW-SH-26-1010</cbc:ID>
    <cac:Consignment>
      <cbc:ID>LMW-CS-26-1010</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">104.6</cbc:GrossWeightMeasure>
      <cbc:NetNetWeightMeasure unitCode="KGM">88.8</cbc:NetNetWeightMeasure>
      <cbc:NetVolumeMeasure unitCode="MTQ">0.3</cbc:NetVolumeMeasure>
      <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
      <cbc:DeclaredForCarriageValueAmount currencyID="XBL">512.00</cbc:DeclaredForCarriageValueAmount>
      <cbc:SplitConsignmentIndicator>false</cbc:SplitConsignmentIndicator>
      <cbc:ConsignmentQuantity unitCode="EA">1</cbc:ConsignmentQuantity>
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
      <cac:FreightForwarderParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Bayforth Forwarding</cbc:Name>
        </cac:PartyName>
      </cac:FreightForwarderParty>
      <cac:TransportEvent>
        <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>12:00:00-01:00</cbc:OccurrenceTime>
        <cbc:TransportEventTypeCode listID="urn:ubl-examples:world:codelist:TransportEventTypeCode">ACCEPTANCE</cbc:TransportEventTypeCode>
        <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XBLMA</cbc:ID>
          <cbc:Name>Lumeport airport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:TransportEvent>
      <cac:TransportHandlingUnit>
        <cbc:ID schemeID="GS1 SSCC">095206100003729347</cbc:ID>
        <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">SI</cbc:TransportHandlingUnitTypeCode>
        <cac:ReferencedShipment>
          <cbc:ID>LMW-SH-26-1010</cbc:ID>
        </cac:ReferencedShipment>
        <cac:Package>
          <cbc:ID>LMW-AIR-BOX</cbc:ID>
          <cbc:Quantity unitCode="EA">8</cbc:Quantity>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
          <cac:GoodsItem>
            <cbc:ID>1</cbc:ID>
            <cbc:Description>Bench side frame castings</cbc:Description>
          </cac:GoodsItem>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">790</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">680</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">100</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:DeliveryUnit>
            <cbc:BatchQuantity unitCode="EA">8</cbc:BatchQuantity>
          </cac:DeliveryUnit>
          <cac:Delivery>
            <cac:RequestedDeliveryPeriod>
              <cbc:StartDate>2026-05-13</cbc:StartDate>
              <cbc:EndDate>2026-05-14</cbc:EndDate>
            </cac:RequestedDeliveryPeriod>
          </cac:Delivery>
          <cac:Pickup>
            <cbc:ID>BYF-PU-26-0611</cbc:ID>
            <cbc:EarliestPickupDate>2026-05-13</cbc:EarliestPickupDate>
            <cac:PickupParty>
              <cac:PartyIdentification>
                <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
              </cac:PartyIdentification>
              <cac:PartyName>
                <cbc:Name>Bayforth Forwarding</cbc:Name>
              </cac:PartyName>
            </cac:PickupParty>
          </cac:Pickup>
          <cac:Despatch>
            <cbc:RequestedDespatchDate>2026-05-13</cbc:RequestedDespatchDate>
          </cac:Despatch>
          <cac:Status>
            <cbc:ConditionCode listID="urn:ubl-examples:world:codelist:StatusConditionCode">SCHEDULED</cbc:ConditionCode>
            <cbc:Description>Cast at Valdara on 12 May, galvanised and packed on 13 May, then trucked to the despatch area under transit.</cbc:Description>
          </cac:Status>
        </cac:Package>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Bench side frame casting</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">97.6</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">8</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Bench side frame casting</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940199</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>26-0065</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">OrderChange</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:Signature>
    <cbc:ID>LD-SIG-FI-03</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ForwardingInstructions>
```
