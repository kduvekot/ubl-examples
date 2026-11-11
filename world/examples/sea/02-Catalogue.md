# Catalogue: Lumeway Distribution to Velumi Trading

*Example 2 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Catalogue in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-CATALOGUE-SCHEMA)*

The export catalogue for the island customer.

[The XML file](02-Catalogue.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:sea**  
  The business process the document belongs to: the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)".
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **LD-CAT-26-0124**  
  The provider's catalogue number.
- `UUID` = **40262193-531c-5797-8c01-d23252c67188**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `Name` = **Lumeway Distribution catalogue**  
  The catalogue's title.
- `IssueDate` = **2026-05-04**  
  The export catalogue for the island customer.
- `IssueTime` = **09:17:00**  
  The time the sender's system issued the document, in the sender's local time.

### Validity Period

Inside `ValidityPeriod`:

- `StartDate` = **2026-05-04**  
  The prices apply from the issue date.
- `EndDate` = **2026-10-31**  
  Until the next catalogue.

### Provider Party

Inside `ProviderParty`:

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
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
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
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
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

### Receiver Party

Inside `ReceiverParty`:

- `WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json).
- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `PostalAddress/StreetName` = **Kavama Timeku** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Velumi Trading (world/parties.json).
- `PostalAddress/StreetName` = **Reef Street** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Velumi Trading (world/parties.json).
- `PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Velumi Trading (world/parties.json).
- `PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
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
- `Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Contact/Telephone` = **+999 3 3000 1859**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Velumi Trading (world/parties.json).
- `Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The same party as at ProviderParty, where its full details are given; only its identifier and name are repeated.

### Catalogue Line

Inside `CatalogueLine`:

