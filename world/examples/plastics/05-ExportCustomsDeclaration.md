# Export Customs Declaration: Rinova Recovery to Customs Administration of Urvania

*Example 5 of the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)" · [Export Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-EXPORT-CUSTOMS-DECLARATION-SCHEMA)*

The granulate leaves Urvania; the waste processor declares the export.

[The XML file](05-ExportCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:plastics**  
  The business process the document belongs to: the flow "Recycled plastic granulate by river barge (Urvania → Bayvarra)".
- `ProfileExecutionID` = **PLASTICS-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **RR-EX-26-0887**  
  The exporter's reference.
- `UUID` = **9d7cd654-55a1-5b6b-af72-1c8f54670605**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-19**  
  Declared the day the barge is loaded.
- `IssueTime` = **16:08:00**  
  The time the sender's system issued the document, in the sender's local time.
- `ExportTypeCode` = **Permanent**  
  A permanent export: the goods are sold abroad.
- `ExportReasonCode` = **Sale**  
  The reason: a sale to a buyer abroad.
- `Note` = **Grolsofeov polfellae vigaor vevoe cisoov cagroesk.** (languageID `qau`)  
  The note in Urvanian, the sender's language (world/countries.json): How it was declared.
- `Note` = **Declared electronically before the goods leave.** (languageID `en`)  
  The same note in English, the working language between the countries: How it was declared.
- `VersionID` = **1**  
  The first version.

### Exporter Party

Inside `ExporterParty`:

- `WebsiteURI` = **https://www.rinova.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rinova Recovery (world/parties.json).
- `IndustryClassificationCode` = **3830** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rinova Recovery (world/parties.json).
- `PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104548** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Rinova Recovery (world/parties.json).
- `PartyName/Name` = **Rinova Recovery**  
  The trading name; identity of Rinova Recovery (world/parties.json).
- `Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/StreetName` = **Ganluar Bonfuar Panpea** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Rinova Recovery (world/parties.json).
- `PostalAddress/StreetName` = **Via del Riciclo** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Rinova Recovery (world/parties.json).
- `PostalAddress/BuildingNumber` = **31**  
  Building number of the postal address. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/PostalZone` = **4140**  
  Postal code in Urvania's format (4 digits). identity of Rinova Recovery (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Rinova Recovery (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered for value added tax; identity of Rinova Recovery (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007318479**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Rinova Recovery (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Rinova Recovery SRU**  
  The name under which the party is registered, with its legal form; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104548**  
  Number in the Commercial register of Urvania; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Rinova Recovery (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Rinova Recovery (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rinova Recovery (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rinova Recovery (world/parties.json).
- `Contact/Telephone` = **+999 1 4140 4548**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Rinova Recovery (world/parties.json).
- `Contact/ElectronicMail` = **customer@rinova.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rinova Recovery (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rinova Recovery (world/parties.json).
- `PartyAuthorization/PurposeCode` = **R3**  
  The purpose as a code.
- `PartyAuthorization/Purpose` = **Recovery of non-hazardous plastic waste**  
  What the authority has authorized the party to do; identity of Rinova Recovery (world/parties.json).
- `PartyAuthorization/ValidityPeriod/EndDate` = **2029-12-31**  
  The authorization expires on this date.
- `PartyAuthorization/Certificate/ID` = **XU-ENV-2024-0311**  
  The number of the permit.
- `PartyAuthorization/Certificate/CertificateTypeCode` = **Permit**  
  A permit issued by an authority of the party's country.
- `PartyAuthorization/Certificate/CertificateType` = **Operating permit**  
  The kind of certificate, in words.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104548** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rinova Recovery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customs Declaration

Inside `CustomsDeclaration`:

- `ID` = **RR-CD-26-0888**  
  The declaration as lodged with the customs of the exporting country.
- `FunctionCode` = **Original**  
  An original declaration, not an amendment.
- `ValidityPeriod/StartDate` = **2026-04-19**  
  From the declaration.
- `ValidityPeriod/DurationMeasure` = **90** (unitCode `DAY`)  
  The goods must leave within 90 days.
- `ApplicableTerritoryAddress/Country/IdentificationCode` = **XU**  
  The customs territory the goods leave.
- `Shipment/ID` = **RR-SH-26-0889**  
  The shipment declared.
- `Shipment/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight leaving the country.
- `Shipment/Consignment/ID` = **RR-CS-26-0885**  
  The consignment carried.
- `Shipment/Consignment/CarrierParty/WebsiteURI` = **https://www.fiumella.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/IndustryClassificationCode` = **5022** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104959** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Shipment/Consignment/CarrierParty/PartyName/Name` = **Fiumella Barges**  
  The trading name; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Shipment/Consignment/CarrierParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Shipment/Consignment/CarrierParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Shipment/Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Shipment/Consignment/CarrierParty/PostalAddress/StreetName` = **Voncisgroe Bonfuar Lidio** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/StreetName` = **Banchina del Fiume** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/BuildingNumber` = **52**  
  Building number of the postal address. identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/PostalZone` = **4170**  
  Postal code in Urvania's format (4 digits). identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Shipment/Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Shipment/Consignment/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Shipment/Consignment/CarrierParty/PartyTaxScheme/RegistrationName` = **Fiumella Barges SRU**  
  The name under which the party is registered for value added tax; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyTaxScheme/CompanyID` = **XU007347248**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Shipment/Consignment/CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Shipment/Consignment/CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Shipment/Consignment/CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/RegistrationName` = **Fiumella Barges SRU**  
  The name under which the party is registered, with its legal form; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104959**  
  Number in the Commercial register of Urvania; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Shipment/Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Shipment/Consignment/CarrierParty/Contact/Name` = **Chartering desk**  
  The desk that handles this document; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/Contact/Telephone` = **+999 1 4170 4959**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/Contact/ElectronicMail` = **chartering@fiumella.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Fiumella Barges (world/parties.json).
- `Shipment/Consignment/CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Shipment/Consignment/CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104959** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Fiumella Barges (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Recycled PE granulate**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **9984000** (currencyID `XUF`)  
  The value of the granulate, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **120480** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **120** (unitCode `TNE`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.**  
  The seller's description; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Gremefua PE standaboa** (languageID `qau`)  
  The item's name in Urvanian, the seller's language; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Recycled PE granulate** (languageID `en`)  
  The item's name in English, the working language between the countries; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **RR-PE-R1**  
  The seller's own item number; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **771030000048** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/CommodityClassification/NatureCode` = **VII**  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification.
- `Shipment/GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN**  
  The kind of cargo as the parties code it: bulk, or general cargo in packages.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **3901.10** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Density**  
  A measured property of the item.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **0.92** (unitCode `23`)  
  Its measured value; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Recycled content**  
  A measured property of the item.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **100** (unitCode `P1`)  
  Its measured value; item granulate-pe of Rinova Recovery (world/items.json).
- `Shipment/GoodsItem/Item/EnvironmentalCertificate/ID` = **XU-RC-2026-007**  
  The number of the environmental certificate.
- `Shipment/GoodsItem/Item/EnvironmentalCertificate/CertificateTypeCode` = **Recycledcontent**  
  The kind of claim, as a code.
- `Shipment/GoodsItem/Item/EnvironmentalCertificate/CertificateType` = **Recycled content**  
  The environmental claim certified.
- `Shipment/GoodsItem/Item/EnvironmentalCertificate/Remarks` = **Made entirely from sorted production waste recovered in Urvania.**  
  What the certificate states.
- `CustomsExitOfficeLocation/Name` = **Customs post at the river border**  
  Where the goods leave the country.
- `ConsignorParty/PartyIdentification/ID` = **XU-R-104548** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsignorParty/PartyName/Name` = **Rinova Recovery**  
  A party referred to from another party's details: its identifier and name are enough.
- `ConsigneeParty/WebsiteURI` = **https://www.rivermouth.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/IndustryClassificationCode` = **2220** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyIdentification/ID` = **20412740** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ConsigneeParty/AdditionalPartyIdentification/ID` = **XB-TR-412740** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyName/Name` = **Rivermouth Packaging**  
  The trading name; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Language/ID` = **en**  
  English, the language the party does business in.
- `ConsigneeParty/Language/Name` = **English**  
  The language's name.
- `ConsigneeParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `ConsigneeParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `ConsigneeParty/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `ConsigneeParty/PostalAddress/StreetName` = **Estuary Road**  
  Street of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/BuildingNumber` = **28**  
  Building number of the postal address. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/PostalZone` = **38505**  
  Postal code in Bayvarra's format (5 digits). identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `ConsigneeParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `ConsigneeParty/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `ConsigneeParty/PartyTaxScheme/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered for state sales tax; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyTaxScheme/CompanyID` = **CO-1238220**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `ConsigneeParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `ConsigneeParty/PartyLegalEntity/RegistrationName` = **Rivermouth Packaging Ltd**  
  The name under which the party is registered, with its legal form; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyID` = **20412740**  
  Number in the Federal business register of Bayvarra; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `ConsigneeParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
  The registered office, as entered in the register.
- `ConsigneeParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `ConsigneeParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `ConsigneeParty/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/Telephone` = **+999 2 3850 2740**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/ElectronicMail` = **order@rivermouth.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Rivermouth Packaging (world/parties.json).
- `ConsigneeParty/FinancialAccount/ID` = **XB66BLUM0004712805** (schemeID `urn:ubl-examples:world:account`)  
  The party's account, given with its details so that payments can be sent to it. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `ConsigneeParty/FinancialAccount/Name` = **Rivermouth Packaging Ltd**  
  The account holder, as the bank knows it.
- `ConsigneeParty/FinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `ConsigneeParty/FinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `ConsigneeParty/FinancialAccount/CurrencyCode` = **XBL**  
  The account is kept in the currency of the bank's country.
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/ID` = **BLUM-001**  
  The branch that keeps the account.
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUM**  
  The bank code, the part of every account number that names the bank; identity of Bank of Lumeport (world/parties.json).
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  The bank's head office; identity of Bank of Lumeport (world/parties.json).
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Its building number; identity of Bank of Lumeport (world/parties.json).
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  Its town; identity of Bank of Lumeport (world/parties.json).
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB**  
  The bank's country.
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The branch is at the bank's head office.
- `ConsigneeParty/FinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB**  
  Its country.
- `ConsigneeParty/FinancialAccount/Country/IdentificationCode` = **XB**  
  The country where the account is kept.
- `ConsigneeParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ConsigneeParty/ElectronicAddress/ElectronicAddressID` = **XB:20412740** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Rivermouth Packaging (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `CustomsParty/IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CustomsParty/PartyName/Name` = **Customs Administration of Urvania**  
  The trading name; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `CustomsParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `CustomsParty/PostalAddress/AddressTypeCode` = **Postal**  
  The kind of address.
- `CustomsParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `CustomsParty/PostalAddress/Postbox` = **PB 18**  
  The customs office receives its post in a post box. identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/StreetName` = **Lisgaov Cisiar Vulgreor** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/StreetName` = **Valico di Confine** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/BuildingNumber` = **22**  
  Building number of the postal address. identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `CustomsParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `CustomsParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `CustomsParty/PartyTaxScheme/RegistrationName` = **Customs Administration of Urvania**  
  The name under which the party is registered for value added tax; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PartyTaxScheme/CompanyID` = **XU007385602**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `CustomsParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `CustomsParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `CustomsParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `CustomsParty/PartyLegalEntity/RegistrationName` = **Customs Administration of Urvania**  
  The name under which the party is registered, with its legal form; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PartyLegalEntity/CompanyID` = **XU-R-105507**  
  Number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `CustomsParty/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `CustomsParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `CustomsParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `CustomsParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `CustomsParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `CustomsParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `CustomsParty/Contact/Name` = **Border office**  
  The desk that handles this document; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Contact/Telephone` = **+999 1 4120 5507**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Contact/Telefax` = **+999 1 4180 0018**  
  The customs office still lists a fax number; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Contact/ElectronicMail` = **border@customs-xu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Customs Administration of Urvania (world/parties.json).
- `CustomsParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CustomsParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105507** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs Administration of Urvania (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `AdditionalDocumentReference/ID` = **RP-PO-26-0882**  
  The order behind the export.

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
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:plastics</cbc:ProfileID>
  <cbc:ProfileExecutionID>PLASTICS-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>RR-EX-26-0887</cbc:ID>
  <cbc:UUID>9d7cd654-55a1-5b6b-af72-1c8f54670605</cbc:UUID>
  <cbc:IssueDate>2026-04-19</cbc:IssueDate>
  <cbc:IssueTime>16:08:00</cbc:IssueTime>
  <cbc:ExportTypeCode>Permanent</cbc:ExportTypeCode>
  <cbc:ExportReasonCode>Sale</cbc:ExportReasonCode>
  <cbc:Note languageID="qau">Grolsofeov polfellae vigaor vevoe cisoov cagroesk.</cbc:Note>
  <cbc:Note languageID="en">Declared electronically before the goods leave.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:ExporterParty>
    <cbc:WebsiteURI>https://www.rinova.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3830</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104548</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104548</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Rinova Recovery</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>qau</cbc:ID>
      <cbc:Name>Urvanian</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qau">Ganluar Bonfuar Panpea</cbc:StreetName>
      <cbc:StreetName languageID="en">Via del Riciclo</cbc:StreetName>
      <cbc:BuildingNumber>31</cbc:BuildingNumber>
      <cbc:CityName>Ferrano</cbc:CityName>
      <cbc:PostalZone>4140</cbc:PostalZone>
      <cbc:Region>Province of Ferrano</cbc:Region>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        <cbc:Name>Urvania</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
      <cbc:CompanyID>XU007318479</cbc:CompanyID>
      <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>VAT</cbc:ID>
        <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Rinova Recovery SRU</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-104548</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>SRU</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
      <cac:RegistrationAddress>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XU:CR</cbc:ID>
        <cbc:Name>Commercial register of Urvania</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 4140 4548</cbc:Telephone>
      <cbc:ElectronicMail>customer@rinova.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:PartyAuthorization>
      <cbc:PurposeCode>R3</cbc:PurposeCode>
      <cbc:Purpose>Recovery of non-hazardous plastic waste</cbc:Purpose>
      <cac:ValidityPeriod>
        <cbc:EndDate>2029-12-31</cbc:EndDate>
      </cac:ValidityPeriod>
      <cac:Certificate>
        <cbc:ID>XU-ENV-2024-0311</cbc:ID>
        <cbc:CertificateTypeCode>Permit</cbc:CertificateTypeCode>
        <cbc:CertificateType>Operating permit</cbc:CertificateType>
      </cac:Certificate>
    </cac:PartyAuthorization>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104548</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:CustomsDeclaration>
    <cbc:ID>RR-CD-26-0888</cbc:ID>
    <cbc:FunctionCode>Original</cbc:FunctionCode>
    <cac:ValidityPeriod>
      <cbc:StartDate>2026-04-19</cbc:StartDate>
      <cbc:DurationMeasure unitCode="DAY">90</cbc:DurationMeasure>
    </cac:ValidityPeriod>
    <cac:ApplicableTerritoryAddress>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:ApplicableTerritoryAddress>
    <cac:Shipment>
      <cbc:ID>RR-SH-26-0889</cbc:ID>
      <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
      <cac:Consignment>
        <cbc:ID>RR-CS-26-0885</cbc:ID>
        <cac:CarrierParty>
          <cbc:WebsiteURI>https://www.fiumella.example</cbc:WebsiteURI>
          <cbc:IndustryClassificationCode listID="ISIC Rev.4">5022</cbc:IndustryClassificationCode>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104959</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Fiumella Barges</cbc:Name>
          </cac:PartyName>
          <cac:Language>
            <cbc:ID>qau</cbc:ID>
            <cbc:Name>Urvanian</cbc:Name>
          </cac:Language>
          <cac:PostalAddress>
            <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
            <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
            <cbc:StreetName languageID="qau">Voncisgroe Bonfuar Lidio</cbc:StreetName>
            <cbc:StreetName languageID="en">Banchina del Fiume</cbc:StreetName>
            <cbc:BuildingNumber>52</cbc:BuildingNumber>
            <cbc:CityName>Ferrano</cbc:CityName>
            <cbc:PostalZone>4170</cbc:PostalZone>
            <cbc:Region>Province of Ferrano</cbc:Region>
            <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
              <cbc:Name>Urvania</cbc:Name>
            </cac:Country>
          </cac:PostalAddress>
          <cac:PartyTaxScheme>
            <cbc:RegistrationName>Fiumella Barges SRU</cbc:RegistrationName>
            <cbc:CompanyID>XU007347248</cbc:CompanyID>
            <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
            <cac:TaxScheme>
              <cbc:ID>VAT</cbc:ID>
              <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
              <cac:JurisdictionRegionAddress>
                <cac:Country>
                  <cbc:IdentificationCode>XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:JurisdictionRegionAddress>
            </cac:TaxScheme>
          </cac:PartyTaxScheme>
          <cac:PartyLegalEntity>
            <cbc:RegistrationName>Fiumella Barges SRU</cbc:RegistrationName>
            <cbc:CompanyID>XU-R-104959</cbc:CompanyID>
            <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
            <cbc:CompanyLegalFormCode>SRU</cbc:CompanyLegalFormCode>
            <cbc:CompanyLegalForm>Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
            <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
            <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
            <cac:RegistrationAddress>
              <cbc:CityName>Ferrano</cbc:CityName>
              <cac:Country>
                <cbc:IdentificationCode>XU</cbc:IdentificationCode>
              </cac:Country>
            </cac:RegistrationAddress>
            <cac:CorporateRegistrationScheme>
              <cbc:ID>XU:CR</cbc:ID>
              <cbc:Name>Commercial register of Urvania</cbc:Name>
              <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
              <cac:JurisdictionRegionAddress>
                <cac:Country>
                  <cbc:IdentificationCode>XU</cbc:IdentificationCode>
                </cac:Country>
              </cac:JurisdictionRegionAddress>
            </cac:CorporateRegistrationScheme>
          </cac:PartyLegalEntity>
          <cac:Contact>
            <cbc:Name>Chartering desk</cbc:Name>
            <cbc:JobTitle>Operations planner</cbc:JobTitle>
            <cbc:Department>Operations</cbc:Department>
            <cbc:Telephone>+999 1 4170 4959</cbc:Telephone>
            <cbc:ElectronicMail>chartering@fiumella.example</cbc:ElectronicMail>
            <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
          </cac:Contact>
          <cac:ElectronicAddress>
            <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
            <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104959</cbc:ElectronicAddressID>
          </cac:ElectronicAddress>
        </cac:CarrierParty>
      </cac:Consignment>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Recycled PE granulate</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">9984000</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">120480</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="TNE">120</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Polyethylene granulate recovered from production waste, density below 0.94, in jumbo bags of 1 tonne.</cbc:Description>
          <cbc:Name languageID="qau">Gremefua PE standaboa</cbc:Name>
          <cbc:Name languageID="en">Recycled PE granulate</cbc:Name>
          <cac:SellersItemIdentification>
            <cbc:ID>RR-PE-R1</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771030000048</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:NatureCode>VII</cbc:NatureCode>
            <cbc:CargoTypeCode>GEN</cbc:CargoTypeCode>
            <cbc:ItemClassificationCode listID="HS">3901.10</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
          <cac:AdditionalItemProperty>
            <cbc:Name>Density</cbc:Name>
            <cbc:ValueQuantity unitCode="23">0.92</cbc:ValueQuantity>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:Name>Recycled content</cbc:Name>
            <cbc:ValueQuantity unitCode="P1">100</cbc:ValueQuantity>
          </cac:AdditionalItemProperty>
          <cac:EnvironmentalCertificate>
            <cbc:ID>XU-RC-2026-007</cbc:ID>
            <cbc:CertificateTypeCode>Recycledcontent</cbc:CertificateTypeCode>
            <cbc:CertificateType>Recycled content</cbc:CertificateType>
            <cbc:Remarks>Made entirely from sorted production waste recovered in Urvania.</cbc:Remarks>
          </cac:EnvironmentalCertificate>
        </cac:Item>
      </cac:GoodsItem>
    </cac:Shipment>
    <cac:CustomsExitOfficeLocation>
      <cbc:Name>Customs post at the river border</cbc:Name>
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
      <cbc:WebsiteURI>https://www.rivermouth.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">2220</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412740</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412740</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Rivermouth Packaging</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Estuary Road</cbc:StreetName>
        <cbc:BuildingNumber>28</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38505</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
        <cbc:CompanyID>CO-1238220</cbc:CompanyID>
        <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
          <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Rivermouth Packaging Ltd</cbc:RegistrationName>
        <cbc:CompanyID>20412740</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XB:FBR</cbc:ID>
          <cbc:Name>Federal business register of Bayvarra</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 3850 2740</cbc:Telephone>
        <cbc:ElectronicMail>order@rivermouth.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:FinancialAccount>
        <cbc:ID schemeID="urn:ubl-examples:world:account">XB66BLUM0004712805</cbc:ID>
        <cbc:Name>Rivermouth Packaging Ltd</cbc:Name>
        <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
        <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
        <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
        <cac:FinancialInstitutionBranch>
          <cbc:ID>BLUM-001</cbc:ID>
          <cbc:Name>Main branch</cbc:Name>
          <cac:FinancialInstitution>
            <cbc:ID>BLUM</cbc:ID>
            <cbc:Name>Bank of Lumeport</cbc:Name>
            <cac:Address>
              <cbc:StreetName>Exchange Street</cbc:StreetName>
              <cbc:BuildingNumber>48</cbc:BuildingNumber>
              <cbc:CityName>Lumeport</cbc:CityName>
              <cac:Country>
                <cbc:IdentificationCode>XB</cbc:IdentificationCode>
              </cac:Country>
            </cac:Address>
          </cac:FinancialInstitution>
          <cac:Address>
            <cbc:CityName>Lumeport</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode>XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitutionBranch>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:FinancialAccount>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412740</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:ConsigneeParty>
    <cac:CustomsParty>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105507</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Customs Administration of Urvania</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qau</cbc:ID>
        <cbc:Name>Urvanian</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Postal</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:Postbox>PB 18</cbc:Postbox>
        <cbc:StreetName languageID="qau">Lisgaov Cisiar Vulgreor</cbc:StreetName>
        <cbc:StreetName languageID="en">Valico di Confine</cbc:StreetName>
        <cbc:BuildingNumber>22</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Customs Administration of Urvania</cbc:RegistrationName>
        <cbc:CompanyID>XU007385602</cbc:CompanyID>
        <cbc:TaxLevelCode>National</cbc:TaxLevelCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
          <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Customs Administration of Urvania</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-105507</cbc:CompanyID>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cac:RegistrationAddress>
          <cbc:CityName>Ferrano</cbc:CityName>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:Country>
        </cac:RegistrationAddress>
        <cac:CorporateRegistrationScheme>
          <cbc:ID>XU:CR</cbc:ID>
          <cbc:Name>Commercial register of Urvania</cbc:Name>
          <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
          <cac:JurisdictionRegionAddress>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:JurisdictionRegionAddress>
        </cac:CorporateRegistrationScheme>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Border office</cbc:Name>
        <cbc:JobTitle>Public service officer</cbc:JobTitle>
        <cbc:Department>Public services</cbc:Department>
        <cbc:Telephone>+999 1 4120 5507</cbc:Telephone>
        <cbc:Telefax>+999 1 4180 0018</cbc:Telefax>
        <cbc:ElectronicMail>border@customs-xu.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105507</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CustomsParty>
    <cac:AdditionalDocumentReference>
      <cbc:ID>RP-PO-26-0882</cbc:ID>
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
