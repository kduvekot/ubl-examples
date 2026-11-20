# Import Customs Declaration: Hafefo Fresh Produce to Island Customs Service

*Example 9 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Import Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-IMPORT-CUSTOMS-DECLARATION-SCHEMA)*

The wholesaler lodges its import declaration before the ship arrives, so that the fruit is released when the reefer is discharged; the import consumption tax applies to food as to every import.

[The XML file](09-ImportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:import-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Import customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **REEFER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **HFP-IM-26-0564**  
  The importer's declaration number.
- `UUID` = **04b3c1d3-d600-57c6-b790-ffbf27e1ac34**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-24**  
  Lodged on Friday 24 April, while the reefer is at sea, so that the fruit can be released when it is discharged.
- `IssueTime` = **17:32:00+00:00**  
  The time the sender's system issued the document, in the sender's local time; in the issuer's local time, with its offset from UTC.
- `TypeCode` = **IMPORT** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode`)  
  An import declaration. The code is from the Trade Accord's customs declaration type list: IMPORT = Import declaration.
- `SubTypeCode` = **FREECIRC** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationSubTypeCode`)  
  For release into free circulation. The code is from the Trade Accord's customs declaration subtype list: FREECIRC = Release for free circulation.
- `NatureOfTransactionCode` = **PURCHASE** (listID `urn:ubl-examples:world:codelist:NatureOfTransactionCode`)  
  The goods were bought. The code is from the Trade Accord's nature of transaction list: PURCHASE = Outright purchase or sale.
- `Note` = **Lelaha namafe: liape mutaki Accord lanate. Musaka mofilufo vukape: 10 % mutaki tafone venete mutaki 11,547.200 venamo, 1,154.720 venamo. Lavamu tilasi letasi famima: tivufo tiava limana lavamu vevisi metolike pehaka tavase tokita.** (languageID `qal`)  
  The note in Lisavan, the sender's language: What is due at import, by the importing country's rule.
- `Note` = **No duty: goods of Accord origin. Import consumption tax: 10 % of the landed value of 11,547.200 coral, 1,154.720 coral. Food pays it too: the island taxes imported food to encourage its own farms.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: What is due at import, by the importing country's rule.
- `VersionID` = **1**  
  The first version.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-04-24**  
  Lodged before the goods arrive.
- `EndDate` = **2026-05-24**  
  A declaration lodged before arrival lapses if the goods are not presented to customs within 30 days.

### Jurisdiction Region Address

Inside `JurisdictionRegionAddress`:

- `Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The customs territory of import. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Hafefo Fresh Produce gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-043529** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Hafefo Fresh Produce gives it.
- `PartyName/Name` = **Hafefo Fresh Produce**  
  The trading name; as Hafefo Fresh Produce gives it.
- `Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/ID` = **40618392** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Hafefo Fresh Produce gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Hafefo Fresh Produce gives it.
- `PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Hafefo Fresh Produce gives it.
- `PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. as Hafefo Fresh Produce gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. as Hafefo Fresh Produce gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. as Hafefo Fresh Produce gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Hafefo Fresh Produce Ltd**  
  The name under which the party is registered, with its legal form; as Hafefo Fresh Produce gives it.
- `PartyLegalEntity/CompanyID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; as Hafefo Fresh Produce gives it. The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Hafefo Fresh Produce gives it.
- `Contact/JobTitle` = **Import clerk**  
  The job of the person who answers at the desk; as Hafefo Fresh Produce gives it.
- `Contact/Department` = **Purchasing**  
  The department the desk belongs to; as Hafefo Fresh Produce gives it.
- `Contact/Telephone` = **+999 3 726 8104**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. as Hafefo Fresh Produce gives it.
- `Contact/ElectronicMail` = **customs@hafefo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Hafefo Fresh Produce gives it.
- `Contact/Note` = **Monday to Saturday 05:00–14:00**  
  When the desk can be reached; as Hafefo Fresh Produce gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC43529** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Hafefo Fresh Produce gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Harrowmead Fruit Growers gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9527430900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Harrowmead Fruit Growers gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-415873** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Harrowmead Fruit Growers gives it.
