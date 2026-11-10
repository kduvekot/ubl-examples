# Purchase Receipt: Brightmarket Stores to Robin Ashdale

*Example 13 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Purchase Receipt in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-PURCHASE-RECEIPT-SCHEMA)*

A consumer buys in the shop and gets a receipt.

[The XML file](13-PurchaseReceipt.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **BS-PR-26-0237**  
  The till's receipt number.
- `IssueDate` = **2026-05-15**  
  A consumer buys a bench during the promotion week.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the currency of the shop; it has two decimals.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/StreetName` = **Market Street**  
  Street of the postal address; identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **50**  
  Building number of the postal address; identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38515**  
  Postal code in Bayvarra's format (5 digits); identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Brightmarket Stores (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **CO-1231233**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Brightmarket Stores (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyLegalEntity/RegistrationName` = **Brightmarket Stores**  
  The name under which the party is registered; identity of Brightmarket Stores (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410411**  
  Number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/Name` = **Buying office**  
  The department that handles this document; identity of Brightmarket Stores (world/parties.json).
- `Party/Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyName/Name` = **Robin Ashdale**  
  The trading name; identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/StreetName` = **Gull Lane**  
  Street of the postal address; identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **57**  
  Building number of the postal address; identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38516**  
  Postal code in Bayvarra's format (5 digits); identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Robin Ashdale (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **10** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 10: in cash.

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **48.69** (currencyID `XBL`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **749.00** (currencyID `XBL`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **48.69** (currencyID `XBL`)  
  6.5 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `TaxSubtotal/TaxCategory/Percent` = **6.5**  
  The rate for this category.
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **749.00** (currencyID `XBL`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **749.00** (currencyID `XBL`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **797.69** (currencyID `XBL`)  
  The total without tax plus the tax.
- `PayableAmount` = **797.69** (currencyID `XBL`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Purchase Receipt Line

Inside `PurchaseReceiptLine`:

- `ID` = **1**  
  The line number.
- `Quantity` = **1** (unitCode `H87`)  
  One bench.
- `LineExtensionAmount` = **749.00** (currencyID `XBL`)  
  Quantity times the shelf price, before the sales tax.
- `Item/Description` = **The Serra park bench in the store's garden department; the state sales tax is added at the till.**  
  The seller's description; item bench-serra-r of Brightmarket Stores (world/items.json).
- `Item/Name` = **Park bench Serra 180**  
  The item's short name; item bench-serra-r of Brightmarket Stores (world/items.json).
- `Item/SellersItemIdentification/ID` = **BM-551210**  
  The seller's own item number; item bench-serra-r of Brightmarket Stores (world/items.json).
- `Item/ManufacturersItemIdentification/ID` = **VI-B180**  
  The item number of the maker, Valdara Industries: the reseller's item is resale of item bench-serra (world/items.json).
- `Item/StandardItemIdentification/ID` = **771020000027** (schemeID `urn:ubl-examples:world:item`)  
  The world item number issued by the identifier issuing agency, twelve digits with a check digit; a scheme of the world, not a GTIN; item bench-serra of Valdara Industries, which this item resells (world/items.json).
- `Item/OriginCountry/IdentificationCode` = **XU**  
  Where the item was produced; item bench-serra of Valdara Industries, which this item resells (world/items.json).
- `Item/CommodityClassification/ItemClassificationCode` = **9401.79** (listID `HS`)  
  Harmonized System subheading of the World Customs Organization; item bench-serra of Valdara Industries, which this item resells (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **S**  
  A sale to a consumer: the sales tax of Coastal State, where the sale takes place, applies (category S).
- `Item/ClassifiedTaxCategory/Percent` = **6.5**  
  The rate for this category.
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of the seller's tax: state sales tax.
- `Price/PriceAmount` = **749** (currencyID `XBL`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `H87`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<PurchaseReceipt xmlns="urn:oasis:names:specification:ubl:schema:xsd:PurchaseReceipt-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>BS-PR-26-0237</cbc:ID>
  <cbc:IssueDate>2026-05-15</cbc:IssueDate>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Market Street</cbc:StreetName>
        <cbc:BuildingNumber>50</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38515</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>CO-1231233</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Brightmarket Stores</cbc:RegistrationName>
        <cbc:CompanyID>20410411</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Buying office</cbc:Name>
        <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
      </cac:Contact>
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
        <cbc:StreetName>Gull Lane</cbc:StreetName>
        <cbc:BuildingNumber>57</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38516</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">10</cbc:PaymentMeansCode>
  </cac:PaymentMeans>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XBL">48.69</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XBL">749.00</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XBL">48.69</cbc:TaxAmount>
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
    <cbc:LineExtensionAmount currencyID="XBL">749.00</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XBL">749.00</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XBL">797.69</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XBL">797.69</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:PurchaseReceiptLine>
    <cbc:ID>1</cbc:ID>
    <cbc:Quantity unitCode="H87">1</cbc:Quantity>
    <cbc:LineExtensionAmount currencyID="XBL">749.00</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>The Serra park bench in the store's garden department; the state sales tax is added at the till.</cbc:Description>
      <cbc:Name>Park bench Serra 180</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>BM-551210</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ManufacturersItemIdentification>
        <cbc:ID>VI-B180</cbc:ID>
      </cac:ManufacturersItemIdentification>
      <cac:StandardItemIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:item">771020000027</cbc:ID>
      </cac:StandardItemIdentification>
      <cac:OriginCountry>
        <cbc:IdentificationCode>XU</cbc:IdentificationCode>
      </cac:OriginCountry>
      <cac:CommodityClassification>
        <cbc:ItemClassificationCode listID="HS">9401.79</cbc:ItemClassificationCode>
      </cac:CommodityClassification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>6.5</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XBL">749</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="H87">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:PurchaseReceiptLine>
</PurchaseReceipt>
```
