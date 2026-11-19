# Waybill: Ferrano Rail Cargo to Valdara Industries

*Example 8 of the flow "Containers by rail under transit (Urvania → Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The rail consignment note goes to the transport user, now the seller.

[The XML file](08-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **RAIL-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FRC-WB-26-0334**  
  The consignment note number.
- `CarrierAssignedID` = **FRC-CIM-26-0325**  
  The carrier's own number for the carriage.
- `UUID` = **2af02244-330b-5e9f-85c5-1ad7dcce9c43**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-04-14**  
  Issued when the carrier takes over the containers.
- `IssueTime` = **13:10:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `Name` = **Rail consignment note under the CIM uniform rules**  
  The kind of transport document.
- `Description` = **Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.**  
  The carriage in words.
- `Note` = **Gurbul mizstan: drek starzhek, ginrul nartran zaskek drek sundraz hangaz nartran drek valnir; drek trelgir, vek drek valnir; drek vuznek, zhiztrek man drek sundraz.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed (worklist C33).
- `Note` = **Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed (worklist C33).
- `WaybillTypeCode` = **CIM** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: CIM = Rail consignment note (CIM).
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

- `PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; identity of Ferrano Rail Cargo (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4170201115930918** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Rumir Hekrul Zhuzkek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/StreetName` = **Viale della Stazione** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/PostalZone` = **4310**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Ferrano Rail Cargo (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Freight desk**  
  The party's main desk, which handles this document; identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/JobTitle` = **Freight planner**  
  The job of the person who answers at the desk; identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/Telephone` = **+999 1 0413 67100**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/ElectronicMail` = **freight@ferranorail.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Rail Cargo (world/parties.json).
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; identity of Ferrano Rail Cargo (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160200467394686** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Valdara Industries (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Nulban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Valdara Industries (world/parties.json).
- `PostalAddress/StreetName` = **Via delle Officine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **logistics@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

- `ID` = **VI-SH-26-0332**  
  The shipment as the despatching party numbered it.
- `GrossWeightMeasure` = **15768** (unitCode `KGM`)  
  The gross weights of the transport equipment with the goods in it (7884 + 7884 kg): a shipment's gross weight includes the equipment (worklist C15).
- `Consignment/ID` = **VI-CS-26-0327**  
  The manufacturer's consignment number.
- `Consignment/ContractedCarrierAssignedID` = **FRC-CON-2026-005/88**  
  The call-off under the framework contract.
- `Consignment/SummaryDescription` = **192 park benches in two 40-foot containers.**  
  The goods in a few words.
- `Consignment/GrossWeightMeasure` = **7968** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight of the two containers' cargo.
- `Consignment/ContainerizedIndicator` = **true**  
  Two full containers.
- `Consignment/TotalTransportHandlingUnitQuantity` = **2** (unitCode `EA`)  
  Two containers.
- `Consignment/LoadingSequenceID` = **7**  
  The consignment's turn in the loading of the train.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 2 7121 955 964**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **goodsin@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `Consignment/TransportContract/ID` = **FRC-CON-2026-005**  
  The framework contract for container slots.
- `Consignment/TransportContract/IssueDate` = **2026-01-05**  
  Signed at the start of the year.
- `Consignment/TransportContract/ContractType` = **Framework contract for container slots**  
  What it is.
- `Consignment/PrepaidPaymentTerms/Note` = **Freight prepaid by the consignor under DAP.**  
  The seller pays the carriage.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  The main carriage, by rail.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **2** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 2: rail transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 2 = Rail transport.
- `Consignment/MainCarriageShipmentStage/LoadingSequenceID` = **7**  
  The order the boxes go on the train: these two are the seventh lift.
- `Consignment/MainCarriageShipmentStage/SuccessiveSequenceID` = **1**  
  The first and only rail stage.
- `Consignment/MainCarriageShipmentStage/Instructions` = **Shunt to the Lumeway siding on arrival in Marrowdale.**  
  What the railway must do.
- `Consignment/MainCarriageShipmentStage/DemurrageInstructions` = **Free time five days at the siding, then demurrage per container day.**  
  What waiting costs.
- `Consignment/MainCarriageShipmentStage/CrewQuantity` = **2** (unitCode `IE`)  
  Two persons: a driver and a train manager.
- `Consignment/MainCarriageShipmentStage/PassengerQuantity` = **0** (unitCode `IE`)  
  No persons: a freight train carries no passengers.
- `Consignment/MainCarriageShipmentStage/TransportMeans/JourneyID` = **CT 4471**  
  The number of the container train in the hub's timetable.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **WB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: WB = Westbound.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **2302** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: container train Ferrano–Marrowdale; the fleet of Ferrano Rail Cargo (world/parties.json). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 2302 = Train, container.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RailTransport/TrainID` = **FRC 4417**  
  The train number; the fleet of Ferrano Rail Cargo (world/parties.json).
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The timetable departure from the hub.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/OccurrenceTime` = **06:45:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `Consignment/MainCarriageShipmentStage/PlannedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceDate` = **2026-04-15**  
  The timetable arrival at the siding in Marrowdale: the train reaches Marrowdale yard about 15:30 the day before, 173 km from the hub, and the next morning's shunting trip places the boxes on Lumeway's siding.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/OccurrenceTime` = **10:30:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples); world/parties.json.
- `Consignment/MainCarriageShipmentStage/PlannedArrivalTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `Consignment/MainCarriageShipmentStage/PlannedWaypointTransportEvent/OccurrenceDate` = **2026-04-14**  
  Planned departure from the border station, 63 km from the hub: the train stops there from about 08:10 for the crew change, the brake test and the customs' check of the seals, and leaves on its timetabled path into Bayvarra.
- `Consignment/MainCarriageShipmentStage/PlannedWaypointTransportEvent/OccurrenceTime` = **13:00:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/PlannedWaypointTransportEvent/Location/Name` = **Rail border station Urvania–Bayvarra**  
  Where the train crosses the border.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The train left the hub.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/OccurrenceTime` = **06:52:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE; worklist C23).
- `Consignment/MainCarriageShipmentStage/ActualDepartureTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  Where.
- `Consignment/MainCarriageShipmentStage/ActualWaypointTransportEvent/OccurrenceDate` = **2026-04-14**  
  The train passed the border station.
- `Consignment/MainCarriageShipmentStage/ActualWaypointTransportEvent/OccurrenceTime` = **13:20:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/ActualWaypointTransportEvent/Location/Name` = **Rail border station Urvania–Bayvarra**  
  Where the train crosses the border.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceDate` = **2026-04-14**  
  The departure as expected that morning.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/OccurrenceTime` = **06:50:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `Consignment/MainCarriageShipmentStage/EstimatedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/OccurrenceDate` = **2026-04-15**  
  The arrival as expected.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/OccurrenceTime` = **10:40:00**  
  The local time.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples); world/parties.json.
- `Consignment/MainCarriageShipmentStage/EstimatedArrivalTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **FRXU1044175** (schemeID `ISO6346`)  
  The container's number: owner code, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReferencedConsignmentID` = **VI-CS-26-0327**  
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
- `Consignment/TransportHandlingUnit/TransportEquipment/LegalStatusIndicator` = **false**  
  Not under a customs container convention; the goods travel under transit.
- `Consignment/TransportHandlingUnit/TransportEquipment/Characteristics` = **Steel, high cube, wooden floor.**  
  What kind of box it is.
- `Consignment/TransportHandlingUnit/TransportEquipment/DamageRemarks` = **Small dent in the left side panel, noted at pick-up; no effect on the cargo.**  
  Damage noted at the hub, so it is not blamed on this carriage.
- `Consignment/TransportHandlingUnit/TransportEquipment/Description` = **40-foot high cube container**  
  The container in words.
- `Consignment/TransportHandlingUnit/TransportEquipment/SpecialTransportRequirements` = **Load with the doors to the rear of the wagon.**  
  How it rides.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **7884** (unitCode `KGM`)  
  Half the benches and the container's own 3,900 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossVolumeMeasure` = **76.3** (unitCode `MTQ`)  
  The inside volume of a 40-foot high cube.
- `Consignment/TransportHandlingUnit/TransportEquipment/TrackingDeviceCode` = **GPS** (listID `urn:ubl-examples:world:codelist:TrackingDeviceCode`)  
  The box carries a satellite tracker. The code is from the Trade Accord's tracking device list: GPS = Satellite tracker.
- `Consignment/TransportHandlingUnit/TransportEquipment/PowerIndicator` = **false**  
  It needs no power: not a reefer.
- `Consignment/TransportHandlingUnit/TransportEquipment/TraceID` = **TRK-FRXU1044175**  
  The tracker's number.
- `Consignment/TransportHandlingUnit/TransportEquipment/StowagePositionID` = **31 46 4521 042-3 / A**  
  The wagon and the slot on it the box rides in.
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
- `Consignment/TransportHandlingUnit/TransportEquipment/OperatingParty/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportHandlingUnit/TransportEquipment/OperatingParty/PartyName/Name` = **Ferrano Intermodal Hub**  
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
- `Consignment/TransportHandlingUnit/TransportEquipment/StorageLocation/Name` = **Ferrano Intermodal Hub, stack C**  
  Where the box waited for the train.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/OccurrenceDate` = **2026-04-12**  
  The empty box was delivered to the warehouse for packing.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/OccurrenceTime` = **08:00:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/PositioningTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/OccurrenceDate` = **2026-04-15**  
  Planned arrival at the siding.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/OccurrenceTime` = **11:00:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/Location/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples); world/parties.json.
