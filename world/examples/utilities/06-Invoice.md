# Invoice: Coastal State Water Company to Brightmarket Stores

*Example 6 of the flow "Electricity, water and telecom (one utility in each country)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The water bill for the shop. Water is exempt from the state sales tax, and the invoice says so with the exemption reason: leaving the tax out would say nothing (IND6).

[The XML file](06-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **CSWC-INV-26-0317**  
  The seller's invoice number.
- `UUID` = **4c1bf28b-075a-5826-abaf-d62f14b2f8da**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-02**  
  The monthly bill, issued on the first day of the next month.
- `IssueTime` = **09:13:00**  
  The time the sender's system issued the document, in the sender's local time.
- `DueDate` = **2026-04-23**  
  21 days after the issue date, the agreed payment term.
- `InvoiceTypeCode` = **380**  
  UN/EDIFACT 1001 code 380: commercial invoice.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the seller's currency; it has two decimals.
- `AccountingCostCode` = **6120**  
  The buyer's cost centre, quoted in its order, so the invoice is booked without asking.
- `AccountingCost` = **Garden department**  
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

- `ID` = **CSW-C-260118**  
  The customer's contract number with the utility.
- `Description` = **Supply contract**  
  What the number is.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/WebsiteURI` = **https://www.coastalwater.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Coastal State Water Company (world/parties.json).
- `Party/IndustryClassificationCode` = **3600** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Coastal State Water Company**  
  The trading name; identity of Coastal State Water Company (world/parties.json).
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
- `Party/PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Harbour quarter**  
  The quarter of Lumeport the party is in. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits). identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered for state sales tax; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1236576**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Coastal State Water Company (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Coastal State Water Company Ltd**  
  The name under which the party is registered, with its legal form; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412192**  
  Number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Limited company (private)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Coastal State Water Company (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
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
- `Party/Contact/Name` = **Customer service**  
  The desk that handles this document; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 3850 2192**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Coastal State Water Company (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Coastal State Water Company (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/WebsiteURI` = **https://www.brightmarket.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Brightmarket Stores (world/parties.json).
- `Party/LogoReferenceID` = **BM-LOGO-2024**  
  The reference of the logo the store prints on its documents; identity of Brightmarket Stores (world/parties.json).
- `Party/IndustryClassificationCode` = **4719** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `Party/TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
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
- `Party/PostalAddress/StreetName` = **Market Street**  
  Street of the postal address. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits). identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered for state sales tax; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1231233**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brightmarket Stores (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state whose sales tax the party is registered for.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/Country/IdentificationCode` = **XB**  
  The country whose tax this is.
- `Party/PartyLegalEntity/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered, with its legal form; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410411**  
  Number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1979-02-14**  
  The day the company was entered in the register; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Corp**  
  The legal form, as abbreviated in Bayvarra (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Corporation (public)**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Large**  
  The size class of the company (micro, small, medium or large); identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/CompanyLiquidationStatusCode` = **Active**  
  The register shows the company as active, not in liquidation.
- `Party/PartyLegalEntity/CorporateStockAmount` = **12000000** (currencyID `XBL`)  
  The share capital, in lume; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/FullyPaidSharesIndicator` = **true**  
  All shares are paid up.
- `Party/PartyLegalEntity/RegistrationAddress/CityName` = **Lumeport**  
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
- `Party/Contact/Name` = **Buying office**  
  The desk that handles this document; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 3851 0411**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `Party/AdditionalWebSite/Name` = **Online shop**  
  The store's second website, where consumers buy.
- `Party/AdditionalWebSite/URI` = **https://shop.brightmarket.example**  
  Under the reserved .example domain.
- `Party/SocialMediaProfile/Name` = **brightmarket**  
  The store's profile name.
- `Party/SocialMediaProfile/SocialMediaTypeCode` = **Photo sharing**  
  The kind of social medium.
- `Party/SocialMediaProfile/URI` = **https://social.example/brightmarket**  
  The profile's address, under the reserved .example domain.
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Coastal State Water Company**  
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
- `PaymentRailID` = **LUMEPAY**  
  The payment system the transfer runs over: the domestic clearing.
- `InstructionNote` = **Quote RF03CSWCINV260317**  
  What the payer writes in the transfer.
- `PaymentID` = **RF03CSWCINV260317**  
  The structured creditor reference of ISO 11649 to quote with the payment, made from the invoice number with its check digits.
- `PayeeFinancialAccount/ID` = **XB52BLUM0004189160** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/Name` = **Coastal State Water Company Ltd**  
  The account holder, as the bank knows it.
- `PayeeFinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `PayeeFinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `PayeeFinancialAccount/CurrencyCode` = **XBL**  
  The account is kept in the currency of the bank's country.
- `PayeeFinancialAccount/PaymentNote` = **Invoice CSWC-INV-26-0317**  
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
- `PenaltyAmount` = **3.57** (currencyID `XBL`)  
  The surcharge for the first month late.
- `PaymentTermsDetailsURI` = **https://www.coastalwater.example/terms**  
  The seller's general terms of payment.
- `PaymentDueDate` = **2026-04-23**  
  The day the amount is due.
- `PenaltyPeriod/StartDate` = **2026-04-24**  
  From the day after the due date.
- `PenaltyPeriod/DurationMeasure` = **1** (unitCode `MON`)  
  Per month.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.00** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **202.10** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **E**  
  Drinking water is exempt from the state sales tax (category E).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **XB-WATER**  
  The world's code for the exemption reason (world/countries.json).
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Drinking water**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `TaxSubtotal/TaxableAmount` = **36.12** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.00** (currencyID `XBL`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **O**  
  A public levy the seller collects for Lumeport Public Works Department: not a supply, so outside the scope of the sales tax (category O).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxExemptionReasonCode` = **XB-LEVY**  
  The world's code for the exemption reason (world/countries.json).
- `TaxSubtotal/TaxCategory/TaxExemptionReason` = **Levy collected for a public body**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **238.22** (currencyID `XBL`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **238.22** (currencyID `XBL`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **238.22** (currencyID `XBL`)  
  The total without tax plus the tax.
- `PayableAmount` = **238.22** (currencyID `XBL`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **86** (unitCode `MTQ`)  
  The shop's metered consumption in March.
- `LineExtensionAmount` = **202.10** (currencyID `XBL`)  
  86 × 2.35, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **WTER**  
  ISO 20022 purpose code WTER: water bill.
- `InvoicePeriod/StartDate` = **2026-03-01**  
  The month billed: March.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  Its last day.
- `InvoicePeriod/DescriptionCode` = **Month**  
  A monthly bill.
- `InvoicePeriod/Description` = **March 2026**  
  The period in words.
- `PurchaseReference/ID` = **CSW-W-55102**  
  The meter or subscription the line is for.
- `PurchaseReference/Description` = **Shop, Lumeport**  
  Where it is.
- `Item/Description` = **Drinking water supply, per cubic metre.**  
  The seller's description; item water of Coastal State Water Company (world/items.json).
- `Item/Name` = **Drinking water**  
  The item's short name; item water of Coastal State Water Company (world/items.json).
- `Item/SellersItemIdentification/ID` = **CW-M3**  
  The seller's own item number; item water of Coastal State Water Company (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **E**  
  Drinking water is exempt from the state sales tax (category E).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **XB-WATER**  
  The world's code for the exemption reason (world/countries.json).
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Drinking water**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Services**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Price/PriceAmount` = **2.35** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  The price is per one unit.
- `ID` = **2**  
  The line number.
- `Note` = **Collected for the city of Lumeport and paid on to it.**  
  Why the water company bills it.
- `InvoicedQuantity` = **86** (unitCode `MTQ`)  
  The shop's water use, on which the city charges its levy.
- `LineExtensionAmount` = **36.12** (currencyID `XBL`)  
  86 × 0.42, rounded to the minor unit of the currency.
- `PaymentPurposeCode` = **WTER**  
  ISO 20022 purpose code WTER: water bill.
- `InvoicePeriod/StartDate` = **2026-03-01**  
  The month billed: March.
- `InvoicePeriod/EndDate` = **2026-03-31**  
  Its last day.
- `InvoicePeriod/DescriptionCode` = **Month**  
  A monthly bill.
- `InvoicePeriod/Description` = **March 2026**  
  The period in words.
- `CollectedForParty/PartyIdentification/ID` = **20410548** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `CollectedForParty/PartyName/Name` = **Lumeport Public Works Department**  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/Description` = **The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.**  
  The seller's description; item sewage-levy of Coastal State Water Company (world/items.json).
- `Item/Name` = **Sewage levy of the city of Lumeport**  
  The item's short name; item sewage-levy of Coastal State Water Company (world/items.json).
- `Item/SellersItemIdentification/ID` = **CSW-LEVY**  
  The seller's own item number; item sewage-levy of Coastal State Water Company (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **O**  
  A public levy the seller collects for Lumeport Public Works Department: not a supply, so outside the scope of the sales tax (category O).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxExemptionReasonCode` = **XB-LEVY**  
  The world's code for the exemption reason (world/countries.json).
- `Item/ClassifiedTaxCategory/TaxExemptionReason` = **Levy collected for a public body**  
  Why no tax is charged, stated rather than left out (UBL rule IND6).
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Services**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Price/PriceAmount` = **0.42** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `MTQ`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:utilities</cbc:ProfileID>
  <cbc:ProfileExecutionID>UTILITIES-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>CSWC-INV-26-0317</cbc:ID>
  <cbc:UUID>4c1bf28b-075a-5826-abaf-d62f14b2f8da</cbc:UUID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:IssueTime>09:13:00</cbc:IssueTime>
  <cbc:DueDate>2026-04-23</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cbc:AccountingCostCode>6120</cbc:AccountingCostCode>
  <cbc:AccountingCost>Garden department</cbc:AccountingCost>
  <cbc:LineCountNumeric>2</cbc:LineCountNumeric>
  <cbc:DefaultLanguageCode>en</cbc:DefaultLanguageCode>
  <cac:InvoicePeriod>
    <cbc:StartDate>2026-03-01</cbc:StartDate>
    <cbc:EndDate>2026-03-31</cbc:EndDate>
    <cbc:DescriptionCode>Month</cbc:DescriptionCode>
    <cbc:Description>March 2026</cbc:Description>
  </cac:InvoicePeriod>
  <cac:PurchaseReference>
    <cbc:ID>CSW-C-260118</cbc:ID>
    <cbc:Description>Supply contract</cbc:Description>
  </cac:PurchaseReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
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
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
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
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
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
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
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
        <cbc:AddressTypeCode>Business</cbc:AddressTypeCode>
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
        <cbc:CompanyLiquidationStatusCode>Active</cbc:CompanyLiquidationStatusCode>
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
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Coastal State Water Company</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:ID>1</cbc:ID>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cbc:PaymentMeansDescription>Credit transfer</cbc:PaymentMeansDescription>
    <cbc:PaymentDueDate>2026-04-23</cbc:PaymentDueDate>
    <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
    <cbc:PaymentRailID>LUMEPAY</cbc:PaymentRailID>
    <cbc:InstructionNote>Quote RF03CSWCINV260317</cbc:InstructionNote>
    <cbc:PaymentID>RF03CSWCINV260317</cbc:PaymentID>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XB52BLUM0004189160</cbc:ID>
      <cbc:Name>Coastal State Water Company Ltd</cbc:Name>
      <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
      <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
      <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
      <cbc:PaymentNote>Invoice CSWC-INV-26-0317</cbc:PaymentNote>
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
    <cbc:PenaltyAmount currencyID="XBL">3.57</cbc:PenaltyAmount>
    <cbc:PaymentTermsDetailsURI>https://www.coastalwater.example/terms</cbc:PaymentTermsDetailsURI>
    <cbc:PaymentDueDate>2026-04-23</cbc:PaymentDueDate>
    <cac:PenaltyPeriod>
      <cbc:StartDate>2026-04-24</cbc:StartDate>
      <cbc:DurationMeasure unitCode="MON">1</cbc:DurationMeasure>
    </cac:PenaltyPeriod>
  </cac:PaymentTerms>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">202.10</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-WATER</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">36.12</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">0.00</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-LEVY</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Levy collected for a public body</cbc:TaxExemptionReason>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">238.22</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">238.22</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">238.22</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XBL">238.22</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="MTQ">86</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">202.10</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode>WTER</cbc:PaymentPurposeCode>
    <cac:InvoicePeriod>
      <cbc:StartDate>2026-03-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
      <cbc:DescriptionCode>Month</cbc:DescriptionCode>
      <cbc:Description>March 2026</cbc:Description>
    </cac:InvoicePeriod>
    <cac:PurchaseReference>
      <cbc:ID>CSW-W-55102</cbc:ID>
      <cbc:Description>Shop, Lumeport</cbc:Description>
    </cac:PurchaseReference>
    <cac:Item>
      <cbc:Description>Drinking water supply, per cubic metre.</cbc:Description>
      <cbc:Name>Drinking water</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CW-M3</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>E</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-WATER</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Drinking water</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode>Services</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">2.35</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:Note>Collected for the city of Lumeport and paid on to it.</cbc:Note>
    <cbc:InvoicedQuantity unitCode="MTQ">86</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XBL">36.12</cbc:LineExtensionAmount>
    <cbc:PaymentPurposeCode>WTER</cbc:PaymentPurposeCode>
    <cac:InvoicePeriod>
      <cbc:StartDate>2026-03-01</cbc:StartDate>
      <cbc:EndDate>2026-03-31</cbc:EndDate>
      <cbc:DescriptionCode>Month</cbc:DescriptionCode>
      <cbc:Description>March 2026</cbc:Description>
    </cac:InvoicePeriod>
    <cac:CollectedForParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410548</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeport Public Works Department</cbc:Name>
      </cac:PartyName>
    </cac:CollectedForParty>
    <cac:Item>
      <cbc:Description>The city's levy for sewage treatment, per cubic metre of water used; collected by the water company for the city.</cbc:Description>
      <cbc:Name>Sewage levy of the city of Lumeport</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>CSW-LEVY</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cbc:TaxExemptionReasonCode>XB-LEVY</cbc:TaxExemptionReasonCode>
        <cbc:TaxExemptionReason>Levy collected for a public body</cbc:TaxExemptionReason>
        <cbc:SupplyTypeCode>Services</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">0.42</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MTQ">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
