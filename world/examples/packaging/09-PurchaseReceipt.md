# Purchase Receipt: Brightmarket Stores to Velumi Trading

*Example 9 of the flow "Packaging for the benches, clothing for the store" · [Purchase Receipt in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PURCHASE-RECEIPT-SCHEMA)*

The island trader's buyer, in Lumeport for the trade fair, buys shirts for the stand team and pays in coral with the island card: the till converts at the counter.

[The XML file](09-PurchaseReceipt.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

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
- `ID` = **BS-PR-26-0531**  
  The till's receipt number.
- `UUID` = **0a1ab530-6d49-5174-913f-d50624881433**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-23**  
  During the trade fair in Lumeport.
- `IssueTime` = **12:20:00**  
  Printed at the till.
- `TransactionDate` = **2026-05-23**  
  The day of the sale.
- `TransactionTime` = **12:20:00**  
  The time of the sale.
- `PurchaseDate` = **2026-05-23**  
  The day the customer bought.
- `PurchaseTime` = **12:20:00**  
  And when.
- `Note` = **Paid in coral: the card's currency was chosen at the till.**  
  Printed on the receipt.
- `DocumentCurrencyCode` = **XLC**  
  The coral, the currency the customer chose to pay in; it has three decimals.

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
- `Party/Contact/ID` = **BM-CT-01**  
  The desk's number in the party's own contact list.
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

- `Party/WebsiteURI` = **https://www.velumi.example**  
  The party's website, under the reserved .example domain (RFC 2606); identity of Velumi Trading (world/parties.json).
- `Party/IndustryClassificationCode` = **4649** (listID `ISIC Rev.4`)  
  What the party does, as an ISIC Rev. 4 class of the United Nations' industry classification; identity of Velumi Trading (world/parties.json).
- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/AdditionalPartyIdentification/ID` = **XL-TR-041859** (schemeID `urn:ubl-examples:world:XL:customs-trader`)  
  A second identifier: the party's customs trader number, because it imports or exports (XL-TR- and 6 digits); identity of Velumi Trading (world/parties.json).
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Party/Language/ID` = **qal**  
  Lisavan, the language of Lisavu and of the party; the code is from the range ISO 639 reserves for local use (qaa–qtz), as the world's languages are invented (world/countries.json).
- `Party/Language/Name` = **Lisavan**  
  The language's name in English; in the language itself: Lisavuana.
- `Party/PostalAddress/AddressTypeCode` = **Business**  
  The kind of address.
- `Party/PostalAddress/AddressFormatCode` = **XL**  
  The address follows Lisavu's address format (world/countries.json): BuildingNumber StreetName / CityName.
- `Party/PostalAddress/StreetName` = **Reef Street**  
  Street of the postal address. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state. identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/TimezoneOffset` = **-1**  
  The party's time zone, one hour behind UTC, where the world lies (world/countries.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PostalAddress/Country/Name` = **Lisavu**  
  The country's name, for readers of the address.
- `Party/PartyLegalEntity/RegistrationName` = **Velumi Trading Ltd**  
  The name under which the party is registered, with its legal form; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/RegistrationDate` = **1996-01-01**  
  The day the company was entered in the register; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyLegalFormCode` = **Ltd**  
  The legal form, as abbreviated in Lisavu (world/countries.json).
- `Party/PartyLegalEntity/CompanyLegalForm` = **Island limited company**  
  The legal form, in words.
- `Party/PartyLegalEntity/EntitySizeCode` = **Small**  
  The size class of the company (micro, small, medium or large); identity of Velumi Trading (world/parties.json).
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
- `Party/Contact/Name` = **Purchasing**  
  The desk that handles this document; identity of Velumi Trading (world/parties.json).
- `Party/Contact/JobTitle` = **Customer service officer**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Department` = **Sales**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Telephone` = **+999 3 3000 1859**  
  Telephone under +999, a country code the ITU keeps in reserve (ITU-T E.164), so the number reaches no one; identity of Velumi Trading (world/parties.json).
- `Party/Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

- `Telephone` = **+999 2 3851 0411**  
  The shop's number, for questions about the purchase.

### Payment

Inside `Payment`:

- `PaidAmount` = **38.276** (currencyID `XLC`)  
  Charged to the card in coral.
- `PaidDate` = **2026-05-23**  
  At the till.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **54** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 54: credit card.
- `CardAccount/PrimaryAccountNumberID` = **************2286**  
  Masked.
- `CardAccount/NetworkID` = **CORALCARD**  
  The island's card scheme.
- `CardAccount/HolderName` = **VELUMI TRADING**  
  A company card.

### Tax Exchange Rate

Inside `TaxExchangeRate`:

- `SourceCurrencyCode` = **XLC**  
  The receipt's currency.
- `TargetCurrencyCode` = **XBL**  
  The sales tax is owed to the state in lume.
- `CalculationRate` = **2.5**  
  The reference rate.
- `MathematicOperatorCode` = **Multiply**  
  Coral times the rate gives lume.
- `Date` = **2026-05-23**  
  The day of the sale.

### Pricing Exchange Rate

Inside `PricingExchangeRate`:

- `SourceCurrencyCode` = **XBL**  
  The shelf prices are in lume.
- `TargetCurrencyCode` = **XLC**  
  The receipt is in coral.
- `CalculationRate` = **0.4**  
  The world's reference rate, which the till applies.
- `MathematicOperatorCode` = **Multiply**  
  Lume times the rate gives coral.
- `Date` = **2026-05-23**  
  The day of the sale.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **2.336** (currencyID `XLC`)  
  The state sales tax, in coral.
- `TaxSubtotal/TaxableAmount` = **35.940** (currencyID `XLC`)  
  The shirts.
- `TaxSubtotal/TaxAmount` = **2.336** (currencyID `XLC`)  
  6.5 % of the lume price, converted.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `TaxAmount` = **5.84** (currencyID `XBL`)  
  The same tax in lume, as the store owes it to the state.
- `TaxSubtotal/TaxableAmount` = **89.85** (currencyID `XBL`)  
  Three shirts at the shelf price.
- `TaxSubtotal/TaxAmount` = **5.84** (currencyID `XBL`)  
  6.5 %.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **35.940** (currencyID `XLC`)  
  The shirts, in coral.
- `TaxExclusiveAmount` = **35.940** (currencyID `XLC`)  
  Before tax.
- `TaxInclusiveAmount` = **38.276** (currencyID `XLC`)  
  With tax.
- `PayableAmount` = **38.276** (currencyID `XLC`)  
  Paid by card: no rounding.

### Purchase Receipt Line

Inside `PurchaseReceiptLine`:

- `ID` = **1**  
  The line.
- `Quantity` = **3** (unitCode `H87`)  
  Three shirts.
- `LineExtensionAmount` = **35.940** (currencyID `XLC`)  
  Three at the converted price.
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
- `Price/PriceAmount` = **11.98** (currencyID `XLC`)  
  The shelf price of 29.95 lume, in coral.
- `Price/BaseQuantity` = **1** (unitCode `H87`)  
  Per shirt.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<PurchaseReceipt xmlns="urn:oasis:names:specification:ubl:schema:xsd:PurchaseReceipt-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:process:packaging</cbc:ProfileID>
  <cbc:ProfileExecutionID>PACKAGING-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BS-PR-26-0531</cbc:ID>
  <cbc:UUID>0a1ab530-6d49-5174-913f-d50624881433</cbc:UUID>
  <cbc:IssueDate>2026-05-23</cbc:IssueDate>
  <cbc:IssueTime>12:20:00</cbc:IssueTime>
  <cbc:TransactionDate>2026-05-23</cbc:TransactionDate>
  <cbc:TransactionTime>12:20:00</cbc:TransactionTime>
  <cbc:PurchaseDate>2026-05-23</cbc:PurchaseDate>
  <cbc:PurchaseTime>12:20:00</cbc:PurchaseTime>
  <cbc:Note>Paid in coral: the card's currency was chosen at the till.</cbc:Note>
  <cbc:DocumentCurrencyCode>XLC</cbc:DocumentCurrencyCode>
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
        <cbc:Telephone>+999 2 3851 0411</cbc:Telephone>
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
        <cbc:StreetName>Reef Street</cbc:StreetName>
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
    <cbc:Telephone>+999 2 3851 0411</cbc:Telephone>
  </cac:PointOfSaleContact>
  <cac:Payment>
    <cbc:PaidAmount currencyID="XLC">38.276</cbc:PaidAmount>
    <cbc:PaidDate>2026-05-23</cbc:PaidDate>
  </cac:Payment>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">54</cbc:PaymentMeansCode>
    <cac:CardAccount>
      <cbc:PrimaryAccountNumberID>************2286</cbc:PrimaryAccountNumberID>
      <cbc:NetworkID>CORALCARD</cbc:NetworkID>
      <cbc:HolderName>VELUMI TRADING</cbc:HolderName>
    </cac:CardAccount>
  </cac:PaymentMeans>
  <cac:TaxExchangeRate>
    <cbc:SourceCurrencyCode>XLC</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XBL</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>2.5</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-05-23</cbc:Date>
  </cac:TaxExchangeRate>
  <cac:PricingExchangeRate>
    <cbc:SourceCurrencyCode>XBL</cbc:SourceCurrencyCode>
    <cbc:TargetCurrencyCode>XLC</cbc:TargetCurrencyCode>
    <cbc:CalculationRate>0.4</cbc:CalculationRate>
    <cbc:MathematicOperatorCode>Multiply</cbc:MathematicOperatorCode>
    <cbc:Date>2026-05-23</cbc:Date>
  </cac:PricingExchangeRate>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XLC">2.336</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">35.940</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XLC">2.336</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>6.5</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">5.84</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">89.85</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">5.84</cbc:TaxAmount>
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
    <cbc:LineExtensionAmount currencyID="XLC">35.940</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XLC">35.940</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XLC">38.276</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XLC">38.276</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:PurchaseReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Quantity unitCode="H87">3</cbc:Quantity>
    <cbc:LineExtensionAmount currencyID="XLC">35.940</cbc:LineExtensionAmount>
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
      <cbc:PriceAmount currencyID="XLC">11.98</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:PurchaseReceiptLine>
</PurchaseReceipt>
```