- `Consignment/TransportHandlingUnit/TransportEquipment/DeliveryTransportEvent/Location/Name` = **Lumeway rail siding, Marrowdale**  
  Where the boxes are placed for unloading.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/OccurrenceDate` = **2026-04-13**  
  Collected packed from the warehouse.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/OccurrenceTime` = **15:00:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/Name` = **Castrano Logistics warehouse, Conciaro**  
  At the 3PL's warehouse in Conciaro, where the boxes are packed.
- `Consignment/TransportHandlingUnit/TransportEquipment/PickupTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/OccurrenceDate` = **2026-04-13**  
  Stacked at the hub overnight.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/OccurrenceTime` = **18:30:00**  
  The local time.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/Name` = **Ferrano Intermodal Hub**  
  At the intermodal hub, where the boxes go on the train.
- `Consignment/TransportHandlingUnit/TransportEquipment/HandlingTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/OccurrenceDate` = **2026-04-14**  
  Lifted onto the wagon.
- `Consignment/TransportHandlingUnit/TransportEquipment/LoadingTransportEvent/OccurrenceTime` = **05:40:00**  
  The local time.
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
  The price of one container slot (world/items.json).
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/LatestDeliveryDate` = **2026-04-16**  
  At the latest.
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/DeliveryLocation/ID` = **9520610900015** (schemeID `GS1 GLN`)  
  The Global Location Number of the place, rail siding of the distribution centre, marrowdale: Lumeway Distribution identifies its places the GS1 way, under its company prefix (952, reserved for examples); world/parties.json.
- `Consignment/TransportHandlingUnit/TransportEquipment/Delivery/DeliveryLocation/Name` = **Rail siding of Lumeway Distribution, Marrowdale**  
  Where.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/ActualPickupDate` = **2026-04-13**  
  Collected.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/ActualPickupTime` = **15:00:00**  
  At three.
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/PickupLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE; worklist C23).
- `Consignment/TransportHandlingUnit/TransportEquipment/Pickup/PickupLocation/Name` = **Castrano Logistics warehouse, Conciaro**  
  Where.
- `Consignment/TransportHandlingUnit/TransportEquipment/Despatch/ActualDespatchDate` = **2026-04-14**  
  The train left the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/Despatch/ActualDespatchTime` = **06:50:00**  
  Ten to seven.