- `PartyName/Name` = **Harrowmead Fruit Growers**  
  The trading name; as Harrowmead Fruit Growers gives it.
- `PostalAddress/ID` = **UL-ADR-418726** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Harrowmead Fruit Growers gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Orchard Road**  
  Street of the postal address. as Harrowmead Fruit Growers gives it.
- `PostalAddress/BuildingNumber` = **3**  
  Building number of the postal address. as Harrowmead Fruit Growers gives it.
- `PostalAddress/CityName` = **Harrowmead**  
  The town or locality nearest to the party's place on the map, in its own country and state. as Harrowmead Fruit Growers gives it.
- `PostalAddress/PostalZone` = **71640**  
  Postal code in Bayvarra's format (5 digits). as Harrowmead Fruit Growers gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. as Harrowmead Fruit Growers gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Hafefo Fresh Produce**  
  The same party as at ImporterParty, where its full details are given; only its identifier and name are repeated.

### Customs Party

Inside `CustomsParty`:

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
  Building number of the postal address. as Island Customs Service gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. as Island Customs Service gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. as Island Customs Service gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Island Customs Service**  
  The public body's official name; as Island Customs Service gives it.
- `PartyLegalEntity/CompanyID` = **GOV-118** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  Number in the Government list of public bodies of Lisavu, which gives every public body a number of its own (GOV- and 3 digits), derived from no other register ; as Island Customs Service gives it. The schemeID names the scheme it is from: the government list of public bodies of Lisavu (GOV- and 3 digits).
- `Contact/Name` = **Import office**  
  The party's import office desk: the desk for its role in this document (an import); as Island Customs Service gives it.
- `Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; as Island Customs Service gives it.
- `Contact/Department` = **Customs**  
  The department the desk belongs to; as Island Customs Service gives it.
- `Contact/Telephone` = **+999 3 728 6449**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. as Island Customs Service gives it.
- `Contact/ElectronicMail` = **import@customs-xl.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Island Customs Service gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Island Customs Service gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:GOV-118** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Government list of public bodies of Lisavu; as Island Customs Service gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **HFG-SH-26-0556**  
  The shipment declared.
- `TotalTransportHandlingUnitQuantity` = **20** (unitCode `EA`)  
  The pallets the goods travel on.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Apples Gala, carton 18 kg, count 100**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **6988.800** (currencyID `XLC`)  
  The customs value in coral: the fruit's landed value in lume, its CIP price, at the world's reference rate (1 lume = 0.4 coral).
- `GoodsItem/GrossWeightMeasure` = **13036.8** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **672** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **P** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XB origin under the Trade Accord, by this criterion: the preference claimed, free of duty. The code is from the Trade Accord's preference criterion list: P = Wholly obtained.
- `GoodsItem/Item/Description` = **Apples of the variety Gala, Class I, 100 fruit to an 18 kg carton, on trays; picked in February and March and kept in the cooperative's cold store.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Apples Gala, carton 18 kg, count 100**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **II** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: II = Vegetable products.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **080810** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080810 = Apples, fresh.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01341** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 01341 = Apples.
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  The island's import consumption tax applies. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **10**  
  Its rate, on the landed value.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **IMP** (schemeID `UN/EDIFACT EDED 5153`)  
  The island's import consumption tax, as the world codes it. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: IMP = Import tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/TaxTypeCode` = **CONSUMPTION** (listID `urn:ubl-examples:world:codelist:TaxTypeCode`)  
  A tax on consumption, charged at import. The code is from the Trade Accord's tax type list: CONSUMPTION = Tax on consumption.
- `GoodsItem/Item/OriginAddress/District` = **Harrowmead, Upland State**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Apples Granny Smith, carton 18 kg, count 100**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **2744.000** (currencyID `XLC`)  
  The customs value in coral: the fruit's landed value in lume, its CIP price, at the world's reference rate (1 lume = 0.4 coral).
