# Export Customs Declaration: Bayforth Forwarding to Customs and Border Service of Bayvarra

*Example 11 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Export Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXPORT-CUSTOMS-DECLARATION-SCHEMA)*

The forwarder, as customs agent, declares the export for the distributor at the seaport.

[The XML file](11-ExportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:export-customs-declaration:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Export customs declaration"; the community specification "Lumeport port community". Each has a public description on the world's pages.
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
- `IssueTime` = **14:25:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
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
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Lumeway Distribution gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples ; as Lumeway Distribution gives it.
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); as Lumeway Distribution gives it.
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; as Lumeway Distribution gives it.
- `PostalAddress/ID` = **UL-ADR-693911** (schemeID `urn:ubl-examples:world:XB:UL:address-register`)  
  The address's number in the address register of Upland State (UL-ADR- and six digits); as Lumeway Distribution gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/BlockName` = **Marrowdale Business Park**  
  The business park the distribution centre stands in. As Lumeway Distribution gives it.
- `PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address. As Lumeway Distribution gives it.
- `PostalAddress/PlotIdentification` = **Plot 14**  
  The plot of the distribution centre in the business park. As Lumeway Distribution gives it.
- `PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Lumeway Distribution gives it.
- `PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits). As Lumeway Distribution gives it.
- `PostalAddress/CountrySubentity` = **Upland State**  
  The name of code XB-UL in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-UL** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Lumeway Distribution gives it. The code is from Bayvarra's national state or territory list: XB-UL = Upland State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
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
- `Shipment/TotalTransportHandlingUnitQuantity` = **27** (unitCode `EA`)  
  The pallets the goods travel on.
- `Shipment/FreeOnBoardValueAmount` = **51813.15** (currencyID `XBL`)  
  On board in Lumeport: the CIF price less the sea freight and the insurance, Bayvarra's basis of value at export.
- `Shipment/Consignment/ID` = **LD-CS-26-0133**  
  The consignment carried.
- `Shipment/Consignment/GrossWeightMeasure` = **5795.8** (unitCode `KGM`)  
  The gross weight of the goods with their packaging, without the transport equipment, as a consignment's weight is defined. The gross weight leaving the country.
- `Shipment/Consignment/TotalPackagesQuantity` = **324** (unitCode `EA`)  
  The parcels declared, on the pallets counted above.
- `Shipment/Consignment/OfficeOfExitLocation/Name` = **Customs office, port of Lumeport**  
  Where the goods leave Bayvarra: the same port.
- `Shipment/Consignment/OfficeOfExportLocation/Name` = **Customs office, port of Lumeport**  
  Where the export is declared.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **51042.97** (currencyID `XBL`)  
  Bayvarra values the goods as they left the exporting country: the goods at 54,080.00 XBL, with less the sea freight and the cargo insurance to the island, which the CIF price holds (-3,082.85 XBL), shared over the goods items by their value.
- `Shipment/GoodsItem/GrossWeightMeasure` = **5621.2** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `Shipment/GoodsItem/Quantity` = **104** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **The manufacturer's Serra bench, from the distributor's stock.**  
  The seller's description.
- `Shipment/GoodsItem/Item/Name` = **Park bench Serra 180**  
  The item's short name.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **XX** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XX = Miscellaneous manufactured articles.
- `Shipment/GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **940179** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940179 = Other seats, with metal frames: other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38111** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38111 = Seats, primarily with metal frames.
- `Shipment/GoodsItem/ContainingPackage/Quantity` = **4** (unitCode `EA`)  
  4 benches to a pallet; the goods item travels on 26 pallets.
