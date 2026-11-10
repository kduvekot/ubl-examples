# Invoice: Marrowdale Sawmill to Valdara Industries

*Example 8 of the flow "Wood: slats for the benches and timber for furniture (Bayvarra → Urvania, and at home)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

Slats and delivery. An export from Bayvarra: no sales tax, with the exemption stated.

[The XML file](08-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:wood**  
  The business process the document belongs to: the flow "Wood: slats for the benches and timber for furniture (Bayvarra → Urvania, and at home)".
- `ProfileExecutionID` = **WOOD-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **MS-INV-26-0635**  
  The seller's invoice number.
- `UUID` = **ae3fabe1-02f6-56f3-a403-bd58b53f0ab9**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-02-26**  
  Issued when the slats leave.
- `DueDate` = **2026-03-28**  
  30 days after the issue date, the agreed payment term.
- `InvoiceTypeCode` = **380**  
  UN/EDIFACT 1001 code 380: commercial invoice.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the seller's currency; it has two decimals.
- `AccountingCostCode` = **3100**  
  The buyer's cost centre, quoted in its order, so the invoice is booked without asking.
- `AccountingCost` = **Raw materials and parts**  
  The cost centre in words.
- `LineCountNumeric` = **1**  
  The number of invoice lines, as a check on the transfer.
- `DefaultLanguageCode` = **en**  
  The language the texts of the invoice are in: the seller's country's language.

### Order Reference

Inside `OrderReference`:

- `ID` = **VI-PO-26-0627**  
  The manufacturer's order.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.marrowdalesawmill.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Marrowdale Sawmill (world/parties.json).
- `Party/IndustryClassificationCode` = **1610** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Marrowdale Sawmill (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XB-TR-412329** (schemeID `urn:ubl-examples:world:XB:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XB-TR- and 6 digits); identity of Marrowdale Sawmill (world/parties.json).
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The trading name; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json): BuildingNumber StreetName / CityName CountrySubentity PostalZone.
- `Party/PostalAddress/StreetName` = **Timber Lane**  
  Street of the postal address. identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **7**  
  Building number of the postal address. identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71202**  
  Postal code in Bayvarra's format (5 digits). identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra. identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **UL**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Marrowdale Sawmill (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Marrowdale Sawmill Ltd**  
  The name under which the party is registered for state sales tax; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **UL-1236987**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Marrowdale Sawmill (world/parties.json).
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
- `Party/PartyLegalEntity/RegistrationName` = **Marrowdale Sawmill Ltd**  
  The name under which the party is registered, with its legal form; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412329**  
  Number in the Federal business register of Bayvarra; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Marrowdale Sawmill (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Marrowdale Sawmill (world/parties.json).
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
- `Party/Contact/Name` = **Sales office**  
  The desk that handles this document; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 7120 2329**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/ElectronicMail` = **sales@marrowdalesawmill.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Marrowdale Sawmill (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Marrowdale Sawmill (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412329** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Marrowdale Sawmill (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

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
- `Party/ServiceProviderParty/ServiceType` = **Warehousing and despatch**  
  What the service provider does for the party; identity of Valdara Industries (world/parties.json).
- `Party/ServiceProviderParty/Party/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ServiceProviderParty/Party/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Valdara Industries (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Valdara Industries**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412329** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Marrowdale Sawmill**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-03-28**  
  When the transfer must be credited.
- `PaymentChannelCode` = **IBAN**  
  Paid to an account identified in the format of ISO 13616.
- `PaymentRailID` = **TRADE-ACCORD-PAY**  
  The payment system the transfer runs over: the trade accord's link between the countries.
- `InstructionNote` = **Quote RF83MSINV260635**  
  What the payer writes in the transfer.
- `PaymentID` = **RF83MSINV260635**  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits.
- `ChargeBearerCode` = **SHAR**  
  ISO 20022 SHAR: each side pays its own bank's charges.
- `PayeeFinancialAccount/ID` = **XB77BLUM0004398618** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Marrowdale Sawmill Ltd**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XBL**  
  The account is kept in the currency of the bank's country.
- `PayeeFinancialAccount/PaymentNote` = **Invoice MS-INV-26-0635**  
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
- `PenaltyAmount` = **518.40** (currencyID `XBL`)  
  The surcharge for the first month late.
- `PaymentTermsDetailsURI` = **https://www.marrowdalesawmill.example/terms**  
  The seller's general terms of payment.
- `PaymentDueDate` = **2026-03-28**  
  The day the amount is due.
- `PenaltyPeriod/StartDate` = **2026-03-29**  
  From the day after the due date.
- `PenaltyPeriod/DurationMeasure` = **1** (unitCode `MON`)  
  Per month.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **34560.00** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **G**  
  An export from Bayvarra: the state sales tax is not charged (category G).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **34560.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **34560.00** (currencyID `XBL`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **34560.00** (currencyID `XBL`)  
  The total without tax plus the tax.
- `PayableAmount` = **34560.00** (currencyID `XBL`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **4800** (unitCode `H87`)  
  The slats despatched.
- `LineExtensionAmount` = **34560.00** (currencyID `XBL`)  
  4800 × 7.2, rounded to the minor unit of the currency.
- `Item/Description` = **Sawn hardwood slat, 1800 × 95 × 38 mm, planed, kiln dried.**  
  The seller's description; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/PackQuantity` = **1** (unitCode `H87`)  
  One pack of this item.
- `Item/PackSizeNumeric` = **50**  
  The units in one pack: 50 in a bundle; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/Name` = **Hardwood bench slat 1800**  
  The item's short name; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/SellersItemIdentification/ID` = **MS-SL-1800**  
  The seller's own item number; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/SellersItemIdentification/MeasurementDimension/AttributeID` = **Length**  
  The seller numbers its slats by length: this number is for one length.
- `Item/SellersItemIdentification/MeasurementDimension/Measure` = **1800** (unitCode `MMT`)  
  The length the number stands for.
- `Item/StandardItemIdentification/ID` = **772010000058** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/AdditionalItemIdentification/ID` = **772010000065** (schemeID `urn:ubl-examples:world:item`)  
  The world item number of the pack of 50, the unit the item is traded in; the item number above is for one piece.
- `Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **4407.99** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **G**  
  An export from Bayvarra: the state sales tax is not charged (category G).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Export outside Bayvarra**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Item/AdditionalItemProperty/ID` = **MC**  
  The maker's identifier for the property.
- `Item/AdditionalItemProperty/Name` = **Moisture content**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/NameCode` = **MC**  
  The property's name as a code, as the property standard lists it.
- `Item/AdditionalItemProperty/TestMethod` = **Oven-dry method on samples from each kiln charge**  
  How the value is tested.
- `Item/AdditionalItemProperty/ValueQuantity` = **12** (unitCode `P1`)  
  Its measured value; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/AdditionalItemProperty/ValueQualifier` = **Average of the kiln charge**  
  What the value stands for.
- `Item/AdditionalItemProperty/ImportanceCode` = **Mandatory**  
  How much the property matters in describing the item.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ID` = **QUA**  
  The group of properties this one belongs to.
- `Item/AdditionalItemProperty/ItemPropertyGroup/Name` = **Wood quality**  
  The group's name.
- `Item/AdditionalItemProperty/ItemPropertyGroup/ImportanceCode` = **Mandatory**  
  How much the group matters.
- `Item/AdditionalItemProperty/ItemPropertyRange/MinimumValue` = **10**  
  The lowest value accepted.
- `Item/AdditionalItemProperty/ItemPropertyRange/MaximumValue` = **14**  
  The highest value accepted.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/ID` = **UR-WD-0012**  
  The property's number in the property standard of the identification agency.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerScopeID` = **Codana timber properties**  
  The part of the agency's standards it is taken from.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyIdentification/ID` = **XU-R-105644** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/AdditionalItemProperty/StandardPropertyIdentification/IssuerParty/PartyName/Name` = **Codana Identification Agency**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/AdditionalItemProperty/SubItemProperty/Name` = **Moisture at the core**  
  Measured at the centre of the slat.
- `Item/AdditionalItemProperty/SubItemProperty/ValueQuantity` = **13** (unitCode `P1`)  
  Its measured value; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Thickness tolerance**  
  How far a slat may be off its thickness.
- `Item/AdditionalItemProperty/RangeDimension/AttributeID` = **Thickness**  
  The dimension the tolerance is for.
- `Item/AdditionalItemProperty/RangeDimension/Measure` = **38** (unitCode `MMT`)  
  Its nominal size.
- `Item/AdditionalItemProperty/RangeDimension/MinimumMeasure` = **37.5** (unitCode `MMT`)  
  The smallest size accepted.
- `Item/AdditionalItemProperty/RangeDimension/MaximumMeasure` = **38.5** (unitCode `MMT`)  
  The largest size accepted.
- `Item/AdditionalItemProperty/Name` = **Surface**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **Planed on four sides**  
  Its value; item slat-1800 of Marrowdale Sawmill (world/items.json).
- `Item/AdditionalItemProperty/UsabilityPeriod/DurationMeasure` = **12** (unitCode `MON`)  
  Oiled within twelve months of planing, before the surface greys
- `Item/Certificate/ID` = **XB-FOR-2025-118**  
  The number of the certificate.
- `Item/Certificate/CertificateTypeCode` = **Sustainableforestry**  
  The kind of certificate, as a code.
- `Item/Certificate/CertificateType` = **Sustainable forestry**  
  The kind of certificate, in words.
- `Item/Certificate/CertificateReferenceID` = **XB-FOR-REG-0118**  
  The certificate's number in the issuer's public register.
- `Item/Certificate/ApplicableCategoryCode` = **HW**  
  The category of goods the certificate covers.
- `Item/Certificate/ApplicableCategory` = **Hardwood sawn timber**  
  The category in words.
- `Item/Certificate/CertificateURI` = **https://forestry.xb.example/certificates/XB-FOR-2025-118**  
  Where the certificate can be checked.
- `Item/Certificate/Remarks` = **The timber comes from forests in Upland State managed for regrowth.**  
  What the certificate states about the goods.
- `Item/Certificate/CertificateValidityPeriod/EndDate` = **2027-12-31**  
  The certificate is valid until then.
- `Item/Certificate/DocumentReference/ID` = **XB-FOR-AUD-2025-118**  
  The audit report the certificate is based on.
- `Item/Dimension/AttributeID` = **Length**  
  Which dimension.
- `Item/Dimension/Measure` = **1800** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/AttributeID` = **Width**  
  Which dimension.
- `Item/Dimension/Measure` = **95** (unitCode `MMT`)  
  Its size.
- `Item/Dimension/AttributeID` = **Thickness**  
  Which dimension.
- `Item/Dimension/Measure` = **38** (unitCode `MMT`)  
  Its size.
- `Price/PriceAmount` = **7.2** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `H87`)  
  The price is per one unit.
- `Price/OrderableUnitFactorRate` = **50**  
  The item is priced per piece and ordered in packs: one pack holds 50 pieces.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:wood</cbc:ProfileID>
  <cbc:ProfileExecutionID>WOOD-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>MS-INV-26-0635</cbc:ID>
  <cbc:UUID>ae3fabe1-02f6-56f3-a403-bd58b53f0ab9</cbc:UUID>
  <cbc:IssueDate>2026-02-26</cbc:IssueDate>
  <cbc:DueDate>2026-03-28</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>3100</cbc:AccountingCostCode>
  <cbc:AccountingCost>Raw materials and parts</cbc:AccountingCost>
  <cbc:LineCountNumeric>1</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode>en</cbc:DefaultLanguageCode>
  <cac:OrderReference>
    <cbc:ID>VI-PO-26-0627</cbc:ID>
  </cac:OrderReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.marrowdalesawmill.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">1610</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:AdditionalPartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:customs-trader">XB-TR-412329</cbc:ID>
      </cac:AdditionalPartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Timber Lane</cbc:StreetName>
        <cbc:BuildingNumber>7</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71202</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>UL</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Marrowdale Sawmill Ltd</cbc:RegistrationName>
        <cbc:CompanyID>UL-1236987</cbc:CompanyID>
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
        <cbc:RegistrationName>Marrowdale Sawmill Ltd</cbc:RegistrationName>
        <cbc:CompanyID>20412329</cbc:CompanyID>
        <cbc:RegistrationDate>1996-01-01</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>Ltd</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Limited company (private)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Small</cbc:EntitySizeCode>
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
        <cbc:Name>Sales office</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 7120 2329</cbc:Telephone>
        <cbc:ElectronicMail>sales@marrowdalesawmill.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412329</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
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
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412329</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Marrowdale Sawmill</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-03-28</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>TRADE-ACCORD-PAY</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF83MSINV260635</cbc:InstructionNote>
    <cbc:PaymentID>RF83MSINV260635</cbc:PaymentID>
    <cbc:ChargeBearerCode>SHAR</cbc:ChargeBearerCode>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XB77BLUM0004398618</cbc:ID>
      <cbc:Name>Marrowdale Sawmill Ltd</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice MS-INV-26-0635</cbc:PaymentNote>
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
    <cbc:PenaltyAmount currencyID="XBL">518.40</cbc:PenaltyAmount>
    <cbc:PaymentTermsDetailsURI>https://www.marrowdalesawmill.example/terms</cbc:PaymentTermsDetailsURI>
    <cbc:PaymentDueDate>2026-03-28</cbc:PaymentDueDate>
    <cac:PenaltyPeriod>
      <cbc:StartDate>2026-03-29</cbc:StartDate>
      <cbc:DurationMeasure unitCode="MON">1</cbc:DurationMeasure>
    </cac:PenaltyPeriod>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">34560.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">34560.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">34560.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">34560.00</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XBL">34560.00</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="H87">4800</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">34560.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Sawn hardwood slat, 1800 × 95 × 38 mm, planed, kiln dried.</cbc:Description>
      <cbc:PackQuantity unitCode="H87">1</cbc:PackQuantity>
      <cbc:PackSizeNumeric>50</cbc:PackSizeNumeric>
      <cbc:Name>Hardwood bench slat 1800</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>MS-SL-1800</cbc:ID>
        <cac:MeasurementDimension>
          <cbc:AttributeID>Length</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">1800</cbc:Measure>
        </cac:MeasurementDimension>
      </cac:SellersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">772010000058</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:AdditionalItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">772010000065</cbc:ID>
      </cac:AdditionalItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="HS">4407.99</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>G</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReason>Export outside Bayvarra</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
      <cac:AdditionalItemProperty>
        <cbc:ID>MC</cbc:ID>
        <cbc:Name>Moisture content</cbc:Name>
        <cbc:NameCode>MC</cbc:NameCode>
        <cbc:TestMethod>Oven-dry method on samples from each kiln charge</cbc:TestMethod>
        <cbc:ValueQuantity unitCode="P1">12</cbc:ValueQuantity>
        <cbc:ValueQualifier>Average of the kiln charge</cbc:ValueQualifier>
        <cbc:ImportanceCode>Mandatory</cbc:ImportanceCode>
        <cac:ItemPropertyGroup>
          <cbc:ID>QUA</cbc:ID>
          <cbc:Name>Wood quality</cbc:Name>
          <cbc:ImportanceCode>Mandatory</cbc:ImportanceCode>
        </cac:ItemPropertyGroup>
        <cac:ItemPropertyRange>
          <cbc:MinimumValue>10</cbc:MinimumValue>
          <cbc:MaximumValue>14</cbc:MaximumValue>
        </cac:ItemPropertyRange>
        <cac:StandardPropertyIdentification>
          <cbc:ID>UR-WD-0012</cbc:ID>
          <cbc:IssuerScopeID>Codana timber properties</cbc:IssuerScopeID>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105644</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Codana Identification Agency</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:StandardPropertyIdentification>
        <cac:SubItemProperty>
          <cbc:Name>Moisture at the core</cbc:Name>
          <cbc:ValueQuantity unitCode="P1">13</cbc:ValueQuantity>
        </cac:SubItemProperty>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Thickness tolerance</cbc:Name>
        <cac:RangeDimension>
          <cbc:AttributeID>Thickness</cbc:AttributeID>
          <cbc:Measure unitCode="MMT">38</cbc:Measure>
          <cbc:MinimumMeasure unitCode="MMT">37.5</cbc:MinimumMeasure>
          <cbc:MaximumMeasure unitCode="MMT">38.5</cbc:MaximumMeasure>
        </cac:RangeDimension>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Surface</cbc:Name>
        <cbc:Value>Planed on four sides</cbc:Value>
        <cac:UsabilityPeriod>
          <cbc:DurationMeasure unitCode="MON">12</cbc:DurationMeasure>
        </cac:UsabilityPeriod>
      </cac:AdditionalItemProperty>
      <cac:Certificate>
        <cbc:ID>XB-FOR-2025-118</cbc:ID>
        <cbc:CertificateTypeCode>Sustainableforestry</cbc:CertificateTypeCode>
        <cbc:CertificateType>Sustainable forestry</cbc:CertificateType>
        <cbc:CertificateReferenceID>XB-FOR-REG-0118</cbc:CertificateReferenceID>
        <cbc:ApplicableCategoryCode>HW</cbc:ApplicableCategoryCode>
        <cbc:ApplicableCategory>Hardwood sawn timber</cbc:ApplicableCategory>
        <cbc:CertificateURI>https://forestry.xb.example/certificates/XB-FOR-2025-118</cbc:CertificateURI>
        <cbc:Remarks>The timber comes from forests in Upland State managed for regrowth.</cbc:Remarks>
        <cac:CertificateValidityPeriod>
          <cbc:EndDate>2027-12-31</cbc:EndDate>
        </cac:CertificateValidityPeriod>
        <cac:DocumentReference>
          <cbc:ID>XB-FOR-AUD-2025-118</cbc:ID>
        </cac:DocumentReference>
      </cac:Certificate>
      <cac:Dimension>
        <cbc:AttributeID>Length</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">1800</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID>Width</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">95</cbc:Measure>
      </cac:Dimension>
      <cac:Dimension>
        <cbc:AttributeID>Thickness</cbc:AttributeID>
        <cbc:Measure unitCode="MMT">38</cbc:Measure>
      </cac:Dimension>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">7.2</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
      <cbc:OrderableUnitFactorRate>50</cbc:OrderableUnitFactorRate>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
