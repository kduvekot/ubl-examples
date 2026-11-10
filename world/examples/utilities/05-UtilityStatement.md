# Utility Statement: Coastal State Water Company to Brightmarket Stores

*Example 5 of the flow "Electricity, water and telecom (one utility in each country)" · [Utility Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-UTILITY-STATEMENT-SCHEMA)*

The shop's water consumption, read from its meter.

[The XML file](05-UtilityStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:utilities**  
  The business process the document belongs to: the flow "Electricity, water and telecom (one utility in each country)".
- `ProfileExecutionID` = **UTILITIES-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **CSWC-DOC-26-0318**  
  The utility's statement number.
- `UUID` = **7bdfb021-49a1-5341-b641-0343b4c0240e**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  Issued with the bill for March.
- `IssueTime` = **11:55:00**  
  The time the sender's system issued the document, in the sender's local time.
- `UtilityStatementTypeCode` = **Water**  
  The kind of utility the statement is about.
- `Note` = **This statement explains the consumption behind your bill.**  
  What the statement is.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the utility's currency; it has two decimals.
- `AccountingCostCode` = **6120**  
  The customer's cost centre, as on the bill.
- `AccountingCost` = **Garden department**  
  The cost centre in words.

### Parent Document Reference

Inside `ParentDocumentReference`:

- `ID` = **CSWC-INV-26-0317**  
  The invoice this statement supplements: a utility statement adds the consumption behind the bill.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **CSWC-TARIFF-2026**  
  The utility's tariff sheet for 2026.
- `DocumentTypeCode` = **Tariff**  
  What the document is.
- `DocumentDescription` = **Prices per unit and the terms of supply.**  
  What it holds.

### Sender Party

Inside `SenderParty`:

- `WebsiteURI` = **https://www.coastalwater.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Coastal State Water Company (world/parties.json).
- `IndustryClassificationCode` = **3600** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Coastal State Water Company (world/parties.json).
- `PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Coastal State Water Company**  
  The trading name; identity of Coastal State Water Company (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address. identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address. identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits). identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Coastal State Water Company (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered for state sales tax; identity of Coastal State Water Company (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1236576**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Coastal State Water Company (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered, with its legal form; identity of Coastal State Water Company (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20412192**  
  Number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Coastal State Water Company (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Coastal State Water Company (world/parties.json).
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
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
  The desk that handles this document; identity of Coastal State Water Company (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Coastal State Water Company (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Coastal State Water Company (world/parties.json).
- `Contact/Telephone` = **+999 2 3850 2192**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Coastal State Water Company (world/parties.json).
- `Contact/ElectronicMail` = **customer@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Coastal State Water Company (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Coastal State Water Company (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Coastal State Water Company (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.brightmarket.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Brightmarket Stores (world/parties.json).
- `LogoReferenceID` = **BM-LOGO-2024**  
  The reference of the logo the store prints on its documents; identity of Brightmarket Stores (world/parties.json).
- `IndustryClassificationCode` = **4719** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Brightmarket Stores (world/parties.json).
- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
- `Language/ID` = **en**  
  English, the language the party does business in.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PartyTaxScheme/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered for state sales tax; identity of Brightmarket Stores (world/parties.json).
- `PartyTaxScheme/CompanyID` = **CO-1231233**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brightmarket Stores (world/parties.json).
- `PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `PartyLegalEntity/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered, with its legal form; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20410411**  
  Number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1979-02-14**  
  The day the company was entered in the register; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Corp**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/CorporateStockAmount` = **12000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Brightmarket Stores (world/parties.json).
- `PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
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
- `Contact/Name` = **Buying office**  
  The desk that handles this document; identity of Brightmarket Stores (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Contact/Telephone` = **+999 2 3851 0411**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Brightmarket Stores (world/parties.json).
- `Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `AdditionalWebSite/Name` = **Online shop**  
  The store's second website, where consumers buy.
- `AdditionalWebSite/URI` = **https://shop.brightmarket.example**  
  Under the reserved .example domain.
- `SocialMediaProfile/Name` = **brightmarket**  
  The store's profile name.
- `SocialMediaProfile/SocialMediaTypeCode` = **Photo sharing**  
  The kind of social medium.
- `SocialMediaProfile/URI` = **https://social.example/brightmarket**  
  The profile's address, under the reserved .example domain.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Customer Party

Inside `CustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Subscriber Party

Inside `SubscriberParty`:

- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Brightmarket Stores**  
  The same party as at ReceiverParty, where its full details are given; only its identifier and name are repeated.

### Subscriber Consumption

Inside `SubscriberConsumption`:

- `ConsumptionID` = **CSW-CP-38510-411-2603**  
  The consumption of the point in March.
- `SpecificationTypeCode` = **Detailed**  
  A detailed specification.
- `Note` = **Shop, Lumeport**  
  The point.
- `TotalMeteredQuantity` = **86** (unitCode `MTQ`)  
  Metered in March.
- `UtilityConsumptionPoint/ID` = **CSW-CP-38510-411**  
  The connection's number.
- `UtilityConsumptionPoint/Description` = **Shop, Lumeport**  
  Where.
- `UtilityConsumptionPoint/SubscriberID` = **CSW-C-260118**  
  The contract it belongs to.
- `UtilityConsumptionPoint/SubscriberType` = **Commercial**  
  The kind of customer.
- `UtilityConsumptionPoint/SubscriberTypeCode` = **COM**  
  As a code.
- `UtilityConsumptionPoint/TotalDeliveredQuantity` = **86** (unitCode `MTQ`)  
  Delivered in March.
- `UtilityConsumptionPoint/Address/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `UtilityConsumptionPoint/Address/StreetName` = **Market Street**  
  Street of the postal address. identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/BuildingNumber` = **50**  
  Building number of the postal address. identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json).
