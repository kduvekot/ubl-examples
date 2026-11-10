# Certificate of Origin: Ferrano Chamber of Commerce to Lumeway Distribution

*Example 7 of the flow "Finished goods by truck across the land border (Urvania → Bayvarra)" · [Certificate of Origin in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CERTIFICATE-OF-ORIGIN-SCHEMA)*

The chamber endorses the certificate and makes it available to the importer, who needs it for the import declaration.

[The XML file](07-CertificateOfOrigin.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:road**  
  The business process the document belongs to: the flow "Finished goods by truck across the land border (Urvania → Bayvarra)".
- `ProfileExecutionID` = **ROAD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FCC-CO-26-0157**  
  The number of the certificate, given by the chamber.
- `UUID` = **3152b116-509a-5a0d-8b57-97a8e2b066d0**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-22**  
  The day the chamber endorsed the certificate.
- `IssueTime` = **08:41:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Description` = **Certificate of origin for park benches and castings made in Urvania.**  
  What the certificate is for.
- `Note` = **Preferential origin under the trade accord.**  
  What the certificate is for.
- `VersionID` = **1**  
  The first version.

### Signature

Inside `Signature`:

- `ID` = **FCC-SIG-CO-07**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

### Exporter Party

Inside `ExporterParty`:

- `WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json).
- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
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
- `Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Contact/Telephone` = **+999 1 4120 4274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Valdara Industries (world/parties.json).
- `Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Contact/OtherCommunication/ChannelCode` = **AL**  
  UN/EDIFACT 3155 code AL: cellular phone.
- `Contact/OtherCommunication/Value` = **+999 1 7000 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Importer Party

Inside `ImporterParty`:

