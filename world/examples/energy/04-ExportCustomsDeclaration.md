# Export Customs Declaration: Kelpstone Gas to Customs and Border Service of Bayvarra

*Example 4 of the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)" · [Export Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXPORT-CUSTOMS-DECLARATION-SCHEMA)*

The gas producer declares March's gas leaving Bayvarra by pipeline, in one monthly declaration: one shipment, the month's flow measured at the border metering station, with a consignment for each buyer, the power station and the retail company.

[The XML file](04-ExportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:export-customs-declaration:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Export customs declaration". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900034203**  
  The collaboration this document belongs to: Kelpstone's monthly export declaration of March's gas by pipeline, to its release for export. Kelpstone Gas started it and gave it this identifier, which every document of it repeats.
- `ID` = **7600006841**  
  The exporter's reference.
- `UUID` = **ea7c1231-2189-5410-b62d-f96106f6767f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  The monthly declaration of the gas exported in March.
- `IssueTime` = **16:41:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Kelpstone Gas gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **0990:19676** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Kelpstone Gas gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-412877** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Kelpstone Gas gives it.
- `PartyName/Name` = **Kelpstone Gas**  
  The trading name; as Kelpstone Gas gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
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
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PhysicalLocation/Description` = **Gas treatment plant on the north coast; the platform of the offshore field lies about 80 kilometres out.**  
  Where the party actually operates, apart from its postal address. The distance is measured along the route on the map, rounded to 10 km.
- `PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **28** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **15.95** (unitCode `D61`)  
  The minutes of the latitude.
- `PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **33.76** (unitCode `D61`)  
  The minutes of the longitude.
- `PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `PartyLegalEntity/RegistrationName` = **Kelpstone Gas Corp**  
  The name under which the party is registered, with its legal form; as Kelpstone Gas gives it.
- `PartyLegalEntity/CompanyID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Kelpstone Gas gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Kelpstone Gas gives it.
- `Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Kelpstone Gas gives it.
- `Contact/Department` = **Logistics**  
  The department the desk belongs to; as Kelpstone Gas gives it.
- `Contact/Telephone` = **+999 2 38522 68330**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Kelpstone Gas gives it.
- `Contact/ElectronicMail` = **customs@kelpstone.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Kelpstone Gas gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Kelpstone Gas gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412877** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Kelpstone Gas gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customs Declaration

Inside `CustomsDeclaration`:

- `ID` = **7500006841**  
  The declaration as lodged with the customs of the exporting country.
- `Shipment/ID` = **7400034203**  
  The shipment declared.
- `Shipment/Consignment/ID` = **7300034203**  
  The consignment of Montebrio Power.
- `Shipment/Consignment/SummaryDescription` = **Goods item 1: 36,800 MWh of natural gas, delivered to the power station.**  
  What the consignment holds: the goods item of this buyer.
- `Shipment/Consignment/GrossWeightMeasure` = **2760000** (unitCode `KGM`)  
  The weight of this buyer's gas.
- `Shipment/Consignment/ConsigneeParty/PartyIdentification/ID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Montebrio Power gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Shipment/Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **0990:10087** (schemeID `ISO 6523`)  
  A further identifier (the endorsed PartyIdentification holds one only), the party's organisation identifier in the structure of ISO/IEC 6523: the international code designator 0990 of the Codana Identification Agency and the party's Codana company number, which also starts its licence plates. No real scheme has the code designator 0990; as Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XU-TR-105918** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PartyName/Name` = **Montebrio Power**  
  The trading name; as Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/ID` = **4170200397702895** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/StreetName` = **Bek Hekrul Trinskul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/StreetName` = **Via della Centrale** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. As Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/CityName` = **Serravona** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/PostalZone` = **4310**  
  Postal code in Urvania's format (4 digits). As Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Montebrio Power gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Shipment/Consignment/CarrierParty/PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `Shipment/Consignment/CarrierParty/PartyName/Name` = **Kelpstone Gas**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `Shipment/Consignment/ID` = **7300034204**  
  The consignment of Ferrano Energy.
- `Shipment/Consignment/SummaryDescription` = **Goods item 2: 2,400 MWh of natural gas, fed into the grid at the city gate for the retail company's gas customers.**  
  What the consignment holds: the goods item of this buyer.
- `Shipment/Consignment/GrossWeightMeasure` = **180000** (unitCode `KGM`)  
  The weight of this buyer's gas.
- `Shipment/Consignment/ConsigneeParty/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; as Ferrano Energy gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Shipment/Consignment/ConsigneeParty/AdditionalPartyIdentification/ID` = **XU-TR-105781** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); as Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PartyName/Name` = **Ferrano Energy**  
  The trading name; as Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/ID` = **4160202777983743** (schemeID `urn:ubl-examples:world:XU:address-register`)  
  The address's number in the national address register of Urvania (16 digits: the four-digit code of the municipality, 20 for an address, and a ten-digit serial number); as Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; CountrySubentity. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/StreetName` = **Duznaz Hekrul Skultrir** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages ; as Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/StreetName` = **Corso della Repubblica** (languageID `en-XU`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; as Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/BuildingNumber` = **9**  
  Building number of the postal address. As Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/CityName` = **Ruldraz** (languageID `qau`)  
  The town's Urvanian name, which its people have always used. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/CityName` = **Ferrano** (languageID `en-XU`)  
  The town's English name, inherited from the Italian. The town or locality nearest to the party's place on the map, in its own country and state. As Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). As Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/CountrySubentity` = **Province of Ferrano**  
  The province, part of an address in Urvania: a subdivision of the country. As Ferrano Energy gives it.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Urvanian Time, Urvania's legal time, all year: there is no summer time.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/Consignment/ConsigneeParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Shipment/Consignment/CarrierParty/PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `Shipment/Consignment/CarrierParty/PartyName/Name` = **Kelpstone Gas**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number: one per buyer.
- `Shipment/GoodsItem/Description` = **Natural gas**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **1324800.00** (currencyID `XBL`)  
  The value of this buyer's gas at the contract price, in lume.
- `Shipment/GoodsItem/GrossWeightMeasure` = **2760000** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **36800** (unitCode `MWH`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.**  
  The seller's description.
- `Shipment/GoodsItem/Item/Name` = **Natural gas**  
  The item's short name.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Kelpstone Gas describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **V** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: V = Mineral products.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **271121** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Kelpstone Gas describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 271121 = Natural gas, in gaseous state.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **12020** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Kelpstone Gas describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 12020 = Natural gas, liquefied or in the gaseous state.
- `Shipment/GoodsItem/ID` = **2**  
  The goods item number: one per buyer.
- `Shipment/GoodsItem/Description` = **Natural gas**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **86400.00** (currencyID `XBL`)  
  The value of this buyer's gas at the contract price, in lume.
- `Shipment/GoodsItem/GrossWeightMeasure` = **180000** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **2400** (unitCode `MWH`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.**  
  The seller's description.
- `Shipment/GoodsItem/Item/Name` = **Natural gas**  
  The item's short name.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; as Kelpstone Gas describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **V** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: V = Mineral products.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **271121** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Kelpstone Gas describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 271121 = Natural gas, in gaseous state.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **12020** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Kelpstone Gas describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 12020 = Natural gas, liquefied or in the gaseous state.
- `Shipment/ShipmentStage/ID` = **1**  
  The only stage.
- `Shipment/ShipmentStage/TransportModeCode` = **7** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 7: fixed transport installation, a pipeline. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 7 = Fixed transport installations.
- `Shipment/ShipmentStage/TransitPeriod/StartDate` = **2026-03-01**  
  The gas declared flowed through the pipeline in March: a monthly declaration of a continuous flow.
- `Shipment/ShipmentStage/TransitPeriod/EndDate` = **2026-03-31**  
  The month's last day.
- `Shipment/ShipmentStage/TransportMeans/TransportMeansTypeCode` = **71** (listID `UNECE Recommendation 28`)  
  The gas leaves by pipeline. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 71 = Pipeline.
- `Shipment/OriginAddress/ID` = **19/03** (schemeID `urn:ubl-examples:world:grid`)  
  Where the gas is produced: the platform of the offshore field. Identified by its block of the world's offshore grid (blocks of 14 km, column/row), as offshore installations are identified by grid references.
- `Shipment/OriginAddress/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Shipment/OriginAddress/LocationCoordinate/LatitudeDegreesMeasure` = **27** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Shipment/OriginAddress/LocationCoordinate/LatitudeMinutesMeasure` = **30.54** (unitCode `D61`)  
  The minutes of the latitude.
