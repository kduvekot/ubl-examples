# Waybill: Trasvia Haulage to Lumeway Distribution

*Example 8 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The road consignment note goes to the party that booked the truck, the distributor; it names the manufacturer as consignor.

[The XML file](08-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **TH-WB-26-0159**  
  The consignment note number.
- `CarrierAssignedID` = **TH-CMR-26-0149**  
  The carrier's own number for the carriage.
- `UUID` = **4891662e-273a-5190-9aa7-edb87e35d8b5**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-03-23**  
  Issued when the carrier collects the goods at the warehouse.
- `IssueTime` = **15:22:00-01:00**  
  Issued a few minutes after the last thing of its day that it reports, cites or answers, in the sender's local time, with its offset from UTC.
- `Name` = **Consignment note under the road convention, the CMR**  
  The kind of transport document.
- `Note` = **Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.**  
  The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed.
- `WaybillTypeCode` = **CMR** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: CMR = Road consignment note (CMR).
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Name` = **Castrano Logistics warehouse, Conciaro**  
  Where the carrier took over the goods and issued the note.
- `Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Trasvia Haulage gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Trasvia Haulage**  
  The trading name; as Trasvia Haulage gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XU** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Urvania, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XU = Urvanian English.
- `PostalAddress/ID` = **4160203746888095** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Trasvia Haulage gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Ban Kumek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Trasvia Haulage gives it.
- `PostalAddress/StreetName` = **Via dei Trasporti** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Trasvia Haulage gives it.
- `PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. As Trasvia Haulage gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Trasvia Haulage gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Trasvia Haulage gives it.
- `PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). As Trasvia Haulage gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Trasvia Haulage gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Planning desk**  
  The party's main desk, which handles this document; as Trasvia Haulage gives it.
- `Contact/JobTitle` = **Transport planner**  
  The job of the person who answers at the desk; as Trasvia Haulage gives it.
- `Contact/Department` = **Operations**  
  The department the desk belongs to; as Trasvia Haulage gives it.
- `Contact/Telephone` = **+999 1 041 266 7643**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Trasvia Haulage gives it.
- `Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Trasvia Haulage gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Trasvia Haulage gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104822** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Trasvia Haulage gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); as Lumeway Distribution gives it.
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Contact/ElectronicMail` = **logistics@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Lumeway Distribution gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Valdara Industries gives it.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Valdara Industries gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Valdara Industries gives it.
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Valdara Industries gives it.
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Valdara Industries gives it.
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). As Valdara Industries gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Valdara Industries gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Dispatch office**  
  The party's dispatch office desk: the desk for its role in this document (it sends the goods off); as Valdara Industries gives it.
