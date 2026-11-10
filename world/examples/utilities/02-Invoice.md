# Invoice: Ferrano Energy to Valdara Industries

*Example 2 of the flow "Electricity, water and telecom (one utility in each country)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The electricity bill, with Urvania's VAT; it refers to the utility statement for the consumption.

[The XML file](02-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **FE-INV-26-0313**  
  The seller's invoice number.
- `UUID` = **47af4407-c4e0-59f4-b15c-7ba55c57e130**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  The monthly bill, issued on the first day of the next month.
- `IssueTime` = **13:20:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DueDate` = **2026-04-23**  
  21 days after the issue date, the agreed payment term.
- `InvoiceTypeCode` = **380**  
  UN/EDIFACT 1001 code 380: commercial invoice.
- `TaxPointDate` = **2026-04-02**  
  Urvania's value added tax becomes due on the invoice date.
- `DocumentCurrencyCode` = **XUF**  
  The ferra, the seller's currency; it has no minor unit.
- `AccountingCostCode` = **3100**  
  The buyer's cost centre, quoted in its order, so the invoice is booked without asking.
- `AccountingCost` = **Raw materials and parts**  
  The cost centre in words.
- `LineCountNumeric` = **2**  
  The number of invoice lines, as a check on the transfer.
- `DefaultLanguageCode` = **en**  
  The language the texts of the invoice are in: the seller's country's language.

### Invoice Period

Inside `InvoicePeriod`:

- `StartDate` = **2026-03-01**  
  The month billed: March.
- `EndDate` = **2026-03-31**  
  Its last day.
- `DescriptionCode` = **Month**  
  A monthly bill.
- `Description` = **March 2026**  
  The period in words.

### Purchase Reference

Inside `PurchaseReference`:

- `ID` = **FE-C-0047120**  
  The customer's contract number with the utility.
- `Description` = **Supply contract**  
  What the number is.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.ferranoenergy.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Ferrano Energy (world/parties.json).
- `Party/IndustryClassificationCode` = **3510** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Ferrano Energy (world/parties.json).
- `Party/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Energy (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Energy**  
  The trading name; identity of Ferrano Energy (world/parties.json).
- `Party/Language/ID` = **en**  
  English, the language the party does business in.
- `Party/Language/Name` = **English**  
  The language's name.
- `Party/Language/LocaleCode` = **EN**  
  The language as a code of UBL's language code list (ISO 639).
- `Party/PostalAddress/AddressFormatCode` = **XU**  
  The address follows Urvania's address format (world/countries.json): StreetName BuildingNumber / PostalZone CityName.
- `Party/PostalAddress/StreetName` = **Via della Centrale**  
  Street of the postal address. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **44**  
  Building number of the postal address. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/CityName` = **Serravona**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4130**  
  Postal code in Urvania's format (4 digits). identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/Region` = **Province of Ferrano**  
  The province, part of an address in Urvania. identity of Ferrano Energy (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Urvania**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Ferrano Energy SUA**  
  The name under which the party is registered for value added tax; identity of Ferrano Energy (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **XU007404785**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Energy (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **National**  
  The level of government that levies the tax: Urvania's value added tax is levied by the country.
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XUF**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XU**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Energy SUA**  
  The name under which the party is registered, with its legal form; identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-105781**  
  Number in the Commercial register of Urvania; identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1949-01-15**  
  The day the company was entered in the register; identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **SUA**  
  The legal form, as abbreviated in Urvania (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Società urvaniana per azioni (public limited company)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Ferrano Energy (world/parties.json).
- `Party/PartyLegalEntity/CorporateStockAmount` = **600000000** (currencyID `XUF`)  
  The share capital, in ferra; identity of Ferrano Energy (world/parties.json).
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
- `Party/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Telephone` = **+999 1 4130 5781**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@ferranoenergy.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Energy (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Ferrano Energy (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-105781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Energy (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

- `Party/PartyIdentification/ID` = **XU-R-105781** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Ferrano Energy**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `ID` = **1**  
  The first, and only, way to pay.
- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks.
- `PaymentMeansDescription` = **Credit transfer**  
  In words.
- `PaymentDueDate` = **2026-04-23**  
  When the transfer must be credited.
- `PaymentChannelCode` = **IBAN**  
  Paid to an account identified in the format of ISO 13616.
- `PaymentRailID` = **FERRA-RTGS**  
  The payment system the transfer runs over: the domestic clearing.
- `InstructionNote` = **Quote RF58FEINV260313**  
  What the payer writes in the transfer.
- `PaymentID` = **RF58FEINV260313**  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits.
- `PayeeFinancialAccount/ID` = **XU46CREV0004084431** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Ferrano Energy SUA**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XUF**  
  The account is kept in the currency of the bank's country.
- `PayeeFinancialAccount/PaymentNote` = **Invoice FE-INV-26-0313**  
  What the payer is asked to quote with the transfer, so the payment is matched.
- `PayeeFinancialAccount/FinancialInstitutionBranch/ID` = **CREV-001**  
  The branch that keeps the account.
- `PayeeFinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREV**  
  The bank code, the part of every account number that names the bank; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Piazza della Banca**  
  The bank's head office; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **8**  
  Its building number; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Ferrano**  
  Its town; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XU**  
  The bank's country.
- `PayeeFinancialAccount/Country/IdentificationCode` = **XU**  
  The country where the account is kept.

### Payment Terms

Inside `PaymentTerms`:

- `ID` = **XU-STD**  
  The standard terms of Urvania.
- `PaymentMeansID` = **1**  
  The payment means these terms apply to: the credit transfer below.
- `Note` = **30 days net; 2 % discount when paid within 10 days.**  
  Urvanian practice: a cash discount for early payment, statutory interest on late payment.
- `SettlementDiscountPercent` = **2**  
  The cash discount for early payment.
- `SettlementDiscountAmount` = **289585** (currencyID `XUF`)  
  The 2 % discount on the amount payable, if paid in time.
- `PaymentTermsDetailsURI` = **https://www.ferranoenergy.example/terms**  
  The seller's general terms of payment.
- `PaymentDueDate` = **2026-04-23**  
  The day the amount is due.
- `SettlementPeriod/StartDate` = **2026-04-02**  
  From the invoice date.
- `SettlementPeriod/EndDate` = **2026-04-12**  
  For 10 days.
- `PenaltyInterestRate/InterestRatePercent` = **8**  
  The interest on late payment.
- `PenaltyInterestRate/TimeBasisCode` = **Year**  
  A yearly rate.
- `PenaltyInterestRate/CalculationMethodCode` = **Simple**  
  Simple interest, per day late.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **2702052** (currencyID `XUF`)  
  Energy tax and value added tax together.
- `TaxEvidenceIndicator` = **true**  
  This tax total is the evidence for the customer's deduction of value added tax.
- `TaxIncludedIndicator` = **false**  
  The line prices do not include the taxes.
- `TaxSubtotal/TaxableAmount` = **60000** (currencyID `XUF`)  
  The tax base of the tier, in ferra.
- `TaxSubtotal/TaxAmount` = **60000** (currencyID `XUF`)  
  50000 kWh at 1.2 ferra.
- `TaxSubtotal/CalculationSequenceNumeric` = **1**  
  The energy tax is calculated first.
- `TaxSubtotal/BaseUnitMeasure` = **1** (unitCode `KWH`)  
  The tax is per kilowatt hour.
- `TaxSubtotal/PerUnitAmount` = **1** (currencyID `XUF`)  
  The tax per kWh in this tier.
- `TaxSubtotal/TierRange` = **The first 50,000 kWh of the month**  
  The tier of the monthly consumption.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  The energy tax applies.
- `TaxSubtotal/TaxCategory/Name` = **Energy tax**  
  The tax in words.
- `TaxSubtotal/TaxCategory/BaseUnitMeasure` = **1** (unitCode `KWH`)  
  Per kilowatt hour.
- `TaxSubtotal/TaxCategory/PerUnitAmount` = **1** (currencyID `XUF`)  
  The rate per kWh.
- `TaxSubtotal/TaxCategory/TierRange` = **The first 50,000 kWh of the month**  
  The tier.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **EXC**  
  UN/EDIFACT 5153 code EXC: excise duty, the energy tax.
- `TaxSubtotal/TaxDueCountry/IdentificationCode` = **XU**  
  Due in Urvania.
- `TaxSubtotal/TaxableAmount` = **228840** (currencyID `XUF`)  
  The tax base of the tier, in ferra.
- `TaxSubtotal/TaxAmount` = **228840** (currencyID `XUF`)  
  381400 kWh at 0.6 ferra.
- `TaxSubtotal/CalculationSequenceNumeric` = **1**  
  The energy tax is calculated first.
- `TaxSubtotal/BaseUnitMeasure` = **1** (unitCode `KWH`)  
  The tax is per kilowatt hour.
- `TaxSubtotal/PerUnitAmount` = **1** (currencyID `XUF`)  
  The tax per kWh in this tier.
- `TaxSubtotal/TierRange` = **Above 50,000 kWh: the industrial rate**  
  The tier of the monthly consumption.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  The energy tax applies.
- `TaxSubtotal/TaxCategory/Name` = **Energy tax**  
  The tax in words.
- `TaxSubtotal/TaxCategory/BaseUnitMeasure` = **1** (unitCode `KWH`)  
  Per kilowatt hour.
- `TaxSubtotal/TaxCategory/PerUnitAmount` = **1** (currencyID `XUF`)  
  The rate per kWh.
- `TaxSubtotal/TaxCategory/TierRange` = **Above 50,000 kWh: the industrial rate**  
  The tier.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **EXC**  
  UN/EDIFACT 5153 code EXC: excise duty, the energy tax.
- `TaxSubtotal/TaxDueCountry/IdentificationCode` = **XU**  
  Due in Urvania.
- `TaxSubtotal/TaxableAmount` = **12066060** (currencyID `XUF`)  
  The price plus the energy tax: value added tax is charged on both.
- `TaxSubtotal/TaxAmount` = **2413212** (currencyID `XUF`)  
  20 % of that base.
- `TaxSubtotal/TaxInclusiveAmount` = **14479272** (currencyID `XUF`)  
  The base with the tax.
- `TaxSubtotal/CalculationSequenceNumeric` = **2**  
  Calculated after the energy tax.
- `TaxSubtotal/Percent` = **20**  
  The standard rate.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S).
- `TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **11777220** (currencyID `XUF`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **11777220** (currencyID `XUF`)  
  The line amounts, without any tax.
- `TaxInclusiveAmount` = **14479272** (currencyID `XUF`)  
  With the energy tax and the value added tax.
- `PayableAmount` = **14479272** (currencyID `XUF`)  
  What the manufacturer pays.

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **412800** (unitCode `KWH`)  
  The factory's metered consumption in March.
- `LineExtensionAmount` = **11269440** (currencyID `XUF`)  
  412800 × 27.3, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **ELEC**  
  ISO 20022 purpose code ELEC: electricity bill.
- `InvoicePeriod/StartDate` = **2026-03-01**  
  The month billed: March.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  Its last day.
- `InvoicePeriod/DescriptionCode` = **Month**  
  A monthly bill.
- `InvoicePeriod/Description` = **March 2026**  
  The period in words.
- `PurchaseReference/ID` = **FE-M-881204**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Factory, main connection**  
  Where it is.
- `Item/Description` = **Electricity supply, per kilowatt hour, network charges included.**  
  The seller's description; item electricity of Ferrano Energy (world/items.json).
- `Item/Name` = **Electricity**  
  The item's short name; item electricity of Ferrano Energy (world/items.json).
- `Item/SellersItemIdentification/ID` = **FE-KWH**  
  The seller's own item number; item electricity of Ferrano Energy (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **S**  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S).
- `Item/ClassifiedTaxCategory/Percent` = **20**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Services**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.
- `Price/PriceAmount` = **27.3** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `KWH`)  
  The price is per one unit.
- `ID` = **2**  
  The line number.
- `InvoicedQuantity` = **18600** (unitCode `KWH`)  
  The warehouse's metered consumption in March; the manufacturer pays for its building.
- `LineExtensionAmount` = **507780** (currencyID `XUF`)  
  18600 × 27.3, rounded to the minor unit of the currency.
- `AccountingCostCode` = **7100**  
  The manufacturer books the warehouse's power on its transport cost centre.
- `AccountingCost` = **Warehouse, Castrano Logistics**  
  In words.
- `PaymentPurposeCode` = **ELEC**  
  ISO 20022 purpose code ELEC: electricity bill.
- `InvoicePeriod/StartDate` = **2026-03-01**  
  The month billed: March.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  Its last day.
- `InvoicePeriod/DescriptionCode` = **Month**  
  A monthly bill.
- `InvoicePeriod/Description` = **March 2026**  
  The period in words.
- `PurchaseReference/ID` = **FE-M-881377**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Warehouse of Castrano Logistics**  
  Where it is.
- `OriginatorParty/PartyIdentification/ID` = **XU-R-104411** (schemeID `urn:ubl-examples:world:XU:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `OriginatorParty/PartyName/Name` = **Castrano Logistics**  
  A party referred to from another party's details: its identifier and name are enough.
- `Delivery/DeliveryLocation/Description` = **Castrano Logistics warehouse, Ferrano**  
  Where the power was used.
- `Item/Description` = **Electricity supply, per kilowatt hour, network charges included.**  
  The seller's description; item electricity of Ferrano Energy (world/items.json).
- `Item/Name` = **Electricity**  
  The item's short name; item electricity of Ferrano Energy (world/items.json).
- `Item/SellersItemIdentification/ID` = **FE-KWH**  
  The seller's own item number; item electricity of Ferrano Energy (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **S**  
  A domestic supply in Urvania: its value added tax applies at the standard rate (category S).
- `Item/ClassifiedTaxCategory/Percent` = **20**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Services**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of the seller's tax: value added tax.
- `Price/PriceAmount` = **27.3** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `KWH`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:utilities</cbc:ProfileID>
  <cbc:ProfileExecutionID>UTILITIES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>FE-INV-26-0313</cbc:ID>
  <cbc:UUID>47af4407-c4e0-59f4-b15c-7ba55c57e130</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>13:20:00</cbc:IssueTime>
  <cbc:DueDate>2026-04-23</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:TaxPointDate>2026-04-02</cbc:TaxPointDate>
  <cbc:DocumentCurrencyCode>XUF</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>3100</cbc:AccountingCostCode>
  <cbc:AccountingCost>Raw materials and parts</cbc:AccountingCost>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode>en</cbc:DefaultLanguageCode>
  <cac:InvoicePeriod>
    <cbc:StartDate>2026-03-01</cbc:StartDate>
    <cbc:EndDate>2026-03-31</cbc:EndDate>
    <cbc:DescriptionCode>Month</cbc:DescriptionCode>
    <cbc:Description>March 2026</cbc:Description>
  </cac:InvoicePeriod>
  <cac:PurchaseReference>
    <cbc:ID>FE-C-0047120</cbc:ID>
    <cbc:Description>Supply contract</cbc:Description>
  </cac:PurchaseReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cbc:WebsiteURI>https://www.ferranoenergy.example</cbc:WebsiteURI>
      <cbc:IndustryClassificationCode listID="ISIC Rev.4">3510</cbc:IndustryClassificationCode>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Energy</cbc:Name>
      </cac:PartyName>
      <cac:Language>
        <cbc:ID>en</cbc:ID>
        <cbc:Name>English</cbc:Name>
        <cbc:LocaleCode>EN</cbc:LocaleCode>
      </cac:Language>
      <cac:PostalAddress>
        <cbc:AddressFormatCode>XU</cbc:AddressFormatCode>
        <cbc:StreetName>Via della Centrale</cbc:StreetName>
        <cbc:BuildingNumber>44</cbc:BuildingNumber>
        <cbc:CityName>Serravona</cbc:CityName>
        <cbc:PostalZone>4130</cbc:PostalZone>
        <cbc:Region>Province of Ferrano</cbc:Region>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
          <cbc:Name>Urvania</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:RegistrationName>Ferrano Energy SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU007404785</cbc:CompanyID>
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
        <cbc:RegistrationName>Ferrano Energy SUA</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-105781</cbc:CompanyID>
        <cbc:RegistrationDate>1949-01-15</cbc:RegistrationDate>
        <cbc:CompanyLegalFormCode>SUA</cbc:CompanyLegalFormCode>
        <cbc:CompanyLegalForm>Società urvaniana per azioni (public limited company)</cbc:CompanyLegalForm>
        <cbc:EntitySizeCode>Large</cbc:EntitySizeCode>
        <cbc:CorporateStockAmount currencyID="XUF">600000000</cbc:CorporateStockAmount>
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
        <cbc:Name>Customer service</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 1 4130 5781</cbc:Telephone>
        <cbc:ElectronicMail>customer@ferranoenergy.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-105781</cbc:ElectronicAddressID>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-105781</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Energy</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-04-23</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>FERRA-RTGS</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF58FEINV260313</cbc:InstructionNote>
    <cbc:PaymentID>RF58FEINV260313</cbc:PaymentID>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU46CREV0004084431</cbc:ID>
      <cbc:Name>Ferrano Energy SUA</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XUF</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice FE-INV-26-0313</cbc:PaymentNote>
      <cac:FinancialInstitutionBranch>
        <cbc:ID>CREV-001</cbc:ID>
        <cbc:Name>Main branch</cbc:Name>
        <cac:FinancialInstitution>
          <cbc:ID>CREV</cbc:ID>
          <cbc:Name>Crevalto Bank</cbc:Name>
          <cac:Address>
            <cbc:StreetName>Piazza della Banca</cbc:StreetName>
            <cbc:BuildingNumber>8</cbc:BuildingNumber>
            <cbc:CityName>Ferrano</cbc:CityName>
            <cac:Country>
              <cbc:IdentificationCode>XU</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:FinancialInstitution>
      </cac:FinancialInstitutionBranch>
      <cac:Country>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:Country>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:PaymentTerms>
    <cbc:ID>XU-STD</cbc:ID>
    <cbc:PaymentMeansID>1</cbc:PaymentMeansID>
    <cbc:Note>30 days net; 2 % discount when paid within 10 days.</cbc:Note>
    <cbc:SettlementDiscountPercent>2</cbc:SettlementDiscountPercent>
    <cbc:SettlementDiscountAmount currencyID="XUF">289585</cbc:SettlementDiscountAmount>
    <cbc:PaymentTermsDetailsURI>https://www.ferranoenergy.example/terms</cbc:PaymentTermsDetailsURI>
    <cbc:PaymentDueDate>2026-04-23</cbc:PaymentDueDate>
    <cac:SettlementPeriod>
      <cbc:StartDate>2026-04-02</cbc:StartDate>
      <cbc:EndDate>2026-04-12</cbc:EndDate>
    </cac:SettlementPeriod>
    <cac:PenaltyInterestRate>
      <cbc:InterestRatePercent>8</cbc:InterestRatePercent>
      <cbc:TimeBasisCode>Year</cbc:TimeBasisCode>
      <cbc:CalculationMethodCode>Simple</cbc:CalculationMethodCode>
    </cac:PenaltyInterestRate>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">2702052</cbc:TaxAmount>
    <cbc:TaxEvidenceIndicator>true</cbc:TaxEvidenceIndicator>
    <cbc:TaxIncludedIndicator>false</cbc:TaxIncludedIndicator>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">60000</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">60000</cbc:TaxAmount>
      <cbc:CalculationSequenceNumeric>1</cbc:CalculationSequenceNumeric>
      <cbc:BaseUnitMeasure unitCode="KWH">1</cbc:BaseUnitMeasure>
      <cbc:PerUnitAmount currencyID="XUF">1</cbc:PerUnitAmount>
      <cbc:TierRange>The first 50,000 kWh of the month</cbc:TierRange>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Name>Energy tax</cbc:Name>
        <cbc:BaseUnitMeasure unitCode="KWH">1</cbc:BaseUnitMeasure>
        <cbc:PerUnitAmount currencyID="XUF">1</cbc:PerUnitAmount>
        <cbc:TierRange>The first 50,000 kWh of the month</cbc:TierRange>
        <cac:TaxScheme>
          <cbc:ID>EXC</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
      <cac:TaxDueCountry>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:TaxDueCountry>
    </cac:TaxSubtotal>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">228840</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">228840</cbc:TaxAmount>
      <cbc:CalculationSequenceNumeric>1</cbc:CalculationSequenceNumeric>
      <cbc:BaseUnitMeasure unitCode="KWH">1</cbc:BaseUnitMeasure>
      <cbc:PerUnitAmount currencyID="XUF">1</cbc:PerUnitAmount>
      <cbc:TierRange>Above 50,000 kWh: the industrial rate</cbc:TierRange>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Name>Energy tax</cbc:Name>
        <cbc:BaseUnitMeasure unitCode="KWH">1</cbc:BaseUnitMeasure>
        <cbc:PerUnitAmount currencyID="XUF">1</cbc:PerUnitAmount>
        <cbc:TierRange>Above 50,000 kWh: the industrial rate</cbc:TierRange>
        <cac:TaxScheme>
          <cbc:ID>EXC</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
      <cac:TaxDueCountry>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:TaxDueCountry>
    </cac:TaxSubtotal>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">12066060</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">2413212</cbc:TaxAmount>
      <cbc:TaxInclusiveAmount currencyID="XUF">14479272</cbc:TaxInclusiveAmount>
      <cbc:CalculationSequenceNumeric>2</cbc:CalculationSequenceNumeric>
      <cbc:Percent>20</cbc:Percent>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XUF">11777220</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XUF">11777220</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XUF">14479272</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XUF">14479272</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="KWH">412800</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XUF">11269440</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode>ELEC</cbc:PaymentPurposeCode>
    <cac:InvoicePeriod>
      <cbc:StartDate>2026-03-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
      <cbc:DescriptionCode>Month</cbc:DescriptionCode>
      <cbc:Description>March 2026</cbc:Description>
    </cac:InvoicePeriod>
    <cac:PurchaseReference>
      <cbc:ID>FE-M-881204</cbc:ID>
      <cbc:Description>Factory, main connection</cbc:Description>
    </cac:PurchaseReference>
    <cac:Item>
      <cbc:Description>Electricity supply, per kilowatt hour, network charges included.</cbc:Description>
      <cbc:Name>Electricity</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>FE-KWH</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cbc:SupplyTypeCode>Services</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XUF">27.3</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="KWH">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:InvoicedQuantity unitCode="KWH">18600</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XUF">507780</cbc:LineExtensionAmount>
    <cbc:AccountingCostCode>7100</cbc:AccountingCostCode>
    <cbc:AccountingCost>Warehouse, Castrano Logistics</cbc:AccountingCost>
    <cbc:PaymentPurposeCode>ELEC</cbc:PaymentPurposeCode>
    <cac:InvoicePeriod>
      <cbc:StartDate>2026-03-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
      <cbc:DescriptionCode>Month</cbc:DescriptionCode>
      <cbc:Description>March 2026</cbc:Description>
    </cac:InvoicePeriod>
    <cac:PurchaseReference>
      <cbc:ID>FE-M-881377</cbc:ID>
      <cbc:Description>Warehouse of Castrano Logistics</cbc:Description>
    </cac:PurchaseReference>
    <cac:OriginatorParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Castrano Logistics</cbc:Name>
      </cac:PartyName>
    </cac:OriginatorParty>
    <cac:Delivery>
      <cac:DeliveryLocation>
        <cbc:Description>Castrano Logistics warehouse, Ferrano</cbc:Description>
      </cac:DeliveryLocation>
    </cac:Delivery>
    <cac:Item>
      <cbc:Description>Electricity supply, per kilowatt hour, network charges included.</cbc:Description>
      <cbc:Name>Electricity</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>FE-KWH</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cbc:SupplyTypeCode>Services</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XUF">27.3</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="KWH">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
