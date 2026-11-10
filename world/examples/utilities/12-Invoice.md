# Invoice: Selanu Telecom to Velumi Trading

*Example 12 of the flow "Electricity, water and telecom (one utility in each country)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

The telecom bill. The island has no sales tax or VAT, and the invoice says that no tax applies rather than leaving it out.

[The XML file](12-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **ST-INV-26-0322**  
  The seller's invoice number.
- `IssueDate` = **2026-04-02**  
  The monthly bill, issued on the first day of the next month.
- `DueDate` = **2026-04-23**  
  21 days after the issue date, the agreed payment term.
- `InvoiceTypeCode` = **380**  
  UN/EDIFACT 1001 code 380: commercial invoice.
- `DocumentCurrencyCode` = **XLC**  
  The coral, the seller's currency; it has three decimals.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Telecom (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The trading name; identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/StreetName` = **Mast Hill Road**  
  Street of the postal address; identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **58**  
  Building number of the postal address; identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Selanu Telecom (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyLegalEntity/RegistrationName` = **Selanu Telecom**  
  The name under which the party is registered; identity of Selanu Telecom (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42407**  
  Number in the Island companies register; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/Name` = **Business accounts**  
  The department that handles this document; identity of Selanu Telecom (world/parties.json).
- `Party/Contact/ElectronicMail` = **business@selanutelecom.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Telecom (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42407** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Telecom (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/StreetName` = **Reef Street**  
  Street of the postal address; identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **16**  
  Building number of the postal address; identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Velumi Trading (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyLegalEntity/RegistrationName` = **Velumi Trading**  
  The name under which the party is registered; identity of Velumi Trading (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC41859**  
  Number in the Island companies register; identity of Velumi Trading (world/parties.json).
- `Party/Contact/Name` = **Purchasing**  
  The department that handles this document; identity of Velumi Trading (world/parties.json).
- `Party/Contact/ElectronicMail` = **purchasing@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Buyer Customer Party

Inside `BuyerCustomerParty`:

- `Party/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Velumi Trading**  
  The same party as at AccountingCustomerParty/Party, where its full details are given; only its identifier and name are repeated.

### Seller Supplier Party

Inside `SellerSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42407** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Selanu Telecom**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of UBL's payment means code list, which code list validation checks.
- `PayeeFinancialAccount/ID` = **XL88BSEL0004293889** (schemeID `urn:ubl-examples:world:account`)  
  The account to pay to. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BSEL**  
  The bank code, the part of every account number that names the bank; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Selanu**  
  The bank; identity of Bank of Selanu (world/parties.json).

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **0.000** (currencyID `XLC`)  
  The sum of the tax of all categories.
- `TaxSubtotal/TaxableAmount` = **141.920** (currencyID `XLC`)  
  The sum of the line amounts in this tax category.
- `TaxSubtotal/TaxAmount` = **0.000** (currencyID `XLC`)  
  0 % of the taxable amount, rounded to the minor unit of the currency.
- `TaxSubtotal/TaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `TaxSubtotal/TaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `TaxSubtotal/TaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **141.920** (currencyID `XLC`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **141.920** (currencyID `XLC`)  
  The total without tax: the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **141.920** (currencyID `XLC`)  
  The total without tax plus the tax.
- `PayableAmount` = **141.920** (currencyID `XLC`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The line number.
- `InvoicedQuantity` = **6** (unitCode `MON`)  
  Six business lines for the month.
- `LineExtensionAmount` = **127.080** (currencyID `XLC`)  
  6 × 21.18, rounded to the minor unit of the currency.
- `Item/Description` = **Business telephone and data line, monthly subscription.**  
  The seller's description; item telecom-line of Selanu Telecom (world/items.json).
- `Item/Name` = **Business telephone line**  
  The item's short name; item telecom-line of Selanu Telecom (world/items.json).
- `Item/SellersItemIdentification/ID` = **ST-BL**  
  The seller's own item number; item telecom-line of Selanu Telecom (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.
- `Price/PriceAmount` = **21.18** (currencyID `XLC`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `MON`)  
  The price is per one unit.
- `ID` = **2**  
  The line number.
- `InvoicedQuantity` = **35** (unitCode `E34`)  
  Mobile data beyond the subscriptions.
- `LineExtensionAmount` = **14.840** (currencyID `XLC`)  
  35 × 0.424, rounded to the minor unit of the currency.
- `Item/Description` = **Mobile data beyond the subscription, per gigabyte.**  
  The seller's description; item telecom-data of Selanu Telecom (world/items.json).
- `Item/Name` = **Mobile data**  
  The item's short name; item telecom-data of Selanu Telecom (world/items.json).
- `Item/SellersItemIdentification/ID` = **ST-GB**  
  The seller's own item number; item telecom-data of Selanu Telecom (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **O**  
  Lisavu has no sales tax or value added tax: no tax applies (category O).
- `Item/ClassifiedTaxCategory/Percent` = **0**  
  No tax is charged in this category.
- `Item/ClassifiedTaxCategory/TaxScheme/Name` = **No general sales tax**  
  Lisavu has no general tax on sales; the scheme is named only, as UN/EDIFACT 5153 has no code for the absence of a tax.
- `Price/PriceAmount` = **0.424** (currencyID `XLC`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `E34`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>ST-INV-26-0322</cbc:ID>
  <cbc:IssueDate>2026-04-02</cbc:IssueDate>
  <cbc:DueDate>2026-04-23</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>XLC</cbc:DocumentCurrencyCode>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Mast Hill Road</cbc:StreetName>
        <cbc:BuildingNumber>58</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Selanu Telecom</cbc:RegistrationName>
        <cbc:CompanyID>IC42407</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Business accounts</cbc:Name>
        <cbc:ElectronicMail>business@selanutelecom.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42407</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Reef Street</cbc:StreetName>
        <cbc:BuildingNumber>16</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Velumi Trading</cbc:RegistrationName>
        <cbc:CompanyID>IC41859</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Purchasing</cbc:Name>
        <cbc:ElectronicMail>purchasing@velumi.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:BuyerCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:BuyerCustomerParty>
  <cac:SellerSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42407</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Telecom</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XL88BSEL0004293889</cbc:ID>
      <cac:FinancialInstitutionBranch>
        <cac:FinancialInstitution>
          <cbc:ID>BSEL</cbc:ID>
          <cbc:Name>Bank of Selanu</cbc:Name>
        </cac:FinancialInstitution>
      </cac:FinancialInstitutionBranch>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XLC">141.920</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XLC">0.000</cbc:TaxAmount>
      <cac:TaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cac:TaxScheme>
          <cbc:Name>No general sales tax</cbc:Name>
        </cac:TaxScheme>
      </cac:TaxCategory>
    </cac:TaxSubtotal>
  </cac:TaxTotal>
  <cac:LegalMonetaryTotal>
    <cbc:LineExtensionAmount currencyID="XLC">141.920</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XLC">141.920</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XLC">141.920</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XLC">141.920</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="MON">6</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">127.080</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Business telephone and data line, monthly subscription.</cbc:Description>
      <cbc:Name>Business telephone line</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>ST-BL</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cac:TaxScheme>
          <cbc:Name>No general sales tax</cbc:Name>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">21.18</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="MON">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
  <cac:InvoiceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:InvoicedQuantity unitCode="E34">35</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XLC">14.840</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Mobile data beyond the subscription, per gigabyte.</cbc:Description>
      <cbc:Name>Mobile data</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>ST-GB</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>O</cbc:ID>
        <cbc:Percent>0</cbc:Percent>
        <cac:TaxScheme>
          <cbc:Name>No general sales tax</cbc:Name>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XLC">0.424</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="E34">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
