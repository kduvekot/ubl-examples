# Statement: Harbourline Factoring to Velumi Trading

*Example 20 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-STATEMENT-SCHEMA)*

The factor, who now owns the receivables, sends the statement of account on behalf of the distributor.

[The XML file](20-Statement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **HF-ST-26-0145**  
  The factor's statement number.
- `IssueDate` = **2026-06-13**  
  The monthly statement of account.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the currency of the invoices; it has two decimals.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/StreetName` = **Distribution Drive**  
  Street of the postal address; identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **43**  
  Building number of the postal address; identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CityName` = **Marrowdale**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/PostalZone` = **71214**  
  Postal code in Bayvarra's format (5 digits); identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Upland State**  
  The state, part of an address in federal Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **UL-1230822**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeway Distribution (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyLegalEntity/RegistrationName` = **Lumeway Distribution**  
  The name under which the party is registered; identity of Lumeway Distribution (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20410274**  
  Number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/Name` = **Customer service**  
  The department that handles this document; identity of Lumeway Distribution (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@lumeway.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeway Distribution (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

### Payee Party

Inside `PayeeParty`:

- `PartyIdentification/ID` = **20411233** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Harbourline Factoring (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Harbourline Factoring**  
  The trading name; identity of Harbourline Factoring (world/parties.json).
- `PostalAddress/StreetName` = **Exchange Street**  
  Street of the postal address; identity of Harbourline Factoring (world/parties.json).
- `PostalAddress/BuildingNumber` = **41**  
  Building number of the postal address; identity of Harbourline Factoring (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Harbourline Factoring (world/parties.json).
- `PostalAddress/PostalZone` = **38522**  
  Postal code in Bayvarra's format (5 digits); identity of Harbourline Factoring (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Harbourline Factoring (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **CO-1233699**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Harbourline Factoring (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyLegalEntity/RegistrationName` = **Harbourline Factoring**  
  The name under which the party is registered; identity of Harbourline Factoring (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411233**  
  Number in the Federal business register of Bayvarra; identity of Harbourline Factoring (world/parties.json).
- `Contact/Name` = **Client accounts**  
  The department that handles this document; identity of Harbourline Factoring (world/parties.json).
- `Contact/ElectronicMail` = **client@harbourline.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Harbourline Factoring (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411233** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Harbourline Factoring (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Statement Line

Inside `StatementLine`:

- `ID` = **1**  
  The open invoice.
- `DebitLineAmount` = **53778.00** (currencyID `XBL`)  
  The amount of the invoice, owed to the factor.
- `BalanceAmount` = **53778.00** (currencyID `XBL`)  
  Still open: nothing paid yet.
- `BillingReference/InvoiceDocumentReference/ID` = **LD-INV-26-0144**  
  The distributor's invoice, which the factor bought.
- `BillingReference/InvoiceDocumentReference/IssueDate` = **2026-05-14**  
  Its issue date.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Statement xmlns="urn:oasis:names:specification:ubl:schema:xsd:Statement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>HF-ST-26-0145</cbc:ID>
  <cbc:IssueDate>2026-06-13</cbc:IssueDate>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lumeway Distribution</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Distribution Drive</cbc:StreetName>
        <cbc:BuildingNumber>43</cbc:BuildingNumber>
        <cbc:CityName>Marrowdale</cbc:CityName>
        <cbc:PostalZone>71214</cbc:PostalZone>
        <cbc:CountrySubentity>Upland State</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>UL-1230822</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lumeway Distribution</cbc:RegistrationName>
        <cbc:CompanyID>20410274</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Customer service</cbc:Name>
        <cbc:ElectronicMail>customer@lumeway.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
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
  <cac:PayeeParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411233</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Harbourline Factoring</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Exchange Street</cbc:StreetName>
      <cbc:BuildingNumber>41</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38522</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>CO-1233699</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Harbourline Factoring</cbc:RegistrationName>
      <cbc:CompanyID>20411233</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Client accounts</cbc:Name>
      <cbc:ElectronicMail>client@harbourline.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411233</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:PayeeParty>
  <cac:StatementLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DebitLineAmount currencyID="XBL">53778.00</cbc:DebitLineAmount>
    <cbc:BalanceAmount currencyID="XBL">53778.00</cbc:BalanceAmount>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>LD-INV-26-0144</cbc:ID>
        <cbc:IssueDate>2026-05-14</cbc:IssueDate>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
  </cac:StatementLine>
</Statement>
```
