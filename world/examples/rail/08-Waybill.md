# Waybill: Ferrano Rail Cargo to Valdara Industries

*Example 8 of the flow "Containers by rail under the Accord's common transit (Urvania → Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The rail consignment note under the Accord's uniform rules goes to the transport user, the seller; the road haulage to the hub is a pre-carriage stage of the same contract.

[The XML file](08-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900043586**  
  The collaboration this document belongs to: the rail carriage Valdara books with Ferrano Rail Cargo. Valdara Industries started it and gave it this identifier, which every document of it repeats.
- `ID` = **7200092547**  
  The consignment note number.
- `CarrierAssignedID` = **8900004628**  
  The carrier's own number for the carriage.
- `UUID` = **2af02244-330b-5e9f-85c5-1ad7dcce9c43**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-04-14**  
  Made out at the hub when the boxes are on the train, before it leaves: the note records the takeover, not the journey.
- `IssueTime` = **06:10:00-01:00**  
  After both boxes were lifted onto the train, at 05:40 and 05:55, before the timetabled departure; in the issuer's local time, with its offset from UTC.
- `Name` = **Rail consignment note under the Accord's uniform rules for international carriage by rail**  
  The kind of transport document.
- `Description` = **Two containers of park benches, carried by the carrier's tractor from Castrano's warehouse to the Ferrano hub and by the container train to Lumeway's siding in Marrowdale, under the Accord's common transit.**  
  The rail carriage in words, with its road pre-carriage.
- `Note` = **Gurbul mizstan: drek starzhek, ginrul nartran zaskek drek sundraz hangaz nartran drek valnir; drek trelgir, vek drek valnir; drek vuznek, zhiztrek man drek sundraz.** (languageID `qau`)  
  The note in Urvanian, the sender's language: The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed.
- `Note` = **Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed.
- `WaybillTypeCode` = **CIM** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: CIM = Rail consignment note (the Accord's rules after the CIM).
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Name` = **Ferrano Intermodal Hub**  
  Where the note was made out: the hub, where the boxes went on the train.
- `Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Rail Cargo gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; as Ferrano Rail Cargo gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `PostalAddress/ID` = **4170201115930918** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Rail Cargo gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Rumir Hekrul Zhuzkek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Rail Cargo gives it.
- `PostalAddress/StreetName` = **Viale della Stazione** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Rail Cargo gives it.
- `PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. As Ferrano Rail Cargo gives it.
- `PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Rail Cargo gives it.
- `PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Rail Cargo gives it.
- `PostalAddress/PostalZone` = **4310**  
  Postal code in Urvania's format (4 digits). As Ferrano Rail Cargo gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Rail Cargo gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Freight desk**  
  The party's main desk, which handles this document; as Ferrano Rail Cargo gives it.
- `Contact/JobTitle` = **Freight planner**  
  The job of the person who answers at the desk; as Ferrano Rail Cargo gives it.
- `Contact/Department` = **Operations**  
  The department the desk belongs to; as Ferrano Rail Cargo gives it.
- `Contact/Telephone` = **+999 1 0413 67100**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Ferrano Rail Cargo gives it.
- `Contact/ElectronicMail` = **freight@ferranorail.example**  
  The contact's e-mail address; as Ferrano Rail Cargo gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Ferrano Rail Cargo gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Ferrano Rail Cargo gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Valdara Industries gives it.
- `PartyName/Name` = **Valdara Industries**  
  The trading name; as Valdara Industries gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
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
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); as Valdara Industries gives it.
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Contact/ElectronicMail` = **logistics@valdara.example**  
  The contact's e-mail address; as Valdara Industries gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Valdara Industries gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **7400043688**  
  The shipment as the despatching party numbered it.
- `GrossWeightMeasure` = **18177.6** (unitCode `KGM`)  
  The gross weights of the transport equipment with the goods in it (9088.8 + 9088.8 kg): a shipment's gross weight includes the equipment.
- `Consignment/ID` = **7300043586**  
  The manufacturer's consignment number.
- `Consignment/ContractedCarrierAssignedID` = **FRC-CON-2026-005/88**  
  The call-off under the framework contract.
- `Consignment/SummaryDescription` = **192 park benches in two 40-foot containers.**  
  The goods in a few words.
- `Consignment/GrossWeightMeasure` = **10377.6** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight of the two containers' cargo.
- `Consignment/ContainerizedIndicator` = **true**  
  Two full containers.
- `Consignment/TotalTransportHandlingUnitQuantity` = **2** (unitCode `EA`)  
  Two containers.
- `Consignment/LoadingSequenceID` = **7**  
  The consignment's turn in the loading of the train.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **goodsin@lumeway.example**  
  The contact's e-mail address; as Lumeway Distribution gives it.
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Lumeway Distribution gives it.
- `Consignment/TransportContract/ID` = **FRC-CON-2026-005**  
  The framework contract for container slots.
- `Consignment/TransportContract/IssueDate` = **2026-01-05**  
  Signed at the start of the year.
- `Consignment/TransportContract/ContractType` = **Framework contract for container slots**  
  What it is.
- `Consignment/PrepaidPaymentTerms/Note` = **Freight prepaid by the consignor under DAP.**  
  The seller pays the carriage.
- `Consignment/MainCarriageShipmentStage/ID` = **2**  
  The main carriage, by rail.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **2** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 2: rail transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 2 = Rail transport.
- `Consignment/MainCarriageShipmentStage/LoadingSequenceID` = **7**  
  The order the boxes go on the train: these two are the seventh lift.
- `Consignment/MainCarriageShipmentStage/SuccessiveSequenceID` = **1**  
  The first and only rail stage.
- `Consignment/MainCarriageShipmentStage/Instructions` = **Shunt to the Lumeway siding in Marrowdale once the import is declared.**  
  What the railway must do.
- `Consignment/MainCarriageShipmentStage/DemurrageInstructions` = **Free time five days at the siding, counted from the day after the boxes are placed; then demurrage of 7,500 ferra per container day, under framework contract FRC-CON-2026-005.**  
  What waiting costs: the framework contract's free time and rate.
- `Consignment/MainCarriageShipmentStage/CrewQuantity` = **2** (unitCode `IE`)  
  Two persons: a driver and a train manager.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **CT 4471**  
  The number of the container train in the hub's timetable.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **WB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: WB = Westbound.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **2302** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: container train Ferrano–Marrowdale; the fleet of Ferrano Rail Cargo. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 2302 = Train, container.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RailTransport/TrainID` = **FRC 4417**  
  The train number; the fleet of Ferrano Rail Cargo.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The timetable departure from the hub.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceTime` = **06:45:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceDate` = **2026-04-15**  
  The timetable arrival at the siding in Marrowdale: the train reaches Marrowdale yard about 15:10 the day before, 173 km from the hub, and the next morning's shunting trip places the boxes on Lumeway's siding.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceTime` = **10:30:00-01:00**  
  The local time of Bayvarra, where it happens, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `Consignment/MainCarriageShipmentStage/PlannedWaypointTransportEvent/OccurrenceDate` = **2026-04-14**  
  Planned departure from the border station, 63 km from the hub: the train stops there from about 08:00 for the crew change, the brake test and the customs' check of the seals, and leaves on its timetabled path into Bayvarra.
- `Consignment/MainCarriageShipmentStage/PlannedWaypointTransportEvent/OccurrenceTime` = **13:00:00-01:00**  
  The issuer's local time, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/PlannedWaypointTransportEvent/Location/Name` = **Rail border station Urvania–Bayvarra**  
  Where the train crosses the border.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The departure as expected that morning.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceTime` = **06:50:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/OccurrenceDate` = **2026-04-15**  
  The arrival as expected.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/OccurrenceTime` = **10:40:00-01:00**  
  The local time of Bayvarra, where it happens, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `Consignment/PreCarriageShipmentStage/ID` = **1**  
  The pre-carriage: the carrier's tractor brings the packed boxes to the hub.
- `Consignment/PreCarriageShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `Consignment/PreCarriageShipmentStage/Instructions` = **Two runs of the one tractor and chassis, one box a run: the first leaves the warehouse at 13:00, the second at 15:00.**  
  How the haulage is done: the carrier's container chassis takes one box at a time.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/PreCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **37** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: container tractor for carrier haulage; the fleet of Ferrano Rail Cargo. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 37 = Truck, container.
- `Consignment/PreCarriageShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **UR 4160 RC** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The registration plate of the truck; the fleet of Ferrano Rail Cargo. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `Consignment/PreCarriageShipmentStage/LoadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/PreCarriageShipmentStage/LoadingPortLocation/Name` = **Castrano Logistics warehouse, Conciaro**  
  Where the boxes are collected.
- `Consignment/PreCarriageShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/PreCarriageShipmentStage/UnloadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/PreCarriageShipmentStage/UnloadingPortLocation/Name` = **Ferrano Intermodal Hub**  
  Where they are handed to the terminal.
- `Consignment/PreCarriageShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **FRXU1044175** (schemeID `ISO6346`)  
  The container's number: owner code, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReferencedConsignmentID` = **7300043586**  
  The consignment the container carries.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: CN = Container.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderTypeCode` = **CARRIER** (listID `urn:ubl-examples:world:codelist:EquipmentProviderTypeCode`)  
  The rail carrier provides the container. The code is from the Trade Accord's equipment provider type list: CARRIER = Carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerTypeCode` = **CARRIER** (listID `urn:ubl-examples:world:codelist:EquipmentOwnerTypeCode`)  
  And owns it. The code is from the Trade Accord's equipment owner type list: CARRIER = Carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45G1** (listID `ISO 6346`)  
  ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose. The code is from the world's copy of ISO 6346 container size and type code: 45G1 = 40 ft, 9 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/DispositionCode` = **LOADED** (listID `urn:ubl-examples:world:codelist:EquipmentDispositionCode`)  
  Loaded with cargo. The code is from the Trade Accord's equipment disposition list: LOADED = Loaded.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL** (listID `urn:ubl-examples:world:codelist:LoadTypeCode`)  
  A full container load for one consignee. The code is from the Trade Accord's load type list: FCL = Full container load.
- `Consignment/TransportHandlingUnit/TransportEquipment/Information` = **Return empty to the Ferrano hub within five days.**  
  What happens to the box afterwards.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The container goes back to its owner.
- `Consignment/TransportHandlingUnit/TransportEquipment/Characteristics` = **Steel, high cube, wooden floor.**  
  What kind of box it is.
- `Consignment/TransportHandlingUnit/TransportEquipment/DamageRemarks` = **Small dent in the left side panel, noted at pick-up; no effect on the cargo.**  
  Damage noted when the box was positioned, so it is not blamed on this carriage.
- `Consignment/TransportHandlingUnit/TransportEquipment/Description` = **40-foot high cube container**  
  The container in words.
- `Consignment/TransportHandlingUnit/TransportEquipment/SpecialTransportRequirements` = **Load with the doors to the rear of the wagon.**  
  How it rides.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **9088.8** (unitCode `KGM`)  
  Half the benches, on their 24 pallets, and the container's own 3,900 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossVolumeMeasure` = **76.3** (unitCode `MTQ`)  
  The inside volume of a 40-foot high cube.
- `Consignment/TransportHandlingUnit/TransportEquipment/TrackingDeviceCode` = **GPS** (listID `urn:ubl-examples:world:codelist:TrackingDeviceCode`)  
  The box carries a satellite tracker. The code is from the Trade Accord's tracking device list: GPS = Satellite tracker.
- `Consignment/TransportHandlingUnit/TransportEquipment/PowerIndicator` = **false**  
  It needs no power: not a reefer.
- `Consignment/TransportHandlingUnit/TransportEquipment/TraceID` = **TRK-FRXU1044175**  
  The tracker's number.
- `Consignment/TransportHandlingUnit/TransportEquipment/StowagePositionID` = **31 46 4521 042-3 / A**  
  The wagon and the slot on it the box rides in: the first container wagon of the train, each box on a wagon of its own.
- `Consignment/TransportHandlingUnit/TransportEquipment/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The outside length. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MeasurementDimension/Measure` = **12192** (unitCode `MMT`)  
  Forty feet.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **XU-VI-30411**  
  The number of the bolt seal on the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **SHIPPER** (listID `urn:ubl-examples:world:codelist:SealIssuerTypeCode`)  
  The seal was issued by the shipper. The code is from the Trade Accord's seal issuer type list: SHIPPER = Shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/Condition` = **Intact**  
  As found at the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealStatusCode` = **APPLIED** (listID `urn:ubl-examples:world:codelist:SealStatusCode`)  
  The seal is in place. The code is from the Trade Accord's seal status list: APPLIED = Applied.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  And put on by the shipper when it packed the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingProofParty/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingProofParty/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/Name` = **Ferrano**  
  Packed at the 3PL's warehouse in Conciaro.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/ID` = **XBMRW** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/Name` = **Marrowdale**  
  Unpacked at the distributor's siding.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/OccurrenceDate` = **2026-04-10**  
  The carrier's tractor delivered the empty box to the warehouse for packing, on the Friday before.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/OccurrenceTime` = **08:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/OccurrenceDate` = **2026-04-15**  
  Planned arrival at the siding.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/OccurrenceTime` = **11:00:00-01:00**  
  The local time of Bayvarra, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/OccurrenceDate` = **2026-04-13**  
  Collected packed from the warehouse: the first of the tractor's two runs to the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/OccurrenceTime` = **13:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/OccurrenceDate` = **2026-04-13**  
  Stacked at the hub overnight, 46 km from the warehouse.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/OccurrenceTime` = **14:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/Name` = **Ferrano Intermodal Hub, stack C**  
  The hub's stack where the boxes wait for the train.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/OccurrenceDate` = **2026-04-14**  
  Lifted onto its wagon.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/OccurrenceTime` = **05:40:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/ApplicableTransportMeans/RailTransport/TrainID` = **FRC 4417**  
  The train.
- `Consignment/TransportHandlingUnit/TransportEquipment/ApplicableTransportMeans/RailTransport/RailCarID` = **31 46 4521 042-3** (schemeID `urn:ubl-examples:world:XU:rail-vehicle-register`)  
  The container wagon it rides on. The schemeID names the scheme it is from: the national vehicle register of Urvania (railway vehicles) (the UIC 12-digit wagon number: interoperability and gauge (2 digits), country 46, type (4), serial (3) and the check digit).
- `Consignment/TransportHandlingUnit/TransportEquipment/HaulageTradingTerms/Information` = **Carrier haulage: the rail carrier brings the box to the warehouse and back.**  
  Who moves the empty box.
- `Consignment/TransportHandlingUnit/TransportEquipment/HaulageTradingTerms/Reference` = **FRC-HT-2026**  
  The carrier's haulage terms.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The freight for this box.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/AllowanceChargeReason` = **Rail freight per container**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/Amount` = **54600** (currencyID `XUF`)  
  The price of one container slot.
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/LatestDeliveryDate` = **2026-04-16**  
  At the latest.
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/DeliveryLocation/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/DeliveryLocation/Name` = **Rail siding of Lumeway Distribution, Marrowdale**  
  Where.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/ActualPickupDate` = **2026-04-13**  
  Collected.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/ActualPickupTime` = **13:00:00-01:00**  
  The time; in the local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/PickupLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/PickupLocation/Name` = **Castrano Logistics warehouse, Conciaro**  
  Where.
- `Consignment/TransportHandlingUnit/TransportEquipment/Despatch/EstimatedDespatchDate` = **2026-04-14**  
  The train is expected to leave the hub that morning; the consignment note is made out before it leaves.
- `Consignment/TransportHandlingUnit/TransportEquipment/Despatch/EstimatedDespatchTime` = **06:50:00-01:00**  
  Ten to seven; in the local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/ID` = **7800004369**  
  The transit declaration the box travels under.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/IssuerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/IssuerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/EnergyConsumptionAllocation/EnergySourceTypeCode` = **ELECTRICITY** (listID `urn:ubl-examples:world:codelist:EnergySourceCode`)  
  The train runs on electricity. The code is from the Trade Accord's energy source list: ELECTRICITY = Electricity.
- `Consignment/TransportHandlingUnit/EnergyConsumptionAllocation/AllocatedEnergyMeasure` = **610** (unitCode `KWH`)  
  This box's share of the train's energy, by weight.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **FRXU1044180** (schemeID `ISO6346`)  
  The container's number: owner code, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReferencedConsignmentID` = **7300043586**  
  The consignment the container carries.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: CN = Container.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderTypeCode` = **CARRIER** (listID `urn:ubl-examples:world:codelist:EquipmentProviderTypeCode`)  
  The rail carrier provides the container. The code is from the Trade Accord's equipment provider type list: CARRIER = Carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerTypeCode` = **CARRIER** (listID `urn:ubl-examples:world:codelist:EquipmentOwnerTypeCode`)  
  And owns it. The code is from the Trade Accord's equipment owner type list: CARRIER = Carrier.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45G1** (listID `ISO 6346`)  
  ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose. The code is from the world's copy of ISO 6346 container size and type code: 45G1 = 40 ft, 9 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/DispositionCode` = **LOADED** (listID `urn:ubl-examples:world:codelist:EquipmentDispositionCode`)  
  Loaded with cargo. The code is from the Trade Accord's equipment disposition list: LOADED = Loaded.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL** (listID `urn:ubl-examples:world:codelist:LoadTypeCode`)  
  A full container load for one consignee. The code is from the Trade Accord's load type list: FCL = Full container load.
- `Consignment/TransportHandlingUnit/TransportEquipment/Information` = **Return empty to the Ferrano hub within five days.**  
  What happens to the box afterwards.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReturnabilityIndicator` = **true**  
  The container goes back to its owner.
- `Consignment/TransportHandlingUnit/TransportEquipment/Characteristics` = **Steel, high cube, wooden floor.**  
  What kind of box it is.
- `Consignment/TransportHandlingUnit/TransportEquipment/Description` = **40-foot high cube container**  
  The container in words.
- `Consignment/TransportHandlingUnit/TransportEquipment/SpecialTransportRequirements` = **Load with the doors to the rear of the wagon.**  
  How it rides.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **9088.8** (unitCode `KGM`)  
  Half the benches, on their 24 pallets, and the container's own 3,900 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossVolumeMeasure` = **76.3** (unitCode `MTQ`)  
  The inside volume of a 40-foot high cube.
- `Consignment/TransportHandlingUnit/TransportEquipment/TrackingDeviceCode` = **GPS** (listID `urn:ubl-examples:world:codelist:TrackingDeviceCode`)  
  The box carries a satellite tracker. The code is from the Trade Accord's tracking device list: GPS = Satellite tracker.
- `Consignment/TransportHandlingUnit/TransportEquipment/PowerIndicator` = **false**  
  It needs no power: not a reefer.
- `Consignment/TransportHandlingUnit/TransportEquipment/TraceID` = **TRK-FRXU1044180**  
  The tracker's number.
- `Consignment/TransportHandlingUnit/TransportEquipment/StowagePositionID` = **31 46 4521 043-1 / A**  
  The wagon and the slot on it the box rides in: the second container wagon of the train, each box on a wagon of its own.
- `Consignment/TransportHandlingUnit/TransportEquipment/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The outside length. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/TransportHandlingUnit/TransportEquipment/MeasurementDimension/Measure` = **12192** (unitCode `MMT`)  
  Forty feet.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **XU-VI-30412**  
  The number of the bolt seal on the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **SHIPPER** (listID `urn:ubl-examples:world:codelist:SealIssuerTypeCode`)  
  The seal was issued by the shipper. The code is from the Trade Accord's seal issuer type list: SHIPPER = Shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/Condition` = **Intact**  
  As found at the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealStatusCode` = **APPLIED** (listID `urn:ubl-examples:world:codelist:SealStatusCode`)  
  The seal is in place. The code is from the Trade Accord's seal status list: APPLIED = Applied.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  And put on by the shipper when it packed the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/ProviderParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingProofParty/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingProofParty/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OwnerParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/Name` = **Ferrano**  
  Packed at the 3PL's warehouse in Conciaro.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/ID` = **XBMRW** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/Name` = **Marrowdale**  
  Unpacked at the distributor's siding.
- `Consignment/TransportHandlingUnit/TransportEquipment/UnloadingLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/OccurrenceDate` = **2026-04-10**  
  The carrier's tractor delivered the empty box to the warehouse for packing, on the Friday before.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/OccurrenceTime` = **10:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/OccurrenceDate` = **2026-04-15**  
  Planned arrival at the siding.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/OccurrenceTime` = **11:00:00-01:00**  
  The local time of Bayvarra, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/OccurrenceDate` = **2026-04-13**  
  Collected packed from the warehouse: the second of the tractor's two runs to the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/OccurrenceTime` = **15:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/OccurrenceDate` = **2026-04-13**  
  Stacked at the hub overnight, 46 km from the warehouse.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/OccurrenceTime` = **16:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/Name` = **Ferrano Intermodal Hub, stack C**  
  The hub's stack where the boxes wait for the train.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/OccurrenceDate` = **2026-04-14**  
  Lifted onto its wagon.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/OccurrenceTime` = **05:55:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/ApplicableTransportMeans/RailTransport/TrainID` = **FRC 4417**  
  The train.
- `Consignment/TransportHandlingUnit/TransportEquipment/ApplicableTransportMeans/RailTransport/RailCarID` = **31 46 4521 043-1** (schemeID `urn:ubl-examples:world:XU:rail-vehicle-register`)  
  The container wagon it rides on. The schemeID names the scheme it is from: the national vehicle register of Urvania (railway vehicles) (the UIC 12-digit wagon number: interoperability and gauge (2 digits), country 46, type (4), serial (3) and the check digit).
- `Consignment/TransportHandlingUnit/TransportEquipment/HaulageTradingTerms/Information` = **Carrier haulage: the rail carrier brings the box to the warehouse and back.**  
  Who moves the empty box.
- `Consignment/TransportHandlingUnit/TransportEquipment/HaulageTradingTerms/Reference` = **FRC-HT-2026**  
  The carrier's haulage terms.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The freight for this box.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/AllowanceChargeReason` = **Rail freight per container**  
  In words.
- `Consignment/TransportHandlingUnit/TransportEquipment/FreightAllowanceCharge/Amount` = **54600** (currencyID `XUF`)  
  The price of one container slot.
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/LatestDeliveryDate` = **2026-04-16**  
  At the latest.
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/DeliveryLocation/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples).
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/DeliveryLocation/Name` = **Rail siding of Lumeway Distribution, Marrowdale**  
  Where.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/ActualPickupDate` = **2026-04-13**  
  Collected.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/ActualPickupTime` = **15:00:00-01:00**  
  The time; in the local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/PickupLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/PickupLocation/Name` = **Castrano Logistics warehouse, Conciaro**  
  Where.
- `Consignment/TransportHandlingUnit/TransportEquipment/Despatch/EstimatedDespatchDate` = **2026-04-14**  
  The train is expected to leave the hub that morning; the consignment note is made out before it leaves.
- `Consignment/TransportHandlingUnit/TransportEquipment/Despatch/EstimatedDespatchTime` = **06:50:00-01:00**  
  Ten to seven; in the local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/ID` = **7800004369**  
  The transit declaration the box travels under.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/IssuerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/IssuerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/EnergyConsumptionAllocation/EnergySourceTypeCode` = **ELECTRICITY** (listID `urn:ubl-examples:world:codelist:EnergySourceCode`)  
  The train runs on electricity. The code is from the Trade Accord's energy source list: ELECTRICITY = Electricity.
- `Consignment/TransportHandlingUnit/EnergyConsumptionAllocation/AllocatedEnergyMeasure` = **610** (unitCode `KWH`)  
  This box's share of the train's energy, by weight.
- `Consignment/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  Greenhouse gases of the carriage, as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Consignment/EnvironmentalEmission/ValueMeasure` = **410** (unitCode `KGM`)  
  For the two containers over the route.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  From the electric train's energy use. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementFromLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementFromLocation/Name` = **Ferrano Intermodal Hub**  
  From.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementToLocation/ID` = **XBMRW** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementToLocation/Name` = **Marrowdale**  
  To.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/EmissionCalculationLocation/Name` = **Ferrano Rail Cargo, energy office**  
  Where the figure was calculated.
- `GoodsItem/ID` = **1**  
  The goods item number: the benches in the first container.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **5188.8** (unitCode `KGM`)  
  The gross weight of these benches, in their parcels and with the 24 pallets they travel on.
- `GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The benches of one lot, which fill the first container.
- `GoodsItem/Item/Name` = **Park bench Serra 180**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `GoodsItem/Item/ItemInstance/LotIdentification/LotNumberID` = **VI-LOT-260409**  
  The production lot the box holds, as the consignor declared it; the lot's other facts are in the despatch advice.
- `GoodsItem/GoodsItemContainer/ID` = **1**  
  The goods item travels in one container only.
- `GoodsItem/GoodsItemContainer/TransportEquipment/ID` = **FRXU1044175** (schemeID `ISO6346`)  
  The first container, the box this lot was packed in.
- `GoodsItem/ID` = **2**  
  The goods item number: the benches in the second container.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **5188.8** (unitCode `KGM`)  
  The gross weight of these benches, in their parcels and with the 24 pallets they travel on.
- `GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The benches of one lot, which fill the second container.
- `GoodsItem/Item/Name` = **Park bench Serra 180**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `GoodsItem/Item/ItemInstance/LotIdentification/LotNumberID` = **VI-LOT-260410**  
  The production lot the box holds, as the consignor declared it; the lot's other facts are in the despatch advice.
- `GoodsItem/GoodsItemContainer/ID` = **1**  
  The goods item travels in one container only.
- `GoodsItem/GoodsItemContainer/TransportEquipment/ID` = **FRXU1044180** (schemeID `ISO6346`)  
  The second container, the box this lot was packed in.

### Document Reference

Inside `DocumentReference`:

- `ID` = **9500055446**  
  The transport plan under which the carriage is performed.
- `DocumentTypeCode` = **TransportExecutionPlan** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 9500055446 is the example rail/03, a TransportExecutionPlan; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: TransportExecutionPlan = Transport Execution Plan.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The original for the consignor.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALHANDED** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The consignor's original, handed over when the carrier took over the goods, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALHANDED = Original, handed over.
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **2**  
  The original for the consignee.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALWITHGOODS** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  One of the three originals travels with the goods to the consignee, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALWITHGOODS = Original, with the goods.
- `DistributionType` = **Rikzhek, vek drek valnir: drek trelgir rikzhek** (languageID `qau`)  
  The name of code ORIGINALWITHGOODS in the Trade Accord's distribution type list, followed by the detail of this case: the original the consignee signs on delivery. In Urvanian, the sender's language.
- `DistributionType` = **Original, with the goods: the consignee's original** (languageID `en-XU`)  
  The name of code ORIGINALWITHGOODS in the Trade Accord's distribution type list, followed by the detail of this case: the original the consignee signs on delivery. In English.
- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FRC-SIG-7200092547**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Rail Cargo**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:waybill:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900043586</cbc:ProfileExecutionID>
  <cbc:ID>7200092547</cbc:ID>
  <cbc:CarrierAssignedID>8900004628</cbc:CarrierAssignedID>
  <cbc:UUID>2af02244-330b-5e9f-85c5-1ad7dcce9c43</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-04-14</cbc:IssueDate>
  <cbc:IssueTime>06:10:00-01:00</cbc:IssueTime>
  <cbc:Name>Rail consignment note under the Accord's uniform rules for international carriage by rail</cbc:Name>
  <cbc:Description>Two containers of park benches, carried by the carrier's tractor from Castrano's warehouse to the Ferrano hub and by the container train to Lumeway's siding in Marrowdale, under the Accord's common transit.</cbc:Description>
  <cbc:Note languageID="qau">Gurbul mizstan: drek starzhek, ginrul nartran zaskek drek sundraz hangaz nartran drek valnir; drek trelgir, vek drek valnir; drek vuznek, zhiztrek man drek sundraz.</cbc:Note>
  <cbc:Note languageID="en-XU">Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.</cbc:Note>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">CIM</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
    <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Rail Cargo</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4170201115930918</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Rumir Hekrul Zhuzkek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Viale della Stazione</cbc:StreetName>
      <cbc:BuildingNumber>38</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
      <cbc:CityName languageID="en-XU">Serravona</cbc:CityName>
      <cbc:PostalZone>4310</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Freight desk</cbc:Name>
      <cbc:JobTitle>Freight planner</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 1 0413 67100</cbc:Telephone>
      <cbc:ElectronicMail>freight@ferranorail.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104685</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
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
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
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
      <cbc:Name>Transport planning</cbc:Name>
      <cbc:JobTitle>Logistics planner</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>logistics@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Rail Cargo</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:Shipment>
    <cbc:ID>7400043688</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">18177.6</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>7300043586</cbc:ID>
      <cbc:ContractedCarrierAssignedID>FRC-CON-2026-005/88</cbc:ContractedCarrierAssignedID>
      <cbc:SummaryDescription>192 park benches in two 40-foot containers.</cbc:SummaryDescription>
      <cbc:GrossWeightMeasure unitCode="KGM">10377.6</cbc:GrossWeightMeasure>
      <cbc:ContainerizedIndicator>true</cbc:ContainerizedIndicator>
      <cbc:TotalTransportHandlingUnitQuantity unitCode="EA">2</cbc:TotalTransportHandlingUnitQuantity>
      <cbc:LoadingSequenceID>7</cbc:LoadingSequenceID>
      <cac:ConsigneeParty>
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
          <cbc:Name>Goods-in</cbc:Name>
          <cbc:JobTitle>Goods-in supervisor</cbc:JobTitle>
          <cbc:Department>Warehouse</cbc:Department>
          <cbc:Telephone>+999 2 7121 955 964</cbc:Telephone>
          <cbc:ElectronicMail>goodsin@lumeway.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:TransportContract>
        <cbc:ID>FRC-CON-2026-005</cbc:ID>
        <cbc:IssueDate>2026-01-05</cbc:IssueDate>
        <cbc:ContractType>Framework contract for container slots</cbc:ContractType>
      </cac:TransportContract>
      <cac:PrepaidPaymentTerms>
        <cbc:Note>Freight prepaid by the consignor under DAP.</cbc:Note>
      </cac:PrepaidPaymentTerms>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>2</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">2</cbc:TransportModeCode>
        <cbc:LoadingSequenceID>7</cbc:LoadingSequenceID>
        <cbc:SuccessiveSequenceID>1</cbc:SuccessiveSequenceID>
        <cbc:Instructions>Shunt to the Lumeway siding in Marrowdale once the import is declared.</cbc:Instructions>
        <cbc:DemurrageInstructions>Free time five days at the siding, counted from the day after the boxes are placed; then demurrage of 7,500 ferra per container day, under framework contract FRC-CON-2026-005.</cbc:DemurrageInstructions>
        <cbc:CrewQuantity unitCode="IE">2</cbc:CrewQuantity>
        <cac:TransportMeans>
          <cbc:JourneyID>CT 4471</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">WB</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">2302</cbc:TransportMeansTypeCode>
          <cac:RailTransport>
            <cbc:TrainID>FRC 4417</cbc:TrainID>
          </cac:RailTransport>
        </cac:TransportMeans>
        <cac:PlannedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:45:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:PlannedDepartureTransportEvent>
        <cac:PlannedArrivalTransportEvent>
          <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:30:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
            <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
          </cac:Location>
        </cac:PlannedArrivalTransportEvent>
        <cac:PlannedWaypointTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:00:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:Name>Rail border station Urvania–Bayvarra</cbc:Name>
          </cac:Location>
        </cac:PlannedWaypointTransportEvent>
        <cac:EstimatedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:50:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:EstimatedDepartureTransportEvent>
        <cac:EstimatedArrivalTransportEvent>
          <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>10:40:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
            <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
          </cac:Location>
        </cac:EstimatedArrivalTransportEvent>
      </cac:MainCarriageShipmentStage>
      <cac:PreCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
        <cbc:Instructions>Two runs of the one tractor and chassis, one box a run: the first leaves the warehouse at 13:00, the second at 15:00.</cbc:Instructions>
        <cac:TransportMeans>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">37</cbc:TransportMeansTypeCode>
          <cac:RoadTransport>
            <cbc:LicensePlateID schemeID="urn:ubl-examples:world:XU:vehicle-register">UR 4160 RC</cbc:LicensePlateID>
          </cac:RoadTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:UnloadingPortLocation>
      </cac:PreCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRXU1044175</cbc:ID>
          <cbc:ReferencedConsignmentID>7300043586</cbc:ReferencedConsignmentID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:ProviderTypeCode listID="urn:ubl-examples:world:codelist:EquipmentProviderTypeCode">CARRIER</cbc:ProviderTypeCode>
          <cbc:OwnerTypeCode listID="urn:ubl-examples:world:codelist:EquipmentOwnerTypeCode">CARRIER</cbc:OwnerTypeCode>
          <cbc:SizeTypeCode listID="ISO 6346">45G1</cbc:SizeTypeCode>
          <cbc:DispositionCode listID="urn:ubl-examples:world:codelist:EquipmentDispositionCode">LOADED</cbc:DispositionCode>
          <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:LoadTypeCode">FCL</cbc:FullnessIndicationCode>
          <cbc:Information>Return empty to the Ferrano hub within five days.</cbc:Information>
          <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
          <cbc:Characteristics>Steel, high cube, wooden floor.</cbc:Characteristics>
          <cbc:DamageRemarks>Small dent in the left side panel, noted at pick-up; no effect on the cargo.</cbc:DamageRemarks>
          <cbc:Description>40-foot high cube container</cbc:Description>
          <cbc:SpecialTransportRequirements>Load with the doors to the rear of the wagon.</cbc:SpecialTransportRequirements>
          <cbc:GrossWeightMeasure unitCode="KGM">9088.8</cbc:GrossWeightMeasure>
          <cbc:GrossVolumeMeasure unitCode="MTQ">76.3</cbc:GrossVolumeMeasure>
          <cbc:TrackingDeviceCode listID="urn:ubl-examples:world:codelist:TrackingDeviceCode">GPS</cbc:TrackingDeviceCode>
          <cbc:PowerIndicator>false</cbc:PowerIndicator>
          <cbc:TraceID>TRK-FRXU1044175</cbc:TraceID>
          <cbc:StowagePositionID>31 46 4521 042-3 / A</cbc:StowagePositionID>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">12192</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:TransportEquipmentSeal>
            <cbc:ID>XU-VI-30411</cbc:ID>
            <cbc:SealIssuerTypeCode listID="urn:ubl-examples:world:codelist:SealIssuerTypeCode">SHIPPER</cbc:SealIssuerTypeCode>
            <cbc:Condition>Intact</cbc:Condition>
            <cbc:SealStatusCode listID="urn:ubl-examples:world:codelist:SealStatusCode">APPLIED</cbc:SealStatusCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
          <cac:ProviderParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Rail Cargo</cbc:Name>
            </cac:PartyName>
          </cac:ProviderParty>
          <cac:LoadingProofParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Castrano Logistics</cbc:Name>
            </cac:PartyName>
          </cac:LoadingProofParty>
          <cac:OwnerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Rail Cargo</cbc:Name>
            </cac:PartyName>
          </cac:OwnerParty>
          <cac:LoadingLocation>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:LoadingLocation>
          <cac:UnloadingLocation>
            <cbc:ID schemeID="UN/LOCODE">XBMRW</cbc:ID>
            <cbc:Name>Marrowdale</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:UnloadingLocation>
          <cac:PositioningTransportEvent>
            <cbc:OccurrenceDate>2026-04-10</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>08:00:00-01:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:PositioningTransportEvent>
          <cac:DeliveryTransportEvent>
            <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>11:00:00-01:00</cbc:OccurrenceTime>
            <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
            <cac:Location>
              <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
              <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
            </cac:Location>
          </cac:DeliveryTransportEvent>
          <cac:PickupTransportEvent>
            <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>13:00:00-01:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:PickupTransportEvent>
          <cac:HandlingTransportEvent>
            <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>14:00:00-01:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Ferrano Intermodal Hub, stack C</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:HandlingTransportEvent>
          <cac:LoadingTransportEvent>
            <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>05:40:00-01:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:LoadingTransportEvent>
          <cac:ApplicableTransportMeans>
            <cac:RailTransport>
              <cbc:TrainID>FRC 4417</cbc:TrainID>
              <cbc:RailCarID schemeID="urn:ubl-examples:world:XU:rail-vehicle-register">31 46 4521 042-3</cbc:RailCarID>
            </cac:RailTransport>
          </cac:ApplicableTransportMeans>
          <cac:HaulageTradingTerms>
            <cbc:Information>Carrier haulage: the rail carrier brings the box to the warehouse and back.</cbc:Information>
            <cbc:Reference>FRC-HT-2026</cbc:Reference>
          </cac:HaulageTradingTerms>
          <cac:FreightAllowanceCharge>
            <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Rail freight per container</cbc:AllowanceChargeReason>
            <cbc:Amount currencyID="XUF">54600</cbc:Amount>
          </cac:FreightAllowanceCharge>
          <cac:Delivery>
            <cbc:LatestDeliveryDate>2026-04-16</cbc:LatestDeliveryDate>
            <cac:DeliveryLocation>
              <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
              <cbc:Name>Rail siding of Lumeway Distribution, Marrowdale</cbc:Name>
            </cac:DeliveryLocation>
          </cac:Delivery>
          <cac:Pickup>
            <cbc:ActualPickupDate>2026-04-13</cbc:ActualPickupDate>
            <cbc:ActualPickupTime>13:00:00-01:00</cbc:ActualPickupTime>
            <cac:PickupLocation>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
            </cac:PickupLocation>
          </cac:Pickup>
          <cac:Despatch>
            <cbc:EstimatedDespatchDate>2026-04-14</cbc:EstimatedDespatchDate>
            <cbc:EstimatedDespatchTime>06:50:00-01:00</cbc:EstimatedDespatchTime>
          </cac:Despatch>
        </cac:TransportEquipment>
        <cac:CustomsDeclaration>
          <cbc:ID>7800004369</cbc:ID>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Valdara Industries</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:CustomsDeclaration>
        <cac:EnergyConsumptionAllocation>
          <cbc:EnergySourceTypeCode listID="urn:ubl-examples:world:codelist:EnergySourceCode">ELECTRICITY</cbc:EnergySourceTypeCode>
          <cbc:AllocatedEnergyMeasure unitCode="KWH">610</cbc:AllocatedEnergyMeasure>
        </cac:EnergyConsumptionAllocation>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRXU1044180</cbc:ID>
          <cbc:ReferencedConsignmentID>7300043586</cbc:ReferencedConsignmentID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:ProviderTypeCode listID="urn:ubl-examples:world:codelist:EquipmentProviderTypeCode">CARRIER</cbc:ProviderTypeCode>
          <cbc:OwnerTypeCode listID="urn:ubl-examples:world:codelist:EquipmentOwnerTypeCode">CARRIER</cbc:OwnerTypeCode>
          <cbc:SizeTypeCode listID="ISO 6346">45G1</cbc:SizeTypeCode>
          <cbc:DispositionCode listID="urn:ubl-examples:world:codelist:EquipmentDispositionCode">LOADED</cbc:DispositionCode>
          <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:LoadTypeCode">FCL</cbc:FullnessIndicationCode>
          <cbc:Information>Return empty to the Ferrano hub within five days.</cbc:Information>
          <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
          <cbc:Characteristics>Steel, high cube, wooden floor.</cbc:Characteristics>
          <cbc:Description>40-foot high cube container</cbc:Description>
          <cbc:SpecialTransportRequirements>Load with the doors to the rear of the wagon.</cbc:SpecialTransportRequirements>
          <cbc:GrossWeightMeasure unitCode="KGM">9088.8</cbc:GrossWeightMeasure>
          <cbc:GrossVolumeMeasure unitCode="MTQ">76.3</cbc:GrossVolumeMeasure>
          <cbc:TrackingDeviceCode listID="urn:ubl-examples:world:codelist:TrackingDeviceCode">GPS</cbc:TrackingDeviceCode>
          <cbc:PowerIndicator>false</cbc:PowerIndicator>
          <cbc:TraceID>TRK-FRXU1044180</cbc:TraceID>
          <cbc:StowagePositionID>31 46 4521 043-1 / A</cbc:StowagePositionID>
          <cac:MeasurementDimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">12192</cbc:Measure>
          </cac:MeasurementDimension>
          <cac:TransportEquipmentSeal>
            <cbc:ID>XU-VI-30412</cbc:ID>
            <cbc:SealIssuerTypeCode listID="urn:ubl-examples:world:codelist:SealIssuerTypeCode">SHIPPER</cbc:SealIssuerTypeCode>
            <cbc:Condition>Intact</cbc:Condition>
            <cbc:SealStatusCode listID="urn:ubl-examples:world:codelist:SealStatusCode">APPLIED</cbc:SealStatusCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
          <cac:ProviderParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Rail Cargo</cbc:Name>
            </cac:PartyName>
          </cac:ProviderParty>
          <cac:LoadingProofParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Castrano Logistics</cbc:Name>
            </cac:PartyName>
          </cac:LoadingProofParty>
          <cac:OwnerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Rail Cargo</cbc:Name>
            </cac:PartyName>
          </cac:OwnerParty>
          <cac:LoadingLocation>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:LoadingLocation>
          <cac:UnloadingLocation>
            <cbc:ID schemeID="UN/LOCODE">XBMRW</cbc:ID>
            <cbc:Name>Marrowdale</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:UnloadingLocation>
          <cac:PositioningTransportEvent>
            <cbc:OccurrenceDate>2026-04-10</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>10:00:00-01:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:PositioningTransportEvent>
          <cac:DeliveryTransportEvent>
            <cbc:OccurrenceDate>2026-04-15</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>11:00:00-01:00</cbc:OccurrenceTime>
            <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
            <cac:Location>
              <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
              <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
            </cac:Location>
          </cac:DeliveryTransportEvent>
          <cac:PickupTransportEvent>
            <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>15:00:00-01:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:PickupTransportEvent>
          <cac:HandlingTransportEvent>
            <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>16:00:00-01:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Ferrano Intermodal Hub, stack C</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:HandlingTransportEvent>
          <cac:LoadingTransportEvent>
            <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>05:55:00-01:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:LoadingTransportEvent>
          <cac:ApplicableTransportMeans>
            <cac:RailTransport>
              <cbc:TrainID>FRC 4417</cbc:TrainID>
              <cbc:RailCarID schemeID="urn:ubl-examples:world:XU:rail-vehicle-register">31 46 4521 043-1</cbc:RailCarID>
            </cac:RailTransport>
          </cac:ApplicableTransportMeans>
          <cac:HaulageTradingTerms>
            <cbc:Information>Carrier haulage: the rail carrier brings the box to the warehouse and back.</cbc:Information>
            <cbc:Reference>FRC-HT-2026</cbc:Reference>
          </cac:HaulageTradingTerms>
          <cac:FreightAllowanceCharge>
            <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
            <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
            <cbc:AllowanceChargeReason>Rail freight per container</cbc:AllowanceChargeReason>
            <cbc:Amount currencyID="XUF">54600</cbc:Amount>
          </cac:FreightAllowanceCharge>
          <cac:Delivery>
            <cbc:LatestDeliveryDate>2026-04-16</cbc:LatestDeliveryDate>
            <cac:DeliveryLocation>
              <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
              <cbc:Name>Rail siding of Lumeway Distribution, Marrowdale</cbc:Name>
            </cac:DeliveryLocation>
          </cac:Delivery>
          <cac:Pickup>
            <cbc:ActualPickupDate>2026-04-13</cbc:ActualPickupDate>
            <cbc:ActualPickupTime>15:00:00-01:00</cbc:ActualPickupTime>
            <cac:PickupLocation>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
            </cac:PickupLocation>
          </cac:Pickup>
          <cac:Despatch>
            <cbc:EstimatedDespatchDate>2026-04-14</cbc:EstimatedDespatchDate>
            <cbc:EstimatedDespatchTime>06:50:00-01:00</cbc:EstimatedDespatchTime>
          </cac:Despatch>
        </cac:TransportEquipment>
        <cac:CustomsDeclaration>
          <cbc:ID>7800004369</cbc:ID>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Valdara Industries</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:CustomsDeclaration>
        <cac:EnergyConsumptionAllocation>
          <cbc:EnergySourceTypeCode listID="urn:ubl-examples:world:codelist:EnergySourceCode">ELECTRICITY</cbc:EnergySourceTypeCode>
          <cbc:AllocatedEnergyMeasure unitCode="KWH">610</cbc:AllocatedEnergyMeasure>
        </cac:EnergyConsumptionAllocation>
      </cac:TransportHandlingUnit>
      <cac:EnvironmentalEmission>
        <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
        <cbc:ValueMeasure unitCode="KGM">410</cbc:ValueMeasure>
        <cac:EmissionCalculationMethod>
          <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
          <cac:MeasurementFromLocation>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          </cac:MeasurementFromLocation>
          <cac:MeasurementToLocation>
            <cbc:ID schemeID="UN/LOCODE">XBMRW</cbc:ID>
            <cbc:Name>Marrowdale</cbc:Name>
          </cac:MeasurementToLocation>
          <cac:EmissionCalculationLocation>
            <cbc:Name>Ferrano Rail Cargo, energy office</cbc:Name>
          </cac:EmissionCalculationLocation>
        </cac:EmissionCalculationMethod>
      </cac:EnvironmentalEmission>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">5188.8</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Park bench Serra 180</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
        </cac:CommodityClassification>
        <cac:ItemInstance>
          <cac:LotIdentification>
            <cbc:LotNumberID>VI-LOT-260409</cbc:LotNumberID>
          </cac:LotIdentification>
        </cac:ItemInstance>
      </cac:Item>
      <cac:GoodsItemContainer>
        <cbc:ID>1</cbc:ID>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRXU1044175</cbc:ID>
        </cac:TransportEquipment>
      </cac:GoodsItemContainer>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">5188.8</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">96</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Park bench Serra 180</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
        </cac:CommodityClassification>
        <cac:ItemInstance>
          <cac:LotIdentification>
            <cbc:LotNumberID>VI-LOT-260410</cbc:LotNumberID>
          </cac:LotIdentification>
        </cac:ItemInstance>
      </cac:Item>
      <cac:GoodsItemContainer>
        <cbc:ID>1</cbc:ID>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRXU1044180</cbc:ID>
        </cac:TransportEquipment>
      </cac:GoodsItemContainer>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>9500055446</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">TransportExecutionPlan</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALHANDED</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALWITHGOODS</cbc:DistributionTypeCode>
    <cbc:DistributionType languageID="qau">Rikzhek, vek drek valnir: drek trelgir rikzhek</cbc:DistributionType>
    <cbc:DistributionType languageID="en-XU">Original, with the goods: the consignee's original</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>FRC-SIG-7200092547</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Rail Cargo</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
