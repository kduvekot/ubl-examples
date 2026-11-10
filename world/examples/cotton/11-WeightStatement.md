# Weight Statement: Selanu Cotton Ginnery to Tidewell Ocean Lines

*Example 11 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Weight Statement in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-WEIGHT-STATEMENT-SCHEMA)*

Before loading, the shipper declares the verified gross mass of the container, weighed on the port's weighbridge.

[The XML file](11-WeightStatement.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **SCG-WS-26-0204**  
  The shipper's weight statement number.
- `IssueDate` = **2026-03-01**  
  Declared before the container is loaded, as required for every packed container.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The trading name; identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/StreetName` = **Gin Yard Road**  
  Street of the postal address; identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/BuildingNumber` = **42**  
  Building number of the postal address; identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Selanu Cotton Ginnery (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyLegalEntity/RegistrationName` = **Selanu Cotton Ginnery**  
  The name under which the party is registered; identity of Selanu Cotton Ginnery (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC42681**  
  Number in the Island companies register; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/Name` = **Cotton sales**  
  The department that handles this document; identity of Selanu Cotton Ginnery (world/parties.json).
- `Contact/ElectronicMail` = **cotton@selanuginnery.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Selanu Cotton Ginnery (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42681** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Selanu Cotton Ginnery (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address; identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address; identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits); identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The state, part of an address in federal Bayvarra; identity of Tidewell Ocean Lines (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XB**  
  Bayvarra: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyTaxScheme/CompanyID` = **CO-1235754**  
  Tax number under Bayvarra's state sales tax (state code (UL Upland State, CO Coastal State), hyphen, 7 digits (sales tax permit of the state)); identity of Tidewell Ocean Lines (world/parties.json).
- `PartyTaxScheme/TaxScheme/ID` = **STT**  
  UN/EDIFACT 5153 code of Bayvarra's state sales tax.
- `PartyLegalEntity/RegistrationName` = **Tidewell Ocean Lines**  
  The name under which the party is registered; identity of Tidewell Ocean Lines (world/parties.json).
- `PartyLegalEntity/CompanyID` = **20411918**  
  Number in the Federal business register of Bayvarra; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/Name` = **Bookings**  
  The department that handles this document; identity of Tidewell Ocean Lines (world/parties.json).
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Tidewell Ocean Lines (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Tidewell Ocean Lines (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Weighing Party

Inside `WeighingParty`:

- `PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Port of Selanu (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Port of Selanu**  
  The trading name; identity of Port of Selanu (world/parties.json).
- `PostalAddress/StreetName` = **Wharf Road**  
  Street of the postal address; identity of Port of Selanu (world/parties.json).
- `PostalAddress/BuildingNumber` = **32**  
  Building number of the postal address; identity of Port of Selanu (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Port of Selanu (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyLegalEntity/RegistrationName` = **Port of Selanu**  
  The name under which the party is registered; identity of Port of Selanu (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC41037**  
  Number in the Island companies register; identity of Port of Selanu (world/parties.json).
- `Contact/Name` = **Port control**  
  The department that handles this document; identity of Port of Selanu (world/parties.json).
- `Contact/ElectronicMail` = **port@port-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Port of Selanu (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC41037** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Port of Selanu (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Shipper Party

Inside `ShipperParty`:

- `PartyIdentification/ID` = **IC42681** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Selanu Cotton Ginnery**  
  The same party as at SenderParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **SCG-SH-26-0199**  
  The shipment weighed.
- `TransportHandlingUnit/TransportEquipment/ID` = **TWLU4123110** (schemeID `ISO6346`)  
  The container, with its ISO 6346 check digit.
- `TransportHandlingUnit/TransportEquipment/GrossWeightMeasure` = **9940.29** (unitCode `KGM`)  
  The verified gross mass: the bales and the container's own weight, weighed on the port's weighbridge.
- `TransportHandlingUnit/TransportEquipment/TareWeightMeasure` = **3750** (unitCode `KGM`)  
  The empty container's own weight.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<WeightStatement xmlns="urn:oasis:names:specification:ubl:schema:xsd:WeightStatement-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>SCG-WS-26-0204</cbc:ID>
  <cbc:IssueDate>2026-03-01</cbc:IssueDate>
  <cac:SenderParty>
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
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>18</cbc:BuildingNumber>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38527</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cac:Country>
        <cbc:IdentificationCode>XB</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyTaxScheme>
      <cbc:CompanyID>CO-1235754</cbc:CompanyID>
      <cac:TaxScheme>
        <cbc:ID>STT</cbc:ID>
      </cac:TaxScheme>
    </cac:PartyTaxScheme>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Tidewell Ocean Lines</cbc:RegistrationName>
      <cbc:CompanyID>20411918</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Bookings</cbc:Name>
      <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReceiverParty>
  <cac:WeighingParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC41037</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Port of Selanu</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>32</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Port of Selanu</cbc:RegistrationName>
      <cbc:CompanyID>IC41037</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Port control</cbc:Name>
      <cbc:ElectronicMail>port@port-selanu.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC41037</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:WeighingParty>
  <cac:ShipperParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42681</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Selanu Cotton Ginnery</cbc:Name>
    </cac:PartyName>
  </cac:ShipperParty>
  <cac:Shipment>
    <cbc:ID>SCG-SH-26-0199</cbc:ID>
    <cac:TransportHandlingUnit>
      <cac:TransportEquipment>
        <cbc:ID schemeID="ISO6346">TWLU4123110</cbc:ID>
        <cbc:GrossWeightMeasure unitCode="KGM">9940.29</cbc:GrossWeightMeasure>
        <cbc:TareWeightMeasure unitCode="KGM">3750</cbc:TareWeightMeasure>
      </cac:TransportEquipment>
    </cac:TransportHandlingUnit>
  </cac:Shipment>
</WeightStatement>
```
