# Export Customs Declaration: Rinova Recovery to Customs Administration of Urvania

*Example 5 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Export Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXPORT-CUSTOMS-DECLARATION-SCHEMA)*

The granulate leaves Urvania; the waste processor declares the export.

[The XML file](05-ExportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:export-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Export customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **26-0451**  
  The collaboration this document belongs to: Rinova's export declaration of the granulate, to its release for export. Rinova Recovery started it and gave it this identifier, which every document of it repeats.
- `ID` = **26-0091**  
  The exporter's reference.
- `UUID` = **9d7cd654-55a1-5b6b-af72-1c8f54670605**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-20**  
  Declared the day the barge is loaded.
- `IssueTime` = **12:40:00-01:00**  
  While the bags are loaded, so that customs releases them before the barge leaves; in the issuer's local time, with its offset from UTC.
- `ExportTypeCode` = **PERMANENT** (listID `urn:ubl-examples:world:codelist:ExportTypeCode`)  
  A permanent export: the goods are sold abroad. The code is from the Trade Accord's export type list: PERMANENT = Permanent export.
- `ExportReasonCode` = **SALE** (listID `urn:ubl-examples:world:codelist:ExportReasonCode`)  
  The reason: a sale to a buyer abroad. The code is from the Trade Accord's export reason list: SALE = Sale.
- `Note` = **Tragan zunir dizek drek valnir krukek.** (languageID `qau`)  
  The note in Urvanian, the sender's language: How it was declared.
- `Note` = **Declared electronically before the goods leave.** (languageID `en-XU`)  
  The same note in English, the working language between the countries: How it was declared.
- `VersionID` = **1**  
  The first version.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Rinova Recovery gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:13362** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Rinova Recovery gives it.
- `AdditionalPartyIdentification/ID` = **XU-TR-104548** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Rinova Recovery gives it.
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; as Rinova Recovery gives it.
- `Language/ID` = **qau** (schemeID `ISO 639`)  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz). The code is from the world's copy of ISO 639 Language: qau = Urvanian. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: binbir.
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
- `PartyLegalEntity/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered, with its legal form; as Rinova Recovery gives it.
- `PartyLegalEntity/CompanyID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  Number in the Commercial register of Urvania; as Rinova Recovery gives it. The schemeID names the scheme it is from: the Commercial register of Urvania (XU-R- and 6 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Rinova Recovery gives it.
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Rinova Recovery gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Rinova Recovery gives it.
- `Contact/Telephone` = **+999 1 041 697 6856**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Rinova Recovery gives it.
- `Contact/ElectronicMail` = **customs@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Rinova Recovery gives it.
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Rinova Recovery gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Commercial register of Urvania; as Rinova Recovery gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customs Declaration

Inside `CustomsDeclaration`:

- `ID` = **26-0092**  
  The declaration as lodged with the customs of the exporting country.
- `FunctionCode` = **9** (listID `UN/EDIFACT EDED 1225`)  
  An original declaration, not an amendment. The code is from the world's copy of UN/EDIFACT 1225 Message function: 9 = Original.
- `ValidityPeriod/StartDate` = **2026-04-20**  
  From the declaration.
- `ValidityPeriod/DurationMeasure` = **90** (unitCode `DAY`)  
  The goods must leave within 90 days.
- `ApplicableTerritoryAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The customs territory the goods leave. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/ID` = **26-0452**  
  The shipment declared.
- `Shipment/Consignment/ID` = **26-0426**  
  The consignment carried.
- `Shipment/Consignment/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight leaving the country.
- `Shipment/Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Fiumella Barges gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Shipment/Consignment/CarrierParty/PartyName/Name` = **Fiumella Barges**  
  The trading name; as Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/ID` = **4160204198475331** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Shipment/Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Shipment/Consignment/CarrierParty/PostalAddress/StreetName` = **Skikzek Han Nestan** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/StreetName` = **Banchina del Fiume** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/BuildingNumber` = **52**  
  Building number of the postal address. As Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/PostalZone` = **4170**  
  Postal code in Urvania's format (4 digits). As Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Fiumella Barges gives it.
- `Shipment/Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Shipment/Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/Consignment/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Recycled PE granulate**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **9984000** (currencyID `XUF`)  
  The value of the granulate in ferra: Urvania values goods with freight and insurance to its border, and the invoice has one price, which includes the barge to the river quay, with no freight distinguished from it: the whole price is the value.
- `Shipment/GoodsItem/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight of the goods of this item, with their packaging.
- `Shipment/GoodsItem/Quantity` = **120** (unitCode `TNE`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Zhaldrek skalsir razkir mir huntaz drunvir, tidrek krirstul 0.94, trek sazdran nihan skul 1 zhurkaz.** (languageID `qau`)  
  The seller's description in Urvanian, the seller's language.
- `Shipment/GoodsItem/Item/Description` = **Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.** (languageID `en-XU`)  
  The seller's description in English, the working language between the countries.
- `Shipment/GoodsItem/Item/Name` = **Ranstan PE skalsir** (languageID `qau`)  
  The item's name in Urvanian, the seller's language.
- `Shipment/GoodsItem/Item/Name` = **Recycled PE granulate** (languageID `en-XU`)  
  The item's name in English, the working language between the countries.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Rinova Recovery describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **VII** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: VII = Plastics and articles thereof; rubber and articles thereof.
- `Shipment/GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **390110** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Rinova Recovery describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 390110 = Polyethylene having a specific gravity of less than 0.94, in primary forms.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **34710** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Rinova Recovery describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 34710 = Polymers of ethylene, in primary forms.
- `Shipment/ShipmentStage/TransportModeCode` = **8** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  The goods cross the border by river. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 8 = Inland water transport.
- `CustomsExitOfficeLocation/ID` = **XU001003** (schemeID `urn:ubl-examples:world:XU:customs-office`)  
  The office's number in the customs office list of Urvania.
- `CustomsExitOfficeLocation/Name` = **Customs post at the river border**  
  Where the goods leave the country.
- `CustomsExitOfficeLocation/Address/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country the office is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `ConsignorParty/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsignorParty/PartyName/Name` = **Rinova Recovery**  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsigneeParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Rivermouth Packaging gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **0990:15128** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Rivermouth Packaging gives it.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-412740** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Rivermouth Packaging gives it.
- `ConsigneeParty/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; as Rivermouth Packaging gives it.
- `ConsigneeParty/PostalAddress/ID` = **LUM-ADR-411619** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Rivermouth Packaging gives it.
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `ConsigneeParty/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. As Rivermouth Packaging gives it.
- `ConsigneeParty/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. As Rivermouth Packaging gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Rivermouth Packaging gives it.
- `ConsigneeParty/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). As Rivermouth Packaging gives it.
- `ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `ConsigneeParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Rivermouth Packaging gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `CustomsParty/PartyIdentification/ID` = **xu_k4r7** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  The party's preferred identifier: its number in the Index of Public Administrations of Urvania; as Customs Administration of Urvania gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `CustomsParty/PartyName/Name` = **Customs Administration of Urvania**  
  The trading name; as Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/ID` = **4180202968066555** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/AddressTypeCode` = **POSTAL** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: POSTAL = Postal address.
- `CustomsParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `CustomsParty/PostalAddress/Postbox` = **PB 18**  
  The customs office receives its post in a post box. As Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/StreetName` = **Zalsul Han Trurdrek** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/StreetName` = **Strada del Confine** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/BuildingNumber` = **22**  
  Building number of the postal address. As Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/CityName` = **Menbaz** (languageID `qau`)  
  The place's Urvanian name, as the map gives it. The town or locality nearest to the party's place on the map, in its own country and state. As Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/CityName` = **Valico Euridice** (languageID `en-XU`)  
  The place's English name, the Italian one. The town or locality nearest to the party's place on the map, in its own country and state. As Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/PostalZone` = **4530**  
  Postal code in Urvania's format (4 digits). As Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Customs Administration of Urvania gives it.
- `CustomsParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `CustomsParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `CustomsParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `CustomsParty/PartyLegalEntity/RegistrationName` = **Customs Administration of Urvania**  
  The public body's official name; as Customs Administration of Urvania gives it.
- `CustomsParty/PartyLegalEntity/CompanyID` = **xu_k4r7** (schemeID `urn:ubl-examples:world:XU:public-body-register`)  
  Number in the Index of Public Administrations of Urvania, which gives every public body a number of its own (xu_ and four lower-case letters or digits), derived from no other register ; as Customs Administration of Urvania gives it. The schemeID names the scheme it is from: the index of public administrations of Urvania (xu_ and four lower-case letters or digits, assigned by the index on the body's accreditation; no real IPA code of Italy's index starts with xu_).
- `CustomsParty/Contact/Name` = **Export office**  
  The party's export office desk: the desk for its role in this document (an export); as Customs Administration of Urvania gives it.
- `CustomsParty/Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; as Customs Administration of Urvania gives it.
- `CustomsParty/Contact/Department` = **Customs**  
  The department the desk belongs to; as Customs Administration of Urvania gives it.
- `CustomsParty/Contact/Telephone` = **+999 1 041 850 3855**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. As Customs Administration of Urvania gives it.
- `CustomsParty/Contact/ElectronicMail` = **export@customs-xu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Customs Administration of Urvania gives it.
- `CustomsParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Customs Administration of Urvania gives it.
- `CustomsParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CustomsParty/ElectronicAddress/ElectronicAddressID` = **XU:xu_k4r7** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Index of Public Administrations of Urvania; as Customs Administration of Urvania gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `AdditionalDocumentReference/ID` = **26-0339**  
  The order behind the export.
- `AdditionalDocumentReference/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: 26-0339 is the example plastics/01, a Order; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Order.

### Signature

Inside `Signature`:

- `ID` = **RR-SIG-EX-plastics**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Rinova Recovery**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ExportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ExportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:export-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>26-0451</cbc:ProfileExecutionID>
  <cbc:ID>26-0091</cbc:ID>
  <cbc:UUID>9d7cd654-55a1-5b6b-af72-1c8f54670605</cbc:UUID>
  <cbc:IssueDate>2026-04-20</cbc:IssueDate>
  <cbc:IssueTime>12:40:00-01:00</cbc:IssueTime>
  <cbc:ExportTypeCode listID="urn:ubl-examples:world:codelist:ExportTypeCode">PERMANENT</cbc:ExportTypeCode>
  <cbc:ExportReasonCode listID="urn:ubl-examples:world:codelist:ExportReasonCode">SALE</cbc:ExportReasonCode>
  <cbc:Note languageID="qau">Tragan zunir dizek drek valnir krukek.</cbc:Note>
  <cbc:Note languageID="en-XU">Declared electronically before the goods leave.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ExporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="ISO 6523">0990:13362</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104548</cbc:ID>
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
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 1 041 697 6856</cbc:Telephone>
      <cbc:ElectronicMail>customs@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:CustomsDeclaration>
    <cbc:ID>26-0092</cbc:ID>
    <cbc:FunctionCode listID="UN/EDIFACT EDED 1225">9</cbc:FunctionCode>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-04-20</cbc:StartDate>
      <cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
    </cac:ValidityPeriod>
    <cac:ApplicableTerritoryAddress>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:ApplicableTerritoryAddress>
    <cac:Shipment>
      <cbc:ID>26-0452</cbc:ID>
      <cac:Consignment>
        <cbc:ID>26-0426</cbc:ID>
        <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Fiumella Barges</cbc:Name>
          </cac:PartyName>
          <cac:PostalAddress>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160204198475331</cbc:ID>
            <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
            <cbc:StreetName languageID="qau">Skikzek Han Nestan</cbc:StreetName>
            <cbc:StreetName languageID="en-XU">Banchina del Fiume</cbc:StreetName>
            <cbc:BuildingNumber>52</cbc:BuildingNumber>
            <cbc:CityName languageID="qau">Ruldraz</cbc:CityName>
            <cbc:CityName languageID="en-XU">Ferrano</cbc:CityName>
            <cbc:PostalZone>4170</cbc:PostalZone>
            <cbc:CountrySubentity>Province of Ferrano</cbc:CountrySubentity>
            <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
              <cbc:Name>Urvania</cbc:Name>
            </cac:Country>
          </cac:PostalAddress>
        </cac:CarrierParty>
      </cac:Consignment>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Recycled PE granulate</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">9984000</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="TNE">120</cbc:Quantity>
        <cac:Item>
          <cbc:Description languageID="qau">Zhaldrek skalsir razkir mir huntaz drunvir, tidrek krirstul 0.94, trek sazdran nihan skul 1 zhurkaz.</cbc:Description>
          <cbc:Description languageID="en-XU">Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.</cbc:Description>
          <cbc:Name languageID="qau">Ranstan PE skalsir</cbc:Name>
          <cbc:Name languageID="en-XU">Recycled PE granulate</cbc:Name>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:NatureCode listID="WCO HS 2022 Sections">VII</cbc:NatureCode>
            <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
            <cbc:CommodityCode listID="WCO HS 2022">390110</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">34710</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
      <cac:ShipmentStage>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">8</cbc:TransportModeCode>
      </cac:ShipmentStage>
    </cac:Shipment>
    <cac:CustomsExitOfficeLocation>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-office">XU001003</cbc:ID>
      <cbc:Name>Customs post at the river border</cbc:Name>
      <cac:Address>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:Address>
    </cac:CustomsExitOfficeLocation>
    <cac:ConsignorParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
      </cac:PartyName>
    </cac:ConsignorParty>
    <cac:ConsigneeParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="ISO 6523">0990:15128</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412740</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-411619</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Estuary Road</cbc:StreetName>
        <cbc:BuildingNumber>28</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38505</cbc:PostalZone>
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
        <cbc:Name>Export office</cbc:Name>
        <cbc:JobTitle>Customs officer</cbc:JobTitle>
        <cbc:Department>Customs</cbc:Department>
        <cbc:Telephone>+999 1 041 850 3855</cbc:Telephone>
        <cbc:ElectronicMail>export@customs-xu.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:xu_k4r7</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CustomsParty>
    <cac:AdditionalDocumentReference>
      <cbc:ID>26-0339</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
    </cac:AdditionalDocumentReference>
  </cac:CustomsDeclaration>
  <cac:Signature>
    <cbc:ID>RR-SIG-EX-plastics</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rinova Recovery</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ExportCustomsDeclaration>
```
