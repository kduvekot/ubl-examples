# Purchase Receipt: Brightmarket Stores to Robin Ashdale

*Example 21 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Purchase Receipt in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PURCHASE-RECEIPT-SCHEMA)*

A consumer buys in the shop and gets a receipt.

[The XML file](21-PurchaseReceipt.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:retail**  
  The business process the document belongs to: the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)".
- `ProfileExecutionID` = **RETAIL-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BS-PR-26-0239**  
  The till's receipt number.
- `UUID` = **bcdeb9a7-e515-519a-b488-de52151e844f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-15**  
  A consumer buys a bench during the promotion week.
- `IssueTime` = **11:42:00**  
  Printed at the till.
- `TransactionDate` = **2026-05-15**  
  The day of the sale.
- `TransactionTime` = **11:42:00**  
  The time of the sale.
- `PurchaseDate` = **2026-05-15**  
  The day the customer bought.
- `PurchaseTime` = **11:42:00**  
  And when.
- `Note` = **Home delivery booked for Saturday.**  
  Printed on the receipt.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the currency of the shop; it has two decimals.

### Purchase Reference

Inside `PurchaseReference`:

- `ID` = **BM-LOYAL-0088127**  
  The customer's loyalty card.
- `Description` = **Loyalty card**  
  What the number is.

### Sales Document Reference

Inside `SalesDocumentReference`:

- `ID` = **BM-DEL-26-0518-07**  
  The home delivery order.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **VI-WARRANTY-B180**  
  The maker's warranty card.

### Signature

Inside `Signature`:

- `ID` = **BM-SIG-POS-G2**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

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
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
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
- `Party/Contact/ID` = **BM-CT-01**  
  The desk's number in the party's own contact list.
- `Party/Contact/Name` = **Buying office**  
  The desk that handles this document; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Telephone` = **+999 2 38 2511 0411**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `Party/AdditionalWebSite/Name` = **Online shop**  
  The store's second website, where consumers buy.
- `Party/AdditionalWebSite/URI` = **https://shop.brightmarket.example**  
  Under the reserved .example domain.
- `Party/SocialMediaProfile/ID` = **10442197**  
  The profile's number on the medium.
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

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyName/Name` = **Robin Ashdale**  
  The trading name; identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/AddressTypeCode` = **Residential**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `Party/PostalAddress/StreetName` = **Gull Lane**  
  Street of the postal address. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **57**  
  Building number of the postal address. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/Person/FirstName` = **Robin**  
  The consumer's first name; identity of Robin Ashdale (world/parties.json).
- `Party/Person/FamilyName` = **Ashdale**  
  The consumer's family name; identity of Robin Ashdale (world/parties.json).
- `Party/Person/FinancialAccount/ID` = **XB95BLUM0007251840** (schemeID `urn:ubl-examples:world:account`)  
  The consumer's own account, from which the bills are paid. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `Party/Person/FinancialAccount/Name` = **Robin Ashdale**  
  The account holder, as the bank knows it.
- `Party/Person/FinancialAccount/AccountTypeCode` = **Current**  
  A current account, for payments in and out.
- `Party/Person/FinancialAccount/AccountFormatCode` = **ISO13616**  
  The account number has the structure of ISO 13616.
- `Party/Person/FinancialAccount/CurrencyCode` = **XBL**  
  The account is kept in the currency of the bank's country.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/ID` = **BLUM-001**  
  The branch that keeps the account.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Name` = **Main branch**  
  The branch's name.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUM**  
  The bank code, the part of every account number that names the bank; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/StreetName` = **Exchange Street**  
  The bank's head office; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/BuildingNumber` = **48**  
  Its building number; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/CityName` = **Lumeport**  
  Its town; identity of Bank of Lumeport (world/parties.json).
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Address/Country/IdentificationCode` = **XB**  
  The bank's country.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Address/CityName` = **Lumeport**  
  The branch is at the bank's head office.
- `Party/Person/FinancialAccount/FinancialInstitutionBranch/Address/Country/IdentificationCode` = **XB**  
  Its country.
