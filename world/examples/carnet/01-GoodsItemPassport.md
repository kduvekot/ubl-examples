# Goods Item Passport: Ferrano Chamber of Commerce to Valdara Industries

*Example 1 of the flow "Samples to a trade fair on the island (temporary export)" · [Goods Item Passport in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-GOODS-ITEM-PASSPORT-SCHEMA)*

The chamber issues the carnet to the manufacturer, who holds it while the samples travel.

[The XML file](01-GoodsItemPassport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:goods-item-passport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Goods item passport". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:temporary-admission:1.0**  
  The Trade Accord's process profile the document belongs to: temporary admission, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **FCC/2026/3170**  
  The collaboration this document belongs to: the carnet the Ferrano Chamber of Commerce issues and its proof of re-exportation. Ferrano Chamber of Commerce started it and gave it this identifier, which every document of it repeats.
- `ID` = **FCC/ATA/2026/0159**  
  The carnet number, given by the chamber.
- `UUID` = **eba67af9-0d62-5339-b7c5-75faae5007fc**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-25**  
  Issued before the samples leave for the fair.
- `IssueTime` = **15:04:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `StatusCode` = **VALID** (listID `urn:ubl-examples:world:codelist:RecordStatusCode`)  
  The carnet is valid. The code is from the Trade Accord's record status list: VALID = Valid.
- `Status` = **Issued**  
  In words.
- `Note` = **Barhek gan drek Selanu rizir tran trek geskek June; kildrek traz hek skuskan drek tran.** (languageID `qau`)  
  The note in Urvanian, the sender's language: What it is for.
- `Note` = **Samples for the Selanu trade fair in early June; they come home after the fair.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What it is for.
- `VersionID` = **1**  
  The first version.
- `ExportReasonCode` = **EXHIBITION** (listID `urn:ubl-examples:world:codelist:ExportReasonCode`)  
  Temporary export for a fair. The code is from the Trade Accord's export reason list: EXHIBITION = Exhibition or fair.
- `ExportReason` = **Exhibition at the Selanu trade fair**  
  In words.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-05-25**  
  Valid from issue.
- `EndDate` = **2027-05-25**  
  A carnet is valid for one year.

### Issuer Party

Inside `IssuerParty`:

- `PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The party's preferred identifier: its number in the Index of Public Administrations of Urvania; as Ferrano Chamber of Commerce gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; as Ferrano Chamber of Commerce gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `PostalAddress/ID` = **4160202319527073** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Chamber of Commerce gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Trazhek Han Zhatrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Chamber of Commerce gives it.
- `PostalAddress/StreetName` = **Piazza del Mercato** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Chamber of Commerce gives it.
- `PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address. As Ferrano Chamber of Commerce gives it.
- `PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Chamber of Commerce gives it.
- `PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Chamber of Commerce gives it.
- `PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). As Ferrano Chamber of Commerce gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Chamber of Commerce gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The public body's official name; as Ferrano Chamber of Commerce gives it.
- `PartyLegalEntity/CompanyID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  Number in the Index of Public Administrations of Urvania, which gives every public body a number of its own (xu_ and four lower-case letters or digits), derived from no other register ; as Ferrano Chamber of Commerce gives it. The schemeID names the scheme it is from: the index of public administrations of Urvania (xu_ and four lower-case letters or digits, assigned by the index on the body's accreditation; no real IPA code of Italy's index starts with xu_).
- `Contact/Name` = **Carnet office**  
  The party's carnet office desk: the desk for its role in this document (a carnet); as Ferrano Chamber of Commerce gives it.
- `Contact/JobTitle` = **Carnet officer**  
  The job of the person who answers at the desk; as Ferrano Chamber of Commerce gives it.
- `Contact/Department` = **Carnets**  
  The department the desk belongs to; as Ferrano Chamber of Commerce gives it.
- `Contact/Telephone` = **+999 1 041 714 2503**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Ferrano Chamber of Commerce gives it.
- `Contact/ElectronicMail` = **carnets@camera-ferrano.example**  
  The contact's e-mail address; as Ferrano Chamber of Commerce gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Ferrano Chamber of Commerce gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:xu_m2vd** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Index of Public Administrations of Urvania; as Ferrano Chamber of Commerce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Holder Party

Inside `HolderParty`:

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
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; as Valdara Industries gives it.
- `PartyLegalEntity/CompanyID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; as Valdara Industries gives it. The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Valdara Industries gives it.
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Valdara Industries gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Valdara Industries gives it.
- `Contact/Telephone` = **+999 1 041 386 4551**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Valdara Industries gives it.
- `Contact/ElectronicMail` = **customs@valdara.example**  
  The contact's e-mail address; as Valdara Industries gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Valdara Industries gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Valdara Industries gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Representative Party

Inside `RepresentativeParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at HolderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at HolderParty, where its full details are given; only its identifier and name are repeated.
- `Person/ID` = **VI-E-0412**  
  The employee's staff number; as Valdara Industries gives it.
- `Person/FirstName` = **Davide**  
  The first name of the employee who travels with the samples; as Valdara Industries gives it.
- `Person/FamilyName` = **Orsenna**  
  Their family name; as Valdara Industries gives it.
- `Person/Title` = **Ing.**  
  The professional title, as on the travel documents.
- `Person/JobTitle` = **Sales engineer**  
  Their job; as Valdara Industries gives it.
- `Person/NationalID` = **XU-NID-55102311**  
  The national identity number, which customs may ask for at the border.
- `Person/NationalityCode` = **XU** (listID `ISO 3166`)  
  Urvanian. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Person/BirthDate` = **1984-05-17**  
  The birth date, as in the passport.
- `Person/BirthplaceName` = **Ferrano**  
  The place of birth, as in the passport.
- `Person/OrganizationDepartment` = **Export sales**  
  The department the employee works in; as Valdara Industries gives it.
- `Person/BirthplaceLocation/ID` = **XUFER** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Person/BirthplaceLocation/Name` = **Ferrano**  
  The place of birth.
- `Person/BirthplaceLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  In Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Person/CitizenshipCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The employee is a citizen of Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Person/Contact/Name` = **Mobile on the road**  
  How to reach the employee at the fair.
- `Person/Contact/Telephone` = **+999 1 347 612 0893**  
  The employee's own mobile, not the holder's order desk.
- `Person/IdentityDocumentReference/ID` = **XU-P-2210931**  
  The passport the employee travels on.
- `Person/IdentityDocumentReference/DocumentType` = **Passport**  
  The kind of identity document.
- `Person/ResidenceAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. Where the employee lives.
- `Person/ResidenceAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. Where the employee lives.
- `Person/ResidenceAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  In Urvania. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Exporting Guarantor Party

Inside `ExportingGuarantorParty`:

- `PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The same party as at IssuerParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at IssuerParty, where its full details are given; only its identifier and name are repeated.

### Importing Guarantor Party

Inside `ImportingGuarantorParty`:

- `PartyIdentification/ID` = **GOV-243** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Selanu Chamber of Commerce gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Chamber of Commerce**  
  The trading name; as Selanu Chamber of Commerce gives it.
- `PostalAddress/ID` = **95763809** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Chamber of Commerce gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Chamber of Commerce gives it.
- `PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Chamber of Commerce gives it.
- `PostalAddress/BuildingNumber` = **30**  
  Building number of the postal address. As Selanu Chamber of Commerce gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Chamber of Commerce gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Chamber of Commerce gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.

### Exporting Customs Party

Inside `ExportingCustomsParty`:

- `PartyIdentification/ID` = **xu_k4r7** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The party's preferred identifier: its number in the Index of Public Administrations of Urvania; as Customs Administration of Urvania gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Customs Administration of Urvania**  
  The trading name; as Customs Administration of Urvania gives it.
- `PostalAddress/ID` = **4180202968066555** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Customs Administration of Urvania gives it.
- `PostalAddress/AddressTypeCode` = **POSTAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: POSTAL = Postal address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/Postbox` = **PB 18**  
  The customs office receives its post in a post box. As Customs Administration of Urvania gives it.
- `PostalAddress/StreetName` = **Zalsul Han Trurdrek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Customs Administration of Urvania gives it.
- `PostalAddress/StreetName` = **Strada del Confine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Customs Administration of Urvania gives it.
- `PostalAddress/BuildingNumber` = **22**  
  Building number of the postal address. As Customs Administration of Urvania gives it.
- `PostalAddress/CityName` = **Menbaz** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Customs Administration of Urvania gives it.
- `PostalAddress/CityName` = **Valico Euridice** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Customs Administration of Urvania gives it.
- `PostalAddress/PostalZone` = **4530**  
  Postal code in Urvania's format (4 digits). As Customs Administration of Urvania gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Customs Administration of Urvania gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.

### Importing Customs Party

Inside `ImportingCustomsParty`:

- `PartyIdentification/ID` = **GOV-118** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Island Customs Service gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Island Customs Service**  
  The trading name; as Island Customs Service gives it.
- `PostalAddress/ID` = **65334843** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Island Customs Service gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Island Customs Service gives it.
- `PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Island Customs Service gives it.
- `PostalAddress/BuildingNumber` = **53**  
  Building number of the postal address. As Island Customs Service gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Island Customs Service gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Island Customs Service gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.

### Shipment

Inside `Shipment`:

- `ID` = **7400044378**  
  The samples travelling under the carnet.
- `Consignment/ID` = **7300044378**  
  The consignment of the samples, in Valdara's series of consignment numbers.
- `Consignment/TransportAdvisorParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransportAdvisorParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `Consignment/TransitCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The samples cross Bayvarra by road to Lumeport airport: a transit country between Urvania and the island, on the carnet's transit counterfoils. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **99800** (currencyID `XUF`)  
  The value of the samples, for the guarantee.
- `GoodsItem/GrossWeightMeasure` = **94** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels.
- `GoodsItem/Quantity` = **2** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries.
- `GoodsItem/Item/Name` = **Haz nanskir Serra 180** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `GoodsItem/Item/Name` = **Park bench Serra 180** (languageID `en-XU`)  
  The item's name in English, the working language between the countries.
- `GoodsItem/Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; as Valdara Industries describes the item.
- `GoodsItem/Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRY = Grey.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `GoodsItem/Item/StandardItemIdentification/ID` = **KXU10014B180** (schemeID `ISO 15459-6`)  
  The item's number in its globally unique form under ISO/IEC 15459, which Valdara Industries gives it: the issuing agency code KXU of the Codana Identification Agency, the company number Codana gave Valdara Industries and the company's own reference for the item, without a check character. Codana gives a company its number; the company numbers its own items; as Valdara Industries describes the item.
- `GoodsItem/Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label: Code 128 carries letters and digits.
- `GoodsItem/Item/StandardItemIdentification/IssuerScopeID` = **KXU10014**  
  The scope within which Valdara Industries gives its item numbers: its company prefix, the issuing agency code KXU and its Codana company number; what follows is the company's own reference.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **XX** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XX = Miscellaneous manufactured articles.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **94017910** (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`)  
  The national tariff code of Urvania, two digits below the HS subheading, as its customs uses it: a second classification; as Valdara Industries describes the item. The code is from Urvania's national customs tariff list: 94017910 = Benches for parks and gardens, with metal frames.
- `GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `GoodsItem/ContainingPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `GoodsItem/ContainingPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `GoodsItem/ContainingPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `GoodsItem/ContainingPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `GoodsItem/ContainingPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `GoodsItem/ContainingPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `GoodsItem/ContainingPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `GoodsItem/ContainingPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `GoodsItem/ContainingPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `GoodsItem/ContainingPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/ContainingPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).

### Goods Item Passport Counterfoil

Inside `GoodsItemPassportCounterfoil`:

- `ID` = **EXP-1**  
  The exportation counterfoil (yellow sheet) of the carnet.
- `GoodsItemPassportID` = **FCC/ATA/2026/0159**  
  The carnet the counterfoil belongs to.
- `Note` = **To be stamped by customs when the samples leave Urvania.**  
  What the counterfoil is for: at issue no counterfoil is stamped yet.
- `CustomsOfficeLocation/ID` = **XU001001** (schemeID `urn:ubl-examples:world:XU:customs-office`)  
  The office's number in the customs office list of Urvania.
- `CustomsOfficeLocation/LocationTypeCode` = **BORDERPOST** (listID `urn:ubl-examples:world:codelist:CustomsLocationTypeCode`)  
  A customs post at the road border crossing. The code is from the Trade Accord's customs location type list: BORDERPOST = Border crossing point.
- `CustomsOfficeLocation/Name` = **Customs Administration of Urvania, Valico Euridice**  
  The customs office where the counterfoil is presented.
- `CustomsOfficeLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `EA`)  
  Two.
