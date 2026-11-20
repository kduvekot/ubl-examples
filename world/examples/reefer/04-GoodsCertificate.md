# Goods Certificate: Federal Department of Agriculture of Bayvarra to Harrowmead Fruit Growers

*Example 4 of the flow "Apples and pears in a reefer container by sea (Bayvarra → island Lisavu)" · [Goods Certificate in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-GOODS-CERTIFICATE-SCHEMA)*

Bayvarra's plant protection organisation under the IPPC, the Plant Health Service of the federal Department of Agriculture, inspects the fruit at the packhouse and certifies it free of the pests the island names, at the cooperative's application.

[The XML file](04-GoodsCertificate.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:goods-certificate:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Goods certificate". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **REEFER-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FDAB-GC-26-0558**  
  The Plant Health Service's certificate number.
- `UUID` = **616346e3-707a-5e63-8f7d-13691b27093e**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-21**  
  Issued after the inspection at the packhouse on Tuesday 21 April, the day before loading, at the cooperative's application.
- `IssueTime` = **11:30:00-01:00**  
  When the inspector had finished the sample, late in the morning; in the issuer's local time, with its offset from UTC (D27).
- `TypeCode` = **PHYTO** (listID `urn:ubl-examples:world:codelist:GoodsCertificateTypeCode`)  
  A phytosanitary certificate for export. The code is from the Trade Accord's goods certificate type list: PHYTO = Phytosanitary certificate.
- `Description` = **The fruit has been inspected and is considered free of the quarantine pests the island names.**  
  What it certifies, in the words of the IPPC's model certificate.
- `Note` = **Inspected at the packhouse in Harrowmead before loading.**  
  Where.
- `VersionID` = **1**  
  The first version.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-04-21**  
  From the inspection.
- `EndDate` = **2026-05-05**  
  For two weeks: the fruit must ship by then.

### Applicable Territory Address

Inside `ApplicableTerritoryAddress`:

- `Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  For import into the island. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Harrowmead Fruit Growers (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9527430900003** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Harrowmead Fruit Growers (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-415873** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Harrowmead Fruit Growers (world/parties.json).
- `PartyName/Name` = **Harrowmead Fruit Growers**  
  The trading name; identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-418726** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Orchard Road**  
  Street of the postal address. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/BuildingNumber` = **3**  
  Building number of the postal address. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/CityName` = **Harrowmead**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/PostalZone` = **71640**  
  Postal code in Bayvarra's format (5 digits). identity of Harrowmead Fruit Growers (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Harrowmead Fruit Growers (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Harrowmead Fruit Growers Co-op**  
  The name under which the party is registered, with its legal form; identity of Harrowmead Fruit Growers (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Harrowmead Fruit Growers (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Sales office**  
  The party's main desk, which handles this document; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/JobTitle` = **Export sales coordinator**  
  The job of the person who answers at the desk; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Telephone` = **+999 2 7164 281 590**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/ElectronicMail` = **sales@harrowmeadfruit.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Harrowmead Fruit Growers (world/parties.json).
- `Contact/Note` = **Weekdays 07:00–16:00**  
  When the desk can be reached; identity of Harrowmead Fruit Growers (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20415873** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; identity of Harrowmead Fruit Growers (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Hafefo Fresh Produce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-043529** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Hafefo Fresh Produce (world/parties.json).
- `PartyName/Name` = **Hafefo Fresh Produce**  
  The trading name; identity of Hafefo Fresh Produce (world/parties.json).
- `PostalAddress/ID` = **40618392** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Hafefo Fresh Produce (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Hafefo Fresh Produce (world/parties.json).
- `PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; identity of Hafefo Fresh Produce (world/parties.json).
- `PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Hafefo Fresh Produce (world/parties.json).
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Hafefo Fresh Produce (world/parties.json).
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Hafefo Fresh Produce (world/parties.json).
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.

### Warehouse Party

Inside `WarehouseParty`:

- `PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Harrowmead Fruit Growers**  
  A party referred to from another party's details: its identifier and name are enough.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Harrowmead Fruit Growers**  
  A party referred to from another party's details: its identifier and name are enough.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **IC43529** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Hafefo Fresh Produce**  
  A party referred to from another party's details: its identifier and name are enough.

### Issuer Party

Inside `IssuerParty`:

- `PartyIdentification/ID` = **5946128073** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; identity of Federal Department of Agriculture of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Federal Department of Agriculture of Bayvarra**  
  The trading name; identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-582034** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Civic Square**  
  Street of the postal address. identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Government Hill**  
  The quarter of Lumeport the party is in: one of the town's districts on the map (world/map.json). identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `PostalAddress/PostalZone` = **38521**  
  Postal code in Bayvarra's format (5 digits). identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Federal Department of Agriculture of Bayvarra (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time (D27, world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Federal Department of Agriculture of Bayvarra**  
  The public body's official name; identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `PartyLegalEntity/CompanyID` = **5946128073** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register (O142); identity of Federal Department of Agriculture of Bayvarra (world/parties.json). The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `Contact/Name` = **Export certification**  
  The party's main desk, which handles this document; identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `Contact/JobTitle` = **Plant health inspector**  
  The job of the person who answers at the desk; identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `Contact/Department` = **Plant Health Service**  
  The department the desk belongs to; identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `Contact/Telephone` = **+999 2 38 6719 2485**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `Contact/ElectronicMail` = **export.certification@agriculture-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `Contact/Note` = **Weekdays 07:30–16:00**  
  When the desk can be reached; identity of Federal Department of Agriculture of Bayvarra (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:5946128073** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; identity of Federal Department of Agriculture of Bayvarra (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Applicant Party

Inside `ApplicantParty`:

- `PartyIdentification/ID` = **20415873** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Harrowmead Fruit Growers**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **HFG-SH-26-0556**  
  The shipment certified.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Apples Gala, carton 18 kg, count 100**  
  What the goods are, in words.
- `GoodsItem/GrossWeightMeasure` = **13036.8** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **672** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Apples of the variety Gala, Class I, 100 fruit to an 18 kg carton, on trays; picked in February and March and kept in the cooperative's cold store.**  
  The seller's description; item apples-gala of Harrowmead Fruit Growers (world/items.json).
- `GoodsItem/Item/Name` = **Apples Gala, carton 18 kg, count 100**  
  The item's short name; item apples-gala of Harrowmead Fruit Growers (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item apples-gala of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **II** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: II = Vegetable products.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **080810** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item apples-gala of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080810 = Apples, fresh.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01341** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item apples-gala of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 01341 = Apples.
- `GoodsItem/Item/OriginAddress/District` = **Harrowmead, Upland State**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/ID` = **2**  
  The goods item number.
- `GoodsItem/Description` = **Apples Granny Smith, carton 18 kg, count 100**  
  What the goods are, in words.
- `GoodsItem/GrossWeightMeasure` = **5432** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **280** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Apples of the variety Granny Smith, Class I, 100 fruit to an 18 kg carton, on trays; picked in April, the season's late variety.**  
  The seller's description; item apples-granny of Harrowmead Fruit Growers (world/items.json).
- `GoodsItem/Item/Name` = **Apples Granny Smith, carton 18 kg, count 100**  
  The item's short name; item apples-granny of Harrowmead Fruit Growers (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item apples-granny of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **II** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: II = Vegetable products.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **080810** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item apples-granny of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080810 = Apples, fresh.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01341** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item apples-granny of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 01341 = Apples.
- `GoodsItem/Item/OriginAddress/District` = **Harrowmead, Upland State**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/ID` = **3**  
  The goods item number.
- `GoodsItem/Description` = **Pears Packham's Triumph, carton 18 kg, count 80**  
  What the goods are, in words.
- `GoodsItem/GrossWeightMeasure` = **3259.2** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `GoodsItem/Quantity` = **168** (unitCode `EA`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Pears of the variety Packham's Triumph, Class I, 80 fruit to an 18 kg carton, on trays; picked in March and kept in the cooperative's cold store.**  
  The seller's description; item pears-packham of Harrowmead Fruit Growers (world/items.json).
- `GoodsItem/Item/Name` = **Pears Packham's Triumph, carton 18 kg, count 80**  
  The item's short name; item pears-packham of Harrowmead Fruit Growers (world/items.json).
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item pears-packham of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **II** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: II = Vegetable products.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **080830** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item pears-packham of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 080830 = Pears, fresh.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01342** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item pears-packham of Harrowmead Fruit Growers (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 01342 = Pears and quinces.
- `GoodsItem/Item/OriginAddress/District` = **Harrowmead, Upland State**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Attestation

Inside `Attestation`:

- `ID` = **FDA-ATT-26-0218**  
  The inspector's attestation.
- `Name` = **Freedom from quarantine pests**  
  What is attested.
- `Description` = **Sampled at the packhouse and found free of codling moth and fire blight.**  
  In words: the two pests of apples and pears that the island, which has neither, keeps out.
- `Note` = **Two per cent of the cartons sampled: 23 of 1,120.**  
  The sample.
- `AcceptanceIndicator` = **true**  
  Accepted.
- `IssuerParty/PartyIdentification/ID` = **5946128073** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuerParty/PartyName/Name` = **Federal Department of Agriculture of Bayvarra**  
  A party referred to from another party's details: its identifier and name are enough.
- `AttestationLine/ID` = **1**  
  The pests checked.
- `AttestationLine/TypeCode` = **PEST** (listID `urn:ubl-examples:world:codelist:AttestationTypeCode`)  
  A pest check. The code is from the Trade Accord's attestation type list: PEST = Pest check.
- `AttestationLine/Description` = **Codling moth (Cydia pomonella): none found.**  
  The finding.
- `AttestationLine/CriterionItem/ID` = **XL-PH-12**  
  The island's import rule for pome fruit.
- `AttestationLine/CriterionItem/CriterionDescription` = **No live larvae and no entry holes in a sample of 2 % of the cartons.**  
  The criterion.
- `AttestationLine/CriterionItem/DeclaredPropertyItem/Name` = **Apples and pears, fresh**  
  The goods it is about.
- `AttestationLine/SubAttestationLine/ID` = **1.1**  
  The second pest.
- `AttestationLine/SubAttestationLine/Description` = **Fire blight (Erwinia amylovora): no symptoms in the orchards of origin this season.**  
  The finding.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **HFP-PO-26-0553**  
  The wholesaler's order.
- `DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: HFP-PO-26-0553 is the example reefer/01, a Order; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Order.

### Signature

Inside `Signature`:

- `ID` = **FDA-SIG-26-PH**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **5946128073** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Federal Department of Agriculture of Bayvarra**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<GoodsCertificate xmlns="urn:oasis:names:specification:ubl:schema:xsd:GoodsCertificate-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:goods-certificate:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>REEFER-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FDAB-GC-26-0558</cbc:ID>
  <cbc:UUID>616346e3-707a-5e63-8f7d-13691b27093e</cbc:UUID>
  <cbc:IssueDate>2026-04-21</cbc:IssueDate>
  <cbc:IssueTime>11:30:00-01:00</cbc:IssueTime>
  <cbc:TypeCode listID="urn:ubl-examples:world:codelist:GoodsCertificateTypeCode">PHYTO</cbc:TypeCode>
  <cbc:Description>The fruit has been inspected and is considered free of the quarantine pests the island names.</cbc:Description>
  <cbc:Note>Inspected at the packhouse in Harrowmead before loading.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-04-21</cbc:StartDate>
    <cbc:EndDate>2026-05-05</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ApplicableTerritoryAddress>
    <cac:Country>
      <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
    </cac:Country>
  </cac:ApplicableTerritoryAddress>
  <cac:ExporterParty>
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
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Harrowmead Fruit Growers Co-op</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Sales office</cbc:Name>
      <cbc:JobTitle>Export sales coordinator</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7164 281 590</cbc:Telephone>
      <cbc:ElectronicMail>sales@harrowmeadfruit.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 07:00–16:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20415873</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
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
  </cac:ImporterParty>
  <cac:WarehouseParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
    </cac:PartyName>
  </cac:WarehouseParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC43529</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Hafefo Fresh Produce</cbc:Name>
    </cac:PartyName>
  </cac:ConsigneeParty>
  <cac:IssuerParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">5946128073</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Federal Department of Agriculture of Bayvarra</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-582034</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Civic Square</cbc:StreetName>
      <cbc:BuildingNumber>9</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Government Hill</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38521</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Federal Department of Agriculture of Bayvarra</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:public-body-register">5946128073</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Export certification</cbc:Name>
      <cbc:JobTitle>Plant health inspector</cbc:JobTitle>
      <cbc:Department>Plant Health Service</cbc:Department>
      <cbc:Telephone>+999 2 38 6719 2485</cbc:Telephone>
      <cbc:ElectronicMail>export.certification@agriculture-xb.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 07:30–16:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:5946128073</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:IssuerParty>
  <cac:ApplicantParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20415873</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Harrowmead Fruit Growers</cbc:Name>
    </cac:PartyName>
  </cac:ApplicantParty>
  <cac:Shipment>
    <cbc:ID>HFG-SH-26-0556</cbc:ID>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Apples Gala, carton 18 kg, count 100</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">13036.8</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">672</cbc:Quantity>
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
      <cbc:GrossWeightMeasure unitCode="KGM">5432</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">280</cbc:Quantity>
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
      <cbc:GrossWeightMeasure unitCode="KGM">3259.2</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="EA">168</cbc:Quantity>
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
        <cac:OriginAddress>
          <cbc:District>Harrowmead, Upland State</cbc:District>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:OriginAddress>
      </cac:Item>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:Attestation>
    <cbc:ID>FDA-ATT-26-0218</cbc:ID>
    <cbc:Name>Freedom from quarantine pests</cbc:Name>
    <cbc:Description>Sampled at the packhouse and found free of codling moth and fire blight.</cbc:Description>
    <cbc:Note>Two per cent of the cartons sampled: 23 of 1,120.</cbc:Note>
    <cbc:AcceptanceIndicator>true</cbc:AcceptanceIndicator>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">5946128073</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Federal Department of Agriculture of Bayvarra</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
    <cac:AttestationLine>
      <cbc:ID>1</cbc:ID>
      <cbc:TypeCode listID="urn:ubl-examples:world:codelist:AttestationTypeCode">PEST</cbc:TypeCode>
      <cbc:Description>Codling moth (Cydia pomonella): none found.</cbc:Description>
      <cac:CriterionItem>
        <cbc:ID>XL-PH-12</cbc:ID>
        <cbc:CriterionDescription>No live larvae and no entry holes in a sample of 2 % of the cartons.</cbc:CriterionDescription>
        <cac:DeclaredPropertyItem>
          <cbc:Name>Apples and pears, fresh</cbc:Name>
        </cac:DeclaredPropertyItem>
      </cac:CriterionItem>
      <cac:SubAttestationLine>
        <cbc:ID>1.1</cbc:ID>
        <cbc:Description>Fire blight (Erwinia amylovora): no symptoms in the orchards of origin this season.</cbc:Description>
      </cac:SubAttestationLine>
    </cac:AttestationLine>
  </cac:Attestation>
  <cac:AdditionalDocumentReference>
    <cbc:ID>HFP-PO-26-0553</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>FDA-SIG-26-PH</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">5946128073</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Federal Department of Agriculture of Bayvarra</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</GoodsCertificate>
```
