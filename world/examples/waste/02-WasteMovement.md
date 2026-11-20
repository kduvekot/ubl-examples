# Waste Movement: Rinova Recovery to Environment Agency of Urvania

*Example 2 of the flow "Production waste to recovery (domestic, Urvania)" · [Waste Movement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WASTE-MOVEMENT-SCHEMA)*

The recovery facility reports to the environment agency the first load it has received under the notified stream: 54 bales, 22.9 tonnes net as its weighbridge found them, under the waste-stream number.

[The XML file](02-WasteMovement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; the document type WasteMovement first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:waste-movement:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Waste movement". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:waste-shipment:1.0**  
  The Trade Accord's process profile the document belongs to: waste shipment, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900043338**  
  The collaboration this document belongs to: the movement of Valdara's waste to Rinova Recovery. Valdara Industries started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0021**  
  The movement report number.
- `UUID` = **dbd3deda-0d71-53e4-9a07-a1f9d4add949**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Reported the day the load was received.
- `IssueTime` = **11:45:00-01:00**  
  Once the truck had been weighed empty; in the issuer's local time, with its offset from UTC.
- `WasteMovementTypeCode` = **RECOVERY** (listID `urn:ubl-examples:world:codelist:WasteOperationCategoryCode`)  
  The waste goes to recovery: Rinova recycles the film into granulate (operation R3 of its permit). The code is from the Trade Accord's waste operation category list: RECOVERY = Recovery.
- `SequenceNumberID` = **1**  
  The first load of the stream.
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
  The party's preferred identifier: its number in the Commercial register of Urvania; as Rinova Recovery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:13362** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Rinova Recovery gives it.
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; as Rinova Recovery gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
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
- `Contact/Name` = **Customer service**  
  The party's main desk, which handles this document; as Rinova Recovery gives it.
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; as Rinova Recovery gives it.
- `Contact/Department` = **Customer service**  
  The department the desk belongs to; as Rinova Recovery gives it.
- `Contact/Telephone` = **+999 1 041 697 6856**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Rinova Recovery gives it.
- `Contact/ElectronicMail` = **customer@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Rinova Recovery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Rinova Recovery gives it.
- `PartyAuthorization/PurposeCode` = **R3** (listID `Basel Convention Annex IV`)  
  The purpose as a code. The code is from the world's copy of Basel Convention, Annex IV: disposal and recovery operations: R3 = Recycling/reclamation of organic substances which are not used as solvents.
- `PartyAuthorization/Purpose` = **Recovery of non-hazardous plastic waste**  
  What the authority has authorized the party to do; as Rinova Recovery gives it.
- `PartyAuthorization/ValidityPeriod/EndDate` = **2029-12-31**  
  The authorization expires on this date.
- `PartyAuthorization/Certificate/ID` = **XU-ENV-2024-0311** (schemeID `urn:ubl-examples:world:XU:waste-permit`)  
  The number of the permit in the register of waste treatment permits of Urvania; the schemeID names the register, and with it the authority that keeps it, so no issuer party is needed.
- `PartyAuthorization/Certificate/CertificateTypeCode` = **PERMIT** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  A permit issued by an authority of the party's country. The code is from the Trade Accord's certificate type list: PERMIT = Operating permit.
- `PartyAuthorization/Certificate/CertificateType` = **Kusul treznul** (languageID `qau`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In Urvanian, the sender's language.
- `PartyAuthorization/Certificate/CertificateType` = **Operating permit** (languageID `en-XU`)  
  The name of code PERMIT in the Trade Accord's certificate type list. In English.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Rinova Recovery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **xu_p3wz** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The party's preferred identifier: its number in the Index of Public Administrations of Urvania; as Environment Agency of Urvania gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Environment Agency of Urvania**  
  The trading name; as Environment Agency of Urvania gives it.
- `PostalAddress/ID` = **4160204417730582** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Environment Agency of Urvania gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Drarban** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Environment Agency of Urvania gives it.
- `PostalAddress/StreetName` = **Via delle Acque** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Environment Agency of Urvania gives it.
- `PostalAddress/BuildingNumber` = **8**  
  Building number of the postal address. As Environment Agency of Urvania gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Environment Agency of Urvania gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Environment Agency of Urvania gives it.
- `PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). As Environment Agency of Urvania gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Environment Agency of Urvania gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Contact/Name` = **Waste reporting office**  
  The party's main desk, which handles this document; as Environment Agency of Urvania gives it.
- `Contact/JobTitle` = **Waste reporting officer**  
  The job of the person who answers at the desk; as Environment Agency of Urvania gives it.
- `Contact/Department` = **Waste and resources**  
  The department the desk belongs to; as Environment Agency of Urvania gives it.
- `Contact/Telephone` = **+999 1 041 732 5019**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Environment Agency of Urvania gives it.
- `Contact/ElectronicMail` = **waste@environment-xu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Environment Agency of Urvania gives it.
- `Contact/Note` = **Weekdays 08:00–16:00**  
  When the desk can be reached; as Environment Agency of Urvania gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:xu_p3wz** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Index of Public Administrations of Urvania; as Environment Agency of Urvania gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Notifier Party

Inside `NotifierParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Valdara Industries gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10014** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Valdara Industries gives it.
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
- `Contact/Name` = **Order desk**  
  The party's main desk, which handles this document; as Valdara Industries gives it.
- `Contact/JobTitle` = **Order administrator**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Contact/Department` = **Sales**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Contact/Telephone` = **+999 1 041 386 4551**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Valdara Industries gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `Contact/OtherCommunication/ChannelCode` = **AL** (listID `UN/EDIFACT EDED 3155`)  
  UN/EDIFACT 3155 code AL: cellular phone. The code is from UBL's default Communication channel (UN/EDIFACT 3155) list: AL = Cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 351 400 5258**  
  The sales desk's mobile number, also under the reserved +999.

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

- `ID` = **7400043504**  
  This load's own shipment number, beside the stream's.
- `NetWeightMeasure` = **22900** (unitCode `KGM`)  
  The waste received, net, from the weighbridge ticket.
- `Consignment/ID` = **7300043504**  
  This load's consignment, carried by the waste carrier.
- `Consignment/TotalPackagesQuantity` = **54**  
  54 bales on the truck, in two layers.
- `Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Trasvia Haulage gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Trasvia Haulage**  
  The trading name; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/ID` = **4160203746888095** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Bek Ban Kumek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Via dei Trasporti** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **45**  
  Building number of the postal address. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **4160**  
  Postal code in Urvania's format (4 digits). As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/Contact/Name` = **Planning desk**  
  The party's main desk, which handles this document; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/JobTitle` = **Transport planner**  
  The job of the person who answers at the desk; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/Telephone` = **+999 1 041 266 7643**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/ElectronicMail` = **planning@trasvia.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PartyAuthorization/Purpose` = **Transport of non-hazardous waste by road**  
  What the authority has authorized the party to do; as Trasvia Haulage gives it.
- `Consignment/CarrierParty/PartyAuthorization/ValidityPeriod/EndDate` = **2028-10-31**  
  The authorization expires on this date.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/ID` = **XU-ENV-T-2023-0187** (schemeID `urn:ubl-examples:world:XU:waste-carrier`)  
  The number of the permit in the register of waste carriers of Urvania; the schemeID names the register, and with it the authority that keeps it, so no issuer party is needed.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/CertificateTypeCode` = **WASTECARRIER** (listID `urn:ubl-examples:world:codelist:CertificateTypeCode`)  
  A registration with an authority of the party's country. The code is from the Trade Accord's certificate type list: WASTECARRIER = Waste carrier registration.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/CertificateType` = **Drunvir sundraz dradrek** (languageID `qau`)  
  The name of code WASTECARRIER in the Trade Accord's certificate type list. In Urvanian, the sender's language.
- `Consignment/CarrierParty/PartyAuthorization/Certificate/CertificateType` = **Waste carrier registration** (languageID `en-XU`)  
  The name of code WASTECARRIER in the Trade Accord's certificate type list. In English.
- `GoodsItem/ID` = **1**  
  The only goods item: one kind of waste.
- `GoodsItem/Description` = **Used polyethylene stretch film and film offcuts, baled**  
  What the waste is, in words.
- `GoodsItem/HazardousRiskIndicator` = **false**  
  Polyethylene film is not hazardous waste: its entry in the waste list has no asterisk.
- `GoodsItem/Item/Description` = **Used polyethylene stretch film and film offcuts, baled**  
  The waste, in words.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **150102** (listID `urn:ubl-examples:world:XU:codelist:WasteCode`)  
  The waste by its entry in Urvania's waste list, numbered after the European List of Waste: the film comes from the packaging of the parts and materials the factory receives and from the wrapping of its own pallets, and no chapter for the factory's activity (metal working and coating, chapters 08, 11 and 12) has an entry for packaging, so the list's rule sends it to chapter 15: 15 01 02 plastic packaging. The code is from Urvania's national waste list list: 150102 = Plastic packaging.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. Loose film would fill the trailer long before its payload; pressed into bales of about 1.2 × 0.8 × 1.0 m and 425 kg, two layers high, a load reaches the weight limit first. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `GoodsItem/ContainingPackage/PackingMaterial` = **Steel baling wire**  
  What holds a bale together.
- `ShipmentStage/ID` = **1**  
  The one road leg, across Ferrano.
- `ShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 3: road transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.
- `ShipmentStage/TransportMeans/RegistrationNationalityID` = **XU** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/TransportMeans/RegistrationNationality` = **Urvania**  
  The same, in words.
- `ShipmentStage/TransportMeans/TransportMeansTypeCode` = **395** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tractor unit 07 with curtain-side trailer; the fleet of Trasvia Haulage. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 395 = Truck, with trailer.
- `ShipmentStage/TransportMeans/RoadTransport/LicensePlateID` = **UR 4160 KT** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The registration plate of the truck; the fleet of Trasvia Haulage. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `ShipmentStage/TransportMeans/RoadTransport/TrailerLicensePlateID` = **UR 4160 TR** (schemeID `urn:ubl-examples:world:XU:vehicle-register`)  
  The trailer's own plate. The schemeID names the scheme it is from: the vehicle register of Urvania (UR, the four-digit number of the registering district (4160 Ferrano) and two letters).
- `ShipmentStage/TransportMeans/OwnerParty/PartyIdentification/ID` = **XU-R-104822** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ShipmentStage/TransportMeans/OwnerParty/PartyName/Name` = **Trasvia Haulage**  
  A party referred to from another party's details: its identifier and name are enough.
- `ShipmentStage/TransportMeans/MeasurementDimension/AttributeID` = **LOADINGLENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The length of the loading floor. The code is from the Trade Accord's dimension attribute list: LOADINGLENGTH = Loading length. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/TransportMeans/MeasurementDimension/Measure` = **13.6** (unitCode `MTR`)  
  Room for 33 pallets.
- `ShipmentStage/DriverPerson/ID` = **XU-DL-0417722**  
  The number of the driving licence.
- `ShipmentStage/DriverPerson/FirstName` = **Ilario**  
  The driver.
- `ShipmentStage/DriverPerson/FamilyName` = **Bencetti**  
  The family name.
- `Delivery/ActualDeliveryDate` = **2026-04-02**  
  The load arrived at the recovery plant.
- `Delivery/ActualDeliveryTime` = **10:05:00**  
  Trasvia's truck at the weighbridge.
- `Delivery/DeliveryLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Delivery/DeliveryLocation/Name` = **Rinova Recovery plant, Ferrano**  
  Where the waste was delivered.
- `Delivery/DeliveryLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Delivery/Despatch/ActualDespatchDate` = **2026-04-02**  
  Loaded at the factory the same morning.
- `Delivery/Despatch/ActualDespatchTime` = **09:35:00**  
  The truck left the factory; the two sites are a few kilometres apart in Ferrano.
- `Delivery/Despatch/DespatchLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Delivery/Despatch/DespatchLocation/Name` = **Valdara Industries works, Ferrano**  
  Where the bales were loaded.
- `Delivery/Despatch/DespatchLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Waste Notification Document Reference

Inside `WasteNotificationDocumentReference`:

- `ID` = **5700002167**  
  The notification of the stream the load belongs to.
- `IssueDate` = **2026-03-23**  
  Its date.

### Weight Statement Document Reference

Inside `WeightStatementDocumentReference`:

- `ID` = **26-0019**  
  The weighbridge ticket of the load, whose net weight this report states.
- `IssueDate` = **2026-04-02**  
  Its date.

### Document Reference

Inside `DocumentReference`:

- `ID` = **XU-ENV-WS-2026-04417**  
  The waste-stream number the environment agency gave the notified stream.
- `IssueDate` = **2026-03-25**  
  The day of the agency's acknowledgement.
- `DocumentType` = **Acknowledgement of the waste-stream notification**  
  The agency's acknowledgement, whose number each report of the stream quotes; a domestic stream of non-hazardous waste for recovery needs no consent.
- `IssuerParty/PartyIdentification/ID` = **xu_p3wz** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuerParty/PartyName/Name` = **Environment Agency of Urvania**  
  A party referred to from another party's details: its identifier and name are enough.
- `ID` = **26-0020**  
  The certificate of recovery to follow.
- `DocumentType` = **Certificate of recovery**  
  The kind of document referred to, Rinova's certificate of recovery, a document outside the examples, in words: no list has an exact code for it (cited).

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
  <cbc:ProfileExecutionID>9900043338</cbc:ProfileExecutionID>
  <cbc:ID>26-0021</cbc:ID>
  <cbc:UUID>dbd3deda-0d71-53e4-9a07-a1f9d4add949</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>11:45:00-01:00</cbc:IssueTime>
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
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:13362</cbc:ID>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Customer service</cbc:Department>
      <cbc:Telephone>+999 1 041 697 6856</cbc:Telephone>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_p3wz</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Environment Agency of Urvania</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160204417730582</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Stuzman Drarban</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via delle Acque</cbc:StreetName>
      <cbc:BuildingNumber>8</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4150</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Waste reporting office</cbc:Name>
      <cbc:JobTitle>Waste reporting officer</cbc:JobTitle>
      <cbc:Department>Waste and resources</cbc:Department>
      <cbc:Telephone>+999 1 041 732 5019</cbc:Telephone>
      <cbc:ElectronicMail>waste@environment-xu.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–16:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:xu_p3wz</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:NotifierParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10014</cbc:ID>
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
      <cbc:Name>Order desk</cbc:Name>
      <cbc:JobTitle>Order administrator</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      <cac:OtherCommunication>
        <cbc:ChannelCode listID="UN/EDIFACT EDED 3155">AL</cbc:ChannelCode>
        <cbc:Value>+999 1 351 400 5258</cbc:Value>
      </cac:OtherCommunication>
    </cac:Contact>
  </cac:NotifierParty>
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
    <cbc:ID>7400043504</cbc:ID>
    <cbc:NetWeightMeasure unitCode="KGM">22900</cbc:NetWeightMeasure>
    <cac:Consignment>
      <cbc:ID>7300043504</cbc:ID>
      <cbc:TotalPackagesQuantity>54</cbc:TotalPackagesQuantity>
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
        <cac:PartyAuthorization>
          <cbc:Purpose>Transport of non-hazardous waste by road</cbc:Purpose>
          <cac:ValidityPeriod>
            <cbc:EndDate>2028-10-31</cbc:EndDate>
          </cac:ValidityPeriod>
          <cac:Certificate>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:waste-carrier">XU-ENV-T-2023-0187</cbc:ID>
            <cbc:CertificateTypeCode listID="urn:ubl-examples:world:codelist:CertificateTypeCode">WASTECARRIER</cbc:CertificateTypeCode>
            <cbc:CertificateType languageID="qau">Drunvir sundraz dradrek</cbc:CertificateType>
            <cbc:CertificateType languageID="en-XU">Waste carrier registration</cbc:CertificateType>
          </cac:Certificate>
        </cac:PartyAuthorization>
      </cac:CarrierParty>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Used polyethylene stretch film and film offcuts, baled</cbc:Description>
      <cbc:HazardousRiskIndicator>false</cbc:HazardousRiskIndicator>
      <cac:Item>
        <cbc:Description>Used polyethylene stretch film and film offcuts, baled</cbc:Description>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="urn:ubl-examples:world:XU:codelist:WasteCode">150102</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
      </cac:Item>
      <cac:ContainingPackage>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
        <cbc:PackingMaterial>Steel baling wire</cbc:PackingMaterial>
      </cac:ContainingPackage>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
      <cac:TransportMeans>
        <cbc:RegistrationNationalityID schemeID="ISO 3166">XU</cbc:RegistrationNationalityID>
        <cbc:RegistrationNationality>Urvania</cbc:RegistrationNationality>
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
      <cac:DriverPerson>
        <cbc:ID>XU-DL-0417722</cbc:ID>
        <cbc:FirstName>Ilario</cbc:FirstName>
        <cbc:FamilyName>Bencetti</cbc:FamilyName>
      </cac:DriverPerson>
    </cac:ShipmentStage>
    <cac:Delivery>
      <cbc:ActualDeliveryDate>2026-04-02</cbc:ActualDeliveryDate>
      <cbc:ActualDeliveryTime>10:05:00</cbc:ActualDeliveryTime>
      <cac:DeliveryLocation>
        <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
        <cbc:Name>Rinova Recovery plant, Ferrano</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:DeliveryLocation>
      <cac:Despatch>
        <cbc:ActualDespatchDate>2026-04-02</cbc:ActualDespatchDate>
        <cbc:ActualDespatchTime>09:35:00</cbc:ActualDespatchTime>
        <cac:DespatchLocation>
          <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
          <cbc:Name>Valdara Industries works, Ferrano</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:DespatchLocation>
      </cac:Despatch>
    </cac:Delivery>
  </cac:Shipment>
  <cac:WasteNotificationDocumentReference>
    <cbc:ID>5700002167</cbc:ID>
    <cbc:IssueDate>2026-03-23</cbc:IssueDate>
  </cac:WasteNotificationDocumentReference>
  <cac:WeightStatementDocumentReference>
    <cbc:ID>26-0019</cbc:ID>
    <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  </cac:WeightStatementDocumentReference>
  <cac:DocumentReference>
    <cbc:ID>XU-ENV-WS-2026-04417</cbc:ID>
    <cbc:IssueDate>2026-03-25</cbc:IssueDate>
    <cbc:DocumentType>Acknowledgement of the waste-stream notification</cbc:DocumentType>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_p3wz</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Environment Agency of Urvania</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
  </cac:DocumentReference>
  <cac:DocumentReference>
    <cbc:ID>26-0020</cbc:ID>
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