- `VoucherDocumentReference/ID` = **V-EXP-1**  
  The voucher customs detach and keep.
- `ID` = **TRA-1**  
  The transit counterfoil (blue sheet), outbound of the carnet.
- `GoodsItemPassportID` = **FCC/ATA/2026/0159**  
  The carnet the counterfoil belongs to.
- `Note` = **To be stamped by customs when the samples enter Bayvarra at Euridice Crossing and leave it at Lumeport airport.**  
  What the counterfoil is for: at issue no counterfoil is stamped yet.
- `CustomsOfficeLocation/ID` = **XB001001** (schemeID `urn:ubl-examples:world:XB:customs-office`)  
  The office's number in the customs office list of Bayvarra.
- `CustomsOfficeLocation/LocationTypeCode` = **BORDERPOST** (listID `urn:ubl-examples:world:codelist:CustomsLocationTypeCode`)  
  A customs post at the road border crossing. The code is from the Trade Accord's customs location type list: BORDERPOST = Border crossing point.
- `CustomsOfficeLocation/Name` = **Customs and Border Service of Bayvarra, Euridice Crossing**  
  The customs office where the counterfoil is presented.
- `CustomsOfficeLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `EA`)  
  Two.
- `VoucherDocumentReference/ID` = **V-TRA-1-IN**  
  The transit voucher Bayvarra's customs keep on entry.
- `VoucherDocumentReference/ID` = **V-TRA-1-OUT**  
  The transit voucher they keep on exit.
- `ID` = **IMP-1**  
  The importation counterfoil (white sheet) of the carnet.
- `GoodsItemPassportID` = **FCC/ATA/2026/0159**  
  The carnet the counterfoil belongs to.
- `Note` = **To be stamped by customs when the samples arrive on the island.**  
  What the counterfoil is for: at issue no counterfoil is stamped yet.
- `CustomsOfficeLocation/ID` = **XL001002** (schemeID `urn:ubl-examples:world:XL:customs-office`)  
  The office's number in the customs office list of Lisavu.
- `CustomsOfficeLocation/LocationTypeCode` = **CUSTOMSOFFICE** (listID `urn:ubl-examples:world:codelist:CustomsLocationTypeCode`)  
  A customs office at the airport. The code is from the Trade Accord's customs location type list: CUSTOMSOFFICE = Customs office.
- `CustomsOfficeLocation/Name` = **Island Customs Service, Selanu airport**  
  The customs office where the counterfoil is presented.
- `CustomsOfficeLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `EA`)  
  Two.
