# Goods Item Passport: Ferrano Chamber of Commerce to Valdara Industries

*Example 1 of the flow "Samples to a trade fair on the island (temporary export)" · [Goods Item Passport in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-GOODS-ITEM-PASSPORT-SCHEMA)*

The chamber issues the carnet to the manufacturer, who holds it while the samples travel.

[The XML file](01-GoodsItemPassport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:carnet**  
  The business process the document belongs to: the flow "Samples to a trade fair on the island (temporary export)".
- `ProfileExecutionID` = **CARNET-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **FCC-DOC-26-0724**  
  The carnet number, given by the chamber.
- `UUID` = **eba67af9-0d62-5339-b7c5-75faae5007fc**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-25**  
  Issued before the samples leave for the fair.
- `IssueTime` = **15:04:00**  
  The time the sender's system issued the document, in the sender's local time.
- `StatusCode` = **Valid**  
  The carnet is valid.
- `Status` = **Issued**  
  In words.
- `Note` = **Samples for the Selanu trade fair; to come back within six months.**  
  What it is for.
- `VersionID` = **1**  
  The first version.
- `ExportReasonCode` = **Exhibition**  
  Temporary export for a fair.
- `ExportReason` = **Exhibition at the Selanu trade fair**  
  In words.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-05-25**  
  Valid from issue.
- `EndDate` = **2027-05-25**  
  A carnet is valid for one year.

### Issuer Party

Inside `IssuerParty`:

- `IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Chamber of Commerce (world/parties.json).
- `PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Ferrano Chamber of Commerce**  
  The trading name; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `PostalAddress/StreetName` = **Piazza del Mercato**  
  Street of the postal address. identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/BuildingNumber` = **15**  
  Building number of the postal address. identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Chamber of Commerce (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered for value added tax; identity of Ferrano Chamber of Commerce (world/parties.json).
- `PartyTaxScheme/CompanyID` = **XU007376017**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Chamber of Commerce (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Ferrano Chamber of Commerce**  
  The name under which the party is registered, with its legal form; identity of Ferrano Chamber of Commerce (world/parties.json).
- `PartyLegalEntity/CompanyID` = **XU-R-105370**  
  Number in the Commercial register of Urvania; identity of Ferrano Chamber of Commerce (world/parties.json).
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
- `Contact/Name` = **Certificates office**  
  The desk that handles this document; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/Telephone` = **+999 1 4110 5370**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/ElectronicMail` = **certificates@camera-ferrano.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Chamber of Commerce (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Chamber of Commerce (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105370** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Holder Party

Inside `HolderParty`:

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

### Representative Party

Inside `RepresentativeParty`:

- `PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at HolderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Valdara Industries**  
  The same party as at HolderParty, where its full details are given; only its identifier and name are repeated.
- `Person/ID` = **VI-E-0412**  
  The employee's staff number; identity of Valdara Industries (world/parties.json).
- `Person/FirstName` = **Davide**  
  The first name of the employee who travels with the samples; identity of Valdara Industries (world/parties.json).
- `Person/FamilyName` = **Orsenna**  
  Their family name; identity of Valdara Industries (world/parties.json).
- `Person/JobTitle` = **Sales engineer**  
  Their job; identity of Valdara Industries (world/parties.json).
- `Person/NationalID` = **XU-NID-55102311**  
  The national identity number, which customs may ask for at the border.
- `Person/BirthDate` = **1984-05-17**  
  The birth date, as in the passport.
- `Person/BirthplaceName` = **Ferrano**  
  The place of birth, as in the passport.
- `Person/OrganizationDepartment` = **Export sales**  
  The department the employee works in; identity of Valdara Industries (world/parties.json).
- `Person/CitizenshipCountry/IdentificationCode` = **XU**  
  The employee is a citizen of Urvania.
- `Person/IdentityDocumentReference/ID` = **XU-P-2210931**  
  The passport the employee travels on.
- `Person/IdentityDocumentReference/DocumentType` = **Passport**  
  The kind of identity document.

### Exporting Guarantor Party

Inside `ExportingGuarantorParty`:

- `PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at IssuerParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Ferrano Chamber of Commerce**  
  The same party as at IssuerParty, where its full details are given; only its identifier and name are repeated.

### Importing Guarantor Party

Inside `ImportingGuarantorParty`:

- `IndustryClassificationCode` = **9411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Chamber of Commerce (world/parties.json).
- `PartyIdentification/ID` = **IC42133** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Chamber of Commerce (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Chamber of Commerce**  
  The trading name; identity of Selanu Chamber of Commerce (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `PostalAddress/StreetName` = **Reef Street**  
  Street of the postal address. identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/BuildingNumber` = **30**  
  Building number of the postal address. identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Chamber of Commerce (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Selanu Chamber of Commerce**  
  The name under which the party is registered, with its legal form; identity of Selanu Chamber of Commerce (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC42133**  
  Number in the Island companies register; identity of Selanu Chamber of Commerce (world/parties.json).
- `PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Contact/Name` = **Carnet office**  
  The desk that handles this document; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Telephone` = **+999 3 3000 2133**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/ElectronicMail` = **carnet@chamber-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Chamber of Commerce (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Chamber of Commerce (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42133** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Chamber of Commerce (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Exporting Customs Party

Inside `ExportingCustomsParty`:

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

### Importing Customs Party

Inside `ImportingCustomsParty`:

- `IndustryClassificationCode` = **8411** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Island Customs Service (world/parties.json).
- `PartyIdentification/ID` = **IC41448** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Island Customs Service (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Island Customs Service**  
  The trading name; identity of Island Customs Service (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `PostalAddress/StreetName` = **Wharf Road**  
  Street of the postal address. identity of Island Customs Service (world/parties.json).
- `PostalAddress/BuildingNumber` = **53**  
  Building number of the postal address. identity of Island Customs Service (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Island Customs Service (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Island Customs Service**  
  The name under which the party is registered, with its legal form; identity of Island Customs Service (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC41448**  
  Number in the Island companies register; identity of Island Customs Service (world/parties.json).
- `PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Contact/Name` = **Import office**  
  The desk that handles this document; identity of Island Customs Service (world/parties.json).
- `Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Island Customs Service (world/parties.json).
- `Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Island Customs Service (world/parties.json).
- `Contact/Telephone` = **+999 3 3000 1448**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Island Customs Service (world/parties.json).
- `Contact/ElectronicMail` = **import@customs-xl.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Island Customs Service (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Island Customs Service (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41448** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Island Customs Service (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipment

Inside `Shipment`:

- `ID` = **VI-SH-26-0725**  
  The samples travelling under the carnet.
- `GoodsItem/ID` = **1**  
  The goods item number.
- `GoodsItem/Description` = **Park bench Serra 180**  
  What the goods are, in words.
- `GoodsItem/DeclaredCustomsValueAmount` = **99800** (currencyID `XUF`)  
  The value of the samples, for the guarantee.
- `GoodsItem/GrossWeightMeasure` = **83** (unitCode `KGM`)  
  The gross weight of the goods of this item.
- `GoodsItem/Quantity` = **2** (unitCode `H87`)  
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

### Goods Item Passport Counterfoil

Inside `GoodsItemPassportCounterfoil`:

- `ID` = **EXP-1**  
  The exportation counterfoil, stamped by Urvania's customs when the samples leave.
- `GoodsItemPassportID` = **FCC-DOC-26-0724**  
  The carnet.
- `FinalReexportationDate` = **2026-11-21**  
  The samples must be back by then.
- `Note` = **Stamped by customs.**  
  How it is used.
- `CustomsOfficeLocation/Name` = **Customs post at the land border, Urvanian side**  
  The customs office that stamps it.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `H87`)  
  Two.
- `ExportationDocumentReference/ID` = **EXP-1-STAMP**  
  The export stamp.
- `VoucherDocumentReference/ID` = **V-EXP-1**  
  The voucher that customs keeps.
- `ID` = **IMP-1**  
  The importation counterfoil, stamped by Lisavu's customs when they arrive.
- `GoodsItemPassportID` = **FCC-DOC-26-0724**  
  The carnet.
- `Note` = **Stamped by customs.**  
  How it is used.
- `CustomsOfficeLocation/Name` = **Customs office, Selanu airport**  
  The customs office that stamps it.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `H87`)  
  Two.
- `ImportationDocumentReference/ID` = **IMP-1-STAMP**  
  The import stamp on the island.
- `VoucherDocumentReference/ID` = **V-IMP-1**  
  The voucher that customs keeps.
- `ID` = **REEXP-1**  
  The re-exportation counterfoil, to be stamped when they leave the island.
- `GoodsItemPassportID` = **FCC-DOC-26-0724**  
  The carnet.
- `Note` = **Stamped by customs.**  
  How it is used.
- `CustomsOfficeLocation/Name` = **Customs office, Selanu airport**  
  The customs office that stamps it.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `H87`)  
  Two.
- `ReexportationDocumentReference/ID` = **REEXP-1-STAMP**  
  The re-export stamp.
- `VoucherDocumentReference/ID` = **V-REEXP-1**  
  The voucher that customs keeps.
- `ID` = **REIMP-1**  
  The re-importation counterfoil, stamped when they come home.
- `GoodsItemPassportID` = **FCC-DOC-26-0724**  
  The carnet.
- `Note` = **Stamped by customs.**  
  How it is used.
- `CustomsOfficeLocation/Name` = **Customs post at the land border, Urvanian side**  
  The customs office that stamps it.
- `GoodsItem/ID` = **1**  
  The two sample benches.
- `GoodsItem/Quantity` = **2** (unitCode `H87`)  
  Two.
- `ReimportationDocumentReference/ID` = **REIMP-1-STAMP**  
  The re-import stamp.
- `VoucherDocumentReference/ID` = **V-REIMP-1**  
  The voucher that customs keeps.

### Issuer Endorsement

Inside `IssuerEndorsement`:

- `DocumentID` = **FCC-DOC-26-0724**  
  The carnet.
- `ApprovalStatus` = **Issued**  
  The chamber issued it.
- `EndorserParty/RoleCode` = **Issuer**  
  The issuing chamber.
- `EndorserParty/SequenceNumeric` = **1**  
  The first endorsement.
- `EndorserParty/Party/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/Party/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.
- `EndorserParty/SignatoryContact/Name` = **Carnet desk**  
  The chamber's desk.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **SCC-FAIR-26-INV**  
  The fair's invitation to exhibit.

### Document Distribution

Inside `DocumentDistribution`:

- `ID` = **1**  
  The holder's carnet.
- `DistributionTypeCode` = **Paper**  
  On paper.
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

### Signature

Inside `Signature`:

- `ID` = **FCC-SIG-26-ATA**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **XU-R-105370** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Ferrano Chamber of Commerce**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<GoodsItemPassport xmlns="urn:oasis:names:specification:ubl:schema:xsd:GoodsItemPassport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:carnet</cbc:ProfileID>
  <cbc:ProfileExecutionID>CARNET-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FCC-DOC-26-0724</cbc:ID>
  <cbc:UUID>eba67af9-0d62-5339-b7c5-75faae5007fc</cbc:UUID>
  <cbc:IssueDate>2026-05-25</cbc:IssueDate>
  <cbc:IssueTime>15:04:00</cbc:IssueTime>
  <cbc:StatusCode>Valid</cbc:StatusCode>
  <cbc:Status>Issued</cbc:Status>
  <cbc:Note>Samples for the Selanu trade fair; to come back within six months.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cbc:ExportReasonCode>Exhibition</cbc:ExportReasonCode>
  <cbc:ExportReason>Exhibition at the Selanu trade fair</cbc:ExportReason>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-05-25</cbc:StartDate>
    <cbc:EndDate>2027-05-25</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:IssuerParty>
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
  </cac:IssuerParty>
  <cac:HolderParty>
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
  </cac:HolderParty>
  <cac:RepresentativeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Valdara Industries</cbc:Name>
    </cac:PartyName>
    <cac:Person>
      <cbc:ID>VI-E-0412</cbc:ID>
      <cbc:FirstName>Davide</cbc:FirstName>
      <cbc:FamilyName>Orsenna</cbc:FamilyName>
      <cbc:JobTitle>Sales engineer</cbc:JobTitle>
      <cbc:NationalID>XU-NID-55102311</cbc:NationalID>
      <cbc:BirthDate>1984-05-17</cbc:BirthDate>
      <cbc:BirthplaceName>Ferrano</cbc:BirthplaceName>
      <cbc:OrganizationDepartment>Export sales</cbc:OrganizationDepartment>
      <cac:CitizenshipCountry>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:CitizenshipCountry>
      <cac:IdentityDocumentReference>
        <cbc:ID>XU-P-2210931</cbc:ID>
        <cbc:DocumentType>Passport</cbc:DocumentType>
      </cac:IdentityDocumentReference>
    </cac:Person>
  </cac:RepresentativeParty>
  <cac:ExportingGuarantorParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
    </cac:PartyName>
  </cac:ExportingGuarantorParty>
  <cac:ImportingGuarantorParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">9411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42133</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Chamber of Commerce</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
      <cbc:StreetName>Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>30</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Selanu Chamber of Commerce</cbc:RegistrationName>
      <cbc:CompanyID>IC42133</cbc:CompanyID>
      <cac:RegistrationAddress>
        <cbc:CityName>Selanu</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XL:ICR</cbc:ID>
        <cbc:Name>Island companies register</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Carnet office</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 3 3000 2133</cbc:Telephone>
      <cbc:ElectronicMail>carnet@chamber-selanu.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42133</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImportingGuarantorParty>
  <cac:ExportingCustomsParty>
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
  </cac:ExportingCustomsParty>
  <cac:ImportingCustomsParty>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">8411</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41448</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Island Customs Service</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
      <cbc:StreetName>Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>53</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Island Customs Service</cbc:RegistrationName>
      <cbc:CompanyID>IC41448</cbc:CompanyID>
      <cac:RegistrationAddress>
        <cbc:CityName>Selanu</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:RegistrationAddress>
      <cac:CorporateRegistrationScheme>
        <cbc:ID>XL:ICR</cbc:ID>
        <cbc:Name>Island companies register</cbc:Name>
        <cbc:CorporateRegistrationTypeCode>Commercial</cbc:CorporateRegistrationTypeCode>
        <cac:JurisdictionRegionAddress>
          <cac:Country>
            <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:JurisdictionRegionAddress>
      </cac:CorporateRegistrationScheme>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Import office</cbc:Name>
      <cbc:JobTitle>Public service officer</cbc:JobTitle>
      <cbc:Department>Public services</cbc:Department>
      <cbc:Telephone>+999 3 3000 1448</cbc:Telephone>
      <cbc:ElectronicMail>import@customs-xl.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41448</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ImportingCustomsParty>
  <cac:Shipment>
    <cbc:ID>VI-SH-26-0725</cbc:ID>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Description>Park bench Serra 180</cbc:Description>
      <cbc:DeclaredCustomsValueAmount currencyID="XUF">99800</cbc:DeclaredCustomsValueAmount>
      <cbc:GrossWeightMeasure unitCode="KGM">83</cbc:GrossWeightMeasure>
      <cbc:Quantity unitCode="H87">2</cbc:Quantity>
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
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>EXP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC-DOC-26-0724</cbc:GoodsItemPassportID>
    <cbc:FinalReexportationDate>2026-11-21</cbc:FinalReexportationDate>
    <cbc:Note>Stamped by customs.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:Name>Customs post at the land border, Urvanian side</cbc:Name>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="H87">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:ExportationDocumentReference>
      <cbc:ID>EXP-1-STAMP</cbc:ID>
    </cac:ExportationDocumentReference>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-EXP-1</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>IMP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC-DOC-26-0724</cbc:GoodsItemPassportID>
    <cbc:Note>Stamped by customs.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:Name>Customs office, Selanu airport</cbc:Name>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="H87">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:ImportationDocumentReference>
      <cbc:ID>IMP-1-STAMP</cbc:ID>
    </cac:ImportationDocumentReference>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-IMP-1</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>REEXP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC-DOC-26-0724</cbc:GoodsItemPassportID>
    <cbc:Note>Stamped by customs.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:Name>Customs office, Selanu airport</cbc:Name>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="H87">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:ReexportationDocumentReference>
      <cbc:ID>REEXP-1-STAMP</cbc:ID>
    </cac:ReexportationDocumentReference>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-REEXP-1</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:GoodsItemPassportCounterfoil>
    <cbc:ID>REIMP-1</cbc:ID>
    <cbc:GoodsItemPassportID>FCC-DOC-26-0724</cbc:GoodsItemPassportID>
    <cbc:Note>Stamped by customs.</cbc:Note>
    <cac:CustomsOfficeLocation>
      <cbc:Name>Customs post at the land border, Urvanian side</cbc:Name>
    </cac:CustomsOfficeLocation>
    <cac:GoodsItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="H87">2</cbc:Quantity>
    </cac:GoodsItem>
    <cac:ReimportationDocumentReference>
      <cbc:ID>REIMP-1-STAMP</cbc:ID>
    </cac:ReimportationDocumentReference>
    <cac:VoucherDocumentReference>
      <cbc:ID>V-REIMP-1</cbc:ID>
    </cac:VoucherDocumentReference>
  </cac:GoodsItemPassportCounterfoil>
  <cac:IssuerEndorsement>
    <cbc:DocumentID>FCC-DOC-26-0724</cbc:DocumentID>
    <cbc:ApprovalStatus>Issued</cbc:ApprovalStatus>
    <cac:EndorserParty>
      <cbc:RoleCode>Issuer</cbc:RoleCode>
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
        <cbc:Name>Carnet desk</cbc:Name>
      </cac:SignatoryContact>
    </cac:EndorserParty>
  </cac:IssuerEndorsement>
  <cac:AdditionalDocumentReference>
    <cbc:ID>SCC-FAIR-26-INV</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:DocumentDistribution>
    <cbc:ID>1</cbc:ID>
    <cbc:DistributionTypeCode>Paper</cbc:DistributionTypeCode>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:DocumentDistribution>
  <cac:Signature>
    <cbc:ID>FCC-SIG-26-ATA</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105370</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Chamber of Commerce</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
</GoodsItemPassport>
```
