# Import Customs Declaration: Montebrio Power to Customs Administration of Urvania

*Example 5 of the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The power station declares its consignment of March's gas into Urvania, under the shipment of the export declaration.

[The XML file](05-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900004628**  
  The collaboration this document belongs to: Montebrio Power's import declaration of its consignment of March's gas, to its release for free circulation. Montebrio Power started it and gave it this identifier, which every document of it repeats.
- `ID` = **7700000926**  
  The importer's declaration number.
- `UUID` = **588c4166-cc9d-5604-8074-7a2b5bb9884a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-03**  
  The monthly declaration of the gas received in March, lodged once the producer's invoice with its statement on origin is in.
- `IssueTime` = **16:55:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `Note` = **Sarhek murdrir: valnir skul Accord dranan. Balstir munran vanbir raz: 20 % skul drek garsul munran skul 132,480,000 tezhul, 26,496,000 tezhul, zhan hir drek dizzan; drek stazstan serdaz skukstek trensek trek nakskek trikrul.** (languageID `qau`)  
  The note in Urvanian, the sender's language: What is due at import, by the importing country's rule.
- `Note` = **No duty: goods of Accord origin. Import value added tax: 20 % of the customs value of 132,480,000 ferra, 26,496,000 ferra, paid at the border; the importer deducts it again in its return.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What is due at import, by the importing country's rule.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Montebrio Power gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10087** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Montebrio Power gives it.
- `AdditionalPartyIdentification/ID` = **XU-TR-105918** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Montebrio Power gives it.
- `PartyName/Name` = **Montebrio Power**  
  The trading name; as Montebrio Power gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
- `PostalAddress/ID` = **4170200397702895** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Montebrio Power gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Hekrul Trinskul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Montebrio Power gives it.
- `PostalAddress/StreetName` = **Via della Centrale** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Montebrio Power gives it.
- `PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. As Montebrio Power gives it.
- `PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Montebrio Power gives it.
- `PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Montebrio Power gives it.
- `PostalAddress/PostalZone` = **4310**  
  Postal code in Urvania's format (4 digits). As Montebrio Power gives it.
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Montebrio Power gives it.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered for value added tax; as Montebrio Power gives it.
- `PartyTaxScheme/CompanyID` = **XU007414377** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); as Montebrio Power gives it. The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered, with its legal form; as Montebrio Power gives it.
- `PartyLegalEntity/CompanyID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; as Montebrio Power gives it. The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Montebrio Power gives it.
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Montebrio Power gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Montebrio Power gives it.
- `Contact/Telephone` = **+999 1 0413 46716**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Montebrio Power gives it.
- `Contact/ElectronicMail` = **customs@montebrio.example**  
  The contact's e-mail address; as Montebrio Power gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Montebrio Power gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Montebrio Power gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Kelpstone Gas gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:19676** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Kelpstone Gas gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-412877** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Kelpstone Gas gives it.
- `PartyName/Name` = **Kelpstone Gas**  
  The trading name; as Kelpstone Gas gives it.
- `PostalAddress/ID` = **NT-ADR-587853** (schemeID `urn:ubl-examples:world:XB:NT:address-register`)  
  The address's number in the address register of Northern Territory (NT-ADR- and six digits); as Kelpstone Gas gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Shoreline Road**  
  Street of the postal address. As Kelpstone Gas gives it.
- `PostalAddress/BuildingNumber` = **2**  
  Building number of the postal address. As Kelpstone Gas gives it.
- `PostalAddress/CityName` = **Gullhaven**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Kelpstone Gas gives it.
- `PostalAddress/PostalZone` = **90540**  
  Postal code in Bayvarra's format (5 digits). As Kelpstone Gas gives it.
- `PostalAddress/CountrySubentity` = **Northern Territory**  
  The name of code XB-NT in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-NT** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Kelpstone Gas gives it. The code is from Bayvarra's national state or territory list: XB-NT = Northern Territory.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Montebrio Power**  
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

- `ID` = **7400034203**  
  The shipment of the export declaration: March's gas through the pipeline, of which this declaration covers one consignment.
- `Consignment/ID` = **7300034203**  
  The importer's consignment, as the export declaration names it.
- `Consignment/GrossWeightMeasure` = **2760000** (unitCode `KGM`)  
  The weight of the gas declared.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Natural gas**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **132480000** (currencyID `XUF`)  
  The customs value in ferra.
- `GoodsItem/GrossWeightMeasure` = **2760000** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **36800** (unitCode `MWH`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **P** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XB origin under the Trade Accord, by this criterion: the preference claimed, free of duty. The code is from the Trade Accord's preference criterion list: P = Wholly obtained.
- `GoodsItem/Item/Description` = **Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Natural gas**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Kelpstone Gas describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **V** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: V = Mineral products.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **271121** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Kelpstone Gas describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 271121 = Natural gas, in gaseous state.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **12020** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Kelpstone Gas describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 12020 = Natural gas, liquefied or in the gaseous state.
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  Urvania's value added tax at import, at the standard rate. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **20**  
  The standard rate.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code VAT: value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `ShipmentStage/ID` = **1**  
  The only stage.
- `ShipmentStage/TransportModeCode` = **7** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 7: fixed transport installation, a pipeline. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 7 = Fixed transport installations.
- `ShipmentStage/TransitPeriod/StartDate` = **2026-03-01**  
  The gas declared flowed through the pipeline in March: a monthly declaration of a continuous flow.
- `ShipmentStage/TransitPeriod/EndDate` = **2026-03-31**  
  The month's last day.
- `ShipmentStage/TransportMeans/TransportMeansTypeCode` = **71** (listID `UNECE Recommendation 28`)  
  The gas arrives by pipeline. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 71 = Pipeline.
- `FirstArrivalPortLocation/Description` = **On Bayvarra's side of the border with Urvania, in the Northern Territory.**  
  Where it stands.
- `FirstArrivalPortLocation/Name` = **Border metering station of the Kelpstone gas pipeline**  
  Where the gas comes into Urvania: the border metering station, just before the border, measures it.
- `FirstArrivalPortLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `FirstArrivalPortLocation/LocationCoordinate/LatitudeDegreesMeasure` = **28** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `FirstArrivalPortLocation/LocationCoordinate/LatitudeMinutesMeasure` = **40.54** (unitCode `D61`)  
  The minutes of the latitude.
- `FirstArrivalPortLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `FirstArrivalPortLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `FirstArrivalPortLocation/LocationCoordinate/LongitudeMinutesMeasure` = **42.48** (unitCode `D61`)  
  The minutes of the longitude.
- `FirstArrivalPortLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **7600006841**  
  The export declaration of the shipment, which names this consignment.
- `IssueDate` = **2026-04-02**  
  Lodged the day before in Bayvarra.
- `DocumentTypeCode` = **ExportCustomsDeclaration** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  An export declaration: the other country's, so not a previous declaration of this customs. The code is from the Trade Accord's UBL document type list: ExportCustomsDeclaration = Export Customs Declaration.
- `ID` = **9000034209**  
  The commercial invoice the customs value rests on; its statement on origin is the proof of origin the preference claim refers to.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 9000034209 is the example energy/06, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900004628</cbc:ProfileExecutionID>
  <cbc:ID>7700000926</cbc:ID>
  <cbc:UUID>588c4166-cc9d-5604-8074-7a2b5bb9884a</cbc:UUID>
  <cbc:IssueDate>2026-04-03</cbc:IssueDate>
  <cbc:IssueTime>16:55:00-01:00</cbc:IssueTime>
  <cbc:Note languageID="qau">Sarhek murdrir: valnir skul Accord dranan. Balstir munran vanbir raz: 20 % skul drek garsul munran skul 132,480,000 tezhul, 26,496,000 tezhul, zhan hir drek dizzan; drek stazstan serdaz skukstek trensek trek nakskek trikrul.</cbc:Note>
  <cbc:Note languageID="en-XU">No duty: goods of Accord origin. Import value added tax: 20 % of the customs value of 132,480,000 ferra, 26,496,000 ferra, paid at the border; the importer deducts it again in its return.</cbc:Note>
  <cac:ImporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10087</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-105918</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Montebrio Power</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4170200397702895</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Bek Hekrul Trinskul</cbc:StreetName>
      <cbc:StreetName languageID="en-XU">Via della Centrale</cbc:StreetName>
      <cbc:BuildingNumber>44</cbc:BuildingNumber>
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
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Montebrio Power SUA</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:tax">XU007414377</cbc:CompanyID>
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
      <cbc:RegistrationName>Montebrio Power SUA</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 0413 46716</cbc:Telephone>
      <cbc:ElectronicMail>customs@montebrio.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105918</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:19676</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412877</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelpstone Gas</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:NT:address-register">NT-ADR-587853</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Shoreline Road</cbc:StreetName>
      <cbc:BuildingNumber>2</cbc:BuildingNumber>
      <cbc:CityName>Gullhaven</cbc:CityName>
      <cbc:PostalZone>90540</cbc:PostalZone>
      <cbc:CountrySubentity>Northern Territory</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-NT</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Montebrio Power</cbc:Name>
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
    <cbc:ID>7400034203</cbc:ID>
    <cac:Consignment>
      <cbc:ID>7300034203</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">2760000</cbc:GrossWeightMeasure>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Natural gas</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XUF">132480000</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">2760000</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="MWH">36800</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">P</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description>Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.</cbc:Description>
        <cbc:Name>Natural gas</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">V</cbc:NatureCode>
          <cbc:CommodityCode listID="WCO HS 2022">271121</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">12020</cbc:ItemClassificationCode>
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
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">7</cbc:TransportModeCode>
      <cac:TransitPeriod>
        <cbc:StartDate>2026-03-01</cbc:StartDate>
        <cbc:EndDate>2026-03-31</cbc:EndDate>
      </cac:TransitPeriod>
      <cac:TransportMeans>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">71</cbc:TransportMeansTypeCode>
      </cac:TransportMeans>
    </cac:ShipmentStage>
    <cac:FirstArrivalPortLocation>
      <cbc:Description>On Bayvarra's side of the border with Urvania, in the Northern Territory.</cbc:Description>
      <cbc:Name>Border metering station of the Kelpstone gas pipeline</cbc:Name>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure unitCode="DD">28</cbc:LatitudeDegreesMeasure>
        <cbc:LatitudeMinutesMeasure unitCode="D61">40.54</cbc:LatitudeMinutesMeasure>
        <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
        <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
        <cbc:LongitudeMinutesMeasure unitCode="D61">42.48</cbc:LongitudeMinutesMeasure>
        <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
      </cac:LocationCoordinate>
    </cac:FirstArrivalPortLocation>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>7600006841</cbc:ID>
    <cbc:IssueDate>2026-04-02</cbc:IssueDate>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ExportCustomsDeclaration</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>9000034209</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
</ImportCustomsDeclaration>
```