- `VoucherDocumentReference/ID` = **V-IMP-1**  
  The voucher customs detach and keep.
- `ID` = **REEXP-1**  
  The re-exportation counterfoil (white sheet) of the carnet.
- `GoodsItemPassportID` = **FCC/ATA/2026/0159**  
  The carnet the counterfoil belongs to.
- `Note` = **To be stamped by customs when the samples leave the island.**  
  What the counterfoil is for: at issue no counterfoil is stamped yet.
- `CustomsOfficeLocation/ID` = **XL001002** (schemeID `urn:ubl-examples:world:XL:customs-office`)  
  The office's number in the customs office list of Lisavu.
- `CustomsOfficeLocation/LocationTypeCode` = **CUSTOMSOFFICE** (listID `urn:ubl-examples:world:codelist:CustomsLocationTypeCode`)  
  A customs office at the airport. The code is from the Trade Accord's customs location type list: CUSTOMSOFFICE = Customs office.
- `CustomsOfficeLocation/Name` = **Island Customs Service, Selanu airport**  
  The customs office where the counterfoil is presented.
- `CustomsOfficeLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `EA`)  
  Two.
- `VoucherDocumentReference/ID` = **V-REEXP-1**  
  The voucher customs detach and keep.
- `ID` = **TRA-2**  
  The transit counterfoil (blue sheet), homeward of the carnet.
- `GoodsItemPassportID` = **FCC/ATA/2026/0159**  
  The carnet the counterfoil belongs to.
- `Note` = **To be stamped by customs when the samples enter Bayvarra at Lumeport airport and leave it at Euridice Crossing.**  
  What the counterfoil is for: at issue no counterfoil is stamped yet.
- `CustomsOfficeLocation/ID` = **XB002002** (schemeID `urn:ubl-examples:world:XB:customs-office`)  
  The office's number in the customs office list of Bayvarra.
- `CustomsOfficeLocation/LocationTypeCode` = **CUSTOMSOFFICE** (listID `urn:ubl-examples:world:codelist:CustomsLocationTypeCode`)  
  A customs office at the airport. The code is from the Trade Accord's customs location type list: CUSTOMSOFFICE = Customs office.
- `CustomsOfficeLocation/Name` = **Customs and Border Service of Bayvarra, Lumeport airport**  
  The customs office where the counterfoil is presented.
- `CustomsOfficeLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `EA`)  
  Two.
