# Waybill: Fiumella Barges to Rinova Recovery

*Example 6 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Waybill in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WAYBILL-SCHEMA)*

The inland waterway consignment note, issued to the shipper.

[The XML file](06-Waybill.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waybill:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waybill". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **26-0425**  
  The collaboration this document belongs to: the barge carriage Rinova books with Fiumella Barges. Rinova Recovery started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0181**  
  The consignment note number.
- `CarrierAssignedID` = **26-0023**  
  The carrier's own number for the carriage.
- `UUID` = **0a38e2bd-26a7-55f9-833d-9ab2e55cfd4a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `VersionID` = **1**  
  The original, not a corrected version.
- `StatusCode` = **ISSUED** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The note is issued and in force. The code is from the Trade Accord's record status list: ISSUED = Issued.
- `IssueDate` = **2026-04-20**  
  Issued when the barge is loaded.
- `IssueTime` = **15:26:00-01:00**  
  Issued a few minutes after the last thing of its day that it reports, cites or answers, in the sender's local time, with its offset from UTC.
- `Name` = **Inland waterway consignment note under the CMNI**  
  The kind of transport document.
- `Description` = **The barge from the quay next to the recovery plant down the river to the packaging maker.**  
  The carriage in words.
- `Note` = **Gurbul mizstan: drek starzhek, ginrul nartran zaskek drek sundraz hangaz nartran drek valnir; drek trelgir, vek drek valnir; drek vuznek, zhiztrek man drek sundraz.** (languageID `qau`)  
  The note in Urvanian, the sender's language: The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed.
- `Note` = **Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: The originals the convention prescribes, as the distribution below lists them; the carrier's own is not distributed.
- `WaybillTypeCode` = **CMNI** (listID `urn:ubl-examples:world:codelist:WaybillTypeCode`)  
  The convention the document follows. The code is from the Trade Accord's waybill type list: CMNI = Inland waterway waybill (CMNI).
- `ConsolidatedIndicator` = **false**  
  One consignment, not a consolidation.
- `OtherInstruction` = **Deliver against signature of the consignee.**  
  What the carrier must do at delivery.

### Issue Location

Inside `IssueLocation`:

- `ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Name` = **Quay of Rinova Recovery, Ferrano**  
  Where the carrier took over the goods and issued the note.
- `Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Fiumella Barges gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Fiumella Barges**  
  The trading name; as Fiumella Barges gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `PostalAddress/ID` = **4160204198475331** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Fiumella Barges gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Skikzek Han Nestan** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Fiumella Barges gives it.
- `PostalAddress/StreetName` = **Banchina del Fiume** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Fiumella Barges gives it.
- `PostalAddress/BuildingNumber` = **52**  
  Building number of the postal address. As Fiumella Barges gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Fiumella Barges gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Fiumella Barges gives it.
- `PostalAddress/PostalZone` = **4170**  
  Postal code in Urvania's format (4 digits). As Fiumella Barges gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Fiumella Barges gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Chartering desk**  
  The party's main desk, which handles this document; as Fiumella Barges gives it.
- `Contact/JobTitle` = **Chartering manager**  
  The job of the person who answers at the desk; as Fiumella Barges gives it.
- `Contact/Department` = **Operations**  
  The department the desk belongs to; as Fiumella Barges gives it.
- `Contact/Telephone` = **+999 1 041 672 6403**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Fiumella Barges gives it.
- `Contact/ElectronicMail` = **chartering@fiumella.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Fiumella Barges gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Fiumella Barges gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104959** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Fiumella Barges gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Rinova Recovery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:13362** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Rinova Recovery gives it.
- `AdditionalPartyIdentification/ID` = **XU-TR-104548** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Rinova Recovery gives it.
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; as Rinova Recovery gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `PostalAddress/ID` = **4160202983340277** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Rinova Recovery gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Han Zugaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Rinova Recovery gives it.
- `PostalAddress/StreetName` = **Via del Riciclo** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Rinova Recovery gives it.
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. As Rinova Recovery gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Rinova Recovery gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Rinova Recovery gives it.
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). As Rinova Recovery gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Rinova Recovery gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Transport planning**  
  The party's transport planning desk: the desk for its role in this document (it books or uses the transport); as Rinova Recovery gives it.
- `Contact/JobTitle` = **Logistics planner**  
  The job of the person who answers at the desk; as Rinova Recovery gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Rinova Recovery gives it.
- `Contact/Telephone` = **+999 1 041 697 6856**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Rinova Recovery gives it.
- `Contact/ElectronicMail` = **logistics@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Rinova Recovery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Rinova Recovery gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Rinova Recovery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Rinova Recovery**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Carrier Party

Inside `CarrierParty`:

- `PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Fiumella Barges**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **26-0452**  
  The shipment as the despatching party numbered it.
- `Consignment/ID` = **26-0426**  
  The seller's consignment number.
- `Consignment/CarrierAssignedID` = **FB4-26-031/2**  
  The barge operator's number: the second lot of the voyage.
- `Consignment/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight on board.
- `Consignment/TotalPackagesQuantity` = **120**  
  The 120 jumbo bags of a tonne each.
- `Consignment/ConsigneeParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Rivermouth Packaging gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **0990:15128** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-412740** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; as Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/PostalAddress/ID` = **LUM-ADR-411619** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. As Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. As Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). As Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Consignment/ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Rivermouth Packaging gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Consignment/ConsigneeParty/Contact/Name` = **Goods-in**  
  The party's goods-in desk: the desk for its role in this document (it receives the goods); as Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/Contact/JobTitle` = **Goods-in supervisor**  
  The job of the person who answers at the desk; as Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/Contact/Department` = **Warehouse**  
  The department the desk belongs to; as Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/Contact/Telephone` = **+999 2 38 7320 9007**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/Contact/ElectronicMail` = **goodsin@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Rivermouth Packaging gives it.
- `Consignment/ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Rivermouth Packaging gives it.
- `Consignment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The freight, a charge.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Consignment/FreightAllowanceCharge/AllowanceChargeReason` = **River freight**  
  What it is for.
- `Consignment/FreightAllowanceCharge/Amount` = **179400** (currencyID `XUF`)  
  120 tonnes at 1,495 ferra.
- `Consignment/FreightAllowanceCharge/PerUnitAmount` = **1495** (currencyID `XUF`)  
  The rate per tonne, times the 120 chargeable tonnes of the goods item.
- `Consignment/MainCarriageShipmentStage/ID` = **1**  
  Down the river, from the recovery plant's quay to the river quay in Lumeport.
- `Consignment/MainCarriageShipmentStage/TransportModeCode` = **8** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 8: inland water transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 8 = Inland water transport.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `Consignment/MainCarriageShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `Consignment/MainCarriageShipmentStage/TransportMeans/DirectionCode` = **DS** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: DS = Downstream.
- `Consignment/MainCarriageShipmentStage/TransportMeans/TransportMeansTypeCode` = **815** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: fiumella IV; the fleet of Fiumella Barges. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 815 = Freight barge.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XU-IW-08042** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Fiumella IV**  
  The vessel's name; the fleet of Fiumella Barges.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **QUBF4**  
  The radio call sign, in Urvania's call sign series QU: no ITU series starts with Q, so the sign belongs to no real station.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **297801042**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 297 of Urvania, which the ITU has not allocated to any real country, and the ship's six digits.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **1210** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **860** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **DRYBARGE** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel. The code is from the Trade Accord's ship configuration list: DRYBARGE = Dry cargo barge.
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Consignment/MainCarriageShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Ferrano**  
  The port the vessel is registered in.
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Consignment/MainCarriageShipmentStage/LoadingPortLocation/Name` = **Quay of Rinova Recovery, Ferrano**  
  Where the bags are loaded.
- `Consignment/MainCarriageShipmentStage/UnloadingPortLocation/Name` = **River quay, Lumeport**  
  The place named in the CPT terms.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/OccurrenceDate` = **2026-04-20**  
  Loading finished: 120 bags in the hold.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/OccurrenceTime` = **13:30:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/Location/Name` = **Quay of Rinova Recovery, Ferrano**  
  At the recovery plant's own quay on the river.
- `Consignment/MainCarriageShipmentStage/LoadingTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/ExportationTransportEvent/OccurrenceDate` = **2026-04-21**  
  The barge leaves Urvania at the river border, 105 km below the quay: sailing from the afternoon of loading and through the next day from first light.
- `Consignment/MainCarriageShipmentStage/ExportationTransportEvent/OccurrenceTime` = **13:45:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/ExportationTransportEvent/Location/Name` = **River border Urvania–Bayvarra**  
  Where the barge leaves Urvania.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceDate` = **2026-04-23**  
  Planned unloading at the Lumeport quay, with the consignee's morning shift: the barge arrives about 16:15 the day before and moors at the quay overnight.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/OccurrenceTime` = **08:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Consignment/MainCarriageShipmentStage/DischargeTransportEvent/Location/Name` = **River quay, Lumeport**  
  The quay named in the CPT terms, where the bags are unloaded.
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/OccurrenceDate` = **2026-04-20**  
  The barge operator takes over the bags at the quay.
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/OccurrenceTime` = **09:00:00-01:00**  
  The local time of Urvania, where it happens, with its offset from UTC.
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/Location/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/Location/Name` = **Quay of Rinova Recovery, Ferrano**  
  At the recovery plant's own quay on the river.
- `Consignment/MainCarriageShipmentStage/TakeoverTransportEvent/Location/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/MainCarriageShipmentStage/EstimatedTransitPeriod/DurationMeasure` = **3** (unitCode `DAY`)  
  Three days from takeover to discharge: about 250 km downstream, with no locks, sailing by day.
- `Consignment/MainCarriageShipmentStage/MasterPerson/FirstName` = **Tomaso**  
  The skipper of the barge.
- `Consignment/MainCarriageShipmentStage/MasterPerson/FamilyName` = **Riverra**  
  The family name.
- `Consignment/MainCarriageShipmentStage/MasterPerson/JobTitle` = **Skipper**  
  The person's position.
- `GoodsItem/ID` = **1**  
  The only goods item.
- `GoodsItem/SequenceNumberID` = **1**  
  Its place in the cargo list.
- `GoodsItem/Description` = **Recycled PE granulate**  
  What the goods are.
- `GoodsItem/DeclaredForCarriageValueAmount` = **9984000** (currencyID `XUF`)  
  Declared to the barge operator, which raises its liability to this value.
- `GoodsItem/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  With the bags.
- `GoodsItem/NetWeightMeasure` = **120000** (unitCode `KGM`)  
  The granulate alone.
- `GoodsItem/NetNetWeightMeasure` = **120000** (unitCode `KGM`)  
  No inner packaging: the same as the net weight.
- `GoodsItem/ChargeableWeightMeasure` = **120000** (unitCode `KGM`)  
  The freight is charged per tonne of granulate.
- `GoodsItem/GrossVolumeMeasure` = **204** (unitCode `MTQ`)  
  The 120 bags take 1.7 m³ each.
- `GoodsItem/NetVolumeMeasure` = **200** (unitCode `MTQ`)  
  The granulate as it lies in the bags, at a bulk density of about 0.6 tonne per m³; the bags' fabric and loops make up the rest of the gross volume.
- `GoodsItem/Quantity` = **120** (unitCode `TNE`)  
  120 tonnes.
- `GoodsItem/ChargeableQuantity` = **120** (unitCode `TNE`)  
  The tonnes charged.
- `GoodsItem/TraceID` = **RR-PE-0417**  
  The lot on the bags' labels, the seller's lot number, as in its despatch advice.
- `GoodsItem/OrderLineReference/LineID` = **1**  
  The order line.
- `GoodsItem/OrderLineReference/OrderReference/ID` = **26-0339**  
  The buyer's order.
- `GoodsItem/OriginAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `GoodsItem/OriginAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `GoodsItem/OriginAddress/StreetName` = **Bek Han Zugaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Rinova Recovery gives it.
- `GoodsItem/OriginAddress/StreetName` = **Via del Riciclo** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Rinova Recovery gives it.
- `GoodsItem/OriginAddress/BuildingNumber` = **31**  
  Building number of the postal address. As Rinova Recovery gives it.
- `GoodsItem/OriginAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Rinova Recovery gives it.
- `GoodsItem/OriginAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Rinova Recovery gives it.
- `GoodsItem/OriginAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). As Rinova Recovery gives it.
- `GoodsItem/OriginAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Rinova Recovery gives it.
- `GoodsItem/OriginAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `GoodsItem/OriginAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/OriginAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `GoodsItem/Delivery/LatestDeliveryDate` = **2026-04-24**  
  The last day of the delivery window the buyer's order asks for.
- `GoodsItem/Pickup/EarliestPickupDate` = **2026-04-20**  
  The bags are ready on the quay.
- `GoodsItem/Pickup/EarliestPickupTime` = **08:00:00-01:00**  
  From eight; in the local time of Urvania, where it happens, with its offset from UTC.
- `GoodsItem/Pickup/LatestPickupDate` = **2026-04-20**  
  They must go the same day.
- `GoodsItem/Pickup/LatestPickupTime` = **16:00:00-01:00**  
  Before the quay closes; in the local time of Urvania, where it happens, with its offset from UTC.
- `GoodsItem/Despatch/ActualDespatchDate` = **2026-04-20**  
  The barge cast off.
- `GoodsItem/Despatch/ActualDespatchTime` = **15:10:00-01:00**  
  In the afternoon; in the local time of Urvania, where it happens, with its offset from UTC.
- `GoodsItem/ContainingPackage/Quantity` = **1** (unitCode `TNE`)  
  What one bag holds: a tonne of granulate; the consignment counts the 120 bags.
- `GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The bags go back to the recovery plant for reuse.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **JB** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code JB: bag, jumbo. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: JB = Bag, jumbo.
- `GoodsItem/ContainingPackage/PackagingType` = **Jumbo bag of one tonne with four lifting loops**  
  In words.
