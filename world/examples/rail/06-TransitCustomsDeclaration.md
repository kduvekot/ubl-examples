# Transit Customs Declaration: Valdara Industries to Customs Administration of Urvania

*Example 6 of the flow "Containers by rail under transit (Urvania → Bayvarra)" · [Transit Customs Declaration in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSIT-CUSTOMS-DECLARATION-SCHEMA)*

The goods travel under customs transit from Urvania to the destination in Bayvarra; the manufacturer, as holder of the procedure, lodges the declaration at the office of departure.

[The XML file](06-TransitCustomsDeclaration.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:rail**  
  The business process the document belongs to: the flow "Containers by rail under transit (Urvania → Bayvarra)".
- `ProfileExecutionID` = **RAIL-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VI-TD-26-0331**  
  The transit declaration number.
- `UUID` = **39a0d3b7-c2fe-5e50-8ee2-54287be65033**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-14**  
  Lodged at the office of departure before the train leaves.
- `IssueTime` = **17:29:00**  
  The time the sender's system issued the document, in the sender's local time.

### Transit Exporter Party

Inside `TransitExporterParty`:

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

### Consignor Party

Inside `ConsignorParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at TransitExporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at TransitExporterParty, where its full details are given; only its identifier and name are repeated.

### Consignee Party

Inside `ConsigneeParty`:

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

### Customs Party

Inside `CustomsParty`:

- `IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Customs Administration of Urvania (world/parties.json).
- `PartyIdentification/ID` = **XU-R-105507** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Customs Administration of Urvania**  
  The trading name; identity of Customs Administration of Urvania (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/Postbox` = **PB 18**  
  The customs office receives its post in a post box. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/StreetName` = **Valico di Confine**  
  Street of the postal address. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/BuildingNumber` = **22**  
  Building number of the postal address. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Customs Administration of Urvania (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Customs Administration of Urvania**  
  The name under which the party is registered for value added tax; identity of Customs Administration of Urvania (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007385602**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Customs Administration of Urvania (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Customs Administration of Urvania**  
  The name under which the party is registered, with its legal form; identity of Customs Administration of Urvania (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-105507**  
  Number in the Commercial register of Urvania; identity of Customs Administration of Urvania (world/parties.json).
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
- `Contact/Name` = **Border office**  
  The desk that handles this document; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Telephone` = **+999 1 4120 5507**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Telefax` = **+999 1 4180 0018**  
  The customs office still lists a fax number; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/ElectronicMail` = **border@customs-xu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Customs Administration of Urvania (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Customs Administration of Urvania (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105507** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Customs Administration of Urvania (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **VI-SH-26-0332**  
  The shipment under transit.
- `GrossWeightMeasure` = **7968** (unitCode `KGM`)  
  The gross weight under transit.
- `Consignment/ID` = **VI-CS-26-0327**  
  The consignment on the train.
- `Consignment/CarrierParty/WebsiteURI` = **https://www.ferranorail.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/IndustryClassificationCode` = **4912** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Consignment/CarrierParty/PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/Language/ID` = **en**  
  English, the language the party does business in.
- `Consignment/CarrierParty/Language/Name` = **English**  
  The language's name.
- `Consignment/CarrierParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Consignment/CarrierParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Consignment/CarrierParty/PostalAddress/StreetName` = **Viale della Stazione**  
  Street of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/CityName` = **Serravona**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Consignment/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Consignment/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Consignment/CarrierParty/PartyTaxScheme/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered for value added tax; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PartyTaxScheme/CompanyID` = **XU007328060**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Consignment/CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered, with its legal form; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104685**  
  Number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Consignment/CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `Consignment/CarrierParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
  The registered office, as entered in the register.
- `Consignment/CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Consignment/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Consignment/CarrierParty/Contact/Name` = **Freight desk**  
  The desk that handles this document; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/Contact/Telephone` = **+999 1 4150 4685**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/Contact/ElectronicMail` = **freight@ferranorail.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Rail Cargo (world/parties.json).
- `Consignment/CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Consignment/CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Rail Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **FRCU1044171** (schemeID `ISO6346`)  
  The container's number: owner code, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReferencedConsignmentID` = **VI-CS-26-0327**  
  The consignment the container carries.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45G1**  
  ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL**  
  A full container load for one consignee.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **7884** (unitCode `KGM`)  
  Half the benches and the container's own 3,900 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **XU-VI-30411**  
  The number of the bolt seal on the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **Shipper**  
  The seal was issued by the shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/Condition` = **Intact**  
  As found at the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealStatusCode` = **Applied**  
  The seal is in place.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  And put on by the shipper when it packed the container.
- `Consignment/TransportHandlingUnit/TransportEquipment/ID` = **FRCU1044187** (schemeID `ISO6346`)  
  The container's number: owner code, U for a freight container, six digits and the ISO 6346 check digit.
- `Consignment/TransportHandlingUnit/TransportEquipment/ReferencedConsignmentID` = **VI-CS-26-0327**  
  The consignment the container carries.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentTypeCode` = **CN** (listID `UN/EDIFACT EDED 8053`)  
  UN/EDIFACT 8053 code CN: container.
- `Consignment/TransportHandlingUnit/TransportEquipment/SizeTypeCode` = **45G1**  
  ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose.
- `Consignment/TransportHandlingUnit/TransportEquipment/FullnessIndicationCode` = **FCL**  
  A full container load for one consignee.
- `Consignment/TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **7884** (unitCode `KGM`)  
  Half the benches and the container's own 3,900 kg.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/ID` = **XU-VI-30412**  
  The number of the bolt seal on the doors.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealIssuerTypeCode` = **Shipper**  
  The seal was issued by the shipper.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/Condition` = **Intact**  
  As found at the hub.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealStatusCode` = **Applied**  
  The seal is in place.
- `Consignment/TransportHandlingUnit/TransportEquipment/TransportEquipmentSeal/SealingPartyType` = **Shipper**  
  And put on by the shipper when it packed the container.
- `Consignment/OfficeOfEntryLocation/Name` = **Customs post at the rail border station, Bayvarran side**  
  Where the goods enter Bayvarra.
- `Consignment/OfficeOfExitLocation/Name` = **Customs post at the rail border station, Urvanian side**  
  Where the goods leave Urvania.
- `Consignment/OfficeOfDepartureLocation/Name` = **Customs office Ferrano Intermodal Hub**  
  Where the transit starts.
- `Consignment/OfficeOfDestinationLocation/Name` = **Customs office Marrowdale**  
  Where the transit ends and the goods are declared for import.
- `Consignment/OfficeOfImportLocation/Name` = **Customs office Marrowdale**  
  Where the import is declared.
- `Consignment/OfficeOfTransitLocation/Name` = **Customs post at the rail border station, Bayvarran side**  
  Where the transit is checked on entering Bayvarra.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **9580800** (currencyID `XUF`)  
  The value of the goods, in ferra, for the transit guarantee.
- `GoodsItem/GrossWeightMeasure` = **7968** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **192** (unitCode `H87`)  
  The quantity declared.
- `GoodsItem/Item/Description` = **Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.**  
  The seller's description; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.**  
  What comes with the item; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/Keyword` = **park bench**  
  A word buyers search the item by.
- `GoodsItem/Item/Keyword` = **street furniture**  
  A word buyers search the item by.
- `GoodsItem/Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/ModelName` = **Serra 180**  
  The model; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/WarrantyInformation` = **Five years on the frame against corrosion.**  
  The maker's warranty; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/SellersItemIdentification/ID` = **VI-B180**  
  The seller's own item number; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **Colour**  
  The attribute the variant differs in.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM**  
  The part of the item the attribute is on: the frame.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY**  
  The variant's code for it.
- `GoodsItem/Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `GoodsItem/Item/StandardItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label.
- `GoodsItem/Item/StandardItemIdentification/IssuerScopeID` = **771**  
  The range of item numbers the agency gives out in the maker's country.
- `GoodsItem/Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `GoodsItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/CommodityClassification/NatureCode` = **XX**  
  The section of the Harmonized System the goods fall in, the highest level of the World Customs Organization's classification.
- `GoodsItem/Item/CommodityClassification/CargoTypeCode` = **GEN**  
  The kind of cargo as the parties code it: bulk, or general cargo in packages.
- `GoodsItem/Item/CommodityClassification/CommodityCode` = **9401.79.10**  
  The national tariff code below the HS subheading, as the customs of the maker's country uses it.
- `GoodsItem/Item/CommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Frame material**  
  A property buyers ask about.
- `GoodsItem/Item/AdditionalItemProperty/Value` = **Cast steel, hot-dip galvanised**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Slat wood**  
  A property buyers ask about.
- `GoodsItem/Item/AdditionalItemProperty/Value` = **Kiln-dried hardwood**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Seats**  
  A property buyers ask about.
- `GoodsItem/Item/AdditionalItemProperty/Value` = **3**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/ID` = **COL**  
  The maker's identifier for the property.
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Frame colour**  
  The colours the frame is offered in.
- `GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **Optional**  
  How much the property matters in describing the item.
- `GoodsItem/Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  One of the values the property can take.
- `GoodsItem/Item/AdditionalItemProperty/ListValue` = **Moss green**  
  One of the values the property can take.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **APP**  
  The group of properties this one belongs to.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Appearance**  
  The group's name.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **Optional**  
  How much the group matters.
- `GoodsItem/Item/AdditionalItemProperty/ID` = **LOAD**  
  The maker's identifier for the property.
- `GoodsItem/Item/AdditionalItemProperty/Name` = **Load capacity**  
  A property buyers ask about.
- `GoodsItem/Item/AdditionalItemProperty/NameCode` = **LOAD**  
  The property's name as a code, as the property standard lists it.
- `GoodsItem/Item/AdditionalItemProperty/TestMethod` = **Static load on the seat for one hour, three seats loaded evenly, no lasting deformation**  
  How the value is tested.
- `GoodsItem/Item/AdditionalItemProperty/ValueQuantity` = **450** (unitCode `KGM`)  
  Its measured value; item bench-serra of Valdara Industries (world/items.json).
- `GoodsItem/Item/AdditionalItemProperty/ValueQualifier` = **Distributed over the seat**  
  What the value stands for.
- `GoodsItem/Item/AdditionalItemProperty/ImportanceCode` = **Mandatory**  
  How much the property matters in describing the item.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **SAF**  
  The group of properties this one belongs to.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Safety**  
  The group's name.
- `GoodsItem/Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **Mandatory**  
  How much the group matters.
- `GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-SF-0450**  
  The property's number in the property standard of the identification agency.
- `GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **Codana street furniture properties**  
  The part of the agency's standards it is taken from.
- `GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `GoodsItem/Item/Dimension/AttributeID` = **Length**  
  Which dimension.
- `GoodsItem/Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `GoodsItem/Item/Dimension/Description` = **Over the armrests**  
  Where it is measured.
- `GoodsItem/Item/Dimension/AttributeID` = **Depth**  
  Which dimension.
- `GoodsItem/Item/Dimension/Measure` = **620** (unitCode `MMT`)  
  Its size.
- `GoodsItem/Item/Dimension/AttributeID` = **Height**  
  Which dimension.
- `GoodsItem/Item/Dimension/Measure` = **780** (unitCode `MMT`)  
  Its size.
- `GoodsItem/Item/Dimension/Description` = **Seat back at its highest point**  
  Where it is measured.
- `GoodsItem/Item/Dimension/AttributeID` = **Seat height**  
  Which dimension.
- `GoodsItem/Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `GoodsItem/Item/Dimension/Description` = **Above the ground when anchored**  
  Where it is measured.
- `GoodsItem/Item/Dimension/MinimumMeasure` = **440** (unitCode `MMT`)  
  The lowest it can be set to.
- `GoodsItem/Item/Dimension/MaximumMeasure` = **460** (unitCode `MMT`)  
  The highest it can be set to.
- `GoodsItem/Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2e**  
  The emission reported: greenhouse gases as CO2 equivalent.
- `GoodsItem/Item/EnvironmentalEmission/ValueMeasure` = **96** (unitCode `KGM`)  
  The emission of one item.
- `GoodsItem/Item/EnvironmentalEmission/ValueFactorNumeric` = **0.82**  
  The share of the footprint the steel frame accounts for.
- `GoodsItem/Item/EnvironmentalEmission/ValueBaseMeasure` = **1** (unitCode `H87`)  
  The emission is per one bench.
- `GoodsItem/Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `GoodsItem/Item/EnvironmentalEmission/LifecycleStageCode` = **Manufacturing**  
  The part of the bench's life the figure covers.
- `GoodsItem/Item/EnvironmentalEmission/LifecycleStageDescription` = **From the ore at the mine to the bench leaving the factory gate.**  
  That part in words.
- `GoodsItem/Item/EnvironmentalEmission/Description` = **Mining, steel making, casting, galvanising, sawing and the transport between them.**  
  What the figure includes.
- `GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **Calculated**  
  Calculated, not measured.
- `GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **Cradle to gate**  
  How much of the chain is included.
- `GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **The steelworks' and sawmill's measured energy use of 2025**  
  Where the factors come from.
- `GoodsItem/Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `GoodsItem/Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `GoodsItem/Item/CircularityProfile/MaintenanceFrequencyCode` = **Yearly**  
  How often the item needs maintenance.
- `GoodsItem/Item/CircularityProfile/MaintenanceFrequencyDescription` = **Tighten the slat bolts and touch up the coating once a year.**  
  What the maintenance is.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **Steel**  
  A material the item is made of.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **34** (unitCode `KGM`)  
  How much of it one item uses.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Steel made from Serravona ore in Urvania**  
  Where the material comes from.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **Hardwood**  
  A material the item is made of.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **22.5** (unitCode `KGM`)  
  How much of it one item uses.
- `GoodsItem/Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Slats from Upland State, Bayvarra**  
  Where the material comes from.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeCode` = **Packaging**  
  The kind of waste the item leaves.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/WasteTypeDescription` = **Stretch film and pallet straps, per bench**  
  The waste in words.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/WasteMeasure` = **0.4** (unitCode `KGM`)  
  How much of it per item.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the deliveries of 2025.
- `GoodsItem/Item/CircularityProfile/WasteGenerated/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoreNumeric` = **8**  
  Side frames and slats can be replaced one by one, which is why the spare side frame exists.
- `GoodsItem/Item/CircularityProfile/RepairabilityScore/ScoringSystemCode` = **Repairability index, 0–10**  
  The scale of the score.
- `GoodsItem/Item/CircularityProfile/ProductDocumentationDocumentReference/ID` = **VI-RM-B180**  
  The repair and maintenance manual.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransitCustomsDeclaration xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransitCustomsDeclaration-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:rail</cbc:ProfileID>
  <cbc:ProfileExecutionID>RAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VI-TD-26-0331</cbc:ID>
  <cbc:UUID>39a0d3b7-c2fe-5e50-8ee2-54287be65033</cbc:UUID>
  <cbc:IssueDate>2026-04-14</cbc:IssueDate>
  <cbc:IssueTime>17:29:00</cbc:IssueTime>
  <cac:TransitExporterParty>
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
  </cac:TransitExporterParty>
  <cac:ConsignorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
  </cac:ConsignorParty>
  <cac:ConsigneeParty>
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
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
      <cbc:Postbox>PB 18</cbc:Postbox>
      <cbc:StreetName>Valico di Confine</cbc:StreetName>
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
  <cac:Shipment>
    <cbc:ID>VI-SH-26-0332</cbc:ID>
    <cbc:GrossWeightMeasure unitCode="KGM">7968</cbc:GrossWeightMeasure>
    <cac:Consignment>
      <cbc:ID>VI-CS-26-0327</cbc:ID>
      <cac:CarrierParty>
        <cbc:WebsiteURI>https://www.ferranorail.example</cbc:WebsiteURI>
        <cbc:IndustryClassificationCode listID="ISIC Rev.4">4912</cbc:IndustryClassificationCode>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Ferrano Rail Cargo</cbc:Name>
        </cac:PartyName>
        <cac:Language>
          <cbc:ID>en</cbc:ID>
          <cbc:Name>English</cbc:Name>
          <cbc:LocaleCode>EN</cbc:LocaleCode>
        </cac:Language>
        <cac:PostalAddress>
          <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
          <cbc:StreetName>Viale della Stazione</cbc:StreetName>
          <cbc:BuildingNumber>38</cbc:BuildingNumber>
          <cbc:CityName>Serravona</cbc:CityName>
          <cbc:PostalZone>4150</cbc:PostalZone>
          <cbc:Region>Province of Ferrano</cbc:Region>
          <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
          <cac:Country>
            <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            <cbc:Name>Urvania</cbc:Name>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:RegistrationName>Ferrano Rail Cargo SRU</cbc:RegistrationName>
          <cbc:CompanyID>XU007328060</cbc:CompanyID>
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
          <cbc:RegistrationName>Ferrano Rail Cargo SRU</cbc:RegistrationName>
          <cbc:CompanyID>XU-R-104685</cbc:CompanyID>
          <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
          <cbc:CompanyLegalFormCode>SRU</cbc:CompanyLegalFormCode>
          <cbc:CompanyLegalForm>Società a responsabilità urvaniana (private limited company)</cbc:CompanyLegalForm>
          <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
          <cac:RegistrationAddress>
            <cbc:CityName>Serravona</cbc:CityName>
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
          <cbc:Name>Freight desk</cbc:Name>
          <cbc:JobTitle>Operations planner</cbc:JobTitle>
          <cbc:Department>Operations</cbc:Department>
          <cbc:Telephone>+999 1 4150 4685</cbc:Telephone>
          <cbc:ElectronicMail>freight@ferranorail.example</cbc:ElectronicMail>
          <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104685</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:CarrierParty>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRCU1044171</cbc:ID>
          <cbc:ReferencedConsignmentID>VI-CS-26-0327</cbc:ReferencedConsignmentID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:SizeTypeCode>45G1</cbc:SizeTypeCode>
          <cbc:FullnessIndicationCode>FCL</cbc:FullnessIndicationCode>
          <cbc:GrossWeightMeasure unitCode="KGM">7884</cbc:GrossWeightMeasure>
          <cac:TransportEquipmentSeal>
            <cbc:ID>XU-VI-30411</cbc:ID>
            <cbc:SealIssuerTypeCode>Shipper</cbc:SealIssuerTypeCode>
            <cbc:Condition>Intact</cbc:Condition>
            <cbc:SealStatusCode>Applied</cbc:SealStatusCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
        </cac:TransportEquipment>
      </cac:TransportHandlingUnit>
      <cac:TransportHandlingUnit>
        <cac:TransportEquipment>
          <cbc:ID schemeID="ISO6346">FRCU1044187</cbc:ID>
          <cbc:ReferencedConsignmentID>VI-CS-26-0327</cbc:ReferencedConsignmentID>
          <cbc:TransportEquipmentTypeCode listID="UN/EDIFACT EDED 8053">CN</cbc:TransportEquipmentTypeCode>
          <cbc:SizeTypeCode>45G1</cbc:SizeTypeCode>
          <cbc:FullnessIndicationCode>FCL</cbc:FullnessIndicationCode>
          <cbc:GrossWeightMeasure unitCode="KGM">7884</cbc:GrossWeightMeasure>
          <cac:TransportEquipmentSeal>
            <cbc:ID>XU-VI-30412</cbc:ID>
            <cbc:SealIssuerTypeCode>Shipper</cbc:SealIssuerTypeCode>
            <cbc:Condition>Intact</cbc:Condition>
            <cbc:SealStatusCode>Applied</cbc:SealStatusCode>
            <cbc:SealingPartyType>Shipper</cbc:SealingPartyType>
          </cac:TransportEquipmentSeal>
        </cac:TransportEquipment>
      </cac:TransportHandlingUnit>
      <cac:OfficeOfEntryLocation>
        <cbc:Name>Customs post at the rail border station, Bayvarran side</cbc:Name>
      </cac:OfficeOfEntryLocation>
      <cac:OfficeOfExitLocation>
        <cbc:Name>Customs post at the rail border station, Urvanian side</cbc:Name>
      </cac:OfficeOfExitLocation>
      <cac:OfficeOfDepartureLocation>
        <cbc:Name>Customs office Ferrano Intermodal Hub</cbc:Name>
      </cac:OfficeOfDepartureLocation>
      <cac:OfficeOfDestinationLocation>
        <cbc:Name>Customs office Marrowdale</cbc:Name>
      </cac:OfficeOfDestinationLocation>
      <cac:OfficeOfImportLocation>
        <cbc:Name>Customs office Marrowdale</cbc:Name>
      </cac:OfficeOfImportLocation>
      <cac:OfficeOfTransitLocation>
        <cbc:Name>Customs post at the rail border station, Bayvarran side</cbc:Name>
      </cac:OfficeOfTransitLocation>
    </cac:Consignment>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XUF">9580800</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">7968</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="H87">192</cbc:Quantity>
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
          <cbc:NatureCode>XX</cbc:NatureCode>
          <cbc:CargoTypeCode>GEN</cbc:CargoTypeCode>
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
  </cac:Shipment>
</TransitCustomsDeclaration>
```