- `Party/Person/FinancialAccount/Country/IdentificationCode` = **XB**  
  The country where the account is kept.

### Cashier Contact

Inside `CashierContact`:

- `Name` = **Mira**  
  The cashier, by first name, as printed.

### Cash Register

Inside `CashRegister`:

- `ID` = **G2**  
  The till.
- `SerialNumberID` = **BM-POS-G2-2219**  
  The till's serial number, as the tax rules require on a receipt.

### Point of Sale Location

Inside `PointOfSaleLocation`:

- `Description` = **Garden department, ground floor**  
  Where in the shop.
- `Name` = **Brightmarket Stores, Lumeport**  
  The shop.

### Point of Sale Contact

Inside `PointOfSaleContact`:

- `Telephone` = **+999 2 38 2511 0411**  
  The shop's number, for questions about the purchase.

### Delivery

Inside `Delivery`:

- `DeliveryAddress/AddressTypeCode` = **Residential**  
  The kind of address.
- `DeliveryAddress/AddressFormatCode` = **XB**  
  The address follows Bayvarra's address format (world/countries.json), one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines.
- `DeliveryAddress/StreetName` = **Gull Lane**  
  Street of the postal address. identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/BuildingNumber` = **57**  
  Building number of the postal address. identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/CitySubdivisionName` = **Old town**  
  The quarter of Lumeport the party is in. identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits). identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra. identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/CountrySubentityCode` = **CO**  
  The state as a code of Bayvarra's address scheme (world/countries.json). identity of Robin Ashdale (world/parties.json).
- `DeliveryAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `DeliveryAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `DeliveryAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `RequestedDeliveryPeriod/StartDate` = **2026-05-17**  
  Saturday.
- `RequestedDeliveryPeriod/StartTime` = **09:00:00**  
  Morning.
- `RequestedDeliveryPeriod/EndTime` = **12:00:00**  
  Until noon.
- `CarrierParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `CarrierParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Payment

Inside `Payment`:

- `ID` = **BM-G2-26-0518-0047**  
  The till's number for the payment.
- `PaidAmount` = **744.54** (currencyID `XBL`)  
  Paid by card.
- `PaidDate` = **2026-05-15**  
  Paid at the till.
- `PaidTime` = **11:42:00**  
  At the time of the sale.
- `MerchantID` = **LUMECARD-M-0026118**  
  The store's merchant number with the card scheme.
- `AuthorizationID` = **A71520**  
  The approval code of the card issuer.
- `TransactionID` = **TX-26-0518-773104**  
  The card transaction.
- `PaymentTerminalID` = **PT-G2**  
  The card terminal at the till.
- `StatusCode` = **Approved**  
  The payment was approved.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **55** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 55: debit card.
- `CardAccount/PrimaryAccountNumberID` = **************4417**  
  The card number, masked: a receipt shows only the last four digits.
- `CardAccount/NetworkID` = **LUMECARD**  
  The card scheme of the world: Lumeport's interbank card.
- `CardAccount/CardTypeCode` = **Debit**  
  A debit card.
- `CardAccount/ValidityStartDate` = **2025-06-01**  
  The card is valid from.
- `CardAccount/ExpiryDate` = **2029-05-31**  
  And until.
- `CardAccount/IssuerID` = **BLUM**  
  Issued by the Bank of Lumeport.
- `CardAccount/IssueNumberID` = **01**  
  The card's issue number: the first card of this account.
- `CardAccount/CV2ID` = *******  
  Masked: card rules forbid printing or storing the card's security code.
- `CardAccount/CardChipCode` = **Chip**  
  Read from the chip.
- `CardAccount/ChipApplicationID` = **A0000099990001**  
  The chip application used; an identifier of the world, not a registered one.
- `CardAccount/HolderName` = **R ASHDALE**  
  The name on the card.
- `CardAccount/RoleCode` = **Holder**  
  Paid by the card holder.

### Allowance Charge

Inside `AllowanceCharge`:

