# Export Customs Declaration: Bayforth Forwarding to Customs and Border Service of Bayvarra

*Example 11 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Export Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXPORT-CUSTOMS-DECLARATION-SCHEMA)*

The forwarder, as customs agent, declares the export for the distributor at the seaport.

[The XML file](11-ExportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:export-customs-declaration:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Export customs declaration"; the community specification "Lumeport port community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:customs:1.0**  
  The Trade Accord's process profile the document belongs to: customs, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BF-EX-26-0135**  
  The exporter's reference.
- `UUID` = **4b360143-92f4-557a-aac2-22d33c03e880**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-12**  
  The forwarder, as customs agent, declares the export at the seaport.
- `IssueTime` = **14:25:00**  
  The time the sender's system issued the document, in the sender's local time.
- `ExportTypeCode` = **PERMANENT** (listID `urn:ubl-examples:world:codelist:ExportTypeCode`)  
  A permanent export: the goods are sold abroad. The code is from the Trade Accord's export type list: PERMANENT = Permanent export.
- `ExportReasonCode` = **SALE** (listID `urn:ubl-examples:world:codelist:ExportReasonCode`)  
  The reason: a sale to a buyer abroad. The code is from the Trade Accord's export reason list: SALE = Sale.
- `Note` = **Declared electronically before the goods leave.**  
  How it was declared.
- `VersionID` = **1**  
  The first version.

### Exporter Party

Inside `ExporterParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json). The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.

### Customs Declaration

Inside `CustomsDeclaration`:

- `ID` = **BF-CD-26-0136**  
  The declaration as lodged with the customs of the exporting country.
- `FunctionCode` = **9** (listID `UN/EDIFACT EDED 1225`)  
  An original declaration, not an amendment. The code is from the world's copy of UN/EDIFACT 1225 Message function: 9 = Original.
- `ValidityPeriod/StartDate` = **2026-05-12**  
  From the declaration.
- `ValidityPeriod/DurationMeasure` = **90** (unitCode `DAY`)  
  The goods must leave within 90 days.
- `ApplicableTerritoryAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The customs territory the goods leave. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Shipment/ID` = **LD-SH-26-0132**  
  The shipment declared.
- `Shipment/InsuranceValueAmount` = **59155.80** (currencyID `XBL`)  
  The cargo insurance the seller took out under CIF.
- `Shipment/FreeOnBoardValueAmount` = **50688.00** (currencyID `XBL`)  
  On board in Lumeport.
- `Shipment/Consignment/ID` = **LD-CS-26-0133**  
  The consignment carried.
- `Shipment/Consignment/GrossWeightMeasure` = **4106.4** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined (worklist C15). The gross weight leaving the country.
- `Shipment/Consignment/OfficeOfExitLocation/Name` = **Customs office, port of Lumeport**  
  Where the goods leave Bayvarra: the same port.
- `Shipment/Consignment/OfficeOfExportLocation/Name` = **Customs office, port of Lumeport**  
  Where the export is declared.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **49920.00** (currencyID `XBL`)  
  The value of the goods at export, in lume.
- `Shipment/GoodsItem/GrossWeightMeasure` = **3984** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **96** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **The manufacturer's Serra bench, from the distributor's stock.**  
  The seller's description; item bench-serra-b of Lumeway Distribution (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra-b of Lumeway Distribution (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.**  
  What comes with the item; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Keyword` = **park bench, street furniture**  
  The search string buyers find the item by, the maker's keywords in one element; item bench-serra of Valdara Industries (world/items.json). A second Keyword would have to be in another language (UBL rule IND7).
- `Shipment/GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/ModelName` = **Serra 180**  
  The model; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/WarrantyInformation` = **Five years on the frame against corrosion.**  
  The maker's warranty; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **LD-10442**  
  The seller's own item number; item bench-serra-b of Lumeway Distribution (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **COLOUR** (schemeID `urn:ubl-examples:world:codelist:OtherAttributeCode`)  
  The attribute the variant differs in. The code is from the Trade Accord's attribute list: COLOUR = Colour. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM** (listID `urn:ubl-examples:world:codelist:ItemPartPositionCode`)  
  The part of the item the attribute is on: the frame. The code is from the Trade Accord's item part position list: FRM = Frame.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY** (listID `urn:ubl-examples:world:codelist:ColourCode`)  
  The variant's code for it. The code is from the Trade Accord's colour list: GRY = Grey.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `Shipment/GoodsItem/Item/ManufacturersItemIdentification/ID` = **VI-B180**  
  The item number of the maker, Valdara Industries: the reseller's item is resale of item bench-serra.
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **9520610000012** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The maker's own number for the item, its Codana item number, which travels along with the GTIN; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **XX** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XX = Miscellaneous manufactured articles.
- `Shipment/GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-serra of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Shipment/GoodsItem/Item/TransactionConditions/ID` = **LD-TC-01**  
  The seller's number for these conditions of sale.
- `Shipment/GoodsItem/Item/TransactionConditions/Description` = **Sold to trade customers only, per pallet of four benches.**  
  The conditions in words.
- `Shipment/GoodsItem/Item/TransactionConditions/DocumentReference/ID` = **LD-GTC-2026**  
  The seller's general terms of trade.
- `Shipment/GoodsItem/Item/TransactionConditions/DocumentReference/DocumentTypeCode` = **774** (listID `UN/EDIFACT EDED 1001`)  
  The kind of document referred to, Lumeway's general terms of trade, a document outside the examples (world/documents.json, cited; decision Q29). The code is from the world's copy of UN/EDIFACT 1001 Document name: 774 = General terms and conditions.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Frame material**  
  A property buyers ask about.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Value` = **Cast steel, hot-dip galvanised**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Slat wood**  
  A property buyers ask about.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Value` = **Kiln-dried hardwood**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Seats**  
  A property buyers ask about.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Value` = **3**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ID` = **COL**  
  The maker's identifier for the property.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Frame colour**  
  The colour of the frame, one of the colours it is offered in.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  The property's value, taken from the maker's list of values (Ferro grey, Moss green; item bench-serra of Valdara Industries (world/items.json)). One ListValue only: UBL rule IND7 allows a second one only in another language.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **APP**  
  The group of properties this one belongs to.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Appearance**  
  The group's name.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **OPTIONAL** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: OPTIONAL = Optional.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ID` = **LOAD**  
  The maker's identifier for the property.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Load capacity**  
  The name of code LOAD in the Trade Accord's item property name list.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/NameCode` = **LOAD** (listID `urn:ubl-examples:world:codelist:ItemPropertyNameCode`)  
  The property's name as a code. The code is from the Trade Accord's item property name list: LOAD = Load capacity.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/TestMethod` = **Static load on the seat for one hour, three seats loaded evenly, no lasting deformation**  
  How the value is tested.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **450** (unitCode `KGM`)  
  Its measured value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ValueQualifier` = **Distributed over the seat**  
  What the value stands for.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the property matters in describing the item. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **SAF**  
  The group of properties this one belongs to.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Safety**  
  The group's name.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **MANDATORY** (listID `urn:ubl-examples:world:codelist:PropertyImportanceCode`)  
  How much the group matters. The code is from the Trade Accord's property importance list: MANDATORY = Mandatory.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-SF-0450** (schemeID `urn:ubl-examples:world:XU:property`)  
  The property's number in the property standard of the identification agency. The schemeID names the scheme it is from: the property standard of the Codana Identification Agency (UR-, two letters for the part of the standard (SF street furniture, WD wood), four digits).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **SF**  
  The part of the agency's property standard it is taken from (SF street furniture, WD wood), as the number itself shows.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/ManufacturerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/ManufacturerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Over the armrests**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **DEPTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: DEPTH = Depth. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **620** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **780** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Seat back at its highest point**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **SEATHEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  Which dimension. The code is from the Trade Accord's dimension attribute list: SEATHEIGHT = Seat height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Above the ground when anchored**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/MinimumMeasure` = **440** (unitCode `MMT`)  
  The lowest it can be set to.
- `Shipment/GoodsItem/Item/Dimension/MaximumMeasure` = **460** (unitCode `MMT`)  
  The highest it can be set to.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2E** (listID `urn:ubl-examples:world:codelist:EmissionTypeCode`)  
  The emission reported: greenhouse gases as CO2 equivalent. The code is from the Trade Accord's emission type list: CO2E = Greenhouse gases as CO2 equivalent.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueMeasure` = **96** (unitCode `KGM`)  
  The emission of one item.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueFactorNumeric` = **0.82**  
  The share of the footprint the steel frame accounts for.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueBaseMeasure` = **1** (unitCode `EA`)  
  The emission is per one bench.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/LifecycleStageCode` = **MANUFACTURING** (listID `urn:ubl-examples:world:codelist:LifecycleStageCode`)  
  The part of the bench's life the figure covers. The code is from the Trade Accord's life cycle stage list: MANUFACTURING = Manufacturing.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/LifecycleStageDescription` = **From the ore at the mine to the bench leaving the factory gate.**  
  That part in words.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/Description` = **Mining, steel making, casting, galvanising, sawing and the transport between them.**  
  What the figure includes.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **CALCULATED** (listID `urn:ubl-examples:world:codelist:EmissionCalculationMethodCode`)  
  Calculated, not measured. The code is from the Trade Accord's emission calculation method list: CALCULATED = Calculated.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **CRADLETOGATE** (listID `urn:ubl-examples:world:codelist:EmissionBoundaryCode`)  
  How much of the chain is included. The code is from the Trade Accord's emission boundary list: CRADLETOGATE = Cradle to gate.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **The steelworks' and sawmill's measured energy use of 2025**  
  Where the factors come from.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/MaintenanceFrequencyCode` = **YEARLY** (listID `urn:ubl-examples:world:codelist:MaintenanceFrequencyCode`)  
  How often the item needs maintenance. The code is from the Trade Accord's maintenance frequency list: YEARLY = Once a year.
- `Shipment/GoodsItem/Item/CircularityProfile/MaintenanceFrequencyDescription` = **Tighten the slat bolts and touch up the coating once a year.**  
  What the maintenance is.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **STEEL** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: STEEL = Steel.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **34** (unitCode `KGM`)  
  How much of it one item uses.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Steel made from Serravona ore in Urvania**  
  Where the material comes from.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **HARDWOOD** (listID `urn:ubl-examples:world:codelist:MaterialResourceCode`)  
  A material the item is made of. The code is from the Trade Accord's material resource list: HARDWOOD = Hardwood.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **22.5** (unitCode `KGM`)  
  How much of it one item uses.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Slats from Upland State, Bayvarra**  
  Where the material comes from.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeCode` = **PACKAGING** (listID `urn:ubl-examples:world:codelist:WasteTypeCode`)  
  The kind of waste the item leaves. The code is from the Trade Accord's waste type list: PACKAGING = Packaging.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeDescription` = **Stretch film and pallet straps, per bench**  
  The waste in words.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/WasteMeasure` = **0.4** (unitCode `KGM`)  
  How much of it per item.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the deliveries of 2025.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoreNumeric` = **8**  
  Side frames and slats can be replaced one by one, which is why the spare side frame exists.
- `Shipment/GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoringSystemCode` = **REPAIR10** (listID `urn:ubl-examples:world:codelist:ScoringSystemCode`)  
  The scale of the score. The code is from the Trade Accord's scoring system list: REPAIR10 = Repairability index, 0 to 10.
- `Shipment/GoodsItem/Item/CircularityProfile/ProductDocumentationDocumentReference/ID` = **VI-RM-B180**  
  The repair and maintenance manual.
- `Shipment/GoodsItem/ID` = **2**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **768.00** (currencyID `XBL`)  
  The value of the goods at export, in lume.
- `Shipment/GoodsItem/GrossWeightMeasure` = **122.4** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Spare side frame for the Serra bench.**  
  The seller's description; item bench-casting-b of Lumeway Distribution (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Bench side frame casting**  
  The item's short name; item bench-casting-b of Lumeway Distribution (world/items.json).
- `Shipment/GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/ModelName` = **Serra 180 side frame**  
  The model; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **LD-10443**  
  The seller's own item number; item bench-casting-b of Lumeway Distribution (world/items.json).
- `Shipment/GoodsItem/Item/ManufacturersItemIdentification/ID` = **VI-C180**  
  The item number of the maker, Valdara Industries: the reseller's item is resale of item bench-casting.
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **9520610000029** (schemeID `GS1 GTIN`)  
  The GTIN Lumeway Distribution gives the item, under its GS1 company prefix, which starts with 952: GS1 reserves that prefix for demonstrations and examples, so the number belongs to no real product; the maker numbers its items in another scheme, and GS1 lets a wholesaler or importer allocate the GTIN where the brand owner has none (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemIdentification/ID` = **771020000034** (schemeID `urn:ubl-examples:world:item`)  
  The maker's own number for the item, its Codana item number, which travels along with the GTIN; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **XV** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XV = Base metals and articles of base metal.
- `Shipment/GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **732599** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 732599 = Other cast articles of iron or steel: other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **42999** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; item bench-casting of Valdara Industries (world/items.json). The code is from the world's copy of UN Central Product Classification, Version 2.1: 42999 = Metal goods n.e.c..
- `Shipment/GoodsItem/Item/ManufacturerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/ManufacturerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/ShipmentStage/CustomsAgentParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Shipment/ShipmentStage/CustomsAgentParty/PartyName/Name` = **Bayforth Forwarding**  
  The trading name; identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/ShipmentStage/CustomsAgentParty/Language/Name` = **English**  
  The language's name.
- `Shipment/ShipmentStage/CustomsAgentParty/Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/ID` = **LUM-ADR-953846** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Bayforth Forwarding (world/parties.json). The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Shipment/ShipmentStage/CustomsAgentParty/PartyLegalEntity/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered, with its legal form; identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/PartyLegalEntity/CompanyID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; identity of Bayforth Forwarding (world/parties.json). The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/Name` = **Customs desk**  
  The party's customs desk desk: the desk for its role in this document (it deals with customs); identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/Department` = **Logistics**  
  The department the desk belongs to; identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/Telephone` = **+999 2 38 2144 1644**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/ElectronicMail` = **customs@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Bayforth Forwarding (world/parties.json).
- `Shipment/ShipmentStage/CustomsAgentParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Shipment/ShipmentStage/CustomsAgentParty/ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Bayforth Forwarding (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Shipment/FreightAllowanceCharge/ChargeIndicator` = **true**  
  The sea freight, paid by the seller.
- `Shipment/FreightAllowanceCharge/AllowanceChargeReasonCode` = **FC** (listID `UN/EDIFACT EDED 7161`)  
  The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services). The code is from the world's copy of UN/EDIFACT 7161 Special service description: FC = Freight service.
- `Shipment/FreightAllowanceCharge/AllowanceChargeReason` = **Ocean freight to Selanu**  
  Stated because it is part of the CIF price, not of the export value.
- `Shipment/FreightAllowanceCharge/Amount` = **2950.00** (currencyID `XBL`)  
  Freight and bunker surcharge.
- `CustomsExitOfficeLocation/Name` = **Customs office, port of Lumeport**  
  Where the goods leave the country.
- `ConsignorParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsignorParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XB`)  
  The street's name in English, the country's other official language; identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XB`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one (world/countries.json). The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists). The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `FreightForwarderParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `FreightForwarderParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
- `CustomsParty/PartyIdentification/ID` = **20410137** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Customs and Border Service of Bayvarra (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CustomsParty/PartyName/Name` = **Customs and Border Service of Bayvarra**  
  The trading name; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/PostalAddress/ID` = **UL-ADR-479100** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); identity of Customs and Border Service of Bayvarra (world/parties.json).
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
  The public body's official name; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/Name` = **Export office**  
  The party's export office desk: the desk for its role in this document (an export); identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/JobTitle` = **Customs officer**  
  The job of the person who answers at the desk; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/Department` = **Customs**  
  The department the desk belongs to; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/Telephone` = **+999 2 7121 337 137**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/ElectronicMail` = **export@customs-xb.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Customs and Border Service of Bayvarra (world/parties.json).
- `CustomsParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CustomsParty/ElectronicAddress/ElectronicAddressID` = **XB:20410137** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs and Border Service of Bayvarra (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `PreviousCustomsDeclaration/ID` = **LD-IM-26-0161**  
  The import declaration under which the benches entered Bayvarra from Urvania (flow road): the goods now leave again.
- `PreviousCustomsDeclaration/FunctionCode` = **IMPORT** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode`)  
  The kind of the previous declaration. The code is from the Trade Accord's customs declaration type list: IMPORT = Import declaration.