- `GoodsItem/GrossWeightMeasure` = **5432** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **280** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **P** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XB origin under the Trade Accord, by this criterion: the preference claimed, free of duty. The code is from the Trade Accord's preference criterion list: P = Wholly obtained.
- `GoodsItem/Item/Description` = **Apples of the variety Granny Smith, Class I, 100 fruit to an 18 kg carton, on trays; picked in April, the season's late variety.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Apples Granny Smith, carton 18 kg, count 100**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **II** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: II = Vegetable products.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **080810** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080810 = Apples, fresh.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01341** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 01341 = Apples.
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  The island's import consumption tax applies. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **10**  
  Its rate, on the landed value.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **IMP** (schemeID `UN/EDIFACT EDED 5153`)  
  The island's import consumption tax, as the world codes it. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: IMP = Import tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/TaxTypeCode` = **CONSUMPTION** (listID `urn:ubl-examples:world:codelist:TaxTypeCode`)  
  A tax on consumption, charged at import. The code is from the Trade Accord's tax type list: CONSUMPTION = Tax on consumption.
- `GoodsItem/Item/OriginAddress/District` = **Harrowmead, Upland State**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/ID` = **3**  
  The goods item number.
- `GoodsItem/Description` = **Pears Packham's Triumph, carton 18 kg, count 80**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **1814.400** (currencyID `XLC`)  
  The customs value in coral: the fruit's landed value in lume, its CIP price, at the world's reference rate (1 lume = 0.4 coral).
- `GoodsItem/GrossWeightMeasure` = **3259.2** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **168** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/PreferenceCriterionCode` = **P** (listID `urn:ubl-examples:world:codelist:PreferenceCriterionCode`)  
  The goods are of XB origin under the Trade Accord, by this criterion: the preference claimed, free of duty. The code is from the Trade Accord's preference criterion list: P = Wholly obtained.
- `GoodsItem/Item/Description` = **Pears of the variety Packham's Triumph, Class I, 80 fruit to an 18 kg carton, on trays; picked in March and kept in the cooperative's cold store.**  
  The seller's description.
- `GoodsItem/Item/Name` = **Pears Packham's Triumph, carton 18 kg, count 80**  
  The item's short name.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **II** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: II = Vegetable products.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **080830** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080830 = Pears, fresh.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01342** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Harrowmead Fruit Growers describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 01342 = Pears and quinces.
- `GoodsItem/Item/ClassifiedTaxCategory/ID` = **S** (schemeID `UN/EDIFACT EDED 5305`)  
  The island's import consumption tax applies. The code is from the world's copy of UN/EDIFACT 5305 Duty or tax or fee category: S = Standard rate. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/Percent` = **10**  
  Its rate, on the landed value.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/ID` = **IMP** (schemeID `UN/EDIFACT EDED 5153`)  
  The island's import consumption tax, as the world codes it. The code is from the world's copy of UN/EDIFACT 5153 Duty or tax or fee type name: IMP = Import tax. An identifier that holds a code names the code's list in its schemeID.
- `GoodsItem/Item/ClassifiedTaxCategory/TaxScheme/TaxTypeCode` = **CONSUMPTION** (listID `urn:ubl-examples:world:codelist:TaxTypeCode`)  
  A tax on consumption, charged at import. The code is from the Trade Accord's tax type list: CONSUMPTION = Tax on consumption.
- `GoodsItem/Item/OriginAddress/District` = **Harrowmead, Upland State**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by sea. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **TOL-BL-26-0562**  
  The bill of lading of the reefer.
- `DocumentTypeCode` = **BillOfLading** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: TOL-BL-26-0562 is the example reefer/07, a BillOfLading; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: BillOfLading = Bill Of Lading.
- `ID` = **FDAB-GC-26-0558**  
  The phytosanitary certificate made out for the island, on which the release of the fruit under its plant health rules depends.
