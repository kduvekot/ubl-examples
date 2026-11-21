# Export Customs Declaration: Selanu Cotton Ginnery to Island Customs Service

*Example 11 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Export Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXPORT-CUSTOMS-DECLARATION-SCHEMA)*

The island's export: the ginnery declares the bales to customs.

[The XML file](11-ExportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:export-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Export customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **SCG-TX-26-0241**  
  The collaboration this document belongs to: the ginnery's export declaration of the bales, to their release for export. Selanu Cotton Ginnery started it and gave it this identifier, which every document of it repeats.
- `ID` = **SCG-EX-26-0049**  
  The exporter's reference.
- `UUID` = **f5f1bfda-9201-580a-8a6a-bce4e1381b33**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-06**  
  The island's export: declared before loading.
- `IssueTime` = **13:33:00+00:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `ExportTypeCode` = **PERMANENT** (listID `urn:ubl-examples:world:codelist:ExportTypeCode`)  
  A permanent export: the goods are sold abroad. The code is from the Trade Accord's export type list: PERMANENT = Permanent export.
- `ExportReasonCode` = **SALE** (listID `urn:ubl-examples:world:codelist:ExportReasonCode`)  
  The reason: a sale to a buyer abroad. The code is from the Trade Accord's export reason list: SALE = Sale.
- `Note` = **Fevelo vueseso lasati liape matiko.** (languageID `qal`)  
  The note in Lisavan, the sender's language: How it was declared.
- `Note` = **Declared electronically before the goods leave.** (languageID `en-XL`)  
  The same note in English, the working language between the countries: How it was declared.
- `VersionID` = **1**  
  The first version.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Selanu Cotton Ginnery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-042681** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Selanu Cotton Ginnery gives it.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; as Selanu Cotton Ginnery gives it.
- `Language/ID` = **qal** (schemeID `ISO 639`)  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented. The code is from the world's copy of ISO 639 Language: qal = Lisavan. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: kopele.
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
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
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
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Selanu Cotton Ginnery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Selanu Cotton Ginnery gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Island companies register; as Selanu Cotton Ginnery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customs Declaration

Inside `CustomsDeclaration`:

- `ID` = **SCG-CD-26-0049**  
  The declaration as lodged with the customs of the exporting country.
- `FunctionCode` = **9** (listID `UN/EDIFACT EDED 1225`)  
  An original declaration, not an amendment. The code is from the world's copy of UN/EDIFACT 1225 Message function: 9 = Original.
- `ValidityPeriod/StartDate` = **2026-05-06**  
  From the declaration.
- `ValidityPeriod/DurationMeasure` = **90** (unitCode `DAY`)  
  The goods must leave within 90 days.
- `ApplicableTerritoryAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The customs territory the goods leave. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Shipment/ID` = **SCG-SH-26-0218**  
  The shipment declared.
- `Shipment/Consignment/ID` = **7300013298**  
  The consignment carried.
- `Shipment/Consignment/GrossWeightMeasure` = **6190.29** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight leaving the country.
- `Shipment/Consignment/TotalPackagesQuantity` = **27** (unitCode `EA`)  
  The number of packages declared for export: the bales.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Cotton lint, compressed bale**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **6055.452** (currencyID `XLC`)  
  The value of the bales, in coral.
- `Shipment/GoodsItem/GrossWeightMeasure` = **6190.29** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `Shipment/GoodsItem/Quantity` = **6129** (unitCode `KGM`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Nipupe tekapa suhema, hivile lakati vapene vilofo, tefata lafatite sefeta mutaki katani 227 kg.** (languageID `qal`)  
  The seller's description in Lisavan, the seller's language.
- `Shipment/GoodsItem/Item/Description` = **Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.** (languageID `en-XL`)  
  The seller's description in English, the working language between the countries.
- `Shipment/GoodsItem/Item/Name` = **Tekapa suhema, lafatite senehu** (languageID `qal`)  
  The item's name in Lisavan, the seller's language.
- `Shipment/GoodsItem/Item/Name` = **Cotton lint, compressed bale** (languageID `en-XL`)  
  The item's name in English, the working language between the countries.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Where the item was produced; as Selanu Cotton Ginnery describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **XI** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XI = Textiles and textile articles.
- `Shipment/GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **520100** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Selanu Cotton Ginnery describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 520100 = Cotton, not carded or combed.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **01921** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Selanu Cotton Ginnery describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 01921 = Cotton, whether or not ginned.
- `Shipment/GoodsItem/Item/OriginAddress/District` = **North coast**  
  The district of the island where the cotton was grown, as the farm's address names it.
- `Shipment/GoodsItem/Item/OriginAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country of origin. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `Shipment/GoodsItem/ContainingPackage/PackagingTypeCode` = **BL** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BL: bale, compressed. The goods travel in 27 of them, the consignment's package count. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BL = Bale, compressed.
- `Shipment/ShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by sea. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.
- `CustomsExitOfficeLocation/Name` = **Customs office, port of Selanu**  
  Where the goods leave the country.
- `ConsignorParty/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsignorParty/PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsigneeParty/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeport Textile Mill gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **9524010900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeport Textile Mill gives it.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-412603** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Lumeport Textile Mill gives it.
- `ConsigneeParty/PartyName/Name` = **Lumeport Textile Mill**  
  The trading name; as Lumeport Textile Mill gives it.
- `ConsigneeParty/PostalAddress/ID` = **LUM-ADR-933254** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Lumeport Textile Mill gives it.
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `ConsigneeParty/PostalAddress/StreetName` = **Mill Street**  
  Street of the postal address. As Lumeport Textile Mill gives it.
- `ConsigneeParty/PostalAddress/BuildingNumber` = **21**  
  Building number of the postal address. As Lumeport Textile Mill gives it.
- `ConsigneeParty/PostalAddress/CitySubdivisionName` = **Mill Quarter**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Lumeport Textile Mill gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeport Textile Mill gives it.
- `ConsigneeParty/PostalAddress/PostalZone` = **38504**  
  Postal code in Bayvarra's format (5 digits). As Lumeport Textile Mill gives it.
- `ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeport Textile Mill gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `CustomsParty/PartyIdentification/ID` = **GOV-118** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  The party's preferred identifier: its number in the Government list of public bodies of Lisavu; as Island Customs Service gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `CustomsParty/PartyName/Name` = **Island Customs Service**  
  The trading name; as Island Customs Service gives it.
- `CustomsParty/PostalAddress/ID` = **65334843** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Island Customs Service gives it.
- `CustomsParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CustomsParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `CustomsParty/PostalAddress/StreetName` = **Vosapi Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Island Customs Service gives it.
- `CustomsParty/PostalAddress/StreetName` = **Wharf Road** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Island Customs Service gives it.
- `CustomsParty/PostalAddress/BuildingNumber` = **53**  
  Building number of the postal address. As Island Customs Service gives it.
- `CustomsParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Island Customs Service gives it.
- `CustomsParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Island Customs Service gives it.
- `CustomsParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `CustomsParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `CustomsParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `CustomsParty/PartyLegalEntity/RegistrationName` = **Island Customs Service**  
  The public body's official name; as Island Customs Service gives it.
- `CustomsParty/PartyLegalEntity/CompanyID` = **GOV-118** (schemeID `urn:ubl-examples:world:XL:public-body-register`)  
  Number in the Government list of public bodies of Lisavu, which gives every public body a number of its own (GOV- and 3 digits), derived from no other register ; as Island Customs Service gives it. The schemeID names the scheme it is from: the government list of public bodies of Lisavu (GOV- and 3 digits).
- `CustomsParty/Contact/Name` = **Export office**  
  The party's export office desk: the desk for its role in this document (an export); as Island Customs Service gives it.
- `CustomsParty/Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; as Island Customs Service gives it.
- `CustomsParty/Contact/Department` = **Customs**  
  The department the desk belongs to; as Island Customs Service gives it.
- `CustomsParty/Contact/Telephone` = **+999 3 728 6449**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. As Island Customs Service gives it.
- `CustomsParty/Contact/ElectronicMail` = **export@customs-xl.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Island Customs Service gives it.
- `CustomsParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Island Customs Service gives it.
- `CustomsParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CustomsParty/ElectronicAddress/ElectronicAddressID` = **XL:GOV-118** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Government list of public bodies of Lisavu; as Island Customs Service gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `AdditionalDocumentReference/ID` = **4500013293**  
  The order behind the export.
- `AdditionalDocumentReference/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 4500013293 is the example cotton/08, a Order; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Order.
- `AdditionalDocumentReference/ID` = **DAL/2026/0309**  
  The phytosanitary certificate of the bales, presented with the export of plant products: the Plant Protection Service's certificate goes with the goods from export onward.
- `AdditionalDocumentReference/DocumentTypeCode` = **GoodsCertificate** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: DAL/2026/0309 is the example cotton/10, a GoodsCertificate; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: GoodsCertificate = Goods Certificate.

### Signature

Inside `Signature`:

- `ID` = **SCG-SIG-EX-cotton**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Selanu Cotton Ginnery**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ExportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ExportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:export-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SCG-TX-26-0241</cbc:ProfileExecutionID>
  <cbc:ID>SCG-EX-26-0049</cbc:ID>
  <cbc:UUID>f5f1bfda-9201-580a-8a6a-bce4e1381b33</cbc:UUID>
  <cbc:IssueDate>2026-05-06</cbc:IssueDate>
  <cbc:IssueTime>13:33:00+00:00</cbc:IssueTime>
  <cbc:ExportTypeCode listID="urn:ubl-examples:world:codelist:ExportTypeCode">PERMANENT</cbc:ExportTypeCode>
  <cbc:ExportReasonCode listID="urn:ubl-examples:world:codelist:ExportReasonCode">SALE</cbc:ExportReasonCode>
  <cbc:Note languageID="qal">Fevelo vueseso lasati liape matiko.</cbc:Note>
  <cbc:Note languageID="en-XL">Declared electronically before the goods leave.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
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
    <cac:Language>
      <cbc:ID schemeID="ISO 639">qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
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
  <cac:CustomsDeclaration>
    <cbc:ID>SCG-CD-26-0049</cbc:ID>
    <cbc:FunctionCode listID="UN/EDIFACT EDED 1225">9</cbc:FunctionCode>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-05-06</cbc:StartDate>
      <cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
    </cac:ValidityPeriod>
    <cac:ApplicableTerritoryAddress>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
      </cac:Country>
    </cac:ApplicableTerritoryAddress>
    <cac:Shipment>
      <cbc:ID>SCG-SH-26-0218</cbc:ID>
      <cac:Consignment>
        <cbc:ID>7300013298</cbc:ID>
        <cbc:GrossWeightMeasure unitCode="KGM">6190.29</cbc:GrossWeightMeasure>
        <cbc:TotalPackagesQuantity unitCode="EA">27</cbc:TotalPackagesQuantity>
      </cac:Consignment>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Cotton lint, compressed bale</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XLC">6055.452</cbc:DeclaredCustomsValueAmount>
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
      <cac:ShipmentStage>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
      </cac:ShipmentStage>
    </cac:Shipment>
    <cac:CustomsExitOfficeLocation>
      <cbc:Name>Customs office, port of Selanu</cbc:Name>
    </cac:CustomsExitOfficeLocation>
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
        <cbc:Name>Export office</cbc:Name>
        <cbc:JobTitle>Customs officer</cbc:JobTitle>
        <cbc:Department>Customs</cbc:Department>
        <cbc:Telephone>+999 3 728 6449</cbc:Telephone>
        <cbc:ElectronicMail>export@customs-xl.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:GOV-118</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CustomsParty>
    <cac:AdditionalDocumentReference>
      <cbc:ID>4500013293</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
    </cac:AdditionalDocumentReference>
    <cac:AdditionalDocumentReference>
      <cbc:ID>DAL/2026/0309</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">GoodsCertificate</cbc:DocumentTypeCode>
    </cac:AdditionalDocumentReference>
  </cac:CustomsDeclaration>
  <cac:Signature>
    <cbc:ID>SCG-SIG-EX-cotton</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ExportCustomsDeclaration>
```
