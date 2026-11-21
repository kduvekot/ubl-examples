# Import Customs Declaration: Tostara Wood Modification to Customs Administration of Urvania

*Example 5 of the flow "Modification: bench slats modified under contract (Bayvarra → Urvania)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The plant, holder of the authorisation, enters the blanks into inward processing: no import VAT while they are worked, for they are not released for free circulation.

[The XML file](05-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **26-0015**  
  The collaboration this document belongs to: Tostara's declaration entering the first load of ash blanks into inward processing, to their release into the procedure. Tostara Wood Modification started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0003**  
  The importer's declaration number.
- `UUID` = **42bf875d-0c59-5c56-8017-2165bd938f88**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-01-13**  
  Lodged when the first load reaches the border.
- `IssueTime` = **10:30:00-01:00**  
  When the truck stands at the Urvanian post, after the Bayvarran export; in the issuer's local time, with its offset from UTC.
- `TypeCode` = **IMPORT** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode`)  
  An import declaration. The code is from the Trade Accord's customs declaration type list: IMPORT = Import declaration.
- `SubTypeCode` = **INWARDPROC** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationSubTypeCode`)  
  Entry into inward processing: the goods are worked in Urvania without duty or import VAT until they are released. The code is from the Trade Accord's customs declaration subtype list: INWARDPROC = Inward processing.
- `NatureOfTransactionCode` = **PROCESSING** (listID `urn:ubl-examples:world:codelist:NatureOfTransactionCode`)  
  The goods come for processing under contract; they are not bought. The code is from the Trade Accord's nature of transaction list: PROCESSING = For or after processing.
- `Note` = **Sakrek matir: sarhek murdrir stan sarhek balstir munran vanbir raz hunir drek valnir datrir duzhaz karul drek trelhek. Drek valnir datrir skul Accord dranan; drek balstir munran vanbir raz skul 20 % rek haskek garsul munran skul 1,212,000 tezhul dir skalran hanvek zaskek drek kradran nilvek datrir kedan gan nudrir sarskir. Drek valnir takzek drek hunek skul Marrowdale Sawmill, Marrowdale, Bayvarra, gan dravul drek zhisir skul drek havaz zhakrek karhan.** (languageID `qau`)  
  The note in Urvanian, the sender's language: What is due at import, by the importing country's rule; and whose the goods are.
- `Note` = **Inward processing: no duty and no import value added tax while the goods are worked under the procedure. The goods are of Accord origin; the import value added tax of 20 % on their customs value of 1,212,000 ferra is due only when the processed products are released for free circulation. The goods remain the property of Marrowdale Sawmill, Marrowdale, Bayvarra, for which the holder of the authorisation processes them.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What is due at import, by the importing country's rule; and whose the goods are.
- `VersionID` = **1**  
  The first version.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-01-13**  
  From the entry.
- `EndDate` = **2026-07-13**  
  The period of the authorisation within which the processed products must be discharged: six months.

### Jurisdiction Region Address

Inside `JurisdictionRegionAddress`:

- `Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The customs territory of import. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-106192** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Tostara Wood Modification gives it.
- `PartyName/Name` = **Tostara Wood Modification**  
  The trading name; as Tostara Wood Modification gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `PostalAddress/ID` = **4160205830117402** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Tostara Wood Modification gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Stuzman Tuntrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Tostara Wood Modification gives it.
- `PostalAddress/StreetName` = **Via delle Concerie** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Tostara Wood Modification gives it.
- `PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Tostara Wood Modification gives it.
- `PostalAddress/CityName` = **Zhildir** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Tostara Wood Modification gives it.
- `PostalAddress/CityName` = **Conciaro** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Tostara Wood Modification gives it.
- `PostalAddress/PostalZone` = **4190**  
  Postal code in Urvania's format (4 digits). As Tostara Wood Modification gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Tostara Wood Modification gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Tostara Wood Modification SRU**  
  The name under which the party is registered for value added tax; as Tostara Wood Modification gives it.
