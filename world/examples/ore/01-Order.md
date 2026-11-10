# Order: Valdara Industries to Serravona Mining

*Example 1 of the flow "Ore from the mine to the factory (domestic, Urvania)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

Monthly ore call-off. Delivery terms FCA mine: the buyer books the train, so the order names the rail carrier that will collect.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:ore**  
  The business process the document belongs to: the flow "Ore from the mine to the factory (domestic, Urvania)".
- `ProfileExecutionID` = **ORE-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VI-PO-26-0304**  
  The buyer's order number.
- `UUID` = **f7a41c69-f150-5204-9582-ff383282ea1c**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-03-02**  
  The first working day of the month: the monthly ore call-off.
- `IssueTime` = **11:10:00**  
  The time the sender's system issued the document, in the sender's local time.
- `OrderTypeCode` = **220**  
  UN/EDIFACT 1001 code 220: order.
- `Note` = **Monthly call-off, one train.**  
  Says in words what the order is for.
- `DocumentCurrencyCode` = **XUF**  
  The ferra, the seller's currency, in which the seller's prices are; it has no minor unit.
- `AccountingCostCode` = **3100**  
  The buyer's cost centre, to be quoted on the invoice.
- `AccountingCost` = **Raw materials and parts**  
  The cost centre in words.
- `LineCountNumeric` = **1**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/WebsiteURI` = **https://www.valdara.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Valdara Industries (world/parties.json).
- `Party/IndustryClassificationCode` = **3100** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Valdara Industries (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XU-TR-104274** (schemeID `urn:ubl-examples:world:XU:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XU-TR- and 6 digits); identity of Valdara Industries (world/parties.json).
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits). identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered for value added tax; identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries SUA**  
  The name under which the party is registered, with its legal form; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1962-04-12**  
  The day the company was entered in the register; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **250000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
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
- `Party/PartyLegalEntity/SecurityListing/ID` = **XU0001042505**  
  The identifier of the listed shares, in the form of an ISIN with the world's country code.
- `Party/PartyLegalEntity/SecurityListing/MarketName` = **Ferrano Stock Exchange**  
  The regulated market where the shares are listed.
- `Party/PartyLegalEntity/SecurityListing/MarketCode` = **FSE**  
  The market's code.
- `Party/Contact/Name` = **Order desk**  
  The desk that handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4120 4274**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Valdara Industries (world/parties.json).
- `Party/Contact/OtherCommunication/ChannelCode` = **AL**  
  UN/EDIFACT 3155 code AL: cellular phone.
- `Party/Contact/OtherCommunication/Value` = **+999 1 7000 4274**  
  The sales desk's mobile number, also under the reserved +999.
- `Party/ServiceProviderParty/ID` = **5-xu-SP-8-xu**  
  The service contract between the two.
- `Party/ServiceProviderParty/ServiceTypeCode` = **Logistics**  
  The kind of service, as a code.
- `Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/SellerContact/Name` = **Key account desk**  
  The provider's contact for this customer.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/WebsiteURI` = **https://www.serravona.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Serravona Mining (world/parties.json).