- `Contact/JobTitle` = **Dispatch coordinator**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Contact/ElectronicMail` = **dispatch@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Valdara Industries gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Trasvia Haulage**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **CL-SH-26-0154**  
  The shipment as the despatching party numbered it.
- `HandlingCode` = **KEEPDRY** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: keep dry, for the goods travel in cardboard cartons. The code is from the Trade Accord's handling instruction list: KEEPDRY = Keep dry.
- `Information` = **Park benches, knocked down, and spare side frames, for resale.**  
  What the goods are, for the driver.
- `GrossWeightMeasure` = **12863.4** (unitCode `KGM`)  
  The goods (5363.4 kg) and the tare of the transport equipment (7500 kg): a shipment's gross weight includes the equipment.
- `NetNetWeightMeasure` = **4366.8** (unitCode `KGM`)  
  The goods alone, without any packaging.
- `GrossVolumeMeasure` = **24.1** (unitCode `MTQ`)  
  The volume of the 25 loaded pallets.
- `TotalGoodsItemQuantity` = **2** (unitCode `EA`)  
  Two kinds of goods, the goods items below: benches and side frames.
- `SplitConsignmentIndicator` = **false**  
  The whole consignment travels on this truck.
- `ConsignmentQuantity` = **1** (unitCode `EA`)  
  One consignment on the truck.
- `Consignment/ID` = **LD-CS-26-0152**  
  The distributor's consignment number, from its booking.
- `Consignment/CarrierAssignedID` = **TH-26-04471**  
  The carrier's job number.
- `Consignment/ConsigneeAssignedID` = **LD-GI-0412**  
  The distributor's goods-in booking for the slot.
- `Consignment/SummaryDescription` = **Park benches and spare side frames on 25 pallets.**  
  The goods in a few words, as on the consignment note.
- `Consignment/GrossWeightMeasure` = **5363.4** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight the carrier takes over.
- `Consignment/NetWeightMeasure` = **4366.8** (unitCode `KGM`)  
  The weight of the goods without packaging.
- `Consignment/LoadingLengthMeasure` = **9.3** (unitCode `MTR`)  
  The 24 bench pallets two high, three abreast, in four rows of 1.85 m, and the pallet of frame cartons in a fifth row: that much of the 13.6 m floor.
- `Consignment/Remarks` = **Received in apparent good order; trailer doors sealed by the 3PL, seal as recorded.**  
  The driver's remarks at taking over, as the consignment note asks; the seal's number is in the trailer's own seal element.
- `Consignment/ContainerizedIndicator` = **false**  
  The pallets are loaded on the truck, not in a container.
- `Consignment/GeneralCargoIndicator` = **true**  
  Packed goods on pallets.
- `Consignment/ThirdPartyPayerIndicator` = **false**  
  The consignee, who booked the truck, pays the freight.
- `Consignment/CustomsClearanceServiceInstructions` = **The export is declared by the seller in Ferrano; the import by the distributor at the border.**  
  Who clears the goods through customs.
- `Consignment/TotalTransportHandlingUnitQuantity` = **25** (unitCode `EA`)  
  The pallets they travel on: 24 of benches and one of frame cartons.
- `Consignment/DeliveryInstructions` = **Enter by gate 3 of the business park and report to the gatehouse; unload at dock 4.**  
  Where to go on arrival.
- `Consignment/HaulageInstructions` = **Wait at the warehouse until customs has released the export declaration.**  
  What the driver must do before leaving.
- `Consignment/TotalPackagesQuantity` = **300** (unitCode `EA`)  
  The parcels: 96 benches in three parcels each and 12 frame cartons.
- `Consignment/CustomsDeclaration/ID` = **VI-CD-26-0156**  
  The export declaration the goods travel under.
- `Consignment/CustomsDeclaration/IssuerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/CustomsDeclaration/IssuerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/ActualPickupTransportEvent/OccurrenceDate` = **2026-03-23**  
  When the carrier took over the goods.
- `Consignment/ActualPickupTransportEvent/OccurrenceTime` = **15:05:00**  
  The local time.
- `Consignment/ActualPickupTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/ActualPickupTransportEvent/Location/Name` = **Ferrano**  
  The 3PL's warehouse.
- `Consignment/ActualPickupTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Consignment/ConsigneeParty/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `Consignment/OriginalDepartureCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The goods start in Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/FinalDestinationCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  And end in Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/DeliveryTerms/ID` = **FCA** (schemeID `INCOTERMS`)  
  Incoterms 2020: free carrier at the seller's warehouse. The code is from the world's copy of Incoterms 2020: FCA = Free Carrier. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/DeliveryTerms/SpecialTerms` = **The buyer's carrier presents the truck; the seller loads it.**  
  Who loads, under FCA at the seller's premises.
- `Consignment/DeliveryTerms/LossRiskResponsibilityCode` = **BUYER** (listID `urn:ubl-examples:world:codelist:RiskResponsiblePartyCode`)  
  The risk passed to the buyer when the goods were loaded on the truck. The code is from the Trade Accord's party bearing the risk list: BUYER = Buyer.
- `Consignment/DeliveryTerms/LossRisk` = **The risk passes on loading at the 3PL's warehouse.**  
  In words.
- `Consignment/CollectPaymentTerms/Note` = **The freight is paid by the consignee under its contract with the carrier.**  
  Freight collect: the consignee pays.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The only stage: one truck from the warehouse to the distribution centre.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/MainCarriageShipmentStage/TransportMeansTypeCode` = **395** (listID `UNECE Recommendation 28`)  
  The truck pulls a trailer: the carrier's tractor unit 07 with its curtain-side trailer. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 395 = Truck, with trailer.
