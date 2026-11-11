# Invoice: Saltmere Engineering to Selanu Telecom

*Example 5 of the flow "Batteries for the island's telecom mast, by air (dangerous goods)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

Goods and carriage to the site; an export, so no sales tax.

[The XML file](05-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **SE-INV-26-0719**  
  The seller's invoice number.
- `UUID` = **40aff29f-0459-5985-901d-8a4a505d1f5d**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-06-04**  
  Issued on despatch.
- `IssueTime` = **17:34:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DueDate` = **2026-07-19**  
  45 days after the issue date, the agreed payment term.
- `InvoiceTypeCode` = **380**  
  UN/EDIFACT 1001 code 380: commercial invoice.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the seller's currency; it has two decimals.
- `PaymentCurrencyCode` = **XBL**  
  Payment is asked in the invoice currency, also from abroad.
- `LineCountNumeric` = **3**  
  The number of invoice lines, as a check on the transfer.
- `DefaultLanguageCode` = **en**  
  The language of the texts that carry no language identifier: English, the working language between the countries; a seller from Urvania or the island also gives its notes in its own language.

### Order Reference

Inside `OrderReference`:

- `ID` = **ST-PO-26-0713**  
  The telecom company's order.

### Despatch Document Reference

Inside `DespatchDocumentReference`:

- `ID` = **SE-DA-26-0718**  
  The despatch advice.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

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
- `Party/Contact/Telephone` = **+999 2 7121 885 685**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/ElectronicMail` = **bids@saltmere.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Saltmere Engineering (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Saltmere Engineering (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Saltmere Engineering (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

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
  The street's name in English, the country's other official language; identity of Selanu Telecom (world/parties.json).
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
- `Party/Contact/Telephone` = **+999 3 727 2407**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Selanu Telecom (world/parties.json).
- `Party/Contact/ElectronicMail` = **business@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Selanu Telecom (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Telecom (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20410685** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Saltmere Engineering**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-07-19**  
  When the transfer must be credited.
- `PaymentChannelCode` = **IBAN**  
  Paid to an account identified in the format of ISO 13616.
- `PaymentRailID` = **TRADE-ACCORD-PAY**  
  The payment system the transfer runs over: the trade accord's link between the countries.
- `InstructionNote` = **Quote RF78SEINV260719**  
  What the payer writes in the transfer.
- `PaymentID` = **RF78SEINV260719**  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits.
- `ChargeBearerCode` = **SHAR**  
  ISO 20022 SHAR: each side pays its own bank's charges.
- `PayeeFinancialAccount/ID` = **XB68BLUM0001885122** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Saltmere Engineering**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XBL**  
  The account is kept in the currency of the bank's country.
- `PayeeFinancialAccount/PaymentNote` = **Invoice SE-INV-26-0719**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **BLUM-001**  
  The branch that keeps the account.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUM**  
  The bank code, the part of every account number that names the bank; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  The bank's head office; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Its building number; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  Its town; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB**  
  The bank's country.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The branch is at the bank's head office.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB**  
  Its country.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XB**  
  The country where the account is kept.

### Payment Terms

Inside `PaymentTerms`:

- `ID` = **XB-STD**  
  The standard terms of Bayvarra.
- `PaymentMeansID` = **1**  
  The payment means these terms apply to: the credit transfer below.
- `Note` = **30 days net; 1.5 % surcharge per month late.**  
  Bayvarran practice: a surcharge per month of late payment, no discount.
- `PenaltySurchargePercent` = **1.5**  
  The surcharge per month of late payment.
- `PenaltyAmount` = **221.55** (currencyID `XBL`)  
  The surcharge for the first month late.
- `PaymentDueDate` = **2026-07-19**  
  The day the amount is due.
- `PenaltyPeriod/StartDate` = **2026-07-20**  
  From the day after the due date.
- `PenaltyPeriod/DurationMeasure` = **1** (unitCode `MON`)  
  Per month.

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

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **14770.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **14770.00** (currencyID `XBL`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **14770.00** (currencyID `XBL`)  
  The total without tax plus the tax.
- `PayableAmount` = **14770.00** (currencyID `XBL`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **6** (unitCode `H87`)  
  The quantity delivered.
- `LineExtensionAmount` = **14400.00** (currencyID `XBL`)  
  6 × 2400.0, rounded to the minor unit of the currency.
- `OrderLineReference/LineID` = **1**  
  The order line this invoice line bills.
- `PricingReference/OriginalItemLocationQuantity/HazardousRiskIndicator` = **true**  
  The batteries are dangerous goods wherever they are delivered.
- `PricingReference/OriginalItemLocationQuantity/DeliveryUnit/BatchQuantity` = **1** (unitCode `C62`)  
  Delivered in single crates.
- `PricingReference/OriginalItemLocationQuantity/DeliveryUnit/HazardousRiskIndicator` = **true**  
  Each crate is dangerous goods: lithium-ion batteries.
- `Item/Description` = **Back-up battery for telecom masts, lithium-ion, 4.8 kWh, in a steel case.**  
  The seller's description; item battery-pack of Saltmere Engineering (world/items.json).
- `Item/Name` = **Lithium-ion battery pack 48 V 100 Ah**  
  The item's short name; item battery-pack of Saltmere Engineering (world/items.json).
- `Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `Item/SellersItemIdentification/ID` = **SE-BAT-48100**  
  The seller's own item number; item battery-pack of Saltmere Engineering (world/items.json).
- `Item/StandardItemIdentification/ID` = **772050000117** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item battery-pack of Saltmere Engineering (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item battery-pack of Saltmere Engineering (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **8507.60** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item battery-pack of Saltmere Engineering (world/items.json).
- `Item/HazardousItem/ID` = **SE-BAT-48100-DG**  
  The seller's dangerous goods record of the item.
- `Item/HazardousItem/PlacardNotation` = **9**  
  The class shown on the placard.
- `Item/HazardousItem/PlacardEndorsement` = **9A**  
  The hazard label on the package.
- `Item/HazardousItem/AdditionalInformation` = **State of charge below 30 %, as the air rules require.**  
  What the shipper adds.
- `Item/HazardousItem/UNDGCode` = **3480** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `Item/HazardousItem/EmergencyProceduresCode` = **F-A, S-I**  
  The emergency schedules for ships (EmS).
- `Item/HazardousItem/MedicalFirstAidGuideCode` = **147**  
  The emergency response guide number.
- `Item/HazardousItem/TunnelRestrictionCode` = **E**  
  The tunnel restriction code for road transport.
- `Item/HazardousItem/ProperShippingName` = **Lithium ion batteries**  
  The proper shipping name.
- `Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
- `Item/HazardousItem/MarkingID` = **UN3480**  
  The UN number marked on each package.
- `Item/HazardousItem/HazardClassID` = **9**  
  The UN hazard class.
- `Item/ClassifiedTaxCategory/ID` = **G**  
  An export from Bayvarra: the state sales tax is not charged (category G).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **XB-EXP**  
  The world's code for the exemption reason (world/countries.json).
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Goods**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Price/PriceAmount` = **2400** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `H87`)  
  The price is per one unit.
- `ID` = **2**  
  The line number.
- `InvoicedQuantity` = **1** (unitCode `SET`)  
  The quantity delivered.
- `LineExtensionAmount` = **180.00** (currencyID `XBL`)  
  1 × 180.0, rounded to the minor unit of the currency.
- `OrderLineReference/LineID` = **2**  
  The order line this invoice line bills.
- `Item/Description` = **Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.**  
  The seller's description; item smoke-detector of Saltmere Engineering (world/items.json).
- `Item/Name` = **Ionisation smoke detector set**  
  The item's short name; item smoke-detector of Saltmere Engineering (world/items.json).
- `Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `Item/SellersItemIdentification/ID` = **SE-SMK-10**  
  The seller's own item number; item smoke-detector of Saltmere Engineering (world/items.json).
- `Item/StandardItemIdentification/ID` = **772050000124** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item smoke-detector of Saltmere Engineering (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item smoke-detector of Saltmere Engineering (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **8531.10** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item smoke-detector of Saltmere Engineering (world/items.json).
- `Item/HazardousItem/ID` = **SE-SMK-10-DG**  
  The seller's dangerous goods record of the item.
- `Item/HazardousItem/PlacardNotation` = **7**  
  The class shown on the placard.
- `Item/HazardousItem/AdditionalInformation` = **Excepted package: no radioactive label, the UN number on the package.**  
  What the shipper adds.
- `Item/HazardousItem/UNDGCode` = **2911** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `Item/HazardousItem/EmergencyProceduresCode` = **None**  
  The emergency schedules for ships (EmS).
- `Item/HazardousItem/MedicalFirstAidGuideCode` = **161**  
  The emergency response guide number.
- `Item/HazardousItem/ProperShippingName` = **Radioactive material, excepted package - instruments or articles**  
  The proper shipping name.
- `Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
- `Item/HazardousItem/MarkingID` = **UN2911**  
  The UN number marked on each package.
- `Item/HazardousItem/HazardClassID` = **7**  
  The UN hazard class.
- `Item/HazardousItem/RadioactiveMaterial/Name` = **Americium-241 sources in smoke detectors**  
  The material.
- `Item/HazardousItem/RadioactiveMaterial/SpecialFormDescription` = **Sealed source, not special form.**  
  Its form.
- `Item/HazardousItem/RadioactiveMaterial/TransportIndexNumeric` = **0**  
  Excepted package: no dose rate to speak of.
- `Item/HazardousItem/RadioactiveMaterial/FissileCriticalitySafetyIndexNumeric` = **0**  
  Not fissile.
- `Item/HazardousItem/RadioactiveMaterial/ApplicableRadioactiveIsotope/Name` = **Americium-241**  
  The isotope.
- `Item/HazardousItem/RadioactiveMaterial/ApplicableRadioactiveIsotope/ActivityLevelMeasure` = **37** (unitCode `2Q`)  
  Per detector.
- `Item/ClassifiedTaxCategory/ID` = **G**  
  An export from Bayvarra: the state sales tax is not charged (category G).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **XB-EXP**  
  The world's code for the exemption reason (world/countries.json).
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Goods**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Price/PriceAmount` = **180** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `SET`)  
  The price is per one unit.
- `ID` = **3**  
  The line number.
- `InvoicedQuantity` = **20** (unitCode `LTR`)  
  The quantity delivered.
- `LineExtensionAmount` = **190.00** (currencyID `XBL`)  
  20 × 9.5, rounded to the minor unit of the currency.
- `OrderLineReference/LineID` = **3**  
  The order line this invoice line bills.
- `Item/Description` = **Remover for the protective coating of circuit boards, in 5-litre cans.**  
  The seller's description; item coating-stripper of Saltmere Engineering (world/items.json).
- `Item/Name` = **Coating stripper for electronics**  
  The item's short name; item coating-stripper of Saltmere Engineering (world/items.json).
- `Item/HazardousRiskIndicator` = **true**  
  The item is dangerous goods.
- `Item/SellersItemIdentification/ID` = **SE-CS-05**  
  The seller's own item number; item coating-stripper of Saltmere Engineering (world/items.json).
- `Item/StandardItemIdentification/ID` = **772050000131** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item coating-stripper of Saltmere Engineering (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item coating-stripper of Saltmere Engineering (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **3814.00** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item coating-stripper of Saltmere Engineering (world/items.json).
- `Item/HazardousItem/ID` = **SE-CS-05-DG**  
  The seller's dangerous goods record of the item.
- `Item/HazardousItem/PlacardNotation` = **8**  
  The class shown on the placard.
- `Item/HazardousItem/PlacardEndorsement` = **8**  
  The hazard label on the package.
- `Item/HazardousItem/AdditionalInformation` = **Packed as the rules require.**  
  What the shipper adds.
- `Item/HazardousItem/UNDGCode` = **2920** (listID `UNCL8273`)  
  The UN number of the UN Model Regulations.
- `Item/HazardousItem/UNPackingGroupCode` = **II**  
  The packing group: medium danger.
- `Item/HazardousItem/UNPackingGroup` = **Medium danger**  
  In words.
- `Item/HazardousItem/EmergencyProceduresCode` = **F-E, S-C**  
  The emergency schedules for ships (EmS).
- `Item/HazardousItem/MedicalFirstAidGuideCode` = **132**  
  The emergency response guide number.
- `Item/HazardousItem/TunnelRestrictionCode` = **D/E**  
  The tunnel restriction code for road transport.
- `Item/HazardousItem/MaritimePollutantCode` = **N**  
  Not a marine pollutant.
- `Item/HazardousItem/TechnicalName` = **ethanolamine, propanol**  
  The technical name, needed with an n.o.s. entry.
- `Item/HazardousItem/ProperShippingName` = **Corrosive liquid, flammable, n.o.s.**  
  The proper shipping name.
- `Item/HazardousItem/HazardousCategoryCode` = **UN**  
  Classified under the UN Model Regulations.
- `Item/HazardousItem/MarkingID` = **UN2920**  
  The UN number marked on each package.
- `Item/HazardousItem/HazardClassID` = **8**  
  The UN hazard class.
- `Item/HazardousItem/SecondaryHazard/ID` = **3**  
  The subsidiary hazard: flammable.
- `Item/HazardousItem/SecondaryHazard/PlacardNotation` = **3**  
  Shown on a second label.
- `Item/HazardousItem/SecondaryHazard/PlacardEndorsement` = **3**  
  The flammable liquid label.
- `Item/HazardousItem/SecondaryHazard/EmergencyProceduresCode` = **F-E**  
  The fire schedule.
- `Item/HazardousItem/SecondaryHazard/Extension` = **Subsidiary risk 3**  
  In words.
- `Item/HazardousItem/FlashpointTemperature/AttributeID` = **Flashpoint**  
  Closed cup.
- `Item/HazardousItem/FlashpointTemperature/Measure` = **28** (unitCode `CEL`)  
  The flashpoint.
- `Item/ClassifiedTaxCategory/ID` = **G**  
  An export from Bayvarra: the state sales tax is not charged (category G).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **XB-EXP**  
  The world's code for the exemption reason (world/countries.json).
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Goods**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Price/PriceAmount` = **9.5** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `LTR`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:mast</cbc:ProfileID>
  <cbc:ProfileExecutionID>MAST-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>SE-INV-26-0719</cbc:ID>
  <cbc:UUID>40aff29f-0459-5985-901d-8a4a505d1f5d</cbc:UUID>
  <cbc:IssueDate>2026-06-04</cbc:IssueDate>
  <cbc:IssueTime>17:34:00</cbc:IssueTime>
  <cbc:DueDate>2026-07-19</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cbc:PaymentCurrencyCode>XBL</cbc:PaymentCurrencyCode>
  <cbc:LineCountNumeric>3</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode>en</cbc:DefaultLanguageCode>
  <cac:OrderReference>
    <cbc:ID>ST-PO-26-0713</cbc:ID>
  </cac:OrderReference>
  <cac:DespatchDocumentReference>
    <cbc:ID>SE-DA-26-0718</cbc:ID>
  </cac:DespatchDocumentReference>
  <cac:AccountingSupplierParty>
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
        <cbc:Telephone>+999 2 7121 885 685</cbc:Telephone>
        <cbc:ElectronicMail>bids@saltmere.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410685</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
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
        <cbc:Telephone>+999 3 727 2407</cbc:Telephone>
        <cbc:ElectronicMail>business@selanutelecom.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Saltmere Engineering</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-07-19</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>TRADE-ACCORD-PAY</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF78SEINV260719</cbc:InstructionNote>
    <cbc:PaymentID>RF78SEINV260719</cbc:PaymentID>
    <cbc:ChargeBearerCode>SHAR</cbc:ChargeBearerCode>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XB68BLUM0001885122</cbc:ID>
      <cbc:Name>Saltmere Engineering</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice SE-INV-26-0719</cbc:PaymentNote>
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
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:PaymentTerms>
    <cbc:ID>XB-STD</cbc:ID>
    <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
    <cbc:Note>30 days net; 1.5 % surcharge per month late.</cbc:Note>
    <cbc:PenaltySurchargePercent>1.5</cbc:PenaltySurchargePercent>
    <cbc:PenaltyAmount currencyID="XBL">221.55</cbc:PenaltyAmount>
    <cbc:PaymentDueDate>2026-07-19</cbc:PaymentDueDate>
    <cac:PenaltyPeriod>
      <cbc:StartDate>2026-07-20</cbc:StartDate>
      <cbc:DurationMeasure unitCode="MON">1</cbc:DurationMeasure>
    </cac:PenaltyPeriod>
  </cac:PaymentTerms>
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
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">14770.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">14770.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">14770.00</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XBL">14770.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="H87">6</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">14400.00</cbc:LineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>1</cbc:LineID>
    </cac:OrderLineReference>
    <cac:PricingReference>
      <cac:OriginalItemLocationQuantity>
        <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        <cac:DeliveryUnit>
          <cbc:BatchQuantity unitCode="C62">1</cbc:BatchQuantity>
          <cbc:HazardousRiskIndicator>true</cbc:HazardousRiskIndicator>
        </cac:DeliveryUnit>
      </cac:OriginalItemLocationQuantity>
    </cac:PricingReference>
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
      <cac:ClassifiedTaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode>Goods</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">2400</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:InvoicedQuantity unitCode="SET">1</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">180.00</cbc:LineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>2</cbc:LineID>
    </cac:OrderLineReference>
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
      <cac:ClassifiedTaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode>Goods</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">180</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="SET">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>3</cbc:ID>
    <cbc:InvoicedQuantity unitCode="LTR">20</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">190.00</cbc:LineExtensionAmount>
    <cac:OrderLineReference>
      <cbc:LineID>3</cbc:LineID>
    </cac:OrderLineReference>
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
      <cac:ClassifiedTaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-EXP</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode>Goods</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">9.5</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="LTR">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