- `DocumentTypeCode` = **GoodsCertificate** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: FDAB-GC-26-0558 is the example reefer/04, a GoodsCertificate; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: GoodsCertificate = Goods Certificate.
- `ID` = **BF-EX-26-0559**  
  The export declaration of the goods in the country of departure, for information.
- `DocumentTypeCode` = **ExportCustomsDeclaration** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: BF-EX-26-0559 is the example reefer/05, a ExportCustomsDeclaration; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: ExportCustomsDeclaration = Export Customs Declaration.
- `ID` = **HFG-INV-26-0563**  
  The commercial invoice the customs value rests on; its statement on origin is the proof of origin the preference claim refers to.
- `DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: HFG-INV-26-0563 is the example reefer/08, a Invoice; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Invoice.

### Signature

Inside `Signature`:

- `ID` = **HFP-SIG-IM-reefer**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Hafefo Fresh Produce**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ImportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ImportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:import-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>REEFER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>HFP-IM-26-0564</cbc:ID>
  <cbc:UUID>04b3c1d3-d600-57c6-b790-ffbf27e1ac34</cbc:UUID>
  <cbc:IssueDate>2026-04-24</cbc:IssueDate>
  <cbc:IssueTime>17:32:00+00:00</cbc:IssueTime>
  <cbc:TypeCode listID="urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode">IMPORT</cbc:TypeCode>
  <cbc:SubTypeCode listID="urn:ubl-examples:world:codelist:CustomsDeclarationSubTypeCode">FREECIRC</cbc:SubTypeCode>
  <cbc:NatureOfTransactionCode listID="urn:ubl-examples:world:codelist:NatureOfTransactionCode">PURCHASE</cbc:NatureOfTransactionCode>
  <cbc:Note languageID="qal">Lelaha namafe: liape mutaki Accord lanate. Musaka mofilufo vukape: 10 % mutaki tafone venete mutaki 11,547.200 venamo, 1,154.720 venamo. Lavamu tilasi letasi famima: tivufo tiava limana lavamu vevisi metolike pehaka tavase tokita.</cbc:Note>
  <cbc:Note languageID="en-XL">No duty: goods of Accord origin. Import consumption tax: 10 % of the landed value of 11,547.200 coral, 1,154.720 coral. Food pays it too: the island taxes imported food to encourage its own farms.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-04-24</cbc:StartDate>
    <cbc:EndDate>2026-05-24</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:JurisdictionRegionAddress>
    <cac:Country>
      <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
    </cac:Country>
  </cac:JurisdictionRegionAddress>
  <cac:ImporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-043529</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Hafefo Fresh Produce</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40618392</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Vosapi Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>58</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Hafefo Fresh Produce Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Import clerk</cbc:JobTitle>
      <cbc:Department>Purchasing</cbc:Department>
      <cbc:Telephone>+999 3 726 8104</cbc:Telephone>
      <cbc:ElectronicMail>customs@hafefo.example</cbc:ElectronicMail>
      <cbc:Note>Monday to Saturday 05:00–14:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC43529</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9527430900003</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-415873</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-418726</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Orchard Road</cbc:StreetName>
      <cbc:BuildingNumber>3</cbc:BuildingNumber>
      <cbc:CityName>Harrowmead</cbc:CityName>
      <cbc:PostalZone>71640</cbc:PostalZone>
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
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Hafefo Fresh Produce</cbc:Name>
    </cac:PartyName>
  </cac:ConsigneeParty>
  <cac:CustomsParty>
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
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Island Customs Service</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-118</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Import office</cbc:Name>
      <cbc:JobTitle>Customs officer</cbc:JobTitle>
      <cbc:Department>Customs</cbc:Department>
      <cbc:Telephone>+999 3 728 6449</cbc:Telephone>
      <cbc:ElectronicMail>import@customs-xl.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:GOV-118</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:CustomsParty>
  <cac:Shipment>
    <cbc:ID>HFG-SH-26-0556</cbc:ID>
    <cbc:TotalTransportHandlingUnitQuantity unitCode="EA">20</cbc:TotalTransportHandlingUnitQuantity>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Apples Gala, carton 18 kg, count 100</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XLC">6988.800</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">13036.8</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">672</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">P</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description>Apples of the variety Gala, Class I, 100 fruit to an 18 kg carton, on trays; picked in February and March and kept in the cooperative's cold store.</cbc:Description>
        <cbc:Name>Apples Gala, carton 18 kg, count 100</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">II</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">080810</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">01341</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ClassifiedTaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
          <cbc:Percent>10</cbc:Percent>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">IMP</cbc:ID>
            <cbc:TaxTypeCode listID="urn:ubl-examples:world:codelist:TaxTypeCode">CONSUMPTION</cbc:TaxTypeCode>
          </cac:TaxScheme>
        </cac:ClassifiedTaxCategory>
        <cac:OriginAddress>
          <cbc:District>Harrowmead, Upland State</cbc:District>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:OriginAddress>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Description>Apples Granny Smith, carton 18 kg, count 100</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XLC">2744.000</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">5432</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">280</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">P</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description>Apples of the variety Granny Smith, Class I, 100 fruit to an 18 kg carton, on trays; picked in April, the season's late variety.</cbc:Description>
        <cbc:Name>Apples Granny Smith, carton 18 kg, count 100</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">II</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">080810</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">01341</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ClassifiedTaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
          <cbc:Percent>10</cbc:Percent>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">IMP</cbc:ID>
            <cbc:TaxTypeCode listID="urn:ubl-examples:world:codelist:TaxTypeCode">CONSUMPTION</cbc:TaxTypeCode>
          </cac:TaxScheme>
        </cac:ClassifiedTaxCategory>
        <cac:OriginAddress>
          <cbc:District>Harrowmead, Upland State</cbc:District>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:OriginAddress>
      </cac:Item>
    </cac:GoodsItem>
    <cac:GoodsItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Description>Pears Packham's Triumph, carton 18 kg, count 80</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XLC">1814.400</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">3259.2</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">168</cbc:Quantity>
      <cbc:PreferenceCriterionCode listID="urn:ubl-examples:world:codelist:PreferenceCriterionCode">P</cbc:PreferenceCriterionCode>
      <cac:Item>
        <cbc:Description>Pears of the variety Packham's Triumph, Class I, 80 fruit to an 18 kg carton, on trays; picked in March and kept in the cooperative's cold store.</cbc:Description>
        <cbc:Name>Pears Packham's Triumph, carton 18 kg, count 80</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">II</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">080830</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">01342</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:ClassifiedTaxCategory>
          <cbc:ID schemeID="UN/EDIFACT EDED 5305">S</cbc:ID>
          <cbc:Percent>10</cbc:Percent>
          <cac:TaxScheme>
            <cbc:ID schemeID="UN/EDIFACT EDED 5153">IMP</cbc:ID>
            <cbc:TaxTypeCode listID="urn:ubl-examples:world:codelist:TaxTypeCode">CONSUMPTION</cbc:TaxTypeCode>
          </cac:TaxScheme>
        </cac:ClassifiedTaxCategory>
        <cac:OriginAddress>
          <cbc:District>Harrowmead, Upland State</cbc:District>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:OriginAddress>
      </cac:Item>
    </cac:GoodsItem>
    <cac:ShipmentStage>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:AdditionalDocumentReference>
    <cbc:ID>TOL-BL-26-0562</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">BillOfLading</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>FDAB-GC-26-0558</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">GoodsCertificate</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>BF-EX-26-0559</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ExportCustomsDeclaration</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>HFG-INV-26-0563</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>HFP-SIG-IM-reefer</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Hafefo Fresh Produce</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ImportCustomsDeclaration>
```
