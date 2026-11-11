# Export Customs Declaration: Kelpstone Gas to Customs and Border Service of Bayvarra

*Example 4 of the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)" · [Export Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXPORT-CUSTOMS-DECLARATION-SCHEMA)*

The gas producer declares March's gas leaving Bayvarra by pipeline, in one monthly declaration.

[The XML file](04-ExportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:energy**  
  The business process the document belongs to: the flow "Gas and electricity in an unbundled market (Bayvarra's gas field → Urvania)".
- `ProfileExecutionID` = **ENERGY-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **KG-EX-26-0152**  
  The exporter's reference.
- `UUID` = **ea7c1231-2189-5410-b62d-f96106f6767f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  The monthly declaration of the gas exported in March.
- `IssueTime` = **16:41:00**  
  The time the sender's system issued the document, in the sender's local time.

### Exporter Party

Inside `ExporterParty`:

- `WebsiteURI` = **https://www.kelpstone.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Kelpstone Gas (world/parties.json).
- `IndustryClassificationCode` = **0620** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Kelpstone Gas (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 0620 = Extraction of natural gas.
- `PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Kelpstone Gas (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-412877** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Kelpstone Gas (world/parties.json).
- `PartyName/Name` = **Kelpstone Gas**  
  The trading name; identity of Kelpstone Gas (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
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
- `PostalAddress/PostalZone` = **38540**  
  Postal code in Bayvarra's format (5 digits). identity of Kelpstone Gas (world/parties.json).
- `PostalAddress/CountrySubentity` = **Northern Territory**  
  The name of code XB-NT in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-NT** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Kelpstone Gas (world/parties.json). The code is from Bayvarra's national state or territory list: XB-NT = Northern Territory.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PhysicalLocation/Description` = **Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.**  
  Where the party actually operates, apart from its postal address.
- `PhysicalLocation/InformationURI` = **https://www.kelpstone.example**  
  Where to find more about the place.
- `PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **52.80** (unitCode `D61`)  
  The minutes of the latitude.
- `PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **18.00** (unitCode `D61`)  
  The minutes of the longitude.
- `PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `PartyTaxScheme/RegistrationName` = **Kelpstone Gas Ltd**  
  The name under which the party is registered for state sales tax; identity of Kelpstone Gas (world/parties.json).
- `PartyTaxScheme/CompanyID` = **NT-1238631**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Kelpstone Gas (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **STATE** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states. The code is from the Trade Accord's tax level list: STATE = Levied by a state or territory.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XBL = Lume.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Northern Territory**  
  The state or territory whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/RegistrationName` = **Kelpstone Gas Ltd**  
  The name under which the party is registered, with its legal form; identity of Kelpstone Gas (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20412877**  
  Number in the Federal business register of Bayvarra; identity of Kelpstone Gas (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **2011-04-01**  
  The day the company was entered in the register; identity of Kelpstone Gas (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **LTD** (listID `urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Bayvarra's national list: only the listID tells the forms of different countries apart. The code is from Bayvarra's national company legal form list: LTD = Limited company (private).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The name of code LTD in Bayvarra's national company legal form list.
- `PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 1315 persons and its turnover of 833000000.00 XBL in 2025, by the Trade Accord's limits; identity of Kelpstone Gas (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `PartyLegalEntity/CorporateStockAmount` = **120000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Kelpstone Gas (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Gullhaven**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Contact/Name` = **Gas sales**  
  The desk that handles this document; identity of Kelpstone Gas (world/parties.json).
- `Contact/JobTitle` = **Gas sales manager**  
  The job of the person who answers at the desk; identity of Kelpstone Gas (world/parties.json).
- `Contact/Department` = **Commercial**  
  The department the desk belongs to; identity of Kelpstone Gas (world/parties.json).
- `Contact/Telephone` = **+999 2 38522 12877**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Kelpstone Gas (world/parties.json).
- `Contact/ElectronicMail` = **gas@kelpstone.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Kelpstone Gas (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Kelpstone Gas (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412877** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Kelpstone Gas (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customs Declaration

Inside `CustomsDeclaration`:

- `ID` = **KG-CD-26-0153**  
  The declaration as lodged with the customs of the exporting country.
- `Shipment/ID` = **KG-SH-26-0154**  
  The shipment declared.
- `Shipment/GrossWeightMeasure` = **2940000** (unitCode `KGM`)  
  The gross weight leaving the country.
- `Shipment/Consignment/ID` = **KG-CS-26-0155**  
  The consignment carried.
- `Shipment/Consignment/CarrierParty/PartyIdentification/ID` = **20412877** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `Shipment/Consignment/CarrierParty/PartyName/Name` = **Kelpstone Gas**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Natural gas**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **1411200.00** (currencyID `XBL`)  
  The value of the gas at the contract price, in lume.
- `Shipment/GoodsItem/GrossWeightMeasure` = **2940000** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **39200** (unitCode `MWH`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.**  
  The seller's description; item natural-gas of Kelpstone Gas (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Natural gas**  
  The item's short name; item natural-gas of Kelpstone Gas (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **KG-NG**  
  The seller's own item number; item natural-gas of Kelpstone Gas (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **772060000015** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item natural-gas of Kelpstone Gas (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Where the item was produced; item natural-gas of Kelpstone Gas (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **V** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: V = Mineral products.
- `Shipment/GoodsItem/Item/CommodityClassification/CargoTypeCode` = **BULK** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: BULK = Dry bulk.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **271121** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item natural-gas of Kelpstone Gas (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 271121 = Natural gas, in gaseous state.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **12020** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item natural-gas of Kelpstone Gas (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 12020 = Natural gas, liquefied or in the gaseous state.
- `Shipment/ShipmentStage/ID` = **1**  
  The only stage.
- `Shipment/ShipmentStage/TransportModeCode` = **7** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  UN/ECE Recommendation 19 code 7: fixed transport installation, a pipeline. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 7 = Fixed transport installations.
- `Shipment/ShipmentStage/TransportMeans/JourneyID` = **KG-P1-2603**  
  The month's flow through the pipeline.
- `Shipment/ShipmentStage/TransportMeans/TransportMeansTypeCode` = **PIPELINE** (listID `urn:ubl-examples:world:codelist:TransportMeansTypeCode`)  
  The gas leaves by pipeline. The code is from the Trade Accord's transport means type list: PIPELINE = Pipeline.
- `Shipment/OriginAddress/ID` = **33/03** (schemeID `urn:ubl-examples:world:grid`)  
  Where the gas is produced: the platform of the offshore field. Identified by its square of the world's map grid (column/row), as offshore installations are identified by grid references.
- `Shipment/OriginAddress/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `Shipment/OriginAddress/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Shipment/OriginAddress/LocationCoordinate/LatitudeMinutesMeasure` = **49.80** (unitCode `D61`)  
  The minutes of the latitude.
- `Shipment/OriginAddress/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `Shipment/OriginAddress/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Shipment/OriginAddress/LocationCoordinate/LongitudeMinutesMeasure` = **16.20** (unitCode `D61`)  
  The minutes of the longitude.
- `Shipment/OriginAddress/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `ConsigneeParty/WebsiteURI` = **https://www.montebrio.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/IndustryClassificationCode` = **3510** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Montebrio Power (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 3510 = Electric power generation, transmission and distribution.
- `ConsigneeParty/PartyIdentification/ID` = **XU-R-105918** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Montebrio Power (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XU-TR-105918** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PartyName/Name` = **Montebrio Power**  
  The trading name; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `ConsigneeParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XU** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Urvania's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; StreetName BuildingNumber; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; PostalZone CityName; Region. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XU = Address format of Urvania.
- `ConsigneeParty/PostalAddress/StreetName` = **Bek Hekrul Trinskul** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PostalAddress/StreetName` = **Via della Centrale** (languageID `en-XB`)  
  The street's name in English, the country's other official language; the Italian names the British kept are part of English now; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Drinzul** (languageID `qau`)  
  The town's Urvanian name, which its people have always used; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Serravona** (languageID `en-XB`)  
  The town's English name, inherited from the Italian; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PostalAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `ConsigneeParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `ConsigneeParty/PartyTaxScheme/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered for value added tax; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PartyTaxScheme/CompanyID` = **XU007414377**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PartyTaxScheme/TaxLevelCode` = **NATIONAL** (listID `urn:ubl-examples:world:codelist:TaxLevelCode`)  
  The level of government that levies the tax: Urvania's value added tax is levied by the country. The code is from the Trade Accord's tax level list: NATIONAL = Levied by the country.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF** (listID `ISO 4217 Alpha`)  
  The tax is accounted for in the country's currency. The code is from the world's copy of UBL's Currency (ISO 4217) list: XUF = Ferra.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country whose tax this is. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `ConsigneeParty/PartyLegalEntity/RegistrationName` = **Montebrio Power SUA**  
  The name under which the party is registered, with its legal form; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyID` = **XU-R-105918**  
  Number in the Commercial register of Urvania; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1974-06-01**  
  The day the company was entered in the register; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **SUA** (listID `urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode`)  
  The legal form, as a code of Urvania's national list: only the listID tells the forms of different countries apart. The code is from Urvania's national company legal form list: SUA = Società urvaniana per azioni (public limited company).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The name of code SUA in Urvania's national company legal form list.
- `ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **LARGE** (listID `urn:ubl-examples:world:codelist:EntitySizeCode`)  
  The size class follows from the company's 2935 persons and its turnover of 35700000000 XUF in 2025, by the Trade Accord's limits; identity of Montebrio Power (world/parties.json). The code is from the Trade Accord's entity size list: LARGE = Large enterprise.
- `ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `ConsigneeParty/PartyLegalEntity/CorporateStockAmount` = **400000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
  The registered office, as entered in the register.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `ConsigneeParty/Contact/Name` = **Energy trading**  
  The desk that handles this document; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/Contact/JobTitle` = **Energy trader**  
  The job of the person who answers at the desk; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/Contact/Department` = **Trading**  
  The department the desk belongs to; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/Contact/Telephone` = **+999 1 0413 55918**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Urvania's own plan: Open numbering, kept from Italian times: the area code starts with 0 and stays in the number, also from abroad; the longer the area code, the shorter the number: Ferrano 041 and 7 digits (10 in all), Serravona 0413 and 5 digits (9). Mobiles start with 3 and have 10 digits. identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/Contact/ElectronicMail` = **trading@montebrio.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/Contact/Note` = **Weekdays 07:00–19:00**  
  When the desk can be reached; identity of Montebrio Power (world/parties.json).
- `ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Montebrio Power (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `CustomsParty/IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Customs and Border Service of Bayvarra (world/parties.json). The code is from the world's copy of International Standard Industrial Classification of All Economic Activities, Revision 4: 8411 = General public administration activities.
- `CustomsParty/PartyIdentification/ID` = **20410137** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Customs and Border Service of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CustomsParty/PartyName/Name` = **Customs and Border Service of Bayvarra**  
  The trading name; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Language/ID` = **en**  
  English, the language the party does business in.
- `CustomsParty/Language/Name` = **English**  
  The language's name.
- `CustomsParty/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `CustomsParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `CustomsParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `CustomsParty/PostalAddress/StreetName` = **Border Crossing Road**  
  Street of the postal address. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/PostalAddress/BuildingNumber` = **36**  
  Building number of the postal address. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/PostalAddress/PostalZone` = **71213**  
  Postal code in Bayvarra's format (5 digits). identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `CustomsParty/PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Customs and Border Service of Bayvarra (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `CustomsParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CustomsParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CustomsParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `CustomsParty/PartyLegalEntity/RegistrationName` = **Customs and Border Service of Bayvarra**  
  The name under which the party is registered, with its legal form; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/PartyLegalEntity/CompanyID` = **20410137**  
  Number in the Federal business register of Bayvarra; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **ACTIVE** (listID `urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode`)  
  The register shows the company as active, not in liquidation. The code is from the Trade Accord's company liquidation status list: ACTIVE = Active, not in liquidation.
- `CustomsParty/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `CustomsParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country of registration. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CustomsParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `CustomsParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `CustomsParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **COMMERCIAL** (listID `urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode`)  
  A register of businesses, not a register of charities or associations. The code is from the Trade Accord's corporate registration type list: COMMERCIAL = Commercial register.
- `CustomsParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The register covers the whole country. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CustomsParty/Contact/Name` = **Border office**  
  The desk that handles this document; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/Telephone` = **+999 2 7121 337 137**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/ElectronicMail` = **border@customs-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CustomsParty/ElectronicAddress/ElectronicAddressID` = **XB:20410137** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs and Border Service of Bayvarra (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ExportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ExportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:energy</cbc:ProfileID>
  <cbc:ProfileExecutionID>ENERGY-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>KG-EX-26-0152</cbc:ID>
  <cbc:UUID>ea7c1231-2189-5410-b62d-f96106f6767f</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>16:41:00</cbc:IssueTime>
  <cac:ExporterParty>
    <cbc:WebsiteURI>https://www.kelpstone.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">0620</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412877</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412877</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelpstone Gas</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Shoreline Road</cbc:StreetName>
      <cbc:BuildingNumber>2</cbc:BuildingNumber>
      <cbc:CityName>Gullhaven</cbc:CityName>
      <cbc:PostalZone>38540</cbc:PostalZone>
      <cbc:CountrySubentity>Northern Territory</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-NT</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PhysicalLocation>
      <cbc:Description>Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.</cbc:Description>
      <cbc:InformationURI>https://www.kelpstone.example</cbc:InformationURI>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
        <cbc:LatitudeMinutesMeasure unitCode="D61">52.80</cbc:LatitudeMinutesMeasure>
        <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
        <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
        <cbc:LongitudeMinutesMeasure unitCode="D61">18.00</cbc:LongitudeMinutesMeasure>
        <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
      </cac:LocationCoordinate>
    </cac:PhysicalLocation>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Kelpstone Gas Ltd</cbc:RegistrationName>
      <cbc:CompanyID>NT-1238631</cbc:CompanyID>
      <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">STATE</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
        <cbc:CurrencyCode listID="ISO 4217 Alpha">XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Northern Territory</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Kelpstone Gas Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20412877</cbc:CompanyID>
      <cbc:RegistrationDate>2011-04-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode">LTD</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
      <cbc:CorporateStockAmount currencyID="XBL">120000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
      <cac:RegistrationAddress>
        <cbc:CityName>Gullhaven</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XB:FBR</cbc:ID>
        <cbc:Name>Federal business register of Bayvarra</cbc:Name>
        <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Gas sales</cbc:Name>
      <cbc:JobTitle>Gas sales manager</cbc:JobTitle>
      <cbc:Department>Commercial</cbc:Department>
      <cbc:Telephone>+999 2 38522 12877</cbc:Telephone>
      <cbc:ElectronicMail>gas@kelpstone.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412877</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:CustomsDeclaration>
    <cbc:ID>KG-CD-26-0153</cbc:ID>
    <cac:Shipment>
      <cbc:ID>KG-SH-26-0154</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">2940000</cbc:GrossWeightMeasure>
      <cac:Consignment>
        <cbc:ID>KG-CS-26-0155</cbc:ID>
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
        <cbc:DeclaredCustomsValueAmount currencyID="XBL">1411200.00</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">2940000</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="MWH">39200</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.</cbc:Description>
          <cbc:Name>Natural gas</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>KG-NG</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">772060000015</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:NatureCode listID="WCO HS 2022 Sections">V</cbc:NatureCode>
            <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">BULK</cbc:CargoTypeCode>
            <cbc:CommodityCode listID="WCO HS 2022">271121</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">12020</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
      <cac:ShipmentStage>
        <cbc:ID>1</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">7</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>KG-P1-2603</cbc:JourneyID>
          <cbc:TransportMeansTypeCode listID="urn:ubl-examples:world:codelist:TransportMeansTypeCode">PIPELINE</cbc:TransportMeansTypeCode>
        </cac:TransportMeans>
      </cac:ShipmentStage>
      <cac:OriginAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:grid">33/03</cbc:ID>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">49.80</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">16.20</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:OriginAddress>
    </cac:Shipment>
    <cac:ConsigneeParty>
      <cbc:WebsiteURI>https://www.montebrio.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3510</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105918</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-105918</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Montebrio Power</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XU</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qau">Bek Hekrul Trinskul</cbc:StreetName>
        <cbc:StreetName languageID="en-XB">Via della Centrale</cbc:StreetName>
        <cbc:BuildingNumber>44</cbc:BuildingNumber>
        <cbc:CityName languageID="qau">Drinzul</cbc:CityName>
        <cbc:CityName languageID="en-XB">Serravona</cbc:CityName>
        <cbc:PostalZone>4130</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Montebrio Power SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007414377</cbc:CompanyID>
        <cbc:TaxLevelCode listID="urn:ubl-examples:world:codelist:TaxLevelCode">NATIONAL</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
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
        <cbc:CompanyID>XU-R-105918</cbc:CompanyID>
        <cbc:RegistrationDate>1974-06-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode listID="urn:ubl-examples:world:XU:codelist:CompanyLegalFormCode">SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode listID="urn:ubl-examples:world:codelist:EntitySizeCode">LARGE</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XUF">400000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
        <cac:RegistrationAddress>
          <cbc:CityName>Serravona</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XU:CR</cbc:ID>
          <cbc:Name>Commercial register of Urvania</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Energy trading</cbc:Name>
        <cbc:JobTitle>Energy trader</cbc:JobTitle>
        <cbc:Department>Trading</cbc:Department>
        <cbc:Telephone>+999 1 0413 55918</cbc:Telephone>
        <cbc:ElectronicMail>trading@montebrio.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 07:00–19:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105918</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:ConsigneeParty>
    <cac:CustomsParty>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410137</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Customs and Border Service of Bayvarra</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
        <cbc:StreetName>Border Crossing Road</cbc:StreetName>
        <cbc:BuildingNumber>36</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71213</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Customs and Border Service of Bayvarra</cbc:RegistrationName>
        <cbc:CompanyID>20410137</cbc:CompanyID>
        <cbc:CompanyLiquidationStatusCode listID="urn:ubl-examples:world:codelist:CompanyLiquidationStatusCode">ACTIVE</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Marrowdale</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode listID="urn:ubl-examples:world:codelist:CorporateRegistrationTypeCode">COMMERCIAL</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Border office</cbc:Name>
        <cbc:JobTitle>Public service officer</cbc:JobTitle>
        <cbc:Department>Public services</cbc:Department>
        <cbc:Telephone>+999 2 7121 337 137</cbc:Telephone>
        <cbc:ElectronicMail>border@customs-xb.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410137</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CustomsParty>
  </cac:CustomsDeclaration>
</ExportCustomsDeclaration>
```