- `GoodsItem/ContainingPackage/PackingMaterial` = **Woven polypropylene**  
  What the bags are made of.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The height of one filled bag. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **1300** (unitCode `MMT`)  
  In millimetres.
- `GoodsItem/ShipmentDocumentReference/ID` = **26-0104**  
  The transport plan of the sailing.
- `GoodsItem/ShipmentDocumentReference/DocumentTypeCode` = **TransportExecutionPlan** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 26-0104 is the example plastics/04, a TransportExecutionPlan; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: TransportExecutionPlan = Transport Execution Plan.
- `GoodsItem/EnergyConsumptionAllocation/EnergySourceTypeCode` = **DIESEL** (listID `urn:ubl-examples:world:codelist:EnergySourceCode`)  
  The barge's engine fuel. The code is from the Trade Accord's energy source list: DIESEL = Diesel.
- `GoodsItem/EnergyConsumptionAllocation/AllocatedEnergyMeasure` = **5400** (unitCode `KWH`)  
  The goods' share of the voyage's energy, as fuel energy.
- `GoodsItem/EnergyConsumptionAllocation/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  Greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `GoodsItem/EnergyConsumptionAllocation/EnvironmentalEmission/ValueMeasure` = **1447** (unitCode `KGM`)  
  Tank to wheel: the 5,400 kWh of diesel allocated to the goods times 0.268 kg CO2e per kWh, about 2.67 kg per litre of diesel of about 10 kWh, the order of the diesel factor used in calculations under ISO 14083.

### Document Reference

Inside `DocumentReference`:

- `ID` = **26-0104**  
  The transport plan under which the carriage is performed.
- `DocumentTypeCode` = **TransportExecutionPlan** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 26-0104 is the example plastics/04, a TransportExecutionPlan; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: TransportExecutionPlan = Transport Execution Plan.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The original for the consignor.
- `DocumentTypeCode` = **Waybill** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this waybill. The code is from the Trade Accord's UBL document type list: Waybill.
- `DistributionTypeCode` = **ORIGINALHANDED** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The consignor's original, handed over when the carrier took over the goods, as the convention prescribes. The code is from the Trade Accord's distribution type list: ORIGINALHANDED = Original, handed over.
- `Party/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Rinova Recovery**  
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
- `Party/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Rivermouth Packaging**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FB-SIG-26-0181**  
  The carrier's signature on taking over the goods.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Fiumella Barges**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Waybill xmlns="urn:oasis:names:specification:ubl:schema:xsd:Waybill-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:waybill:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>26-0425</cbc:ProfileExecutionID>
  <cbc:ID>26-0181</cbc:ID>
  <cbc:CarrierAssignedID>26-0023</cbc:CarrierAssignedID>
  <cbc:UUID>0a38e2bd-26a7-55f9-833d-9ab2e55cfd4a</cbc:UUID>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">ISSUED</cbc:StatusCode>
  <cbc:IssueDate>2026-04-20</cbc:IssueDate>
  <cbc:IssueTime>15:26:00-01:00</cbc:IssueTime>
  <cbc:Name>Inland waterway consignment note under the CMNI</cbc:Name>
  <cbc:Description>The barge from the quay next to the recovery plant down the river to the packaging maker.</cbc:Description>
  <cbc:Note languageID="qau">Gurbul mizstan: drek starzhek, ginrul nartran zaskek drek sundraz hangaz nartran drek valnir; drek trelgir, vek drek valnir; drek vuznek, zhiztrek man drek sundraz.</cbc:Note>
  <cbc:Note languageID="en-XU">Three originals: the consignor's, handed over when the carrier took over the goods; the consignee's, with the goods; the carrier's, kept by the carrier.</cbc:Note>
  <cbc:WaybillTypeCode listID="urn:ubl-examples:world:codelist:WaybillTypeCode">CMNI</cbc:WaybillTypeCode>
  <cbc:ConsolidatedIndicator>false</cbc:ConsolidatedIndicator>
  <cbc:OtherInstruction>Deliver against signature of the consignee.</cbc:OtherInstruction>
  <cac:IssueLocation>
    <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
    <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
    <cac:Address>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:Address>
  </cac:IssueLocation>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Fiumella Barges</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160204198475331</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Skikzek Han Nestan</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Banchina del Fiume</cbc:StreetName>
      <cbc:BuildingNumber>52</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4170</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Chartering desk</cbc:Name>
      <cbc:JobTitle>Chartering manager</cbc:JobTitle>
      <cbc:Department>Operations</cbc:Department>
      <cbc:Telephone>+999 1 041 672 6403</cbc:Telephone>
      <cbc:ElectronicMail>chartering@fiumella.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104959</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:13362</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104548</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202983340277</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Han Zugaz</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via del Riciclo</cbc:StreetName>
      <cbc:BuildingNumber>31</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4140</cbc:PostalZone>
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
      <cbc:Telephone>+999 1 041 697 6856</cbc:Telephone>
      <cbc:ElectronicMail>logistics@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:CarrierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Fiumella Barges</cbc:Name>
    </cac:PartyName>
  </cac:CarrierParty>
  <cac:Shipment>
    <cbc:ID>26-0452</cbc:ID>
    <cac:Consignment>
      <cbc:ID>26-0426</cbc:ID>
      <cbc:CarrierAssignedID>FB4-26-031/2</cbc:CarrierAssignedID>
      <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
      <cbc:TotalPackagesQuantity>120</cbc:TotalPackagesQuantity>
      <cac:ConsigneeParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
        </cac:PartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="ISO 6523">0990:15128</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:AdditionalPartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412740</cbc:ID>
        </cac:AdditionalPartyIdentification>
        <cac:PartyName>
          <cbc:Name>Rivermouth Packaging</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-411619</cbc:ID>
          <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
          <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
          <cbc:StreetName>Estuary Road</cbc:StreetName>
          <cbc:BuildingNumber>28</cbc:BuildingNumber>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38505</cbc:PostalZone>
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
          <cbc:Telephone>+999 2 38 7320 9007</cbc:Telephone>
          <cbc:ElectronicMail>goodsin@rivermouth.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
      </cac:ConsigneeParty>
      <cac:FreightAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>River freight</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XUF">179400</cbc:Amount>
        <cbc:PerUnitAmount currencyID="XUF">1495</cbc:PerUnitAmount>
      </cac:FreightAllowanceCharge>
      <cac:MainCarriageShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">8</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">DS</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">815</cbc:TransportMeansTypeCode>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XU-IW-08042</cbc:VesselID>
            <cbc:VesselName>Fiumella IV</cbc:VesselName>
            <cbc:RadioCallSignID>QUBF4</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>297801042</cbc:MMSIRegistrationID>
            <cbc:GrossTonnageMeasure unitCode="C62">1210</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">860</cbc:NetTonnageMeasure>
            <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">DRYBARGE</cbc:ShipConfigurationCode>
            <cac:RegistryPortLocation>
              <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
              <cbc:Name>Ferrano</cbc:Name>
            </cac:RegistryPortLocation>
          </cac:MaritimeTransport>
        </cac:TransportMeans>
        <cac:LoadingPortLocation>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
        </cac:LoadingPortLocation>
        <cac:UnloadingPortLocation>
          <cbc:Name>River quay, Lumeport</cbc:Name>
        </cac:UnloadingPortLocation>
        <cac:LoadingTransportEvent>
          <cbc:OccurrenceDate>2026-04-20</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:30:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:LoadingTransportEvent>
        <cac:ExportationTransportEvent>
          <cbc:OccurrenceDate>2026-04-21</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>13:45:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:Name>River border Urvania–Bayvarra</cbc:Name>
          </cac:Location>
        </cac:ExportationTransportEvent>
        <cac:DischargeTransportEvent>
          <cbc:OccurrenceDate>2026-04-23</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>08:00:00-01:00</cbc:OccurrenceTime>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:Location>
            <cbc:Name>River quay, Lumeport</cbc:Name>
          </cac:Location>
        </cac:DischargeTransportEvent>
        <cac:TakeoverTransportEvent>
          <cbc:OccurrenceDate>2026-04-20</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>09:00:00-01:00</cbc:OccurrenceTime>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
            <cbc:Name>Quay of Rinova Recovery, Ferrano</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:TakeoverTransportEvent>
        <cac:EstimatedTransitPeriod>
          <cbc:DurationMeasure unitCode="DAY">3</cbc:DurationMeasure>
        </cac:EstimatedTransitPeriod>
        <cac:MasterPerson>
          <cbc:FirstName>Tomaso</cbc:FirstName>
          <cbc:FamilyName>Riverra</cbc:FamilyName>
          <cbc:JobTitle>Skipper</cbc:JobTitle>
        </cac:MasterPerson>
      </cac:MainCarriageShipmentStage>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
      <cbc:Description>Recycled PE granulate</cbc:Description>
      <cbc:DeclaredForCarriageValueAmount currencyID="XUF">9984000</cbc:DeclaredForCarriageValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
      <cbc:NetWeightMeasure unitCode="KGM">120000</cbc:NetWeightMeasure>
      <cbc:NetNetWeightMeasure unitCode="KGM">120000</cbc:NetNetWeightMeasure>
      <cbc:ChargeableWeightMeasure unitCode="KGM">120000</cbc:ChargeableWeightMeasure>
      <cbc:GrossVolumeMeasure unitCode="MTQ">204</cbc:GrossVolumeMeasure>
      <cbc:NetVolumeMeasure unitCode="MTQ">200</cbc:NetVolumeMeasure>
      <cbc:Quantity unitCode="TNE">120</cbc:Quantity>
      <cbc:ChargeableQuantity unitCode="TNE">120</cbc:ChargeableQuantity>
      <cbc:TraceID>RR-PE-0417</cbc:TraceID>
      <cac:OrderLineReference>
        <cbc:LineID>1</cbc:LineID>
        <cac:OrderReference>
          <cbc:ID>26-0339</cbc:ID>
        </cac:OrderReference>
      </cac:OrderLineReference>
      <cac:OriginAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Han Zugaz</cbc:StreetName>
        <cbc:StreetName languageID="en-XU">Via del Riciclo</cbc:StreetName>
        <cbc:BuildingNumber>31</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cbc:PostalZone>4140</cbc:PostalZone>
        <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:OriginAddress>
      <cac:Delivery>
        <cbc:LatestDeliveryDate>2026-04-24</cbc:LatestDeliveryDate>
      </cac:Delivery>
      <cac:Pickup>
        <cbc:EarliestPickupDate>2026-04-20</cbc:EarliestPickupDate>
        <cbc:EarliestPickupTime>08:00:00-01:00</cbc:EarliestPickupTime>
        <cbc:LatestPickupDate>2026-04-20</cbc:LatestPickupDate>
        <cbc:LatestPickupTime>16:00:00-01:00</cbc:LatestPickupTime>
      </cac:Pickup>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-04-20</cbc:ActualDespatchDate>
        <cbc:ActualDespatchTime>15:10:00-01:00</cbc:ActualDespatchTime>
      </cac:Despatch>
      <cac:ContainingPackage>
        <cbc:Quantity unitCode="TNE">1</cbc:Quantity>
        <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">JB</cbc:PackagingTypeCode>
        <cbc:PackagingType>Jumbo bag of one tonne with four lifting loops</cbc:PackagingType>
        <cbc:PackingMaterial>Woven polypropylene</cbc:PackingMaterial>
        <cac:MeasurementDimension>
          <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1300</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:ContainingPackage>
      <cac:ShipmentDocumentReference>
        <cbc:ID>26-0104</cbc:ID>
        <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">TransportExecutionPlan</cbc:DocumentTypeCode>
      </cac:ShipmentDocumentReference>
      <cac:EnergyConsumptionAllocation>
        <cbc:EnergySourceTypeCode listID="urn:ubl-examples:world:codelist:EnergySourceCode">DIESEL</cbc:EnergySourceTypeCode>
        <cbc:AllocatedEnergyMeasure unitCode="KWH">5400</cbc:AllocatedEnergyMeasure>
        <cac:EnvironmentalEmission>
          <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
          <cbc:ValueMeasure unitCode="KGM">1447</cbc:ValueMeasure>
        </cac:EnvironmentalEmission>
      </cac:EnergyConsumptionAllocation>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:DocumentReference>
    <cbc:ID>26-0104</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">TransportExecutionPlan</cbc:DocumentTypeCode>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Waybill</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ORIGINALHANDED</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>FB-SIG-26-0181</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Fiumella Barges</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</Waybill>
```