- `PartyTaxScheme/CompanyID` = **XU007433554** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); as Tostara Wood Modification gives it. The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/RegistrationName` = **Tostara Wood Modification SRU**  
  The name under which the party is registered, with its legal form; as Tostara Wood Modification gives it.
- `PartyLegalEntity/CompanyID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; as Tostara Wood Modification gives it. The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Tostara Wood Modification gives it.
- `Contact/JobTitle` = **Customs and stock clerk**  
  The job of the person who answers at the desk; as Tostara Wood Modification gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Tostara Wood Modification gives it.
- `Contact/Telephone` = **+999 1 041 573 2290**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Tostara Wood Modification gives it.
- `Contact/ElectronicMail` = **customs@tostara.example**  
  The contact's e-mail address; as Tostara Wood Modification gives it.
- `Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; as Tostara Wood Modification gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-106192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Tostara Wood Modification gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Marrowdale Sawmill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-412329** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Marrowdale Sawmill gives it.
- `PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; as Marrowdale Sawmill gives it.
- `PostalAddress/ID` = **UL-ADR-296778** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Marrowdale Sawmill gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Timber Lane**  
  Street of the postal address. As Marrowdale Sawmill gives it.
- `PostalAddress/BuildingNumber` = **7**  
  Building number of the postal address. As Marrowdale Sawmill gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Marrowdale Sawmill gives it.
- `PostalAddress/PostalZone` = **71202**  
  Postal code in Bayvarra's format (5 digits). As Marrowdale Sawmill gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Marrowdale Sawmill gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tostara Wood Modification**  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.

### Customs Party

Inside `CustomsParty`:

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
- `PartyLegalEntity/RegistrationName` = **Customs Administration of Urvania**  
  The public body's official name; as Customs Administration of Urvania gives it.
- `PartyLegalEntity/CompanyID` = **xu_k4r7** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  Number in the Index of Public Administrations of Urvania, which gives every public body a number of its own (xu_ and four lower-case letters or digits), derived from no other register ; as Customs Administration of Urvania gives it. The schemeID names the scheme it is from: the index of public administrations of Urvania (xu_ and four lower-case letters or digits, assigned by the index on the body's accreditation; no real IPA code of Italy's index starts with xu_).
- `Contact/Name` = **Import office**  
  The party's import office desk: the desk for its role in this document (an import); as Customs Administration of Urvania gives it.
- `Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; as Customs Administration of Urvania gives it.
- `Contact/Department` = **Customs**  
  The department the desk belongs to; as Customs Administration of Urvania gives it.
- `Contact/Telephone` = **+999 1 041 850 3855**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Customs Administration of Urvania gives it.
- `Contact/ElectronicMail` = **import@customs-xu.example**  
  The contact's e-mail address; as Customs Administration of Urvania gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Customs Administration of Urvania gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:xu_k4r7** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Index of Public Administrations of Urvania; as Customs Administration of Urvania gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **MDS-SH-26-0051**  
  The shipment declared.
- `TotalTransportHandlingUnitQuantity` = **12** (unitCode `EA`)  
  The pallets the goods travel on.
- `DeclaredStatisticsValueAmount` = **1212000** (currencyID `XUF`)  
  The value trade statistics record the blanks at as they enter the procedure: what they would be invoiced at, with the carriage to the border; their later release into free circulation is not recorded again.
- `Consignment/ID` = **MDS-CS-26-0051**  
  The sawmill's number for the load.
- `Consignment/GrossWeightMeasure` = **14448** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight arriving.
- `Consignment/OfficeOfEntryLocation/ID` = **XU001001** (schemeID `urn:ubl-examples:world:XU:customs-office`)  
  The office's number in the customs office list of Urvania.
- `Consignment/OfficeOfEntryLocation/Name` = **Customs post at the land border, Urvanian side**  
  One of the offices the authorisation names as empowered to accept the plant's entries: the border post, for loads that come by road.
- `Consignment/OfficeOfEntryLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Consignment/OfficeOfEntryLocation/SubsidiaryLocation/ID` = **XU002001** (schemeID `urn:ubl-examples:world:XU:customs-office`)  
  The office's number in the customs office list of Urvania.
- `Consignment/OfficeOfEntryLocation/SubsidiaryLocation/Name` = **Inland customs office, Ferrano**  
  The other office the authorisation names, for entries lodged inland.
- `Consignment/OfficeOfEntryLocation/SubsidiaryLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Ash blank 1830, kiln dried**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **1212000** (currencyID `XUF`)  
  Urvania values the goods with freight and insurance to its border: the goods at 1,152,000 XUF, with the carriage to the border on the sawmill's own truck, at its cost as the sawmill reckons it (60,000 XUF), shared over the goods items by their value.
