# Document Status Request: Brightmarket Stores to Lumeway Distribution

*Example 9 of the flow "Distributor to retailer, delivered duty paid (domestic, Bayvarra)" · [Document Status Request in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-DOCUMENT-STATUS-REQUEST-SCHEMA)*

The store asks where its order stands.

[The XML file](09-DocumentStatusRequest.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5 (world/ubl-versions.json); Party/AdditionalPartyIdentification first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:order-status:1.0#compliant#urn:ubl-examples:world:community:retail:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Order status"; the community specification "Retail community". Each has a public description on the world's pages (world/specifications.json).
- `ProfileID` = **urn:ubl-examples:world:profile:ordering:1.0**  
  The Trade Accord's process profile the document belongs to: ordering, a generic, versioned profile, not the flow; the run of the process is the ProfileExecutionID.
- `ProfileExecutionID` = **RETAIL-2026-01**  
  This run of the process: the same in every document of the flow.
- `ID` = **BS-DOC-26-0225**  
  The sender's number for this document.
- `UUID` = **44994824-762c-5e0e-a7c5-0010d1f4141f**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-04-26**  
  Asked two days after ordering.
- `IssueTime` = **11:52:00**  
  The time the sender's system issued the document, in the sender's local time.
- `Note` = **Has the order been accepted?**  
  The question.
- `TrackingID` = **BS-PO-26-0224**  
  The order the store tracks.

### Requested Document Reference

Inside `RequestedDocumentReference`:

- `ID` = **BS-PO-26-0224**  
  The order asked about.
- `DocumentTypeCode` = **Order** (listID `urn:ubl-examples:world:codelist:UBLDocumentTypeCode`)  
  The kind of document referred to: BS-PO-26-0224 is the example retail/08, a Order; a generic reference names the UBL document type (decision Q29). The code is from the Trade Accord's UBL document type list: Order.

### Signature

Inside `Signature`:

- `ID` = **BM-SIG-26-DSR**  
  The sender's electronic seal.
- `SignatoryParty/PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  A party referred to from another party's details: its identifier and name are enough.
- `SignatoryParty/PartyName/Name` = **Brightmarket Stores**  
  A party referred to from another party's details: its identifier and name are enough.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20410411** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Brightmarket Stores (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9522610900002** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Brightmarket Stores (world/parties.json).
- `PartyName/Name` = **Brightmarket Stores**  
  The trading name; identity of Brightmarket Stores (world/parties.json).
- `TradePartyName/Name` = **Brightmarket**  
  The name the shops trade under, shorter than the company's name; identity of Brightmarket Stores (world/parties.json).
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party does business in. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en** (listID `ISO 639`)  
  The language as a lower-case code of the world's ISO 639 list (ISO 639). The code is from the world's copy of ISO 639 Language: en = English.
- `Contact/ID` = **BM-CT-01**  
  The desk's number in the party's own contact list.
- `Contact/Name` = **Buying office**  
  The party's main desk, which handles this document; identity of Brightmarket Stores (world/parties.json).
- `Contact/JobTitle` = **Buyer**  
  The job of the person who answers at the desk; identity of Brightmarket Stores (world/parties.json).
- `Contact/Department` = **Purchasing**  
  The department the desk belongs to; identity of Brightmarket Stores (world/parties.json).
- `Contact/Telephone` = **+999 2 38 2511 0411**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 to 5 of them (Lumeport 38, Upland State 7121, Gullhaven 38522 in the Northern Territory: the plan is national and does not follow state borders) and the trunk prefix 0 is dropped from abroad. Mobiles start with 7. identity of Brightmarket Stores (world/parties.json).
- `Contact/ElectronicMail` = **buying@brightmarket.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Brightmarket Stores (world/parties.json).
- `Contact/Note` = **Weekdays 08:00–17:00**  
  When the desk can be reached; identity of Brightmarket Stores (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410411** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Brightmarket Stores (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20410274** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeway Distribution (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `AdditionalPartyIdentification/ID` = **9520610900008** (schemeID `GS1 GLN`)  
  A further identifier, the party's Global Location Number (the endorsed PartyIdentification holds one only): it identifies itself, its items and its places the GS1 way, under its company prefix, which starts with 952, the prefix GS1 reserves for examples (decision ID-Q7); identity of Lumeway Distribution (world/parties.json).
- `PartyName/Name` = **Lumeway Distribution**  
  The trading name; identity of Lumeway Distribution (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20410274** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeway Distribution (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<DocumentStatusRequest xmlns="urn:oasis:names:specification:ubl:schema:xsd:DocumentStatusRequest-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:order-status:1.0#compliant#urn:ubl-examples:world:community:retail:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:ordering:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>RETAIL-2026-01</cbc:ProfileExecutionID>
  <cbc:ID>BS-DOC-26-0225</cbc:ID>
  <cbc:UUID>44994824-762c-5e0e-a7c5-0010d1f4141f</cbc:UUID>
  <cbc:IssueDate>2026-04-26</cbc:IssueDate>
  <cbc:IssueTime>11:52:00</cbc:IssueTime>
  <cbc:Note>Has the order been accepted?</cbc:Note>
  <cbc:TrackingID>BS-PO-26-0224</cbc:TrackingID>
  <cac:RequestedDocumentReference>
    <cbc:ID>BS-PO-26-0224</cbc:ID>
    <cbc:DocumentTypeCode listID="urn:ubl-examples:world:codelist:UBLDocumentTypeCode">Order</cbc:DocumentTypeCode>
  </cac:RequestedDocumentReference>
  <cac:Signature>
    <cbc:ID>BM-SIG-26-DSR</cbc:ID>
    <cac:SignatoryParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Brightmarket Stores</cbc:Name>
      </cac:PartyName>
    </cac:SignatoryParty>
  </cac:Signature>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20410411</cbc:ID>
    </cac:PartyIdentification>
    <cac:AdditionalPartyIdentification>
      <cbc:ID schemeID="GS1 GLN">9522610900002</cbc:ID>
    </cac:AdditionalPartyIdentification>
    <cac:PartyName>
      <cbc:Name>Brightmarket Stores</cbc:Name>
    </cac:PartyName>
    <cac:TradePartyName>
      <cbc:Name>Brightmarket</cbc:Name>
    </cac:TradePartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>
    </cac:Language>
    <cac:Contact>
      <cbc:ID>BM-CT-01</cbc:ID>
      <cbc:Name>Buying office</cbc:Name>
      <cbc:JobTitle>Buyer</cbc:JobTitle>
      <cbc:Department>Purchasing</cbc:Department>
      <cbc:Telephone>+999 2 38 2511 0411</cbc:Telephone>
      <cbc:ElectronicMail>buying@brightmarket.example</cbc:ElectronicMail>
      <cbc:Note>Weekdays 08:00–17:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410411</cbc:ElectronicAddressID>
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
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20410274</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
</DocumentStatusRequest>
```
