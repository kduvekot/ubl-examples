# Purchase Receipt: Brightmarket Stores to Robin Ashdale

*Example 8 of the flow "Packaging for the benches, clothing for the store" · [Purchase Receipt in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PURCHASE-RECEIPT-SCHEMA)*

The consumer buys a shirt; the receipt shows the state sales tax, the only point where Bayvarra's tax is charged.

[The XML file](08-PurchaseReceipt.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ProfileID` = **urn:ubl-examples:world:process:packaging**  
  The business process the document belongs to: the flow "Packaging for the benches, clothing for the store".
- `ProfileExecutionID` = **PACKAGING-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BS-PR-26-0530**  
  The till's receipt number.
- `UUID` = **cce7560b-887a-56e6-8fcd-571ce027241e**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-22**  
  A consumer buys two shirts.
- `IssueTime` = **16:05:00**  
  Printed at the till.
- `TransactionDate` = **2026-05-22**  
  The day of the sale.
- `TransactionTime` = **16:05:00**  
  The time of the sale.
- `PurchaseDate` = **2026-05-22**  
  The day the customer bought.
- `PurchaseTime` = **16:05:00**  
  And when.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the currency of the shop; it has two decimals.

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
  The state or territory, part of an address in federal Bayvarra. identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Party/PartyTaxScheme/RegistrationName` = **Brightmarket Stores Corp**  
  The name under which the party is registered for state sales tax; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyTaxScheme/CompanyID` = **CO-1231233**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State, NT Northern Territory), hyphen, 7 digits (sales tax permit of the state or territory)); identity of Brightmarket Stores (world/parties.json).
- `Party/PartyTaxScheme/TaxLevelCode` = **State**  
  The level of government that levies the tax: Bayvarra's state sales tax is levied by the states.
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyTaxScheme/TaxScheme/CurrencyCode` = **XBL**  
  The tax is accounted for in the country's currency.
- `Party/PartyTaxScheme/TaxScheme/JurisdictionRegionAddress/CountrySubentity` = **Coastal State**  
  The state or territory whose sales tax the party is registered for.
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
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brightmarket Stores (world/parties.json).
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
  The state or territory, part of an address in federal Bayvarra. identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CountrySubentityCode` = **CO**  
  The state or territory as a code of Bayvarra's address scheme (world/countries.json). identity of Robin Ashdale (world/parties.json).
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

- `Name` = **Joss**  
  The cashier, by first name, as printed.

### Cash Register

Inside `CashRegister`:

- `ID` = **C1**  
  The till.
- `SerialNumberID` = **BM-POS-C1-2219**  
  The till's serial number, as the tax rules require on a receipt.

### Point of Sale Location

Inside `PointOfSaleLocation`:

- `Description` = **Clothing, first floor**  
  Where in the shop.
- `Name` = **Brightmarket Stores, Lumeport**  
  The shop.

### Point of Sale Contact

Inside `PointOfSaleContact`:

- `Telephone` = **+999 2 38 2511 0411**  
  The shop's number, for questions about the purchase.

### Payment

Inside `Payment`:

- `PaidAmount` = **58.45** (currencyID `XBL`)  
  Paid in cash.
- `PaidCashAmount` = **70.00** (currencyID `XBL`)  
  The notes the customer handed over.
- `CashChangeAmount` = **11.55** (currencyID `XBL`)  
  The change given.
- `PaidDate` = **2026-05-22**  
  At the till.
- `PaidTime` = **16:05:00**  
  At the time of the sale.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **10** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 10: in cash.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **3.57** (currencyID `XBL`)  
  6.5 % state sales tax, the only point where Bayvarra's tax is charged.
- `TaxSubtotal/TaxableAmount` = **54.90** (currencyID `XBL`)  
  The shirts less the offer.
- `TaxSubtotal/TaxAmount` = **3.57** (currencyID `XBL`)  
  6.5 %.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **54.90** (currencyID `XBL`)  
  The line.
- `TaxExclusiveAmount` = **54.90** (currencyID `XBL`)  
  Before tax.
- `TaxInclusiveAmount` = **58.47** (currencyID `XBL`)  
  With tax.
- `PayableRoundingAmount` = **-0.02** (currencyID `XBL`)  
  Cash is rounded to 5 cents, Bayvarra's smallest coin.
- `PayableAmount` = **58.45** (currencyID `XBL`)  
  Paid in cash, rounded.

### Purchase Receipt Line

Inside `PurchaseReceiptLine`:

- `ID` = **1**  
  The line number.
- `Quantity` = **2** (unitCode `H87`)  
  Two shirts.
- `LineExtensionAmount` = **54.90** (currencyID `XBL`)  
  Two shirts less the offer.
- `AllowanceCharge/ChargeIndicator` = **false**  
  An allowance on the line.
- `AllowanceCharge/AllowanceChargeReason` = **Two shirts: 5.00 off the pair**  
  The store's offer.
- `AllowanceCharge/Amount` = **5.00** (currencyID `XBL`)  
  Off the pair.
- `AllowanceCharge/BaseAmount` = **59.90** (currencyID `XBL`)  
  Two shirts at the shelf price.
- `Item/Description` = **Men's cotton shirt; the state sales tax is added at the till.**  
  The seller's description; item shirt-r of Brightmarket Stores (world/items.json).
- `Item/Name` = **Cotton shirt**  
  The item's short name; item shirt-r of Brightmarket Stores (world/items.json).
- `Item/BrandName` = **Lumeport**  
  The brand the maker sells the item under; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/SellersItemIdentification/ID` = **BM-778120**  
  The seller's own item number; item shirt-r of Brightmarket Stores (world/items.json).
- `Item/ManufacturersItemIdentification/ID` = **LT-SH-01**  
  The item number of the maker, Lumeport Textile Mill: the reseller's item is resale of item shirt.
- `Item/StandardItemIdentification/ID` = **772030000090** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XB**  
  Where the item was produced; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **6205.20** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `Item/ClassifiedTaxCategory/Percent` = **6.5**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/SupplyTypeCode` = **Goods**  
  Whether the category applies to goods or services.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Item/AdditionalItemProperty/Name` = **Material**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **100 % cotton grown on Lisavu**  
  Its value; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/AdditionalItemProperty/Name` = **Sizes**  
  A property buyers ask about.
- `Item/AdditionalItemProperty/Value` = **S to XL**  
  Its value; item shirt of Lumeport Textile Mill (world/items.json).
- `Item/ManufacturerParty/PartyIdentification/ID` = **20412603** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `Item/ManufacturerParty/PartyName/Name` = **Lumeport Textile Mill**  
  A party referred to from another party's details: its identifier and name are enough.
- `Price/PriceAmount` = **29.95** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/TaxInclusivePriceAmount` = **31.9** (currencyID `XBL`)  
  The price the customer pays, with the 6.5 % sales tax.
- `Price/BaseQuantity` = **1** (unitCode `H87`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<PurchaseReceipt xmlns="urn:oasis:names:specification:ubl:schema:xsd:PurchaseReceipt-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:packaging</cbc:ProfileID>
  <cbc:ProfileExecutionID>PACKAGING-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BS-PR-26-0530</cbc:ID>
  <cbc:UUID>cce7560b-887a-56e6-8fcd-571ce027241e</cbc:UUID>
  <cbc:IssueDate>2026-05-22</cbc:IssueDate>
  <cbc:IssueTime>16:05:00</cbc:IssueTime>
  <cbc:TransactionDate>2026-05-22</cbc:TransactionDate>
  <cbc:TransactionTime>16:05:00</cbc:TransactionTime>
  <cbc:PurchaseDate>2026-05-22</cbc:PurchaseDate>
  <cbc:PurchaseTime>16:05:00</cbc:PurchaseTime>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
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
    <cbc:Name>Joss</cbc:Name>
  </cac:CashierContact>
  <cac:CashRegister>
    <cbc:ID>C1</cbc:ID>
    <cbc:SerialNumberID>BM-POS-C1-2219</cbc:SerialNumberID>
  </cac:CashRegister>
  <cac:PointOfSaleLocation>
    <cbc:Description>Clothing, first floor</cbc:Description>
    <cbc:Name>Brightmarket Stores, Lumeport</cbc:Name>
  </cac:PointOfSaleLocation>
  <cac:PointOfSaleContact>
    <cbc:Telephone>+999 2 38 2511 0411</cbc:Telephone>
  </cac:PointOfSaleContact>
  <cac:Payment>
    <cbc:PaidAmount currencyID="XBL">58.45</cbc:PaidAmount>
    <cbc:PaidCashAmount currencyID="XBL">70.00</cbc:PaidCashAmount>
    <cbc:CashChangeAmount currencyID="XBL">11.55</cbc:CashChangeAmount>
    <cbc:PaidDate>2026-05-22</cbc:PaidDate>
    <cbc:PaidTime>16:05:00</cbc:PaidTime>
  </cac:Payment>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">10</cbc:PaymentMeansCode>
  </cac:PaymentMeans>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">3.57</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">54.90</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">3.57</cbc:TaxAmount>
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
    <cbc:LineExtensionAmount currencyID="XBL">54.90</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">54.90</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">58.47</cbc:TaxInclusiveAmount>
    <cbc:PayableRoundingAmount currencyID="XBL">-0.02</cbc:PayableRoundingAmount>
    <cbc:PayableAmount currencyID="XBL">58.45</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:PurchaseReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Quantity unitCode="H87">2</cbc:Quantity>
    <cbc:LineExtensionAmount currencyID="XBL">54.90</cbc:LineExtensionAmount>
    <cac:AllowanceCharge>
      <cbc:ChargeIndicator>false</cbc:ChargeIndicator>
      <cbc:AllowanceChargeReason>Two shirts: 5.00 off the pair</cbc:AllowanceChargeReason>
      <cbc:Amount currencyID="XBL">5.00</cbc:Amount>
      <cbc:BaseAmount currencyID="XBL">59.90</cbc:BaseAmount>
    </cac:AllowanceCharge>
    <cac:Item>
      <cbc:Description>Men's cotton shirt; the state sales tax is added at the till.</cbc:Description>
      <cbc:Name>Cotton shirt</cbc:Name>
      <cbc:BrandName>Lumeport</cbc:BrandName>
      <cac:SellersItemIdentification>
        <cbc:ID>BM-778120</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>LT-SH-01</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">772030000090</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="HS">6205.20</cbc:ItemClassificationCode>
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
        <cbc:Name>Material</cbc:Name>
        <cbc:Value>100 % cotton grown on Lisavu</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:AdditionalItemProperty>
        <cbc:Name>Sizes</cbc:Name>
        <cbc:Value>S to XL</cbc:Value>
      </cac:AdditionalItemProperty>
      <cac:ManufacturerParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412603</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Textile Mill</cbc:Name>
        </cac:PartyName>
      </cac:ManufacturerParty>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">29.95</cbc:PriceAmount>
      <cbc:TaxInclusivePriceAmount currencyID="XBL">31.9</cbc:TaxInclusivePriceAmount>
      <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:PurchaseReceiptLine>
</PurchaseReceipt>
```