- `GoodsItem/GrossWeightMeasure` = **14448** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **2400** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **P** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XB origin under the Trade Accord, by this criterion: the preference claimed, free of duty. The code is from the Trade Accord's preference criterion list: P = Wholly obtained.
- `GoodsItem/Item/Description` = **Sawn and kiln-dried European ash, 1830 × 101 × 51 mm, a blank for the bench slat MDS-SL-1800 before it is modified and planed.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Ash blank 1830, kiln dried**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Marrowdale Sawmill describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **IX** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: IX = Wood and articles of wood; cork; basketware.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **440795** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Marrowdale Sawmill describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 440795 = Wood sawn or chipped lengthwise, of a thickness exceeding 6 mm: of ash (Fraxinus spp.).
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **31102** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Marrowdale Sawmill describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 31102 = Wood, sawn or chipped lengthwise, sliced or peeled, of a thickness exceeding 6 mm, of non-coniferous wood .
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  Urvania's value added tax at import, at the standard rate. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **20**  
  The standard rate.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code VAT: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/TransportModeCode` = **3** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by road. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 3 = Road transport.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **XU-IP-AUT-0217**  
  The plant's authorisation for inward processing, under which the entry is made.
- `DocumentType` = **Inward processing authorisation**  
  What it is.
- `ID` = **MDS-PF-26-0113**  
  The sawmill's pro forma invoice: the value of the blanks for customs, there being no sale; it carries the sawmill's statement on origin as their exporter, the proof of the Accord origin the entry claims.
- `DocumentTypeCode` = **325** (listID `UN/EDIFACT EDED 1001`)  
  UN/EDIFACT 1001 code 325: proforma invoice. The code is from the world's copy of UN/EDIFACT 1001 Document name: 325 = Proforma invoice.
- `ID` = **MDS-EX-26-0011**  
  The export declaration of the goods in the country of departure, for information.
- `DocumentTypeCode` = **ExportCustomsDeclaration** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: MDS-EX-26-0011 is the example modification/04, a ExportCustomsDeclaration; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: ExportCustomsDeclaration = Export Customs Declaration.

### Signature

Inside `Signature`:

- `ID` = **TWM-SIG-IM-modification**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-106192** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Tostara Wood Modification**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>26-0015</cbc:ProfileExecutionID>
  <cbc:ID>26-0003</cbc:ID>
  <cbc:UUID>42bf875d-0c59-5c56-8017-2165bd938f88</cbc:UUID>
  <cbc:IssueDate>2026-01-13</cbc:IssueDate>
  <cbc:IssueTime>10:30:00-01:00</cbc:IssueTime>
  <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode">IMPORT</cbc:TypeCode>
  <cbc:SubTypeCode listID="urn:ubl-examples:world:codelist:CustomsDeclarationSubTypeCode">INWARDPROC</cbc:SubTypeCode>
  <cbc:NatureOfTransactionCode listID="urn:ubl-examples:world:codelist:NatureOfTransactionCode">PROCESSING</cbc:NatureOfTransactionCode>
  <cbc:Note languageID="qau">Sakrek matir: sarhek murdrir stan sarhek balstir munran vanbir raz hunir drek valnir datrir duzhaz karul drek trelhek. Drek valnir datrir skul Accord dranan; drek balstir munran vanbir raz skul 20 % rek haskek garsul munran skul 1,212,000 tezhul dir skalran hanvek zaskek drek kradran nilvek datrir kedan gan nudrir sarskir. Drek valnir takzek drek hunek skul Marrowdale Sawmill, Marrowdale, Bayvarra, gan dravul drek zhisir skul drek havaz zhakrek karhan.</cbc:Note>
  <cbc:Note languageID="en-XU">Inward processing: no duty and no import value added tax while the goods are worked under the procedure. The goods are of Accord origin; the import value added tax of 20 % on their customs value of 1,212,000 ferra is due only when the processed products are released for free circulation. The goods remain the property of Marrowdale Sawmill, Marrowdale, Bayvarra, for which the holder of the authorisation processes them.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-01-13</cbc:StartDate>
    <cbc:EndDate>2026-07-13</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:JurisdictionRegionAddress>
    <cac:Country>
      <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
    </cac:Country>
  </cac:JurisdictionRegionAddress>
  <cac:ImporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-106192</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tostara Wood Modification</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160205830117402</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Stuzman Tuntrir</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via delle Concerie</cbc:StreetName>
      <cbc:BuildingNumber>9</cbc:BuildingNumber>
      <cbc:CityName languageID="qau">Zhildir</cbc:CityName>
      <cbc:CityName languageID="en-XU">Conciaro</cbc:CityName>
      <cbc:PostalZone>4190</cbc:PostalZone>
      <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Tostara Wood Modification SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007433554</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XUF</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Tostara Wood Modification SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs and stock clerk</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 041 573 2290</cbc:Telephone>
      <cbc:ElectronicMail>customs@tostara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-106192</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412329</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Marrowdale Sawmill</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-296778</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Timber Lane</cbc:StreetName>
      <cbc:BuildingNumber>7</cbc:BuildingNumber>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71202</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tostara Wood Modification</cbc:Name>
    </cac:PartyName>
  </cac:ConsigneeParty>
  <cac:CustomsParty>
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
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Customs Administration of Urvania</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:public-body-register">xu_k4r7</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Import office</cbc:Name>
      <cbc:JobTitle>Customs officer</cbc:JobTitle>
      <cbc:Department>Customs</cbc:Department>
      <cbc:Telephone>+999 1 041 850 3855</cbc:Telephone>
      <cbc:ElectronicMail>import@customs-xu.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:xu_k4r7</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:CustomsParty>
  <cac:Shipment>
    <cbc:ID>MDS-SH-26-0051</cbc:ID>
    <cbc:TotalTransportHandlingUnitQuantity unitCode="EA">12</cbc:TotalTransportHandlingUnitQuantity>
    <cbc:DeclaredStatisticsValueAmount currencyID="XUF">1212000</cbc:DeclaredStatisticsValueAmount>
    <cac:Consignment>
      <cbc:ID>MDS-CS-26-0051</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">14448</cbc:GrossWeightMeasure>
      <cac:OfficeOfEntryLocation>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-office">XU001001</cbc:ID>
        <cbc:Name>Customs post at the land border, Urvanian side</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
        <cac:SubsidiaryLocation>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-office">XU002001</cbc:ID>
          <cbc:Name>Inland customs office, Ferrano</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:SubsidiaryLocation>
      </cac:OfficeOfEntryLocation>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Ash blank 1830, kiln dried</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XUF">1212000</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">14448</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">2400</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">P</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description>Sawn and kiln-dried European ash, 1830 × 101 × 51 mm, a blank for the bench slat MDS-SL-1800 before it is modified and planed.</cbc:Description>
        <cbc:Name>Ash blank 1830, kiln dried</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">IX</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">440795</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">31102</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ClassifiedTaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
          <cbc:Percent>20</cbc:Percent>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">VAT</cbc:ID>
          </cac:TaxScheme>
        </cac:ClassifiedTaxCategory>
      </cac:Item>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">3</cbc:TransportModeCode>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>XU-IP-AUT-0217</cbc:ID>
    <cbc:DocumentType>Inward processing authorisation</cbc:DocumentType>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>MDS-PF-26-0113</cbc:ID>
    <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">325</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>MDS-EX-26-0011</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ExportCustomsDeclaration</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>TWM-SIG-IM-modification</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-106192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Tostara Wood Modification</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ImportCustomsDeclaration>
```
