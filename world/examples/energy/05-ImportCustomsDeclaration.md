# Import Customs Declaration: Montebrio Power to Customs Administration of Urvania

*Example 5 of the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The power station declares the gas it received in March into Urvania.

[The XML file](05-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **ENERGY-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **MP-IM-26-0156**  
  The importer's declaration number.
- `UUID` = **588c4166-cc9d-5604-8074-7a2b5bb9884a**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  The monthly declaration of the gas received in March.
- `IssueTime` = **16:55:00-01:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC (D27).
- `Note` = **Sarhek murdrir: valnir skul Accord dranan. Balstir munran vanbir raz: 20 % skul drek garsul munran skul 132,480,000 tezhul, 26,496,000 tezhul, zhan hir drek dizzan; drek stazstan serdaz skukstek trensek trek nakskek trikrul.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): What is due at import, by the importing country's rule (D18).
- `Note` = **No duty: goods of Accord origin. Import value added tax: 20 % of the customs value of 132,480,000 ferra, 26,496,000 ferra, paid at the border; the importer deducts it again in its return.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: What is due at import, by the importing country's rule (D18).

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Montebrio Power (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:10591** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates (decision ID-Q7). No real scheme has the code designator 0990; identity of Montebrio Power (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XU-TR-105918** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Montebrio Power (world/parties.json).
- `PartyName/Name` = **Montebrio Power**  
  The trading name; identity of Montebrio Power (world/parties.json).
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/ID` = **4170200397702895** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Montebrio Power (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/StreetName` = **Bek Hekrul Trinskul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Montebrio Power (world/parties.json).
- `PostalAddress/StreetName` = **Via della Centrale** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Montebrio Power (world/parties.json).
- `PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. identity of Montebrio Power (world/parties.json).
- `PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. identity of Montebrio Power (world/parties.json).
- `PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. identity of Montebrio Power (world/parties.json).
- `PostalAddress/PostalZone` = **4310**  
  Postal code in Urvania's format (4 digits). identity of Montebrio Power (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Montebrio Power (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered for value added tax; identity of Montebrio Power (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007414377** (schemeID `urn:ubl-examples:world:XU:tax`)  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Montebrio Power (world/parties.json). The schemeID names the scheme it is from: the VAT number of Urvania (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)).
- `PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT** (schemeID `UN/EDIFACT EDED 5153`)  
  UN/EDIFACT 5153 code of Urvania's value added tax. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: VAT = Value added tax. An identifier that holds a code names the code's list in its schemeID.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PartyLegalEntity/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered, with its legal form; identity of Montebrio Power (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; identity of Montebrio Power (world/parties.json). The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk desk: the desk for its role in this document (it deals with customs); identity of Montebrio Power (world/parties.json).
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; identity of Montebrio Power (world/parties.json).
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Montebrio Power (world/parties.json).
- `Contact/Telephone` = **+999 1 0413 55918**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Montebrio Power (world/parties.json).
- `Contact/ElectronicMail` = **customs@montebrio.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Montebrio Power (world/parties.json).
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Montebrio Power (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Montebrio Power (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Kelpstone Gas (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-412877** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Kelpstone Gas (world/parties.json).
- `PartyName/Name` = **Kelpstone Gas**  
  The trading name; identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/ID` = **NT-ADR-587853** (schemeID `urn:ubl-examples:world:XB:NT:address-register`)  
  The address's number in the address register of Northern Territory (NT-ADR- and six digits); identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Shoreline Road**  
  Street of the postal address. identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/BuildingNumber` = **2**  
  Building number of the postal address. identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/CityName` = **Gullhaven**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/PostalZone` = **90540**  
  Postal code in Bayvarra's format (5 digits). identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/CountrySubentity` = **Northern Territory**  
  The name of code XB-NT in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-NT** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Kelpstone Gas (world/parties.json). The code is from Bayvarra's national state or territory list: XB-NT = Northern Territory.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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

- `PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Customs Administration of Urvania**  
  The trading name; identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/ID` = **4180202968066555** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/AddressTypeCode` = **POSTAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: POSTAL = Postal address.
- `PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `PostalAddress/Postbox` = **PB 18**  
  The customs office receives its post in a post box. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/StreetName` = **Zalsul Han Trurdrek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/StreetName` = **Strada del Confine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/BuildingNumber` = **22**  
  Building number of the postal address. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/CityName` = **Menbaz** (languageID `qau`)  
  The place's Urvanian name, as the map gives it (world/map.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/CityName` = **Valico Euridice** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/PostalZone` = **4530**  
  Postal code in Urvania's format (4 digits). identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country (world/countries.json). identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Customs Administration of Urvania**  
  The public body's official name; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Name` = **Import office**  
  The party's import office desk: the desk for its role in this document (an import); identity of Customs Administration of Urvania (world/parties.json).
- `Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Department` = **Customs**  
  The department the desk belongs to; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Telephone` = **+999 1 041 349 5507**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Customs Administration of Urvania (world/parties.json).
- `Contact/ElectronicMail` = **import@customs-xu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; identity of Customs Administration of Urvania (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105507** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs Administration of Urvania (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **KG-SH-26-0154**  
  The shipment declared.
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
  The goods are of XB origin under the Trade Accord, by this criterion: the preference claimed, free of duty (D18). The code is from the Trade Accord's preference criterion list: P = Wholly obtained.
- `GoodsItem/Item/Description` = **Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.**  
  The seller's description; item natural-gas of Kelpstone Gas (world/items.json).
- `GoodsItem/Item/Name` = **Natural gas**  
  The item's short name; item natural-gas of Kelpstone Gas (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item natural-gas of Kelpstone Gas (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **V** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: V = Mineral products.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **BULK** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: BULK = Dry bulk.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **271121** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item natural-gas of Kelpstone Gas (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 271121 = Natural gas, in gaseous state.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **12020** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item natural-gas of Kelpstone Gas (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 12020 = Natural gas, liquefied or in the gaseous state.
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
- `ShipmentStage/TransportMeans/TransportMeansTypeCode` = **71** (listID `UNECE Recommendation 28`)  
  The gas arrives by pipeline. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 71 = Pipeline.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>ENERGY-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>MP-IM-26-0156</cbc:ID>
  <cbc:UUID>588c4166-cc9d-5604-8074-7a2b5bb9884a</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>16:55:00-01:00</cbc:IssueTime>
  <cbc:Note languageID="qau">Sarhek murdrir: valnir skul Accord dranan. Balstir munran vanbir raz: 20 % skul drek garsul munran skul 132,480,000 tezhul, 26,496,000 tezhul, zhan hir drek dizzan; drek stazstan serdaz skukstek trensek trek nakskek trikrul.</cbc:Note>
  <cbc:Note languageID="en-XU">No duty: goods of Accord origin. Import value added tax: 20 % of the customs value of 132,480,000 ferra, 26,496,000 ferra, paid at the border; the importer deducts it again in its return.</cbc:Note>
  <cac:ImporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:10591</cbc:ID>
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
      <cbc:Telephone>+999 1 0413 55918</cbc:Telephone>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105507</cbc:ID>
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
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Import office</cbc:Name>
      <cbc:JobTitle>Customs officer</cbc:JobTitle>
      <cbc:Department>Customs</cbc:Department>
      <cbc:Telephone>+999 1 041 349 5507</cbc:Telephone>
      <cbc:ElectronicMail>import@customs-xu.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105507</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:CustomsParty>
  <cac:Shipment>
    <cbc:ID>KG-SH-26-0154</cbc:ID>
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
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">BULK</cbc:CargoTypeCode>
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
      <cac:TransportMeans>
        <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">71</cbc:TransportMeansTypeCode>
      </cac:TransportMeans>
    </cac:ShipmentStage>
  </cac:Shipment>
</ImportCustomsDeclaration>
```