- `ChargeIndicator` = **true**  
  A charge.
- `AllowanceChargeReason` = **Home delivery**  
  Delivered on Saturday, as booked.
- `Amount` = **25.00** (currencyID `XBL`)  
  The store's flat delivery charge.
- `TaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **45.44** (currencyID `XBL`)  
  6.5 % state sales tax on the bench and the delivery.
- `TaxSubtotal/TaxableAmount` = **699.10** (currencyID `XBL`)  
  The bench and the home delivery.
- `TaxSubtotal/TaxAmount` = **45.44** (currencyID `XBL`)  
  6.5 %.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **674.10** (currencyID `XBL`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **699.10** (currencyID `XBL`)  
  Before the sales tax.
- `TaxInclusiveAmount` = **744.54** (currencyID `XBL`)  
  With the sales tax.
- `ChargeTotalAmount` = **25.00** (currencyID `XBL`)  
  The home delivery.
- `PayableAmount` = **744.54** (currencyID `XBL`)  
  Paid by card: no cash rounding.

### Purchase Receipt Line

Inside `PurchaseReceiptLine`:

- `ID` = **1**  
  The line number.
- `UUID` = **ea701e0e-2453-5802-8bbd-0356ea20503d**  
  A universally unique identifier of the line, derived from the document and the line number.
- `Note` = **Promotion price.**  
  As printed.
- `Quantity` = **1** (unitCode `H87`)  
  One bench.
- `LineExtensionAmount` = **674.10** (currencyID `XBL`)  
  Quantity times the price paid, before the sales tax.
- `TaxInclusiveLineExtensionAmount` = **717.92** (currencyID `XBL`)  
  With the 6.5 % sales tax.
- `PurchaseLinePeriod/StartDate` = **2026-05-15**  
  The warranty runs from the purchase
- `PurchaseLinePeriod/EndDate` = **2031-05-15**  
  for five years.
- `PurchaseReference/ID` = **VI-SF-02170**  
  The serial number of the bench's frame, for the warranty.
- `PurchaseReference/Description` = **Frame serial number**  
  What the number is.
- `TaxTotal/TaxAmount` = **43.82** (currencyID `XBL`)  
  The sales tax of the line.
- `Item/Description` = **The Serra park bench in the store's garden department; the state sales tax is added at the till.**  
  The seller's description; item bench-serra-r of Brightmarket Stores (world/items.json).
- `Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra-r of Brightmarket Stores (world/items.json).
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
- `Item/SellersItemIdentification/ID` = **BM-551210**  
  The seller's own item number; item bench-serra-r of Brightmarket Stores (world/items.json).
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
- `Item/ItemSpecificationDocumentReference/ID` = **VI-DS-B180**  
  The maker's datasheet with drawings and assembly instructions.