- `Consignment/MainCarriageShipmentStage/TransitDirectionCode` = **EXPORT** (listID `urn:ubl-examples:world:codelist:TransitDirectionCode`)  
  The goods leave Urvania by this stage. The code is from the Trade Accord's transit direction list: EXPORT = Export.
- `Consignment/MainCarriageShipmentStage/CabotageIndicator` = **false**  
  A carriage between two countries, not within a foreign one.
- `Consignment/MainCarriageShipmentStage/EstimatedDeliveryDate` = **2026-03-25**  
  The carrier's estimate when it takes over the goods: the goods-in slot of the third day. The leg is 174 km, about three hours' driving, but the truck reaches the border about 17:20, after the distributor's customs desk has closed, so the driver takes his night rest at the border and the import is declared in the morning; the distribution centre takes full loads in morning slots only, and the slot booked a week ahead is the next morning's.
- `Consignment/MainCarriageShipmentStage/EstimatedDeliveryTime` = **09:00:00**  
  Early in the working day.
- `Consignment/MainCarriageShipmentStage/RequiredDeliveryDate` = **2026-03-25**  
  The distributor's goods-in slot.
- `Consignment/MainCarriageShipmentStage/RequiredDeliveryTime` = **10:00:00**  
  By the end of the goods-in slot, 09:00 to 10:00; the latest delivery time of the note is the same.