- `Consignment/TransportHandlingUnit/TransportEquipment/ShipmentDocumentReference/ID` = **FRC-WB-26-0334**  
  The rail consignment note.
- `Consignment/TransportHandlingUnit/TransportEquipment/ShipmentDocumentReference/DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: FRC-WB-26-0334 is the example rail/08, a Waybill; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Waybill.
- `Consignment/TransportHandlingUnit/TransportEquipment/ContainedInTransportEquipment/ID` = **31 46 4521 042-3** (schemeID `urn:ubl-examples:world:XU:rail-vehicle-register`)  
  The container wagon the box rides on. The schemeID names the scheme it is from: the national vehicle register of Urvania (railway vehicles) (the UIC 12-digit wagon number: interoperability and gauge (2 digits), country 46, type (4), serial (3) and the check digit).
- `Consignment/TransportHandlingUnit/TransportEquipment/ContainedInTransportEquipment/TransportEquipmentTypeCode` = **RR** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code RR: rail car. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: RR = Rail car.
- `Consignment/TransportHandlingUnit/CustomsDeclaration/ID` = **VI-TD-26-0331**  
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
- `Consignment/TransportHandlingUnit/TransportEquipment/ReferencedConsignmentID` = **VI-CS-26-0327**  
  The consignment the container carries.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container. The code is from UBL's default Transport equipment type (UN/EDIFACT 8053) list: CN = Container.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45G1** (listID `ISO 6346`)  
  ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose. The code is from the world's copy of ISO 6346 container size and type code: 45G1 = 40 ft, 9 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL** (listID `urn:ubl-examples:world:codelist:LoadTypeCode`)  
  A full container load for one consignee. The code is from the Trade Accord's load type list: FCL = Full container load.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **7884** (unitCode `KGM`)  
  Half the benches and the container's own 3,900 kg.
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
- `Consignment/TransportHandlingUnit/CustomsDeclaration/ID` = **VI-TD-26-0331**  
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
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE; worklist C23).
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementFromLocation/Name` = **Ferrano Intermodal Hub**  
  From.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementToLocation/ID` = **XBMRW** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE; worklist C23).
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/MeasurementToLocation/Name` = **Marrowdale**  
  To.