- `ID` = **1**  
  The line number.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **3** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **4** (unitCode `H87`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/MaximumQuantity` = **192** (unitCode `H87`)  
  The most one order can take from stock: two containers.
- `RequiredItemLocationQuantity/TradingRestrictions` = **Not sold to consumers.**  
  The bench is sold through retailers.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XB**  
  The catalogue is offered for buyers in the seller's country.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **520** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `H87`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD**  
  The seller's code for its trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  A price for resellers, before sales tax.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-05-04**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-10-31**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **6-XB-PL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **Active**  
  The price list is in force.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/PriceAmount` = **208** (currencyID `XLC`)  
  The same price in the buyer's currency, at the world's reference rate on the catalogue's issue day; for information only.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/BaseQuantity` = **1** (unitCode `H87`)  
  Per one unit.
- `RequiredItemLocationQuantity/DeliveryUnit/BatchQuantity` = **4** (unitCode `H87`)  
  The benches are delivered per pallet of four.
- `RequiredItemLocationQuantity/DeliveryUnit/ConsumerUnitQuantity` = **1** (unitCode `H87`)  
  One bench is one consumer unit.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **G**  
  An export from Bayvarra: the state sales tax is not charged (category G).
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **XB-EXP**  
  The world's code for the exemption reason (world/countries.json).
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `RequiredItemLocationQuantity/Package/ID` = **PAL-4**  
  The pallet the price is for.
- `RequiredItemLocationQuantity/Package/Quantity` = **4** (unitCode `H87`)  
  Four benches to a pallet.
- `RequiredItemLocationQuantity/Package/PackagingTypeCode` = **PX**  
  UN/ECE Recommendation 21 code PX: pallet.
- `RequiredItemLocationQuantity/AllowanceCharge/ChargeIndicator` = **false**  
  A discount.
- `RequiredItemLocationQuantity/AllowanceCharge/AllowanceChargeReasonCode` = **78** (listID `UN/EDIFACT EDED 5189`)  
  UN/EDIFACT 5189 code 78: volume discount.
- `RequiredItemLocationQuantity/AllowanceCharge/AllowanceChargeReason` = **Full container**  
  The discount for a full container.
- `RequiredItemLocationQuantity/AllowanceCharge/MultiplierFactorNumeric` = **0.03**  
  Three percent off.
- `RequiredItemLocationQuantity/AllowanceCharge/Amount` = **15.60** (currencyID `XBL`)  
  The discount per bench.
- `RequiredItemLocationQuantity/AllowanceCharge/BaseAmount` = **520.00** (currencyID `XBL`)  
  The catalogue price the discount is taken from.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/StartDate` = **2026-05-11**  
  The first deliveries from the season's stock.
- `RequiredItemLocationQuantity/ApplicableDeliveryPeriod/EndDate` = **2026-10-31**  
  The last.
- `Item/Description` = **The manufacturer's Serra bench, from the distributor's stock.**  
  The seller's description; item bench-serra-b of Lumeway Distribution (world/items.json).
- `Item/CatalogueIndicator` = **true**  
  The item is described as it appears in the seller's catalogue.
- `Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra-b of Lumeway Distribution (world/items.json).
- `Item/AdditionalInformation` = **Supplied with four ground anchors and the bolts to fix them.**  
  What comes with the item; item bench-serra of Valdara Industries (world/items.json).
- `Item/Keyword` = **park bench**  
  A word buyers search the item by.
- `Item/Keyword` = **street furniture**  
  A word buyers search the item by.
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-serra of Valdara Industries (world/items.json).
- `Item/ModelName` = **Serra 180**  
  The model; item bench-serra of Valdara Industries (world/items.json).
- `Item/WarrantyInformation` = **Five years on the frame against corrosion.**  
  The maker's warranty; item bench-serra of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **LD-10442**  
  The seller's own item number; item bench-serra-b of Lumeway Distribution (world/items.json).
- `Item/SellersItemIdentification/ExtendedID` = **GRY**  
  The variant of the item: the frame colour, added to the item number.
- `Item/SellersItemIdentification/PhysicalAttribute/AttributeID` = **Colour**  
  The attribute the variant differs in.
- `Item/SellersItemIdentification/PhysicalAttribute/PositionCode` = **FRM**  
  The part of the item the attribute is on: the frame.
- `Item/SellersItemIdentification/PhysicalAttribute/DescriptionCode` = **GRY**  
  The variant's code for it.
- `Item/SellersItemIdentification/PhysicalAttribute/Description` = **Frame in Ferro grey**  
  The variant in words.
- `Item/ManufacturersItemIdentification/ID` = **VI-B180**  
  The item number of the maker, Valdara Industries: the reseller's item is resale of item bench-serra.
- `Item/StandardItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-serra of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/BarcodeSymbologyID` = **Code128**  
  The barcode the number is printed in on the label.
- `Item/StandardItemIdentification/IssuerScopeID` = **771**  
  The range of item numbers the agency gives out in the maker's country.
- `Item/StandardItemIdentification/IssuerParty/IndustryClassificationCode` = **8299** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Codana Identification Agency (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Item/StandardItemIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  The trading name; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/Language/ID` = **qau**  
  Urvanian, the language of Urvania and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Item/StandardItemIdentification/IssuerParty/Language/Name` = **Urvanian**  
  The language's name in English; in the language itself: urvanese.
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/StreetName` = **Ganluar Ranvua Culsceor** (languageID `qau`)  
  The street's name in Urvanian: Urvania is officially bilingual, and street names are given in both languages (world/countries.json); identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/StreetName` = **Via dei Codici** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/BuildingNumber` = **29**  
  Building number of the postal address. identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Item/StandardItemIdentification/IssuerParty/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Item/StandardItemIdentification/IssuerParty/PartyTaxScheme/RegistrationName` = **Codana Identification Agency SRU**  
  The name under which the party is registered for value added tax; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PartyTaxScheme/CompanyID` = **XU007395206**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Item/StandardItemIdentification/IssuerParty/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Item/StandardItemIdentification/IssuerParty/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Item/StandardItemIdentification/IssuerParty/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/RegistrationName` = **Codana Identification Agency SRU**  
  The name under which the party is registered, with its legal form; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/CompanyID` = **XU-R-105644**  
  Number in the Commercial register of Urvania; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/CompanyLegalFormCode` = **SRU**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/CompanyLegalForm` = **Società a responsabilità urvaniana (private limited company)**  
  The legal form, in words.
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/RegistrationAddress/CityName` = **Ferrano**  
  The registered office, as entered in the register.
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XU**  
  The country of registration.
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XU:CR**  
  The identifier of the register in the world (world/countries.json).
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Commercial register of Urvania**  
  The register the company is entered in.
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Item/StandardItemIdentification/IssuerParty/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The register covers the whole country.
- `Item/StandardItemIdentification/IssuerParty/Contact/Name` = **Member services**  
  The desk that handles this document; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/Contact/JobTitle` = **Public service officer**  
  The job of the person who answers at the desk; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/Contact/Department` = **Public services**  
  The department the desk belongs to; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/Contact/Telephone` = **+999 1 4130 5644**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/Contact/ElectronicMail` = **member@codana.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Codana Identification Agency (world/parties.json).
- `Item/StandardItemIdentification/IssuerParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Item/StandardItemIdentification/IssuerParty/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105644** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Codana Identification Agency (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `Item/CatalogueItemIdentification/ID` = **LD-CAT-26-0124-1**  
  The item's place in the catalogue: the catalogue number and the line.
- `Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json).
- `Item/CommodityClassification/CommodityCode` = **9401.79.10**  
  The national tariff code below the HS subheading, as the customs of the maker's country uses it.
- `Item/CommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-serra of Valdara Industries (world/items.json).
- `Item/TransactionConditions/ID` = **LD-TC-01**  
  The seller's number for these conditions of sale.
- `Item/TransactionConditions/ActionCode` = **Trade**  
  To whom the conditions apply.
- `Item/TransactionConditions/Description` = **Sold to trade customers only, per pallet of four benches.**  
  The conditions in words.
- `Item/TransactionConditions/DocumentReference/ID` = **LD-GTC-2026**  
  The seller's general terms of trade.
- `Item/AdditionalItemProperty/Name` = **Frame material**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Cast steel, hot-dip galvanised**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Slat wood**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Kiln-dried hardwood**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Seats**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **3**  
  Its value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/ID` = **COL**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Frame colour**  
  The colours the frame is offered in.
- `Item/AdditionalItemProperty/ImportanceCode` = **Optional**  
  How much the property matters in describing the item.
- `Item/AdditionalItemProperty/ListValue` = **Ferro grey**  
  One of the values the property can take.
- `Item/AdditionalItemProperty/ListValue` = **Moss green**  
  One of the values the property can take.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **APP**  
  The group of properties this one belongs to.
- `Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Appearance**  
  The group's name.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **Optional**  
  How much the group matters.
- `Item/AdditionalItemProperty/ID` = **LOAD**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Load capacity**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/NameCode` = **LOAD**  
  The property's name as a code, as the property standard lists it.
- `Item/AdditionalItemProperty/TestMethod` = **Static load on the seat for one hour, three seats loaded evenly, no lasting deformation**  
  How the value is tested.
- `Item/AdditionalItemProperty/ValueQuantity` = **450** (unitCode `KGM`)  
  Its measured value; item bench-serra of Valdara Industries (world/items.json).
- `Item/AdditionalItemProperty/ValueQualifier` = **Distributed over the seat**  
  What the value stands for.
- `Item/AdditionalItemProperty/ImportanceCode` = **Mandatory**  
  How much the property matters in describing the item.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **SAF**  
  The group of properties this one belongs to.
- `Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Safety**  
  The group's name.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **Mandatory**  
  How much the group matters.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-SF-0450**  
  The property's number in the property standard of the identification agency.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **Codana street furniture properties**  
  The part of the agency's standards it is taken from.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/ManufacturerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/ManufacturerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/InformationContentProviderParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/InformationContentProviderParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Dimension/AttributeID` = **Length**  
  Which dimension.
- `Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Over the armrests**  
  Where it is measured.
- `Item/Dimension/AttributeID` = **Depth**  
  Which dimension.
- `Item/Dimension/Measure` = **620** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/AttributeID` = **Height**  
  Which dimension.
- `Item/Dimension/Measure` = **780** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Seat back at its highest point**  
  Where it is measured.
- `Item/Dimension/AttributeID` = **Seat height**  
  Which dimension.
- `Item/Dimension/Measure` = **450** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/Description` = **Above the ground when anchored**  
  Where it is measured.
- `Item/Dimension/MinimumMeasure` = **440** (unitCode `MMT`)  
  The lowest it can be set to.
- `Item/Dimension/MaximumMeasure` = **460** (unitCode `MMT`)  
  The highest it can be set to.
- `Item/EnvironmentalEmission/EnvironmentalEmissionTypeCode` = **CO2e**  
  The emission reported: greenhouse gases as CO2 equivalent.
- `Item/EnvironmentalEmission/ValueMeasure` = **96** (unitCode `KGM`)  
  The emission of one item.
- `Item/EnvironmentalEmission/ValueFactorNumeric` = **0.82**  
  The share of the footprint the steel frame accounts for.
- `Item/EnvironmentalEmission/ValueBaseMeasure` = **1** (unitCode `H87`)  
  The emission is per one bench.
- `Item/EnvironmentalEmission/EmissionStandardReference` = **Greenhouse Gas Protocol Product Standard**  
  The standard the footprint is calculated by.
- `Item/EnvironmentalEmission/LifecycleStageCode` = **Manufacturing**  
  The part of the bench's life the figure covers.
- `Item/EnvironmentalEmission/LifecycleStageDescription` = **From the ore at the mine to the bench leaving the factory gate.**  
  That part in words.
- `Item/EnvironmentalEmission/Description` = **Mining, steel making, casting, galvanising, sawing and the transport between them.**  
  What the figure includes.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/CalculationMethodCode` = **Calculated**  
  Calculated, not measured.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/FullnessIndicationCode` = **Cradle to gate**  
  How much of the chain is included.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorSource` = **The steelworks' and sawmill's measured energy use of 2025**  
  Where the factors come from.
- `Item/EnvironmentalEmission/EmissionCalculationMethod/EmissionFactorDocumentReference/ID` = **VI-LCA-2025**  
  The report with the emission factors.
- `Item/EnvironmentalEmission/MeasurementPeriod/StartDate` = **2025-01-01**  
  The year the figures are from.
- `Item/EnvironmentalEmission/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/MaintenanceFrequencyCode` = **Yearly**  
  How often the item needs maintenance.
- `Item/CircularityProfile/MaintenanceFrequencyDescription` = **Tighten the slat bolts and touch up the coating once a year.**  
  What the maintenance is.
- `Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **Steel**  
  A material the item is made of.
- `Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **34** (unitCode `KGM`)  
  How much of it one item uses.
- `Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Steel made from Serravona ore in Urvania**  
  Where the material comes from.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/ResourceConsumption/ResourceTypeCode` = **Hardwood**  
  A material the item is made of.
- `Item/CircularityProfile/ResourceConsumption/ConsumptionMeasure` = **22.5** (unitCode `KGM`)  
  How much of it one item uses.
- `Item/CircularityProfile/ResourceConsumption/ResourceOriginDescription` = **Slats from Upland State, Bayvarra**  
  Where the material comes from.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the production of 2025.
- `Item/CircularityProfile/ResourceConsumption/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/WasteGenerated/WasteTypeCode` = **Packaging**  
  The kind of waste the item leaves.
- `Item/CircularityProfile/WasteGenerated/WasteTypeDescription` = **Stretch film and pallet straps, per bench**  
  The waste in words.
- `Item/CircularityProfile/WasteGenerated/WasteMeasure` = **0.4** (unitCode `KGM`)  
  How much of it per item.
- `Item/CircularityProfile/WasteGenerated/MeasurementPeriod/StartDate` = **2025-01-01**  
  Measured over the deliveries of 2025.
- `Item/CircularityProfile/WasteGenerated/MeasurementPeriod/EndDate` = **2025-12-31**  
  Its last day.
- `Item/CircularityProfile/RepairabilityScore/ScoreNumeric` = **8**  
  Side frames and slats can be replaced one by one, which is why the spare side frame exists.
- `Item/CircularityProfile/RepairabilityScore/ScoringSystemCode` = **Repairability index, 0–10**  
  The scale of the score.
- `Item/CircularityProfile/ProductDocumentationDocumentReference/ID` = **VI-RM-B180**  
  The repair and maintenance manual.
- `ID` = **2**  
  The line number.
- `RequiredItemLocationQuantity/LeadTimeMeasure` = **2** (unitCode `DAY`)  
  The days between order and despatch.
- `RequiredItemLocationQuantity/MinimumQuantity` = **1** (unitCode `H87`)  
  The smallest quantity the seller accepts on an order.
- `RequiredItemLocationQuantity/ApplicableTerritoryAddress/Country/IdentificationCode` = **XB**  
  The catalogue is offered for buyers in the seller's country.
- `RequiredItemLocationQuantity/Price/PriceAmount` = **64** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `RequiredItemLocationQuantity/Price/BaseQuantity` = **1** (unitCode `H87`)  
  The price is per one unit.
- `RequiredItemLocationQuantity/Price/PriceTypeCode` = **TRD**  
  The seller's code for its trade price.
- `RequiredItemLocationQuantity/Price/PriceType` = **Trade price**  
  A price for resellers, before sales tax.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/StartDate` = **2026-05-04**  
  The price applies from the catalogue's issue date.
- `RequiredItemLocationQuantity/Price/ValidityPeriod/EndDate` = **2026-10-31**  
  And until the catalogue ends.
- `RequiredItemLocationQuantity/Price/PriceList/ID` = **6-XB-PL-2026**  
  The seller's price list this price is taken from.
- `RequiredItemLocationQuantity/Price/PriceList/StatusCode` = **Active**  
  The price list is in force.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/PriceAmount` = **25.6** (currencyID `XLC`)  
  The same price in the buyer's currency, at the world's reference rate on the catalogue's issue day; for information only.
- `RequiredItemLocationQuantity/Price/AlternativeCurrencyPrice/BaseQuantity` = **1** (unitCode `H87`)  
  Per one unit.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/ID` = **G**  
  An export from Bayvarra: the state sales tax is not charged (category G).
- `RequiredItemLocationQuantity/ApplicableTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReasonCode` = **XB-EXP**  
  The world's code for the exemption reason (world/countries.json).
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `RequiredItemLocationQuantity/ApplicableTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `RequiredItemLocationQuantity/DependentPriceReference/Percent` = **12.31**  
  The spare frame costs this share of the bench's price, as the distributor's price rule sets it.
- `RequiredItemLocationQuantity/DependentPriceReference/DependentLineReference/LineID` = **1**  
  The catalogue line of the bench.
- `Item/Description` = **Spare side frame for the Serra bench.**  
  The seller's description; item bench-casting-b of Lumeway Distribution (world/items.json).
- `Item/CatalogueIndicator` = **true**  
  The item is described as it appears in the seller's catalogue.
- `Item/Name` = **Bench side frame casting**  
  The item's short name; item bench-casting-b of Lumeway Distribution (world/items.json).
- `Item/BrandName` = **Valdara**  
  The brand the maker sells the item under; item bench-casting of Valdara Industries (world/items.json).
- `Item/ModelName` = **Serra 180 side frame**  
  The model; item bench-casting of Valdara Industries (world/items.json).
- `Item/SellersItemIdentification/ID` = **LD-10443**  
  The seller's own item number; item bench-casting-b of Lumeway Distribution (world/items.json).
- `Item/ManufacturersItemIdentification/ID` = **VI-C180**  
  The item number of the maker, Valdara Industries: the reseller's item is resale of item bench-casting.
- `Item/StandardItemIdentification/ID` = **771020000034** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-casting of Valdara Industries (world/items.json).
- `Item/StandardItemIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at CatalogueLine/Item/StandardItemIdentification/IssuerParty, where its full details are given; only its identifier and name are repeated.
- `Item/StandardItemIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  The same party as at CatalogueLine/Item/StandardItemIdentification/IssuerParty, where its full details are given; only its identifier and name are repeated.
- `Item/CatalogueItemIdentification/ID` = **LD-CAT-26-0124-2**  
  The item's place in the catalogue: the catalogue number and the line.
- `Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-casting of Valdara Industries (world/items.json).
- `Item/CommodityClassification/CommodityCode` = **7325.99.90**  
  The national tariff code below the HS subheading, as the customs of the maker's country uses it.
- `Item/CommodityClassification/ItemClassificationCode` = **7325.99** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-casting of Valdara Industries (world/items.json).
- `Item/ManufacturerParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/ManufacturerParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/InformationContentProviderParty/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/InformationContentProviderParty/PartyName/Name` = **Valdara Industries**  
  A party referred to from another party's details: its identifier and name are enough.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Catalogue xmlns="urn:oasis:names:specification:ubl:schema:xsd:Catalogue-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:sea</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>LD-CAT-26-0124</cbc:ID>
  <cbc:UUID>40262193-531c-5797-8c01-d23252c67188</cbc:UUID>
  <cbc:Name>Lumeway Distribution catalogue</cbc:Name>
  <cbc:IssueDate>2026-05-04</cbc:IssueDate>
  <cbc:IssueTime>09:17:00</cbc:IssueTime>
  <cac:ValidityPeriod>
    <cbc:StartDate>2026-05-04</cbc:StartDate>
    <cbc:EndDate>2026-10-31</cbc:EndDate>
  </cac:ValidityPeriod>
  <cac:ProviderParty>
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
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
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
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
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
  </cac:ProviderParty>
  <cac:ReceiverParty>
    <cbc:WebsiteURI>https://www.velumi.example</cbc:WebsiteURI>
    <cbc:IndustryClassificationCode listID="ISIC Rev.4">4649</cbc:IndustryClassificationCode>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:customs-trader">XL-TR-041859</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID>qal</cbc:ID>
      <cbc:Name>Lisavan</cbc:Name>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
      <cbc:StreetName languageID="qal">Kavama Timeku</cbc:StreetName>
      <cbc:StreetName languageID="en">Reef Street</cbc:StreetName>
      <cbc:BuildingNumber>16</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        <cbc:Name>Lisavu</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Velumi Trading Ltd</cbc:RegistrationName>
      <cbc:CompanyID>IC41859</cbc:CompanyID>
      <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
      <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
      <cbc:CompanyLegalForm>Island limited company</cbc:CompanyLegalForm>
      <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
      <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
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
      <cbc:Name>Purchasing</cbc:Name>
      <cbc:JobTitle>Customer service officer</cbc:JobTitle>
      <cbc:Department>Sales</cbc:Department>
      <cbc:Telephone>+999 3 3000 1859</cbc:Telephone>
      <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:CatalogueLine>
    <cbc:ID>1</cbc:ID>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">3</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="H87">4</cbc:MinimumQuantity>
      <cbc:MaximumQuantity unitCode="H87">192</cbc:MaximumQuantity>
      <cbc:TradingRestrictions>Not sold to consumers.</cbc:TradingRestrictions>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">520</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode>TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-05-04</cbc:StartDate>
          <cbc:EndDate>2026-10-31</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>6-XB-PL-2026</cbc:ID>
          <cbc:StatusCode>Active</cbc:StatusCode>
        </cac:PriceList>
        <cac:AlternativeCurrencyPrice>
          <cbc:PriceAmount currencyID="XLC">208</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
        </cac:AlternativeCurrencyPrice>
      </cac:Price>
      <cac:DeliveryUnit>
        <cbc:BatchQuantity unitCode="H87">4</cbc:BatchQuantity>
        <cbc:ConsumerUnitQuantity unitCode="H87">1</cbc:ConsumerUnitQuantity>
      </cac:DeliveryUnit>
      <cac:ApplicableTaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
      <cac:Package>
        <cbc:ID>PAL-4</cbc:ID>
        <cbc:Quantity unitCode="H87">4</cbc:Quantity>
        <cbc:PackagingTypeCode>PX</cbc:PackagingTypeCode>
      </cac:Package>
      <cac:AllowanceCharge>
        <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">78</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Full container</cbc:AllowanceChargeReason>
        <cbc:MultiplierFactorNumeric>0.03</cbc:MultiplierFactorNumeric>
        <cbc:Amount currencyID="XBL">15.60</cbc:Amount>
        <cbc:BaseAmount currencyID="XBL">520.00</cbc:BaseAmount>
      </cac:AllowanceCharge>
      <cac:ApplicableDeliveryPeriod>
        <cbc:StartDate>2026-05-11</cbc:StartDate>
        <cbc:EndDate>2026-10-31</cbc:EndDate>
      </cac:ApplicableDeliveryPeriod>
    </cac:RequiredItemLocationQuantity>
    <cac:Item>
      <cbc:Description>The manufacturer's Serra bench, from the distributor's stock.</cbc:Description>
      <cbc:CatalogueIndicator>true</cbc:CatalogueIndicator>
      <cbc:Name>Park bench Serra 180</cbc:Name>
      <cbc:AdditionalInformation>Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
      <cbc:Keyword>park bench</cbc:Keyword>
      <cbc:Keyword>street furniture</cbc:Keyword>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:ModelName>Serra 180</cbc:ModelName>
      <cbc:WarrantyInformation>Five years on the frame against corrosion.</cbc:WarrantyInformation>
      <cac:SellersItemIdentification>
        <cbc:ID>LD-10442</cbc:ID>
        <cbc:ExtendedID>GRY</cbc:ExtendedID>
        <cac:PhysicalAttribute>
          <cbc:AttributeID>Colour</cbc:AttributeID>
          <cbc:PositionCode>FRM</cbc:PositionCode>
          <cbc:DescriptionCode>GRY</cbc:DescriptionCode>
          <cbc:Description>Frame in Ferro grey</cbc:Description>
        </cac:PhysicalAttribute>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
        <cbc:BarcodeSymbologyID>Code128</cbc:BarcodeSymbologyID>
        <cbc:IssuerScopeID>771</cbc:IssuerScopeID>
        <cac:IssuerParty>
          <cbc:IndustryClassificationCode listID="ISIC Rev.4">8299</cbc:IndustryClassificationCode>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105644</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Codana Identification Agency</cbc:Name>
          </cac:PartyName>
          <cac:Language>
            <cbc:ID>qau</cbc:ID>
            <cbc:Name>Urvanian</cbc:Name>
          </cac:Language>
          <cac:PostalAddress>
            <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
            <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
            <cbc:StreetName languageID="qau">Ganluar Ranvua Culsceor</cbc:StreetName>
            <cbc:StreetName languageID="en">Via dei Codici</cbc:StreetName>
            <cbc:BuildingNumber>29</cbc:BuildingNumber>
            <cbc:CityName>Ferrano</cbc:CityName>
            <cbc:PostalZone>4130</cbc:PostalZone>
            <cbc:Region>Province of Ferrano</cbc:Region>
            <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
              <cbc:Name>Urvania</cbc:Name>
            </cac:Country>
          </cac:PostalAddress>
          <cac:PartyTaxScheme>
            <cbc:RegistrationName>Codana Identification Agency SRU</cbc:RegistrationName>
            <cbc:CompanyID>XU007395206</cbc:CompanyID>
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
            <cbc:RegistrationName>Codana Identification Agency SRU</cbc:RegistrationName>
            <cbc:CompanyID>XU-R-105644</cbc:CompanyID>
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
            <cbc:Name>Member services</cbc:Name>
            <cbc:JobTitle>Public service officer</cbc:JobTitle>
            <cbc:Department>Public services</cbc:Department>
            <cbc:Telephone>+999 1 4130 5644</cbc:Telephone>
            <cbc:ElectronicMail>member@codana.example</cbc:ElectronicMail>
            <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
          </cac:Contact>
          <cac:ElectronicAddress>
            <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
            <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105644</cbc:ElectronicAddressID>
          </cac:ElectronicAddress>
        </cac:IssuerParty>
      </cac:StandardItemIdentification>
      <cac:CatalogueItemIdentification>
        <cbc:ID>LD-CAT-26-0124-1</cbc:ID>
      </cac:CatalogueItemIdentification>
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
      <cac:TransactionConditions>
        <cbc:ID>LD-TC-01</cbc:ID>
        <cbc:ActionCode>Trade</cbc:ActionCode>
        <cbc:Description>Sold to trade customers only, per pallet of four benches.</cbc:Description>
        <cac:DocumentReference>
          <cbc:ID>LD-GTC-2026</cbc:ID>
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
      <cac:ManufacturerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:ManufacturerParty>
      <cac:InformationContentProviderParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:InformationContentProviderParty>
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
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
        </cac:ResourceConsumption>
        <cac:ResourceConsumption>
          <cbc:ResourceTypeCode>Hardwood</cbc:ResourceTypeCode>
          <cbc:ConsumptionMeasure unitCode="KGM">22.5</cbc:ConsumptionMeasure>
          <cbc:ResourceOriginDescription>Slats from Upland State, Bayvarra</cbc:ResourceOriginDescription>
          <cac:MeasurementPeriod>
            <cbc:StartDate>2025-01-01</cbc:StartDate>
            <cbc:EndDate>2025-12-31</cbc:EndDate>
          </cac:MeasurementPeriod>
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
  </cac:CatalogueLine>
  <cac:CatalogueLine>
    <cbc:ID>2</cbc:ID>
    <cac:RequiredItemLocationQuantity>
      <cbc:LeadTimeMeasure unitCode="DAY">2</cbc:LeadTimeMeasure>
      <cbc:MinimumQuantity unitCode="H87">1</cbc:MinimumQuantity>
      <cac:ApplicableTerritoryAddress>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:ApplicableTerritoryAddress>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">64</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
        <cbc:PriceTypeCode>TRD</cbc:PriceTypeCode>
        <cbc:PriceType>Trade price</cbc:PriceType>
        <cac:ValidityPeriod>
          <cbc:StartDate>2026-05-04</cbc:StartDate>
          <cbc:EndDate>2026-10-31</cbc:EndDate>
        </cac:ValidityPeriod>
        <cac:PriceList>
          <cbc:ID>6-XB-PL-2026</cbc:ID>
          <cbc:StatusCode>Active</cbc:StatusCode>
        </cac:PriceList>
        <cac:AlternativeCurrencyPrice>
          <cbc:PriceAmount currencyID="XLC">25.6</cbc:PriceAmount>
          <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
        </cac:AlternativeCurrencyPrice>
      </cac:Price>
      <cac:ApplicableTaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ApplicableTaxCategory>
      <cac:DependentPriceReference>
        <cbc:Percent>12.31</cbc:Percent>
        <cac:DependentLineReference>
          <cbc:LineID>1</cbc:LineID>
        </cac:DependentLineReference>
      </cac:DependentPriceReference>
    </cac:RequiredItemLocationQuantity>
    <cac:Item>
      <cbc:Description>Spare side frame for the Serra bench.</cbc:Description>
      <cbc:CatalogueIndicator>true</cbc:CatalogueIndicator>
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
        <cbc:ID schemeID="urn:ubl-examples:world:item">771020000034</cbc:ID>
        <cac:IssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105644</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Codana Identification Agency</cbc:Name>
          </cac:PartyName>
        </cac:IssuerParty>
      </cac:StandardItemIdentification>
      <cac:CatalogueItemIdentification>
        <cbc:ID>LD-CAT-26-0124-2</cbc:ID>
      </cac:CatalogueItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:CommodityCode>7325.99.90</cbc:CommodityCode>
        <cbc:ItemClassificationCode listID="HS">7325.99</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:ManufacturerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:ManufacturerParty>
      <cac:InformationContentProviderParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Valdara Industries</cbc:Name>
        </cac:PartyName>
      </cac:InformationContentProviderParty>
    </cac:Item>
  </cac:CatalogueLine>
</Catalogue>
```
