# Waste Movement: Rinova Recovery to Customs Administration of Urvania

*Example 2 of the flow "Production waste to recovery (domestic, Urvania)" · [Waste Movement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WASTE-MOVEMENT-SCHEMA)*

The recovery facility reports each movement received to the competent authority.

[The XML file](02-WasteMovement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); the document type WasteMovement first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waste-movement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waste movement". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:waste-shipment:1.0**  
  The Trade Accord's process profile the document belongs to: waste shipment, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **WASTE-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **RR-DOC-26-0207**  
  The movement document number.
- `UUID` = **dbd3deda-0d71-53e4-9a07-a1f9d4add949**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Reported when the waste has been received.
- `IssueTime` = **12:34:00**  
  The time the sender's system issued the document, in the sender's local time.
- `WasteMovementTypeCode` = **RECOVERY** (listID `urn:ubl-examples:world:codelist:WasteOperationCategoryCode`)  
  A movement of waste for recovery. The code is from the Trade Accord's waste operation category list: RECOVERY = Recovery.
- `SequenceNumberID` = **1**  
  The first movement under the notification.
- `ConsignmentQuantity` = **12** (unitCode `EA`)  
  Of about twelve notified.

### Signature

Inside `Signature`:

- `ID` = **RR-SIG-WM**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Rinova Recovery**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4160202983340277** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Han Zugaz** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/StreetName` = **Via del Riciclo** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Rinova Recovery (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Customer service**  
  The party's main desk, which handles this document; identity of Rinova Recovery (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rinova Recovery (world/parties.json).
- `Contact/Department` = **Customer service**  
  The department the desk belongs to; identity of Rinova Recovery (world/parties.json).
- `Contact/Telephone` = **+999 1 041 836 4548**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Rinova Recovery (world/parties.json).
- `Contact/ElectronicMail` = **customer@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rinova Recovery (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rinova Recovery (world/parties.json).
- `PartyAuthorization/PurposeCode` = **R3** (listID `Basel Convention Annex IV`)  
  The purpose as a code. The code is from the world's copy of Basel Convention, Annex IV: disposal and recovery operations: R3 = Recycling/reclamation of organic substances which are not used as solvents.
- `PartyAuthorization/Purpose` = **Recovery of non-hazardous plastic waste**  
  What the authority has authorized the party to do; identity of Rinova Recovery (world/parties.json).
- `PartyAuthorization/ValidityPeriod/EndDate` = **2029-12-31**  
  The authorization expires on this date.
- `PartyAuthorization/Certificate/ID` = **XU-ENV-2024-0311** (schemeID `urn:ubl-examples:world:XU:waste-permit`)  
  The number of the permit in the register of waste treatment permits of Urvania; the schemeID names the register, and with it the authority that keeps it, so no issuer party is needed (decision ID-Q10).
- `PartyAuthorization/Certificate/CertificateTypeCode` = **PERMIT** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  A permit issued by an authority of the party's country. The code is from the Trade Accord's certificate type list: PERMIT = Operating permit.
- `PartyAuthorization/Certificate/CertificateType` = **Kusul treznul** (languageID `qau`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In Urvanian, the sender's language.
- `PartyAuthorization/Certificate/CertificateType` = **Operating permit** (languageID `en-XU`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In English.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rinova Recovery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Customs Administration of Urvania**  
  The trading name; identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/ID` = **4160202968066555** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/AddressTypeCode` = **POSTAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: POSTAL = Postal address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/Postbox` = **PB 18**  
  The customs office receives its post in a post box. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/StreetName` = **Birran Stir Trurdrek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/StreetName` = **Valico di Confine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/BuildingNumber` = **22**  
  Building number of the postal address. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Border office**  
  The party's main desk, which handles this document; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Department` = **Customs**  
  The department the desk belongs to; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Telephone` = **+999 1 041 349 5507**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Telefax` = **+999 1 041 326 0018**  
  The customs office still lists a fax number; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/ElectronicMail` = **border@customs-xu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Customs Administration of Urvania (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105507** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs Administration of Urvania (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Notifier Party

Inside `NotifierParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10427** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
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
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Order desk**  
  The party's main desk, which handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Order administrator**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 041 518 4274**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 344 474 4274**  
  The sales desk's mobile number, also under the reserved +999.

### Disposal Facility Party

Inside `DisposalFacilityParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Rinova Recovery**  
  A party referred to from another party's details: its identifier and name are enough.

### Recovery Facility Party

Inside `RecoveryFacilityParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Rinova Recovery**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Waste Producer Party