- `AdditionalDocumentReference/ID` = **VT-PO-26-0127**  
  The order behind the export.
- `AdditionalDocumentReference/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: VT-PO-26-0127 is the example sea/05, a Order; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Order.

### Signature

Inside `Signature`:

- `ID` = **BF-SIG-EX-sea**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<ExportCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:ExportCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:export-customs-declaration:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:customs:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BF-EX-26-0135</cbc:ID>
  <cbc:UUID>4b360143-92f4-557a-aac2-22d33c03e880</cbc:UUID>
  <cbc:IssueDate>2026-05-12</cbc:IssueDate>
  <cbc:IssueTime>14:25:00</cbc:IssueTime>
  <cbc:ExportTypeCode listID="urn:ubl-examples:world:codelist:ExportTypeCode">PERMANENT</cbc:ExportTypeCode>
  <cbc:ExportReasonCode listID="urn:ubl-examples:world:codelist:ExportReasonCode">SALE</cbc:ExportReasonCode>
  <cbc:Note>Declared electronically before the goods leave.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ExporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-693911</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
  </cac:ExporterParty>
  <cac:CustomsDeclaration>
    <cbc:ID>BF-CD-26-0136</cbc:ID>
    <cbc:FunctionCode listID="UN/EDIFACT EDED 1225">9</cbc:FunctionCode>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-05-12</cbc:StartDate>
      <cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
    </cac:ValidityPeriod>
    <cac:ApplicableTerritoryAddress>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:ApplicableTerritoryAddress>
    <cac:Shipment>
      <cbc:ID>LD-SH-26-0132</cbc:ID>
      <cbc:InsuranceValueAmount currencyID="XBL">59155.80</cbc:InsuranceValueAmount>
      <cbc:FreeOnBoardValueAmount currencyID="XBL">50688.00</cbc:FreeOnBoardValueAmount>
      <cac:Consignment>
        <cbc:ID>LD-CS-26-0133</cbc:ID>
        <cbc:GrossWeightMeasure unitCode="KGM">4106.4</cbc:GrossWeightMeasure>
        <cac:OfficeOfExitLocation>
          <cbc:Name>Customs office, port of Lumeport</cbc:Name>
        </cac:OfficeOfExitLocation>
        <cac:OfficeOfExportLocation>
          <cbc:Name>Customs office, port of Lumeport</cbc:Name>
        </cac:OfficeOfExportLocation>
      </cac:Consignment>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Park bench Serra 180</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XBL">49920.00</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">3984</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">96</cbc:Quantity>
        <cac:Item>
          <cbc:Description>The manufacturer's Serra bench, from the distributor's stock.</cbc:Description>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cbc:AdditionalInformation>Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
          <cbc:Keyword>park bench, street furniture</cbc:Keyword>
          <cbc:BrandName>Valdara</cbc:BrandName>
          <cbc:ModelName>Serra 180</cbc:ModelName>
          <cbc:WarrantyInformation>Five years on the frame against corrosion.</cbc:WarrantyInformation>
          <cac:SellersItemIdentification>
            <cbc:ID>LD-10442</cbc:ID>
            <cbc:ExtendedID>GRY</cbc:ExtendedID>
            <cac:PhysicalAttribute>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:OtherAttributeCode">COLOUR</cbc:AttributeID>
              <cbc:PositionCode listID="urn:ubl-examples:world:codelist:ItemPartPositionCode">FRM</cbc:PositionCode>
              <cbc:DescriptionCode listID="urn:ubl-examples:world:codelist:ColourCode">GRY</cbc:DescriptionCode>
              <cbc:Description>Frame in Ferro grey</cbc:Description>
            </cac:PhysicalAttribute>
          </cac:SellersItemIdentification>
          <cac:ManufacturersItemIdentification>
            <cbc:ID>VI-B180</cbc:ID>
          </cac:ManufacturersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="GS1 GTIN">9520610000012</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:AdditionalItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
          </cac:AdditionalItemIdentification>
          <cac:ItemSpecificationDocumentReference>
            <cbc:ID>VI-DS-B180</cbc:ID>
          </cac:ItemSpecificationDocumentReference>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:NatureCode listID="WCO HS 2022 Sections">XX</cbc:NatureCode>
            <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
            <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
          <cac:TransactionConditions>
            <cbc:ID>LD-TC-01</cbc:ID>
            <cbc:Description>Sold to trade customers only, per pallet of four benches.</cbc:Description>
            <cac:DocumentReference>
              <cbc:ID>LD-GTC-2026</cbc:ID>
              <cbc:DocumentTypeCode listID="UN/EDIFACT EDED 1001">774</cbc:DocumentTypeCode>
            </cac:DocumentReference>
          </cac:TransactionConditions>
          <cac:AdditionalItemProperty>
            <cbc:Name>Frame material</cbc:Name>
            <cbc:Value>Cast steel, hot-dip galvanised</cbc:Value>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:Name>Slat wood</cbc:Name>
            <cbc:Value>Kiln-dried hardwood</cbc:Value>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:Name>Seats</cbc:Name>
            <cbc:Value>3</cbc:Value>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:ID>COL</cbc:ID>
            <cbc:Name>Frame colour</cbc:Name>
            <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">OPTIONAL</cbc:ImportanceCode>
            <cbc:ListValue>Ferro grey</cbc:ListValue>
            <cac:ItemPropertyGroup>
              <cbc:ID>APP</cbc:ID>
              <cbc:Name>Appearance</cbc:Name>
              <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">OPTIONAL</cbc:ImportanceCode>
            </cac:ItemPropertyGroup>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:ID>LOAD</cbc:ID>
            <cbc:Name>Load capacity</cbc:Name>
            <cbc:NameCode listID="urn:ubl-examples:world:codelist:ItemPropertyNameCode">LOAD</cbc:NameCode>
            <cbc:TestMethod>Static load on the seat for one hour, three seats loaded evenly, no lasting deformation</cbc:TestMethod>
            <cbc:ValueQuantity unitCode="KGM">450</cbc:ValueQuantity>
            <cbc:ValueQualifier>Distributed over the seat</cbc:ValueQualifier>
            <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
            <cac:ItemPropertyGroup>
              <cbc:ID>SAF</cbc:ID>
              <cbc:Name>Safety</cbc:Name>
              <cbc:ImportanceCode listID="urn:ubl-examples:world:codelist:PropertyImportanceCode">MANDATORY</cbc:ImportanceCode>
            </cac:ItemPropertyGroup>
            <cac:StandardPropertyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:property">UR-SF-0450</cbc:ID>
              <cbc:IssuerScopeID>SF</cbc:IssuerScopeID>
              <cac:IssuerParty>
                <cac:PartyIdentification>
                  <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105644</cbc:ID>
                </cac:PartyIdentification>
                <cac:PartyName>
                  <cbc:Name>Codana Identification Agency</cbc:Name>
                </cac:PartyName>
              </cac:IssuerParty>
            </cac:StandardPropertyIdentification>
          </cac:AdditionalItemProperty>
          <cac:ManufacturerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Valdara Industries</cbc:Name>
            </cac:PartyName>
          </cac:ManufacturerParty>
          <cac:Dimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">1800</cbc:Measure>
            <cbc:Description>Over the armrests</cbc:Description>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">DEPTH</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">620</cbc:Measure>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">780</cbc:Measure>
            <cbc:Description>Seat back at its highest point</cbc:Description>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">SEATHEIGHT</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">450</cbc:Measure>
            <cbc:Description>Above the ground when anchored</cbc:Description>
            <cbc:MinimumMeasure unitCode="MMT">440</cbc:MinimumMeasure>
            <cbc:MaximumMeasure unitCode="MMT">460</cbc:MaximumMeasure>
          </cac:Dimension>
          <cac:EnvironmentalEmission>
            <cbc:EnvironmentalEmissionTypeCode listID="urn:ubl-examples:world:codelist:EmissionTypeCode">CO2E</cbc:EnvironmentalEmissionTypeCode>
            <cbc:ValueMeasure unitCode="KGM">96</cbc:ValueMeasure>
            <cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>
            <cbc:ValueBaseMeasure unitCode="EA">1</cbc:ValueBaseMeasure>
            <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
            <cbc:LifecycleStageCode listID="urn:ubl-examples:world:codelist:LifecycleStageCode">MANUFACTURING</cbc:LifecycleStageCode>
            <cbc:LifecycleStageDescription>From the ore at the mine to the bench leaving the factory gate.</cbc:LifecycleStageDescription>
            <cbc:Description>Mining, steel making, casting, galvanising, sawing and the transport between them.</cbc:Description>
            <cac:EmissionCalculationMethod>
              <cbc:CalculationMethodCode listID="urn:ubl-examples:world:codelist:EmissionCalculationMethodCode">CALCULATED</cbc:CalculationMethodCode>
              <cbc:FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode">CRADLETOGATE</cbc:FullnessIndicationCode>
              <cbc:EmissionFactorSource>The steelworks' and sawmill's measured energy use of 2025</cbc:EmissionFactorSource>
              <cac:EmissionFactorDocumentReference>
                <cbc:ID>VI-LCA-2025</cbc:ID>
              </cac:EmissionFactorDocumentReference>
            </cac:EmissionCalculationMethod>
            <cac:MeasurementPeriod>
              <cbc:StartDate>2025-01-01</cbc:StartDate>
              <cbc:EndDate>2025-12-31</cbc:EndDate>
            </cac:MeasurementPeriod>
          </cac:EnvironmentalEmission>
          <cac:CircularityProfile>
            <cbc:MaintenanceFrequencyCode listID="urn:ubl-examples:world:codelist:MaintenanceFrequencyCode">YEARLY</cbc:MaintenanceFrequencyCode>
            <cbc:MaintenanceFrequencyDescription>Tighten the slat bolts and touch up the coating once a year.</cbc:MaintenanceFrequencyDescription>
            <cac:ResourceConsumption>
              <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">STEEL</cbc:ResourceTypeCode>
              <cbc:ConsumptionMeasure unitCode="KGM">34</cbc:ConsumptionMeasure>
              <cbc:ResourceOriginDescription>Steel made from Serravona ore in Urvania</cbc:ResourceOriginDescription>
              <cac:MeasurementPeriod>
                <cbc:StartDate>2025-01-01</cbc:StartDate>
                <cbc:EndDate>2025-12-31</cbc:EndDate>
              </cac:MeasurementPeriod>
            </cac:ResourceConsumption>
            <cac:ResourceConsumption>
              <cbc:ResourceTypeCode listID="urn:ubl-examples:world:codelist:MaterialResourceCode">HARDWOOD</cbc:ResourceTypeCode>
              <cbc:ConsumptionMeasure unitCode="KGM">22.5</cbc:ConsumptionMeasure>
              <cbc:ResourceOriginDescription>Slats from Upland State, Bayvarra</cbc:ResourceOriginDescription>
              <cac:MeasurementPeriod>
                <cbc:StartDate>2025-01-01</cbc:StartDate>
                <cbc:EndDate>2025-12-31</cbc:EndDate>
              </cac:MeasurementPeriod>
            </cac:ResourceConsumption>
            <cac:WasteGenerated>
              <cbc:WasteTypeCode listID="urn:ubl-examples:world:codelist:WasteTypeCode">PACKAGING</cbc:WasteTypeCode>
              <cbc:WasteTypeDescription>Stretch film and pallet straps, per bench</cbc:WasteTypeDescription>
              <cbc:WasteMeasure unitCode="KGM">0.4</cbc:WasteMeasure>
              <cac:MeasurementPeriod>
                <cbc:StartDate>2025-01-01</cbc:StartDate>
                <cbc:EndDate>2025-12-31</cbc:EndDate>
              </cac:MeasurementPeriod>
            </cac:WasteGenerated>
            <cac:RepairabilityScore>
              <cbc:ScoreNumeric>8</cbc:ScoreNumeric>
              <cbc:ScoringSystemCode listID="urn:ubl-examples:world:codelist:ScoringSystemCode">REPAIR10</cbc:ScoringSystemCode>
            </cac:RepairabilityScore>
            <cac:ProductDocumentationDocumentReference>
              <cbc:ID>VI-RM-B180</cbc:ID>
            </cac:ProductDocumentationDocumentReference>
          </cac:CircularityProfile>
        </cac:Item>
      </cac:GoodsItem>
      <cac:GoodsItem>
        <cbc:ID>2</cbc:ID>
        <cbc:Description>Bench side frame casting</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XBL">768.00</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">122.4</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">12</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Spare side frame for the Serra bench.</cbc:Description>
          <cbc:Name>Bench side frame casting</cbc:Name>
          <cbc:BrandName>Valdara</cbc:BrandName>
          <cbc:ModelName>Serra 180 side frame</cbc:ModelName>
          <cac:SellersItemIdentification>
            <cbc:ID>LD-10443</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:ManufacturersItemIdentification>
            <cbc:ID>VI-C180</cbc:ID>
          </cac:ManufacturersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="GS1 GTIN">9520610000029</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:AdditionalItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771020000034</cbc:ID>
          </cac:AdditionalItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:NatureCode listID="WCO HS 2022 Sections">XV</cbc:NatureCode>
            <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
            <cbc:CommodityCode listID="WCO HS 2022">732599</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">42999</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
          <cac:ManufacturerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Valdara Industries</cbc:Name>
            </cac:PartyName>
          </cac:ManufacturerParty>
        </cac:Item>
      </cac:GoodsItem>
      <cac:ShipmentStage>
        <cac:CustomsAgentParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Bayforth Forwarding</cbc:Name>
          </cac:PartyName>
          <cac:Language>
            <cbc:ID schemeID="ISO 639">en</cbc:ID>
            <cbc:Name>English</cbc:Name>
            <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
          </cac:Language>
          <cac:PostalAddress>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-953846</cbc:ID>
            <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
            <cbc:StreetName>Dockside Way</cbc:StreetName>
            <cbc:BuildingNumber>4</cbc:BuildingNumber>
            <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
            <cbc:CityName>Lumeport</cbc:CityName>
            <cbc:PostalZone>38525</cbc:PostalZone>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
            <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              <cbc:Name>Bayvarra</cbc:Name>
            </cac:Country>
          </cac:PostalAddress>
          <cac:PartyLegalEntity>
            <cbc:RegistrationName>Bayforth Forwarding Ltd</cbc:RegistrationName>
            <cbc:CompanyID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:CompanyID>
          </cac:PartyLegalEntity>
          <cac:Contact>
            <cbc:Name>Customs desk</cbc:Name>
            <cbc:JobTitle>Customs specialist</cbc:JobTitle>
            <cbc:Department>Logistics</cbc:Department>
            <cbc:Telephone>+999 2 38 2144 1644</cbc:Telephone>
            <cbc:ElectronicMail>customs@bayforth.example</cbc:ElectronicMail>
            <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
          </cac:Contact>
          <cac:ElectronicAddress>
            <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
            <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
          </cac:ElectronicAddress>
        </cac:CustomsAgentParty>
      </cac:ShipmentStage>
      <cac:FreightAllowanceCharge>
        <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 7161">FC</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Ocean freight to Selanu</cbc:AllowanceChargeReason>
        <cbc:Amount currencyID="XBL">2950.00</cbc:Amount>
      </cac:FreightAllowanceCharge>
    </cac:Shipment>
    <cac:CustomsExitOfficeLocation>
      <cbc:Name>Customs office, port of Lumeport</cbc:Name>
    </cac:CustomsExitOfficeLocation>
    <cac:ConsignorParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:ConsignorParty>
    <cac:ConsigneeParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:delivery-point">40351721</cbc:ID>
        <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
        <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
        <cbc:StreetName languageID="en-XB">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XB">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
    </cac:ConsigneeParty>
    <cac:FreightForwarderParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Bayforth Forwarding</cbc:Name>
      </cac:PartyName>
    </cac:FreightForwarderParty>
    <cac:CustomsParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410137</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Customs and Border Service of Bayvarra</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:UL:address-register">UL-ADR-479100</cbc:ID>
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
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Export office</cbc:Name>
        <cbc:JobTitle>Customs officer</cbc:JobTitle>
        <cbc:Department>Customs</cbc:Department>
        <cbc:Telephone>+999 2 7121 337 137</cbc:Telephone>
        <cbc:ElectronicMail>export@customs-xb.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410137</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CustomsParty>
    <cac:PreviousCustomsDeclaration>
      <cbc:ID>LD-IM-26-0161</cbc:ID>
      <cbc:FunctionCode listID="urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode">IMPORT</cbc:FunctionCode>
    </cac:PreviousCustomsDeclaration>
    <cac:AdditionalDocumentReference>
      <cbc:ID>VT-PO-26-0127</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
    </cac:AdditionalDocumentReference>
  </cac:CustomsDeclaration>
  <cac:Signature>
    <cbc:ID>BF-SIG-EX-sea</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411644</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Bayforth Forwarding</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</ExportCustomsDeclaration>
```