- `Shipment/GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The pallet goes back to the party that loaded it.
- `Shipment/GoodsItem/ContainingPackage/PackageLevelCode` = **3** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 3: the outer level, the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 3 = Outer.
- `Shipment/GoodsItem/ContainingPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton, parcel 1 of 3 of each bench: one side frame**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **12.2** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **790** (unitCode `MMT`)  
  Its length.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **680** (unitCode `MMT`)  
  Its width.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **13** (unitCode `KGM`)  
  Within the 25 kg one person may lift (ISO 11228-1, the world's handling rule).
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The parcel's packaging stays with the goods.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **BE** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code BE: bundle. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: BE = Bundle.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped**  
  The parcel in words, as its label marks it; one of these per bench on the pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Polyester straps, cardboard edge protectors and end caps, PE film**  
  What the packaging is made of.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **LENGTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: LENGTH = Length. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **1810** (unitCode `MMT`)  
  Its length.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **WIDTH** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: WIDTH = Width. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **295** (unitCode `MMT`)  
  Its width.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **HEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's size. The code is from the Trade Accord's dimension attribute list: HEIGHT = Height. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **100** (unitCode `MMT`)  
  Its height.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/AttributeID` = **GROSSWEIGHT** (schemeID `urn:ubl-examples:world:codelist:DimensionAttributeCode`)  
  The parcel's weight. The code is from the Trade Accord's dimension attribute list: GROSSWEIGHT = Gross weight. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/MeasurementDimension/Measure` = **21.8** (unitCode `KGM`)  
  Within the limit, but 1.81 m long: two people carry it (ISO 11228-1, the world's handling rule).
- `Shipment/GoodsItem/ID` = **2**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **770.18** (currencyID `XBL`)  
  Bayvarra values the goods as they left the exporting country: the goods at 816.00 XBL, with less the sea freight and the cargo insurance to the island, which the CIF price holds (-3,082.85 XBL), shared over the goods items by their value.
- `Shipment/GoodsItem/GrossWeightMeasure` = **174.6** (unitCode `KGM`)  
  The gross weight of the goods of this item, in their parcels and with the pallets they travel on.
- `Shipment/GoodsItem/Quantity` = **12** (unitCode `EA`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Spare side frame for the Serra bench.**  
  The seller's description.
- `Shipment/GoodsItem/Item/Name` = **Bench side frame casting**  
  The item's short name.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU** (listID `ISO 3166`)  
  Where the item was produced; as Valdara Industries describes the item. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XU = Urvania.
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **XX** (listID `WCO HS 2022 Sections`)  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification. The code is from the world's copy of Harmonized System 2022, sections: XX = Miscellaneous manufactured articles.
- `Shipment/GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN** (listID `urn:ubl-examples:world:codelist:CargoTypeCode`)  
  The kind of cargo: bulk, or general cargo in packages. The code is from the Trade Accord's cargo type list: GEN = General cargo.
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **940199** (listID `WCO HS 2022`)  
  The Harmonized System subheading of the World Customs Organization, six digits, for customs and trade statistics; as Valdara Industries describes the item. The code is from the world's copy of Harmonized Commodity Description and Coding System, 2022 edition (subheadings): 940199 = Parts of seats, other.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **38160** (listID `UN CPC Ver.2.1`)  
  What the item is, as a subclass of the UN Central Product Classification (CPC), the trade classification for goods and services; as Valdara Industries describes the item. The code is from the world's copy of UN Central Product Classification, Version 2.1: 38160 = Parts of furniture.
- `Shipment/GoodsItem/ContainingPackage/Quantity` = **12** (unitCode `EA`)  
  12 side frames to a pallet; the goods item travels on 1 pallet.
- `Shipment/GoodsItem/ContainingPackage/ReturnableMaterialIndicator` = **true**  
  The pallet goes back to the party that loaded it.
- `Shipment/GoodsItem/ContainingPackage/PackageLevelCode` = **3** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 3: the outer level, the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 3 = Outer.
- `Shipment/GoodsItem/ContainingPackage/PackagingTypeCode` = **PX** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code PX: pallet. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: PX = Pallet.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/Quantity` = **1** (unitCode `EA`)  
  One side frame in each carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/ReturnableMaterialIndicator` = **false**  
  The carton stays with the frame.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackageLevelCode` = **1** (listID `UN/EDIFACT EDED 7075`)  
  UN/EDIFACT 7075 code 1: the inner level, below the pallet. The code is from the world's copy of UN/EDIFACT 7075 Packaging level: 1 = Inner.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingTypeCode` = **CT** (listID `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)`)  
  UN/ECE Recommendation 21 code CT: carton. The code is from the world's copy of UBL's Packaging type (UNECE Recommendation 21) list, with a listID: CT = Carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackagingType` = **Frame carton, one side frame**  
  The carton in words; the goods item's frames travel one to a carton.
- `Shipment/GoodsItem/ContainingPackage/ContainedPackage/PackingMaterial` = **Corrugated cardboard, tray and lid**  
  What the packaging is made of.
- `Shipment/ShipmentStage/ID` = **2**  
  The sea leg on which the goods leave Bayvarra, stage 2 as on the bill of lading.
- `Shipment/ShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Maritime transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.
- `Shipment/ShipmentStage/TransportMeans/JourneyID` = **TH-26-19E**  
  The voyage the container is booked on.
- `Shipment/ShipmentStage/TransportMeans/RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/ShipmentStage/TransportMeans/RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `Shipment/ShipmentStage/TransportMeans/DirectionCode` = **EB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: EB = Eastbound.
- `Shipment/ShipmentStage/TransportMeans/TransportMeansTypeCode` = **1511** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tidewell Harbour; the fleet of Tidewell Ocean Lines. The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 1511 = Full container ship/cellular vessel.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/VesselID` = **XB-S-20117** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships; a number of the world, not an IMO number.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/VesselName` = **Tidewell Harbour**  
  The vessel's name; the fleet of Tidewell Ocean Lines.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/RadioCallSignID` = **QBTH7**  
  The radio call sign, in Bayvarra's call sign series QB: no ITU series starts with Q, so the sign belongs to no real station.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/MMSIRegistrationID` = **298702117**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 298 of Bayvarra, which the ITU has not allocated to any real country, and the ship's six digits.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/GrossTonnageMeasure` = **9940** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/NetTonnageMeasure` = **5120** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 1,000 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20117**  
  The ship's certificate of registry.
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `Shipment/ShipmentStage/TransportMeans/MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.
- `Shipment/ShipmentStage/CustomsAgentParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `Shipment/ShipmentStage/CustomsAgentParty/PartyName/Name` = **Bayforth Forwarding**  
  The trading name; as Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Shipment/ShipmentStage/CustomsAgentParty/Language/Name` = **English**  
  The language's name.
- `Shipment/ShipmentStage/CustomsAgentParty/Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/ID` = **LUM-ADR-953846** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/StreetName` = **Dockside Way**  
  Street of the postal address. As Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/BuildingNumber` = **4**  
  Building number of the postal address. As Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/PostalZone` = **38525**  
  Postal code in Bayvarra's format (5 digits). As Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Bayforth Forwarding gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `Shipment/ShipmentStage/CustomsAgentParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Shipment/ShipmentStage/CustomsAgentParty/PartyLegalEntity/RegistrationName` = **Bayforth Forwarding Ltd**  
  The name under which the party is registered, with its legal form; as Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/PartyLegalEntity/CompanyID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  Number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. The schemeID names the scheme it is from: the Federal business register of Bayvarra (8 digits).
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/Name` = **Customs desk**  
  The party's customs desk: the desk for its role in this document (it deals with customs); as Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/JobTitle` = **Customs specialist**  
  The job of the person who answers at the desk; as Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/Department` = **Logistics**  
  The department the desk belongs to; as Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/Telephone` = **+999 2 38 5155 2404**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. As Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/ElectronicMail` = **customs@bayforth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; as Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; as Bayforth Forwarding gives it.
- `Shipment/ShipmentStage/CustomsAgentParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Shipment/ShipmentStage/CustomsAgentParty/ElectronicAddress/ElectronicAddressID` = **XB:20411644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Bayforth Forwarding gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Shipment/ShipmentStage/EstimatedDepartureTransportEvent/OccurrenceDate` = **2026-05-14**  
  The timetable departure from Lumeport.
- `Shipment/ShipmentStage/EstimatedDepartureTransportEvent/OccurrenceTime` = **18:00:00**  
  The local time.
- `Shipment/ShipmentStage/EstimatedDepartureTransportEvent/CompletionIndicator` = **false**  
  Whether the event has taken place (true) or is still to come (false).
- `Shipment/ShipmentStage/EstimatedDepartureTransportEvent/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Shipment/ShipmentStage/EstimatedDepartureTransportEvent/Location/Name` = **Port of Lumeport**  
  At the container quay of the Port of Lumeport.
- `Shipment/ShipmentStage/EstimatedDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `CustomsExitOfficeLocation/Name` = **Customs office, port of Lumeport**  
  Where the goods leave the country.
- `ConsignorParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsignorParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsigneeParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; as Velumi Trading gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A further identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); as Velumi Trading gives it.
- `ConsigneeParty/PartyName/Name` = **Velumi Trading**  
  The trading name; as Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/ID` = **40351721** (schemeID `urn:ubl-examples:world:XL:delivery-point`)  
  The address's number in the delivery point number of the Lisavu Post Office (eight digits: the island has no postal codes, and the post office numbers every address it delivers to); as Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XL** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Lisavu's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; Description; District; CityName. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XL = Address format of Lisavu.
- `ConsigneeParty/PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages ; as Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/StreetName` = **Reef Street** (languageID `en-XL`)  
  The street's name in English, the country's other official language; as Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. As Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Selanu** (languageID `qal`)  
  The town's Lisavan name, its name on the island. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/CityName` = **Port Wrenfield** (languageID `en-XL`)  
  The town's English name, which its English-speaking settlers gave it, official beside the Lisavan one. The town or locality nearest to the party's place on the map, in its own country and state. As Velumi Trading gives it.
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **+00:00**  
  The offset from UTC of Lisavu Time, Lisavu's legal time, all year: there is no summer time.
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ConsigneeParty/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `FreightForwarderParty/PartyIdentification/ID` = **20411644** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `FreightForwarderParty/PartyName/Name` = **Bayforth Forwarding**  
  A party referred to from another party's details: its identifier and name are enough.
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
- `PreviousCustomsDeclaration/ID` = **LD-IM-26-0340**  
  The import declaration under which the 96 benches of lot VI-LOT-260409 and the 8 benches of lot VI-LOT-260410 entered Bayvarra from Urvania (the Accord's common transit ended at Marrowdale): the bulk of the goods now leaves again.
- `PreviousCustomsDeclaration/FunctionCode` = **IMPORT** (listID `urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode`)  
  The kind of the previous declaration. The code is from the Trade Accord's customs declaration type list: IMPORT = Import declaration.
- `AdditionalDocumentReference/ID` = **VT-PO-26-0127**  
  The order behind the export.
- `AdditionalDocumentReference/DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: VT-PO-26-0127 is the example sea/05, a Order; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: Order.
- `AdditionalDocumentReference/ID` = **LD-IM-26-0161**  
  The import declaration under which the 12 side frames entered Bayvarra by road in March, a previous customs declaration of the goods beside the one above.
- `AdditionalDocumentReference/DocumentTypeCode` = **ImportCustomsDeclaration** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LD-IM-26-0161 is the example road/10, a ImportCustomsDeclaration; a generic reference names the UBL document type. The code is from the Trade Accord's UBL document type list: ImportCustomsDeclaration = Import Customs Declaration.

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
  <cbc:IssueTime>14:25:00-01:00</cbc:IssueTime>
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
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
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
      <cbc:TotalTransportHandlingUnitQuantity unitCode="EA">27</cbc:TotalTransportHandlingUnitQuantity>
      <cbc:FreeOnBoardValueAmount currencyID="XBL">51813.15</cbc:FreeOnBoardValueAmount>
      <cac:Consignment>
        <cbc:ID>LD-CS-26-0133</cbc:ID>
        <cbc:GrossWeightMeasure unitCode="KGM">5795.8</cbc:GrossWeightMeasure>
        <cbc:TotalPackagesQuantity unitCode="EA">324</cbc:TotalPackagesQuantity>
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
        <cbc:DeclaredCustomsValueAmount currencyID="XBL">51042.97</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">5621.2</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">104</cbc:Quantity>
        <cac:Item>
          <cbc:Description>The manufacturer's Serra bench, from the distributor's stock.</cbc:Description>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:NatureCode listID="WCO HS 2022 Sections">XX</cbc:NatureCode>
            <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
            <cbc:CommodityCode listID="WCO HS 2022">940179</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38111</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
        </cac:Item>
        <cac:ContainingPackage>
          <cbc:Quantity unitCode="EA">4</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">3</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
          <cac:ContainedPackage>
            <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
            <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
            <cbc:PackagingType>Frame carton, parcel 1 of 3 of each bench: one side frame</cbc:PackagingType>
            <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">790</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">680</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">100</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">12.2</cbc:Measure>
            </cac:MeasurementDimension>
          </cac:ContainedPackage>
          <cac:ContainedPackage>
            <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
            <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
            <cbc:PackagingType>Frame carton with the bolt set, parcel 2 of 3 of each bench: the other side frame and the bag of 20 stainless bolts with nuts and washers</cbc:PackagingType>
            <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">790</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">680</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">100</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">13</cbc:Measure>
            </cac:MeasurementDimension>
          </cac:ContainedPackage>
          <cac:ContainedPackage>
            <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
            <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">BE</cbc:PackagingTypeCode>
            <cbc:PackagingType>Slat bundle, parcel 3 of 3 of each bench: five slats, three and two, with edge protectors and end caps, strapped</cbc:PackagingType>
            <cbc:PackingMaterial>Polyester straps, cardboard edge protectors and end caps, PE film</cbc:PackingMaterial>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">LENGTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">1810</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">WIDTH</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">295</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">HEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="MMT">100</cbc:Measure>
            </cac:MeasurementDimension>
            <cac:MeasurementDimension>
              <cbc:AttributeID schemeID="urn:ubl-examples:world:codelist:DimensionAttributeCode">GROSSWEIGHT</cbc:AttributeID>
              <cbc:Measure unitCode="KGM">21.8</cbc:Measure>
            </cac:MeasurementDimension>
          </cac:ContainedPackage>
        </cac:ContainingPackage>
      </cac:GoodsItem>
      <cac:GoodsItem>
        <cbc:ID>2</cbc:ID>
        <cbc:Description>Bench side frame casting</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XBL">770.18</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">174.6</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="EA">12</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Spare side frame for the Serra bench.</cbc:Description>
          <cbc:Name>Bench side frame casting</cbc:Name>
          <cac:OriginCountry>
            <cbc:IdentificationCode listID="ISO 3166">XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:NatureCode listID="WCO HS 2022 Sections">XX</cbc:NatureCode>
            <cbc:CargoTypeCode listID="urn:ubl-examples:world:codelist:CargoTypeCode">GEN</cbc:CargoTypeCode>
            <cbc:CommodityCode listID="WCO HS 2022">940199</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="UN CPC Ver.2.1">38160</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
        </cac:Item>
        <cac:ContainingPackage>
          <cbc:Quantity unitCode="EA">12</cbc:Quantity>
          <cbc:ReturnableMaterialIndicator>true</cbc:ReturnableMaterialIndicator>
          <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">3</cbc:PackageLevelCode>
          <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">PX</cbc:PackagingTypeCode>
          <cac:ContainedPackage>
            <cbc:Quantity unitCode="EA">1</cbc:Quantity>
            <cbc:ReturnableMaterialIndicator>false</cbc:ReturnableMaterialIndicator>
            <cbc:PackageLevelCode listID="UN/EDIFACT EDED 7075">1</cbc:PackageLevelCode>
            <cbc:PackagingTypeCode listID="UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)">CT</cbc:PackagingTypeCode>
            <cbc:PackagingType>Frame carton, one side frame</cbc:PackagingType>
            <cbc:PackingMaterial>Corrugated cardboard, tray and lid</cbc:PackingMaterial>
          </cac:ContainedPackage>
        </cac:ContainingPackage>
      </cac:GoodsItem>
      <cac:ShipmentStage>
        <cbc:ID>2</cbc:ID>
        <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
        <cac:TransportMeans>
          <cbc:JourneyID>TH-26-19E</cbc:JourneyID>
          <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
          <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
          <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">EB</cbc:DirectionCode>
          <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">1511</cbc:TransportMeansTypeCode>
          <cac:MaritimeTransport>
            <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20117</cbc:VesselID>
            <cbc:VesselName>Tidewell Harbour</cbc:VesselName>
            <cbc:RadioCallSignID>QBTH7</cbc:RadioCallSignID>
            <cbc:MMSIRegistrationID>298702117</cbc:MMSIRegistrationID>
            <cbc:GrossTonnageMeasure unitCode="C62">9940</cbc:GrossTonnageMeasure>
            <cbc:NetTonnageMeasure unitCode="C62">5120</cbc:NetTonnageMeasure>
            <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
            <cac:RegistryCertificateDocumentReference>
              <cbc:ID>REG-XB-S-20117</cbc:ID>
            </cac:RegistryCertificateDocumentReference>
            <cac:RegistryPortLocation>
              <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
              <cbc:Name>Lumeport</cbc:Name>
            </cac:RegistryPortLocation>
          </cac:MaritimeTransport>
        </cac:TransportMeans>
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
            <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
          </cac:Language>
          <cac:PostalAddress>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-953846</cbc:ID>
            <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
            <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
            <cbc:StreetName>Dockside Way</cbc:StreetName>
            <cbc:BuildingNumber>4</cbc:BuildingNumber>
            <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
            <cbc:CityName>Lumeport</cbc:CityName>
            <cbc:PostalZone>38525</cbc:PostalZone>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
            <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
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
            <cbc:Telephone>+999 2 38 5155 2404</cbc:Telephone>
            <cbc:ElectronicMail>customs@bayforth.example</cbc:ElectronicMail>
            <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
          </cac:Contact>
          <cac:ElectronicAddress>
            <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
            <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411644</cbc:ElectronicAddressID>
          </cac:ElectronicAddress>
        </cac:CustomsAgentParty>
        <cac:EstimatedDepartureTransportEvent>
          <cbc:OccurrenceDate>2026-05-14</cbc:OccurrenceDate>
          <cbc:OccurrenceTime>18:00:00</cbc:OccurrenceTime>
          <cbc:CompletionIndicator>false</cbc:CompletionIndicator>
          <cac:Location>
            <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
            <cbc:Name>Port of Lumeport</cbc:Name>
            <cac:Address>
              <cac:Country>
                <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:Location>
        </cac:EstimatedDepartureTransportEvent>
      </cac:ShipmentStage>
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
        <cbc:StreetName languageID="en-XL">Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName languageID="qal">Selanu</cbc:CityName>
        <cbc:CityName languageID="en-XL">Port Wrenfield</cbc:CityName>
        <cbc:TimezoneOffset>+00:00</cbc:TimezoneOffset>
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
    <cac:PreviousCustomsDeclaration>
      <cbc:ID>LD-IM-26-0340</cbc:ID>
      <cbc:FunctionCode listID="urn:ubl-examples:world:codelist:CustomsDeclarationTypeCode">IMPORT</cbc:FunctionCode>
    </cac:PreviousCustomsDeclaration>
    <cac:AdditionalDocumentReference>
      <cbc:ID>VT-PO-26-0127</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
    </cac:AdditionalDocumentReference>
    <cac:AdditionalDocumentReference>
      <cbc:ID>LD-IM-26-0161</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">ImportCustomsDeclaration</cbc:DocumentTypeCode>
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