- `UtilityConsumptionPoint/Address/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `UtilityConsumptionPoint/Address/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `UtilityConsumptionPoint/Address/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `UtilityConsumptionPoint/WebSiteAccess/URI` = **https://www.coastalwater.example/meter**  
  Where the customer sees the readings.
- `UtilityConsumptionPoint/WebSiteAccess/Password` = ************  
  Never printed: the customer chose it online.
- `UtilityConsumptionPoint/WebSiteAccess/Login` = **CSW-CP-38510-411**  
  The customer logs in with the point's number.
- `UtilityConsumptionPoint/UtilityMeter/MeterNumber` = **CSW-W-55102**  
  The meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterName` = **Water meter, shop**  
  Its name.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstant` = **1**  
  The register is multiplied by this.
- `UtilityConsumptionPoint/UtilityMeter/MeterConstantCode` = **Direct**  
  Why: direct.
- `UtilityConsumptionPoint/UtilityMeter/TotalDeliveredQuantity` = **86** (unitCode `MTQ`)  
  Delivered in March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/ID` = **CSW-W-55102-2603**  
  The reading of March.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingType` = **Monthly reading**  
  The kind of reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/MeterReadingTypeCode` = **M**  
  As a code.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingDate` = **2026-02-28**  
  The previous reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterQuantity` = **4212** (unitCode `MTQ`)  
  The register then.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingDate` = **2026-03-31**  
  This reading.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterQuantity` = **4298** (unitCode `MTQ`)  
  The register now.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethod` = **Remote reading**  
  How the previous reading was taken.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/PreviousMeterReadingMethodCode` = **REMOTE**  
  As a code.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethod` = **Remote reading**  
  How this reading was taken.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/LatestMeterReadingMethodCode` = **REMOTE**  
  As a code.
- `UtilityConsumptionPoint/UtilityMeter/MeterReading/DeliveredQuantity` = **86** (unitCode `MTQ`)  
  The difference of the readings.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Accuracy class**  
  A property of the meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/NameCode` = **ACC**  
  As a code.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Value` = **1**  
  Class 1.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQualifier` = **Calibrated 2024**  
  When it was checked.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/Name` = **Maximum flow**  
  A rating of the meter.
- `UtilityConsumptionPoint/UtilityMeter/MeterProperty/ValueQuantity` = **2.5** (unitCode `MQH`)  
  Its value.
- `Consumption/UtilityStatementTypeCode` = **Water**  
  The kind of supply.