- `Shipment/OriginAddress/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Shipment/OriginAddress/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Shipment/OriginAddress/LocationCoordinate/LongitudeMinutesMeasure` = **29.41** (unitCode `D61`)  
  The minutes of the longitude.
- `Shipment/OriginAddress/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Shipment/LastExitPortLocation/Description` = **On Bayvarra's side of the border with Urvania, in the Northern Territory.**  
  Where it stands.
- `Shipment/LastExitPortLocation/Name` = **Border metering station of the Kelpstone gas pipeline**  
  Where the gas leaves Bayvarra: the border metering station measures the gas declared.
- `Shipment/LastExitPortLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Shipment/LastExitPortLocation/LocationCoordinate/LatitudeDegreesMeasure` = **28** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Shipment/LastExitPortLocation/LocationCoordinate/LatitudeMinutesMeasure` = **40.54** (unitCode `D61`)  
  The minutes of the latitude.
- `Shipment/LastExitPortLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Shipment/LastExitPortLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `Shipment/LastExitPortLocation/LocationCoordinate/LongitudeMinutesMeasure` = **42.48** (unitCode `D61`)  
  The minutes of the longitude.
- `Shipment/LastExitPortLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `CustomsParty/PartyIdentification/ID` = **3071845926** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  The party's preferred identifier: its number in the Federal list of public bodies of Bayvarra; as Customs and Border Service of Bayvarra gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `CustomsParty/PartyName/Name` = **Customs and Border Service of Bayvarra**  
  The trading name; as Customs and Border Service of Bayvarra gives it.
- `CustomsParty/PostalAddress/ID` = **UL-ADR-479100** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Customs and Border Service of Bayvarra gives it.
- `CustomsParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CustomsParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `CustomsParty/PostalAddress/StreetName` = **Border Road**  
  Street of the postal address. As Customs and Border Service of Bayvarra gives it.
