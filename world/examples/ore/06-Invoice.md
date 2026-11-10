# Invoice: Ferrano Rail Cargo to Valdara Industries

*Example 6 of the flow "Ore from the mine to the factory (domestic, Urvania)" · [Invoice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-SCHEMA)*

Under FCA the buyer pays the carriage: the rail carrier invoices the ore freight to the manufacturer, per tonne.

[The XML file](06-Invoice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **FRC-INV-26-2207**  
  The seller's invoice number.
- `IssueDate` = **2026-03-12**  
  Issued the day after the goods were despatched and weighed.
- `DueDate` = **2026-04-11**  
  Thirty days after the issue date, the payment term of the world's domestic trade.
- `InvoiceTypeCode` = **380**  
  UN/EDIFACT 1001 code 380: commercial invoice.
- `DocumentCurrencyCode` = **XUF**  
  The ferra, the seller's currency, in the world's currency code list.

### Additional Document Reference

Inside `AdditionalDocumentReference`:

- `ID` = **FRC-TEP-26-1193**  
  The transport plan with the agreed price.
- `ID` = **FRC-WB-26-5521**  
  The consignment note of the carriage invoiced.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Ferrano Rail Cargo**  
  The trading name; identity of Ferrano Rail Cargo (world/parties.json).
- `Party/PostalAddress/StreetName` = **Viale della Stazione**  
  Street of the postal address; identity of Ferrano Rail Cargo (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **38**  
  Building number of the postal address; identity of Ferrano Rail Cargo (world/parties.json).
- `Party/PostalAddress/CityName` = **Serravona**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Ferrano Rail Cargo (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4150**  
  Postal code in Urvania's format (4 digits); identity of Ferrano Rail Cargo (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **XU007328060**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Ferrano Rail Cargo (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyLegalEntity/RegistrationName` = **Ferrano Rail Cargo**  
  The name under which the party is registered; identity of Ferrano Rail Cargo (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104685**  
  Number in the Commercial register of Urvania; identity of Ferrano Rail Cargo (world/parties.json).
- `Party/Contact/Name` = **Freight desk**  
  The department that handles this document; identity of Ferrano Rail Cargo (world/parties.json).
- `Party/Contact/ElectronicMail` = **freight@ferranorail.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Ferrano Rail Cargo (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XU:XU-R-104685** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Ferrano Rail Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **XU-R-104274** (schemeID `urn:ubl-examples:world:XU:register`)  
  The party's preferred identifier: its number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Valdara Industries**  
  The trading name; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/StreetName` = **Via delle Officine**  
  Street of the postal address; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **17**  
  Building number of the postal address; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/CityName` = **Ferrano**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/PostalZone` = **4120**  
  Postal code in Urvania's format (4 digits); identity of Valdara Industries (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XU**  
  Urvania: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **XU007299291**  
  Tax number under Urvania's value added tax (XU and 9 digits, the last a check digit (weights 9..2, modulus 11)); identity of Valdara Industries (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Party/PartyLegalEntity/RegistrationName` = **Valdara Industries**  
  The name under which the party is registered; identity of Valdara Industries (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **XU-R-104274**  
  Number in the Commercial register of Urvania; identity of Valdara Industries (world/parties.json).
- `Party/Contact/Name` = **Order desk**  
  The department that handles this document; identity of Valdara Industries (world/parties.json).
- `Party/Contact/ElectronicMail` = **order@valdara.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Valdara Industries (world/parties.json).
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

- `Party/PartyIdentification/ID` = **XU-R-104685** (schemeID `urn:ubl-examples:world:XU:register`)  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.
- `Party/PartyName/Name` = **Ferrano Rail Cargo**  
  The same party as at AccountingSupplierParty/Party, where its full details are given; only its identifier and name are repeated.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer, how businesses in Urvania pay. The listID is the identification of UBL's payment means code list, which code list validation checks.
- `PayeeFinancialAccount/ID` = **XU09CREV0000523645** (schemeID `urn:ubl-examples:world:account`)  
  The seller's account, where the buyer is to pay. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **CREV**  
  The bank code, the part of every account number that names the bank; identity of Crevalto Bank (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Crevalto Bank**  
  The bank; identity of Crevalto Bank (world/parties.json).

### Tax Total

Inside `TaxTotal`:

- `TaxAmount` = **344088** (currencyID `XUF`)  
  The value added tax of the invoice. Rounded to whole ferra, which have no minor unit.
- `TaxSubtotal/TaxableAmount` = **1720441** (currencyID `XUF`)  
  The sum of the line amounts at the standard rate.
- `TaxSubtotal/TaxAmount` = **344088** (currencyID `XUF`)  
  20 % of the taxable amount, rounded to whole ferra.
- `TaxSubtotal/TaxCategory/ID` = **S**  
  A domestic supply in Urvania: Urvania's value added tax applies at the standard rate. UN/EDIFACT 5305 code S, standard rate.
- `TaxSubtotal/TaxCategory/Percent` = **20**  
  The rate of Urvania's value added tax for this category (world/countries.json).
- `TaxSubtotal/TaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `LineExtensionAmount` = **1720441** (currencyID `XUF`)  
  The sum of the line amounts.
- `TaxExclusiveAmount` = **1720441** (currencyID `XUF`)  
  The total without tax: the sum of the line amounts, no allowances or charges.
- `TaxInclusiveAmount` = **2064529** (currencyID `XUF`)  
  The total without tax plus the value added tax.
- `PayableAmount` = **2064529** (currencyID `XUF`)  
  What the buyer is to pay; stated, not left to be calculated (UBL 2.5, 2.2.2 Manifest Values).

### Invoice Line

Inside `InvoiceLine`:

- `ID` = **1**  
  The first and only line.
- `InvoicedQuantity` = **1788.4** (unitCode `TNE`)  
  The weight carried, from the consignment note: the freight is per tonne.
- `LineExtensionAmount` = **1720441** (currencyID `XUF`)  
  1788.4 × 962 ferra, rounded to whole ferra.
- `Item/Description` = **Ore from the mine siding to the factory siding, per tonne.**  
  The seller's description; item rail-ore of Ferrano Rail Cargo (world/items.json).
- `Item/Name` = **Rail freight, ore in bulk wagons**  
  The item's short name; item rail-ore of Ferrano Rail Cargo (world/items.json).
- `Item/SellersItemIdentification/ID` = **FRC-ORE**  
  The seller's own item number; item rail-ore of Ferrano Rail Cargo (world/items.json).
- `Item/ClassifiedTaxCategory/ID` = **S**  
  A domestic supply in Urvania: Urvania's value added tax applies at the standard rate. UN/EDIFACT 5305 code S, standard rate.
- `Item/ClassifiedTaxCategory/Percent` = **20**  
  The rate of Urvania's value added tax for this category (world/countries.json).
- `Item/ClassifiedTaxCategory/TaxScheme/ID` = **VAT**  
  UN/EDIFACT 5153 code of Urvania's value added tax.
- `Price/PriceAmount` = **962** (currencyID `XUF`)  
  The seller's price per unit (world/items.json).
- `Price/BaseQuantity` = **1** (unitCode `TNE`)  
  The price is per one unit.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>FRC-INV-26-2207</cbc:ID>
  <cbc:IssueDate>2026-03-12</cbc:IssueDate>
  <cbc:DueDate>2026-04-11</cbc:DueDate>
  <cbc:InvoiceTypeCode>380</cbc:InvoiceTypeCode>
  <cbc:DocumentCurrencyCode>XUF</cbc:DocumentCurrencyCode>
  <cac:AdditionalDocumentReference>
    <cbc:ID>FRC-TEP-26-1193</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:AdditionalDocumentReference>
    <cbc:ID>FRC-WB-26-5521</cbc:ID>
  </cac:AdditionalDocumentReference>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Rail Cargo</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Viale della Stazione</cbc:StreetName>
        <cbc:BuildingNumber>38</cbc:BuildingNumber>
        <cbc:CityName>Serravona</cbc:CityName>
        <cbc:PostalZone>4150</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>XU007328060</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Ferrano Rail Cargo</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104685</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Freight desk</cbc:Name>
        <cbc:ElectronicMail>freight@ferranorail.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XU:XU-R-104685</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Valdara Industries</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Via delle Officine</cbc:StreetName>
        <cbc:BuildingNumber>17</cbc:BuildingNumber>
        <cbc:CityName>Ferrano</cbc:CityName>
        <cbc:PostalZone>4120</cbc:PostalZone>
        <cac:Country>
          <cbc:IdentificationCode>XU</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>XU007299291</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Valdara Industries</cbc:RegistrationName>
        <cbc:CompanyID>XU-R-104274</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Order desk</cbc:Name>
        <cbc:ElectronicMail>order@valdara.example</cbc:ElectronicMail>
      </cac:Contact>
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
        <cbc:ID schemeID="urn:ubl-examples:world:XU:register">XU-R-104685</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Ferrano Rail Cargo</cbc:Name>
      </cac:PartyName>
    </cac:Party>
  </cac:SellerSupplierParty>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XU09CREV0000523645</cbc:ID>
      <cac:FinancialInstitutionBranch>
        <cac:FinancialInstitution>
          <cbc:ID>CREV</cbc:ID>
          <cbc:Name>Crevalto Bank</cbc:Name>
        </cac:FinancialInstitution>
      </cac:FinancialInstitutionBranch>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:TaxTotal>
    <cbc:TaxAmount currencyID="XUF">344088</cbc:TaxAmount>
    <cac:TaxSubtotal>
      <cbc:TaxableAmount currencyID="XUF">1720441</cbc:TaxableAmount>
      <cbc:TaxAmount currencyID="XUF">344088</cbc:TaxAmount>
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
    <cbc:LineExtensionAmount currencyID="XUF">1720441</cbc:LineExtensionAmount>
    <cbc:TaxExclusiveAmount currencyID="XUF">1720441</cbc:TaxExclusiveAmount>
    <cbc:TaxInclusiveAmount currencyID="XUF">2064529</cbc:TaxInclusiveAmount>
    <cbc:PayableAmount currencyID="XUF">2064529</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:InvoiceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:InvoicedQuantity unitCode="TNE">1788.4</cbc:InvoicedQuantity>
    <cbc:LineExtensionAmount currencyID="XUF">1720441</cbc:LineExtensionAmount>
    <cac:Item>
      <cbc:Description>Ore from the mine siding to the factory siding, per tonne.</cbc:Description>
      <cbc:Name>Rail freight, ore in bulk wagons</cbc:Name>
      <cac:SellersItemIdentification>
        <cbc:ID>FRC-ORE</cbc:ID>
      </cac:SellersItemIdentification>
      <cac:ClassifiedTaxCategory>
        <cbc:ID>S</cbc:ID>
        <cbc:Percent>20</cbc:Percent>
        <cac:TaxScheme>
          <cbc:ID>VAT</cbc:ID>
        </cac:TaxScheme>
      </cac:ClassifiedTaxCategory>
    </cac:Item>
    <cac:Price>
      <cbc:PriceAmount currencyID="XUF">962</cbc:PriceAmount>
      <cbc:BaseQuantity unitCode="TNE">1</cbc:BaseQuantity>
    </cac:Price>
  </cac:InvoiceLine>
</Invoice>
```
