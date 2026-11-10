# Remittance Advice: Selanu Cotton Ginnery to Lisavu Cotton Farm

*Example 5 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Remittance Advice in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-REMITTANCE-ADVICE-SCHEMA)*

The ginnery pays the farm the net amount.

[The XML file](05-RemittanceAdvice.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **SCG-RM-26-0195**  
  The ginnery's remittance number.
- `IssueDate` = **2026-02-16**  
  The ginnery pays the farm after classing.
- `DocumentCurrencyCode` = **XLC**  
  The coral, the island's currency; it has three decimals.
- `TotalPaymentAmount` = **3993.000** (currencyID `XLC`)  
  The invoice minus the credit note.

### Accounting Customer Party

Inside `AccountingCustomerParty`:

- `Party/PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/StreetName` = **Gin Yard Road**  
  Street of the postal address; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyLegalEntity/RegistrationName` = **Selanu Cotton Ginnery**  
  The name under which the party is registered; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42681**  
  Number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/Name` = **Cotton sales**  
  The department that handles this document; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/Contact/ElectronicMail` = **cotton@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Cotton Ginnery (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Cotton Ginnery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Accounting Supplier Party

Inside `AccountingSupplierParty`:

- `Party/PartyIdentification/ID` = **IC42544** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Lisavu Cotton Farm (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `Party/PartyName/Name` = **Lisavu Cotton Farm**  
  The trading name; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/StreetName` = **Plantation Road**  
  Street of the postal address; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/BuildingNumber` = **35**  
  Building number of the postal address; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `Party/PartyLegalEntity/RegistrationName` = **Lisavu Cotton Farm**  
  The name under which the party is registered; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/PartyLegalEntity/CompanyID` = **IC42544**  
  Number in the Island companies register; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/Name` = **Farm office**  
  The department that handles this document; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/Contact/ElectronicMail` = **farm@lisavufarm.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lisavu Cotton Farm (world/parties.json).
- `Party/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `Party/ElectronicAddress/ElectronicAddressID` = **XL:IC42544** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lisavu Cotton Farm (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payment Means

Inside `PaymentMeans`:

- `PaymentMeansCode` = **30** (listID `UN/EDIFACT EDED 4461`)  
  UN/EDIFACT 4461 code 30: credit transfer.
- `PayerFinancialAccount/ID` = **XL66BSEL0004922263** (schemeID `urn:ubl-examples:world:account`)  
  The ginnery's account. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BSEL**  
  The bank code, the part of every account number that names the bank; identity of Bank of Selanu (world/parties.json).
- `PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/Name` = **Bank of Selanu**  
  The bank; identity of Bank of Selanu (world/parties.json).
- `PayeeFinancialAccount/ID` = **XL05BSEL0004817534** (schemeID `urn:ubl-examples:world:account`)  
  The farm's account. The number follows the structure of ISO 13616 with its check digits, with the world's country code; it is not called an IBAN, because the world's countries are not registered IBAN countries.
- `PayeeFinancialAccount/FinancialInstitutionBranch/FinancialInstitution/ID` = **BSEL**  
  The same bank as at PaymentMeans/PayerFinancialAccount/FinancialInstitutionBranch/FinancialInstitution, where its name is given; only its code is repeated.

### Remittance Advice Line

Inside `RemittanceAdviceLine`:

- `ID` = **1**  
  The self-billed invoice.
- `DebitLineAmount` = **4068.000** (currencyID `XLC`)  
  The amount of the self-billed invoice.
- `BillingReference/SelfBilledInvoiceDocumentReference/ID` = **SCG-SBI-26-0193**  
  The self-billed invoice paid.
- `ID` = **2**  
  The self-billed credit note.
- `CreditLineAmount` = **75.000** (currencyID `XLC`)  
  The amount credited, deducted from the payment.
- `BillingReference/SelfBilledCreditNoteDocumentReference/ID` = **SCG-SBC-26-0194**  
  The self-billed credit note set off.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<RemittanceAdvice xmlns="urn:oasis:names:specification:ubl:schema:xsd:RemittanceAdvice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>SCG-RM-26-0195</cbc:ID>
  <cbc:IssueDate>2026-02-16</cbc:IssueDate>
  <cbc:DocumentCurrencyCode>XLC</cbc:DocumentCurrencyCode>
  <cbc:TotalPaymentAmount currencyID="XLC">3993.000</cbc:TotalPaymentAmount>
  <cac:AccountingCustomerParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Gin Yard Road</cbc:StreetName>
        <cbc:BuildingNumber>42</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Selanu Cotton Ginnery</cbc:RegistrationName>
        <cbc:CompanyID>IC42681</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Cotton sales</cbc:Name>
        <cbc:ElectronicMail>cotton@selanuginnery.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42681</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingCustomerParty>
  <cac:AccountingSupplierParty>
    <cac:Party>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42544</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Lisavu Cotton Farm</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Plantation Road</cbc:StreetName>
        <cbc:BuildingNumber>35</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Lisavu Cotton Farm</cbc:RegistrationName>
        <cbc:CompanyID>IC42544</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Farm office</cbc:Name>
        <cbc:ElectronicMail>farm@lisavufarm.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42544</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:Party>
  </cac:AccountingSupplierParty>
  <cac:PaymentMeans>
    <cbc:PaymentMeansCode listID="UN/EDIFACT EDED 4461">30</cbc:PaymentMeansCode>
    <cac:PayerFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XL66BSEL0004922263</cbc:ID>
      <cac:FinancialInstitutionBranch>
        <cac:FinancialInstitution>
          <cbc:ID>BSEL</cbc:ID>
          <cbc:Name>Bank of Selanu</cbc:Name>
        </cac:FinancialInstitution>
      </cac:FinancialInstitutionBranch>
    </cac:PayerFinancialAccount>
    <cac:PayeeFinancialAccount>
      <cbc:ID schemeID="urn:ubl-examples:world:account">XL05BSEL0004817534</cbc:ID>
      <cac:FinancialInstitutionBranch>
        <cac:FinancialInstitution>
          <cbc:ID>BSEL</cbc:ID>
        </cac:FinancialInstitution>
      </cac:FinancialInstitutionBranch>
    </cac:PayeeFinancialAccount>
  </cac:PaymentMeans>
  <cac:RemittanceAdviceLine>
    <cbc:ID>1</cbc:ID>
    <cbc:DebitLineAmount currencyID="XLC">4068.000</cbc:DebitLineAmount>
    <cac:BillingReference>
      <cac:SelfBilledInvoiceDocumentReference>
        <cbc:ID>SCG-SBI-26-0193</cbc:ID>
      </cac:SelfBilledInvoiceDocumentReference>
    </cac:BillingReference>
  </cac:RemittanceAdviceLine>
  <cac:RemittanceAdviceLine>
    <cbc:ID>2</cbc:ID>
    <cbc:CreditLineAmount currencyID="XLC">75.000</cbc:CreditLineAmount>
    <cac:BillingReference>
      <cac:SelfBilledCreditNoteDocumentReference>
        <cbc:ID>SCG-SBC-26-0194</cbc:ID>
      </cac:SelfBilledCreditNoteDocumentReference>
    </cac:BillingReference>
  </cac:RemittanceAdviceLine>
</RemittanceAdvice>
```