- `VoucherDocumentReference/ID` = **V-TRA-2-IN**  
  The transit voucher Bayvarra's customs keep on entry.
- `VoucherDocumentReference/ID` = **V-TRA-2-OUT**  
  The transit voucher they keep on exit.
- `ID` = **REIMP-1**  
  The re-importation counterfoil (yellow sheet) of the carnet.
- `GoodsItemPassportID` = **FCC/ATA/2026/0159**  
  The carnet the counterfoil belongs to.
- `Note` = **To be stamped by customs when the samples come home to Urvania.**  
  What the counterfoil is for: at issue no counterfoil is stamped yet.
- `CustomsOfficeLocation/ID` = **XU001001** (schemeID `urn:ubl-examples:world:XU:customs-office`)  
  The office's number in the customs office list of Urvania.
- `CustomsOfficeLocation/LocationTypeCode` = **BORDERPOST** (listID `urn:ubl-examples:world:codelist:CustomsLocationTypeCode`)  
  A customs post at the road border crossing. The code is from the Trade Accord's customs location type list: BORDERPOST = Border crossing point.
- `CustomsOfficeLocation/Name` = **Customs Administration of Urvania, Valico Euridice**  
  The customs office where the counterfoil is presented.
- `CustomsOfficeLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `EA`)  
  Two.
- `VoucherDocumentReference/ID` = **V-REIMP-1**  
  The voucher customs detach and keep.

### Issuer Endorsement

Inside `IssuerEndorsement`:

- `DocumentID` = **FCC/ATA/2026/0159**  
  The carnet.
- `ApprovalStatus` = **Issued**  
  The chamber issued it.
- `EndorserParty/RoleCode` = **ISSUER** (listID `urn:ubl-examples:world:codelist:EndorserRoleCode`)  
  The issuing chamber. The code is from the Trade Accord's endorser role list: ISSUER = Issuing body.
- `EndorserParty/SequenceNumeric` = **1**  
  The first endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/SignatoryContact/Name` = **Carnet office**  
  The chamber's carnet office, the name its contact has.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **SCC-FAIR-26-INV**  
  The fair's invitation to exhibit.