- `Consignment/MainCarriageShipmentStage/TransitPeriod/StartDate` = **2026-03-23**  
  Collected in the afternoon; the stage has begun when the carrier takes over the goods.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **WB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: WB = Westbound.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **395** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tractor unit 07 with curtain-side trailer; the fleet of Trasvia Haulage. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 395 = Truck, with trailer.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **UR 4160 KT** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The registration plate of the truck; the fleet of Trasvia Haulage. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `Consignment/MainCarriageShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **UR 4160 TR** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `Consignment/MainCarriageShipmentStage/TransportMeans/OwnerParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/MainCarriageShipmentStage/TransportMeans/OwnerParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **LOADINGLENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The length of the loading floor. The code is from the Trade Accord's dimension attribute list: LOADINGLENGTH = Loading length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MeasurementDimension/Measure` = **13.6** (unitCode `MTR`)  
  Room for 33 pallets.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Ferrano**  
  Loaded at the 3PL's warehouse in Conciaro.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/ID` = **XBMRW** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **Marrowdale**  
  Unloaded at the distributor's distribution centre.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceDate` = **2026-03-23**  
  Expected once customs has released the export declaration and the truck may leave.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceTime` = **16:20:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/Name` = **Ferrano**  
  Castrano Logistics warehouse.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/DriverPerson/ID` = **XU-DL-0417722**  
  The number of the driving licence.
- `Consignment/MainCarriageShipmentStage/DriverPerson/FirstName` = **Ilario**  
  The driver of the truck.
- `Consignment/MainCarriageShipmentStage/DriverPerson/FamilyName` = **Bencetti**  
  The family name.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **UR 4160 TR** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The trailer, by its licence plate.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **TE** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code TE: trailer. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: TE = Trailer.
- `Consignment/TransportHandlingUnit/TransportEquipment/Description` = **Curtain-side semi-trailer, 13.6 m loading length**  
  The trailer in words.
- `Consignment/TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **7500** (unitCode `KGM`)  
  The trailer's empty weight, from the carrier's fleet.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **XU-CL-77310**  
  The number of the bolt seal on the trailer doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **SHIPPER** (listID `urn:ubl-examples:world:codelist:SealIssuerTypeCode`)  
  The seal is the 3PL's, which loads for the consignor. The code is from the Trade Accord's seal issuer type list: SHIPPER = Shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealStatusCode` = **APPLIED** (listID `urn:ubl-examples:world:codelist:SealStatusCode`)  
  In place when the carrier took over the goods. The code is from the Trade Accord's seal status list: APPLIED = Applied.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  Put on by the 3PL when the trailer was loaded.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506012** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 001 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506012**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506029** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 002 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506029**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506036** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 003 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506036**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506043** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 004 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506043**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506050** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 005 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506050**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506067** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 006 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506067**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506074** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 007 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506074**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506081** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 008 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506081**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506098** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 009 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506098**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506104** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 010 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506104**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506111** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 011 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506111**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506128** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 012 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506128**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506135** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 013 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506135**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506142** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 014 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506142**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506159** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 015 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506159**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506166** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 016 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506166**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506173** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 017 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506173**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506180** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 018 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506180**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506197** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 019 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506197**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506203** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 020 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506203**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506210** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 021 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506210**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506227** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 022 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506227**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506234** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 023 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506234**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506241** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **STACK2** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: STACK2 = Stack at most two high.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 4 benches in three parcels each: 4 × parcel 1 (frame carton), 4 × parcel 2 (frame carton with the bolt set), 4 × parcel 3 (slat bundle).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 024 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506241**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **745** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **216.2** (unitCode `KGM`)  
  The goods, 188 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **0.5** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ID` = **KXU105190004506258** (schemeID `ISO 15459`)  
  The number on the pallet label: the unit's licence plate in the structure of ISO/IEC 15459, which Castrano Logistics gives every unit it makes up: the Codana Identification Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar code on the label adds the data identifier J, which the document leaves out.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TransportHandlingUnitTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingCode` = **NOSTACK** (listID `urn:ubl-examples:world:codelist:HandlingInstructionCode`)  
  The carrier's handling code: two high, or nothing on top. The code is from the Trade Accord's handling instruction list: NOSTACK = Do not stack.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/HandlingInstructions` = **Fork-lift only. Load on top: nothing may be stacked on the cartons. Unpacked, each carton is a one-person lift.**  
  The handling, in words, with the world's rule for manual handling (ISO 11228-1).
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalGoodsItemQuantity` = **1** (unitCode `EA`)  
  One kind of goods on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TotalPackageQuantity` = **12** (unitCode `EA`)  
  The parcels on the pallet: 12 spare side frames, one to a frame carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/ShippingMarks` = **LD MARROWDALE / 025 of 025**  
  The marks on the pallet: the consignee's mark and the pallet's place in the count.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/TraceID` = **KXU105190004506258**  
  The pallet's barcode, scanned at each handover: it carries the same number.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **1850** (unitCode `MMT`)  
  Its length.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The pallet's footprint. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **700** (unitCode `MMT`)  
  Its width.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of the loaded pallet. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **740** (unitCode `MMT`)  
  Its height.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The loaded pallet's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/MeasurementDimension/Measure` = **174.6** (unitCode `KGM`)  
  The goods, 146.4 kg, and the pallet's own 28.2 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/AttributeID` = **FLOORSPACE** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The floor the pallet takes. The code is from the Trade Accord's attribute list: FLOORSPACE = Floor space. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/FloorSpaceMeasurementDimension/Measure` = **1.3** (unitCode `MTK`)  
  In square metres.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/AttributeID` = **PALLETPLACES** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The pallet places taken on the truck. The code is from the Trade Accord's attribute list: PALLETPLACES = Pallet places. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/PalletSpaceMeasurementDimension/Measure` = **1** (unitCode `C62`)  
  Half a place when two pallets are stacked; the frame cartons' pallet takes a whole one. A number of places, not of articles, so unit C62 (one), which allows a half.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/Quantity` = **1** (unitCode `EA`)  
  One side frame in each carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/ReturnableMaterialIndicator` = **false**  
  The carton stays with the frame.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackagingType` = **Frame carton, one side frame**  
  The carton in words; 12 of them on the pallet.