- `CustomsParty/PostalAddress/BuildingNumber` = **36**  
  Building number of the postal address. As Customs and Border Service of Bayvarra gives it.
- `CustomsParty/PostalAddress/CityName` = **Euridice Crossing**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Customs and Border Service of Bayvarra gives it.
- `CustomsParty/PostalAddress/PostalZone` = **71950**  
  Postal code in Bayvarra's format (5 digits). As Customs and Border Service of Bayvarra gives it.
- `CustomsParty/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `CustomsParty/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Customs and Border Service of Bayvarra gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `CustomsParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `CustomsParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CustomsParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `CustomsParty/PartyLegalEntity/RegistrationName` = **Customs and Border Service of Bayvarra**  
  The public body's official name; as Customs and Border Service of Bayvarra gives it.
- `CustomsParty/PartyLegalEntity/CompanyID` = **3071845926** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Number in the Federal list of public bodies of Bayvarra, which gives every public body a number of its own (10 digits, the first not 0), derived from no other register ; as Customs and Border Service of Bayvarra gives it. The schemeID names the scheme it is from: the federal list of public bodies of Bayvarra (10 digits, the first not 0, given by the Bayvarra Information Service).
- `CustomsParty/Contact/Name` = **Export office**  
  The party's export office desk: the desk for its role in this document (an export); as Customs and Border Service of Bayvarra gives it.