- `Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `Consumption/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  The tax of this point's consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ID` = **CSW-CP-38510-411-2603**  
  The consumption report of the point for March.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionType` = **Monthly consumption**  
  What is reported.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionTypeCode` = **MON**  
  As a code.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Description` = **March consumption of Shop, Lumeport.**  
  In words.
- `Consumption/EnergyWaterSupply/ConsumptionReport/TotalConsumedQuantity` = **86** (unitCode `MTQ`)  
  Used in March.
- `Consumption/EnergyWaterSupply/ConsumptionReport/BasicConsumedQuantity` = **86** (unitCode `MTQ`)  
  All at the basic tariff: no reduced-rate hours.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Period/StartDate` = **2026-03-01**  
  March.
- `Consumption/EnergyWaterSupply/ConsumptionReport/Period/EndDate` = **2026-03-31**  
  Its last day.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionReportID` = **CSW-CP-38510-411-2602**  
  The report of February.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionType` = **Monthly consumption**  
  Of the same kind.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/ConsumptionTypeCode` = **MON**  
  As a code.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/TotalConsumedQuantity` = **79** (unitCode `MTQ`)  
  What February's report said.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/StartDate` = **2026-02-01**  
  February.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionReportReference/Period/EndDate` = **2026-02-28**  
  Its last day.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **CSW-W-55102**  
  The meter.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **81** (unitCode `MTQ`)  
  The month's consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **190.35** (currencyID `XBL`)  
  What it cost at the tariff.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **Normal**  
  Within the usual range.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  In words.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Description` = **Earlier month.**  
  For comparison.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-01-01**  
  The month.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-01-31**  
  Its end.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/MeterNumber` = **CSW-W-55102**  
  The meter.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Quantity` = **79** (unitCode `MTQ`)  
  The month's consumption.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Amount` = **185.65** (currencyID `XBL`)  
  What it cost at the tariff.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevelCode` = **Normal**  
  Within the usual range.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/ConsumptionLevel` = **Normal**  
  In words.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Description` = **Earlier month.**  
  For comparison.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/StartDate` = **2026-02-01**  
  The month.
- `Consumption/EnergyWaterSupply/ConsumptionReport/ConsumptionHistory/Period/EndDate` = **2026-02-28**  
  Its end.
- `Consumption/EnergyWaterSupply/ConsumptionAverage/AverageAmount` = **202.10** (currencyID `XBL`)  
  What this month cost.
- `Consumption/EnergyWaterSupply/ConsumptionAverage/Description` = **The average over the last three months is 82 m³.**  
  For comparison.
- `Consumption/LegalMonetaryTotal/LineExtensionAmount` = **202.10** (currencyID `XBL`)  
  The consumption.
- `Consumption/LegalMonetaryTotal/PayableAmount` = **202.10** (currencyID `XBL`)  
  With its tax.
- `SupplierConsumption/Description` = **The supply under the customer's contract.**  
  What follows.
- `SupplierConsumption/UtilitySupplierParty/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilitySupplierParty/PartyName/Name` = **Coastal State Water Company**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/UtilityCustomerParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.
- `SupplierConsumption/Consumption/UtilityStatementTypeCode` = **Water**  
  The supply under the contract.
- `SupplierConsumption/Consumption/MainPeriod/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/Consumption/MainPeriod/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/LineExtensionAmount` = **202.10** (currencyID `XBL`)  
  The line.
- `SupplierConsumption/Consumption/LegalMonetaryTotal/PayableAmount` = **202.10** (currencyID `XBL`)  
  With its tax.
- `SupplierConsumption/Contract/ID` = **CSW-C-260118**  
  The supply contract.
- `SupplierConsumption/Contract/ContractType` = **Water supply**  
  Its kind.
- `SupplierConsumption/Contract/ValidityPeriod/StartDate` = **2024-01-01**  
  In force since.
- `SupplierConsumption/ConsumptionLine/ID` = **1**  
  The line of the consumption.
- `SupplierConsumption/ConsumptionLine/ParentDocumentLineReferenceID` = **1**  
  The line of the invoice this line explains.
- `SupplierConsumption/ConsumptionLine/InvoicedQuantity` = **86** (unitCode `MTQ`)  
  The consumption of this point.
- `SupplierConsumption/ConsumptionLine/LineExtensionAmount` = **202.10** (currencyID `XBL`)  
  Quantity times the tariff.