- `Consignment/TransportHandlingUnit/TransportEquipment/PackagedTransportHandlingUnit/Package/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `GoodsItem/ID` = **1**  
  The goods item number, as in the export declaration.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `GoodsItem/GrossWeightMeasure` = **5188.8** (unitCode `KGM`)  
  Their gross weight in their parcels, with the pallets they travel on.
- `GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The pieces taken over.
- `GoodsItem/ID` = **2**  
  The goods item number, as in the export declaration.
- `GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `GoodsItem/GrossWeightMeasure` = **174.6** (unitCode `KGM`)  
  Their gross weight in their parcels, with the pallets they travel on.
- `GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The pieces taken over.
- `Delivery/LatestDeliveryDate` = **2026-03-25**  
  The goods-in slot cannot move.
- `Delivery/LatestDeliveryTime` = **10:00:00**  
  The end of the slot, the time the delivery is required by.
- `Delivery/TrackingID` = **TH-26-04471**  
  Track the truck with the carrier's job number.
- `Delivery/EstimatedDeliveryPeriod/StartDate` = **2026-03-25**  
  The morning of the third day.
- `Delivery/EstimatedDeliveryPeriod/StartTime` = **09:00:00**  
  From nine, when the slot opens.
- `Delivery/EstimatedDeliveryPeriod/EndTime` = **10:00:00**  
  Until ten, when it closes.
- `ReturnAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ReturnAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `ReturnAddress/StreetName` = **Bek Han Stalvek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Castrano Logistics gives it.
- `ReturnAddress/StreetName` = **Via del Magazzino** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Castrano Logistics gives it.
- `ReturnAddress/BuildingNumber` = **24**  
  Building number of the postal address. As Castrano Logistics gives it.
- `ReturnAddress/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Castrano Logistics gives it.
- `ReturnAddress/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Castrano Logistics gives it.
- `ReturnAddress/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). As Castrano Logistics gives it.
- `ReturnAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Castrano Logistics gives it.
- `ReturnAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `ReturnAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `ReturnAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `OriginAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `OriginAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `OriginAddress/StreetName` = **Bek Han Stalvek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Castrano Logistics gives it.
- `OriginAddress/StreetName` = **Via del Magazzino** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Castrano Logistics gives it.
- `OriginAddress/BuildingNumber` = **24**  
  Building number of the postal address. As Castrano Logistics gives it.
