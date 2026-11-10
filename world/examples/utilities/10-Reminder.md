# Reminder: Coastal State Water Company to Robin Ashdale

*Example 10 of the flow "Electricity, water and telecom (one utility in each country)" · [Reminder in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-REMINDER-SCHEMA)*

The household has not paid by the due date; the utility reminds it of the amount past due, referring to the invoice.

[The XML file](10-Reminder.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **CSWC-DOC-26-0321**  
  The reminder number.
- `IssueDate` = **2026-05-01**  
  Sent a week after the due date passed without payment.
- `DocumentCurrencyCode` = **XBL**  
  The lume, the currency of the unpaid bill; it has two decimals.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **20412192** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Coastal State Water Company**  
  The trading name; identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/StreetName` = **Reservoir Road**  
  Street of the postal address; identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **51**  
  Building number of the postal address; identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/PostalZone` = **38500**  
  Postal code in Bayvarra's format (5 digits); identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Coastal State Water Company (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyTaxScheme/CompanyID` = **CO-1236576**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Coastal State Water Company (world/parties.json).
- `Party/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `Party/PartyLegalEntity/RegistrationName` = **Coastal State Water Company**  
  The name under which the party is registered; identity of Coastal State Water Company (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **20412192**  
  Number in the Federal business register of Bayvarra; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/Name` = **Customer service**  
  The department that handles this document; identity of Coastal State Water Company (world/parties.json).
- `Party/Contact/ElectronicMail` = **customer@coastalwater.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Coastal State Water Company (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XB:20412192** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Coastal State Water Company (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

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

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer, how the household is asked to pay.
- `PayeeFinancialAccount/ID` = **XB52BLUM0004189160** (schemeID `urn:ubl-examples:world:account`)  
  The utility's account, where the overdue amount is to be paid. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BLUM**  
  The bank code, the part of every account number that names the bank; identity of Bank of Lumeport (world/parties.json).
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Lumeport**  
  The bank; identity of Bank of Lumeport (world/parties.json).

### Legal Monetary Total

Inside `LegalMonetaryTotal`:

- `PayableAmount` = **32.90** (currencyID `XBL`)  
  The amount still due: the whole bill.

### Reminder Line

Inside `ReminderLine`:

- `ID` = **1**  
  The unpaid bill.
- `DebitLineAmount` = **32.90** (currencyID `XBL`)  
  The amount of the unpaid invoice.
- `BillingReference/InvoiceDocumentReference/ID` = **CSWC-INV-26-0319**  
  The invoice not paid.
- `BillingReference/InvoiceDocumentReference/IssueDate` = **2026-04-02**  
  Its issue date.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<Reminder xmlns="urn:oasis:names:specification:ubl:schema:xsd:Reminder-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>CSWC-DOC-26-0321</cbc:ID>
  <cbc:IssueDate>2026-05-01</cbc:IssueDate>
  <cbc:DocumentCurrencyCode>XBL</cbc:DocumentCurrencyCode>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412192</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Coastal State Water Company</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Reservoir Road</cbc:StreetName>
        <cbc:BuildingNumber>51</cbc:BuildingNumber>
        <cbc:CityName>Lumeport</cbc:CityName>
        <cbc:PostalZone>38500</cbc:PostalZone>
        <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
        <cac:Country>
          <cbc:IdentificationCode>XB</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyTaxScheme>
        <cbc:CompanyID>CO-1236576</cbc:CompanyID>
        <cac:TaxScheme>
          <cbc:ID>STT</cbc:ID>
        </cac:TaxScheme>
      </cac:PartyTaxScheme>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Coastal State Water Company</cbc:RegistrationName>
        <cbc:CompanyID>20412192</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Customer service</cbc:Name>
        <cbc:ElectronicMail>customer@coastalwater.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412192</cbc:ElectronicAddressID>
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
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XB52BLUM0004189160</cbc:ID>
      <cac:FinancialInstitutionBranch>
        <cac:FinancialInstitution>
          <cbc:ID>BLUM</cbc:ID>
          <cbc:Name>Bank of Lumeport</cbc:Name>
        </cac:FinancialInstitution>
      </cac:FinancialInstitutionBranch>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:LegalMonetaryTotal>
    <cbc:PayableAmount currencyID="XBL">32.90</cbc:PayableAmount>
  </cac:LegalMonetaryTotal>
  <cac:ReminderLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DebitLineAmount currencyID="XBL">32.90</cbc:DebitLineAmount>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>CSWC-INV-26-0319</cbc:ID>
        <cbc:IssueDate>2026-04-02</cbc:IssueDate>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
  </cac:ReminderLine>
</Reminder>
```