- `Party/IndustryClassificationCode` = **0710** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Serravona Mining (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-104137** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Serravona Mining (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Serravona Mining**  
  The trading name; identity of Serravona Mining (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Strada della Miniera**  
  Street of the postal address. identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **10**  
  Building number of the postal address. identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/CityName` = **Serravona**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4110**  
  Postal code in Urvania's format (4 digits). identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Serravona Mining (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PhysicalLocation/ID` = **XUSRV** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `Party/PhysicalLocation/Description` = **The mine and its rail siding**  
  Where the party actually operates, apart from its postal address.
- `Party/PhysicalLocation/Conditions` = **Unpaved access road; heavy vehicles only.**  
  What a visitor must know about getting there.
- `Party/PhysicalLocation/InformationURI` = **https://www.serravona.example**  
  Where to find more about the place.
- `Party/PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **WGS84**  
  The World Geodetic System 1984, as used by satellite navigation.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **39** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **54.00** (unitCode `D61`)  
  The minutes of the latitude.
- `Party/PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South**  
  South of the equator.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **15** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map (world/countries.json).
- `Party/PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **30.60** (unitCode `D61`)  
  The minutes of the longitude.
- `Party/PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West**  
  West of the Greenwich meridian.
- `Party/PartyTaxScheme/RegistrationName` = **Serravona Mining SUA**  
  The name under which the party is registered for value added tax; identity of Serravona Mining (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007289704**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Serravona Mining (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Serravona Mining SUA**  
  The name under which the party is registered, with its legal form; identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104137**  
  Number in the Commercial register of Urvania; identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1958-06-30**  
  The day the company was entered in the register; identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **120000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Serravona Mining (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
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
- `Party/Contact/Name` = **Sales office**  
  The desk that handles this document; identity of Serravona Mining (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Serravona Mining (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Serravona Mining (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4110 4137**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Serravona Mining (world/parties.json).
- `Party/Contact/ElectronicMail` = **sales@serravona.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Serravona Mining (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Serravona Mining (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104137** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Serravona Mining (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `RequestedDeliveryPeriod/StartDate` = **2026-03-09**  
  The week in which the factory wants the ore.
- `RequestedDeliveryPeriod/EndDate` = **2026-03-13**  
  The end of that week.
- `DeliveryParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `DeliveryParty/PartyName/Name` = **Valdara Industries**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Despatch/DespatchParty/PartyIdentification/ID` = **XU-R-104137** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at SellerSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Despatch/DespatchParty/PartyName/Name` = **Serravona Mining**  
  The same party as at SellerSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Despatch/CarrierParty/WebsiteURI` = **https://www.ferranorail.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/IndustryClassificationCode` = **4912** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Despatch/CarrierParty/PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/Language/ID` = **en**  
  English, the language the party does business in.
- `Despatch/CarrierParty/Language/Name` = **English**  
  The language's name.
- `Despatch/CarrierParty/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Despatch/CarrierParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Despatch/CarrierParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Despatch/CarrierParty/PostalAddress/StreetName` = **Viale della Stazione**  
  Street of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address. identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/CityName` = **Serravona**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Despatch/CarrierParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Despatch/CarrierParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Despatch/CarrierParty/PartyTaxScheme/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered for value added tax; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PartyTaxScheme/CompanyID` = **XU007328060**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Despatch/CarrierParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Despatch/CarrierParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Despatch/CarrierParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Despatch/CarrierParty/PartyLegalEntity/RegistrationName` = **Ferrano Rail Cargo SRU**  
  The name under which the party is registered, with its legal form; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PartyLegalEntity/CompanyID` = **XU-R-104685**  
  Number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Despatch/CarrierParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `Despatch/CarrierParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Despatch/CarrierParty/PartyLegalEntity/RegistrationAddress/CityName` = **Serravona**  
  The registered office, as entered in the register.
- `Despatch/CarrierParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Despatch/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Despatch/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Despatch/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Despatch/CarrierParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Despatch/CarrierParty/Contact/Name` = **Freight desk**  
  The desk that handles this document; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/Contact/JobTitle` = **Operations planner**  
  The job of the person who answers at the desk; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/Contact/Department` = **Operations**  
  The department the desk belongs to; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/Contact/Telephone` = **+999 1 4150 4685**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/Contact/ElectronicMail` = **freight@ferranorail.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Rail Cargo (world/parties.json).
- `Despatch/CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Despatch/CarrierParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Rail Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **FCA** (schemeID `INCOTERMS`)  
  Free carrier at the mine: the buyer arranges and pays the main transport, so the order names the carrier the buyer has booked. Stated, because leaving it out would carry no meaning (UBL rule IND6).
- `DeliveryLocation/Description` = **Mine siding, Serravona**  
  Where the delivery terms place the handover of the goods.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **2901600** (currencyID `XUF`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **14508000** (currencyID `XUF`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **2901600** (currencyID `XUF`)  
  20 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S).
- `TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **14508000** (currencyID `XUF`)  
  The sum of the line amounts.
- `PayableAmount` = **17409600** (currencyID `XUF`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **1800** (unitCode `TNE`)  
  One train: 30 wagons of about 60 tonnes.
- `LineItem/LineExtensionAmount` = **14508000** (currencyID `XUF`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **8060** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `TNE`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.**  
  The seller's description; item ore-lump of Serravona Mining (world/items.json).
- `LineItem/Item/Name` = **Iron ore, lump**  
  The item's short name; item ore-lump of Serravona Mining (world/items.json).
- `LineItem/Item/SellersItemIdentification/ID` = **SM-ORE-L**  
  The seller's own item number; item ore-lump of Serravona Mining (world/items.json).
- `LineItem/Item/StandardItemIdentification/ID` = **771010000013** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item ore-lump of Serravona Mining (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item ore-lump of Serravona Mining (world/items.json).
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **2601.11** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item ore-lump of Serravona Mining (world/items.json).
- `LineItem/Item/AdditionalItemProperty/Name` = **Iron content**  
  A measured property of the item.
- `LineItem/Item/AdditionalItemProperty/ValueQuantity` = **62** (unitCode `P1`)  
  Its measured value; item ore-lump of Serravona Mining (world/items.json).

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:ore</cbc:ProfileID>
  <cbc:ProfileExecutionID>ORE-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VI-PO-26-0304</cbc:ID>
  <cbc:UUID>f7a41c69-f150-5204-9582-ff383282ea1c</cbc:UUID>
  <cbc:IssueDate>2026-03-02</cbc:IssueDate>
  <cbc:IssueTime>11:10:00</cbc:IssueTime>
  <cbc:OrderTypeCode>220</cbc:OrderTypeCode>
  <cbc:Note>Monthly call-off, one train.</cbc:Note>
  <cbc:DocumentCurrencyCode>XUF</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>3100</cbc:AccountingCostCode>
  <cbc:AccountingCost>Raw materials and parts</cbc:AccountingCost>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
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
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
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
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
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
        <cac:SecurityListing>
          <cbc:ID>XU0001042505</cbc:ID>
          <cbc:MarketName>Ferrano Stock Exchange</cbc:MarketName>
          <cbc:MarketCode>FSE</cbc:MarketCode>
        </cac:SecurityListing>
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
        <cbc:ID>5-xu-SP-8-xu</cbc:ID>
        <cbc:ServiceTypeCode>Logistics</cbc:ServiceTypeCode>
        <cbc:ServiceType>Warehousing and despatch</cbc:ServiceType>
        <cac:Party>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Castrano Logistics</cbc:Name>
          </cac:PartyName>
        </cac:Party>
        <cac:SellerContact>
          <cbc:Name>Key account desk</cbc:Name>
        </cac:SellerContact>
      </cac:ServiceProviderParty>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104274</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.serravona.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">0710</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104137</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Serravona Mining</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Strada della Miniera</cbc:StreetName>
        <cbc:BuildingNumber>10</cbc:BuildingNumber>
        <cbc:CityName>Serravona</cbc:CityName>
        <cbc:PostalZone>4110</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PhysicalLocation>
        <cbc:ID schemeID="UN/LOCODE">XUSRV</cbc:ID>
        <cbc:Description>The mine and its rail siding</cbc:Description>
        <cbc:Conditions>Unpaved access road; heavy vehicles only.</cbc:Conditions>
        <cbc:InformationURI>https://www.serravona.example</cbc:InformationURI>
        <cac:LocationCoordinate>
          <cbc:CoordinateSystemCode>WGS84</cbc:CoordinateSystemCode>
          <cbc:LatitudeDegreesMeasure unitCode="DD">39</cbc:LatitudeDegreesMeasure>
          <cbc:LatitudeMinutesMeasure unitCode="D61">54.00</cbc:LatitudeMinutesMeasure>
          <cbc:LatitudeDirectionCode>South</cbc:LatitudeDirectionCode>
          <cbc:LongitudeDegreesMeasure unitCode="DD">15</cbc:LongitudeDegreesMeasure>
          <cbc:LongitudeMinutesMeasure unitCode="D61">30.60</cbc:LongitudeMinutesMeasure>
          <cbc:LongitudeDirectionCode>West</cbc:LongitudeDirectionCode>
        </cac:LocationCoordinate>
      </cac:PhysicalLocation>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Serravona Mining SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007289704</cbc:CompanyID>
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
        <cbc:RegistrationName>Serravona Mining SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104137</cbc:CompanyID>
        <cbc:RegistrationDate>1958-06-30</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
        <cbc:CorporateStockAmount currencyID="XUF">120000000</cbc:CorporateStockAmount>
        <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 4110 4137</cbc:Telephone>
        <cbc:ElectronicMail>sales@serravona.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104137</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-03-09</cbc:StartDate>
      <cbc:EndDate>2026-03-13</cbc:EndDate>
    </cac:RequestedDeliveryPeriod>
    <cac:DeliveryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
    <cac:Despatch>
      <cac:DespatchParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104137</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Serravona Mining</cbc:Name>
        </cac:PartyName>
      </cac:DespatchParty>
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
          <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
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
          <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
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
    </cac:Despatch>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">FCA</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Description>Mine siding, Serravona</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">2901600</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">14508000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">2901600</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XUF">14508000</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XUF">17409600</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="TNE">1800</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XUF">14508000</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XUF">8060</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="TNE">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.</cbc:Description>
        <cbc:Name>Iron ore, lump</cbc:Name>
        <cac:SellersItemIdentification>
          <cbc:ID>SM-ORE-L</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">771010000013</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">2601.11</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:AdditionalItemProperty>
          <cbc:Name>Iron content</cbc:Name>
          <cbc:ValueQuantity unitCode="P1">62</cbc:ValueQuantity>
        </cac:AdditionalItemProperty>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