- `OriginAddress/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Castrano Logistics gives it.
- `OriginAddress/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Castrano Logistics gives it.
- `OriginAddress/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). As Castrano Logistics gives it.
- `OriginAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Castrano Logistics gives it.
- `OriginAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `OriginAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `OriginAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `ExportCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The goods are exported from Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The original for the consignor.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALHANDED** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The consignor's original, handed over when the carrier took over the goods, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALHANDED = Original, handed over.
- `Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **TH-SIG-TH-WB-26-0159**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:waybill:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>TH-WB-26-0159</cbc:ID>
  <cbc:CarrierAssignedID>TH-CMR-26-0149</cbc:CarrierAssignedID>
  <cbc:UUID>4891662e-273a-5190-9aa7-edb87e35d8b5</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-03-23</cbc:IssueDate>
  <cbc:IssueTime>15:22:00-01:00</cbc:IssueTime>
  <cbc:Name>Consignment note under the road convention, the CMR</cbc:Name>
  <cbc:Note>Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.</cbc:Note>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">CMR</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
    <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Trasvia Haulage</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XU</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160203746888095</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Ban Kumek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via dei Trasporti</cbc:StreetName>
      <cbc:BuildingNumber>45</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4160</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Planning desk</cbc:Name>
      <cbc:JobTitle>Transport planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 1 041 266 7643</cbc:Telephone>
      <cbc:ElectronicMail>planning@trasvia.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104822</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
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
      <cbc:Name>Transport planning</cbc:Name>
      <cbc:JobTitle>Logistics planner</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
      <cbc:ElectronicMail>logistics@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160200467394686</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Stuzman Nulban</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Dispatch office</cbc:Name>
      <cbc:JobTitle>Dispatch coordinator</cbc:JobTitle>
      <cbc:Department>Warehouse</cbc:Department>
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>dispatch@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Trasvia Haulage</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:Shipment>
    <cbc:ID>CL-SH-26-0154</cbc:ID>
    <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">KEEPDRY</cbc:HandlingCode>
    <cbc:Information>Park benches, knocked down, and spare side frames, for resale.</cbc:Information>
    <cbc:GrossWeightMeasure unitCode="KGM">12863.4</cbc:GrossWeightMeasure>
    <cbc:NetNetWeightMeasure unitCode="KGM">4366.8</cbc:NetNetWeightMeasure>
    <cbc:GrossVolumeMeasure unitCode="MTQ">24.1</cbc:GrossVolumeMeasure>
    <cbc:TotalGoodsItemQuantity unitCode="EA">2</cbc:TotalGoodsItemQuantity>
    <cbc:SplitConsignmentIndicator>false</cbc:SplitConsignmentIndicator>
    <cbc:ConsignmentQuantity unitCode="EA">1</cbc:ConsignmentQuantity>
    <cac:Consignment>
      <cbc:ID>LD-CS-26-0152</cbc:ID>
      <cbc:CarrierAssignedID>TH-26-04471</cbc:CarrierAssignedID>
      <cbc:ConsigneeAssignedID>LD-GI-0412</cbc:ConsigneeAssignedID>
      <cbc:SummaryDescription>Park benches and spare side frames on 25 pallets.</cbc:SummaryDescription>
      <cbc:GrossWeightMeasure unitCode="KGM">5363.4</cbc:GrossWeightMeasure>
      <cbc:NetWeightMeasure unitCode="KGM">4366.8</cbc:NetWeightMeasure>
      <cbc:LoadingLengthMeasure unitCode="MTR">9.3</cbc:LoadingLengthMeasure>
      <cbc:Remarks>Received in apparent good order; trailer doors sealed by the 3PL, seal as recorded.</cbc:Remarks>
      <cbc:ContainerizedIndicator>false</cbc:ContainerizedIndicator>
      <cbc:GeneralCargoIndicator>true</cbc:GeneralCargoIndicator>
      <cbc:ThirdPartyPayerIndicator>false</cbc:ThirdPartyPayerIndicator>
      <cbc:CustomsClearanceServiceInstructions>The export is declared by the seller in Ferrano; the import by the distributor at the border.</cbc:CustomsClearanceServiceInstructions>
      <cbc:TotalTransportHandlingUnitQuantity unitCode="EA">25</cbc:TotalTransportHandlingUnitQuantity>
      <cbc:DeliveryInstructions>Enter by gate 3 of the business park and report to the gatehouse; unload at dock 4.</cbc:DeliveryInstructions>
      <cbc:HaulageInstructions>Wait at the warehouse until customs has released the export declaration.</cbc:HaulageInstructions>
      <cbc:TotalPackagesQuantity unitCode="EA">300</cbc:TotalPackagesQuantity>
      <cac:CustomsDeclaration>
        <cbc:ID>VI-CD-26-0156</cbc:ID>
        <cac:IssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Valdara Industries</cbc:Name>
          </cac:PartyName>
        </cac:IssuerParty>
      </cac:CustomsDeclaration>
      <cac:ActualPickupTransportEvent>
        <cbc:OccurrenceDate>2026-03-23</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>15:05:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:ActualPickupTransportEvent>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:ConsigneeParty>
      <cac:OriginalDepartureCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:OriginalDepartureCountry>
      <cac:FinalDestinationCountry>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:FinalDestinationCountry>
      <cac:DeliveryTerms>
        <cbc:ID schemeID="INCOTERMS">FCA</cbc:ID>
        <cbc:SpecialTerms>The buyer's carrier presents the truck; the seller loads it.</cbc:SpecialTerms>
        <cbc:LossRiskResponsibilityCode listID="urn:ubl-examples:world:codelist:RiskResponsiblePartyCode">BUYER</cbc:LossRiskResponsibilityCode>
        <cbc:LossRisk>The risk passes on loading at the 3PL's warehouse.</cbc:LossRisk>
      </cac:DeliveryTerms>
      <cac:CollectPaymentTerms>
        <cbc:Note>The freight is paid by the consignee under its contract with the carrier.</cbc:Note>
      </cac:CollectPaymentTerms>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">395</cbc:TransportMeansTypeCode>
        <cbc:TransitDirectionCode listID="urn:ubl-examples:world:codelist:TransitDirectionCode">EXPORT</cbc:TransitDirectionCode>
        <cbc:CabotageIndicator>false</cbc:CabotageIndicator>
        <cbc:EstimatedDeliveryDate>2026-03-25</cbc:EstimatedDeliveryDate>
        <cbc:EstimatedDeliveryTime>09:00:00</cbc:EstimatedDeliveryTime>
        <cbc:RequiredDeliveryDate>2026-03-25</cbc:RequiredDeliveryDate>
        <cbc:RequiredDeliveryTime>10:00:00</cbc:RequiredDeliveryTime>
        <cac:TransitPeriod>
          <cbc:StartDate>2026-03-23</cbc:StartDate>
        </cac:TransitPeriod>
        <cac:TransportMeans>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">WB</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">395</cbc:TransportMeansTypeCode>
          <cac:RoadTransport>
            <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 KT</cbc:LicensePlateID>
            <cbc:TrailerLicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 TR</cbc:TrailerLicensePlateID>
          </cac:RoadTransport>
          <cac:OwnerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Trasvia Haulage</cbc:Name>
            </cac:PartyName>
          </cac:OwnerParty>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LOADINGLENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MTR">13.6</cbc:Measure>
          </cac:MeasurementDimension>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XBMRW</cbc:ID>
          <cbc:Name>Marrowdale</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:UnloadingPortLocation>
        <cac:EstimatedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-03-23</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>16:20:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:EstimatedDepartureTransportEvent>
        <cac:DriverPerson>
          <cbc:ID>XU-DL-0417722</cbc:ID>
          <cbc:FirstName>Ilario</cbc:FirstName>
          <cbc:FamilyName>Bencetti</cbc:FamilyName>
        </cac:DriverPerson>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 TR</cbc:ID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">TE</cbc:TransportEquipmentTypeCode>
          <cbc:Description>Curtain-side semi-trailer, 13.6 m loading length</cbc:Description>
          <cbc:TareWeightMeasure unitCode="KGM">7500</cbc:TareWeightMeasure>
          <cac:TransportEquipmentSeal>
            <cbc:ID>XU-CL-77310</cbc:ID>
            <cbc:SealIssuerTypeCode listID="urn:ubl-examples:world:codelist:SealIssuerTypeCode">SHIPPER</cbc:SealIssuerTypeCode>
            <cbc:SealStatusCode listID="urn:ubl-examples:world:codelist:SealStatusCode">APPLIED</cbc:SealStatusCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506012</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 001 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506012</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506029</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 002 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506029</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506036</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 003 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506036</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506043</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 004 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506043</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506050</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 005 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506050</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506067</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 006 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506067</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506074</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 007 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506074</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506081</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 008 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506081</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506098</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 009 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506098</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506104</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 010 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506104</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506111</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 011 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506111</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506128</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 012 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506128</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506135</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 013 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506135</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506142</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 014 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506142</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506159</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 015 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506159</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506166</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 016 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506166</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506173</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 017 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506173</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506180</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 018 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506180</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506197</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 019 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506197</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506203</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 020 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506203</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506210</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 021 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506210</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506227</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 022 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506227</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506234</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 023 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506234</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506241</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">STACK2</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is a one-person lift; a slat bundle, 1.81 m long, is carried by two.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 024 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506241</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">745</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">216.2</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">0.5</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
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
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">13</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
            <cac:Package>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
              <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
              <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">1810</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">295</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="MMT">100</cbc:Measure>
              </cac:MeasurementDimension>
              <cac:MeasurementDimension>
                <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
                <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
              </cac:MeasurementDimension>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
          <cac:PackagedTransportHandlingUnit>
            <cbc:ID schemeID="ISO 15459">KXU105190004506258</cbc:ID>
            <cbc:TransportHandlingUnitTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:TransportHandlingUnitTypeCode>
            <cbc:HandlingCode listID="urn:ubl-examples:world:codelist:HandlingInstructionCode">NOSTACK</cbc:HandlingCode>
            <cbc:HandlingInstructions>Fork-lift only. Load on top: nothing may be stacked on the cartons. Unpacked, each carton is a one-person lift.</cbc:HandlingInstructions>
            <cbc:TotalGoodsItemQuantity unitCode="EA">1</cbc:TotalGoodsItemQuantity>
            <cbc:TotalPackageQuantity unitCode="EA">12</cbc:TotalPackageQuantity>
            <cbc:ShippingMarks>LD MARROWDALE / 025 of 025</cbc:ShippingMarks>
            <cbc:TraceID>KXU105190004506258</cbc:TraceID>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1850</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">700</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">740</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">174.6</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:FloorSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">FLOORSPACE</cbc:AttributeID>
              <cbc:Measure unitCode="MTK">1.3</cbc:Measure>
            </cac:FloorSpaceMeasurementDimension>
            <cac:PalletSpaceMeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">PALLETPLACES</cbc:AttributeID>
              <cbc:Measure unitCode="C62">1</cbc:Measure>
            </cac:PalletSpaceMeasurementDimension>
            <cac:Package>
              <cbc:Quantity unitCode="EA">1</cbc:Quantity>
              <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
              <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
              <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
              <cbc:PackagingType>Frame carton, one side frame</cbc:PackagingType>
              <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
            </cac:Package>
          </cac:PackagedTransportHandlingUnit>
        </cac:TransportEquipment>
      </cac:TransportHandlingUnit>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">5188.8</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Bench side frame casting</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">174.6</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">12</cbc:Quantity>
    </cac:GoodsItem>
    <cac:Delivery>
      <cbc:LatestDeliveryDate>2026-03-25</cbc:LatestDeliveryDate>
      <cbc:LatestDeliveryTime>10:00:00</cbc:LatestDeliveryTime>
      <cbc:TrackingID>TH-26-04471</cbc:TrackingID>
      <cac:EstimatedDeliveryPeriod>
        <cbc:StartDate>2026-03-25</cbc:StartDate>
        <cbc:StartTime>09:00:00</cbc:StartTime>
        <cbc:EndTime>10:00:00</cbc:EndTime>
      </cac:EstimatedDeliveryPeriod>
    </cac:Delivery>
    <cac:ReturnAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Stalvek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Magazzino</cbc:StreetName>
      <cbc:BuildingNumber>24</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Zhildir</cbc:CityName>
      <cbc:CityName languageID="en-XU">Conciaro</cbc:CityName>
      <cbc:PostalZone>4190</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:ReturnAddress>
    <cac:OriginAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Stalvek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Magazzino</cbc:StreetName>
      <cbc:BuildingNumber>24</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Zhildir</cbc:CityName>
      <cbc:CityName languageID="en-XU">Conciaro</cbc:CityName>
      <cbc:PostalZone>4190</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:OriginAddress>
    <cac:ExportCountry>
      <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
    </cac:ExportCountry>
  </cac:Shipment>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALHANDED</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Castrano Logistics</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>TH-SIG-TH-WB-26-0159</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Trasvia Haulage</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