- `Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-serra of Valdara Industries (world/items.json).
- `Item/CommodityClassification/CommodityCode` = **9401.79.10**  
  The national tariff code below the HS subheading, as the customs of the maker's country uses it.
- `Item/CommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-serra of Valdara Industries (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `Item/ClassifiedTaxCategory/Percent` = **6.5**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Goods**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
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
- `Price/PriceAmount` = **674.1** (currencyID `XBL`)  
  The shelf price of 749.0 less the promotion discount.
- `Price/TaxInclusivePriceAmount` = **717.92** (currencyID `XBL`)  
  The price the customer pays, with the 6.5 % sales tax.
- `Price/BaseQuantity` = **1** (unitCode `H87`)  
  The price is per one unit.
- `Price/PriceChangeReason` = **Spring garden promotion**  
  Why the price differs from the shelf price.
- `Price/ValidityPeriod/StartDate` = **2026-05-12**  
  The first day of the promotion.
- `Price/ValidityPeriod/EndDate` = **2026-05-18**  
  The last day of the promotion.
- `Price/AllowanceCharge/ChargeIndicator` = **false**  
  A discount, not a charge.
- `Price/AllowanceCharge/AllowanceChargeReasonCode` = **75** (listID `UN/EDIFACT EDED 5189`)  
  UN/EDIFACT 5189 code 75: promotion discount.
- `Price/AllowanceCharge/AllowanceChargeReason` = **Spring garden promotion**  
  The promotion, as the till prints it.
- `Price/AllowanceCharge/MultiplierFactorNumeric` = **0.1**  
  The discount rate.
- `Price/AllowanceCharge/Amount` = **74.90** (currencyID `XBL`)  
  The discount per unit, deducted from the shelf price.
- `Price/AllowanceCharge/BaseAmount` = **749.00** (currencyID `XBL`)  
  The shelf price the discount is taken from.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<PurchaseReceipt xmlns="urn:oasis:names:specification:ubl:schema:xsd:PurchaseReceipt-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:retail</cbc:ProfileID>
  <cbc:ProfileExecutionID>RETAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BS-PR-26-0239</cbc:ID>
  <cbc:UUID>bcdeb9a7-e515-519a-b488-de52151e844f</cbc:UUID>
  <cbc:IssueDate>2026-05-15</cbc:IssueDate>
  <cbc:IssueTime>11:42:00</cbc:IssueTime>
  <cbc:TransactionDate>2026-05-15</cbc:TransactionDate>
  <cbc:TransactionTime>11:42:00</cbc:TransactionTime>
  <cbc:PurchaseDate>2026-05-15</cbc:PurchaseDate>
  <cbc:PurchaseTime>11:42:00</cbc:PurchaseTime>
  <cbc:Note>Home delivery booked for Saturday.</cbc:Note>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cac:PurchaseReference>
    <cbc:ID>BM-LOYAL-0088127</cbc:ID>
    <cbc:Description>Loyalty card</cbc:Description>
  </cac:PurchaseReference>
  <cac:SalesDocumentReference>
    <cbc:ID>BM-DEL-26-0518-07</cbc:ID>
  </cac:SalesDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>VI-WARRANTY-B180</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:Signature>
    <cbc:ID>BM-SIG-POS-G2</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:AccountingSupplierParty>
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
        <cbc:ID>BM-CT-01</cbc:ID>
        <cbc:Name>Buying office</cbc:Name>
        <cbc:JobTitle>Customer service officer</cbc:JobTitle>
        <cbc:Department>Sales</cbc:Department>
        <cbc:Telephone>+999 2 38 2511 0411</cbc:Telephone>
        <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
        <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
      </cac:Contact>
      <cac:AdditionalWebSite>
        <cbc:Name>Online shop</cbc:Name>
        <cbc:URI>https://shop.brightmarket.example</cbc:URI>
      </cac:AdditionalWebSite>
      <cac:SocialMediaProfile>
        <cbc:ID>10442197</cbc:ID>
        <cbc:Name>brightmarket</cbc:Name>
        <cbc:SocialMediaTypeCode>Photo sharing</cbc:SocialMediaTypeCode>
        <cbc:URI>https://social.example/brightmarket</cbc:URI>
      </cac:SocialMediaProfile>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyName>
        <cbc:Name>Robin Ashdale</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:AddressTypeCode>Residential</cbc:AddressTypeCode>
        <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
        <cbc:StreetName>Gull Lane</cbc:StreetName>
        <cbc:BuildingNumber>57</cbc:BuildingNumber>
        <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38516</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
        <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          <cbc:Name>Bayvarra</cbc:Name>
        </cac:Country>
      </cac:PostalAddress>
      <cac:Person>
        <cbc:FirstName>Robin</cbc:FirstName>
        <cbc:FamilyName>Ashdale</cbc:FamilyName>
        <cac:FinancialAccount>
          <cbc:ID schemeID="urn:ubl-examples:world:account">XB95BLUM0007251840</cbc:ID>
          <cbc:Name>Robin Ashdale</cbc:Name>
          <cbc:AccountTypeCode>Current</cbc:AccountTypeCode>
          <cbc:AccountFormatCode>ISO13616</cbc:AccountFormatCode>
          <cbc:CurrencyCode>XBL</cbc:CurrencyCode>
          <cac:FinancialInstitutionBranch>
            <cbc:ID>BLUM-001</cbc:ID>
            <cbc:Name>Main branch</cbc:Name>
            <cac:FinancialInstitution>
              <cbc:ID>BLUM</cbc:ID>
              <cbc:Name>Bank of Lumeport</cbc:Name>
              <cac:Address>
                <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
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
        </cac:FinancialAccount>
      </cac:Person>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:CashierContact>
    <cbc:Name>Mira</cbc:Name>
  </cac:CashierContact>
  <cac:CashRegister>
    <cbc:ID>G2</cbc:ID>
    <cbc:SerialNumberID>BM-POS-G2-2219</cbc:SerialNumberID>
  </cac:CashRegister>
  <cac:PointOfSaleLocation>
    <cbc:Description>Garden department, ground floor</cbc:Description>
    <cbc:Name>Brightmarket Stores, Lumeport</cbc:Name>
  </cac:PointOfSaleLocation>
  <cac:PointOfSaleContact>
    <cbc:Telephone>+999 2 38 2511 0411</cbc:Telephone>
  </cac:PointOfSaleContact>
  <cac:Delivery>
    <cac:DeliveryAddress>
      <cbc:AddressTypeCode>Residential</cbc:AddressTypeCode>
      <cbc:AddressFormatCode>XB</cbc:AddressFormatCode>
      <cbc:StreetName>Gull Lane</cbc:StreetName>
      <cbc:BuildingNumber>57</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Old town</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38516</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode>CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-1</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:DeliveryAddress>
    <cac:RequestedDeliveryPeriod>
      <cbc:StartDate>2026-05-17</cbc:StartDate>
      <cbc:StartTime>09:00:00</cbc:StartTime>
      <cbc:EndTime>12:00:00</cbc:EndTime>
    </cac:RequestedDeliveryPeriod>
    <cac:CarrierParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:CarrierParty>
  </cac:Delivery>
  <cac:Payment>
    <cbc:ID>BM-G2-26-0518-0047</cbc:ID>
    <cbc:PaidAmount currencyID="XBL">744.54</cbc:PaidAmount>
    <cbc:PaidDate>2026-05-15</cbc:PaidDate>
    <cbc:PaidTime>11:42:00</cbc:PaidTime>
    <cbc:MerchantID>LUMECARD-M-0026118</cbc:MerchantID>
    <cbc:AuthorizationID>A71520</cbc:AuthorizationID>
    <cbc:TransactionID>TX-26-0518-773104</cbc:TransactionID>
    <cbc:PaymentTerminalID>PT-G2</cbc:PaymentTerminalID>
    <cbc:StatusCode>Approved</cbc:StatusCode>
  </cac:Payment>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">55</cbc:PaymentMeansCode>
    <cac:CardAccount>
      <cbc:PrimaryAccountNumberID>************4417</cbc:PrimaryAccountNumberID>
      <cbc:NetworkID>LUMECARD</cbc:NetworkID>
      <cbc:CardTypeCode>Debit</cbc:CardTypeCode>
      <cbc:ValidityStartDate>2025-06-01</cbc:ValidityStartDate>
      <cbc:ExpiryDate>2029-05-31</cbc:ExpiryDate>
      <cbc:IssuerID>BLUM</cbc:IssuerID>
      <cbc:IssueNumberID>01</cbc:IssueNumberID>
      <cbc:CV2ID>***</cbc:CV2ID>
      <cbc:CardChipCode>Chip</cbc:CardChipCode>
      <cbc:ChipApplicationID>A0000099990001</cbc:ChipApplicationID>
      <cbc:HolderName>R ASHDALE</cbc:HolderName>
      <cbc:RoleCode>Holder</cbc:RoleCode>
    </cac:CardAccount>
  </cac:PaymentMeans>
  <cac:AllowanceCharge>
    <cbc:ChargeIndicator>true</cbc:ChargeIndicator>
    <cbc:AllowanceChargeReason>Home delivery</cbc:AllowanceChargeReason>
    <cbc:Amount currencyID="XBL">25.00</cbc:Amount>
    <cac:TaxCategory>
      <cbc:ID>S</cbc:ID>
      <cbc:Percent>6.5</cbc:Percent>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
      </cac:TaxScheme>
    </cac:TaxCategory>
  </cac:AllowanceCharge>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">45.44</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">699.10</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">45.44</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>6.5</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XBL">674.10</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">699.10</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">744.54</cbc:TaxInclusiveAmount>
    <cbc:ChargeTotalAmount currencyID="XBL">25.00</cbc:ChargeTotalAmount>
    <cbc:PayableAmount currencyID="XBL">744.54</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:PurchaseReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:UUID>ea701e0e-2453-5802-8bbd-0356ea20503d</cbc:UUID>
    <cbc:Note>Promotion price.</cbc:Note>
    <cbc:Quantity unitCode="H87">1</cbc:Quantity>
    <cbc:LineExtensionAmount currencyID="XBL">674.10</cbc:LineExtensionAmount>
    <cbc:TaxInclusiveLineExtensionAmount currencyID="XBL">717.92</cbc:TaxInclusiveLineExtensionAmount>
    <cac:PurchaseLinePeriod>
      <cbc:StartDate>2026-05-15</cbc:StartDate>
      <cbc:EndDate>2031-05-15</cbc:EndDate>
    </cac:PurchaseLinePeriod>
    <cac:PurchaseReference>
      <cbc:ID>VI-SF-02170</cbc:ID>
      <cbc:Description>Frame serial number</cbc:Description>
    </cac:PurchaseReference>
    <cac:TaxTotal>
      <cbc:TaxAmount currencyID="XBL">43.82</cbc:TaxAmount>
    </cac:TaxTotal>
    <cac:Item>
      <cbc:Description>The Serra park bench in the store's garden department; the state sales tax is added at the till.</cbc:Description>
      <cbc:Name>Park bench Serra 180</cbc:Name>
      <cbc:AdditionalInformation>Supplied with four ground anchors and the bolts to fix them.</cbc:AdditionalInformation>
      <cbc:Keyword>park bench</cbc:Keyword>
      <cbc:Keyword>street furniture</cbc:Keyword>
      <cbc:BrandName>Valdara</cbc:BrandName>
      <cbc:ModelName>Serra 180</cbc:ModelName>
      <cbc:WarrantyInformation>Five years on the frame against corrosion.</cbc:WarrantyInformation>
      <cac:SellersItemIdentification>
        <cbc:ID>BM-551210</cbc:ID>
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
      </cac:StandardItemIdentification>
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
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>6.5</cbc:Percent>
        <cbc:SupplyTypeCode>Goods</cbc:SupplyTypeCode>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
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
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">674.1</cbc:PriceAmount>
      <cbc:TaxInclusivePriceAmount currencyID="XBL">717.92</cbc:TaxInclusivePriceAmount>
      <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
      <cbc:PriceChangeReason>Spring garden promotion</cbc:PriceChangeReason>
      <cac:ValidityPeriod>
        <cbc:StartDate>2026-05-12</cbc:StartDate>
        <cbc:EndDate>2026-05-18</cbc:EndDate>
      </cac:ValidityPeriod>
      <cac:AllowanceCharge>
        <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
        <cbc:AllowanceChargeReasonCode listID="UN/EDIFACT EDED 5189">75</cbc:AllowanceChargeReasonCode>
        <cbc:AllowanceChargeReason>Spring garden promotion</cbc:AllowanceChargeReason>
        <cbc:MultiplierFactorNumeric>0.1</cbc:MultiplierFactorNumeric>
        <cbc:Amount currencyID="XBL">74.90</cbc:Amount>
        <cbc:BaseAmount currencyID="XBL">749.00</cbc:BaseAmount>
      </cac:AllowanceCharge>
    </cac:Price>
  </cac:PurchaseReceiptLine>
</PurchaseReceipt>
```