- `DocumentType` = **Invitation to exhibit**  
  The kind of document referred to, the fair's invitation to exhibit, in words: no list has an exact code for it.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The holder's carnet.
- `DocumentTypeCode` = **GoodsItemPassport** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The document distributed: this carnet. The code is from the Trade Accord's UBL document type list: GoodsItemPassport = Goods Item Passport.
- `DistributionTypeCode` = **COLLECT** (listID `urn:ubl-examples:world:codelist:DistributionTypeCode`)  
  The holder collects the paper carnet at the chamber's carnet office: customs stamp its counterfoils as the samples travel. The code is from the Trade Accord's distribution type list: COLLECT = Collect.
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FCC-SIG-26-ATA**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **xu_m2vd** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<GoodsItemPassport xmlns="urn:oasis:names:specification:ubl:schema:xsd:GoodsItemPassport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:goods-item-passport:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:temporary-admission:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>FCC/2026/3170</cbc:ProfileExecutionID>
  <cbc:ID>FCC/ATA/2026/0159</cbc:ID>
  <cbc:UUID>eba67af9-0d62-5339-b7c5-75faae5007fc</cbc:UUID>
  <cbc:IssueDate>2026-05-25</cbc:IssueDate>
  <cbc:IssueTime>15:04:00-01:00</cbc:IssueTime>
  <cbc:StatusCode listID="urn:ubl-examples:world:codelist:RecordStatusCode">VALID</cbc:StatusCode>
  <cbc:Status>Issued</cbc:Status>
  <cbc:Note languageID="qau">Barhek gan drek Selanu rizir tran trek geskek June; kildrek traz hek skuskan drek tran.</cbc:Note>
  <cbc:Note languageID="en-XU">Samples for the Selanu trade fair in early June; they come home after the fair.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:ExportReasonCode listID="urn:ubl-examples:world:codelist:ExportReasonCode">EXHIBITION</cbc:ExportReasonCode>
  <cbc:ExportReason>Exhibition at the Selanu trade fair</cbc:ExportReason>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-05-25</cbc:StartDate>
    <cbc:EndDate>2027-05-25</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:IssuerParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202319527073</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Trazhek Han Zhatrir</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Piazza del Mercato</cbc:StreetName>
      <cbc:BuildingNumber>15</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
      <cbc:PostalZone>4110</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Carnet office</cbc:Name>
      <cbc:JobTitle>Carnet officer</cbc:JobTitle>
      <cbc:Department>Carnets</cbc:Department>
      <cbc:Telephone>+999 1 041 714 2503</cbc:Telephone>
      <cbc:ElectronicMail>carnets@camera-ferrano.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:xu_m2vd</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:IssuerParty>
  <cac:HolderParty>
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
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 041 386 4551</cbc:Telephone>
      <cbc:ElectronicMail>customs@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:HolderParty>
  <cac:RepresentativeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:Person>
      <cbc:ID>VI-E-0412</cbc:ID>
      <cbc:FirstName>Davide</cbc:FirstName>
      <cbc:FamilyName>Orsenna</cbc:FamilyName>
      <cbc:Title>Ing.</cbc:Title>
      <cbc:JobTitle>Sales engineer</cbc:JobTitle>
      <cbc:NationalID>XU-NID-55102311</cbc:NationalID>
      <cbc:NationalityCode listID="ISO 3166">XU</cbc:NationalityCode>
      <cbc:BirthDate>1984-05-17</cbc:BirthDate>
      <cbc:BirthplaceName>Ferrano</cbc:BirthplaceName>
      <cbc:OrganizationDepartment>Export sales</cbc:OrganizationDepartment>
      <cac:BirthplaceLocation>
        <cbc:ID schemeID="UN/LOCODE">XUFER</cbc:ID>
        <cbc:Name>Ferrano</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:BirthplaceLocation>
      <cac:CitizenshipCountry>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:CitizenshipCountry>
      <cac:Contact>
        <cbc:Name>Mobile on the road</cbc:Name>
        <cbc:Telephone>+999 1 347 612 0893</cbc:Telephone>
      </cac:Contact>
      <cac:IdentityDocumentReference>
        <cbc:ID>XU-P-2210931</cbc:ID>
        <cbc:DocumentType>Passport</cbc:DocumentType>
      </cac:IdentityDocumentReference>
      <cac:ResidenceAddress>
        <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
        <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:ResidenceAddress>
    </cac:Person>
  </cac:RepresentativeParty>
  <cac:ExportingGuarantorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
    </cac:PartyName>
  </cac:ExportingGuarantorParty>
  <cac:ImportingGuarantorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-243</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">95763809</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>30</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ImportingGuarantorParty>
  <cac:ExportingCustomsParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_k4r7</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Customs Administration of Urvania</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4180202968066555</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">POSTAL</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:Postbox>PB 18</cbc:Postbox>
      <cbc:StreetName languageID="qau">Zalsul Han Trurdrek</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Strada del Confine</cbc:StreetName>
      <cbc:BuildingNumber>22</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Menbaz</cbc:CityName>
      <cbc:CityName languageID="en-XU">Valico Euridice</cbc:CityName>
      <cbc:PostalZone>4530</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ExportingCustomsParty>
  <cac:ImportingCustomsParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-118</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Island Customs Service</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">65334843</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>53</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ImportingCustomsParty>
  <cac:Shipment>
    <cbc:ID>7400044378</cbc:ID>
    <cac:Consignment>
      <cbc:ID>7300044378</cbc:ID>
      <cac:TransportAdvisorParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Bayforth Forwarding</cbc:Name>
        </cac:PartyName>
      </cac:TransportAdvisorParty>
      <cac:TransitCountry>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:TransitCountry>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XUF">99800</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">94</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
      <cac:Item>
        <cbc:Description languageID="qau">Haz nanskir, 1800 mm, manskan skul vazzhan stan krarhir-trunnir zhukvan stezir gek, bukdrek kalnan skul zhaznul dunnir darhir, gan zharsul krir drek tarkul.</cbc:Description>
        <cbc:Description languageID="en-XU">Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.</cbc:Description>
        <cbc:Name languageID="qau">Haz nanskir Serra 180</cbc:Name>
        <cbc:Name languageID="en-XU">Park bench Serra 180</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>VI-B180</cbc:ID>
          <cbc:ExtendedID>GRY</cbc:ExtendedID>
          <cac:PhysicalAttribute>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
            <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
            <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
            <cbc:Description>Frame in Ferro grey</cbc:Description>
          </cac:PhysicalAttribute>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="ISO 15459-6">KXU10014B180</cbc:ID>
          <cbc:BarcodeSymbologyID>Code128</cbc:BarcodeSymbologyID>
          <cbc:IssuerScopeID>KXU10014</cbc:IssuerScopeID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">XX</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:CommodityClassification>
          <cbc:CommodityCode listID="urn:ubl-examples:world:XU:codelist:CustomsTariffCode">94017910</cbc:CommodityCode>
        </cac:CommodityClassification>
      </cac:Item>
      <cac:ContainingPackage>
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
      </cac:ContainingPackage>
      <cac:ContainingPackage>
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
      </cac:ContainingPackage>
      <cac:ContainingPackage>
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
      </cac:ContainingPackage>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>EXP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC/ATA/2026/0159</cbc:GoodsItemPassportID>
    <cbc:Note>To be stamped by customs when the samples leave Urvania.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-office">XU001001</cbc:ID>
      <cbc:LocationTypeCode listID="urn:ubl-examples:world:codelist:CustomsLocationTypeCode">BORDERPOST</cbc:LocationTypeCode>
      <cbc:Name>Customs Administration of Urvania, Valico Euridice</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-EXP-1</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>TRA-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC/ATA/2026/0159</cbc:GoodsItemPassportID>
    <cbc:Note>To be stamped by customs when the samples enter Bayvarra at Euridice Crossing and leave it at Lumeport airport.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-office">XB001001</cbc:ID>
      <cbc:LocationTypeCode listID="urn:ubl-examples:world:codelist:CustomsLocationTypeCode">BORDERPOST</cbc:LocationTypeCode>
      <cbc:Name>Customs and Border Service of Bayvarra, Euridice Crossing</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-TRA-1-IN</cbc:ID>
    </cac:VoucherDocumentReference>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-TRA-1-OUT</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>IMP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC/ATA/2026/0159</cbc:GoodsItemPassportID>
    <cbc:Note>To be stamped by customs when the samples arrive on the island.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-office">XL001002</cbc:ID>
      <cbc:LocationTypeCode listID="urn:ubl-examples:world:codelist:CustomsLocationTypeCode">CUSTOMSOFFICE</cbc:LocationTypeCode>
      <cbc:Name>Island Customs Service, Selanu airport</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-IMP-1</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>REEXP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC/ATA/2026/0159</cbc:GoodsItemPassportID>
    <cbc:Note>To be stamped by customs when the samples leave the island.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-office">XL001002</cbc:ID>
      <cbc:LocationTypeCode listID="urn:ubl-examples:world:codelist:CustomsLocationTypeCode">CUSTOMSOFFICE</cbc:LocationTypeCode>
      <cbc:Name>Island Customs Service, Selanu airport</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-REEXP-1</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>TRA-2</cbc:ID>
    <cbc:GoodsItemPassportID>FCC/ATA/2026/0159</cbc:GoodsItemPassportID>
    <cbc:Note>To be stamped by customs when the samples enter Bayvarra at Lumeport airport and leave it at Euridice Crossing.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-office">XB002002</cbc:ID>
      <cbc:LocationTypeCode listID="urn:ubl-examples:world:codelist:CustomsLocationTypeCode">CUSTOMSOFFICE</cbc:LocationTypeCode>
      <cbc:Name>Customs and Border Service of Bayvarra, Lumeport airport</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-TRA-2-IN</cbc:ID>
    </cac:VoucherDocumentReference>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-TRA-2-OUT</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>REIMP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC/ATA/2026/0159</cbc:GoodsItemPassportID>
    <cbc:Note>To be stamped by customs when the samples come home to Urvania.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-office">XU001001</cbc:ID>
      <cbc:LocationTypeCode listID="urn:ubl-examples:world:codelist:CustomsLocationTypeCode">BORDERPOST</cbc:LocationTypeCode>
      <cbc:Name>Customs Administration of Urvania, Valico Euridice</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="EA">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-REIMP-1</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:IssuerEndorsement>
    <cbc:DocumentID>FCC/ATA/2026/0159</cbc:DocumentID>
    <cbc:ApprovalStatus>Issued</cbc:ApprovalStatus>
    <cac:EndorserParty>
      <cbc:RoleCode listID="urn:ubl-examples:world:codelist:EndorserRoleCode">ISSUER</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Carnet office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
  </cac:IssuerEndorsement>
  <cac:AdditionalDocumentReference>
    <cbc:ID>SCC-FAIR-26-INV</cbc:ID>
    <cbc:DocumentType>Invitation to exhibit</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">GoodsItemPassport</cbc:DocumentTypeCode>
    <cbc:DistributionTypeCode listID="urn:ubl-examples:world:codelist:DistributionTypeCode">COLLECT</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>FCC-SIG-26-ATA</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_m2vd</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</GoodsItemPassport>
```
