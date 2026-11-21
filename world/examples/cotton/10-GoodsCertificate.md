# Goods Certificate: Department of Agriculture of Lisavu to Selanu Cotton Ginnery

*Example 10 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Goods Certificate in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-GOODS-CERTIFICATE-SCHEMA)*

The Plant Protection Service of Lisavu's Department of Agriculture inspects the bales and certifies them free of the pests Bayvarra names, at the ginnery's application.

[The XML file](10-GoodsCertificate.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:goods-certificate:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Goods certificate". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **SCG-TX-26-0239**  
  The collaboration this document belongs to: the ginnery's application for the phytosanitary certificate of the bales, to its issue. Selanu Cotton Ginnery started it and gave it this identifier, which every document of it repeats.
- `ID` = **DAL/2026/0309**  
  The Plant Protection Service's certificate number.
- `UUID` = **78516adf-5718-5e78-bd9d-8e44536e335b**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-05**  
  Issued after the inspection at the ginnery, before shipment, at the ginnery's application.
- `IssueTime` = **14:43:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `TypeCode` = **PHYTO** (listID `urn:ubl-examples:world:codelist:GoodsCertificateTypeCode`)  
  A plant health certificate for the cotton. The code is from the Trade Accord's goods certificate type list: PHYTO = Phytosanitary certificate.
- `Description` = **The ginned cotton is free of the pests named by Bayvarra's plant health rules.**  
  What it certifies.
- `Note` = **Helatasa momai kelalahu filumuve.** (languageID `qal`)  
  The note in Lisavan, the sender's language: Where.
- `Note` = **Inspected at the ginnery's warehouse.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: Where.
- `VersionID` = **1**  
  The first version.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-05-05**  
  From the inspection.
- `EndDate` = **2026-05-19**  
  For two weeks: the bales must ship by then.

### Applicable Territory Address

Inside `ApplicableTerritoryAddress`:

- `Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  For import into Bayvarra. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Cotton Ginnery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-042681** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Selanu Cotton Ginnery gives it.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; as Selanu Cotton Ginnery gives it.
- `PostalAddress/ID` = **23618907** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Selanu Cotton Ginnery gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Tikesa Luhate Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Selanu Cotton Ginnery gives it.
- `PostalAddress/StreetName` = **Gin Yard Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Selanu Cotton Ginnery gives it.
- `PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address. As Selanu Cotton Ginnery gives it.
- `PostalAddress/CityName` = **Pakesa** (languageID `qal`)  
  The place's Lisavan name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Cotton Ginnery gives it.
- `PostalAddress/CityName` = **Bollworth** (languageID `en-XL`)  
  The place's English name, which its English settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Selanu Cotton Ginnery gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Selanu Cotton Ginnery Ltd**  
  The name under which the party is registered, with its legal form; as Selanu Cotton Ginnery gives it.
- `PartyLegalEntity/CompanyID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  Number in the Island companies register; as Selanu Cotton Ginnery gives it. The schemeID names the scheme it is from: the Island companies register (IC and 5 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Selanu Cotton Ginnery gives it.
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Selanu Cotton Ginnery gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Selanu Cotton Ginnery gives it.
- `Contact/Telephone` = **+999 3 721 0486**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Selanu Cotton Ginnery gives it.
- `Contact/ElectronicMail` = **customs@selanuginnery.example**  
  The contact's e-mail address; as Selanu Cotton Ginnery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Selanu Cotton Ginnery gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Cotton Ginnery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importer Party

Inside `ImporterParty`:

- `PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeport Textile Mill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9524010900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeport Textile Mill gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-412603** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Lumeport Textile Mill gives it.
- `PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; as Lumeport Textile Mill gives it.
- `PostalAddress/ID` = **LUM-ADR-933254** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Textile Mill gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address. As Lumeport Textile Mill gives it.
- `PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address. As Lumeport Textile Mill gives it.
- `PostalAddress/CitySubdivisionName` = **Mill Quarter**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Lumeport Textile Mill gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeport Textile Mill gives it.
- `PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits). As Lumeport Textile Mill gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeport Textile Mill gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.

### Warehouse Party

Inside `WarehouseParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.

### Consignee Party

Inside `ConsigneeParty`:

- `PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.

### Issuer Party

Inside `IssuerParty`:

- `PartyIdentification/ID` = **GOV-206** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Department of Agriculture of Lisavu gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Department of Agriculture of Lisavu**  
  The trading name; as Department of Agriculture of Lisavu gives it.
- `Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: kopele.
- `PostalAddress/ID` = **71826543** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Department of Agriculture of Lisavu gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Department of Agriculture of Lisavu gives it.
- `PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Department of Agriculture of Lisavu gives it.
- `PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. As Department of Agriculture of Lisavu gives it.
- `PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Department of Agriculture of Lisavu gives it.
- `PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Department of Agriculture of Lisavu gives it.
- `PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Department of Agriculture of Lisavu**  
  The public body's official name; as Department of Agriculture of Lisavu gives it.
- `PartyLegalEntity/CompanyID` = **GOV-206** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  Number in the Government list of public bodies of Lisavu, which gives every public body a number of its own (GOV- and 3 digits), derived from no other register ; as Department of Agriculture of Lisavu gives it. The schemeID names the scheme it is from: the government list of public bodies of Lisavu (GOV- and 3 digits).
- `Contact/Name` = **Export certification**  
  The party's main desk, which handles this document; as Department of Agriculture of Lisavu gives it.
- `Contact/JobTitle` = **Plant health inspector**  
  The job of the person who answers at the desk; as Department of Agriculture of Lisavu gives it.
- `Contact/Department` = **Plant Protection Service**  
  The department the desk belongs to; as Department of Agriculture of Lisavu gives it.
- `Contact/Telephone` = **+999 3 724 1958**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Department of Agriculture of Lisavu gives it.
- `Contact/ElectronicMail` = **phyto@agriculture-xl.example**  
  The contact's e-mail address; as Department of Agriculture of Lisavu gives it.
- `Contact/Note` = **Weekdays 07:30–16:00**  
  When the desk can be reached; as Department of Agriculture of Lisavu gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:GOV-206** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Government list of public bodies of Lisavu; as Department of Agriculture of Lisavu gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Applicant Party

Inside `ApplicantParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **SCG-SH-26-0218**  
  The shipment certified.
- `Consignment/ID` = **7300013298**  
  The consignment, as the mill's forwarding instructions number it.
- `Consignment/TotalPackagesQuantity` = **27** (unitCode `EA`)  
  The bales the certificate covers: a plant health certificate states the number of packages.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Cotton lint, compressed bale**  
  What the goods are, in words.
- `GoodsItem/GrossWeightMeasure` = **6190.29** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `GoodsItem/Quantity` = **6129** (unitCode `KGM`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Nipupe tekapa suhema, hivile lakati vapene vilofo, tefata lafatite sefeta mutaki katani 227 kg.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language.
- `GoodsItem/Item/Description` = **Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries.
- `GoodsItem/Item/Name` = **Tekapa suhema, lafatite senehu** (languageID `qal`)  
  The item's name in Lisavan, the seller's language.
- `GoodsItem/Item/Name` = **Cotton lint, compressed bale** (languageID `en-XL`)  
  The item's name in English, the working language between the countries.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Where the item was produced; as Selanu Cotton Ginnery describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `GoodsItem/Item/CommodityClassification/NatureCode` = **XI** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XI = Textiles and textile articles.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **520100** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Selanu Cotton Ginnery describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 520100 = Cotton, not carded or combed.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Selanu Cotton Ginnery describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 01921 = Cotton, whether or not ginned.
- `GoodsItem/Item/OriginAddress/District` = **North coast**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `GoodsItem/ContainingPackage/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The goods travel in 27 of them, the consignment's package count. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.

### Attestation

Inside `Attestation`:

- `ID` = **DAL/2026/0308**  
  The inspector's attestation.
- `Name` = **Freedom from pests**  
  What is attested.
- `Description` = **Sampled and found free of boll weevil and pink bollworm.**  
  In words.
- `Note` = **10 bales sampled out of 27.**  
  The sample, out of the bales of the shipment.
- `AcceptanceIndicator` = **true**  
  Accepted.
- `ValidityPeriod/EndDate` = **2026-05-19**  
  As the certificate.
- `IssuerParty/PartyIdentification/ID` = **GOV-206** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuerParty/PartyName/Name` = **Department of Agriculture of Lisavu**  
  A party referred to from another party's details: its identifier and name are enough.
- `AttestationLine/ID` = **1**  
  The pest checked.
- `AttestationLine/TypeCode` = **PEST** (listID `urn:ubl-examples:world:codelist:AttestationTypeCode`)  
  A pest check. The code is from the Trade Accord's attestation type list: PEST = Pest check.
- `AttestationLine/Description` = **Boll weevil: none found.**  
  The finding.
- `AttestationLine/CriterionItem/ID` = **XB-PH-07**  
  Bayvarra's rule.
- `AttestationLine/CriterionItem/CriterionDescription` = **No live insects in a sample of 10 bales.**  
  The criterion.
- `AttestationLine/CriterionItem/DeclaredPropertyItem/Name` = **Cotton lint, compressed bale**  
  The goods it is about.
- `AttestationLine/SubAttestationLine/ID` = **1.1**  
  The second pest.
- `AttestationLine/SubAttestationLine/Description` = **Pink bollworm: none found.**  
  The finding.

### Goods Processing

Inside `GoodsProcessing`:

- `ID` = **SCG-PROC-26**  
  The processing on the island.
- `TypeCode` = **GINNING** (listID `urn:ubl-examples:world:codelist:GoodsProcessingTypeCode`)  
  The cotton was ginned. The code is from the Trade Accord's goods processing type list: GINNING = Ginning.
- `Description` = **Ginned, cleaned and pressed into bales.**  
  In words.
- `Note` = **At the Selanu cotton ginnery.**  
  Where.
- `Period/StartDate` = **2026-03-23**  
  The ginning and pressing of the 27 bales, in three pressing runs of the harvest, from 23 March.
- `Period/EndDate` = **2026-04-17**  
  The last run, on 17 April, before the chamber classed the lot on 20 April.
- `ProcessingParty/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ProcessingParty/PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.
- `CriterionItem/CriterionDescription` = **Seed removed; lint only.**  
  What processing the rule requires.
- `CriterionItem/DeclaredPropertyItem/Name` = **Cotton lint**  
  The goods.
- `SubGoodsProcessing/TypeCode` = **PRESSING** (listID `urn:ubl-examples:world:codelist:GoodsProcessingTypeCode`)  
  Pressed into bales. The code is from the Trade Accord's goods processing type list: PRESSING = Pressing.
- `SubGoodsProcessing/Description` = **Bales of about 227 kg.**  
  In words.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **4500013293**  
  The mill's order.
- `DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 4500013293 is the example cotton/08, a Order; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Order.

### Signature

Inside `Signature`:

- `ID` = **DAL-SIG-26-PH**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **GOV-206** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Department of Agriculture of Lisavu**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<GoodsCertificate xmlns="urn:oasis:names:specification:ubl:schema:xsd:GoodsCertificate-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:goods-certificate:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SCG-TX-26-0239</cbc:ProfileExecutionID>
  <cbc:ID>DAL/2026/0309</cbc:ID>
  <cbc:UUID>78516adf-5718-5e78-bd9d-8e44536e335b</cbc:UUID>
  <cbc:IssueDate>2026-05-05</cbc:IssueDate>
  <cbc:IssueTime>14:43:00+00:00</cbc:IssueTime>
  <cbc:TypeCode listID="urn:ubl-examples:world:codelist:GoodsCertificateTypeCode">PHYTO</cbc:TypeCode>
  <cbc:Description>The ginned cotton is free of the pests named by Bayvarra's plant health rules.</cbc:Description>
  <cbc:Note languageID="qal">Helatasa momai kelalahu filumuve.</cbc:Note>
  <cbc:Note languageID="en-XL">Inspected at the ginnery's warehouse.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-05-05</cbc:StartDate>
    <cbc:EndDate>2026-05-19</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ApplicableTerritoryAddress>
    <cac:Country>
      <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
    </cac:Country>
  </cac:ApplicableTerritoryAddress>
  <cac:ExporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-042681</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">23618907</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Tikesa Luhate Natii</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Gin Yard Road</cbc:StreetName>
      <cbc:BuildingNumber>42</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Pakesa</cbc:CityName>
      <cbc:CityName languageID="en-XL">Bollworth</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Selanu Cotton Ginnery Ltd</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 3 721 0486</cbc:Telephone>
      <cbc:ElectronicMail>customs@selanuginnery.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:ImporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9524010900002</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412603</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Textile Mill</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-933254</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Mill Street</cbc:StreetName>
      <cbc:BuildingNumber>21</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Mill Quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38504</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ImporterParty>
  <cac:WarehouseParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:WarehouseParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Textile Mill</cbc:Name>
    </cac:PartyName>
  </cac:ConsigneeParty>
  <cac:IssuerParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-206</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Department of Agriculture of Lisavu</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">71826543</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
      <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>44</cbc:BuildingNumber>
      <cbc:CityName languageID="qal">Selanu</cbc:CityName>
      <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
      <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Department of Agriculture of Lisavu</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-206</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Export certification</cbc:Name>
      <cbc:JobTitle>Plant health inspector</cbc:JobTitle>
      <cbc:Department>Plant Protection Service</cbc:Department>
      <cbc:Telephone>+999 3 724 1958</cbc:Telephone>
      <cbc:ElectronicMail>phyto@agriculture-xl.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 07:30–16:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:GOV-206</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:IssuerParty>
  <cac:ApplicantParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:ApplicantParty>
  <cac:Shipment>
    <cbc:ID>SCG-SH-26-0218</cbc:ID>
    <cac:Consignment>
      <cbc:ID>7300013298</cbc:ID>
      <cbc:TotalPackagesQuantity unitCode="EA">27</cbc:TotalPackagesQuantity>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Cotton lint, compressed bale</cbc:Description>
      <cbc:GrossWeightMeasure unitCode="KGM">6190.29</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="KGM">6129</cbc:Quantity>
      <cac:Item>
        <cbc:Description languageID="qal">Nipupe tekapa suhema, hivile lakati vapene vilofo, tefata lafatite sefeta mutaki katani 227 kg.</cbc:Description>
        <cbc:Description languageID="en-XL">Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.</cbc:Description>
        <cbc:Name languageID="qal">Tekapa suhema, lafatite senehu</cbc:Name>
        <cbc:Name languageID="en-XL">Cotton lint, compressed bale</cbc:Name>
        <cac:OriginCountry>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:NatureCode listID="WCO HS 2022 Sections">XI</cbc:NatureCode>
          <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
          <cbc:CommodityCode listID="WCO HS 2022">520100</cbc:CommodityCode>
          <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">01921</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:OriginAddress>
          <cbc:District>North coast</cbc:District>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:OriginAddress>
      </cac:Item>
      <cac:ContainingPackage>
        <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BL</cbc:PackagingTypeCode>
      </cac:ContainingPackage>
    </cac:GoodsItem>
  </cac:Shipment>
  <cac:Attestation>
    <cbc:ID>DAL/2026/0308</cbc:ID>
    <cbc:Name>Freedom from pests</cbc:Name>
    <cbc:Description>Sampled and found free of boll weevil and pink bollworm.</cbc:Description>
    <cbc:Note>10 bales sampled out of 27.</cbc:Note>
    <cbc:AcceptanceIndicator>true</cbc:AcceptanceIndicator>
    <cac:ValidityPeriod>
      <cbc:EndDate>2026-05-19</cbc:EndDate>
    </cac:ValidityPeriod>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-206</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Department of Agriculture of Lisavu</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
    <cac:AttestationLine>
      <cbc:ID>1</cbc:ID>
      <cbc:TypeCode listID="urn:ubl-examples:world:codelist:AttestationTypeCode">PEST</cbc:TypeCode>
      <cbc:Description>Boll weevil: none found.</cbc:Description>
      <cac:CriterionItem>
        <cbc:ID>XB-PH-07</cbc:ID>
        <cbc:CriterionDescription>No live insects in a sample of 10 bales.</cbc:CriterionDescription>
        <cac:DeclaredPropertyItem>
          <cbc:Name>Cotton lint, compressed bale</cbc:Name>
        </cac:DeclaredPropertyItem>
      </cac:CriterionItem>
      <cac:SubAttestationLine>
        <cbc:ID>1.1</cbc:ID>
        <cbc:Description>Pink bollworm: none found.</cbc:Description>
      </cac:SubAttestationLine>
    </cac:AttestationLine>
  </cac:Attestation>
  <cac:GoodsProcessing>
    <cbc:ID>SCG-PROC-26</cbc:ID>
    <cbc:TypeCode listID="urn:ubl-examples:world:codelist:GoodsProcessingTypeCode">GINNING</cbc:TypeCode>
    <cbc:Description>Ginned, cleaned and pressed into bales.</cbc:Description>
    <cbc:Note>At the Selanu cotton ginnery.</cbc:Note>
    <cac:Period>
      <cbc:StartDate>2026-03-23</cbc:StartDate>
      <cbc:EndDate>2026-04-17</cbc:EndDate>
    </cac:Period>
    <cac:ProcessingParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:ProcessingParty>
    <cac:CriterionItem>
      <cbc:CriterionDescription>Seed removed; lint only.</cbc:CriterionDescription>
      <cac:DeclaredPropertyItem>
        <cbc:Name>Cotton lint</cbc:Name>
      </cac:DeclaredPropertyItem>
    </cac:CriterionItem>
    <cac:SubGoodsProcessing>
      <cbc:TypeCode listID="urn:ubl-examples:world:codelist:GoodsProcessingTypeCode">PRESSING</cbc:TypeCode>
      <cbc:Description>Bales of about 227 kg.</cbc:Description>
    </cac:SubGoodsProcessing>
  </cac:GoodsProcessing>
  <cac:AdditionalDocumentReference>
    <cbc:ID>4500013293</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>DAL-SIG-26-PH</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:public-body-register">GOV-206</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Department of Agriculture of Lisavu</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</GoodsCertificate>
```