Inside `WasteProducerParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at NotifierParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at NotifierParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **VI-SH-26-0205**  
  The movement's shipment number.
- `GrossWeightMeasure` = **38200** (unitCode `KGM`)  
  Weighed on arrival at the recovery facility.
- `Consignment/ID` = **VI-CS-26-0206**  
  The consignment carried by the road carrier.
- `Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Trasvia Haulage (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Trasvia Haulage**  
  The trading name; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/ID` = **4160203746888095** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Bek Ban Kumek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Via dei Trasporti** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/Contact/Name` = **Planning desk**  
  The party's main desk, which handles this document; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/JobTitle` = **Transport planner**  
  The job of the person who answers at the desk; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Telephone` = **+999 1 041 354 4822**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyAuthorization/Purpose` = **International road haulage**  
  What the authority has authorized the party to do; identity of Trasvia Haulage (world/parties.json).
- `Consignment/CarrierParty/PartyAuthorization/ValidityPeriod/EndDate` = **2030-06-30**  
  The authorization expires on this date.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/ID` = **XU-HAUL-2020-0877** (schemeID `urn:ubl-examples:world:XU:haulage-licence`)  
  The number of the permit in the register of road haulage licences of Urvania; the schemeID names the register, and with it the authority that keeps it, so no issuer party is needed (decision ID-Q10).
- `Consignment/CarrierParty/PartyAuthorization/Certificate/CertificateTypeCode` = **PERMIT** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  A permit issued by an authority of the party's country. The code is from the Trade Accord's certificate type list: PERMIT = Operating permit.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/CertificateType` = **Kusul treznul** (languageID `qau`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In Urvanian, the sender's language.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/CertificateType` = **Operating permit** (languageID `en-XU`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In English.
- `GoodsItem/ID` = **1**  
  The only goods item.
- `GoodsItem/Description` = **Mixed polyethylene production waste, sorted, in big bags**  
  What the waste is.
- `GoodsItem/HazardousRiskIndicator` = **false**  
  Sorted polyethylene is not hazardous waste.

### Waste Notification Document Reference

Inside `WasteNotificationDocumentReference`:

- `ID` = **VI-DOC-26-0204**  
  The notification the movement is made under.

### Weight Statement Document Reference

Inside `WeightStatementDocumentReference`:

- `ID` = **RR-WB-26-0412**  
  The weighbridge ticket of the recovery plant (not shown).

### Document Reference

Inside `DocumentReference`:

- `ID` = **RR-REC-26-0412**  
  The certificate of recovery to follow.
- `DocumentType` = **Certificate of recovery**  
  The kind of document referred to, Rinova's certificate of recovery, a document outside the examples, in words: no list has an exact code for it (world/documents.json, cited; decision Q29).

### Document Distribution

Inside `DocumentDistribution`:

- `DocumentTypeCode` = **WasteMovement** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this movement document. The code is from the Trade Accord's UBL document type list: WasteMovement = Waste Movement.
- `DistributionTypeCode` = **ELECTRONICCOPY** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  Sent electronically, as a copy. The code is from the Trade Accord's distribution type list: ELECTRONICCOPY = Electronic copy.
- `DistributionType` = **Viskir zuzzir: drek stelskek skukek kazhek skukstek vek drek duntraz** (languageID `qau`)  
  The name of code ELECTRONICCOPY in the Trade Accord's distribution type list, followed by the detail of this case: why the producer gets a copy. In Urvanian, the sender's language.
- `DistributionType` = **Electronic copy: the producer must keep it with the notification** (languageID `en-XU`)  
  The name of code ELECTRONICCOPY in the Trade Accord's distribution type list, followed by the detail of this case: why the producer gets a copy. In English.
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<WasteMovement xmlns="urn:oasis:names:specification:ubl:schema:xsd:WasteMovement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:waste-movement:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:waste-shipment:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>WASTE-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>RR-DOC-26-0207</cbc:ID>
  <cbc:UUID>dbd3deda-0d71-53e4-9a07-a1f9d4add949</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>12:34:00</cbc:IssueTime>
  <cbc:WasteMovementTypeCode listID="urn:ubl-examples:world:codelist:WasteOperationCategoryCode">RECOVERY</cbc:WasteMovementTypeCode>
  <cbc:SequenceNumberID>1</cbc:SequenceNumberID>
  <cbc:ConsignmentQuantity unitCode="EA">12</cbc:ConsignmentQuantity>
  <cac:Signature>
    <cbc:ID>RR-SIG-WM</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
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
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Customer service</cbc:Department>
      <cbc:Telephone>+999 1 041 836 4548</cbc:Telephone>
      <cbc:ElectronicMail>customer@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:PartyAuthorization>
      <cbc:PurposeCode listID="Basel Convention Annex IV">R3</cbc:PurposeCode>
      <cbc:Purpose>Recovery of non-hazardous plastic waste</cbc:Purpose>
      <cac:ValidityPeriod>
        <cbc:EndDate>2029-12-31</cbc:EndDate>
      </cac:ValidityPeriod>
      <cac:Certificate>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:waste-permit">XU-ENV-2024-0311</cbc:ID>
        <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">PERMIT</cbc:CertificateTypeCode>
        <cbc:CertificateType languageID="qau">Kusul treznul</cbc:CertificateType>
        <cbc:CertificateType languageID="en-XU">Operating permit</cbc:CertificateType>
      </cac:Certificate>
    </cac:PartyAuthorization>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105507</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Customs Administration of Urvania</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202968066555</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">POSTAL</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:Postbox>PB 18</cbc:Postbox>
      <cbc:StreetName languageID="qau">Birran Stir Trurdrek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Valico di Confine</cbc:StreetName>
      <cbc:BuildingNumber>22</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4120</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Border office</cbc:Name>
      <cbc:JobTitle>Customs officer</cbc:JobTitle>
      <cbc:Department>Customs</cbc:Department>
      <cbc:Telephone>+999 1 041 349 5507</cbc:Telephone>
      <cbc:Telefax>+999 1 041 326 0018</cbc:Telefax>
      <cbc:ElectronicMail>border@customs-xu.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105507</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:NotifierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10427</cbc:ID>
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
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Order desk</cbc:Name>
      <cbc:JobTitle>Order administrator</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 041 518 4274</cbc:Telephone>
      <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      <cac:OtherCommunication>
        <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
        <cbc:Value>+999 1 344 474 4274</cbc:Value>
      </cac:OtherCommunication>
    </cac:Contact>
  </cac:NotifierParty>
  <cac:DisposalFacilityParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
  </cac:DisposalFacilityParty>
  <cac:RecoveryFacilityParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
  </cac:RecoveryFacilityParty>
  <cac:WasteProducerParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:WasteProducerParty>
  <cac:Shipment>
    <cbc:ID>VI-SH-26-0205</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">38200</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>VI-CS-26-0206</cbc:ID>
      <cac:CarrierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104822</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Trasvia Haulage</cbc:Name>
        </cac:PartyName>
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
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:Contact>
          <cbc:Name>Planning desk</cbc:Name>
          <cbc:JobTitle>Transport planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 1 041 354 4822</cbc:Telephone>
          <cbc:ElectronicMail>planning@trasvia.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:PartyAuthorization>
          <cbc:Purpose>International road haulage</cbc:Purpose>
          <cac:ValidityPeriod>
            <cbc:EndDate>2030-06-30</cbc:EndDate>
          </cac:ValidityPeriod>
          <cac:Certificate>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:haulage-licence">XU-HAUL-2020-0877</cbc:ID>
            <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">PERMIT</cbc:CertificateTypeCode>
            <cbc:CertificateType languageID="qau">Kusul treznul</cbc:CertificateType>
            <cbc:CertificateType languageID="en-XU">Operating permit</cbc:CertificateType>
          </cac:Certificate>
        </cac:PartyAuthorization>
      </cac:CarrierParty>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Mixed polyethylene production waste, sorted, in big bags</cbc:Description>
      <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:WasteNotificationDocumentReference>
    <cbc:ID>VI-DOC-26-0204</cbc:ID>
  </cac:WasteNotificationDocumentReference>
  <cac:WeightStatementDocumentReference>
    <cbc:ID>RR-WB-26-0412</cbc:ID>
  </cac:WeightStatementDocumentReference>
  <cac:DocumentReference>
    <cbc:ID>RR-REC-26-0412</cbc:ID>
    <cbc:DocumentType>Certificate of recovery</cbc:DocumentType>
  </cac:DocumentReference>
  <cac:DocumentDistribution>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">WasteMovement</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">ELECTRONICCOPY</cbc:DistributionTypeCode>
    <cbc:DistributionType languageID="qau">Viskir zuzzir: drek stelskek skukek kazhek skukstek vek drek duntraz</cbc:DistributionType>
    <cbc:DistributionType languageID="en-XU">Electronic copy: the producer must keep it with the notification</cbc:DistributionType>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
</WasteMovement>
```
