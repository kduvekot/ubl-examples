# Transportation Status: Lumeport Airport Cargo Terminal to Kelaro Air Cargo

*Example 7 of the flow "An urgent part of the order by air (Bayvarra → island Lisavu)" · [Transportation Status in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-TRANSPORTATION-STATUS-SCHEMA)*

The air cargo terminal reports the cargo accepted and built up for the flight.

[The XML file](07-TransportationStatus.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **LACT-TS-26-0328**  
  The sender's status report number.
- `IssueDate` = **2026-05-13**  
  Reported when the cargo is built up for the flight.

### Consignment

Inside `Consignment`:

- `ID` = **LD-CS-26-0326**  
  The consignment the report is about.
- `CarrierParty/PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `CarrierParty/PartyName/Name` = **Kelaro Air Cargo**  
  The trading name; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/StreetName` = **Airfield Road**  
  Street of the postal address; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/BuildingNumber` = **46**  
  Building number of the postal address; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `CarrierParty/PartyLegalEntity/RegistrationName` = **Kelaro Air Cargo**  
  The name under which the party is registered; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/PartyLegalEntity/CompanyID` = **IC41311**  
  Number in the Island companies register; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Contact/Name` = **Cargo sales**  
  The department that handles this document; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/Contact/ElectronicMail` = **cargo@kelaro.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Kelaro Air Cargo (world/parties.json).
- `CarrierParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `CarrierParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41311** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Kelaro Air Cargo (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `MainCarriageShipmentStage/ID` = **1**  
  The flight.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **20412055** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Lumeport Airport Cargo Terminal (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyName/Name` = **Lumeport Airport Cargo Terminal**  
  The trading name; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Airport Road**  
  Street of the postal address; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **25**  
  Building number of the postal address; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/PostalZone` = **38528**  
  Postal code in Bayvarra's format (5 digits); identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/CompanyID` = **CO-1236165**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Lumeport Airport Cargo Terminal**  
  The name under which the party is registered; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **20412055**  
  Number in the Federal business register of Bayvarra; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/Name` = **Cargo acceptance**  
  The department that handles this document; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **cargo@lumeport-cargo.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Lumeport Airport Cargo Terminal (world/parties.json).
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `MainCarriageShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XB:20412055** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Lumeport Airport Cargo Terminal (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Transport Event

Inside `TransportEvent`:

- `OccurrenceDate` = **2026-05-13**  
  The day the event took place.
- `Description` = **Cargo accepted and built up for the flight.**  
  What happened, in words.
- `Location/Name` = **Lumeport airport, cargo terminal**  
  Where it happened.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20412055** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Lumeport Airport Cargo Terminal**  
  The same party as at Consignment/MainCarriageShipmentStage/TerminalOperatorParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **IC41311** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Kelaro Air Cargo**  
  The same party as at Consignment/CarrierParty, where its full details are given; only its identifier and name are repeated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<TransportationStatus xmlns="urn:oasis:names:specification:ubl:schema:xsd:TransportationStatus-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>LACT-TS-26-0328</cbc:ID>
  <cbc:IssueDate>2026-05-13</cbc:IssueDate>
  <cac:Consignment>
    <cbc:ID>LD-CS-26-0326</cbc:ID>
    <cac:CarrierParty>
      <cac:PartyIdentification>
        <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
      </cac:PartyIdentification>
      <cac:PartyName>
        <cbc:Name>Kelaro Air Cargo</cbc:Name>
      </cac:PartyName>
      <cac:PostalAddress>
        <cbc:StreetName>Airfield Road</cbc:StreetName>
        <cbc:BuildingNumber>46</cbc:BuildingNumber>
        <cbc:CityName>Selanu</cbc:CityName>
        <cac:Country>
          <cbc:IdentificationCode>XL</cbc:IdentificationCode>
        </cac:Country>
      </cac:PostalAddress>
      <cac:PartyLegalEntity>
        <cbc:RegistrationName>Kelaro Air Cargo</cbc:RegistrationName>
        <cbc:CompanyID>IC41311</cbc:CompanyID>
      </cac:PartyLegalEntity>
      <cac:Contact>
        <cbc:Name>Cargo sales</cbc:Name>
        <cbc:ElectronicMail>cargo@kelaro.example</cbc:ElectronicMail>
      </cac:Contact>
      <cac:ElectronicAddress>
        <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
        <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41311</cbc:ElectronicAddressID>
      </cac:ElectronicAddress>
    </cac:CarrierParty>
    <cac:MainCarriageShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cac:TerminalOperatorParty>
        <cac:PartyIdentification>
          <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412055</cbc:ID>
        </cac:PartyIdentification>
        <cac:PartyName>
          <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
        </cac:PartyName>
        <cac:PostalAddress>
          <cbc:StreetName>Airport Road</cbc:StreetName>
          <cbc:BuildingNumber>25</cbc:BuildingNumber>
          <cbc:CityName>Lumeport</cbc:CityName>
          <cbc:PostalZone>38528</cbc:PostalZone>
          <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
          <cac:Country>
            <cbc:IdentificationCode>XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:PostalAddress>
        <cac:PartyTaxScheme>
          <cbc:CompanyID>CO-1236165</cbc:CompanyID>
          <cac:TaxScheme>
            <cbc:ID>STT</cbc:ID>
          </cac:TaxScheme>
        </cac:PartyTaxScheme>
        <cac:PartyLegalEntity>
          <cbc:RegistrationName>Lumeport Airport Cargo Terminal</cbc:RegistrationName>
          <cbc:CompanyID>20412055</cbc:CompanyID>
        </cac:PartyLegalEntity>
        <cac:Contact>
          <cbc:Name>Cargo acceptance</cbc:Name>
          <cbc:ElectronicMail>cargo@lumeport-cargo.example</cbc:ElectronicMail>
        </cac:Contact>
        <cac:ElectronicAddress>
          <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
          <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20412055</cbc:ElectronicAddressID>
        </cac:ElectronicAddress>
      </cac:TerminalOperatorParty>
    </cac:MainCarriageShipmentStage>
  </cac:Consignment>
  <cac:TransportEvent>
    <cbc:OccurrenceDate>2026-05-13</cbc:OccurrenceDate>
    <cbc:Description>Cargo accepted and built up for the flight.</cbc:Description>
    <cac:Location>
      <cbc:Name>Lumeport airport, cargo terminal</cbc:Name>
    </cac:Location>
  </cac:TransportEvent>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20412055</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Lumeport Airport Cargo Terminal</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41311</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Kelaro Air Cargo</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
</TransportationStatus>
```
