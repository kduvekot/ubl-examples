# Invoice Status Response: Velumi Trading to Lumeway Distribution

*Example 24 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Invoice Status Response in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-INVOICE-STATUS-RESPONSE-SCHEMA)*

The buyer answers: accepted and scheduled for payment.

[The XML file](24-InvoiceStatusResponse.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); the document type InvoiceStatusResponse first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:invoice-status:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Invoice status". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:billing:1.0**  
  The Trade Accord's process profile the document belongs to: billing, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **SEA-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **VT-DOC-26-0149**  
  The sender's number for this document.
- `UUID` = **46a32b33-e5ba-5fe5-96d0-d30eada68245**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-30**  
  Answered the next day.
- `IssueTime` = **13:49:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Approved; the balance will be paid to the factor.**  
  The answer.
- `VersionID` = **1**  
  The first answer.

### Signature

Inside `Signature`:

- `ID` = **VT-SIG-26-ISP**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Velumi Trading**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **IC41859** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Velumi Trading (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Velumi Trading**  
  The trading name; identity of Velumi Trading (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document: documents between the countries of the Trade Accord are in English (O19). The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XL** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Lisavu, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XL = Lisavan English.
- `Contact/Name` = **Accounts payable**  
  The party's accounts payable desk: the desk for its role in this document (it pays); identity of Velumi Trading (world/parties.json).
- `Contact/JobTitle` = **Accounts payable clerk**  
  The job of the person who answers at the desk; identity of Velumi Trading (world/parties.json).
- `Contact/Department` = **Finance**  
  The department the desk belongs to; identity of Velumi Trading (world/parties.json).
- `Contact/Telephone` = **+999 3 729 1859**  
  The party's switchboard, which puts the caller through to the desk. Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Lisavu's own plan: A small island: 7-digit numbers without area codes; fixed lines start with 72, mobiles with 77, ships with 79. identity of Velumi Trading (world/parties.json).
- `Contact/ElectronicMail` = **payables@velumi.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Velumi Trading (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Velumi Trading (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41859** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Velumi Trading (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which (decision D1). The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Payment

Inside `Payment`:

- `ID` = **VT-PAY-26-0199**  
  The payment planned.
- `PaidAmount` = **43778.00** (currencyID `XBL`)  
  The balance to be paid.
- `PaidDate` = **2026-06-25**  
  The planned payment day.
- `InstructionID` = **VT-PAY-26-0199**  
  The buyer's payment order.
- `BillingReference/InvoiceDocumentReference/ID` = **LD-INV-26-0147**  
  The invoice.
- `RemittanceDocumentReference/ID` = **VT-RM-26-0150**  
  The remittance advice the buyer prepared with the payment order; it is sent on the payment day.

### Document Response

Inside `DocumentResponse`:

- `Response/ResponseCode` = **AP** (listID `UN/EDIFACT EDED 4343`)  
  UN/EDIFACT 4343 code AP: accepted; the invoice is scheduled for payment. The code is from the world's copy of UN/EDIFACT 4343 Response type: AP = Accepted.
- `DocumentReference/ID` = **LD-INV-26-0147**  
  The invoice the status is about.
- `DocumentReference/DocumentTypeCode` = **Invoice** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: LD-INV-26-0147 is the example sea/22, a Invoice; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Invoice.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<InvoiceStatusResponse xmlns="urn:oasis:names:specification:ubl:schema:xsd:InvoiceStatusResponse-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:invoice-status:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:billing:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>SEA-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>VT-DOC-26-0149</cbc:ID>
  <cbc:UUID>46a32b33-e5ba-5fe5-96d0-d30eada68245</cbc:UUID>
  <cbc:IssueDate>2026-05-30</cbc:IssueDate>
  <cbc:IssueTime>13:49:00</cbc:IssueTime>
  <cbc:Note>Approved; the balance will be paid to the factor.</cbc:Note>
  <cbc:VersionID>1</cbc:VersionID>
  <cac:Signature>
    <cbc:ID>VT-SIG-26-ISP</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Velumi Trading</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41859</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Velumi Trading</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XL</cbc:LocaleCode>
    </cac:Language>
    <cac:Contact>
      <cbc:Name>Accounts payable</cbc:Name>
      <cbc:JobTitle>Accounts payable clerk</cbc:JobTitle>
      <cbc:Department>Finance</cbc:Department>
      <cbc:Telephone>+999 3 729 1859</cbc:Telephone>
      <cbc:ElectronicMail>payables@velumi.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41859</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410274</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9520610900008</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeway Distribution</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:Payment>
    <cbc:ID>VT-PAY-26-0199</cbc:ID>
    <cbc:PaidAmount currencyID="XBL">43778.00</cbc:PaidAmount>
    <cbc:PaidDate>2026-06-25</cbc:PaidDate>
    <cbc:InstructionID>VT-PAY-26-0199</cbc:InstructionID>
    <cac:BillingReference>
      <cac:InvoiceDocumentReference>
        <cbc:ID>LD-INV-26-0147</cbc:ID>
      </cac:InvoiceDocumentReference>
    </cac:BillingReference>
    <cac:RemittanceDocumentReference>
      <cbc:ID>VT-RM-26-0150</cbc:ID>
    </cac:RemittanceDocumentReference>
  </cac:Payment>
  <cac:DocumentResponse>
    <cac:Response>
      <cbc:ResponseCode listID="UN/EDIFACT EDED 4343">AP</cbc:ResponseCode>
    </cac:Response>
    <cac:DocumentReference>
      <cbc:ID>LD-INV-26-0147</cbc:ID>
      <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Invoice</cbc:DocumentTypeCode>
    </cac:DocumentReference>
  </cac:DocumentResponse>
</InvoiceStatusResponse>
```
