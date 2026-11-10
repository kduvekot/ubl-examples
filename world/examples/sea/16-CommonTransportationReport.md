# Common Transportation Report: Tidewell Ocean Lines to Maritime Administration of Lisavu

*Example 16 of the flow "Overseas by container ship, cost insurance and freight (Bayvarra → island Lisavu)" · [Common Transportation Report in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-COMMON-TRANSPORTATION-REPORT-SCHEMA)*

The ship flies the island's flag; before entering port the carrier reports to the maritime administration, which also issued the ship's security certificate.

[The XML file](16-CommonTransportationReport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The documents of the world use UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world**  
  The example world is a customization of UBL: it uses its own code lists for countries and currencies.
- `ID` = **TOL-CTR-26-0141**  
  The carrier's report number.
- `IssueDate` = **2026-05-16**  
  Sent before the ship enters the port of Selanu.

### Reporter Party

Inside `ReporterParty`:

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

### Authority Party

Inside `AuthorityParty`:

- `PartyIdentification/ID` = **IC42270** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Maritime Administration of Lisavu (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Maritime Administration of Lisavu**  
  The trading name; identity of Maritime Administration of Lisavu (world/parties.json).
- `PostalAddress/StreetName` = **Wharf Road**  
  Street of the postal address; identity of Maritime Administration of Lisavu (world/parties.json).
- `PostalAddress/BuildingNumber` = **37**  
  Building number of the postal address; identity of Maritime Administration of Lisavu (world/parties.json).
- `PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Maritime Administration of Lisavu (world/parties.json).
- `PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `PartyLegalEntity/RegistrationName` = **Maritime Administration of Lisavu**  
  The name under which the party is registered; identity of Maritime Administration of Lisavu (world/parties.json).
- `PartyLegalEntity/CompanyID` = **IC42270**  
  Number in the Island companies register; identity of Maritime Administration of Lisavu (world/parties.json).
- `Contact/Name` = **Ship registry**  
  The department that handles this document; identity of Maritime Administration of Lisavu (world/parties.json).
- `Contact/ElectronicMail` = **ship@maritime-xl.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Maritime Administration of Lisavu (world/parties.json).
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XL:IC42270** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Maritime Administration of Lisavu (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **IC42270** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Maritime Administration of Lisavu**  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **LD-SH-26-0132**  
  The shipment the report is for.
- `ShipmentStage/ID` = **1**  
  The sea leg to Selanu.
- `ShipmentStage/TerminalOperatorParty/PartyIdentification/ID` = **IC41037** (schemeID `urn:ubl-examples:world:XL:register`)  
  The party's preferred identifier: its number in the Island companies register; identity of Port of Selanu (world/parties.json). Later mentions of the same party in this document repeat only this identifier and the name.
- `ShipmentStage/TerminalOperatorParty/PartyName/Name` = **Port of Selanu**  
  The trading name; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/StreetName` = **Wharf Road**  
  Street of the postal address; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/BuildingNumber` = **32**  
  Building number of the postal address; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/CityName` = **Selanu**  
  The town or locality nearest to the party's place on the map, in its own country and state; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PostalAddress/Country/IdentificationCode` = **XL**  
  Lisavu: a user-assigned ISO 3166-1 code, in the world's country code list (world/codelists).
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/RegistrationName` = **Port of Selanu**  
  The name under which the party is registered; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/PartyLegalEntity/CompanyID` = **IC41037**  
  Number in the Island companies register; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/Contact/Name` = **Port control**  
  The department that handles this document; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/Contact/ElectronicMail` = **port@port-selanu.example**  
  E-mail under the reserved .example domain (RFC 2606), so it cannot reach anyone; identity of Port of Selanu (world/parties.json).
- `ShipmentStage/TerminalOperatorParty/ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ShipmentStage/TerminalOperatorParty/ElectronicAddress/ElectronicAddressID` = **XL:IC41037** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and registry number; identity of Port of Selanu (world/parties.json). UBL 2.5 carries it here; Party/EndpointID is deprecated.
- `ShipmentStage/ISPSRequirements/ID` = **ISSC-XL-2026-0117**  
  The number of the ship's International Ship Security Certificate.
- `ShipmentStage/ISPSRequirements/ValidISSCIndicator` = **true**  
  The ship holds a valid security certificate.
- `ShipmentStage/ISPSRequirements/ISSCExpiryDate` = **2028-09-30**  
  The certificate is valid for five years from its issue.
- `ShipmentStage/ISPSRequirements/CurrentOperatingSecurityLevelCode` = **1**  
  Security level 1, the normal level.
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyIdentification/ID` = **IC42270** (schemeID `urn:ubl-examples:world:XL:register`)  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyName/Name` = **Maritime Administration of Lisavu**  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CommonTransportationReport xmlns="urn:oasis:names:specification:ubl:schema:xsd:CommonTransportationReport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world</cbc:CustomizationID>
  <cbc:ID>TOL-CTR-26-0141</cbc:ID>
  <cbc:IssueDate>2026-05-16</cbc:IssueDate>
  <cac:ReporterParty>
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
  </cac:ReporterParty>
  <cac:AuthorityParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42270</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Maritime Administration of Lisavu</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:StreetName>Wharf Road</cbc:StreetName>
      <cbc:BuildingNumber>37</cbc:BuildingNumber>
      <cbc:CityName>Selanu</cbc:CityName>
      <cac:Country>
        <cbc:IdentificationCode>XL</cbc:IdentificationCode>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PartyLegalEntity>
      <cbc:RegistrationName>Maritime Administration of Lisavu</cbc:RegistrationName>
      <cbc:CompanyID>IC42270</cbc:CompanyID>
    </cac:PartyLegalEntity>
    <cac:Contact>
      <cbc:Name>Ship registry</cbc:Name>
      <cbc:ElectronicMail>ship@maritime-xl.example</cbc:ElectronicMail>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XL:IC42270</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:AuthorityParty>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42270</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Maritime Administration of Lisavu</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:Shipment>
    <cbc:ID>LD-SH-26-0132</cbc:ID>
    <cac:ShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cac:TerminalOperatorParty>
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
      </cac:TerminalOperatorParty>
      <cac:ISPSRequirements>
        <cbc:ID>ISSC-XL-2026-0117</cbc:ID>
        <cbc:ValidISSCIndicator>true</cbc:ValidISSCIndicator>
        <cbc:ISSCExpiryDate>2028-09-30</cbc:ISSCExpiryDate>
        <cbc:CurrentOperatingSecurityLevelCode>1</cbc:CurrentOperatingSecurityLevelCode>
        <cac:ISSCIssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XL:register">IC42270</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Maritime Administration of Lisavu</cbc:Name>
          </cac:PartyName>
        </cac:ISSCIssuerParty>
      </cac:ISPSRequirements>
    </cac:ShipmentStage>
  </cac:Shipment>
</CommonTransportationReport>
```