- `WebsiteURI` = **https://www.lumeway.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Lumeway Distribution (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Lumeway Distribution (world/parties.json).
- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XB-TR-410274** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/AdditionalStreetName` = **Gate 3**  
  The gate of the business park to use. identity of Lumeway Distribution (world/parties.json).
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
  The state, part of an address in federal Bayvarra. identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Lumeway Distribution (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered for state sales tax; identity of Lumeway Distribution (world/parties.json).
- `PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeway Distribution (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Lumeway Distribution Ltd**  
  The name under which the party is registered, with its legal form; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1988-10-03**  
  The day the company was entered in the register; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Medium**  
  The size class of the company (micro, small, medium or large); identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/CorporateStockAmount` = **2500000** (currencyID `XBL`)  
  The share capital, in lume; identity of Lumeway Distribution (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Lumeway Distribution (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Lumeway Distribution (world/parties.json).
- `Contact/Telephone` = **+999 2 7121 0274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Lumeway Distribution (world/parties.json).
- `Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Endorser Party

Inside `EndorserParty`:

- `RoleCode` = **Chamber**  
  The endorser is the chamber of commerce of the exporting country.
- `SequenceNumeric` = **1**  
  The first and only endorsement.
- `Party/IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Piazza del Mercato**  
  Street of the postal address. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered for value added tax; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007376017**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered, with its legal form; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-105370**  
  Number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Party/Contact/Name` = **Certificates office**  
  The desk that handles this document; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4110 5370**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/ElectronicMail` = **certificates@camera-ferrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105370** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.

### Certificate of Origin Application

Inside `CertificateOfOriginApplication`:

- `ReferenceID` = **VI-AP-26-0158**  
  The exporter's reference for its application.
- `CertificateType` = **Preferential**  
  The goods qualify for the preferential duty rate in Bayvarra; the importer needs this certificate to claim it.
- `ApplicationStatusCode` = **Approved**  
  The chamber has approved the application.
- `OriginalJobID` = **LD-PO-26-0149**  
  The order the goods are for.
- `PreviousJobID` = **VI-CO-25-0412**  
  The exporter's application of last year for the same goods.
- `Remarks` = **Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.**  
  Why the goods are of Urvanian origin.
- `Shipment/ID` = **CL-SH-26-0154**  
  The shipment the certificate covers.
- `Shipment/GoodsItem/ID` = **1**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **4790400** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **3984** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **96** (unitCode `H87`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.**  
  The seller's description; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.**  
  What comes with the item; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Keyword` = **park bench**  
  A word buyers search the item by.
- `Shipment/GoodsItem/Item/Keyword` = **street furniture**  
  A word buyers search the item by.
- `Shipment/GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/ModelName` = **Serra 180**  
  The model; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/WarrantyInformation` = **Five years on the frame against corrosion.**  
  The maker's warranty; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **Colour**  
  The attribute the variant differs in.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM**  
  The part of the item the attribute is on: the frame.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY**  
  The variant's code for it.
- `Shipment/GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label.
- `Shipment/GoodsItem/Item/StandardItemIdentification/IssuerScopeID` = **771**  
  The range of item numbers the agency gives out in the maker's country.
- `Shipment/GoodsItem/Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **9401.79.10**  
  The national tariff code below the HS subheading, as the customs of the maker's country uses it.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-serra of Valdara Industries (world/items.json).
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
  The colours the frame is offered in.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **Optional**  
  How much the property matters in describing the item.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  One of the values the property can take.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ListValue` = **Moss green**  
  One of the values the property can take.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **APP**  
  The group of properties this one belongs to.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Appearance**  
  The group's name.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **Optional**  
  How much the group matters.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ID` = **LOAD**  
  The maker's identifier for the property.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/Name` = **Load capacity**  
  A property buyers ask about.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/NameCode` = **LOAD**  
  The property's name as a code, as the property standard lists it.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/TestMethod` = **Static load on the seat for one hour, three seats loaded evenly, no lasting deformation**  
  How the value is tested.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **450** (unitCode `KGM`)  
  Its measured value; item bench-serra of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ValueQualifier` = **Distributed over the seat**  
  What the value stands for.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **Mandatory**  
  How much the property matters in describing the item.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **SAF**  
  The group of properties this one belongs to.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Safety**  
  The group's name.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **Mandatory**  
  How much the group matters.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-SF-0450**  
  The property's number in the property standard of the identification agency.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **Codana street furniture properties**  
  The part of the agency's standards it is taken from.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **Length**  
  Which dimension.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Over the armrests**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **Depth**  
  Which dimension.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **620** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **Height**  
  Which dimension.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **780** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Seat back at its highest point**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/AttributeID` = **Seat height**  
  Which dimension.
- `Shipment/GoodsItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `Shipment/GoodsItem/Item/Dimension/Description` = **Above the ground when anchored**  
  Where it is measured.
- `Shipment/GoodsItem/Item/Dimension/MinimumMeasure` = **440** (unitCode `MMT`)  
  The lowest it can be set to.
- `Shipment/GoodsItem/Item/Dimension/MaximumMeasure` = **460** (unitCode `MMT`)  
  The highest it can be set to.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2e**  
  The emission reported: greenhouse gases as CO2 equivalent.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueMeasure` = **96** (unitCode `KGM`)  
  The emission of one item.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueFactorNumeric` = **0.82**  
  The share of the footprint the steel frame accounts for.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/ValueBaseMeasure` = **1** (unitCode `H87`)  
  The emission is per one bench.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/LifecycleStageCode` = **Manufacturing**  
  The part of the bench's life the figure covers.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/LifecycleStageDescription` = **From the ore at the mine to the bench leaving the factory gate.**  
  That part in words.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/Description` = **Mining, steel making, casting, galvanising, sawing and the transport between them.**  
  What the figure includes.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **Calculated**  
  Calculated, not measured.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **Cradle to gate**  
  How much of the chain is included.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **The steelworks' and sawmill's measured energy use of 2025**  
  Where the factors come from.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `Shipment/GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Shipment/GoodsItem/Item/CircularityProfile/MaintenanceFrequencyCode` = **Yearly**  
  How often the item needs maintenance.
- `Shipment/GoodsItem/Item/CircularityProfile/MaintenanceFrequencyDescription` = **Tighten the slat bolts and touch up the coating once a year.**  
  What the maintenance is.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **Steel**  
  A material the item is made of.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **34** (unitCode `KGM`)  
  How much of it one item uses.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Steel made from Serravona ore in Urvania**  
  Where the material comes from.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **Hardwood**  
  A material the item is made of.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **22.5** (unitCode `KGM`)  
  How much of it one item uses.
- `Shipment/GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Slats from Upland State, Bayvarra**  
  Where the material comes from.
- `Shipment/GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeCode` = **Packaging**  
  The kind of waste the item leaves.
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
- `Shipment/GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoringSystemCode` = **Repairability index, 0–10**  
  The scale of the score.
- `Shipment/GoodsItem/Item/CircularityProfile/ProductDocumentationDocumentReference/ID` = **VI-RM-B180**  
  The repair and maintenance manual.
- `Shipment/GoodsItem/ID` = **2**  
  The goods item number.
- `Shipment/GoodsItem/Description` = **Bench side frame casting**  
  What the goods are, in words.
- `Shipment/GoodsItem/DeclaredCustomsValueAmount` = **71760** (currencyID `XUF`)  
  The value of the goods, in ferra.
- `Shipment/GoodsItem/GrossWeightMeasure` = **122.4** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `Shipment/GoodsItem/Quantity` = **12** (unitCode `H87`)  
  The quantity declared.
- `Shipment/GoodsItem/Item/Description` = **Replacement side frame for the Serra bench, cast steel, galvanised.**  
  The seller's description; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/Name` = **Bench side frame casting**  
  The item's short name; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/ModelName` = **Serra 180 side frame**  
  The model; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/SellersItemIdentification/ID` = **VI-C180**  
  The seller's own item number; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/StandardItemIdentification/ID` = **771020000034** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json).
