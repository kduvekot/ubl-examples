# Order: Selanu Telecom to Saltmere Engineering

*Example 1 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Order in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-ORDER-SCHEMA)*

The telecom company orders back-up power and safety equipment for its mast. Carriage paid to its site: the seller arranges the dangerous goods transport.

[The XML file](01-Order.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:mast**  
  The business process the document belongs to: the flow "Batteries for the island's telecom mast, by air (dangerous goods)".
- `ProfileExecutionID` = **MAST-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **ST-PO-26-0713**  
  The buyer's order number.
- `UUID` = **b63839e1-7b35-5e81-a17d-ef60734d2fe6**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-01**  
  The telecom company orders before the storm season.
- `IssueTime` = **08:15:00**  
  The time the sender's system issued the document, in the sender's local time.
- `OrderTypeCode` = **220**  
  UN/EDIFACT 1001 code 220: order.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the seller's currency, in which the seller's prices are; it has two decimals.
- `LineCountNumeric` = **3**  
  The number of order lines.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/WebsiteURI` = **https://www.selanutelecom.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Selanu Telecom (world/parties.json).
- `Party/IndustryClassificationCode` = **6110** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Selanu Telecom (world/parties.json).
- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Party/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Party/PostalAddress/StreetName` = **Kitata Vekase Natii** (languageID `qal`)  
  The street's name in Lisavan: Lisavu is officially bilingual, and street names are given in both languages (world/countries.json); identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/StreetName` = **Mast Hill Road** (languageID `en`)  
  The street's name in English, the island's other official language; identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address. identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Selanu Telecom Ltd**  
  The name under which the party is registered, with its legal form; identity of Selanu Telecom (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42407**  
  Number in the Island companies register; identity of Selanu Telecom (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Selanu Telecom (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Selanu Telecom (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Selanu**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XL**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XL:ICR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Island companies register**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XL**  
  The register covers the whole country.
- `Party/Contact/Name` = **Business accounts**  
  The desk that handles this document; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 3000 2407**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/ElectronicMail` = **business@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Telecom (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Telecom (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/IndustryClassificationCode` = **4290** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Saltmere Engineering (world/parties.json).
- `Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Saltmere Engineering**  
  The trading name; identity of Saltmere Engineering (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `Party/PostalAddress/StreetName` = **Foundry Road**  
  Street of the postal address. identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **13**  
  Building number of the postal address. identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71218**  
  Postal code in Bayvarra's format (5 digits). identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Saltmere Engineering (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered for state sales tax; identity of Saltmere Engineering (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **UL-1232055**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Saltmere Engineering (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Upland State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Saltmere Engineering**  
  The name under which the party is registered, with its legal form; identity of Saltmere Engineering (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410685**  
  Number in the Federal business register of Bayvarra; identity of Saltmere Engineering (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Marrowdale**  
  The registered office, as entered in the register.
- `Party/PartyLegalEntity/RegistrationAddress/Country/IdentificationCode` = **XB**  
  The country of registration.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/ID` = **XB:FBR**  
  The identifier of the register in the world (world/countries.json).
- `Party/PartyLegalEntity/CorporateRegistrationScheme/Name` = **Federal business register of Bayvarra**  
  The register the company is entered in.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/CorporateRegistrationTypeCode` = **Commercial**  
  A register of businesses, not a register of charities or associations.
- `Party/PartyLegalEntity/CorporateRegistrationScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The register covers the whole country.
- `Party/Contact/Name` = **Bids office**  
  The desk that handles this document; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/JobTitle` = **Procurement officer**  
  The job of the person who answers at the desk; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/Department` = **Procurement**  
  The department the desk belongs to; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7121 0685**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/ElectronicMail` = **bids@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Delivery

Inside `Delivery`:

- `DeliveryParty/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `DeliveryParty/PartyName/Name` = **Selanu Telecom**  
  The same party as at BuyerCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Delivery Terms

Inside `DeliveryTerms`:

- `ID` = **CPT** (schemeID `INCOTERMS`)  
  Carriage paid to the telecom company's site: the seller arranges the dangerous goods transport.
- `DeliveryLocation/Description` = **Selanu Telecom, mast site**  
  Where the delivery terms place the handover of the goods.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **14770.00** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G**  
  An export from Bayvarra: the state sales tax is not charged (category G).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **XB-EXP**  
  The world's code for the exemption reason (world/countries.json).
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Anticipated Monetary Total

Inside `AnticipatedMonetaryTotal`:

- `LineExtensionAmount` = **14770.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `PayableAmount` = **14770.00** (currencyID `XBL`)  
  What the buyer expects to pay, tax included.

### Order Line

Inside `OrderLine`:

- `LineItem/ID` = **1**  
  The line number.
- `LineItem/Quantity` = **6** (unitCode `H87`)  
  Six packs: four hours of back-up power for the mast.
- `LineItem/LineExtensionAmount` = **14400.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **2400** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `H87`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Back-up battery for telecom masts, lithium-ion, 4.8 kWh, in a steel case.**  
  The seller's description; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/Name` = **Lithium-ion battery pack 48 V 100 Ah**  
  The item's short name; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-BAT-48100**  
  The seller's own item number; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/StandardItemIdentification/ID` = **772050000117** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **8507.60** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item battery-pack of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousItem/ID` = **SE-BAT-48100-DG**  
  The seller's dangerous goods record of the item.
- `LineItem/Item/HazardousItem/PlacardNotation` = **9**  
  The class shown on the placard.
- `LineItem/Item/HazardousItem/PlacardEndorsement` = **9A**  
  The hazard label on the package.
- `LineItem/Item/HazardousItem/AdditionalInformation` = **State of charge below 30 %, as the air rules require.**  
  What the shipper adds.
- `LineItem/Item/HazardousItem/UNDGCode` = **3480** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `LineItem/Item/HazardousItem/EmergencyProceduresCode` = **F-A, S-I**  
  The emergency schedules for ships (EmS).
- `LineItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **147**  
  The emergency response guide number.
- `LineItem/Item/HazardousItem/TunnelRestrictionCode` = **E**  
  The tunnel restriction code for road transport.
- `LineItem/Item/HazardousItem/ProperShippingName` = **Lithium ion batteries**  
  The proper shipping name.
- `LineItem/Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
- `LineItem/Item/HazardousItem/MarkingID` = **UN3480**  
  The UN number marked on each package.
- `LineItem/Item/HazardousItem/HazardClassID` = **9**  
  The UN hazard class.
- `LineItem/ID` = **2**  
  The line number.
- `LineItem/Quantity` = **1** (unitCode `SET`)  
  One set of ten for the equipment room.
- `LineItem/LineExtensionAmount` = **180.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **180** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `SET`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.**  
  The seller's description; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/Name` = **Ionisation smoke detector set**  
  The item's short name; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-SMK-10**  
  The seller's own item number; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/StandardItemIdentification/ID` = **772050000124** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **8531.10** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item smoke-detector of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousItem/ID` = **SE-SMK-10-DG**  
  The seller's dangerous goods record of the item.
- `LineItem/Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the placard.
- `LineItem/Item/HazardousItem/AdditionalInformation` = **Excepted package: no radioactive label, the UN number on the package.**  
  What the shipper adds.
- `LineItem/Item/HazardousItem/UNDGCode` = **2911** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `LineItem/Item/HazardousItem/EmergencyProceduresCode` = **None**  
  The emergency schedules for ships (EmS).
- `LineItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **161**  
  The emergency response guide number.
- `LineItem/Item/HazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  The proper shipping name.
- `LineItem/Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
- `LineItem/Item/HazardousItem/MarkingID` = **UN2911**  
  The UN number marked on each package.
- `LineItem/Item/HazardousItem/HazardClassID` = **7**  
  The UN hazard class.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/Name` = **Americium-241 sources in smoke detectors**  
  The material.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Sealed source, not special form.**  
  Its form.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **0**  
  Excepted package: no dose rate to speak of.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/FissileCriticalitySafetyIndexNumeric` = **0**  
  Not fissile.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/ApplicableRadioactiveIsotope/Name` = **Americium-241**  
  The isotope.
- `LineItem/Item/HazardousItem/RadioactiveMaterial/ApplicableRadioactiveIsotope/ActivityLevelMeasure` = **37** (unitCode `2Q`)  
  Per detector.
- `LineItem/ID` = **3**  
  The line number.
- `LineItem/Quantity` = **20** (unitCode `LTR`)  
  Four cans of five litres for the circuit boards.
- `LineItem/LineExtensionAmount` = **190.00** (currencyID `XBL`)  
  Quantity times price, rounded to the minor unit.
- `LineItem/Price/PriceAmount` = **9.5** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `LineItem/Price/BaseQuantity` = **1** (unitCode `LTR`)  
  The price is per one unit.
- `LineItem/Item/Description` = **Remover for the protective coating of circuit boards, in 5-litre cans.**  
  The seller's description; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/Name` = **Coating stripper for electronics**  
  The item's short name; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `LineItem/Item/SellersItemIdentification/ID` = **SE-CS-05**  
  The seller's own item number; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/StandardItemIdentification/ID` = **772050000131** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/CommodityClassification/ItemClassificationCode` = **3814.00** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item coating-stripper of Saltmere Engineering (world/items.json).
- `LineItem/Item/HazardousItem/ID` = **SE-CS-05-DG**  
  The seller's dangerous goods record of the item.
- `LineItem/Item/HazardousItem/PlacardNotation` = **8**  
  The class shown on the placard.
- `LineItem/Item/HazardousItem/PlacardEndorsement` = **8**  
  The hazard label on the package.
- `LineItem/Item/HazardousItem/AdditionalInformation` = **Packed as the rules require.**  
  What the shipper adds.
- `LineItem/Item/HazardousItem/UNDGCode` = **2920** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `LineItem/Item/HazardousItem/UNPackingGroupCode` = **II**  
  The packing group: medium danger.
- `LineItem/Item/HazardousItem/UNPackingGroup` = **Medium danger**  
  In words.
- `LineItem/Item/HazardousItem/EmergencyProceduresCode` = **F-E, S-C**  
  The emergency schedules for ships (EmS).
- `LineItem/Item/HazardousItem/MedicalFirstAidGuideCode` = **132**  
  The emergency response guide number.
- `LineItem/Item/HazardousItem/TunnelRestrictionCode` = **D/E**  
  The tunnel restriction code for road transport.
- `LineItem/Item/HazardousItem/MaritimePollutantCode` = **N**  
  Not a marine pollutant.
- `LineItem/Item/HazardousItem/TechnicalName` = **ethanolamine, propanol**  
  The technical name, needed with an n.o.s. entry.
- `LineItem/Item/HazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  The proper shipping name.
- `LineItem/Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
- `LineItem/Item/HazardousItem/MarkingID` = **UN2920**  
  The UN number marked on each package.
- `LineItem/Item/HazardousItem/HazardClassID` = **8**  
  The UN hazard class.
- `LineItem/Item/HazardousItem/SecondaryHazard/ID` = **3**  
  The subsidiary hazard: flammable.
- `LineItem/Item/HazardousItem/SecondaryHazard/PlacardNotation` = **3**  
  Shown on a second label.
- `LineItem/Item/HazardousItem/SecondaryHazard/PlacardEndorsement` = **3**  
  The flammable liquid label.
- `LineItem/Item/HazardousItem/SecondaryHazard/EmergencyProceduresCode` = **F-E**  
  The fire schedule.
- `LineItem/Item/HazardousItem/SecondaryHazard/Extension` = **Subsidiary risk 3**  
  In words.
- `LineItem/Item/HazardousItem/FlashpointTemperature/AttributeID` = **Flashpoint**  
  Closed cup.
- `LineItem/Item/HazardousItem/FlashpointTemperature/Measure` = **28** (unitCode `CEL`)  
  The flashpoint.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Order xmlns="urn:oasis:names:specification:ubl:schema:xsd:Order-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:mast</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>ST-PO-26-0713</cbc:ID>
  <cbc:UUID>b63839e1-7b35-5e81-a17d-ef60734d2fe6</cbc:UUID>
  <cbc:IssueDate>2026-06-01</cbc:IssueDate>
  <cbc:IssueTime>08:15:00</cbc:IssueTime>
  <cbc:OrderTypeCode>220</cbc:OrderTypeCode>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.selanutelecom.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">6110</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>qal</cbc:ID>
        <cbc:Name>Lisavan</cbc:Name>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XL</cbc:AddressFormatCode>
        <cbc:StreetName languageID="qal">Kitata Vekase Natii</cbc:StreetName>
        <cbc:StreetName languageID="en">Mast Hill Road</cbc:StreetName>
        <cbc:BuildingNumber>58</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
          <cbc:Name>Lisavu</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Selanu Telecom Ltd</cbc:RegistrationName>
        <cbc:CompanyID>IC42407</cbc:CompanyID>
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
        <cbc:Name>Business accounts</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 3 3000 2407</cbc:Telephone>
        <cbc:ElectronicMail>business@selanutelecom.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">4290</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Saltmere Engineering</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Foundry Road</cbc:StreetName>
        <cbc:BuildingNumber>13</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71218</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
        <cbc:CompanyID>UL-1232055</cbc:CompanyID>
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
        <cbc:RegistrationName>Saltmere Engineering</cbc:RegistrationName>
        <cbc:CompanyID>20410685</cbc:CompanyID>
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
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
        <cbc:Name>Bids office</cbc:Name>
        <cbc:JobTitle>Procurement officer</cbc:JobTitle>
        <cbc:Department>Procurement</cbc:Department>
        <cbc:Telephone>+999 2 7121 0685</cbc:Telephone>
        <cbc:ElectronicMail>bids@saltmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:Delivery>
    <cac:DeliveryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
    </cac:DeliveryParty>
  </cac:Delivery>
  <cac:DeliveryTerms>
    <cbc:ID schemeID="INCOTERMS">CPT</cbc:ID>
    <cac:DeliveryLocation>
      <cbc:Description>Selanu Telecom, mast site</cbc:Description>
    </cac:DeliveryLocation>
  </cac:DeliveryTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">14770.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:AnticipatedMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">14770.00</cbc:LineExtensionAmount>
    <cbc:PayableAmount currencyID="XBL">14770.00</cbc:PayableAmount>
  </cac:AnticipatedMonetaryTotal>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>1</cbc:ID>
      <cbc:Quantity unitCode="H87">6</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">14400.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">2400</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Back-up battery for telecom masts, lithium-ion, 4.8 kWh, in a steel case.</cbc:Description>
        <cbc:Name>Lithium-ion battery pack 48 V 100 Ah</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-BAT-48100</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">772050000117</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">8507.60</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-BAT-48100-DG</cbc:ID>
          <cbc:PlacardNotation>9</cbc:PlacardNotation>
          <cbc:PlacardEndorsement>9A</cbc:PlacardEndorsement>
          <cbc:AdditionalInformation>State of charge below 30 %, as the air rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UNCL8273">3480</cbc:UNDGCode>
          <cbc:EmergencyProceduresCode>F-A, S-I</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode>147</cbc:MedicalFirstAidGuideCode>
          <cbc:TunnelRestrictionCode>E</cbc:TunnelRestrictionCode>
          <cbc:ProperShippingName>Lithium ion batteries</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode>UN</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN3480</cbc:MarkingID>
          <cbc:HazardClassID>9</cbc:HazardClassID>
        </cac:HazardousItem>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>2</cbc:ID>
      <cbc:Quantity unitCode="SET">1</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">180.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">180</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="SET">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.</cbc:Description>
        <cbc:Name>Ionisation smoke detector set</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-SMK-10</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">772050000124</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">8531.10</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-SMK-10-DG</cbc:ID>
          <cbc:PlacardNotation>7</cbc:PlacardNotation>
          <cbc:AdditionalInformation>Excepted package: no radioactive label, the UN number on the package.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UNCL8273">2911</cbc:UNDGCode>
          <cbc:EmergencyProceduresCode>None</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode>161</cbc:MedicalFirstAidGuideCode>
          <cbc:ProperShippingName>Radioactive material, excepted package - instruments or articles</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode>UN</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2911</cbc:MarkingID>
          <cbc:HazardClassID>7</cbc:HazardClassID>
          <cac:RadioactiveMaterial>
            <cbc:Name>Americium-241 sources in smoke detectors</cbc:Name>
            <cbc:SpecialFormDescription>Sealed source, not special form.</cbc:SpecialFormDescription>
            <cbc:TransportIndexNumeric>0</cbc:TransportIndexNumeric>
            <cbc:FissileCriticalitySafetyIndexNumeric>0</cbc:FissileCriticalitySafetyIndexNumeric>
            <cac:ApplicableRadioactiveIsotope>
              <cbc:Name>Americium-241</cbc:Name>
              <cbc:ActivityLevelMeasure unitCode="2Q">37</cbc:ActivityLevelMeasure>
            </cac:ApplicableRadioactiveIsotope>
          </cac:RadioactiveMaterial>
        </cac:HazardousItem>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
  <cac:OrderLine>
    <cac:LineItem>
      <cbc:ID>3</cbc:ID>
      <cbc:Quantity unitCode="LTR">20</cbc:Quantity>
      <cbc:LineExtensionAmount currencyID="XBL">190.00</cbc:LineExtensionAmount>
      <cac:Price>
        <cbc:PriceAmount currencyID="XBL">9.5</cbc:PriceAmount>
        <cbc:BaseQuantity unitCode="LTR">1</cbc:BaseQuantity>
      </cac:Price>
      <cac:Item>
        <cbc:Description>Remover for the protective coating of circuit boards, in 5-litre cans.</cbc:Description>
        <cbc:Name>Coating stripper for electronics</cbc:Name>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:SellersItemIdentification>
          <cbc:ID>SE-CS-05</cbc:ID>
        </cac:SellersItemIdentification>
        <cac:StandardItemIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:item">772050000131</cbc:ID>
        </cac:StandardItemIdentification>
        <cac:OriginCountry>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:OriginCountry>
        <cac:CommodityClassification>
          <cbc:ItemClassificationCode listID="HS">3814.00</cbc:ItemClassificationCode>
        </cac:CommodityClassification>
        <cac:HazardousItem>
          <cbc:ID>SE-CS-05-DG</cbc:ID>
          <cbc:PlacardNotation>8</cbc:PlacardNotation>
          <cbc:PlacardEndorsement>8</cbc:PlacardEndorsement>
          <cbc:AdditionalInformation>Packed as the rules require.</cbc:AdditionalInformation>
          <cbc:UNDGCode listID="UNCL8273">2920</cbc:UNDGCode>
          <cbc:UNPackingGroupCode>II</cbc:UNPackingGroupCode>
          <cbc:UNPackingGroup>Medium danger</cbc:UNPackingGroup>
          <cbc:EmergencyProceduresCode>F-E, S-C</cbc:EmergencyProceduresCode>
          <cbc:MedicalFirstAidGuideCode>132</cbc:MedicalFirstAidGuideCode>
          <cbc:TunnelRestrictionCode>D/E</cbc:TunnelRestrictionCode>
          <cbc:MaritimePollutantCode>N</cbc:MaritimePollutantCode>
          <cbc:TechnicalName>ethanolamine, propanol</cbc:TechnicalName>
          <cbc:ProperShippingName>Corrosive liquid, flammable, n.o.s.</cbc:ProperShippingName>
          <cbc:HazardousCategoryCode>UN</cbc:HazardousCategoryCode>
          <cbc:MarkingID>UN2920</cbc:MarkingID>
          <cbc:HazardClassID>8</cbc:HazardClassID>
          <cac:SecondaryHazard>
            <cbc:ID>3</cbc:ID>
            <cbc:PlacardNotation>3</cbc:PlacardNotation>
            <cbc:PlacardEndorsement>3</cbc:PlacardEndorsement>
            <cbc:EmergencyProceduresCode>F-E</cbc:EmergencyProceduresCode>
            <cbc:Extension>Subsidiary risk 3</cbc:Extension>
          </cac:SecondaryHazard>
          <cac:FlashpointTemperature>
            <cbc:AttributeID>Flashpoint</cbc:AttributeID>
            <cbc:Measure unitCode="CEL">28</cbc:Measure>
          </cac:FlashpointTemperature>
        </cac:HazardousItem>
      </cac:Item>
    </cac:LineItem>
  </cac:OrderLine>
</Order>
```
