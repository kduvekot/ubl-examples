# Waybill: Kelaro Air Cargo to Bayforth Forwarding

*Example 4 of the flow "Urgent spare frames by air (Urvania → Bayvarra → island Lisavu)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The direct air waybill, issued when the airline accepted the cargo after the cut-off for the afternoon flight: it names the next morning's flight, and the 3PL as the party to notify.

[The XML file](04-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **AIR-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **KXL-WB-26-0325**  
  The consignment note number.
- `UUID` = **cbf5d04c-eecc-510a-b84b-bf76e2526b98**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-05-13**  
  The air waybill, issued when the airline accepted the cargo on the evening of 13 May, after the cut-off for KXL209.
- `IssueTime` = **20:15:00+00:00**  
  At acceptance, 19:15 in Lumeport; in the issuer's local time, with its offset from UTC.
- `Name` = **Air waybill under the Montreal Convention**  
  The kind of transport document.
- `Description` = **The flight to the island: booked on KXL209 of 13 May, flown on KXL207 of 14 May.**  
  The carriage in words.
- `Note` = **Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.**  
  The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed.
- `ShippingOrderID` = **LD-FI-26-0322**  
  The forwarding instructions the carriage is booked under.
- `WaybillTypeCode` = **AWB** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: AWB = Air waybill.
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `DeclaredCarriageValueAmount` = **512.00** (currencyID `XBL`)  
  The value declared for carriage.
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
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Kelaro Air Cargo gives it.
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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Bayforth Forwarding gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Bayforth Forwarding gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **dispatch@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.

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

- `ID` = **LD-SH-26-0323**  
  The shipment as the despatching party numbered it.
- `DeclaredForCarriageValueAmount` = **512.00** (currencyID `XBL`)  
  The value declared on the air waybill, as the distributor instructed.
- `Consignment/ID` = **LD-CS-26-0324**  
  The consignment of the transport booking.
- `Consignment/GrossWeightMeasure` = **104.6** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight of the cargo: the eight frame cartons and their skid.
- `Consignment/ChargeableWeightMeasure` = **105** (unitCode `KGM`)  
  The gross weight of 97.6 kg, rounded up to the next half kilogram: it is higher than the volume weight, 0.52 m³ at 167 kg per m³.
- `Consignment/GrossVolumeMeasure` = **0.52** (unitCode `MTQ`)  
  The stack of eight frame cartons of 790 x 680 x 100 mm on its skid of 800 x 700 mm.
- `Consignment/SpecialServiceInstructions` = **Priority handling at Selanu: the customer is waiting.**  
  The service asked for.
- `Consignment/ShippingPriorityLevelCode` = **PRIORITY** (listID `urn:ubl-examples:world:codelist:ShippingPriorityCode`)  
  Flown on the first flight with room. The code is from the Trade Accord's shipping priority list: PRIORITY = Priority.
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
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Velumi Trading gives it.
- `Consignment/ConsigneeParty/Contact/Note` = **Monday to Saturday 09:00–18:00**  
  When the desk can be reached; as Velumi Trading gives it.
- `Consignment/NotifyParty/PartyIdentification/ID` = **IC41722** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Nalevi Warehousing gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/NotifyParty/PartyName/Name` = **Nalevi Warehousing**  
  The trading name; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/ID` = **95940358** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/NotifyParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Vilafa Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/StreetName` = **Lagoon Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Nalevi Warehousing gives it.
- `Consignment/NotifyParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `Consignment/NotifyParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Consignment/NotifyParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Consignment/NotifyParty/Contact/Name` = **Goods inwards**  
  The party's main desk, which handles this document; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/JobTitle` = **Warehouse supervisor**  
  The job of the person who answers at the desk; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/Telephone` = **+999 3 722 1882**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/ElectronicMail` = **goods@nalevi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Nalevi Warehousing gives it.
- `Consignment/NotifyParty/Contact/Note` = **Monday to Saturday 07:00–18:00**  
  When the desk can be reached; as Nalevi Warehousing gives it.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The flight.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **4** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Air transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 4 = Air transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **KXL207**  
  The morning flight of 14 May, with the airline's ICAO-style designator KXL, which no real airline holds: the cargo missed the cut-off for KXL209 of 13 May.
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
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceDate` = **2026-05-14**  
  The flight's timetabled departure, in Lumeport's time, with its offset.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceTime` = **07:00:00-01:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/ID` = **XBLMA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Name` = **Lumeport airport**  
  The airport of departure.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceDate` = **2026-05-14**  
  The timetabled arrival, in island time, an hour ahead of Lumeport's: a block time of 2 h 45 eastbound.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceTime` = **10:45:00+00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/ID` = **XLSLA** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Name` = **Selanu airport**  
  The airport of destination.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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

- `ID` = **VI-TD-26-0513**  
  The transit declaration the frames travel under to Selanu airport, the office of destination; a document outside the examples.
- `DocumentType` = **Transit declaration**  
  The kind of document referred to, Valdara's transit declaration under the Trade Accord's common transit, from Ferrano to Selanu airport, a document outside the examples, in words: no list has an exact code for it (cited).

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

- `ID` = **KXL-SIG-KXL-WB-26-0325**  
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
  <cbc:ProfileExecutionID>AIR-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>KXL-WB-26-0325</cbc:ID>
  <cbc:UUID>cbf5d04c-eecc-510a-b84b-bf76e2526b98</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-05-13</cbc:IssueDate>
  <cbc:IssueTime>20:15:00+00:00</cbc:IssueTime>
  <cbc:Name>Air waybill under the Montreal Convention</cbc:Name>
  <cbc:Description>The flight to the island: booked on KXL209 of 13 May, flown on KXL207 of 14 May.</cbc:Description>
  <cbc:Note>Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.</cbc:Note>
  <cbc:ShippingOrderID>LD-FI-26-0322</cbc:ShippingOrderID>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">AWB</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:DeclaredCarriageValueAmount currencyID="XBL">512.00</cbc:DeclaredCarriageValueAmount>
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
      <cbc:Name>Dispatch office</cbc:Name>
      <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@lumeway.example</cbc:ElectronicMail>
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
    <cbc:ID>LD-SH-26-0323</cbc:ID>
    <cbc:DeclaredForCarriageValueAmount currencyID="XBL">512.00</cbc:DeclaredForCarriageValueAmount>
    <cac:Consignment>
      <cbc:ID>LD-CS-26-0324</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">104.6</cbc:GrossWeightMeasure>
      <cbc:ChargeableWeightMeasure unitCode="KGM">105</cbc:ChargeableWeightMeasure>
      <cbc:GrossVolumeMeasure unitCode="MTQ">0.52</cbc:GrossVolumeMeasure>
      <cbc:SpecialServiceInstructions>Priority handling at Selanu: the customer is waiting.</cbc:SpecialServiceInstructions>
      <cbc:ShippingPriorityLevelCode listID="urn:ubl-examples:world:codelist:ShippingPriorityCode">PRIORITY</cbc:ShippingPriorityLevelCode>
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
      <cac:NotifyParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41722</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Nalevi Warehousing</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">95940358</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
          <cbc:StreetName languageID="qal">Vilafa Natii</cbc:StreetName>
          <cbc:StreetName languageID="en-XL">Lagoon Road</cbc:StreetName>
          <cbc:BuildingNumber>9</cbc:BuildingNumber>
          <cbc:CityName languageID="qal">Selanu</cbc:CityName>
          <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
          <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            <cbc:Name>Lisavu</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Goods inwards</cbc:Name>
          <cbc:JobTitle>Warehouse supervisor</cbc:JobTitle>
          <cbc:Department>Warehouse</cbc:Department>
          <cbc:Telephone>+999 3 722 1882</cbc:Telephone>
          <cbc:ElectronicMail>goods@nalevi.example</cbc:ElectronicMail>
          <cbc:Note>Monday to Saturday 07:00–18:00</cbc:Note>
        </cac:Contact>
      </cac:NotifyParty>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">4</cbc:TransportModeCode>
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
          <cbc:OccurrenceDate>2026-05-14</cbc:OccurrenceDate>
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
          <cbc:OccurrenceDate>2026-05-14</cbc:OccurrenceDate>
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
    <cbc:ID>VI-TD-26-0513</cbc:ID>
    <cbc:DocumentType>Transit declaration</cbc:DocumentType>
  </cac:DocumentReference>
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
    <cbc:ID>KXL-SIG-KXL-WB-26-0325</cbc:ID>
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