- `Shipment/GoodsItem/Item/CommodityClassification/CommodityCode` = **7325.99.90**  
  The national tariff code below the HS subheading, as the customs of the maker's country uses it.
- `Shipment/GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **7325.99** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-casting of Valdara Industries (world/items.json).
- `EndorserParty/RoleCode` = **Chamber**  
  The endorser is the chamber of commerce of the exporting country.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.
- `PreparationParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `PreparationParty/PartyName/Name` = **Valdara Industries**  
  The same party as at ExporterParty, where its full details are given; only its identifier and name are repeated.
- `IssuerParty/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `IssuerParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `ExporterParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ExporterParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `ImporterParty/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `ImporterParty/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `IssuingCountry/IdentificationCode` = **XU**  
  The goods were made in Urvania, and the certificate is issued there.
- `DocumentDistribution/ID` = **1**  
  The importer's copy.
- `DocumentDistribution/DistributionTypeCode` = **Electronic**  
  As this document.
- `DocumentDistribution/Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `DocumentDistribution/Party/PartyName/Name` = **Lumeway Distribution**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupportingDocumentReference/ID` = **LD-PO-26-0149**  
  The commercial document behind the goods.
- `Signature/ID` = **VI-SIG-COA**  
  The sender's electronic seal.
- `Signature/SignatoryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Issuer Endorsement

Inside `IssuerEndorsement`:

- `DocumentID` = **FCC-CO-26-0157**  
  The certificate this endorsement belongs to.
- `ApprovalStatus` = **Approved**  
  The chamber has endorsed the certificate.
- `Remarks` = **Origin verified against the exporter's production records.**  
  What the chamber checked.
- `EndorserParty/RoleCode` = **Chamber**  
  The endorser is the chamber of commerce of the exporting country.
- `EndorserParty/SequenceNumeric` = **1**  
  The first and only endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at EndorserParty/Party, where its full details are given; only its identifier and name are repeated.
- `EndorserParty/SignatoryContact/Name` = **Certificates office**  
  The office of the chamber that signs certificates of origin.
- `Signature/ID` = **FCC-SIG-26-0309**  
  The sender's electronic seal.