- `CustomsParty/Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; as Customs and Border Service of Bayvarra gives it.
- `CustomsParty/Contact/Department` = **Customs**  
  The department the desk belongs to; as Customs and Border Service of Bayvarra gives it.
- `CustomsParty/Contact/Telephone` = **+999 2 7121 503 398**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Customs and Border Service of Bayvarra gives it.
- `CustomsParty/Contact/ElectronicMail` = **export@customs-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Customs and Border Service of Bayvarra gives it.
- `CustomsParty/Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Customs and Border Service of Bayvarra gives it.
- `CustomsParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CustomsParty/ElectronicAddress/ElectronicAddressID` = **XB:3071845926** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal list of public bodies of Bayvarra; as Customs and Border Service of Bayvarra gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ExportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ExportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:export-customs-declaration:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900034203</cbc:ProfileExecutionID>
  <cbc:ID>7600006841</cbc:ID>
  <cbc:UUID>ea7c1231-2189-5410-b62d-f96106f6767f</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>16:41:00-01:00</cbc:IssueTime>
  <cac:ExporterParty>
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
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
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
    <cac:PhysicalLocation>
      <cbc:Description>Gas treatment plant on the north coast; the platform of the offshore field lies about 80 kilometres out.</cbc:Description>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure unitCode="DD">28</cbc:LatitudeDegreesMeasure>
        <cbc:LatitudeMinutesMeasure unitCode="D61">15.95</cbc:LatitudeMinutesMeasure>
        <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
        <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
        <cbc:LongitudeMinutesMeasure unitCode="D61">33.76</cbc:LongitudeMinutesMeasure>
        <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
      </cac:LocationCoordinate>
    </cac:PhysicalLocation>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Kelpstone Gas Corp</cbc:RegistrationName>
      <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customs desk</cbc:Name>
      <cbc:JobTitle>Customs specialist</cbc:JobTitle>
      <cbc:Department>Logistics</cbc:Department>
      <cbc:Telephone>+999 2 38522 68330</cbc:Telephone>
      <cbc:ElectronicMail>customs@kelpstone.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412877</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:CustomsDeclaration>
    <cbc:ID>7500006841</cbc:ID>
    <cac:Shipment>
      <cbc:ID>7400034203</cbc:ID>
      <cac:Consignment>
        <cbc:ID>7300034203</cbc:ID>
        <cbc:SummaryDescription>Goods item 1: 36,800 MWh of natural gas, delivered to the power station.</cbc:SummaryDescription>
        <cbc:GrossWeightMeasure unitCode="KGM">2760000</cbc:GrossWeightMeasure>
        <cac:ConsigneeParty>
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
        </cac:ConsigneeParty>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Kelpstone Gas</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
      </cac:Consignment>
      <cac:Consignment>
        <cbc:ID>7300034204</cbc:ID>
        <cbc:SummaryDescription>Goods item 2: 2,400 MWh of natural gas, fed into the grid at the city gate for the retail company's gas customers.</cbc:SummaryDescription>
        <cbc:GrossWeightMeasure unitCode="KGM">180000</cbc:GrossWeightMeasure>
        <cac:ConsigneeParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
          </cac:PartyIdentification>
          <cac:AdditionalPartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-105781</cbc:ID>
          </cac:AdditionalPartyIdentification>
          <cac:PartyName>
            <cbc:Name>Ferrano Energy</cbc:Name>
          </cac:PartyName>
          <cac:PostalAddress>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:address-register">4160202777983743</cbc:ID>
            <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
            <cbc:StreetName languageID="qau">Duznaz Hekrul Skultrir</cbc:StreetName>
            <cbc:StreetName languageID="en-XU">Corso della Repubblica</cbc:StreetName>
            <cbc:BuildingNumber>9</cbc:BuildingNumber>
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
        </cac:ConsigneeParty>
        <cac:CarrierParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Kelpstone Gas</cbc:Name>
          </cac:PartyName>
        </cac:CarrierParty>
      </cac:Consignment>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Natural gas</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XBL">1324800.00</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">2760000</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="MWH">36800</cbc:Quantity>
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
        </cac:Item>
      </cac:GoodsItem>
      <cac:GoodsItem>
        <cbc:ID>2</cbc:ID>
        <cbc:Description>Natural gas</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XBL">86400.00</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">180000</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="MWH">2400</cbc:Quantity>
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
      <cac:OriginAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:grid">19/03</cbc:ID>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">27</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">30.54</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">29.41</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:OriginAddress>
      <cac:LastExitPortLocation>
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
      </cac:LastExitPortLocation>
    </cac:Shipment>
    <cac:CustomsParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">3071845926</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Customs and Border Service of Bayvarra</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-479100</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Border Road</cbc:StreetName>
        <cbc:BuildingNumber>36</cbc:BuildingNumber>
        <cbc:CityName>Euridice Crossing</cbc:CityName>
        <cbc:PostalZone>71950</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Customs and Border Service of Bayvarra</cbc:RegistrationName>
        <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:public-body-register">3071845926</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Export office</cbc:Name>
        <cbc:JobTitle>Customs officer</cbc:JobTitle>
        <cbc:Department>Customs</cbc:Department>
        <cbc:Telephone>+999 2 7121 503 398</cbc:Telephone>
        <cbc:ElectronicMail>export@customs-xb.example</cbc:ElectronicMail>
        <cbc:Note>Every day, around the clock</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:3071845926</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CustomsParty>
  </cac:CustomsDeclaration>
</ExportCustomsDeclaration>
```