- `Consignment/EnvironmentalEmission/EmissionCalculationMethod/EmissionCalculationLocation/Name` = **Ferrano Rail Cargo, energy office**  
  Where the figure was calculated.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What is carried, in words.
- `GoodsItem/GrossWeightMeasure` = **7968** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **192** (unitCode `EA`)  
  How much is carried.
- `GoodsItem/Item/Name` = **Park bench Serra 180**  
  The goods.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  Its Harmonized System subheading, which carriers use to describe the cargo. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.

### Document Reference

Inside `DocumentReference`:

- `ID` = **FRC-TEP-26-0328**  
  The transport plan under which the carriage is performed.
- `DocumentTypeCode` = **TransportExecutionPlan** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: FRC-TEP-26-0328 is the example rail/03, a TransportExecutionPlan; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: TransportExecutionPlan = Transport Execution Plan.

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
- `Party/PartyIdentification/ID` = **XU-R-105096** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Ferrano Intermodal Hub**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FRC-SIG-FRC-WB-26-0334**  
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
  <cbc:ProfileExecutionID>RAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FRC-WB-26-0334</cbc:ID>
  <cbc:CarrierAssignedID>FRC-CIM-26-0325</cbc:CarrierAssignedID>
  <cbc:UUID>2af02244-330b-5e9f-85c5-1ad7dcce9c43</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-04-14</cbc:IssueDate>
  <cbc:IssueTime>13:10:00-01:00</cbc:IssueTime>
  <cbc:Name>Rail consignment note under the CIM uniform rules</cbc:Name>
  <cbc:Description>Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.</cbc:Description>
  <cbc:Note languageID="qau">Gurbul mizstan: drek starzhek, ginrul nartran zaskek drek sundraz hangaz nartran drek valnir; drek trelgir, vek drek valnir; drek vuznek, zhiztrek man drek sundraz.</cbc:Note>
  <cbc:Note languageID="en-XU">Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.</cbc:Note>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">CIM</cbc:WaybillTypeCode>
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
    <cbc:ID>VI-SH-26-0332</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">15768</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>VI-CS-26-0327</cbc:ID>
      <cbc:ContractedCarrierAssignedID>FRC-CON-2026-005/88</cbc:ContractedCarrierAssignedID>
      <cbc:SummaryDescription>192 park benches in two 40-foot containers.</cbc:SummaryDescription>
      <cbc:GrossWeightMeasure unitCode="KGM">7968</cbc:GrossWeightMeasure>
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
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">2</cbc:TransportModeCode>
        <cbc:LoadingSequenceID>7</cbc:LoadingSequenceID>
        <cbc:SuccessiveSequenceID>1</cbc:SuccessiveSequenceID>
        <cbc:Instructions>Shunt to the Lumeway siding on arrival in Marrowdale.</cbc:Instructions>
        <cbc:DemurrageInstructions>Free time five days at the siding, then demurrage per container day.</cbc:DemurrageInstructions>
        <cbc:CrewQuantity unitCode="IE">2</cbc:CrewQuantity>
        <cbc:PassengerQuantity unitCode="IE">0</cbc:PassengerQuantity>
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
          <cbc:OccurrenceTime>06:45:00</cbc:OccurrenceTime>
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
          <cbc:OccurrenceTime>10:30:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
            <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
          </cac:Location>
        </cac:PlannedArrivalTransportEvent>
        <cac:PlannedWaypointTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:00:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:Name>Rail border station Urvania–Bayvarra</cbc:Name>
          </cac:Location>
        </cac:PlannedWaypointTransportEvent>
        <cac:ActualDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:52:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
          </cac:Location>
        </cac:ActualDepartureTransportEvent>
        <cac:ActualWaypointTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:20:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:Name>Rail border station Urvania–Bayvarra</cbc:Name>
          </cac:Location>
        </cac:ActualWaypointTransportEvent>
        <cac:EstimatedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>06:50:00</cbc:OccurrenceTime>
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
          <cbc:OccurrenceTime>10:40:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
            <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
          </cac:Location>
        </cac:EstimatedArrivalTransportEvent>
      </cac:MainCarriageShipmentStage>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRXU1044175</cbc:ID>
          <cbc:ReferencedConsignmentID>VI-CS-26-0327</cbc:ReferencedConsignmentID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:ProviderTypeCode listID="urn:ubl-examples:world:codelist:EquipmentProviderTypeCode">CARRIER</cbc:ProviderTypeCode>
          <cbc:OwnerTypeCode listID="urn:ubl-examples:world:codelist:EquipmentOwnerTypeCode">CARRIER</cbc:OwnerTypeCode>
          <cbc:SizeTypeCode listID="ISO 6346">45G1</cbc:SizeTypeCode>
          <cbc:DispositionCode listID="urn:ubl-examples:world:codelist:EquipmentDispositionCode">LOADED</cbc:DispositionCode>
          <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:LoadTypeCode">FCL</cbc:FullnessIndicationCode>
          <cbc:Information>Return empty to the Ferrano hub within five days.</cbc:Information>
          <cbc:ReturnabilityIndicator>true</cbc:ReturnabilityIndicator>
          <cbc:LegalStatusIndicator>false</cbc:LegalStatusIndicator>
          <cbc:Characteristics>Steel, high cube, wooden floor.</cbc:Characteristics>
          <cbc:DamageRemarks>Small dent in the left side panel, noted at pick-up; no effect on the cargo.</cbc:DamageRemarks>
          <cbc:Description>40-foot high cube container</cbc:Description>
          <cbc:SpecialTransportRequirements>Load with the doors to the rear of the wagon.</cbc:SpecialTransportRequirements>
          <cbc:GrossWeightMeasure unitCode="KGM">7884</cbc:GrossWeightMeasure>
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
          <cac:OperatingParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
            </cac:PartyName>
          </cac:OperatingParty>
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
          <cac:StorageLocation>
            <cbc:Name>Ferrano Intermodal Hub, stack C</cbc:Name>
          </cac:StorageLocation>
          <cac:PositioningTransportEvent>
            <cbc:OccurrenceDate>2026-04-12</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>08:00:00</cbc:OccurrenceTime>
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
            <cbc:OccurrenceTime>11:00:00</cbc:OccurrenceTime>
            <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
            <cac:Location>
              <cbc:ID schemeID="GS1 GLN">9520610900015</cbc:ID>
              <cbc:Name>Lumeway rail siding, Marrowdale</cbc:Name>
            </cac:Location>
          </cac:DeliveryTransportEvent>
          <cac:PickupTransportEvent>
            <cbc:OccurrenceDate>2026-04-13</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>15:00:00</cbc:OccurrenceTime>
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
            <cbc:OccurrenceTime>18:30:00</cbc:OccurrenceTime>
            <cac:Location>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
              <cac:Address>
                <cac:Country>
                  <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:Address>
            </cac:Location>
          </cac:HandlingTransportEvent>
          <cac:LoadingTransportEvent>
            <cbc:OccurrenceDate>2026-04-14</cbc:OccurrenceDate>
            <cbc:OccurrenceTime>05:40:00</cbc:OccurrenceTime>
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
            <cbc:ActualPickupTime>15:00:00</cbc:ActualPickupTime>
            <cac:PickupLocation>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Castrano Logistics warehouse, Conciaro</cbc:Name>
            </cac:PickupLocation>
          </cac:Pickup>
          <cac:Despatch>
            <cbc:ActualDespatchDate>2026-04-14</cbc:ActualDespatchDate>
            <cbc:ActualDespatchTime>06:50:00</cbc:ActualDespatchTime>
          </cac:Despatch>
          <cac:ShipmentDocumentReference>
            <cbc:ID>FRC-WB-26-0334</cbc:ID>
            <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
          </cac:ShipmentDocumentReference>
          <cac:ContainedInTransportEquipment>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:rail-vehicle-register">31 46 4521 042-3</cbc:ID>
            <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">RR</cbc:TransportEquipmentTypeCode>
          </cac:ContainedInTransportEquipment>
        </cac:TransportEquipment>
        <cac:CustomsDeclaration>
          <cbc:ID>VI-TD-26-0331</cbc:ID>
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
          <cbc:ReferencedConsignmentID>VI-CS-26-0327</cbc:ReferencedConsignmentID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:SizeTypeCode listID="ISO 6346">45G1</cbc:SizeTypeCode>
          <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:LoadTypeCode">FCL</cbc:FullnessIndicationCode>
          <cbc:GrossWeightMeasure unitCode="KGM">7884</cbc:GrossWeightMeasure>
          <cac:TransportEquipmentSeal>
            <cbc:ID>XU-VI-30412</cbc:ID>
            <cbc:SealIssuerTypeCode listID="urn:ubl-examples:world:codelist:SealIssuerTypeCode">SHIPPER</cbc:SealIssuerTypeCode>
            <cbc:Condition>Intact</cbc:Condition>
            <cbc:SealStatusCode listID="urn:ubl-examples:world:codelist:SealStatusCode">APPLIED</cbc:SealStatusCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
        </cac:TransportEquipment>
        <cac:CustomsDeclaration>
          <cbc:ID>VI-TD-26-0331</cbc:ID>
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
      <cbc:GrossWeightMeasure unitCode="KGM">7968</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">192</cbc:Quantity>
      <cac:Item>
        <cbc:Name>Park bench Serra 180</cbc:Name>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>FRC-TEP-26-0328</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">TransportExecutionPlan</cbc:DocumentTypeCode>
  </cac:DocumentReference>
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
  <cac:DocumentDistribution>
    <cbc:ID>2</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALWITHGOODS</cbc:DistributionTypeCode>
    <cbc:DistributionType languageID="qau">Rikzhek, vek drek valnir: drek trelgir rikzhek</cbc:DistributionType>
    <cbc:DistributionType languageID="en-XU">Original, with the goods: the consignee's original</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105096</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Intermodal Hub</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>FRC-SIG-FRC-WB-26-0334</cbc:ID>
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