- `SupplierConsumption/ConsumptionLine/TaxInclusiveLineExtensionAmount` = **202.10** (currencyID `XBL`)  
  With the tax of the line.
- `SupplierConsumption/ConsumptionLine/Period/StartDate` = **2026-03-01**  
  March.
- `SupplierConsumption/ConsumptionLine/Period/EndDate` = **2026-03-31**  
  Its last day.
- `SupplierConsumption/ConsumptionLine/Delivery/DeliveryLocation/Description` = **The consumption point of the statement.**  
  Where it was delivered.
- `SupplierConsumption/ConsumptionLine/TaxTotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the line.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ID` = **CW-M3**  
  The utility's tariff item.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberID` = **CSW-C-260118**  
  The customer's contract.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberType` = **Water**  
  The kind of supply.
- `SupplierConsumption/ConsumptionLine/UtilityItem/SubscriberTypeCode` = **WATE**  
  As a code.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Description` = **Drinking water supply, per cubic metre.**  
  The tariff in words.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionType` = **Metered**  
  How the quantity is measured.
- `SupplierConsumption/ConsumptionLine/UtilityItem/ConsumptionTypeCode` = **MET**  
  As a code.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeType` = **Monthly**  
  Charged every month.
- `SupplierConsumption/ConsumptionLine/UtilityItem/CurrentChargeTypeCode` = **M**  
  As a code.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/ID` = **E**  
  Drinking water is exempt from the state sales tax (category E).
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxExemptionReasonCode` = **XB-WATER**  
  The world's code for the exemption reason (world/countries.json).
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxExemptionReason` = **Drinking water**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `SupplierConsumption/ConsumptionLine/UtilityItem/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `SupplierConsumption/ConsumptionLine/UtilityItem/Contract/ID` = **CSW-C-260118**  
  The supply contract the tariff belongs to.
- `SupplierConsumption/ConsumptionLine/Price/PriceAmount` = **2.35** (currencyID `XBL`)  
  The tariff (world/items.json).
- `SupplierConsumption/ConsumptionLine/Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  Per unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<UtilityStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:UtilityStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:utilities</cbc:ProfileID>
  <cbc:ProfileExecutionID>UTILITIES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>CSWC-DOC-26-0318</cbc:ID>
  <cbc:UUID>7bdfb021-49a1-5341-b641-0343b4c0240e</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>11:55:00</cbc:IssueTime>
  <cbc:UtilityStatementTypeCode>Water</cbc:UtilityStatementTypeCode>
  <cbc:Note>This statement explains the consumption behind your bill.</cbc:Note>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>6120</cbc:AccountingCostCode>
  <cbc:AccountingCost>Garden department</cbc:AccountingCost>
  <cac:ParentDocumentReference>
    <cbc:ID>CSWC-INV-26-0317</cbc:ID>
  </cac:ParentDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>CSWC-TARIFF-2026</cbc:ID>
    <cbc:DocumentTypeCode>Tariff</cbc:DocumentTypeCode>
    <cbc:DocumentDescription>Prices per unit and the terms of supply.</cbc:DocumentDescription>
  </cac:AdditionalDocumentReference>
  <cac:SenderParty>
    <cbc:WebsiteURI>https://www.coastalwater.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">3600</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Coastal State Water Company</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Reservoir Road</cbc:StreetName>
      <cbc:BuildingNumber>51</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Harbour quarter</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38500</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Coastal State Water Company Ltd</cbc:RegistrationName>
      <cbc:CompanyID>CO-1236576</cbc:CompanyID>
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
      <cbc:RegistrationName>Coastal State Water Company Ltd</cbc:RegistrationName>
      <cbc:CompanyID>20412192</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
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
      <cbc:Name>Customer service</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 3850 2192</cbc:Telephone>
      <cbc:ElectronicMail>customer@coastalwater.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412192</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.brightmarket.example</cbc:WebsiteURI>
    <cbc:LogoReferenceID>BM-LOGO-2024</cbc:LogoReferenceID>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4719</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
    <cac:TradePartyName>
      <cbc:Name>Brightmarket</cbc:Name>
    </cac:TradePartyName>
    <cac:Language>
      <cbc:ID>en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode>EN</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Market Street</cbc:StreetName>
      <cbc:BuildingNumber>50</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38515</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
      <cbc:CompanyID>CO-1231233</cbc:CompanyID>
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
      <cbc:RegistrationName>Brightmarket Stores Corp</cbc:RegistrationName>
      <cbc:CompanyID>20410411</cbc:CompanyID>
      <cbc:RegistrationDate>1979-02-14</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Corp</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Corporation (public)</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
      <cbc:CorporateStockAmount currencyID="XBL">12000000</cbc:CorporateStockAmount>
      <cbc:FullyPaidSharesIndicator>true</cbc:FullyPaidSharesIndicator>
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
      <cbc:Name>Buying office</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 2 3851 0411</cbc:Telephone>
      <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:AdditionalWebSite>
      <cbc:Name>Online shop</cbc:Name>
      <cbc:URI>https://shop.brightmarket.example</cbc:URI>
    </cac:AdditionalWebSite>
    <cac:SocialMediaProfile>
      <cbc:Name>brightmarket</cbc:Name>
      <cbc:SocialMediaTypeCode>Photo sharing</cbc:SocialMediaTypeCode>
      <cbc:URI>https://social.example/brightmarket</cbc:URI>
    </cac:SocialMediaProfile>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:CustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:CustomerParty>
  <cac:SubscriberParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
  </cac:SubscriberParty>
  <cac:SubscriberConsumption>
    <cbc:ConsumptionID>CSW-CP-38510-411-2603</cbc:ConsumptionID>
    <cbc:SpecificationTypeCode>Detailed</cbc:SpecificationTypeCode>
    <cbc:Note>Shop, Lumeport</cbc:Note>
    <cbc:TotalMeteredQuantity unitCode="MTQ">86</cbc:TotalMeteredQuantity>
    <cac:UtilityConsumptionPoint>
      <cbc:ID>CSW-CP-38510-411</cbc:ID>
      <cbc:Description>Shop, Lumeport</cbc:Description>
      <cbc:SubscriberID>CSW-C-260118</cbc:SubscriberID>
      <cbc:SubscriberType>Commercial</cbc:SubscriberType>
      <cbc:SubscriberTypeCode>COM</cbc:SubscriberTypeCode>
      <cbc:TotalDeliveredQuantity unitCode="MTQ">86</cbc:TotalDeliveredQuantity>
      <cac:Address>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Market Street</cbc:StreetName>
        <cbc:BuildingNumber>50</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38515</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:Address>
      <cac:WebSiteAccess>
        <cbc:URI>https://www.coastalwater.example/meter</cbc:URI>
        <cbc:Password>********</cbc:Password>
        <cbc:Login>CSW-CP-38510-411</cbc:Login>
      </cac:WebSiteAccess>
      <cac:UtilityMeter>
        <cbc:MeterNumber>CSW-W-55102</cbc:MeterNumber>
        <cbc:MeterName>Water meter, shop</cbc:MeterName>
        <cbc:MeterConstant>1</cbc:MeterConstant>
        <cbc:MeterConstantCode>Direct</cbc:MeterConstantCode>
        <cbc:TotalDeliveredQuantity unitCode="MTQ">86</cbc:TotalDeliveredQuantity>
        <cac:MeterReading>
          <cbc:ID>CSW-W-55102-2603</cbc:ID>
          <cbc:MeterReadingType>Monthly reading</cbc:MeterReadingType>
          <cbc:MeterReadingTypeCode>M</cbc:MeterReadingTypeCode>
          <cbc:PreviousMeterReadingDate>2026-02-28</cbc:PreviousMeterReadingDate>
          <cbc:PreviousMeterQuantity unitCode="MTQ">4212</cbc:PreviousMeterQuantity>
          <cbc:LatestMeterReadingDate>2026-03-31</cbc:LatestMeterReadingDate>
          <cbc:LatestMeterQuantity unitCode="MTQ">4298</cbc:LatestMeterQuantity>
          <cbc:PreviousMeterReadingMethod>Remote reading</cbc:PreviousMeterReadingMethod>
          <cbc:PreviousMeterReadingMethodCode>REMOTE</cbc:PreviousMeterReadingMethodCode>
          <cbc:LatestMeterReadingMethod>Remote reading</cbc:LatestMeterReadingMethod>
          <cbc:LatestMeterReadingMethodCode>REMOTE</cbc:LatestMeterReadingMethodCode>
          <cbc:DeliveredQuantity unitCode="MTQ">86</cbc:DeliveredQuantity>
        </cac:MeterReading>
        <cac:MeterProperty>
          <cbc:Name>Accuracy class</cbc:Name>
          <cbc:NameCode>ACC</cbc:NameCode>
          <cbc:Value>1</cbc:Value>
          <cbc:ValueQualifier>Calibrated 2024</cbc:ValueQualifier>
        </cac:MeterProperty>
        <cac:MeterProperty>
          <cbc:Name>Maximum flow</cbc:Name>
          <cbc:ValueQuantity unitCode="MQH">2.5</cbc:ValueQuantity>
        </cac:MeterProperty>
      </cac:UtilityMeter>
    </cac:UtilityConsumptionPoint>
    <cac:Consumption>
      <cbc:UtilityStatementTypeCode>Water</cbc:UtilityStatementTypeCode>
      <cac:MainPeriod>
        <cbc:StartDate>2026-03-01</cbc:StartDate>
        <cbc:EndDate>2026-03-31</cbc:EndDate>
      </cac:MainPeriod>
      <cac:TaxTotal>
        <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      </cac:TaxTotal>
      <cac:EnergyWaterSupply>
        <cac:ConsumptionReport>
          <cbc:ID>CSW-CP-38510-411-2603</cbc:ID>
          <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode>MON</cbc:ConsumptionTypeCode>
          <cbc:Description>March consumption of Shop, Lumeport.</cbc:Description>
          <cbc:TotalConsumedQuantity unitCode="MTQ">86</cbc:TotalConsumedQuantity>
          <cbc:BasicConsumedQuantity unitCode="MTQ">86</cbc:BasicConsumedQuantity>
          <cac:Period>
            <cbc:StartDate>2026-03-01</cbc:StartDate>
            <cbc:EndDate>2026-03-31</cbc:EndDate>
          </cac:Period>
          <cac:ConsumptionReportReference>
            <cbc:ConsumptionReportID>CSW-CP-38510-411-2602</cbc:ConsumptionReportID>
            <cbc:ConsumptionType>Monthly consumption</cbc:ConsumptionType>
            <cbc:ConsumptionTypeCode>MON</cbc:ConsumptionTypeCode>
            <cbc:TotalConsumedQuantity unitCode="MTQ">79</cbc:TotalConsumedQuantity>
            <cac:Period>
              <cbc:StartDate>2026-02-01</cbc:StartDate>
              <cbc:EndDate>2026-02-28</cbc:EndDate>
            </cac:Period>
          </cac:ConsumptionReportReference>
          <cac:ConsumptionHistory>
            <cbc:MeterNumber>CSW-W-55102</cbc:MeterNumber>
            <cbc:Quantity unitCode="MTQ">81</cbc:Quantity>
            <cbc:Amount currencyID="XBL">190.35</cbc:Amount>
            <cbc:ConsumptionLevelCode>Normal</cbc:ConsumptionLevelCode>
            <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
            <cbc:Description>Earlier month.</cbc:Description>
            <cac:Period>
              <cbc:StartDate>2026-01-01</cbc:StartDate>
              <cbc:EndDate>2026-01-31</cbc:EndDate>
            </cac:Period>
          </cac:ConsumptionHistory>
          <cac:ConsumptionHistory>
            <cbc:MeterNumber>CSW-W-55102</cbc:MeterNumber>
            <cbc:Quantity unitCode="MTQ">79</cbc:Quantity>
            <cbc:Amount currencyID="XBL">185.65</cbc:Amount>
            <cbc:ConsumptionLevelCode>Normal</cbc:ConsumptionLevelCode>
            <cbc:ConsumptionLevel>Normal</cbc:ConsumptionLevel>
            <cbc:Description>Earlier month.</cbc:Description>
            <cac:Period>
              <cbc:StartDate>2026-02-01</cbc:StartDate>
              <cbc:EndDate>2026-02-28</cbc:EndDate>
            </cac:Period>
          </cac:ConsumptionHistory>
        </cac:ConsumptionReport>
        <cac:ConsumptionAverage>
          <cbc:AverageAmount currencyID="XBL">202.10</cbc:AverageAmount>
          <cbc:Description>The average over the last three months is 82 m³.</cbc:Description>
        </cac:ConsumptionAverage>
      </cac:EnergyWaterSupply>
      <cac:LegalMonetaryTotal>
        <cbc:LineExtensionAmount currencyID="XBL">202.10</cbc:LineExtensionAmount>
        <cbc:PayableAmount currencyID="XBL">202.10</cbc:PayableAmount>
      </cac:LegalMonetaryTotal>
    </cac:Consumption>
    <cac:SupplierConsumption>
      <cbc:Description>The supply under the customer's contract.</cbc:Description>
      <cac:UtilitySupplierParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Coastal State Water Company</cbc:Name>
        </cac:PartyName>
      </cac:UtilitySupplierParty>
      <cac:UtilityCustomerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Brightmarket Stores</cbc:Name>
        </cac:PartyName>
      </cac:UtilityCustomerParty>
      <cac:Consumption>
        <cbc:UtilityStatementTypeCode>Water</cbc:UtilityStatementTypeCode>
        <cac:MainPeriod>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:MainPeriod>
        <cac:LegalMonetaryTotal>
          <cbc:LineExtensionAmount currencyID="XBL">202.10</cbc:LineExtensionAmount>
          <cbc:PayableAmount currencyID="XBL">202.10</cbc:PayableAmount>
        </cac:LegalMonetaryTotal>
      </cac:Consumption>
      <cac:Contract>
        <cbc:ID>CSW-C-260118</cbc:ID>
        <cbc:ContractType>Water supply</cbc:ContractType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2024-01-01</cbc:StartDate>
        </cac:ValidityPeriod>
      </cac:Contract>
      <cac:ConsumptionLine>
        <cbc:ID>1</cbc:ID>
        <cbc:ParentDocumentLineReferenceID>1</cbc:ParentDocumentLineReferenceID>
        <cbc:InvoicedQuantity unitCode="MTQ">86</cbc:InvoicedQuantity>
        <cbc:LineExtensionAmount currencyID="XBL">202.10</cbc:LineExtensionAmount>
        <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">202.10</cbc:TaxInclusiveLineExtensionAmount>
        <cac:Period>
          <cbc:StartDate>2026-03-01</cbc:StartDate>
          <cbc:EndDate>2026-03-31</cbc:EndDate>
        </cac:Period>
        <cac:Delivery>
          <cac:DeliveryLocation>
            <cbc:Description>The consumption point of the statement.</cbc:Description>
          </cac:DeliveryLocation>
        </cac:Delivery>
        <cac:TaxTotal>
          <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
        </cac:TaxTotal>
        <cac:UtilityItem>
          <cbc:ID>CW-M3</cbc:ID>
          <cbc:SubscriberID>CSW-C-260118</cbc:SubscriberID>
          <cbc:SubscriberType>Water</cbc:SubscriberType>
          <cbc:SubscriberTypeCode>WATE</cbc:SubscriberTypeCode>
          <cbc:Description>Drinking water supply, per cubic metre.</cbc:Description>
          <cbc:ConsumptionType>Metered</cbc:ConsumptionType>
          <cbc:ConsumptionTypeCode>MET</cbc:ConsumptionTypeCode>
          <cbc:CurrentChargeType>Monthly</cbc:CurrentChargeType>
          <cbc:CurrentChargeTypeCode>M</cbc:CurrentChargeTypeCode>
          <cac:TaxCategory>
            <cbc:ID>E</cbc:ID>
            <cbc:Percent>0</cbc:Percent>
            <cbc:TaxExemptionReasonCode>XB-WATER</cbc:TaxExemptionReasonCode>
            <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
            <cac:TaxScheme>
              <cbc:ID>STT</cbc:ID>
            </cac:TaxScheme>
          </cac:TaxCategory>
          <cac:Contract>
            <cbc:ID>CSW-C-260118</cbc:ID>
          </cac:Contract>
        </cac:UtilityItem>
        <cac:Price>
          <cbc:PriceAmount currencyID="XBL">2.35</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
        </cac:Price>
      </cac:ConsumptionLine>
    </cac:SupplierConsumption>
  </cac:SubscriberConsumption>
</UtilityStatement>
```