- `Signature/SignatoryParty/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

### Embassy Endorsement

Inside `EmbassyEndorsement`:

- `DocumentID` = **FCC-CO-26-0157**  
  The certificate legalised.
- `ApprovalStatus` = **Legalised**  
  The trade accord council confirms the chamber's signature.
- `Remarks` = **Signature of the Ferrano chamber confirmed.**  
  What was checked.
- `EndorserParty/RoleCode` = **Legalisation**  
  The council legalises.
- `EndorserParty/SequenceNumeric` = **2**  
  After the chamber.
- `EndorserParty/Party/PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/Party/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/SignatoryContact/Name` = **Legalisation desk**  
  The council's desk that signs.
- `Signature/ID` = **LTAC-SIG-26-0311**  
  The sender's electronic seal.
- `Signature/SignatoryParty/PartyIdentification/ID` = **20411096** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Signature/SignatoryParty/PartyName/Name` = **Lumeport Trade Accord Council**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CertificateOfOrigin xmlns="urn:oasis:names:specification:ubl:schema:xsd:CertificateOfOrigin-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:road</cbc:ProfileID>
  <cbc:ProfileExecutionID>ROAD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FCC-CO-26-0157</cbc:ID>
  <cbc:UUID>3152b116-509a-5a0d-8b57-97a8e2b066d0</cbc:UUID>
  <cbc:IssueDate>2026-03-22</cbc:IssueDate>
  <cbc:IssueTime>08:41:00</cbc:IssueTime>
  <cbc:Description>Certificate of origin for park benches and castings made in Urvania.</cbc:Description>
  <cbc:Note>Preferential origin under the trade accord.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:Signature>
    <cbc:ID>FCC-SIG-CO-07</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:ExporterParty>
    <cbc:WebsiteURI>https://www.valdara.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3100</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:customs-trader">XU-TR-104274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:StreetName>Via delle Officine</cbc:StreetName>
      <cbc:BuildingNumber>17</cbc:BuildingNumber>
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
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID>XU007299291</cbc:CompanyID>
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
      <cbc:RegistrationName>Valdara Industries SUA</cbc:RegistrationName>
      <cbc:CompanyID>XU-R-104274</cbc:CompanyID>
      <cbc:RegistrationDate>1962-04-12</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
      <cbc:CorporateStockAmount currencyID="XUF">250000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
      <cbc:Name>Order desk</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 1 4120 4274</cbc:Telephone>
      <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      <cac:OtherCommunication>
        <cbc:ChannelCode>AL</cbc:ChannelCode>
        <cbc:Value>+999 1 7000 4274</cbc:Value>
      </cac:OtherCommunication>
    </cac:Contact>
    <cac:ServiceProviderParty>
      <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Castrano Logistics</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:ServiceProviderParty>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ExporterParty>
  <cac:ImporterParty>
    <cbc:WebsiteURI>https://www.lumeway.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-410274</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Distribution Drive</cbc:StreetName>
      <cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>
      <cbc:BlockName>Marrowdale Business Park</cbc:BlockName>
      <cbc:BuildingNumber>43</cbc:BuildingNumber>
      <cbc:PlotIdentification>Plot 14</cbc:PlotIdentification>
      <cbc:CityName>Marrowdale</cbc:CityName>
      <cbc:PostalZone>71214</cbc:PostalZone>
      <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID>UL-1230822</cbc:CompanyID>
      <cbc:TaxLevelCode>State</cbc:TaxLevelCode>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
        <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
        <cac:JurisdictionRegionAddress>
          <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Lumeway Distribution Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20410274</cbc:CompanyID>
      <cbc:RegistrationDate>1988-10-03</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Medium</cbc:EntitySizeCode>
      <cbc:CorporateStockAmount currencyID="XBL">2500000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
      <cac:RegistrationAddress>
        <cbc:CityName>Marrowdale</cbc:CityName>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 7121 0274</cbc:Telephone>
      <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImporterParty>
  <cac:EndorserParty>
    <cbc:RoleCode>Chamber</cbc:RoleCode>
    <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
    <cac:Party>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">9411</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Piazza del Mercato</cbc:StreetName>
        <cbc:BuildingNumber>15</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4110</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
        <cbc:CompanyID>XU007376017</cbc:CompanyID>
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
        <cbc:RegistrationName>Ferrano Chamber of Commerce</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-105370</cbc:CompanyID>
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
        <cbc:Name>Certificates office</cbc:Name>
        <cbc:JobTitle>Public service officer</cbc:JobTitle>
        <cbc:Department>Public services</cbc:Department>
        <cbc:Telephone>+999 1 4110 5370</cbc:Telephone>
        <cbc:ElectronicMail>certificates@camera-ferrano.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105370</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
    <cac:SignatoryContact>
      <cbc:Name>Certificates office</cbc:Name>
    </cac:SignatoryContact>
  </cac:EndorserParty>
  <cac:CertificateOfOriginApplication>
    <cbc:ReferenceID>VI-AP-26-0158</cbc:ReferenceID>
    <cbc:CertificateType>Preferential</cbc:CertificateType>
    <cbc:ApplicationStatusCode>Approved</cbc:ApplicationStatusCode>
    <cbc:OriginalJobID>LD-PO-26-0149</cbc:OriginalJobID>
    <cbc:PreviousJobID>VI-CO-25-0412</cbc:PreviousJobID>
    <cbc:Remarks>Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.</cbc:Remarks>
    <cac:Shipment>
      <cbc:ID>CL-SH-26-0154</cbc:ID>
      <cac:GoodsItem>
        <cbc:ID>1</cbc:ID>
        <cbc:Description>Park bench Serra 180</cbc:Description>
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">4790400</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">3984</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="H87">96</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.</cbc:Description>
          <cbc:Name>Park bench Serra 180</cbc:Name>
          <cbc:AdditionalInformation>Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
          <cbc:Keyword>park bench</cbc:Keyword>
          <cbc:Keyword>street furniture</cbc:Keyword>
          <cbc:BrandName>Valdara</cbc:BrandName>
          <cbc:ModelName>Serra 180</cbc:ModelName>
          <cbc:WarrantyInformation>Five years on the frame against corrosion.</cbc:WarrantyInformation>
          <cac:SellersItemIdentification>
            <cbc:ID>VI-B180</cbc:ID>
            <cbc:ExtendedID>GRY</cbc:ExtendedID>
            <cac:PhysicalAttribute>
              <cbc:AttributeID>Colour</cbc:AttributeID>
              <cbc:PositionCode>FRM</cbc:PositionCode>
              <cbc:DescriptionCode>GRY</cbc:DescriptionCode>
              <cbc:Description>Frame in Ferro grey</cbc:Description>
            </cac:PhysicalAttribute>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
            <cbc:BarcodeSymbologyID>Code128</cbc:BarcodeSymbologyID>
            <cbc:IssuerScopeID>771</cbc:IssuerScopeID>
          </cac:StandardItemIdentification>
          <cac:ItemSpecificationDocumentReference>
            <cbc:ID>VI-DS-B180</cbc:ID>
          </cac:ItemSpecificationDocumentReference>
          <cac:OriginCountry>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:CommodityCode>9401.79.10</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="HS">9401.79</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
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
            <cbc:ImportanceCode>Optional</cbc:ImportanceCode>
            <cbc:ListValue>Ferro grey</cbc:ListValue>
            <cbc:ListValue>Moss green</cbc:ListValue>
            <cac:ItemPropertyGroup>
              <cbc:ID>APP</cbc:ID>
              <cbc:Name>Appearance</cbc:Name>
              <cbc:ImportanceCode>Optional</cbc:ImportanceCode>
            </cac:ItemPropertyGroup>
          </cac:AdditionalItemProperty>
          <cac:AdditionalItemProperty>
            <cbc:ID>LOAD</cbc:ID>
            <cbc:Name>Load capacity</cbc:Name>
            <cbc:NameCode>LOAD</cbc:NameCode>
            <cbc:TestMethod>Static load on the seat for one hour, three seats loaded evenly, no lasting deformation</cbc:TestMethod>
            <cbc:ValueQuantity unitCode="KGM">450</cbc:ValueQuantity>
            <cbc:ValueQualifier>Distributed over the seat</cbc:ValueQualifier>
            <cbc:ImportanceCode>Mandatory</cbc:ImportanceCode>
            <cac:ItemPropertyGroup>
              <cbc:ID>SAF</cbc:ID>
              <cbc:Name>Safety</cbc:Name>
              <cbc:ImportanceCode>Mandatory</cbc:ImportanceCode>
            </cac:ItemPropertyGroup>
            <cac:StandardPropertyIdentification>
              <cbc:ID>UR-SF-0450</cbc:ID>
              <cbc:IssuerScopeID>Codana street furniture properties</cbc:IssuerScopeID>
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
          <cac:Dimension>
            <cbc:AttributeID>Length</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">1800</cbc:Measure>
            <cbc:Description>Over the armrests</cbc:Description>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID>Depth</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">620</cbc:Measure>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID>Height</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">780</cbc:Measure>
            <cbc:Description>Seat back at its highest point</cbc:Description>
          </cac:Dimension>
          <cac:Dimension>
            <cbc:AttributeID>Seat height</cbc:AttributeID>
            <cbc:Measure unitCode="MMT">450</cbc:Measure>
            <cbc:Description>Above the ground when anchored</cbc:Description>
            <cbc:MinimumMeasure unitCode="MMT">440</cbc:MinimumMeasure>
            <cbc:MaximumMeasure unitCode="MMT">460</cbc:MaximumMeasure>
          </cac:Dimension>
          <cac:EnvironmentalEmission>
            <cbc:EnvironmentalEmissionTypeCode>CO2e</cbc:EnvironmentalEmissionTypeCode>
            <cbc:ValueMeasure unitCode="KGM">96</cbc:ValueMeasure>
            <cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>
            <cbc:ValueBaseMeasure unitCode="H87">1</cbc:ValueBaseMeasure>
            <cbc:EmissionStandardReference>Greenhouse Gas Protocol Product Standard</cbc:EmissionStandardReference>
            <cbc:LifecycleStageCode>Manufacturing</cbc:LifecycleStageCode>
            <cbc:LifecycleStageDescription>From the ore at the mine to the bench leaving the factory gate.</cbc:LifecycleStageDescription>
            <cbc:Description>Mining, steel making, casting, galvanising, sawing and the transport between them.</cbc:Description>
            <cac:EmissionCalculationMethod>
              <cbc:CalculationMethodCode>Calculated</cbc:CalculationMethodCode>
              <cbc:FullnessIndicationCode>Cradle to gate</cbc:FullnessIndicationCode>
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
            <cbc:MaintenanceFrequencyCode>Yearly</cbc:MaintenanceFrequencyCode>
            <cbc:MaintenanceFrequencyDescription>Tighten the slat bolts and touch up the coating once a year.</cbc:MaintenanceFrequencyDescription>
            <cac:ResourceConsumption>
              <cbc:ResourceTypeCode>Steel</cbc:ResourceTypeCode>
              <cbc:ConsumptionMeasure unitCode="KGM">34</cbc:ConsumptionMeasure>
              <cbc:ResourceOriginDescription>Steel made from Serravona ore in Urvania</cbc:ResourceOriginDescription>
            </cac:ResourceConsumption>
            <cac:ResourceConsumption>
              <cbc:ResourceTypeCode>Hardwood</cbc:ResourceTypeCode>
              <cbc:ConsumptionMeasure unitCode="KGM">22.5</cbc:ConsumptionMeasure>
              <cbc:ResourceOriginDescription>Slats from Upland State, Bayvarra</cbc:ResourceOriginDescription>
            </cac:ResourceConsumption>
            <cac:WasteGenerated>
              <cbc:WasteTypeCode>Packaging</cbc:WasteTypeCode>
              <cbc:WasteTypeDescription>Stretch film and pallet straps, per bench</cbc:WasteTypeDescription>
              <cbc:WasteMeasure unitCode="KGM">0.4</cbc:WasteMeasure>
              <cac:MeasurementPeriod>
                <cbc:StartDate>2025-01-01</cbc:StartDate>
                <cbc:EndDate>2025-12-31</cbc:EndDate>
              </cac:MeasurementPeriod>
            </cac:WasteGenerated>
            <cac:RepairabilityScore>
              <cbc:ScoreNumeric>8</cbc:ScoreNumeric>
              <cbc:ScoringSystemCode>Repairability index, 0–10</cbc:ScoringSystemCode>
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
        <cbc:DeclaredCustomsValueAmount currencyID="XUF">71760</cbc:DeclaredCustomsValueAmount>
        <cbc:GrossWeightMeasure unitCode="KGM">122.4</cbc:GrossWeightMeasure>
        <cbc:Quantity unitCode="H87">12</cbc:Quantity>
        <cac:Item>
          <cbc:Description>Replacement side frame for the Serra bench, cast steel, galvanised.</cbc:Description>
          <cbc:Name>Bench side frame casting</cbc:Name>
          <cbc:BrandName>Valdara</cbc:BrandName>
          <cbc:ModelName>Serra 180 side frame</cbc:ModelName>
          <cac:SellersItemIdentification>
            <cbc:ID>VI-C180</cbc:ID>
          </cac:SellersItemIdentification>
          <cac:StandardItemIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:item">771020000034</cbc:ID>
          </cac:StandardItemIdentification>
          <cac:OriginCountry>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          </cac:OriginCountry>
          <cac:CommodityClassification>
            <cbc:CommodityCode>7325.99.90</cbc:CommodityCode>
            <cbc:ItemClassificationCode listID="HS">7325.99</cbc:ItemClassificationCode>
          </cac:CommodityClassification>
        </cac:Item>
      </cac:GoodsItem>
    </cac:Shipment>
    <cac:EndorserParty>
      <cbc:RoleCode>Chamber</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Certificates office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:PreparationParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:PreparationParty>
    <cac:IssuerParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:IssuerParty>
    <cac:ExporterParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:ExporterParty>
    <cac:ImporterParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:ImporterParty>
    <cac:IssuingCountry>
      <cbc:IdentificationCode>XU</cbc:IdentificationCode>
    </cac:IssuingCountry>
    <cac:DocumentDistribution>
      <cbc:ID>1</cbc:ID>
      <cbc:DistributionTypeCode>Electronic</cbc:DistributionTypeCode>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeway Distribution</cbc:Name>
        </cac:PartyName>
      </cac:Party>
    </cac:DocumentDistribution>
    <cac:SupportingDocumentReference>
      <cbc:ID>LD-PO-26-0149</cbc:ID>
    </cac:SupportingDocumentReference>
    <cac:Signature>
      <cbc:ID>VI-SIG-COA</cbc:ID>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
  </cac:CertificateOfOriginApplication>
  <cac:IssuerEndorsement>
    <cbc:DocumentID>FCC-CO-26-0157</cbc:DocumentID>
    <cbc:ApprovalStatus>Approved</cbc:ApprovalStatus>
    <cbc:Remarks>Origin verified against the exporter's production records.</cbc:Remarks>
    <cac:EndorserParty>
      <cbc:RoleCode>Chamber</cbc:RoleCode>
      <cbc:SequenceNumeric>1</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Certificates office</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:Signature>
      <cbc:ID>FCC-SIG-26-0309</cbc:ID>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
  </cac:IssuerEndorsement>
  <cac:EmbassyEndorsement>
    <cbc:DocumentID>FCC-CO-26-0157</cbc:DocumentID>
    <cbc:ApprovalStatus>Legalised</cbc:ApprovalStatus>
    <cbc:Remarks>Signature of the Ferrano chamber confirmed.</cbc:Remarks>
    <cac:EndorserParty>
      <cbc:RoleCode>Legalisation</cbc:RoleCode>
      <cbc:SequenceNumeric>2</cbc:SequenceNumeric>
      <cac:Party>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
        </cac:PartyName>
      </cac:Party>
      <cac:SignatoryContact>
        <cbc:Name>Legalisation desk</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
    <cac:Signature>
      <cbc:ID>LTAC-SIG-26-0311</cbc:ID>
      <cac:SignatoryParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411096</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Trade Accord Council</cbc:Name>
        </cac:PartyName>
      </cac:SignatoryParty>
    </cac:Signature>
  </cac:EmbassyEndorsement>
</CertificateOfOrigin>
```
